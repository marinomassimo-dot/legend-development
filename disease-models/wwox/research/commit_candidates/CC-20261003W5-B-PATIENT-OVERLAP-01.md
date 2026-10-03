# COMMIT CANDIDATE — CC-20261003W5-B-PATIENT-OVERLAP-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 5 2026-10-03, branch `task/sci-B-20261003w5`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w5_B.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`paper_registry_current.md` · `PAPER 119` (Ehaideb 2018) one field before `LIT link`; `PAPER 018` (Oliver 2023) one field after `Role`. `full_text_queue_current.md` · `FT-140` one paragraph. (`PAPER 156`, `157`, `160` are created by `CC-20261003W5-B-REGISTRY-01`; apply that candidate first or rename the wikilinks.)

## Finding
1. **Burgess 2019 patient 93 = Oliver 2023 patient 6 (stated by the later authors).** The 2023 cohort says its patients 6 and 7 were "briefly reported" and cites PMID 31618474; genotype (`p.Glu17Lys` + intronic deletions in introns 3 and 4), sex, consanguinity and recruiting country agree. One patient. `FT-140`'s "overlap-confounded" occurrence of `p.(Glu17Lys)` is therefore resolved — and not toward the Piard series the 2026-09-21 triage suspected (Piard's `p.(Glu17Lys)` carrier has `p.(Ser304Phe)` in trans).
2. **Al Baradie 2022 family 2 is probably the R54* sibship of Ehaideb 2018**, re-described without cross-citation (allele pair, sibship, sexes, onset, identical dysmorphology and MRI wording, consistent age offset; one EEG descriptor differs). `PREMISE: INFERENZA`, strong; counted once.
3. **Hengel 2020's WWOX family is Mallaret 2014 family 2** (its own Supplementary Table 1 says so); the 2026-09-21 "zero WWOX variants" reading of PMID 32214227 was an artefact of a table-less extraction.

**Counting rule applied (wave-3 L239R rule, wave-4 Tarta-Arsene rule):** a patient matched on allele pair plus at least sex, onset and course across two reports is counted once; where the later authors state the identity it is a DATO, where they do not it is an INFERENZA and still counted once, with the uncertainty recorded on the record.

## Change class
**MINOR** — identity annotations; no claim status or working-model block changes.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main f110c76 merged into the branch (no registry file changed on the branch): exit 0, 2 op(s), anchors ['PAPER 119', 'PAPER 018'])

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 119",
  "old": "**LIT link:** [[literature_tracking_log_current#LIT-0253]]",
  "new": "**Patient overlap (2026-10-03, `CC-20261003W5-B-PATIENT-OVERLAP-01`):** 🔴 the homozygous `p.Arg54*` sibship (older sister, younger brother) is probably family 2 of [[paper_registry_current#PAPER 156]] (Al Baradie 2022), re-described without cross-citation: same allele pair, sibship structure and sexes, onset at two months with spasms, the sister's hypertelorism / large ears / high arched palate, and a word-for-word identical MRI sentence (asymmetrical volume loss with asymmetrical ventricular dilatation and callosal thinning); the ages printed (18 and 3 months here; 5 y and 3 y 9 mo there, the sister 'first seen … at the age of 18 months, with her younger brother') advance by the same interval. One EEG descriptor differs (burst suppression here, hypsarrhythmia there). `PREMISE: INFERENZA` — not author-confirmed: count the sibship once. That paper also lists these three children as separate literature rows.\n**LIT link:** [[literature_tracking_log_current#LIT-0253]]"
 },
 {
  "op": "replace-within",
  "id": "PAPER 018",
  "old": "**Role:** epilettologia WWOX-DEE; sopravvivenza Kaplan-Meier; missense vs non-missense survival",
  "new": "**Role:** epilettologia WWOX-DEE; sopravvivenza Kaplan-Meier; missense vs non-missense survival\n**Patient overlap (2026-10-03, `CC-20261003W5-B-PATIENT-OVERLAP-01`):** patient 6 (EIMFS; `p.Glu17Lys` with two intronic deletions, introns 3 and 4) is the WWOX patient of [[paper_registry_current#PAPER 157]] (Burgess 2019): this paper says its patients 6 and 7 were 'briefly reported' and cites Burgess; genotype, sex, consanguinity and recruiting country agree. One patient, counted here. This paper, not Burgess, carries the RNA result: intron-4 deletion → exon 5 skipping, intron-3 deletion benign."
 }
]
```

## Op list — `full_text_queue_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main f110c76 merged into the branch (no registry file changed on the branch): exit 0, 1 op(s), anchors ['FT-140'])

