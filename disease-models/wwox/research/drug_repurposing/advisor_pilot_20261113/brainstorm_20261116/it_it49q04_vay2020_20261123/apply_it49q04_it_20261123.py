"""IT49-Q04 (IT, 2026-11-23): one dated line on the map row (old text kept; status stays OPEN); idempotent (marker 'Vay 2020').
Run from the repository root."""
from pathlib import Path

DR = Path("disease-models/wwox/research/drug_repurposing")
LINE = (" [IT 2026-11-23, Vay 2020 (PMID 32248813, PMC7132998; primary rat microglia in culture; read: abstract and Results, Kv7 and blocker parts): NARROWED on the protein half only: KCNQ2, KCNQ3 and KCNQ5 transcripts (KCNQ3 and KCNQ5 higher in the LPS state), "
        "Kv7.2 and Kv7.3 protein by immunocytochemistry (supplement not viewed); NO Kv7 current or membrane-potential measurement, NO opener tested, no slice, rat not human; the blocker XE-991 lowered migration only (its efficacy is voltage-dependent, so the other nulls are not evidence of no function). "
        "Absence by three routes (key-tagged PubMed, free-text PubMed, forward citations in Europe PMC): no paper measures a Kv7 current in microglia or applies an opener to microglia in slice; one in-vivo opener paper (QO-83, mouse stroke, PMID 39853651) has a microglial readout, abstract level only, cell-autonomy unknown. "
        "Status stays OPEN; no ranking, direction or compound change. Result: advisor_pilot_20261113/brainstorm_20261116/it_it49q04_vay2020_20261123/RESULT_IT49Q04_VAY2020_IT_20261123.md]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
L = p.read_text(encoding="utf-8").split("\n"); h = L[0].split("\t"); n = 0
for i, l in enumerate(L):
    f = l.split("\t")
    if i and len(f) == len(h) and f[0] == "IT49-Q04" and "Vay 2020" not in f[h.index("status_evidence")]:
        f[h.index("status_evidence")] += LINE
        f[h.index("last_touched")] = max(f[h.index("last_touched")], "2026-11-23")
        L[i] = "\t".join(f); n += 1
p.write_text("\n".join(L), encoding="utf-8")
print("IT49-Q04", n)
