# COMMIT CANDIDATE — CC-20261003W6-C-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist C of intake wave 6, 2026-10-03.
**Change class:** **MINOR.** It creates registry presence for six papers that have none. It
narrows no claim, reverses none, and changes no claim status.
`context_policy: SOURCE_FIRST`
**Not medical advice.**

---

## 0 · Why this exists

Six receipts are prepared for PMIDs with **no record in any registry surface**
(`registry_records.py get --pmid N`, commit `d66d642168b6`: no match in claim_registry,
discovery_ledger, dismissal_ledger, full_text_queue, literature_tracking_log, paper_registry or
working_model). Appending those receipts without a landing produces `ORPHAN_COMPLETE_READ` in LINT
and blocks `BATCH_COMMIT`. Every PMID this scientist handled therefore gets a structured landing
below: a `PAPER` record **and** a `LIT` record, in the same section, with the PMID present in both.

**Yes — every one of the six needs both records.** None existed before this wave.

## 1 · Numbers are provisional

Measured with `registry_records.py catalog` at commit `d66d642168b6`: highest existing
`PAPER 150`, highest existing `LIT-0443`. Next-free therefore **PAPER 151** and **LIT-0444**.
Other branches land continuously, so the integrator **re-measures and renumbers** before
propagation. The pairing of PMID to record content is what matters here, not the integer.

## 2 · Ops — `disease-models/wwox/registries/paper_registry_current.md`

Op for every row: `append` (new record), at the end of the registry's record list.

| provisional id | PMID | record text (one line per field) |
|---|---|---|
| `PAPER 151` | 37515322 | **Title:** Liver injury in cynomolgus monkeys following intravenous and intrathecal scAAV9 gene therapy delivery · **Year:** 2023 · **Journal:** Molecular Therapy · **DOI:** 10.1016/j.ymthe.2023.07.020 · **PMCID:** PMC10556189 · **WWOX content:** none — the string WWOX occurs zero times · **Why held:** nonclinical AAV9 safety primary; the liver arm of the CSF-route dose question; the primary behind reference 10 of PMID 41257285 · **Reading:** `FTR-20261003-37515322-01`, `partial_fulltext_read` · **Dossier:** `disease-models/wwox/research/fulltext_dossiers/PMID37515322.md` |
| `PAPER 152` | 42422766 | **Title:** Intra-CNS AAV9-GBA1 delivery yields species and route of administration differences in safety and transgene expression · **Year:** 2026 · **Journal:** Molecular Therapy Advances · **DOI:** 10.1016/j.omta.2026.201779 · **PMCID:** PMC13343144 · **WWOX content:** none (zero occurrences) · **Why held:** the route-versus-toxicity contrast in one cargo; adverse DRG/cord findings at every intracisterna-magna dose level with no immunosuppression and no antibody screen · **Reading:** `FTR-20261003-42422766-01`, `partial_fulltext_read` · **Dossier:** `.../fulltext_dossiers/PMID42422766.md` |
| `PAPER 153` | 41078870 | **Title:** Biodistribution of AAV1, AAV5, AAV9, and AAVDJ serotypes after intra-cisterna magna delivery in non-human primates · **Year:** 2025 · **Journal:** Molecular Therapy — Methods & Clinical Development · **DOI:** 10.1016/j.omtm.2025.101593 · **PMCID:** PMC12509745 · **WWOX content:** none (zero occurrences) · **Why held:** capsid held against a fixed CSF route; and the worked example of a tolerability statement made under a Methods-only systemic corticosteroid regimen · **Reading:** `FTR-20261003-41078870-01`, `partial_fulltext_read` · **Dossier:** `.../fulltext_dossiers/PMID41078870.md` |
| `PAPER 154` | 42157962 | **Title:** Development of a secretable frataxin for enhanced efficacy in treating Friedreich's Ataxia · **Year:** 2026 (PubMed 2025) · **Journal:** Molecular Therapy Advances · **DOI:** 10.1016/j.omta.2025.201661 · **PMCID:** PMC13182795 · **WWOX content:** none (zero occurrences) · **Why held:** the one design in the corpus that lowers vector burden rather than tolerating it; and the fold-of-endogenous dose window with a measured upper bound · **Reading:** `FTR-20261003-42157962-01`, `partial_fulltext_read` · **Dossier:** `.../fulltext_dossiers/PMID42157962.md` |
| `PAPER 155` | 36951961 | **Title:** Intrathecal AAV9/AP4M1 gene therapy for hereditary spastic paraplegia 50 shows safety and efficacy in preclinical studies · **Year:** 2023 · **Journal:** The Journal of Clinical Investigation · **DOI:** 10.1172/JCI164575 · **PMCID:** PMC10178841 · **WWOX content:** none (zero occurrences) · **Why held:** the recessive-null, intrathecal, IND-directed architecture closest to a WWOX programme, and the only graded per-animal lumbar-DRG incidence table in this corpus · **Reading:** `FTR-20261003-36951961-01`, `partial_fulltext_read` · **Dossier:** `.../fulltext_dossiers/PMID36951961.md` |
| `PAPER 156` | 40301740 | **Title:** Preclinical evaluation of AAV9-coSMN1 gene therapy for spinal muscular atrophy: efficacy and safety in mouse models and non-human primates · **Year:** 2025 · **Journal:** Molecular Medicine · **DOI:** 10.1186/s10020-025-01207-4 · **PMCID:** PMC12042585 · **WWOX content:** none (zero occurrences) · **Why held:** the group's only DRG-negative primate study, and its weakest reporting; carries an unresolved contradiction between its Results text and its own Figure 7 legend · **Reading:** `FTR-20261003-40301740-01`, `partial_fulltext_read` · **Dossier:** `.../fulltext_dossiers/PMID40301740.md` |

