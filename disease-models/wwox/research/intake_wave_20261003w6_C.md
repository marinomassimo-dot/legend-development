# Intake wave 6 — 2026-10-03 — Scientist C

- `context_policy: SOURCE_FIRST`
- ACTOR_ID `scientist`, acting as Scientist C of intake wave 6, branch `task/sci-C-20261003w6`.
- Assigned set: PMID 37515322, 42422766, 41078870, 42157962, 36951961, 40301740 — six AAV
  gene-therapy nonclinical papers, **none of which mentions WWOX**.
- **Nothing here is medical advice.** Every datum below is carried with its transfer limit.

## The assigned question

> What does each source add to, or limit in, the claim that dorsal-root-ganglion (DRG) injury and
> the systemic toxicity of a CSF-route AAV9 dose can be bounded and *modified* before the first
> patient — which part is dose-driven, which is immune-driven and therefore addressable by
> immunosuppression or by neonatal tolerisation, and which part is route-driven — and for each,
> is it measured in a mouse, an NHP or a human?

---

## 0 · The earned null, stated once

The literal string `WWOX` occurs **zero times** in all six artefacts (measured by iterating the
whole JATS tree of each). That is an earned null for the gene, not a failure of the reading. Every
sentence below is a transferable statement from another gene or another indication, and each
carries its transfer limit. Nothing in this wave touches a WWOX claim directly.

## 1 · Verdicts

| # | PMID | Verdict | One line |
|---|---|---|---|
| C1 | 37515322 | **INGEST** | The liver arm of the question, answered: after a CSF route the injury needs a transducing, expressing genome, and no immunosuppressive regimen tested prevented it. |
| C2 | 42422766 | **INGEST** | The route arm, answered against interest by the sponsor: intracisterna-magna dosing produced adverse DRG, cord and nerve findings **at every dose level including the lowest**, with no measurable brain benefit, in animals with no immunosuppression and no antibody screen. |
| C3 | 41078870 | **INGEST** | Capsid is not a lever on where a CSF route puts the vector — and the study's own "well tolerated" was earned under weekly systemic methylprednisolone that the abstract, results and discussion never mention. |
| C4 | 42157962 | **INGEST** | A design built to lower vector burden still left minimal-to-mild DRG degeneration; and it supplies the one dose language that transfers between genes — fold-of-endogenous with a measured upper bound. |
| C5 | 36951961 | **INGEST** | The decisive source of the group: under full corticosteroid + mTOR immunosuppression, **100% of dosed primates still had a lumbar DRG infiltrate**, while neuronal degeneration appeared only at the top dose. |
| C6 | 40301740 | **INGEST (weak)** | The group's only DRG-negative primate study, and the most thinly reported: one dose, one timepoint, H&E only, no nerve conduction, and a figure legend that contradicts its own text. |

All six were first readings: `paper_packet.py packet --pmid N` at commit `663970aa07f1` returned
`manifest: none`, `prior read: depth=none · receipts=0` and `no route recorded` for every one, and
`registry_records.py` matched no record. No retraction, expression of concern or erratum on any of
the six (NCBI ESummary, 2026-10-03); PMID 36951961 carries one "Comment in".

## 2 · The answer, split into the three parts the question names

### 2a · What is DOSE-driven

| Evidence | Species | What it fixes |
|---|---|---|
| C5: lumbar-DRG **neuronal degeneration** 100% at 1.68 × 10^14 vg/NHP in both sexes and **0%** at 8.40 × 10^13 vg/NHP, under identical immunosuppression; the degeneration at the top dose had a functional correlate (fall in sural nerve conduction velocity and amplitude at days 45 and 77) and the peroneal nerve was spared | NHP (n = 2 per cohort) | A **dose step between infiltrate and cell loss**. This is the cleanest dose–response in the group because the immune variable is held constant across it. |
| C1: ~2 × 10^14 vg/kg IV killed every treated animal by day 7–8, while 1.1 × 10^14 vg/kg IV produced only asymptomatic enzyme changes; and within the lethal arm the two animals given the lowest total dose were least affected | NHP | A **steep systemic dose step**, roughly two-fold, between asymptomatic and lethal. |
| C6: raising the mouse dose from 8.0 × 10^13 to 1.6 × 10^14 vg/kg bought no further efficacy, and CNS transgene protein saturated between 5.8 × 10^13 and 1.9 × 10^14 vg/kg | mouse | An **efficacy ceiling below the safety ceiling** — i.e. the top of the useful dose range is set by saturation, not by toxicity. |
| C1: liver injury tracked hepatocellular vector load, and "the affected hepatocytes were not necessarily the cells expressing the transgene at the highest expression concentrations" | NHP | The dose variable that matters for the liver is **vector load**, not peak transgene. |

