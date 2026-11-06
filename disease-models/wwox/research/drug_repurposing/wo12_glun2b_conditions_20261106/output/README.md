# WO-12 result: conditions behind the GluN2B-over-GluN2A ratios of ifenprodil and Ro 25-6981

Run 2026-11-06 (label wo12-p). Rows are in `evidence.tsv`, routes in `queries.tsv`, staged receipts in `receipts/`.

## Answer

1. DATO: neither primary paper (PMID 8768735, PMID 9400004) could be read beyond its abstract. The publisher pages returned an access challenge, neither has a PMC copy (PMID converter and Europe PMC record), and OpenAlex lists no open copy; other repositories were not tested. Methods (glycine, glutamate or NMDA, Mg2+, holding voltage, pH, additions, IC50 fit) are therefore `not_read` for both (E05, E06). By the brief's rule the review was not substituted. Consumer row: "condition is not stated / paper unreachable", so NP5A2 stays NEEDS-DATUM.
2. DATO: the abstracts already show two differences. Hess used human NR1A/NR2A/NR2B in oocytes; Fischer used NR1C with NR2B or NR2A in oocytes, species not stated at abstract level (E01, E02). The review table flags the ifenprodil row as calculated at human receptors and does not flag the Ro 25-6981 row (E08).
3. INFERENZA: the two numbers behind the window are therefore not from one preparation (different species of clone at least, different NR1 splice variant). This already supports describing the window as a compilation across conditions. Whether glycine, glutamate, Mg2+ and pH also differ is unknown.
4. DATO: the module's 359-fold is not in Hess's abstract; the abstract says "approximately 350-fold" (E03). The 110 and 39,500 nM come from the review table. Fischer's own statement is ">5000-fold" and 0.009 versus 52 microM, which match the review (E04). Whether the table's IC50 refers to the same response as the papers (peak or steady state, which agonist level) is undetermined.
5. DATO (third source, full text, E09 E10): in an oocyte set-up with 100 micromolar glutamate and glycine (BaCl2 and Tricine in the solution; Mg2+ not listed, not stated to be absent), pH 7.3, -60 mV, ifenprodil gave 155 nM at NR1/NR2B and 28 micromolar at NR1/NR2A. INFERENZA: about 180-fold, so the ratio under a different single set of conditions sits inside 10^2 to 10^3 but at half of Hess's value.
6. DATO: direction of known condition effects on ifenprodil. Smaller inhibition at alkaline pH (abstract of PMID 9143010, E12); more efficient at high glutamate (use dependence) and low pH (statement in PMID 12122058 citing Kew 1996 and Mott 1998, which were not read; E11). Both push the IC50 down when the agonist level is high or pH is low. Magnitudes not read.
7. DATO (counter, E13 E14): in acutely dissociated rat cortical neurons the high-affinity ifenprodil IC50 is 0.21 micromolar (30 micromolar glycine, -60 mV), close to the oocyte NR2B value, but older neurons show a second, low-glycine-affinity population alongside the high-affinity one, and ifenprodil also partly inhibits it. No native NR2A-only comparator exists in that paper, so no native ratio can be formed.
8. INFERENZA on N17: the evidence cannot yet separate "property of the slice condition" from "oocyte compilation". The 2B-side potency looks portable to native neurons; the 2A-side number (tens of micromolar) has no native counterpart in anything read. Proposed N17 caveat: ratio window is a cross-paper, cross-species compilation; grade unchanged.
9. IPOTESI: if the Methods of both papers are obtained, the discriminating check is whether glycine and glutamate levels, pH and Mg2+ match; a mismatch in agonist level or pH would shift the 2B IC50 in the direction of item 6 and move the ratio.

## Consumers (proposals only; nothing in a shared file was changed)

| Consumer | Proposal |
|---|---|
| `target_first_it15_qa_nmdar_20261101/reopen_searches_it15_qa.tsv` row NP5A2 | stays NEEDS-DATUM; add: both Methods unreachable on 2026-11-06 by open routes; the two papers differ at abstract level in clone species or NR1 splice variant (E01, E02) |
| claim N17 wording | add the caveat "cross-paper, cross-species compilation"; grade unchanged; Hess's abstract says approximately 350-fold, the 359 is the review table's ratio |
| receipt ledger | five staged receipts in `output/receipts/` (three abstract_only, two partial_fulltext_read); not recorded; the integrator records them in event-ID order after a trial |

## What was not established

Every condition in the question for the two primary papers. Magnitudes of pH, glutamate and glycine effects. Species of Fischer's clones. Whether the review table's values are peak or steady-state IC50.

## Added after the independent audit (verify/audit_wo12.md)

Table 2 footnote a of the review says 3 micromolar glycine was used for IC50 determination; which rows it covers is not established, so the review table's conditions are not uniform. The audit read the third-source and native-neuron full texts through a page summariser, not raw; the quotes were consistent across repeated queries. The edits above are narrowings made from the auditor's governing passages and were not re-audited.

## What was not reachable

PMID 8768735 and PMID 9400004 full text (access challenge at the publisher, no PMC, no open repository copy; Unpaywall not used because it needs a contact address). A repository copy of Fischer 1997 listed by OpenAlex was not fetched: the environment refused the request as a copy of walled content, and it was not pursued. Mott 1998 and Kew 1996 were not found as open full text.

## Sources read

PMID 8768735 and PMID 9400004: abstract_only. PMID 9143010: abstract_only. PMID 12122058 and PMID 9482779: partial_fulltext (Methods and Results by keyword; figures not viewed). PMID 29446949: held full text, Table 2 and footnotes only, already verified earlier. No prior receipts existed for the five PMIDs. No search for counter-evidence beyond items 7 and the Kew glycine finding was possible within the bound.

## Queries

See `queries.tsv` (nine routes, all dated 2026-11-06).