## 3 · Ops — `disease-models/wwox/registries/literature_tracking_log_current.md`

Op for every row: `append` (new record).

| provisional id | PMID | record text |
|---|---|---|
| `LIT-0444` | 37515322 | Intake wave 6, 2026-10-03, Scientist C. Status `read — partial`. **Off-WWOX by measurement** (zero occurrences), held as a transferable AAV-safety primary. Receipt `FTR-20261003-37515322-01`. Manifest `.../deepdive_manifests/PMID37515322.json` (VERDICT PASS). Registry twin: `PAPER 151`. |
| `LIT-0445` | 42422766 | Intake wave 6, 2026-10-03, Scientist C. Status `read — partial`. Off-WWOX by measurement. Receipt `FTR-20261003-42422766-01`. Manifest `.../PMID42422766.json` (PASS). Registry twin: `PAPER 152`. Note: no PMIDs in its reference list, so the multi-hop enumeration is by `<ref>` count (55). |
| `LIT-0446` | 41078870 | Intake wave 6, 2026-10-03, Scientist C. Status `read — partial`. Off-WWOX by measurement. Receipt `FTR-20261003-41078870-01`. Manifest `.../PMID41078870.json` (PASS). Registry twin: `PAPER 153`. Note: Tables 1–3 re-extracted cell-wise. |
| `LIT-0447` | 42157962 | Intake wave 6, 2026-10-03, Scientist C. Status `read — partial`. Off-WWOX by measurement. Receipt `FTR-20261003-42157962-01`. Manifest `.../PMID42157962.json` (PASS). Registry twin: `PAPER 154`. |
| `LIT-0448` | 36951961 | Intake wave 6, 2026-10-03, Scientist C. Status `read — partial`. Off-WWOX by measurement. Receipt `FTR-20261003-36951961-01`. Manifest `.../PMID36951961.json` (PASS, two artefacts). Registry twin: `PAPER 155`. Note: Table 1 has no JATS body and was read as its rendered image, persisted as `files/fulltext/PMID36951961_Chen2023_T1.jpg`. One "Comment in" recorded by PubMed. |
| `LIT-0449` | 40301740 | Intake wave 6, 2026-10-03, Scientist C. Status `read — partial`. Off-WWOX by measurement. Receipt `FTR-20261003-40301740-01`. Manifest `.../PMID40301740.json` (PASS). Registry twin: `PAPER 156`. Note: Tables 1–2 have no JATS body and were not fetched. |

## 4 · Verification before propagation

1. Re-run `registry_records.py catalog`; renumber if `PAPER 150` / `LIT-0443` have moved.
2. Append the six receipts in event-ID order **before or with** this candidate, so that neither a
   record without a reading nor a reading without a record exists at any committed state.
3. Run `legend_lint.py .` and confirm no `ORPHAN_COMPLETE_READ` for any of the six.

### LOCATOR TRIPLES FOR BLIND AUDIT

*(None. This candidate asserts no fact about any source: it creates registry presence. The facts it
summarises are audited through `CC-20261003W6-C-DRG-ATTRIBUTION-01` and
`CC-20261003W6-C-IMMUNOSUPPRESSION-LIMIT-01`.)*