### 2b · What is IMMUNE-driven — and whether immunosuppression addresses it

The answer this wave produces is sharper than "immunosuppression helps a bit", and it is the
wave's main result:

| Evidence | Regimen | Outcome |
|---|---|---|
| C5, NHP arm | i.v. methylprednisolone 10 mg/kg day 1 then 1 mg/kg/day to termination **plus** rapamycin 0.01 mg/kg b.d. from day −12 | T-cell ELISpot null — and **every dosed animal still had minimal mononuclear cell infiltration in lumbar DRG at both dose levels** (0% in vehicle). |
| C1, IT arm | prednisolone 1 mg/kg; or rituximab 20 mg/kg + everolimus 0.5 mg/kg b.d. | Neither "prevent[ed] the increase in transaminases"; microscopic findings unchanged; anti-AAV9 titres unchanged despite achieved B-cell depletion. |
| C1, IV arm | prednisolone 1 mg/kg | ALT, platelet and monocyte changes **not** prevented; CRP/albumin/platelet/ALT changes marginally mitigated; periportal CD3+ infiltration and hepatocyte ADAR1 **were** suppressed at 6 weeks — and all differences had vanished by 26 weeks. |
| C3, both studies | methylprednisolone acetate weekly, from 5 days pre-dose through day 24 (study 1) or day 87 (study 2) | DRG degeneration in **1 of 11** dosed animals, despite sacral-DRG transgene positivity of 31–80% of neurons in 9 of 9 study-2 animals. |
| C2 | **none**, and no neutralising-antibody screen | Adverse DRG, trigeminal, cord, cauda equina, nerve-root and peripheral-nerve findings **at every dose level**. |

**Reading of that table.** Immunosuppression demonstrably suppresses the parts of the response it
is aimed at — the T-cell infiltrate in liver (C1), the measurable T-cell response (C5) — and
demonstrably does **not** abolish either the liver injury (C1) or the sensory-ganglion infiltrate
(C5). The C3-versus-C2 contrast is suggestive in the other direction (steroid cover, 1/11 with
DRG pathology; no cover, findings at every dose) but it is **confounded** by cassette, promoter,
dose, timepoint, group size and reporting depth, so it is recorded here as `INFERENZA`, not as a
measurement. The only place the immune variable is held constant while dose moves is C5, and there
the infiltrate does not move with dose while the neuronal loss does. The most defensible split
this wave supports is: **the infiltrate is the immune-flavoured, partly suppressible part, and the
neuron loss is the dose-driven part that immunosuppression did not reach.**

C2 also shows how easily this gets overstated: its only sentence about immunosuppression —
"immunosuppression can greatly reduce but not eliminate the severity and/or incidence of DRG,
spinal cord, and other adverse histopathology findings" — is a **citation to the authors'
unpublished data**, not a measurement in that paper. Anyone carrying it must carry it as a cited
assertion.

### 2c · Neonatal tolerisation

**Not measured anywhere in this group.** C2 contains the only neonatal arm — P0 intracerebro-
ventricular injection in mice, which was clean — but the authors themselves refuse the inference:
age is confounded with species in their design, and they write that a direct early-postnatal
versus young-adult **NHP** comparison "would be valuable", i.e. has not been done. No source read
here tolerises, and none measures DRG pathology after neonatal dosing in a primate. The brief's
pointer to the neonatal-tolerisation primary (PMID 31017018) remains unpaid: it is blocked at the
publisher, as waves 5 and 6 both confirmed.

### 2d · What is ROUTE-driven

