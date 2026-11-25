"""IT 2026-11-25 (IT23): applies the blind-checked wording of edits_it23.py to card packets (cards are rebuilt by repurposing_bridge.py afterwards)
and to the three investigation files. Text-level and idempotent. Run from the repository root. Hypothesis level; nothing here is medical advice.
Card text may not carry a number with a concentration unit (check_cards.py), so 'N uM' is written 'N micromolar' and 'N mM' 'N millimolar' in cards only."""
import importlib.util, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = Path("disease-models/wwox/research/drug_repurposing")
spec = importlib.util.spec_from_file_location("edits_it23", HERE / "edits_it23.py")
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
M = "[IT 2026-11-25, ADV-281: "
EXTRA = [  # M01 stale 'supplement not available' statements (held since 2026-11-21, File010)
    ("M01_neurogenic_output_myc_window", "replace", "the supplementary figures of the main paper are not available locally;",
     "the supplementary figures of the main paper were not available locally when this was written (held since 2026-11-21, File010; Supplementary Fig 7F and 7G viewed on 2026-11-25);"),
    ("M01_neurogenic_output_myc_window", "replace", "(no wild-type-plus-compound arm, supplement unavailable)",
     "(no wild-type-plus-compound arm; the supplement was unavailable when this was written and has been held since 2026-11-21)"),
    ("M01_neurogenic_output_myc_window", "replace", "The supplementary figures of PMID 42397075 were not available.",
     "The supplementary figures of PMID 42397075 were not available. [IT 2026-11-25: held since 2026-11-21 (File010); Supplementary Fig 7F and 7G viewed on 2026-11-25, ADV-281.]"),
]
def j(s): return json.dumps(s, ensure_ascii=False)[1:-1]
def units(s):
    s = re.sub(r"(\d)\s?(?:uM|µM)\b", r"\1 micromolar", s)
    s = re.sub(r"(\d)\s?mM\b", r"\1 millimolar", s)
    s = re.sub(r"(\d)\s?mg/dL\b", r"\1 milligrams per decilitre", s)
    return re.sub(r"(\d)\s?nm\b", r"\1 nanometres", s)
def string_end(raw, i):
    k = i
    while True:
        k = raw.index('"', k)
        n = 0
        while raw[k - 1 - n] == "\\": n += 1
        if n % 2 == 0: return k
        k += 1
def apply_one(raw, mode, old, new, tag):
    o, nw = j(old), j(new)
    if nw in raw and (mode != "replace" or o not in raw or o in nw and raw.count(nw) >= raw.count(o)): return raw, 0
    if o not in raw: raise SystemExit(f"NO MATCH {tag}")
    if mode == "replace": return raw.replace(o, nw), raw.count(o)
    out, pos, n = [], 0, 0
    while True:
        i = raw.find(o, pos)
        if i < 0: break
        k = i + len(o) if mode == "after" else string_end(raw, i + len(o))
        out.append(raw[pos:k]); out.append(nw); pos = k; n += 1
    out.append(raw[pos:]); return "".join(out), n
def cards():
    by = {}
    for x in E.EDITS: by.setdefault(x["card"], []).append((x["mode"], x["old"], units(x["new"]), x["id"]))
    for c, m, o, n in EXTRA: by.setdefault(c, []).append((m, o, n, "M01-stale"))
    tot = 0
    for c, items in by.items():
        p = DR / f"cards/{c}.packet.json"; raw = p.read_text(encoding="utf-8"); before = raw
        for mode, old, new, tag in items:
            raw, n = apply_one(raw, mode, old, new, tag); tot += n
        json.loads(raw)
        if raw != before: p.write_text(raw, encoding="utf-8")
    return tot
def inv_tsv(p):
    t = p.read_text(encoding="utf-8"); L = t.split("\n"); h = L[0].split("\t"); c = h.index("evidence_available"); k = h.index("inv_id"); n = 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[k] in E.INV and E.INV[f[k]].strip() not in f[c]:
            f[c] = f[c].rstrip() + E.INV[f[k]]; L[i] = "\t".join(f); n += 1
    p.write_text("\n".join(L), encoding="utf-8"); return n
def inv_json(p):
    raw = p.read_text(encoding="utf-8"); d = json.loads(raw); n = 0
    for x in [y for k in ("investigations", "further_investigations", "conditional_hypotheses") for y in d.get(k, [])]:
        if x.get("inv_id") in E.INV and E.INV[x["inv_id"]].strip() not in x["evidence_available"]:
            old = j(x["evidence_available"]); assert raw.count(old) == 1, x["inv_id"]
            raw = raw.replace(old, old + j(E.INV[x["inv_id"]])); n += 1
    json.loads(raw); p.write_text(raw, encoding="utf-8"); return n
if __name__ == "__main__":
    RK = DR / "ranking_it8_p9_20261029"
    print("card edits", cards(), "tsv", inv_tsv(RK / "investigations.tsv"), inv_tsv(RK / "investigations_it20.tsv"), "json", inv_json(RK / "ranking.json"))