```json
[
 {
  "op": "replace-within",
  "id": "FT-140",
  "old": "⚠️ `PMID 31618474` reports a second, **overlap-confounded** occurrence of `p.(Glu17Lys)`.",
  "new": "⚠️ `PMID 31618474` reports a second, **overlap-confounded** occurrence of `p.(Glu17Lys)`.\n🟢 **Resolved 2026-10-03 (intake wave 5, Scientist B, `CC-20261003W5-B-PATIENT-OVERLAP-01`).** `31618474` re-read at source with gene symbols, tables and supplement (`FTR-20261003-31618474-01`): its WWOX patient is **patient 6 of `PMID 36779245`** ([[paper_registry_current#PAPER 018]]), which says so itself — not a Piard patient (Piard's `p.(Glu17Lys)` carrier has `p.(Ser304Phe)` in trans). `32214227` re-read (`FTR-20261003-32214227-01`): Table 1 **does** carry a WWOX row — homozygous `p.(Gly372Arg)`, the published SCAR12 family of [[paper_registry_current#PAPER 042]] — so the FT-116 statement 'zero WWOX variants' was an artefact of the table-less extraction. `35715422` read (`FTR-20261003-35715422-01`): one WWOX carrier with an ATP7A second diagnosis. Registry landings `PAPER 157`/`158`/`160` (provisional, `CC-20261003W5-B-REGISTRY-01`). `37095367` untouched by this wave."
 }
]
```

## Registry records needed
`PAPER 156` (35792847), `PAPER 157` (31618474), `PAPER 160` (32214227) — created by `CC-20261003W5-B-REGISTRY-01`. `PAPER 119`, `PAPER 018`, `PAPER 042`, `PAPER 117` exist.

### LOCATOR TRIPLES FOR BLIND AUDIT
(the 2023 cohort's patients 6 and 7 were reported before | including two patients (Patients 6 and 7) briefly reported. | PMID 36779245, Methods, cohort paragraph; files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml)
(patient 6 of the 2023 cohort carries two intronic deletions in introns 3 and 4 | intronic deletions involving intron 3 and intron 4. | PMID 36779245, Results, genetics paragraph; files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml)
(the intron-4 deletion was tested at RNA level and causes exon 5 skipping | RNA sequencing followed by real‐time polymerase chain reaction (RT‐PCR) suggested that the intron 3 deletion was a benign variant, whereas the intron 4 variant resulted in exon 5 skipping | PMID 36779245, Results, genetics paragraph; files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml)
(the 2019 cohort's WWOX patient carries E17K and two intronic deletions in introns 3 and 4 | Compound heterozygous: c.49G>A p.E17K and 2x intronic deletions: intron 3 and 4 | PMID 31618474, Supplementary Table 1, row for Patient 93; files/fulltext/PMID31618474_Burgess2019_supplement/NIHMS1616220-supplement-Supp_Table_1_xlsxdump.txt)
(the 2019 cohort links E17K to a different, earlier carrier | WOREE (p.E17K Piard et al.2018 patient 12) | PMID 31618474, Supplementary Table 2, WWOX row; files/fulltext/PMID31618474_Burgess2019_supplement/NIHMS1616220-supplement-Supp_Table_2_xlsxdump.txt)
(Piard's E17K carrier has a missense in trans | p.[Glu17Lys];[p.Ser304Phe] | PMID 30356099, Supplemental Table 1, Patient 12 protein row; files/fulltext/PMID30356099_Piard2019_supplement/41436_2018_339_MOESM1_ESM.xlsx)
(the Ehaideb sister was 18 months old and sister of the affected boy | 18 months old female (sister of patient 2). | PMID 30746283, Case presentation, Patient 3; files/fulltext/PMID30746283_Ehaideb2018_PMC.xml)
(Ehaideb describes the sister's MRI as asymmetrical volume loss with asymmetrical ventricular dilatation | MRI brain revealed generalized asymmetrical brain tissue volume loss and asymmetrical ventricular dilatation, thinning of corpus callosum | PMID 30746283, Case presentation, Patient 3; files/fulltext/PMID30746283_Ehaideb2018_PMC.xml)
(Al Baradie describes the family-2 sister's MRI in the same words | Brain MRI showed generalized asymmetrical brain tissue volume loss with asymmetrical ventricular dilatation and thinning of the corpus callosum. | PMID 35792847, Results, Patient 2.2; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(the family-2 sister was first seen at 18 months with her younger brother | She was first seen in our hospital at the age of 18 months, with her younger brother. | PMID 35792847, Results, Patient 2.2; files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(Al Baradie lists the Ehaideb children as separate literature patients | Ehaideb et al. (2018) [19] 1 M Seizure 2 months Focal to bilateral tonic-clonic Epileptic Spasms | PMID 35792847, Table 3 (continued); files/fulltext/PMID35792847_AlBaradie2022_JLE_fulltext.html)
(Hengel's WWOX family is a previously published family | this family is published (PMID: 24369382) | PMID 32214227, Supplementary Table 1, WWOX row; files/fulltext/PMID32214227_Hengel2020_supplement/41431_2020_609_MOESM1_ESM_xlsxdump_tab.txt)
(Hengel's Table 1 carries a WWOX row with homozygous G372R | NM_016373.4:c.1114G>C: p.(Gly372Arg) | PMID 32214227, Table 1, WWOX row; files/fulltext/PMID32214227_Hengel2020_PMC.xml)