| Evidence | Species | What it fixes |
|---|---|---|
| C2: intracisterna magna gave spinal cord and DRG transgene RNA up to ~10^6 with adverse DRG/cord findings and **no significant GCase change in any brain region**; intraparenchymal gave brain expression and no AAV-related DRG toxicity, but adverse brain findings and early euthanasia of a whole high-dose group | NHP | Route **relocates** the harm; it does not remove it. |
| C3: after ICM, spinal cord/DRG/trigeminal/olfactory ~10^5–10^7 VG/µg; deep brain ~10^4 VG/µg, below one copy per cell; no transgene immunoreactivity in substantia nigra or striatum for **any** of four capsids | NHP | The sensory-ganglion load is a property of the **CSF route**, not of the capsid. |
| C4: intra-CSF versus i.v. in the same capsid — 25× more cerebellar dentate, 62× more DRG, 10× less heart; intra-CSF cut cardiac biodistribution by ~90% | NHP | Route is the strongest single instrument on the biodistribution **ratio**, and it buys CNS reach by buying DRG exposure. |
| C1: median liver 721 vg/dg after IV versus 19 vg/dg after IT, with injury at day 3–4 after IV and ~2 weeks after IT | NHP | Route sets both the **magnitude and the timing** of the hepatic exposure. |

### 2e · Measured in a human: almost nothing

Only two human facts appear anywhere in the six. C1 cites the clinical record: ~90% of patients in
the onasemnogene trials had at least one abnormal liver function test despite prophylactic
immunosuppression, three deaths from liver failure in a high-dose systemic trial for another
indication, and hepatomegaly / transaminase rises in two patients of an intrathecal cohort. C2
cites the single human report of symptoms attributed to DRG toxicity after intrathecal AAV — in an
ALS patient, transient tingling and reduced sensory nerve potentials — and says it cannot be
definitively attributed. **Every histological statement in this entire group is animal.** There is
no human DRG histology anywhere in the set.

## 3 · The named debt: Hudry 2023 (PMID 37515322) behind reference 10 of PMID 41257285

The debt is **paid**: 37515322 was acquired lawfully, read first-hand and receipted
(`FTR-20261003-37515322-01`, prepared, not appended).

**Which carried claims now have a primary behind them, and does the wording hold?**

`registry_records.py get --pmid 41257285` and `--pmid 37515322` were run at commit `d66d642168b6`.
**Neither PMID has any record in any of the seven surfaces searched** (claim_registry,
discovery_ledger, dismissal_ledger, full_text_queue, literature_tracking_log, paper_registry,
working_model). So the honest answer is:

- **No registry statement in this repository currently rests on reference 10 of PMID 41257285**,
  because PMID 41257285 itself has no record here. The debt the brief named is a debt of the
  *selection record*, not of the registry.
- What the primary does do is **supply a source for a claim the repository has been making
  without one** in its research layer: `CC-20261003W3-C-RESTORATION-SPEC-01` lists "DRG toxicity is
  an AAV class effect" and "transient liver-enzyme rises in every arm" as transferable lessons
  resting on a single STXBP1 paper (PMID 40349107). After this reading, the liver half of that has
  a GLP-grade, 146-animal, six-study primary behind it, and the wording **holds with one
  correction**: the liver injury after a CSF route is not a capsid effect but requires a
  transducing, expressing genome, which the empty-capsid and promoterless arms establish directly.
  That correction is proposed as `CC-20261003W6-C-DRG-ATTRIBUTION-01`.
- **This is a negative finding reported as such, per §B1:** the brief's framing ("say which carried
  claims now have a primary behind them") presupposes carried claims that, measured against the
  registries, do not exist. Searched surfaces and commit are named above so the search can be
  contested.

## 4 · Against the waves 3–5 records (read only after the first pass was written)

Read after the dossiers were complete: `CC-20261003W3-C-RESTORATION-SPEC-01` (the restoration
spec, with its window row and its off-target-organ-risk row) and `CC-20261002-WWOX-DOSE-CEILING-01`.
Wave 4 and wave 5 records are **not on `main`** at commit `d66d642168b6` and could not be read;
that is stated rather than worked around.

