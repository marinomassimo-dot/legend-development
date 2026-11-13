"""IT50/SCI51: consumer_delta rows 1-3 of the SCI51 package (idempotent; dated clause; qualifications kept apart: no public structure / availability not stated / activity unmeasured)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
CLAUSE = ("[SCI51 update] The M1-selective arm is a design role, not a sourced reagent: the reagent named earlier has no public structure (a licence agreement withheld it; a correction and an expression of concern exist), whether it can be obtained from its developer is not stated in anything read, and its EBP activity is unmeasured in every source reached (unmeasured is not inactive). "
          "A role is filled only when a reagent of disclosed structure has its EBP activity measured in the OPC preparation (readout of a pathway intermediate or enzymatic assay) beside an EBP inhibitor; M1 tone is measured at a controlled plating density with an ACh add-back; the pair is read only after these gates, at submaximal doses with a T3 headroom arm. "
          "No M1-selective antagonist has an EBP datum in the sources reached (two antimuscarinic drugs have positive EBP data; four unnamed antimuscarinics were EBP-negative in one OPC line); the CW compounds are M1-low in one single-point assay, not shown M1-clean; the null-baseline occlusion is weaker than first stated but remains. IPOTESI; no reagent is qualified or disqualified.")
NOTES = {"IT50-Q09": " [SCI51] not answerable for the named reagent in the public record (no public structure; availability not stated; EBP activity unmeasured in every source reached); reformulated as IT51-Q01.",
         "IT50-Q03": " [SCI51] add: controlled plating density and an ACh add-back (tone is density-dependent: about 12, 5 and 2 nM at three densities).",
         "IT50-Q04": " [SCI51] only after IT51-Q01 and IT50-Q03, at submaximal doses with a T3 headroom arm."}
NEWQ = [
 ["IT51-Q01", "m1_ebp_reagents_sci51_20261113/README.md open question 1", "What is the EBP activity (sterol-intermediate readout or direct enzymatic assay) of a disclosed-structure M1-selective antagonist in an OPC preparation, beside the two antimuscarinic drugs with positive EBP data and an EBP inhibitor?", "Decides whether any M1 arm is non-sterol; gates every use of the reagent pair (reformulates IT50-Q09).", "wet_lab_measurement", "OPEN", "", "m1_ebp_reagents_sci51_20261113/consumer_delta.md row 3 (priority 1)", "2026-11-13", "Needs a measurement; the reagent first named has no public structure and availability is not stated.", "no", ""],
 ["IT51-Q02", "m1_ebp_reagents_sci51_20261113/README.md open question 3", "Does a CW3388-plus-agonist add-back arm separate the M1 residue (about 18-19% in one single-point assay) from the EBP effect?", "Decides whether the CW compounds can be read as M1-clean at the doses used.", "wet_lab_measurement", "OPEN", "", "m1_ebp_reagents_sci51_20261113/consumer_delta.md row 3 (priority 3)", "2026-11-13", "Needs a measurement; no M2-M5, sigma, hERG or Kir value exists for the CW compounds.", "no", ""],
 ["IT51-Q03", "m1_ebp_reagents_sci51_20261113/README.md open question 5", "Which four antimuscarinics were EBP-negative in one OPC line, and what are their per-compound M1/M3/M5 values?", "Decides whether missing M1 tone or a true M1 independence explains their inertness.", "data_access_blocked", "OPEN", "", "m1_ebp_reagents_sci51_20261113/consumer_delta.md row 3 (reading debt)", "2026-11-13", "The heatmap is not in the text layer and the publisher page returned a bot check twice; a route that exists is needed.", "no", ""],
 ["IT51-Q04", "m1_ebp_reagents_sci51_20261113/README.md open question 6", "What are the structures of the CW compounds (the paper's data supplement) and the drawing of TASIN-1 in the earlier paper?", "Decides the identity cells of the EBP-inhibitor arm.", "data_access_blocked", "OPEN", "", "m1_ebp_reagents_sci51_20261113/consumer_delta.md row 3 (reading debt)", "2026-11-13", "Supplement data and the figure were not reached.", "no", ""],
 ["IT51-Q05", "m1_ebp_reagents_sci51_20261113/README.md open question 7 (DREAM)", "If the IT29 case-1 signed rows are re-annotated by documented EBP status (existing ChEMBL EBP binding rows and the published screen lists), how many 'pro-differentiating' rows are explained by EBP inhibition?", "Decides whether the marker-level signed rows carry an EBP confound before any M1 or other mechanism is read from them.", "literature_executable", "OPEN", "", "m1_ebp_reagents_sci51_20261113/consumer_delta.md row 6 (priority 2; in silico, zero spend, executable in a later batch)", "2026-11-13", "In silico reanalysis of local tables; the screen's supplementary tables were not reached.", "yes", ""]]
def main(check=False):
    csv.field_size_limit(10**9); n = 0
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        p = DR / f; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i, c = h.index("inv_id"), h.index("next_test"); k = 0
        for r in rows[1:]:
            if r[i] == "INV-06" and "[SCI51 update]" not in r[c]: r[c] = (r[c] + " " + CLAUSE).strip(); k += 1
        if not check and k: csv.writer(open(p, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
        n += k
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; have = {r[0] for r in rows}
    for r in rows[1:]:
        if r[0] in NOTES and "[SCI51]" not in r[h.index("status_evidence")]:
            r[h.index("status_evidence")] += NOTES[r[0]]; r[h.index("last_touched")] = "2026-11-13"; n += 1
    for q in NEWQ:
        if q[0] not in have: rows.append(q); n += 1
    if not check and n: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
