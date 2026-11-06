# Blind quote audit A1b — README

Date: 2026-11-06. Method: `legend-locator-audit` (two questions per triple: does the quote carry the
proposition; does the source say more or less). Input: 33 triples (`triples_A1b.tsv`), 29 case-report
rows (`A1b-`) and 4 trial/review rows (`A2b-`). The auditor opened no file of the batch folder other
than this output directory, no registry, dossier, receipt or manifest.

Each labelled field that asserts something was checked against the source; `same_patient_as` was
ignored as instructed. Quotes were matched after normalising whitespace, case, ligatures, dashes and
Greek letters; stitched quotes were checked part by part.

## Counts

| Verdict | Rows |
|---|---|
| SUPPORTED | 33 |
| OVERSHOOT | 0 |
| UNDERSHOOT | 0 |
| NOT_IN_SOURCE | 0 |
| UNVERIFIABLE_SURFACE | 0 |

All 33 quotes were found as text in the named section, table row or abstract. No row carried a
statement the source does not make; no row narrowed a statement the source makes.

## Non-SUPPORTED rows

None.

## Notes on SUPPORTED rows (not defects; recorded so the reader can judge the labels)

- `A1b-A1-08` (PMID 36537114, patient 5): the row labels `genotype_class: missense`. The source's own
  Table 1 and narrative give a compound heterozygote, missense c.689A>C plus a 36.3 kb deletion of
  exon 5. The label is coarse, not contradicted; a scheme with a null/missense class would use that.
- `A1b-A1-14` (PMID 37583270, serial 39): `genotype_class: splice`; Table 1 row 39 is an exonic
  deletion in trans with a 3' splice-site variant. Same remark. The Table 4 key resolves the row:
  FIHT = failed initial hormonal therapy (so `hormonal` -> `none` holds), PES = persistent epileptic
  spasms, SF = seizure free; the cell `PES, SF (6)` is indeed self-contradictory as the row says.
- `A1b-A1-39` / `A1b-A1-45` (PMID 36779245, Patient 7): the "current" marking is typographic
  underlining. In the raw JATS XML the cell underlines LTG, ZNS, CLB, LAC, MDZ only; VGB, PRED and
  ACTH are not underlined, which is what `stopped` rests on. Patient 5's cell underlines VPA only.
- `A1b-A1-57` (PMID 40126049): "no worsening listed in the supplement" was checked against the
  supplement PDF re-extracted with pdftotext (7 pages): the seizure-worsening list (TSC2 x3, SCN1A x3,
  one each MECP2, CDKL5, TUBB2A, TUBA1A, SCN8A, PLA2G6, NEXMIF, MEF2C, KCNT1) and the CGI-worsening
  list do not contain WWOX. The held layout text of the supplement is complete (same content).
- `A1b-A1-01` / `A1b-A1-03` (PMID 30361190): the flat `.txt` interleaves the two columns, so the
  quotes were matched in the PDF text layer (pdftotext, raw mode). Table 1 "This study" columns:
  case 1 = 24m/M, 3 AEDs, AED response Partial; case 2 = 13m/M, 4 AEDs, AED response Poor.
- `A1b-A1-04` to `A1b-A1-07` (PMID 36537114): only Scholar Gateway chunks 0, 1, 2, 18, 22-25 exist
  locally; the per-patient narratives for patients 1-4 were not delivered. The rows say "not stated
  on the delivered surface" for co-therapy, which is the honest reading of that surface; the Table 1
  cells and the Discussion sentence (diet "notably improved seizure control" in patients 1, 2, 4)
  are what the rows rest on.
- `A2b-B13` (PMID 23740534): the quote is the "Authors' conclusions" sentence of the PubMed abstract,
  verbatim. The Europe PMC full-text route failed (below); the abstract carried every asserted field.

## Artefacts read (route, bytes, sha256 at emit time)

Held copies under `files/fulltext/` (read-only):