| Prior record | What this wave ADDS | What it BOUNDS | What it leaves UNTOUCHED |
|---|---|---|---|
| `CC-...W3-C-RESTORATION-SPEC-01`, **window row** ("no therapeutic window has been measured for any of these genes") | Nothing that changes it — and a fifth and sixth independent confirmation. C5 measures age in mice only (P7–P10 beats P90) and never in primates; C2's only early arm is a mouse arm with species confounded. | The statement can now be made **stronger and more specific**: in the primate, where the toxicity is measured, *no source in this corpus has dosed a neonate at all*. The window is unmeasured in exactly the species where the risk is measured. | The negative `DIS-C-20261003w3` stands; its revival trigger (expression matched across ages, efficacy still falling) is not met by anything here. |
| same record, **off-target organ risk row** (DRG toxicity as an AAV class effect, resting on PMID 40349107) | Four further independent primate datasets, three positive and one negative, plus the first **graded, per-animal incidence table** in this repository (C5 Table 1, read at panel level). | Bounds the class-effect wording in three ways: (i) it is a **CSF-route** effect, not an AAV effect — C4 measures 62-fold less DRG exposure by the i.v. route and C2 finds no AAV-related DRG toxicity after intraparenchymal dosing; (ii) **capsid is not the variable** — C3 finds no serotype difference across four capsids at a fixed route; (iii) it is **not universal** — C6 reports a clean primate DRG at 4.67 × 10^13 vg/animal. | The usefulness of a DRG-detargeting element (the PMID 40349107 contribution) is untouched; indeed C5 cites the miRNA-binding-site experiment as the field's own discriminating result. Serum NfL as a toxicity biomarker is untouched — **none** of these six measured it. |
| same record, **dose row** ("the highest dose was not the best dose") | C6 adds a third gene with the same shape: efficacy and CNS protein both saturated below the top dose tested. | — | — |
| same record, **PD-assay row** ("nothing WWOX-specific exists") | C4 adds the dose language the repository lacks: a therapeutic window stated as **fold-of-endogenous** (60%–900%, with >20-fold measured as harmful), which is assay-anchored rather than vector-anchored. | — | The absence of a WWOX PD assay is untouched and is, if anything, more acute: without one, neither the floor nor the ceiling can be stated in these units. |
| `CC-20261002-WWOX-DOSE-CEILING-01` ("raising WWOX can do harm or fail to help; none in a neuron-targeted vector setting") | Nothing WWOX-specific. What this wave adds is the **general form** of that ceiling in a vector setting: C4 measures an over-expression ceiling for another gene and designs to stay under it; C6 measures a saturation ceiling; C1 shows the expressing genome, not the capsid, is the hazard. | — | The WWOX-specific gap stands: no source here raises WWOX in any system. |

## 5 · What would change the model if true, and what would falsify it

- **If true and consequential:** that the DRG infiltrate and the DRG neuron loss are separable, the
  first partly immune and the second dose-driven (the C5 table). If that separation holds, a
  WWOX-directed CSF-route programme would have two independent dials — immunosuppression for the
  infiltrate, dose for the loss — rather than one, and the planning dose would be set by the
  neuron-loss threshold, not by the infiltrate.
- **What falsifies it:** a primate study, under a constant immunosuppressive regimen, in which
  **neuronal degeneration incidence does not change with dose** while infiltrate does; or an
  immunosuppressed-versus-not comparison at a single fixed dose in which the infiltrate rate is
  unchanged. Neither exists in this corpus. C6 is the nearest live threat to the whole picture: if
  its clean DRG at 4.67 × 10^13 vg/animal survives a graded re-reading of its own panels, then the
  "class effect" statement is a cassette-and-promoter statement, not a route statement.
- **What would settle C6 cheaply:** its Figure 7 panels, which were not inspected here, and whose
  legend ("minor detectable sign of toxicity") disagrees with its running text.

## 6 · Things in the brief / selection record that were wrong

1. **C6 is described as "Mouse only".** It is not. PMID 40301740 contains a GLP **cynomolgus**
   intrathecal study with DRG and spinal-cord histology at day 91 (8 treated, 4 control), and that
   primate arm is the only DRG-negative evidence in the whole group — i.e. the member the selection
   record called "deliberately the weakest, drop it first" carries the single most load-bearing
   counterexample in the set.
2. **C3 is described as "four serotypes, one ICM procedure".** It is two separate studies (1 month:
   AAVDJ vs AAV9, n = 2 each; 3 months: AAV1 vs AAV5 vs AAV9, n = 3 each), male-only, and — the
   fact the selection record could not know from the abstract — **run under weekly systemic
   methylprednisolone**. Its "well tolerated, no significant toxicity" is a weak safety claim for a
   reason the selection record did not state.
