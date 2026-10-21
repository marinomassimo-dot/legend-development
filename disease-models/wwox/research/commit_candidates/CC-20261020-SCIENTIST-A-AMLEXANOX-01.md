# COMMIT CANDIDATE — CC-20261020-SCIENTIST-A-AMLEXANOX-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-a`, drug-repurposing P3 known-roads reconnaissance, task
`REPURP-P3-KNOWNROADS-A-20261020`, branch `task/REPURP-P3-KNOWNROADS-A-20261020`.
**target_wm_version:** `WM_v7.22_2026-10-20` (whatever `state_manifest_current.md` carries at
propagation; this candidate changes no working-model block).
**Change class:** **MINOR** — two registry identity records and one dismissal-ledger record. **No
claim status changes, no claim summary changes, no working-model block changes, and no baseline claim
is narrowed or reversed.** A blind locator audit is therefore not required and was not run; the
locator triples are persisted in the two manifests and are available for one.
**Not medical advice.** Class level only. 🔴 **Both papers are NOT WWOX EVIDENCE: neither mentions
WWOX, neither contains a WWOX measurement, and neither carries a WWOX patient.** They are earned
nulls for the gene: they bound what may be *said* about the amlexanox road and assert nothing about
WWOX biology.

---

## 1 · Target and need

The operator's roadmap lists amlexanox among the known therapeutic roads, flagged `DA_APPROFONDIRE`.
The repository held **no scientific record of the molecule at all**: `registry_records.py get --theme
amlexanox` returns **0 records** across all seven registry surfaces, and the only occurrences of the
string in the checkout are in the Harness-owned `drug_repurposing/` directory and in this task's own
contract JSON. So the first need is identity records for the two papers that define the road, and the
second is a **negative** — the kind this repository treats as the dangerous direction if it is left
unwritten, because the next session would otherwise re-triage the same abstracts hopefully.

Full reconnaissance, with the four outcome classes kept apart:
[`repurposing_known_roads_20261020_scientist-a.md`](../repurposing_known_roads_20261020_scientist-a.md) § 4.

---

## 2 · Two PAPER / LIT identity records (provisional numbers left to the integrator)

| PMID | Short title | Source type | Model | Transferability | Role (one line) | Receipt |
|---|---|---|---|---|---|---|
| 22938201 | Gonzalez-Hilarion 2012, amlexanox rescues nonsense mutations | primary, human cell lines | lung-cancer, Duchenne myocyte and CF airway lines, all **nonsense** alleles, all **non-neural** | T4 | The originating claim: amlexanox is the single confirmed hit of a >1200-drug NMD-inhibitor screen and yields some full-length protein; the full-length species can be the minor one and the dual mechanism is declared unresolved in the paper itself | FTR-20261020-22938201-01 |
| 40544182 | Hristodor 2025, read-through drugs in Fanconi anaemia | primary, patient-derived cells | FA lymphoblastoid lines and primary fibroblasts, nonsense alleles | T4 | The independent, comparator-controlled test: amlexanox raised full-length protein in one gene and not the other, did **not** relieve NMD, and **did not improve survival under genotoxic challenge, chromosomal aberrations or micronuclei** while the comparator did | FTR-20261020-40544182-01 |

Both read `partial_fulltext_read` (figures `captions_only`, supplements not fetched — declared debts).
Manifests `deepdive_manifests/PMID22938201.json` (11 locators) and `PMID40544182.json` (9 locators),
both `MANIFEST STRICT PASS`, 0 gaps, exact text match verified against the fingerprinted artefacts.
Reference-list integrity `SCREENED_CLEAN` for both (snapshot 2026-09-10).

---

## 3 · One dismissal-ledger record (next free `DIS-` number to the integrator)

### «Amlexanox is a qualified therapeutic road for WOREE / WWOX-DEE» → ⏸️ **NOT ESTABLISHED — not tested in any WWOX system, and its phenotype-rescue arm is negative where it has been tested with a comparator**

- **`PREMISE: DATO + INFERENZA`** (2026-10-20, `scientist-a`, `context_policy: SOURCE_FIRST`, two
  first reads). **Sources:** PMID 22938201 (`FTR-20261020-22938201-01`), PMID 40544182
  (`FTR-20261020-40544182-01`); neither mentions WWOX.
- **What is rejected is a transfer, not either result.** Each paper is a valid measurement of its own
  protocol.
