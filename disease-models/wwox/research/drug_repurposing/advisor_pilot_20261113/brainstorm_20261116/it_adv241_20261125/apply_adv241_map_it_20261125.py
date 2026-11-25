"""ADV-241 (IT, 2026-11-25): dated re-triage lines on eleven rows of the open-question map (the ten frozen rows except DC-05, which was not checked, plus RS-R8 and RS-R9).
No status change; old text kept; two blocking_reason notes appended (NR-01, RS-R9) where the old text is stale. Idempotent. Run from the repository root. Hypothesis level."""
import csv
from pathlib import Path
MAP = Path("disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv")
RES = "advisor_pilot_20261113/brainstorm_20261116/it_adv241_20261125/RESULT_ADV241_IT_20261125.md"
TAG = "[IT 2026-11-25 ADV-241"
SUF = " Result: " + RES + ".]"
LINES = {
 "RS-NP3B3": TAG + ", no status change: STILL_OPEN. PubMed (WWOX in title or abstract, entry date 2026-10-31 to 2026-11-25) gives one organoid item, a commentary on the held study (PMID 43036373, no new arm); the published supplement of PMID 42397075 (held) shows five arms in its blots and traces, with no wild-type plus AAV9-WWOX lane and no dead-mutant arm." + SUF,
 "RS-R2": TAG + ", no status change: STILL_OPEN. PubMed WWOX with TNK2 or ACK1, same window: 0 records; one ledger event after 2026-10-31 names ACK1 (FTR-20261115-25738261-01, partial read of the HCC paper already carried in R3), no new measurement." + SUF,
 "DC-04": TAG + ", no status change: NARROWED, answerable now as a record repair. R3 already reads SOURCE READ and the radar skips it. NP5A3 was served by catalogue_resilience_it16_p3_20261101 section 4 (186 of 186 assays recovered) and NP1B4 by ADV-029 (RS-NP1B4 CONCLUDED), but both reopen tables still read NEEDS-DATUM and the plan of 2026-11-25 (scout_daily --plan) still asks both. Repair = two verdict cells, N12 and N17 reopen text, regeneration of triggers and views; ready candidate for ADV." + SUF,
 "EN-03": TAG + ", no status change: NARROWED, not answered. HE changes of 2026-11-19 to 11-21 (e0d935bb5, d0bde503d, b89115950, a393995ef) filter hits and drop question-form words, but scout_daily --plan on 2026-11-25 still derives generic terms for NEED-ISR-ATTENUATION (transcripts, harmful, alone, mouse) and NEED-PDH-PYRUVATE-AXIS (effect, neural, cells, need). Owner HE." + SUF,
 "EN-04": TAG + ", no status change: STILL_OPEN. decisions.tsv unchanged since 2026-11-01; later ChEMBL runs record no failure (ADV-029, 2026-11-17, about 75 requests, 0 failed attempts; IT16 P3 replay, all HTTP 200); no reopen condition on record." + SUF,
 "NR-01": TAG + ", no status change: NARROWED to BLOCKED by access. The unread stub (PMID 36621327, lung injury, not neural) has no PMC deposit (Europe PMC 2026-11-25: isOpenAccess N, inEPMC N), no held file, a 2026-09 sweep verdict of unobtainable, and is item 8 of the operator PDF request list of 2026-11-24 (ADV-223). 'Executable by a reading' no longer holds." + SUF,
 "NR-02": TAG + ", no status change: NARROWED (already recorded 2026-11-21, RP-037). No later holding measures NMD or read-through for a WWOX allele; PubMed same window 0 records; blocked by the missing assay." + SUF,
 "NR-04": TAG + ", no status change: BLOCKED. The single-cell route (DL-MECH-181) needs E-MTAB-14792; the BioStudies API answered HTTP 403 on 2026-11-25 (one probe), as on 2026-10-25 and 10-31; the release request is an unsent draft with the operator. The 2026-11-23 ethosuximide Wnt tests concern a drug effect, not organoid maturity." + SUF,
 "NR-05": TAG + ", no status change: BLOCKED (no measurement held). PubMed WWOX with reactive oxygen, oxidative, redox or glutathione, same window: 0 records; the 2026-11-23 compound notes state the redox question as an unmeasured prediction; the Brain 2026 supplement does not measure ROS." + SUF,
 "RS-R8": TAG + ", no status change: still BLOCKED (outside contact; skipped by the frozen rule, checked anyway). PubMed WWOX with TNK2 or ACK1, same window: 0 records." + SUF,
 "RS-R9": TAG + ", no status change: NARROWED. The Brain 2026 supplement (PMID 42397075) is held since 2026-11-21 (FTR-20261121-42397075-31). Original blots read as images: SCAR12 c.1114G>C (G372R) lines 0.1, 0.1, 0.3 of wild type at week 16 (author densitometry, one membrane with wild type); knockout lanes on a different membrane show a faint smear at the same position; one antibody; no IP, no MS; WCH (G137V compound heterozygous) only as iPSC blot without numbers. The printed numbers equal the preprint ones carried in IT12; gate G0 stays unmet." + SUF,
}
APPEND_BR = {
 "NR-01": " [2026-11-25: the unread stub is not obtainable without a publisher copy; see the ADV-241 line.]",
 "RS-R9": " [2026-11-25: the supplement is now held; the remaining gaps are a same-membrane knockout lane at organoid stage, a second antibody, an IP or MS readout and organoid-stage data for G137V.]",
}
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
ie, il, ib = h.index("status_evidence"), h.index("last_touched"), h.index("blocking_reason")
for r in rows[1:]:
    q = r[0]
    if q in LINES and TAG not in r[ie]:
        r[ie] += " " + LINES[q]; r[il] = "2026-11-25"; n += 1
        if q in APPEND_BR and "[2026-11-25:" not in r[ib]:
            r[ib] += APPEND_BR[q]
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("edits", n)