3. **C1 is described as "the immunosuppression primary"** in a way that reads as prednisolone and
   rituximab/everolimus failing to prevent hepatotoxicity "despite reducing T-cell infiltrate".
   Accurate for the IV arm. For the **IT** arm the paper reports no such T-cell reduction, and the
   CD3 result that is reported belongs to the IV arm at 6 weeks and is gone by 26 weeks.
4. **C2's "early postnatal ICV in mice, the neonatal arm"** is accurate, but it is not a neonatal
   *tolerisation* arm and the authors explicitly decline the age inference. Reading it as the
   neonatal evidence for the question would be the error.
5. **The named debt framing** assumed carried claims behind reference 10 of PMID 41257285; neither
   PMID has a registry record here (§3).

## 7 · Receipts prepared (NOT appended)

| PMID | File | event_id | depth |
|---|---|---|---|
| 37515322 | `scratchpad/receipts_pending_w6/sciC_37515322_1.json` | `FTR-20261003-37515322-01` | `partial_fulltext_read` |
| 42422766 | `scratchpad/receipts_pending_w6/sciC_42422766_1.json` | `FTR-20261003-42422766-01` | `partial_fulltext_read` |
| 41078870 | `scratchpad/receipts_pending_w6/sciC_41078870_1.json` | `FTR-20261003-41078870-01` | `partial_fulltext_read` |
| 42157962 | `scratchpad/receipts_pending_w6/sciC_42157962_1.json` | `FTR-20261003-42157962-01` | `partial_fulltext_read` |
| 36951961 | `scratchpad/receipts_pending_w6/sciC_36951961_1.json` | `FTR-20261003-36951961-01` | `partial_fulltext_read` |
| 40301740 | `scratchpad/receipts_pending_w6/sciC_40301740_1.json` | `FTR-20261003-40301740-01` | `partial_fulltext_read` |

Every one is `partial_fulltext_read`, not `complete_fulltext_read`, and the reason is stated rather
than hidden: **figure panels were not inspected and no supplement was fetched** for any of the six.
Where that mattered it is said in the dossier — C6's unresolved text-versus-legend contradiction is
exactly the cost of not opening the panels. The one panel that a carried number lives in **was**
opened: C5's Table 1, which has no body in the JATS and was fetched as its rendered image.

All six dry-recorded cleanly against a throwaway copy of the ledger **and** of the state manifest
(`fulltext_receipts.py --ledger <copy> --manifest <copy> record`), each returning `RECORDED`. The
real ledger is untouched: `fulltext_receipts.py verify` → `OK: 320 chained receipt(s), tail
anchored`.

## 8 · Acquisition record

All six by the same route, first attempt, no cascade needed:
`GET https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`, HTTP 200.

| PMID | Artefact | bytes | sha256 |
|---|---|---|---|
| 37515322 | `files/fulltext/PMID37515322_Hudry2023_PMC.xml` | 134 828 | `0a1aad3f4c79db6901e5059081d0bcf84818424e207913415c722a56343d8b1b` |
| 42422766 | `files/fulltext/PMID42422766_Amaral2026_PMC.xml` | 167 418 | `a24c49a3dbeb13351bb982237236ec664826d4d170b017422ef557634e37212c` |
| 41078870 | `files/fulltext/PMID41078870_Okai2025_PMC.xml` | 184 534 | `4d34f140c8e0af6bc1cd89521b2deb22c7776ec73088f174bc4cb4f1127be53f` |
| 42157962 | `files/fulltext/PMID42157962_DuBreuil2026_PMC.xml` | 184 095 | `f7ca88cabaa0804066a51a6328a2b8dc5697d80515bdf032cc6643565adbaeb4` |
| 36951961 | `files/fulltext/PMID36951961_Chen2023_PMC.xml` | 149 046 | `6f2f5bfc5d0d3f5339e894cb3840f8369b801d73ba6cc25843822beefbb6d958` |
| 40301740 | `files/fulltext/PMID40301740_Ma2025_PMC.xml` | 88 943 | `f6c49665c008763ee025e6f6672cae62244cb5f4448384161212ff64c1c5f8b7` |

One further artefact, and the acquisition lesson of this group:

| PMID | Artefact | bytes | sha256 |
|---|---|---|---|
| 36951961 | `files/fulltext/PMID36951961_Chen2023_T1.jpg` | 57 392 | `71e5f6ee0a711354ad7d88e869b8e72948e75cdec5096958457ae0e3a4fff597` |

