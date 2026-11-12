"""IT49: open-question rows from the KH/HY mapping and the INV-02 case (idempotent; appended to the existing map; no parallel register)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
NEWQ = [
 ["IT49-Q01", "hcn_20261107/output/hypotheses.tsv (HY1)", "At matched starting potential and matched peak excursion, do Wwox-deficient and control layer II/III neurons show the same sag and the same Ih amplitude and V1/2 while Rin and rest still differ?", "Decides whether the K+/leak identity (Kv7 against other leak) goes ahead of any HCN lever (HY1 holds) or HY3 opens.", "wet_lab_measurement", "OPEN", "", "generation_it49_20261112/README.md (HY1 mapped; its outcomes are in the reader row)", "2026-11-12", "Needs a slice measurement; no public voltage-clamp Ih exists in any Wwox preparation.", "no", ""],
 ["IT49-Q02", "generation_it49_20261112/p5_case_inv02/result_it49.md", "What do the held cell-class RNA sources say for the ISR genes (EIF2AK1-4, EIF2B1-5, PPP1R15A/B, EIF2S1)?", "Decides whether an ISR measurement must name its cell class (the join returns unknown for all 11 genes now).", "literature_executable", "OPEN", "", "generation_it49_20261112/p5_case_inv02/result_it49.md", "2026-11-12", "A zero-spend extraction of the same local tables (as IT47-B1); reanalysis, not a measurement; it cannot give the protein-level sign.", "yes", ""],
 ["IT49-Q03", "generation_it49_20261112/p5_case_inv02/result_it49.md", "Can packages that hold a design (steps, controls, decision branches) instead of hypothesis rows be read by the generator without a new layout reader?", "Decides whether design-only knowledge (for example the ISR package) can act on the generator at all.", "engine_or_infrastructure", "OPEN", "", "generation_it49_20261112/p5_case_inv02/result_it49.md (P1)", "2026-11-12", "Hypothesis layouts are consumed by a manifest row and a mapping entry; a design layout is not (handed to Harness).", "no", ""],
]
def main(check=False):
    csv.field_size_limit(10**9)
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); have = {r[0] for r in rows}; n = 0
    for q in NEWQ:
        if q[0] not in have: rows.append(q); n += 1
    if not check and n: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