- **The WWOX side is empty, and it is `NON_TROVATO_NELLA_RICERCA`, never `MAI_TENTATO`.**
  **Queries:** `amlexanox AND WWOX` = 0; `WWOX AND (ataluren OR readthrough OR "nonsense suppression"
  OR gentamicin OR PTC124 OR "ELX-02")` = 0. **Sources:** PubMed ESearch; all seven LEGEND registry
  surfaces via `registry_records.py --theme`; the whole working tree. **Date:** 2026-10-20.
  **Limits:** a PubMed zero on a drug name reaches title/abstract space and not Methods (**`D-25`**:
  the reagent miss rate in this gene has been 100%); the WWOX Foundation's reported individual
  experience is **not formally published** and so is unreachable by any literature query by
  construction; a conference poster abstract may never enter PubMed; and per **`D-18`** a
  selector-based zero is untrustworthy until the selector matches more than zero somewhere — it
  matches 17 records on amlexanox read-through, so the instrument reads.
- 🔴 **The structural reason no amount of amlexanox data can bear on the missense allele.**
  Read-through requires a premature termination codon. `p.(Gln230Pro)` is a **missense** substitution
  with normal transcript level and protein not detected: **there is nothing to read through**, at any
  exposure, by any agent. Every other pharmacological action of the molecule — NMD inhibition,
  TBK1/IKKε inhibition, anti-inflammatory activity — is a **separate hypothesis requiring its own
  evidence**, and none has been tested in a WWOX system. The nonsense alleles the repository does hold
  are a different, **unenumerated** class: there is no count of WWOX PTC alleles and no PTC-context
  annotation (stop-codon identity, +4 nucleotide), and no published cohort separates nonsense from
  splice from frameshift from CNV.
- 🔴 **And where it HAS been tested against a comparator, the protein gain did not become a phenotype
  gain.** In patient-derived cells: *«On the contrary, we observed no effect on FANCF protein levels
  following amlexanox treatment in these cells»*; *«neither amlexanox nor ataluren was able to rescue
  FANCA transcription»*; and *«Conversely, amlexanox showed no effect on either MMC- or DEB-induced
  genotoxicity in FA-A cells, despite a slight increase in FANCA protein synthesis and a significant
  reduction of initial p53 levels»*. The authors' own general statement is the one that matters here:
  *«a partial downregulation of p53 per se is not sufficient to produce phenotypic rescue in human
  cells»*, and their own methodological demand is the gate — *«the need for a reliable experimental
  pipeline to assess whether the minimal amount of neomorphic protein synthesized upon translational
  read-through is actually followed by phenotypic rescue»*. The effect they could attribute was
  pSTAT2 down about 50 %, which they ascribe to **TBK1/IKKε inhibition and not to read-through**.
  ⚠️ Scope: the amlexanox arms are the paper's smallest (n = 3 on the genotoxicity endpoints), the
  group's standing programme is the comparator (a declared directional interest), the systems are
  lymphoblastoid and dermal and never neural, and the supplement was not fetched.
- **`PREMISE_TAG` this record exists to expose:** 🔴 *«more full-length protein means restored
  function»* · `PREMISE: DEFAULT_FROM_TEXTBOOK`. It belongs beside the existing
  `DEFAULTS THAT BIT US` row *«stabilizing a protein restores its function»* (**`D-04`**) and the
  WWOX-internal instance of the same error class, `P282A` — **stable and completely inert**. It is a
  research target, not a foundation. **Candidate new row for that table is proposed in § 4.**
- 🔴 **Two inferences explicitly refused here:** no paediatric suitability and no systemic
  availability may be inferred from historic authorisations for other indications or other routes.
  The 2012 paper's own safety sentence — *«used for more than 30 years per os or topically to treat
  asthma and aphthous ulcers»* — is exactly that inference; it is recorded as the source's statement
  and **not adopted**. That paper contains no paediatric datum, no CNS datum and no pharmacokinetic
  measurement of any kind.
- **Confine, stated so this record cannot be over-read:** this does **not** say amlexanox is inert,
  and it does **not** close the nonsense-allele class as a therapeutic target. It says the molecule
  has never been tested in a WWOX system, that read-through is not a mechanism for a missense
  substitution, and that in the one comparator-controlled study its protein gain produced no
  phenotypic rescue.
- **`REVIVAL_TRIGGER`** — any one of: (a) amlexanox, or any read-through agent, administered to a
  WWOX-deficient system (cell, organoid or animal) with a WWOX protein **and** a WWOX-dependent
  functional readout; (b) a formally published protocol or case report of the reported individual
  experience, carrying variant, endpoint, exposure, concomitant therapy and follow-up; (c) a
  demonstration that amlexanox produces functional rescue — not protein quantity — at a WWOX PTC
  allele in any system; (d) an enumeration of WWOX PTC alleles with stop-codon identity and the +4
  nucleotide, which would at least make the eligible class countable.
- **Re-audit hook:** rejection of a **therapeutic transfer**. Re-examine on any new `DATO` about
  nonsense-allele rescue in WWOX, about NMD in a WWOX allele, or about TBK1/IKKε in a WWOX system.

---

## 4 · Proposed `DEFAULTS THAT BIT US` row (allocation to the integrator)