**Lesson for wave 7.** Three of the six papers declare a `<table-wrap>` whose JATS carries **no
table body** — the table exists only as a served image (C5 Table 1; C6 Tables 1 and 2). A reader
who takes the JATS as the article silently loses those tables, and in C5's case the lost table is
the single most informative object in the paper. The working route is
`https://pmc.ncbi.nlm.nih.gov/articles/instance/<numeric PMCID>/bin/<graphic href>`; the
`europepmc.org/articles/<PMCID>/bin/...` route returns **HTTP 403** and the
`ncbi.nlm.nih.gov/pmc/articles/...` route returns **404**.

## 9 · Commit candidates produced

| id | class | what it changes |
|---|---|---|
| `CC-20261003W6-C-REGISTRY-01` | MINOR | A structured registry landing for each of the six PMIDs, so no `ORPHAN_COMPLETE_READ` is created when the receipts are appended. |
| `CC-20261003W6-C-DRG-ATTRIBUTION-01` | MINOR | One research-line record splitting the CSF-route harm into its dose-driven, immune-flavoured and route-driven parts across six primate datasets, with the species of each measurement. |
| `CC-20261003W6-C-IMMUNOSUPPRESSION-LIMIT-01` | MINOR | One dismissal-ledger negative — "immunosuppression bounds the sensory-ganglion risk of a CSF-route AAV dose" — rejected on the sources read, plus the reading hazard that produced it. |

## 10 · DEFAULTS_TAKEN

1. **Candidate file naming `CC-20261003W6-...` (upper-case W6).** The dispatch line says `W6`, the
   brief's correction 8 says `w6`. Took the dispatch spelling, which also matches the wave-3 files
   already on disk (`CC-20261003W3-...`). The integrator may rename; nothing depends on the case.
2. **`partial_fulltext_read` for all six** rather than opening every figure panel of six papers.
   The brief forbids claiming a complete read over captions-only sections, and the cost of the
   default is named in §5 (C6's unresolved contradiction).
3. **Supplements not fetched** for any of the six. Each dossier says which supplement would settle
   which statement.
4. **Dependency integrity screened for all six** (`dependency_integrity.py screen --manifest-block`)
   rather than waived, since the manifest validator requires the full block once `dependencies` is
   declared at all. All six: `SCREENED_CLEAN`, 0 flagged.
5. **Registry ids provisional**: PAPER 151–156, LIT-0444–0449, measured by `registry_records.py
   catalog` at commit `d66d642168b6`. The integrator renumbers.

## 11 · DECISIONS_TAKEN

1. **Recorded the C3 steroid cover as a finding, not a footnote.** A safety conclusion stated in
   abstract, results and discussion without restating a Methods-only systemic corticosteroid
   regimen is a reading hazard this repository will meet again, so it is written into the
   dossier, the manifest weighting and a candidate rather than left in a reading note.
2. **Refused to resolve the C6 text-versus-legend contradiction.** Resolving it requires the
   panels, which were not opened; it is recorded as an open contradiction instead of adjudicated.
3. **Classed the C2-versus-C3 immunosuppression contrast as `INFERENZA`**, not as a measurement:
   the two differ in cassette, promoter, dose, timepoint, group size and reporting depth.
4. **Fetched one table as an image.** C5's Table 1 carries the only graded per-animal DRG
   incidences in the group and has no JATS body; reading it changed the answer to the assigned
   question, from "immunosuppression reduces DRG findings" to "it did not prevent the infiltrate
   in a single animal, while dose moved the neuron loss".

## 12 · STOP_LOG

| # | Event |
|---|---|
| 1 | **A safety classifier halted the session's first response**, mid-turn, while the Group C assignment and the standing brief were in context. Per brief rules 13 and 21 the content was **not reworded and not retried**; the work continued through scripts and tool calls, and nothing below depends on re-running it. No other call was stopped. |
| 2 | `europepmc.org/articles/PMC10178841/bin/jci-133-164575-g056.jpg` → HTTP 403 (5 569-byte HTML). Not retried in the same form; the PMC article-instance route succeeded. |
| 3 | `ncbi.nlm.nih.gov/pmc/articles/PMC10178841/bin/...` → HTTP 404. |
| 4 | PubMed ESearch rate-limited two author-count queries; re-run with a one-second delay. |
| 5 | No class-3 stop: no question was left open that had a default. |
