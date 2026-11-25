"""ADV-244 wording (IT, 2026-11-25): one carried limit on the organoid transcript set (GSE156243) in the packets of K01, D01, D02, M01, E02, I01 (cards rebuilt by the bridge)
and one dated clause on INV-16 (investigations.tsv, investigations_it20.tsv, ranking.json). Old text kept; idempotent. Run from the repository root.
Hypothesis level; no value, grade, rank or status changes; nothing is medical advice."""
import json
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
MARK = "[IT 2026-11-25, ADV-244"
NK = ("Whether any organoid transcript difference or null on this card (deposit GSE156243) is independent of the CRISPR clone: the sequenced knockout organoids are four "
      "of ONE clone (1B, from edit-spanning reads, ADV-244, SCI, 2026-11-25), the other clone (A2) was not sequenced, the comparator is two organoids of the parental line "
      "(the authors removed two of four wild-type libraries, one for failed quality control and one for not clustering), so a difference here is not shown to be a property of "
      "the knockout rather than of the clone. " + MARK + "]")
CARDS = ["K01_hif_axis_glycolytic_shift", "D01_a51", "D02_wnt_tankyrase", "M01_neurogenic_output_myc_window", "E02_ldh_inhibition", "I01_pdk_inhibition_dca_premise_seizure_glycaemia"]
INV = (" " + MARK + ": the human organoid transcript set is four knockout organoids of one CRISPR clone (1B) against two parental organoids, so 'higher in the organoid' is not shown "
       "to be independent of the clone; the other clone was not sequenced.]")
ANCHOR = "the human organoid shows SLC2A1 higher on transcript"

def packets():
    n = 0
    for c in CARDS:
        p = DR / f"cards/{c}.packet.json"; raw = p.read_text(encoding="utf-8")
        if MARK in raw: continue
        d = json.loads(raw); last = d["not_known"][-1]
        old = json.dumps(last, ensure_ascii=False)
        assert raw.count(old) >= 1
        i = raw.index(old, raw.index('"not_known"'))
        j = i + len(old)
        k = raw.rindex("\n", 0, i) + 1
        indent = raw[k:i]
        assert indent.strip() == "", repr(indent)
        raw = raw[:j] + ",\n" + indent + json.dumps(NK, ensure_ascii=False) + raw[j:]
        json.loads(raw); p.write_text(raw, encoding="utf-8"); n += 1
    return n

def edit_tsv(p):
    t = p.read_text(encoding="utf-8"); L = t.split("\n"); h = L[0].split("\t"); n = 0; c = h.index("evidence_available"); k = h.index("inv_id") if "inv_id" in h else 0
    for i, l in enumerate(L):
        f = l.split("\t")
        if i and len(f) == len(h) and f[k] == "INV-16" and MARK not in f[c]:
            assert ANCHOR in f[c]; f[c] = f[c].rstrip() + INV; L[i] = "\t".join(f); n += 1
    p.write_text("\n".join(L), encoding="utf-8"); return n

def edit_json(p):
    raw = p.read_text(encoding="utf-8"); d = json.loads(raw); n = 0
    for x in [y for k in ("investigations", "further_investigations", "conditional_hypotheses") for y in d.get(k, [])]:
        if x.get("inv_id") == "INV-16" and MARK not in x["evidence_available"]:
            old = json.dumps(x["evidence_available"], ensure_ascii=False)[1:-1]
            assert raw.count(old) == 1
            raw = raw.replace(old, old + json.dumps(INV, ensure_ascii=False)[1:-1]); n += 1
    p.write_text(raw, encoding="utf-8"); return n

if __name__ == "__main__":
    RK = DR / "ranking_it8_p9_20261029"
    print("packets", packets()); print("investigations.tsv", edit_tsv(RK / "investigations.tsv"))
    print("investigations_it20.tsv", edit_tsv(RK / "investigations_it20.tsv")); print("ranking.json", edit_json(RK / "ranking.json"))