> ⚠️ Per the ledger's own allocator note, the next id is `max(D-nn) + 1`, **never** the last row's
> number; `D-17` stays reserved and `D-27`–`D-30` are not minted. The integrator allocates.

| "Obvious" default | Why it is FALSE here | Cost |
|---|---|---|
| *a read-through or NMD-inhibiting drug that restores full-length protein restores the phenotype* | 🔴 **Measured false in the one study that ran a comparator in the same patient-derived cells**: amlexanox raised full-length FANCA to about 9 % of healthy control and reduced p53 by about 40 %, and produced **no** improvement in survival under mitomycin C, **no** reduction of diepoxybutane-induced chromosomal aberrations and **no** significant reduction of micronuclei, while ataluren did all three. Its measured action was attributed by the authors to **TBK1/IKKε inhibition, not read-through**. The authors state the general form themselves: *«a partial downregulation of p53 per se is not sufficient to produce phenotypic rescue in human cells»*. And in the originating paper the full-length species can be the **minor** one — *«a truncated p53 protein was well detected»* against *«a very low level of full-length p53»* — while the only quantitative function measurement lands at *«about 20% of the CFTR activity … measured in Calu-3 cells»*, a comparator the authors themselves say over-expresses the protein | A whole therapeutic road was about to be weighted on protein-quantity data. **Detection rule: for any restoration lever — read-through, NMD inhibition, chaperone, boost or gene addition — ask for the FUNCTION endpoint in the same breath as the abundance endpoint, and ask it of the same cells. Abundance without function is half a result, and in this gene the inert half is already documented (`P282A`: stable and completely inert).** It is `D-04` seen from the pharmacological side |

---

## 5 · Discovery-ledger proposals

**None.** This candidate deliberately produces no molecule lead. The reconnaissance's own verdict is
that amlexanox is **a road to qualify, not a candidate to promote**, and a discovery lead would be a
promotion by filing. The one experimental observation worth a lead was found elsewhere in the census
(the untested genotype-specificity contrast of § 2.3 of the analysis note) and is left to the
Orchestrator rather than staged here, because it belongs to a reading this task did not make.

---

## 6 · What must NOT be inferred from this candidate

- Not that amlexanox is unsafe: no safety assessment is made or implied, in any population.
- Not that amlexanox is inert: it has measured activity in two non-WWOX systems.
- Not that the nonsense-allele class is closed: it is **unenumerated**, which is a different state.
- Not anything about `p.(Gln230Pro)` beyond the mechanical point that a missense substitution has no
  premature termination codon to read through.
- Not a dose, not a route, not a schedule — none is reproduced anywhere in this candidate, including
  for the cell-culture work.

**Not medical advice.**


---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_008`

Propagated by `BATCH_20261019_008` (2026-10-21, MINOR, `WM_v7.26` -> `WM_v7.27`; integrator ACTOR_ID `orchestrator` by stated assumption, task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation).

- **Landed:** `PAPER 427` (PMID 22938201) and `PAPER 428` (PMID 40544182) in the paper registry, with `LIT-0699` and `LIT-0700` in the literature log — both graded **T4, NOT WWOX EVIDENCE**, `clinical relevance` BACKGROUND, `Claim links: none`. `DIS-41` in the dismissal ledger, verbatim from § 3, with the WWOX side marked `NON_TROVATO_NELLA_RICERCA` and its queries, sources and date intact — never `MAI_TENTATO`. The § 4 row is allocated **`D-39`** (`max(D-nn) + 1`; `D-38` was the maximum present) and landed verbatim in `DEFAULTS THAT BIT US`.
- **Preserved, because they are the load-bearing points:** the independent comparator-controlled test relieved **no** NMD and improved **neither** survival under genotoxic challenge, **nor** chromosomal aberrations, **nor** micronuclei while the comparator improved all three, and the action it could attribute was ascribed by those authors to **TBK1/IKKε inhibition rather than read-through**; and read-through requires a premature termination codon, which the Q230P missense substitution does not have. **Protein quantity does not prove function.**
- **No claim created, none reversed, no `Status`, `Type` or `Summary` changed.** No discovery lead was filed (§ 5 asked for none). No dose, route or schedule was reproduced in any landed record.
- **No discrepancy: the candidate's locator counts are correct** [corrected 2026-10-21 by `BATCH_20261019_009`, replacing «One measured discrepancy, reported not repaired: the candidate's § 2 declares 11 and 9 persisted locators; the two manifests on disk carry 6 each. The registry records state the measured count.»]. The manifests carry **11** and **9** entries, exactly as § 2 declares. The batch-008 integrator's re-measurement sized the `verbatim_locators` wrapper object instead of its `entries` array and so reported the number of schema keys, 6, for both files; `PAPER 427` and `PAPER 428` are repaired at source and the error is recorded as `D-40`. **The candidate was right and the integrator was wrong.**