| PMID | File | Bytes | sha256 |
|---|---|---|---|
| 30361190 | PMID30361190_Shaukat2018_JLE.pdf (text layer via pdftotext) | 2144290 | 12e0930fa60a2c06a9ea3ca867506a24ff7d3a2d5eb5b7abeb686cd18d620958 |
| 30361190 | PMID30361190_Shaukat2018_JLE.txt (column-interleaved; partial matches only) | 75964 | ae3103d907aceef77695534708bca43e6b476fca12b401ca0f8c0785842ade78 |
| 36537114 | PMID36537114_Chong2023_SGchunks_text_2026-10-21.txt | 29880 | b3a6d7a077c020ba402ae29556d9a8eba825c0d8d729216613d0d3cc69322ad9 |
| 37583270 | PMID37583270_Nagarajan2023_PMC.xml | 250812 | 7820a11b0bbc0a35e091817dae382d9d5a16a55f8777ce122426d48512e364f6 |
| 39101447 | PMID39101447_You2024_PMC.xml | 71261 | d077cc45b50e52dea87555d2c5ce0263aa5e4d97ee5b6032a26d9731426f312e |
| 35573960 | PMID35573960_Riva2022_PMC.xml | 57567 | e74bfe47c66e4ed906d4c61be665cc28e66717dc2dd98868a39094fba51c4ddc |
| 42092735 | PMID42092735_SercePehlevan2026_PMC.xml | 44418 | 19d041ace7703e21c54d75c2b27e69da9732603f6a0cab2ab6f0c401c5bf16e7 |
| 35792847 | PMID35792847_AlBaradie2022_JLE_fulltext.html | 109376 | 034512f32f31e8483b95e83dfbd16973e6f459ebeabe970e62497fa723d81f87 |
| 36779245 | PMID36779245_Oliver2023_PMC_2026-09-27.xml | 180365 | 780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34 |
| 40126049 | PMID40126049_CerulliIrelli2025_PMC.xml | 128252 | 4f9434222213ea63e33d4c953cd914213084b4ce260214f79cd8aa25fd6e1438 |
| 40126049 | PMID40126049_CerulliIrelli2025_supplement/EPI-66-2253-s001.pdf | 355581 | 324b37e3c39b179c5e4d1b60c3ee34f49a992a1fca6517f4a55d416e22dcd8db |

Acquired 2026-11-06 into the auditor's scratchpad (`audit_A1b/dl/`, outside the repository):

| PMID | Route | Bytes | sha256 |
|---|---|---|---|
| 30061856 | Europe PMC REST fullTextXML, PMC6054992 | 96907 | e6f629eeac644299ebfd3a23fb763009f79623b0bf025947c2270dae53eced8c |
| 41442931 | NCBI efetch PubMed XML (abstract; no PMC record) | 8295 | a95cc93cf84b76928950244195627ad27b8e541c1367cbb149c61868e5163baa |
| 31929713 | Europe PMC REST fullTextXML, PMC6942552 | 14496 | f50efab70799889743d1ed3028619b0bc3e12869a2006d0892d60a9bb521bd89 |
| 23740534 | NCBI efetch PubMed XML (abstract) | 51756 | 4ba629c260f7ac04e16116ef21d5005387c6bc8bfd9de316f9a5701894e58f21 |
| 24225340 | Europe PMC REST fullTextXML, PMC4225757 | 88082 | 47acdd695e979bf673163d5db1c3057278589f14eb4cedcd2b2f16b162c74d35 |
| 42190144 | NCBI efetch PubMed XML (abstract; no PMC record) | 31096 | 8a8916a1e47d71f4e7c8b1e2f74c01506b7f8eb53891a384c6c66dfffe21f2ca |

Derived working texts (not artefacts of record): `PMID30361190_pdftotext_raw.txt`
a5fbfcae808789e4300bec19015484472167274f6a8fced10efbfa9dd251f557; `PMID40126049_supp_pdftotext_layout.txt`
6e11a88dd1690ca9b7c455283db62c8f6c22ce750f0615ff31d75f56fb91b4db. Tag-stripped dumps of each XML/HTML
were used for reading; verdicts were checked against the originals named above.

No e-mail address or contact parameter was sent to any service. No bot check was met.

## What could not be reached

- PMID 23740534 (Hancock 2013): Europe PMC `PMC11194850/fullTextXML` returned HTTP 500 twice
  (2026-11-06 12:11 and 12:13 UTC). Not needed: the audited quote is in the PubMed abstract.
- PMID 41442931 and 42190144: abstract only, by design of the task; no PMC record exists for either.
- PMID 36537114: only the delivered Scholar Gateway chunks exist locally; the per-patient narratives
  for patients 1-4 are not on that surface. Rows A1-04 to A1-07 were judged on the delivered surface,
  as the rows themselves declare.
- PMIDs 28721938, 29808465, 38407561, 42735667 are named in the brief but no triple cites them; they
  were not opened.

## Files

- `audit_A1b.tsv` — 33 rows, 8 columns (triple_id, source_id, verdict, quote_found_as,
  artefact_route, artefact_sha256, justification_max40_words, governing_passage_pointer).
- `audit_A1b_README.md` — this file.
