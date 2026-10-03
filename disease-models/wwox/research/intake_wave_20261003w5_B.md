context_policy: SOURCE_FIRST

# Intake wave 5 (2026-10-03) — Scientist B: is the published WWOX-DEE patient record an independently counted series?

**Actor:** ACTOR_ID `scientist` (Scientist B), branch `task/sci-B-20261003w5`. **Not medical advice.** Class-level only: allele class × zygosity × phenotype band; no names, places, sample identifiers or parent-of-origin are carried.

**Method.** First pass from the six sources, written down before any registry record, claim or ledger lead was opened; registry and held-source comparison afterwards. Every patient was checked against held sources by allele pair, sex, onset, course and outcome, using only what the papers print. The wave-3 L239R rule (same allele, same centre, no cross-citation → never two independent replications) and the wave-4 Tarta-Arsene rule (source-level match → one patient) were applied after the first pass, as was the I136V boundary rule (attribution unproven → not counted as WWOX-DEE).

## Papers

| PMID | Source | Verdict | Depth / receipt file | New patients to the held record |
|---|---|---|---|---|
| 35792847 | Al Baradie 2022, 9 homozygous patients, 6 families | **INGEST** | complete · `receipts_pending_w5/sciB_35792847_1.json` | **7** (possibly 6); family 2 is probably the R54* sibship of `PAPER 119` |
| 31618474 | Burgess 2019, EIMFS cohort of 135 | **INGEST** (re-read; prior coverage inadequate) | complete · `sciB_31618474_1.json` | **0** — its WWOX patient is patient 6 of `PAPER 018`, stated there |
| 35715422 | Yang 2022, EIMFS cohort of 36 | **INGEST** (guardrail) | complete · `sciB_35715422_1.json` | **0** as WWOX-DEE — the one carrier has a pathogenic ATP7A second diagnosis |
| 33919646 | Spagnoli 2021, systematic review | **INGEST** (secondary) | complete · `sciB_33919646_1.json` | **0** — re-describes Piard patients 1, 2, 3, 4, 9, 11 |
| 32214227 | Hengel 2020, family exome cohort | **INGEST** (re-read; prior coverage inadequate) | complete · `sciB_32214227_1.json` | **0** — the WWOX family is Mallaret 2014 family 2 |
| 31353122 | Mori 2019, 16q deletion case report | **INGEST** (negative control) | **partial** (figures not inspected) · `sciB_31353122_1.json` | **0** — heterozygous CNV carrier, not a WWOX-DEE case |

Dossiers: `research/fulltext_dossiers/PMID<pmid>.md`. Manifests: `research/deepdive_manifests/PMID<pmid>.json` (all six STRICT PASS, 0 gaps, artefacts verified).

## Answer to the assigned question

**The published WWOX-DEE record is not an independently counted series, and this group adds measurable evidence of it.** Of the patients these six sources describe, the held record gains **seven at most** (all from 35792847); every other WWOX patient in the group is a re-description:

1. **Stated by later authors (DATO):** the 2019 EIMFS patient is patient 6 of the 2023 WWOX-DEE cohort, which says so; that cohort, not the 2019 paper, supplies the RNA result (intron-4 deletion → exon 5 skipping).
2. **Source-level match without cross-citation (INFERENZA, strong):** the R54* sibship of the 2022 series is the R54* sibship of Ehaideb 2018 — same allele pair, sexes, onset, sibship, dysmorphology, a word-for-word identical MRI sentence, and ages advanced by the same interval in both sibs.
3. **Pointer, not observation:** the 2020 exome cohort's WWOX family is the 2014 SCAR12 G372R family (its own supplement says so); the 2021 review's WWOX section is five or six patients of one 2019 cohort.
4. **Aggregations double-count:** the 2022 series' 70-patient table lists Tarta-Arsene 2017 and its re-description (Piard patient 8) as two rows, lists the Ehaideb children as literature patients beside their own re-description, and counts six SCAR12 patients as WOREE. **Its percentages are not a WOREE denominator.**
5. **Boundary cases not counted:** a WWOX carrier with a Menkes-compatible ATP7A frameshift (35715422); a heterozygous 57-gene deletion ending in WWOX with an exon-clean second allele (31353122); a Q230P-heterozygous affected sib whose second allele was not found (35792847).

**Does each primary say what the aggregating source said it said?** No, twice. (a) The 2021 review's "hypokinesia: 5" is the primary's "poor spontaneous movements" row; the primary's movement-disorder row for those children lists dystonia, myoclonus, startle, pedalling/boxing or "no" (`CC-20261003W5-B-HYPOKINESIA-01`, `DIS-031`). (b) The 2022 series' abstract claims genotype-phenotype correlations its body never computes.

**Limits.** One possible overlap stays open (a 2022 family-3 brother vs the one male of Tabarki 2015, whose primary is unread here); the R54* sibship identity is inferential; two DECIPHER carriers cited by 31353122 cannot be matched to literature patients from what is printed.

