# COMMIT CANDIDATE — CC-20261019-SCIENTISTD-W4B-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), task `W4-W2B-D-20261019`, branch `task/W4-W2B-D-20261019`, 2026-10-20.
**context_policy:** `QUESTION_DRIVEN` for all eight readings (held: the selection file's reason per row; named per paper in `wave4_scientist-d.md`). **Not medical advice.** Class-level statements only; no individual-level record.
**target_wm_version:** `WM_v7.24` · **Change class:** MINOR (registry presence and reading entries for eight papers; no claim status, baseline claim or working-model block is touched; no registry claim op is proposed for the seven substitutes).

## 0 · Why

Wave 4, group W2, second half: the metabolic axes the repository had no record for (folate, biotin, branched-chain amino acids, carnitine, bone and calcium, bile acids, and the cofactor causes of DEE as a class). Eight papers were read in full (one duplicates scientist-c); seven are disease-class substitutes and contain no WWOX occurrence, so they carry no WWOX claim. One, Agarwala 2023, was listed as a substitute with no record but contains three WWOX case rows; for those rows it is a class-level WWOX-direct primary.

## 1 · Ops

None. The seven substitute readings carry no registry claim ops by construction. For Agarwala 2023 the integrator decides whether the three WWOX rows belong in the genotype-phenotype corpus; no op is written here because the rows carry no WWOX-specific outcome and the one citation they share with previously published cohort members needs the queue entry below resolved first.

## 2 · Registry presence proposed (placeholders; the integrator mints ids)

| Placeholder | PMID | Short title | Depth | Registry state found |
|---|---|---|---|---|
| W01 | 38978529 | Girgis 2024, cerebral folate transport deficiency, 2 cases (substitute) | complete (already read and staged by scientist-c; my duplicate manifest and receipt withdrawn) | scientist-c's record only |
| W02 | 34258135 | Papadopoulou 2021, FOLR1 siblings, ketogenic diet (substitute) | complete | no record |
| W03 | 42563882 | Lai 2025, biotinidase deficiency letter (substitute) | complete | no record |
| W04 | 42660645 | Ribeiro-Constante 2026, BCKDK deficiency review (substitute; bronze OA, all-rights-reserved notice) | complete | no record |
| W05 | 39543202 | Nassar 2024, L-carnitine with the ketogenic diet, trial (substitute) | complete | no record |
| W06 | 33406758 | Merlotti 2021, ketogenic diets and skeletal health (substitute) | complete | no record |
| W07 | 36619921 | Nóbrega 2022, cerebrotendinous xanthomatosis review (substitute) | complete | no record |
| W08 | 38074073 | Agarwala 2023, early-infantile DEE aetiologies; WWOX rows 7, 8 and 50 | complete | no record before this reading; WWOX-direct for three case rows |

Receipt event ids staged under `receipt_staging/scientist-d/`: `FTR-20261019-<PMID>-01` for seven (38978529 was staged by scientist-c after my peer check and my duplicate was withdrawn). Manifests: `deepdive_manifests/PMID<PMID>.json`, all seven PASS under `--artifact-workspace` on the shared checkout.

## 3 · Claim-level observations (all MINOR; none narrows or reverses a baseline claim)

- Liver steatosis, one-carbon, folate, biotin, carnitine, bile-acid and creatine axes stay "no WWOX evidence" in the working model; the seven substitute papers add no WWOX occurrence to change that.
- Agarwala 2023: WWOX appears in 3 of 80 recruited children (3.75 percent) and 3 of 53 molecular diagnoses (5.7 percent) of a single-centre early-infantile series; this is a referral-biased proportion, not an incidence, and it is a datum for any statement of how often WWOX loss presents as an early-infantile epileptic encephalopathy.
- A normal genetic evaluation did not exclude vitamin B6 responsiveness in three pyridoxine-dependent patients (class-level screening logic, not advice).

## 4 · Queue and reading entries proposed

| PMID | Item | Why | Route status |
|---|---|---|---|
| 33196034 | Surana 2020, infantile-spasms aetiology cohort (Indian setting) | cited by Agarwala 2023 Table 4 for the WWOX deletion row and for previously published cohort members; no record found | to be triaged (PubMed identity MATCH checked) |
| 30356099 | Piard 2019, WOREE cohort | cited for the c.790C>T rows; manifest exists in the repository | already read |

No parked papers: all eight were read from lawful open text (seven Europe PMC JATS or PMC page; one PMC page with an empty User-Agent; all figures opened as images).

## 5 · Staged leads (not appended to the discovery ledger); all `IPOTESI`

1. **Share of WWOX among early-infantile epileptic encephalopathy.** WWOX in about 4 percent of an unselected-by-gene series (3 of 80). Falsifier: other prospective, gene-agnostic EIDEE cohorts with a count well outside 1 to 8 percent.
2. **Exome-missed intragenic deletion.** A homozygous intragenic WWOX deletion was found by array in a case that the Methods route to array after sequencing-based testing (inference from Methods and Table 4). Falsifier: the cohort's exome copy-number output for that case.
3. **Normal early neuroimaging in WWOX encephalopathy.** One case with onset at 21 days and a normal neuroimaging entry. Falsifier: the primary report of this case or serial imaging.
4. **No WWOX-null amino-acid, folate, carnitine or bile-acid measurement exists.** The measurement that would turn any substitute axis into evidence is a plasma amino-acid panel, CSF 5-MTHF and an acylcarnitine profile in WWOX-null patients or models. Falsifier of "WWOX loss does not alter these axes": a measured abnormal value.

## 6 · Shared surfaces left to the Orchestrator

`pathograph`, `batch_queue`, `coverage_report` and `reading_state` not regenerated (commits carry `LEGEND_STALE_SURFACES_BECAUSE`). The four scientific current files, `full_text_queue_current.md` and the ledger are untouched.

### LOCATOR TRIPLES FOR BLIND AUDIT
Thirty load-bearing triples across the eight papers were audited blind by a separate agent: 24 SUPPORTED, 2 SUPPORTED with a note, 4 OVERSHOOT (three minor); all narrowings applied before commit; table in `wave4_scientist-d.md`, section "Blind audit".
