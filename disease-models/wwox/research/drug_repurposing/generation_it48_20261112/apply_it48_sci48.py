"""IT48 increment 2: SCI48 consumer deltas (rows 1-4) applied as dated clauses and open-question rows. Idempotent; original text stays."""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
RA = ("RA839 (a second non-covalent KEAP1 Kelch binder, myeloid-cell data only, identity from the paper, catalogue id not reconciled)")
COUNTER = ("[SCI48] The second non-covalent Kelch binder (Winkel 2015; text and nine figures read, supplement unreachable) is a second non-covalent Kelch binder with myeloid-cell data only: in germline Nrf2-knockout bone-marrow macrophages 2 of 105 probe sets persisted, but no check of the knockout is printed and the covalent triterpenoid comparator is in no knockout arm, so the paper does not meet the loss criterion as printed; it is a comparator for a survivor set, not a probe. The earlier statement that it reaches the first two comparisons at abstract depth is replaced. "
           "The commonest covalent electrophile has germline-null neural designs in at least four independent groups (benefit lost in the nulls; one partial persistence at 50 mg/kg): a comparator, not a probe (loss germline or unverified, no KEAP1-loss arm, no binder partner); that line is at mixed depth (three texts, abstracts). No reagent is a probe in a neuron or astrocyte; the one probe row is the catalogued binder in rat microglia. No acute NFE2L2 loss verified at the endpoint time exists in any neural source read. The label 'probe' that the comparison engine now derives for these two reagents only means that their mechanism was read in primary texts; the package role of both is comparator (germline or unverified loss, the binder in myeloid cells only), and the engine has no comparator role yet (open with Harness).")
PREMISE = ("[SCI48] An adequate loss is verified as protein and mRNA at the endpoint time, not by an allele PCR; a germline loss is not an acute loss.")
NEXT = ("[SCI48] Step X2 adds: loss verified as protein and mRNA at the endpoint time (not an allele PCR); the electrophile inside the loss arm beside the binder; loss-alone and reagent-alone arms under the same challenge; two electrophile exposures matched on a proximal on-target response (one target gene is not enough). Step X1 adds the inactive analogue of the binder as a control. IPOTESI; does not speak to WWOX; conditional on X0.")
Q06 = ("CONCLUDED", "nrf2_comparator_sci48_20261112/README.md answer 2 (text and nine figures read by plain request, 2026-11-12): does not meet the knockout criterion as printed; comparator for a survivor set. Supplement unread: IT48-Q02")
Q09 = ("CONCLUDED", "nrf2_comparator_sci48_20261112/README.md answer 3 (existence and role only): germline-null neural designs in at least four groups, comparator not probe; acute loss: IT48-Q03; depth beyond abstracts: IT48-Q04")
NEWQ = [
 ["IT48-Q02", "nrf2_comparator_sci48_20261112/consumer_delta.md", "What do Winkel 2015 supplement Tables S1-S4 give (knockout baseline, direction of the two surviving genes, the 93-target panel)?", "Decides whether the survivor set of the second binder can be read as NRF2-independent action.", "literature_executable", "OPEN", "", "nrf2_comparator_sci48_20261112/README.md answer 2", "2026-11-12", "The PMC supplement URL is an interstitial and Europe PMC says not open access; needs a route the operator authorises.", "no", ""],
 ["IT48-Q03", "nrf2_comparator_sci48_20261112/consumer_delta.md", "In a neuron class and an astrocyte class, what do an electrophile and a Kelch binder do with and without an acute NFE2L2 loss verified at protein and mRNA at the endpoint time (loss-alone and reagent-alone arms)?", "Decides whether either reagent can be read as NRF2-dependent in neural cells; no source has an acute verified loss.", "wet_lab_measurement", "OPEN", "", "nrf2_comparator_sci48_20261112/README.md answer 4; engine M-N1, M-N2", "2026-11-12", "Needs a wet laboratory measurement; no public data.", "no", ""],
 ["IT48-Q04", "nrf2_comparator_sci48_20261112/consumer_delta.md", "What do the sulforaphane neural null-design papers without a PMC id (kindling, MPTP, slice, spinal cord, ICH 2007, Moretti 2021) show beyond the abstract?", "Decides whether the abstract-depth comparator rows hold in the full texts (a depth artefact is not a biological result).", "literature_executable", "OPEN", "", "nrf2_comparator_sci48_20261112/README.md answer 3", "2026-11-12", "No route without a PMC id.", "yes", ""]]

def clause(path, idcol, idval, col, txt, tag, check):
    rows = list(csv.reader(open(path, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
    i, c = h.index(idcol), h.index(col)
    for r in rows[1:]:
        if r[i] == idval and tag not in r[c]:
            r[c] = (r[c] + " " + txt).strip(); n += 1
    if not check and n: csv.writer(open(path, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    return n

def main(check=False):
    csv.field_size_limit(10**9); n = 0
    cv = DR / "generation_it41_20261109/compound_view.tsv"
    rows = list(csv.reader(open(cv, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
    for r in rows[1:]:
        if r[h.index("item_id")] == "V19" and "RA839" not in r[h.index("name_full")]:
            r[h.index("name_full")] += "; " + RA; n += 1
    if not check and n: csv.writer(open(cv, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    n += clause(cv, "item_id", "V19", "counter", COUNTER, "[SCI48]", check)
    n += clause(cv, "item_id", "V19", "open_premise", PREMISE, "[SCI48]", check)
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        n += clause(DR / f, "inv_id", "INV-08", "next_test", NEXT, "[SCI48]", check)
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
    for r in rows[1:]:
        for qid, (st, ev) in (("IT46-Q06", Q06), ("IT46-Q09", Q09)):
            if r[0] == qid and r[h.index("status")] != "CONCLUDED":
                r[h.index("status")] = st; r[h.index("status_evidence")] = ev; r[h.index("last_touched")] = "2026-11-12"; r[h.index("blocking_reason")] = ""; n += 1
    have = {r[0] for r in rows}
    for q in NEWQ:
        if q[0] not in have: rows.append(q); n += 1
    if not check and n: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    print(("would change " if check else "changed ") + str(n))

if __name__ == "__main__":
    main("--check" in sys.argv)