**What would change the model if true.** If the 2022 P47T homozygotes are confirmed as a WOREE/SCAR12 intermediate, the two syndromes are a severity continuum within an allele, not allele-defined — relevant to `DL-MECH-022`'s positioning logic (`CC-20261003W5-B-ALBARADIE-01`). **What would falsify the counting conclusions:** author statements that the 2022 family 2 is a different sibship; a Tabarki primary showing distinct patients (which would raise the new-patient count to 7 firmly).

## Answers to the per-paper selection notes (the selection record was tested as a hypothesis)

- **35792847.** "Overlap with the W44X family": **false** — no patient carries W44X; it appears only in the keywords and a reference title. The overlap that exists is with Ehaideb 2018 (R54*), which the selection did not name. "Optic atrophy asserted as part of the syndrome": the abstract's introductory sentence says so; in the series 4 of 9 have it, 2 do not fixate, 3 have none.
- **31618474.** "The patient appears to be new to this cohort": **false** — the 2023 cohort reports it as its patient 6. "Same recurrent allele as the held WOREE cohort's two carriers": correct for the allele, and one of those two carriers *is* this patient. "Predicted, not assayed": correct for this paper; the assay exists in the 2023 paper.
- **35715422.** "Two WWOX alleles … WWOX among genes of poor prognosis": both alleles are in **one** patient, who also carries a pathogenic ATP7A frameshift; the prognosis statement has a denominator of that one patient.
- **33919646.** "The hypokinetic-WWOX observation may rest on a single report": it rests on one report, and on a re-labelling of that report's descriptor.
- **32214227.** "Homozygous nonsense allele … ID, epilepsy, corpus callosum dysgenesis" is the **TMCO1** row, not WWOX; the WWOX row is homozygous G372R. "3 body WWOX hits" understates it: the gene sits in a table row and in the supplement.
- **31353122.** "19 pp" — the repository file has 15 pages. "The registry responds to this PMID only in the full-text queue appendix": `registry_records.py get --pmid 31353122` returns no record. "Other allele screened by panel, may miss deep-intronic or structural variation": correct, and stated in the dossier with what *was* examined.

## Registry statements now with a receipted primary behind them (reading-debt discharge)

- `DL-MECH-059` (Yang 2022, dual diagnosis guardrail): every DATO line re-verified at source; supported as worded. Pointer added by `CC-20261003W5-B-REGISTRY-01`.
- `FT-140`: its "overlap-confounded `p.(Glu17Lys)`" is resolved (toward `PAPER 018`, not the Piard series); the FT-116 triage's "zero WWOX variants" for 32214227 is corrected (`CC-20261003W5-B-PATIENT-OVERLAP-01`).
- `CLAIM 032`'s carrier paragraph: two heterozygous observations *with* a phenotype are added as non-data for haploinsufficiency (`CC-20261003W5-B-CNV-CARRIER-01`).
- The analysis note `analysis/ft116_cohort_triage_20260921.md` §5.3/§6.3 (suspected Burgess–Piard overlap) is superseded by the source-level finding above; it is not edited here (append-only analysis surface, another actor's file).

## Candidates

| Candidate | Class | Triples |
|---|---|---|
| `CC-20261003W5-B-PATIENT-OVERLAP-01` | MINOR | 13 |
| `CC-20261003W5-B-ALBARADIE-01` | MINOR | 6 |
| `CC-20261003W5-B-HYPOKINESIA-01` | MINOR | 8 |
| `CC-20261003W5-B-CNV-CARRIER-01` | MINOR | 8 |
| `CC-20261003W5-B-REGISTRY-01` | MINOR (PAPER 156-161, LIT-0445-0449, provisional) | 7 |

All op lists dry-ran with `record_scoped_edit.py apply` (exit 0); every triple's quote was re-matched against its artefact on disk.

## Defaults taken
1. Al Baradie: the publisher HTML full-text tab is the locator surface because every PDF text layer tried carries four C0 controls; the abstract tab is declared as a second structured surface (`supplement_text`, the only kind available), and abstract-only claims are carried in triples, not manifest locators.
2. Hengel Table S1: dumped in a TAB variant of the corpus xlsx extractor, because `D2=4` trips the verifier's chi-squared signature.
3. Mori: figures deliberately not viewed (Figure 1 is a patient photograph); the reading is declared `partial_fulltext_read` rather than overclaimed.
4. Spagnoli supplement: `pmc_pow_fetch.fetch` refuses `application/zip`; called with that MIME added from a scratch shim (capability gap, below).
5. Registry numbers taken after the highest claimed on main (`PAPER 156`+, `LIT-0445`+), declared provisional.

## Capability gap
`framework/scripts/pmc_pow_fetch.py` rejects `application/zip` supplements, the commonest MDPI/PMC supplement container; a one-line addition to its accepted MIME set would remove the shim. Not edited here (outside a Scientist's write scope).
