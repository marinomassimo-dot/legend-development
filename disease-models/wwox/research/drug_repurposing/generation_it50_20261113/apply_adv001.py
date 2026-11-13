"""ADV-001 (IT51-Q05) consumer rows: INV-06 evidence clause, question rows, dated lines in two READMEs (idempotent; originals kept; public text without catalogue names)."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
CLAUSE = ("[ADV-001] The muscarinic-receptor route rests on genetic rows (culture; abstract level) with a ceiling caveat; for two antimuscarinic drugs of the class the drug-class support carries a documented EBP-inhibition route whose attribution is unsettled, and EBP activity is unmeasured for the other antimuscarinics named. "
          "A profile of the pathway intermediates per compound before target attribution is a design position (INFERENZA); this does not say that EBP explains the muscarinic route, that unmeasured compounds act through EBP, or that M1 is irrelevant. The 216-row signed layer is not committed and no number is reproduced on it.")
Q05 = ("CONCLUDED", "ebp_reannotation_adv001_20261113/README.md: of the 15 favourable compounds of the 20-compound comparison, 4 have documented EBP inhibition (plus one binding-only), 3 indirect negatives, 3 another pathway enzyme with EBP unmeasured, 4 EBP unmeasured; 11 of 22 evidence rows involve a documented compound, from 7 papers (not independent); the 216-row layer is not committed")
Q03N = " [ADV-001] Hubler's open full text names none of the four antimuscarinics in the text (five candidates in the Methods; the heatmap is a figure): names still need a figure route."
NEWQ = [
 ["IT51-Q06", "ebp_reannotation_adv001_20261113/consumer_delta.md row 5 (c)", "Does a pathway-intermediate profile per compound (two antimuscarinics, one anticholinergic bladder drug, one thyromimetic) show EBP-type accumulation at the doses used in OPC preparations?", "Decides whether EBP-unmeasured compounds can carry a target attribution before the next myelination comparison.", "wet_lab_measurement", "OPEN", "", "ebp_reannotation_adv001_20261113/README.md answer 6", "2026-11-13", "Needs a measurement; unmeasured is not inactive.", "no", ""],
 ["IT51-Q07", "ebp_reannotation_adv001_20261113/consumer_delta.md row 5 (d)", "What is the direct EBP activity of the 14-reductase inhibitor of the reanalysis, against a morpholine reference?", "Decides whether it separates the pathway enzymes in the comparison (EBP itself is unmeasured for it).", "wet_lab_measurement", "OPEN", "", "ebp_reannotation_adv001_20261113/README.md answer 3", "2026-11-13", "Needs an in vitro measurement.", "no", ""],
 ["IT51-Q08", "ebp_reannotation_adv001_20261113/consumer_delta.md row 5 (a)", "Does Hubler's figure attribute the NMDA-antagonist compound to EBP or to TM7SF2 (the database binding rows and the paper differ)?", "Decides whether that compound counts as a documented EBP inhibitor.", "data_access_blocked", "OPEN", "", "ebp_reannotation_adv001_20261113/README.md answer 2", "2026-11-13", "A figure route is needed (the image returned HTTP 403).", "no", ""]]
IT14 = ("\n## Update 2026-11-13 (ADV-001; the text above is kept)\nThe muscarinic-class statements used for C1 and C2 attribute the clemastine/benztropine effect to a stated class without an EBP qualification. Two routes are documented for those two drugs (M1 genetics in culture; EBP inhibition with zymostenol accumulation in mouse OPC sterol profiling) and their attribution is unsettled; the qualification must not claim that EBP explains the muscarinic route or that M1 is irrelevant (`../ebp_reannotation_adv001_20261113/README.md`).\n")
IT29 = ("\n## Update 2026-11-13 (ADV-001; the text above is kept)\nA companion annotation of the 20-compound comparison by documented EBP status exists: `../ebp_reannotation_adv001_20261113/annotation_compounds.tsv` (and `annotation_signed_rows.tsv` for the 31-row layer). The 216-row layer quoted above is not committed and no number is reproduced on it; the signed layer is not edited.\n")
def main(check=False):
    csv.field_size_limit(10**9); n = 0
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        p = DR / f; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i, c = h.index("inv_id"), h.index("evidence_available"); k = 0
        for r in rows[1:]:
            if r[i] == "INV-06" and "[ADV-001]" not in r[c]: r[c] = (r[c] + " " + CLAUSE).strip(); k += 1
        if not check and k: csv.writer(open(p, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
        n += k
    qm = DR / "batch_sci_20261105/map/open_questions_map.tsv"
    rows = list(csv.reader(open(qm, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; have = {r[0] for r in rows}
    for r in rows[1:]:
        if r[0] == "IT51-Q05" and r[h.index("status")] != "CONCLUDED":
            r[h.index("status")] = Q05[0]; r[h.index("status_evidence")] = Q05[1]; r[h.index("last_touched")] = "2026-11-13"; r[h.index("blocking_reason")] = ""; n += 1
        if r[0] == "IT51-Q03" and "[ADV-001]" not in r[h.index("status_evidence")]:
            r[h.index("status_evidence")] += Q03N; n += 1
    for q in NEWQ:
        if q[0] not in have: rows.append(q); n += 1
    if not check and n: csv.writer(open(qm, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
    for f, note, tag in ((DR / "glia_maturation_it14_p4_20261101/README.md", IT14, "Update 2026-11-13 (ADV-001"), (DR / "phenotype_first_it29_20261105/README.md", IT29, "Update 2026-11-13 (ADV-001")):
        if tag not in f.read_text(encoding="utf-8") and not check:
            open(f, "a", encoding="utf-8").write(note); n += 1
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
