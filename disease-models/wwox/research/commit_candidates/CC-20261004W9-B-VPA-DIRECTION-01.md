# COMMIT CANDIDATE — CC-20261004W9-B-VPA-DIRECTION-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 9 2026-10-04, branch `task/sci-B-20261004w9`.
**context_policy:** `SOURCE_FIRST` for the four primaries (first pass written and committed before the wave-8 candidate or any registry text was opened); the comparison with `CC-20261004W8-A-VPA-DIRECTION-01` followed. That reading is `QUESTION_DRIVEN` for the comparison step only.
**Not medical advice.** No clinical reading of any kind follows from this candidate.

## Target
`discovery_ledger_current.md`, record `DL-REPO-003` (provisional id; created by `CC-20261004W8-A-VPA-DIRECTION-01`, so this candidate is applied only after that one lands; the integrator renumbers). Two record-scoped `replace` ops on its text.

## Finding
Four of the five primaries behind the valproate row of PMID 41254692 Table S7 are now read (PMIDs 23179753, 24935251, 26272509, 27188386; receipts `FTR-20261004-<pmid>-01`; all `partial_fulltext_read`). The fifth (PMID 28001369) is still unread. In all four:

- WWOX is mentioned **zero times in the text**; it exists only as probe-set rows in supplementary tables. The paper-level statement that "valproate changes WWOX" is therefore carried by no sentence anywhere in the four.
- **Direction with valproate is up, never down**, wherever a sign is recoverable: PMID 23179753 (supplementary lists, ratio above 1 = up per its own legend): five probe-set rows up (1.47 to 2.12; adjusted p 0.0023 to 0.037) in two neural-lineage systems at 1.05 to 2 mM; PMID 24935251: one row up (1.574; adjusted p 0.042) at 600 uM for 4 days; PMID 26272509 (genome-wide table, direction fixed by PAX6 and OTX2 sentinels because its own legend is ambiguous): three of five probe sets up (1.33 to 1.68; adjusted p 0.007 to 0.027) at 600 uM for 6 days; PMID 27188386 (signed fold change; PAX6 is -10.56 in the same block): +2.127 in embryoid bodies and +1.683 in neural induction. PMID 27188386 Table 7 lists the probe set at 1000 uM without direction.
- The only "down" WWOX row in the four (ratio 0.59, PMID 24935251 Table S1, 6 h) is an **untreated developmental change** versus undifferentiated hESC, not a drug effect.
- Same system throughout: H9 hESC differentiated toward neural lineage (immature neuroepithelium, up to 14 days), millimolar-range valproate at 0.6 to 2 mM (the authors cite 0.5 to 1 mM as human-relevant). Not mature neurons, no patient cells, no WWOX allele.
- The data are **not independent**: the neural-induction values in PMID 26272509 and PMID 27188386 are the same measurement (identical 1.68 for probe 223868_s_at), and the embryoid-body values in PMID 23179753 (2.12) and PMID 27188386 (2.13) match.
- A trichostatin A row of the same table is mixed (one WWOX probe set down 0.79 and one up) and entinostat is up, so even within HDAC inhibitors the direction is probe- and compound-dependent.

**Consequence for the wave-8 lead.** The wave-8 reading of Table S7 (CTD "Decreases expression") is not reproduced by any of the four primaries read: all four show up, or nothing. The database annotation is **contradicted by the primaries available**, and the unread fifth (PMID 28001369) is the only remaining candidate source for "decrease". Why CTD says "decreases" is not determined here (INFERENZA candidates, none tested: the fifth paper; a sign error or pooling in the curated row; mis-assignment of the untreated developmental 0.59 row). Nothing here shows that valproate raises WWOX in a patient or in any mature cell.

## Change class
**MINOR** — qualifies one research-layer lead; no claim, registry record or working-model block changes; the lead stays `open` and non-clinical.

## Registry records needed
`PAPER` and `LIT` records for the four PMIDs: see `CC-20261004W9-B-REGISTRY-01`.

## Op list — `discovery_ledger_current.md` (record-scoped; apply after `CC-20261004W8-A-VPA-DIRECTION-01`; `old` strings are verbatim from that candidate's `text` and unique within the record it creates)

