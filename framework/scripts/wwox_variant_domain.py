#!/usr/bin/env python3
"""Map WWOX protein-level variants to UniProt domain classes (a position join, never a reading of assays).

    python3 framework/scripts/wwox_variant_domain.py --table TSV [--variant-col NAME] [--id-col NAME] --out FILE [--uniprot-json FILE]
    python3 framework/scripts/wwox_variant_domain.py --help

Classes are those fixed in `variant_domain_map/CLASSES_FIXED_BEFORE_THE_JOIN.md` (WW1 16-49, WW2 57-90, linker_1 50-56, linker_2 91-124, SDR_catalytic_region 125-414, N_terminal_disordered 1-15). Variant types are separate rows
(missense, nonsense, frameshift, in_frame_deletion, in_frame_insertion, indel, start_loss, splice_no_protein_position, synonymous, unparsed); an in-frame deletion is never a missense; an unrecognised string is kept verbatim as `unparsed`.
Sub-flags (binding site, active site, mitochondrial targeting, NLS, phosphosites, UniProt features at the same position, the P47T model-line mark) are separate columns. Not medical advice.
"""
import argparse, csv, json, re, sys
from pathlib import Path

CLASSES = [("N_terminal_disordered", 1, 15), ("WW1", 16, 49), ("linker_1", 50, 56), ("WW2", 57, 90), ("linker_2", 91, 124), ("SDR_catalytic_region", 125, 414)]
SUBFLAGS = [("NAD(P)_binding_131-137", 131, 137), ("binding_site_260", 260, 260), ("active_site_293", 293, 293), ("mito_targeting_209-273", 209, 273), ("NLS_50-55", 50, 55),
            ("phosphosite_12", 12, 12), ("phosphosite_14", 14, 14), ("phosphosite_33", 33, 33), ("phosphosite_287", 287, 287)]
LENGTH = 414
AA3 = {"Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E", "Gly": "G", "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F", "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V", "Ter": "*", "Sec": "U"}
AAX = "ACDEFGHIKLMNPQRSTVWY"
MODEL_LINES = {("P", 47, "T"): "P47T knock-in line (GSE215425)"}


def aa(tok: str) -> str | None:
    tok = tok.strip()
    if tok in AA3: return AA3[tok]
    if len(tok) == 1 and (tok in AAX or tok in "*X"): return tok
    return None


def classes_of(a: int, b: int) -> list[str]:
    if a < 1 or b > LENGTH: return ["outside_protein"] if (b < 1 or a > LENGTH) else [c for c, s, e in CLASSES if not (b < s or a > e)] + ["partly_outside_protein"]
    return [c for c, s, e in CLASSES if not (b < s or a > e)]


def parse(h: str) -> dict:
    raw = (h or "").strip(); s = raw.replace("p.(", "p.").rstrip(")").replace("(", "").replace(")", "")
    if not s: return {"type": "unparsed", "raw": raw}
    if re.match(r"^c\.", s) and re.search(r"[+-]\d+", s) and "p." not in s: return {"type": "splice_no_protein_position", "raw": raw}
    m = re.match(r"^p\.([A-Za-z]{1,3})(\d+)(?:_([A-Za-z]{1,3})(\d+))?(.*)$", s)
    if not m: return {"type": "unparsed", "raw": raw}
    a1, p1, a2, p2, rest = m.group(1), int(m.group(2)), m.group(3), m.group(4), m.group(5)
    p2 = int(p2) if p2 else p1
    if rest.startswith("fs"): return {"type": "frameshift", "start": p1, "end": p1, "raw": raw}
    if rest.startswith("delins") or (rest.startswith("del") and rest[3:]): return {"type": "indel", "start": p1, "end": p2, "raw": raw}
    if rest.startswith("del"): return {"type": "in_frame_deletion", "start": p1, "end": p2, "raw": raw}
    if rest.startswith("ins") or rest.startswith("dup"): return {"type": "in_frame_insertion", "start": p1, "end": p2, "raw": raw}
    ref = aa(a1); alt = aa(rest) if rest else None
    if rest in ("=", ""): return {"type": "synonymous", "start": p1, "end": p1, "raw": raw} if rest == "=" else {"type": "unparsed", "raw": raw}
    if ref is None or alt is None: return {"type": "unparsed", "raw": raw}
    if alt == "*": return {"type": "nonsense", "start": p1, "end": p1, "ref": ref, "raw": raw}
    if p1 == 1 and ref == "M": return {"type": "start_loss", "start": 1, "end": 1, "ref": ref, "alt": alt, "raw": raw}
    return {"type": "missense", "start": p1, "end": p1, "ref": ref, "alt": alt, "raw": raw}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--table"); ap.add_argument("--variant-col", default="hgvs_p"); ap.add_argument("--id-col", default="child_id"); ap.add_argument("--out"); ap.add_argument("--uniprot-json")
    a = ap.parse_args()
    if not (a.table and a.out):
        ap.print_help(); return
    feats = {}
    if a.uniprot_json:
        for f in json.load(open(a.uniprot_json))["features"]:
            if f["type"] in ("Natural variant", "Mutagenesis"):
                for pos in range(f["location"]["start"]["value"], f["location"]["end"]["value"] + 1):
                    feats.setdefault(pos, []).append(f"{f['type']}: {f.get('description', '')[:60]}")
    rows = list(csv.DictReader(open(a.table, encoding="utf-8", newline=""), delimiter="\t"))
    if rows and a.variant_col not in rows[0]: sys.exit(f"REFUSED: the table has no column {a.variant_col!r} (columns: {', '.join(rows[0])}); pass --variant-col")
    out = []
    for r in rows:
        v = parse(r[a.variant_col]); t = v["type"]
        base = {"child_id": r.get(a.id_col, ""), "hgvs_input": r[a.variant_col], "variant_type": t}
        if t in ("unparsed", "splice_no_protein_position"):
            out.append({**base, "start": "", "end": "", "class": t, "spans_classes": "", "subflags": "", "uniprot_features_at_position": "", "model_line_mark": ""}); continue
        cl = classes_of(v["start"], v["end"])
        subs = [n for n, s, e in SUBFLAGS if not (v["end"] < s or v["start"] > e)]
        uf = sorted({x for pos in range(v["start"], v["end"] + 1) for x in feats.get(pos, [])})
        mark = MODEL_LINES.get((v.get("ref"), v["start"], v.get("alt")), "") if t == "missense" else ""
        if t == "frameshift": cl = cl + [("downstream_lost: " + ", ".join(c for c, s, e in CLASSES if s > v["start"] and c.startswith(("WW2", "SDR", "linker_2")) ) or "downstream_lost: none")]
        if t == "nonsense": cl = cl + ["downstream_lost: " + (", ".join(c for c, s, e in CLASSES if s > v["start"]) or f"residues {v['start'] + 1}-{LENGTH} of {cl[0]}")]
        out.append({**base, "start": v["start"], "end": v["end"], "class": cl[0], "spans_classes": ";".join(cl[1:]) if len(cl) > 1 else "", "subflags": ";".join(subs), "uniprot_features_at_position": " | ".join(uf), "model_line_mark": ("same_variant_as_model_line: " + mark) if mark else ""})
    cols = list(out[0]) if out else ["child_id"]
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
    counts = {}
    for o in out: counts[(o["variant_type"], o["class"])] = counts.get((o["variant_type"], o["class"]), 0) + 1
    print("variants", len(out)); [print(f"  {k[0]:28s} {k[1]:24s} {n}") for k, n in sorted(counts.items())]


if __name__ == "__main__":
    main()