```json
[
 {
  "op": "replace",
  "id": "DL-REPO-003",
  "old": "- **Next action:** read PMIDs 23179753, 24935251, 26272509, 27188386 and 28001369 and record, per paper, the direction, cell type, dose and readout. Until then, **no clinical reading of any kind**, and no entry in the therapeutic tracker.",
  "new": "- **Four of five primaries read (wave 9, Scientist B; receipt events FTR-20261004-23179753-01, -24935251-01, -26272509-01, -27188386-01; all partial reads).** WWOX is mentioned zero times in the text of all four; it appears only as probe-set rows in supplementary tables from one hESC-to-neural platform (H9 cells, immature neural-lineage systems, 14 days at most, valproate 0.6 to 2 mM). Wherever a sign is recoverable the direction is UP with valproate (ratios 1.33 to 2.13, adjusted p 0.007 to 0.042; the sign for the neural-induction system fixed by PAX6/OTX2 sentinels), never down. The one 'down' row (0.59) is an untreated developmental change. The four share data (the neural-induction and embryoid-body values recur across papers), so they are not four replications. **The curated 'Decreases expression' row is therefore contradicted by every primary that could be read; the fifth, PMID 28001369, is still unread and is the only source left that could carry a decrease.** Still: no clinical reading of any kind, no entry in the therapeutic tracker; an up-direction in immature hESC-derived cells at 0.6 to 2 mM says nothing about mature neurons, patient cells, a WWOX allele or a clinical exposure, and for a patient with two loss-of-function alleles there is no residual transcript to raise.\n- **Next action (remaining):** obtain PMID 28001369 (paywalled) and record direction, cell type, dose and readout; ask whether CTD's row rests on it. A WWOX transcript and protein measurement in human neural cells with and without valproate and a positive control for HDAC inhibition remains the only test that would settle direction in a relevant cell."
 },
 {
  "op": "replace",
  "id": "DL-REPO-003",
  "old": "the five primaries are **unread**",
  "new": "four of the five primaries are now read (see the wave-9 entry below); the fifth is **unread**"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(WWOX is up with 2 mM valproate in 14-day embryoid bodies, ratio 2.12 | SHEET=Suppl. Table 1 - Sheet 7 | ROW=860 | A=WWOX | B=2.12 | C=4.64e-06 | D=0.00339 | PMID 23179753, Supplementary Table S1 sheet 7 (UKK 2 mM VPA); files/fulltext/PMID23179753_Krug2013_supplement/204_2012_967_MOESM2_ESM_xlsdump.txt)
(the legend defines ratio above 1 as up | the corresponding fold changes of the PS (<1 = down-regulated; >1 = up-regulated) | PMID 23179753, Supplementary Table S1 legend)
(600 uM valproate for 4 days lists WWOX with ratio 1.574 | SHEET=T4d VPA | ROW=1384 | A=219077_s_at | B=WWOX | C=1.5743166458443683 | D=2.49E-3 | E=4.2000000000000003E-2 | PMID 24935251, Supplementary Table S2 sheet T4d VPA; files/fulltext/PMID24935251_Balmer2014_supplement/204_2014_1279_MOESM3_ESM_xlsxdump.txt)
(the only down-direction WWOX row in PMID 24935251 compares untreated cells with hESC | hESC were differentiated towards NEP and samples were taken after 6h, 4d and 6d of differentiation. Differentially expressed PS were determined compared to hESC. | PMID 24935251, Supplementary Table S1 sheet 6h row 2; files/fulltext/PMID24935251_Balmer2014_supplement/204_2014_1279_MOESM2_ESM_xlsxdump.txt)
(valproate lowers PAX6 in the same table, which fixes the ratio direction | SHEET=VPA-sheet 15 | ROW=15095 | A=15094 | B=205646_s_at | C=PAX6 | D=paired box 6 | E=0.09 | F=0 | G=0 | PMID 26272509, Supplemental Table S1 sheet VPA; files/fulltext/PMID26272509_Rempel2015_supplement/204_2015_1573_MOESM2_ESM_xlsxdump.txt)
(WWOX probe 223868_s_at is up 1.68 with valproate | SHEET=VPA-sheet 15 | ROW=33146 | A=33145 | B=223868_s_at | C=WWOX | D=WW domain containing oxidoreductase | E=1.6800000000000002 | F=1E-3 | G=7.0000000000000001E-3 | PMID 26272509, Supplemental Table S1 sheet VPA row 33146; same artefact)
(valproate raises WWOX probe 219077_s_at by 2.127 in embryoid bodies in a signed-fold-change table | S=219077_s_at | T=2.1265200000000002 | U=5.3745300000000004E-16 | PMID 27188386, Supplementary Table 3 row 553 columns S-U; files/fulltext/PMID27188386_Shinde2016_supplement/204_2016_1741_MOESM2_ESM_xlsxdump.txt)
(the PAX6 sentinel is negative in the same signed table | BC=205646_s_at | BD=-10.5619 | BE=2.3600900000000001E-15 | PMID 27188386, Supplementary Table 3 row 5866 columns BC-BE; same artefact)
(Table 7 lists the WWOX probe set at 1000 uM valproate without direction | SHEET=Suppl. Table 7 | ROW=2661 | D=219106_s_at | E=219077_s_at | F=WWOX | PMID 27188386, Supplementary Table 7 row 2661; same artefact)
(the wave-8 export row lists all five references for valproate and WWOX with 'Decreases expression' | A=Valproic Acid | B=D014635 | C=WWOX | D=Homo sapiens | E=Decreases expression | F=23179753|24935251|26272509|27188386|28001369 | PMID 41254692, Additional file 1 Table S7; files/supplements/PMID41254692/MOESM1_TableS7_rows.txt)

## BATCH DISPOSITION — `BATCH_20261004_003` (2026-10-04, ACTOR_ID `scientist`, Scientist M), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** `PROPAGATED` (MINOR, WM_v7.15 → WM_v7.16).

**Surfaces written:** discovery_ledger_current.md

Both ops applied on `DL-REPO-003`, the record `BATCH_20261004_002` landed. The first `old` string was **`OLD_ABSENT`** and was re-measured on current `main`: the landed next-action line emphasises differently from the wave-8 candidate's draft. One wording change at integration: *«for a patient with two loss-of-function alleles»* became *«where both alleles are loss-of-function»*, which is the same point at class level in a public edition. 🔴 **The direction debt is recorded as NOT settled:** four of five primaries show WWOX **up**, the curated *«Decreases expression»* row is contradicted by every primary that could be read, the four share measurements and are not four replications, and the fifth primary is paywalled and unread. **No clinical reading of any kind**, and no therapeutic-tracker entry. Author outreach for the fifth paper is **reserved to the operator** and was not undertaken.

**Not medical advice.**
