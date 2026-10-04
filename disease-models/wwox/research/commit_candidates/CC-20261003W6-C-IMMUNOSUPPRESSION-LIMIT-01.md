# COMMIT CANDIDATE — CC-20261003W6-C-IMMUNOSUPPRESSION-LIMIT-01 — "immunosuppression bounds the sensory-ganglion risk of a CSF-route AAV dose" is REJECTED on the sources read

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist C of intake wave 6, 2026-10-03.
**Change class:** **MINOR.** It appends one dismissal-ledger negative and one discovery-ledger
method lead. It narrows no `consolidated baseline` claim and reverses none — there is no claim in
this repository that immunosuppression bounds AAV ganglion risk, which is exactly why the negative
is worth recording before one appears.
`context_policy: SOURCE_FIRST`
**Not medical advice.**

---

## 1 · The proposition being rejected

> *Immunosuppression bounds the dorsal-root-ganglion risk of a CSF-route AAV dose, so a programme
> that immunosuppresses can treat that risk as addressed.*

This is a natural inference from the field's own language — DRG findings are described as
inflammatory, mononuclear infiltration is their defining feature, and immunosuppression is
routinely co-administered. It is **not supported** by anything read in this wave, and two sources
contradict it directly.

## 2 · The premises, each sourced

1. **Full immunosuppression did not prevent the infiltrate.** In the GLP primate arm of PMID
   36951961, every animal received i.v. methylprednisolone from day 1 to termination (10 mg/kg on
   day 1, then 1 mg/kg/day) **and** rapamycin 0.01 mg/kg twice daily from twelve days before
   dosing. Under that regimen the T-cell ELISpot was null — and minimal mononuclear cell
   infiltration was present in the lumbar DRG of **every dosed animal, at both dose levels**,
   against none in the vehicle animals.
2. **Three different regimens failed on the liver endpoint.** In PMID 37515322, prednisolone with
   intravenous or intrathecal dosing, and rituximab plus everolimus with intrathecal dosing, did
   not prevent the transaminase elevations or the microscopic findings. Prednisolone did prevent
   periportal CD3+ infiltration at 6 weeks and reduce hepatocyte ADAR1 — and those differences had
   disappeared by 26 weeks.
3. **Nor did B-cell depletion move the humoral response.** Same source: peripheral B-cell
   depletion was achieved, splenic cellularity fell, and anti-AAV9 titres were unchanged.
4. **The field's own strongest statement is weaker than the proposition, and is a citation.** PMID
   42422766 says only that immunosuppression "can greatly reduce but not eliminate" the severity
   and/or incidence of these findings — and that sentence cites the authors' unpublished data, not
   a measurement in that paper.
5. **The apparent positive evidence is confounded.** PMID 41078870, which ran under weekly
   methylprednisolone, found DRG degeneration in 1 of 11 dosed animals despite sacral-DRG
   transgene positivity in 31–80% of neurons; PMID 42422766, which used none, found adverse
   findings at every dose. That contrast is suggestive and it is **not** a controlled comparison:
   the two differ in cassette, promoter, dose, group size, timepoint and reporting depth, and
   neither contains an unmedicated arm of its own.

## 3 · What IS supported instead

Immunosuppression demonstrably suppresses the readouts it is aimed at — the hepatic T-cell
infiltrate and the measurable T-cell response — and the endpoint that moved with **dose** under a
constant regimen was neuronal degeneration, not infiltration (PMID 36951961: 100% at the high dose
in both sexes, 0% at the low dose). The defensible statement is therefore about **which dial moves
which endpoint**, and it is carried by `CC-20261003W6-C-DRG-ATTRIBUTION-01`, not here.

## 4 · The reading hazard this uncovered, and why it belongs in the ledger

PMID 41078870 states in its abstract, its results and its discussion that intracisterna-magna
delivery "was well tolerated with no significant toxicity" and that "ICM delivery is safe with all
of these AAVs". **Every animal in both of its studies was under weekly systemic
methylprednisolone**, and that fact appears in exactly one sentence of Methods and is restated
nowhere. A reader taking the abstract, or taking the discussion, acquires a tolerability claim
stripped of its single most important condition.

This is a general hazard, not a complaint about one paper: a nonclinical safety statement must be
read against the Methods that produced it, and a corticosteroid regimen is part of the dose.

## 5 · Ops (provisional; anchors and next-free ids re-measured at commit time)

### 5.1 · `disease-models/wwox/research/dismissal_ledger_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `DIS-C-20261003w6 — "Immunosuppression bounds the DRG risk of a CSF-route AAV dose" — REJECTED on the sources read` |
| body | The proposition of §1, the five premises of §2 each with its PMID, and the statement of §3 about what is supported instead. |
| revival trigger | A primate study, at a fixed dose and cassette, that compares an immunosuppressed arm against a concurrent unmedicated arm and reports graded DRG histopathology for both — i.e. the controlled comparison none of these six contains. A second, weaker trigger: publication of the unpublished data that PMID 42422766's "greatly reduce but not eliminate" sentence cites. |
| tag | `DATO` for the premises, `INFERENZA` for the rejection |

### 5.2 · `disease-models/wwox/research/discovery_ledger_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `DL-METH-118 — A nonclinical tolerability statement is not readable without its Methods: read the immunosuppression regimen before carrying the safety sentence` |
| status | `open` |
| tag | `DATO` |
| body | The worked example of §4 (PMID 41078870), with the general rule: before carrying any "well tolerated / no significant toxicity" sentence out of a nonclinical AAV paper, locate and record (i) the immunosuppression regimen and its duration, (ii) whether animals were pre-screened for neutralising antibodies, (iii) the group size and the number of dose levels, and (iv) whether the pathology was graded per animal or summarised in prose. Record each as present or absent — an absent one is a finding, as PMID 40301740's silence on immunosuppression is. |
| why it compounds | This repository will read many more nonclinical packages. The four checks above are cheap, mechanical, and in this wave of six papers they changed the reading of two of them. |

## 6 · Verification items before propagation

1. Confirm the artefacts and sha256 of PMID 36951961, 37515322, 41078870 and 42422766
   (`deepdive_manifest.py --verify-artifacts` returned PASS for all four at commit `d66d642168b6`).
2. Confirm that no claim asserting the rejected proposition has landed from another branch in the
   meantime; if one has, this candidate's change class becomes **MAJOR** and it must be re-filed
   with the claim id named.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (The primate arm was under a corticosteroid from day 1 to termination | all animals received i.v. methylprednisolone starting on day 1 until the study termination | PMID 36951961, Results, GLP NHP study design paragraph)
- (Under that regimen every dosed animal still had a lumbar sensory-ganglion infiltrate | there were minimal mononuclear cell infiltrates in lumbar DRG in all AAV9/AP4M1-dosed animals | PMID 36951961, Results, rat-and-NHP DRG comparison section)
- (The regimen did abolish the measurable T-cell response, with the condition stated | the AAV9/AP4M1 vector did not generate a detectable T cell immune response to either AAV9 or the human AP4M1 protein in WT NHPs under the immunosuppressant protocol | PMID 36951961, Results, NHP ELISpot paragraph)
- (Neither a corticosteroid nor B-cell depletion with an mTOR inhibitor prevented the injury after intrathecal dosing | Co-administration of prednisolone (1 mg/kg) or rituximab plus everolimus with scAAV9-CBA-SMN1 did not prevent the increase in transaminases | PMID 37515322, Results, impact-of-immunosuppression section)
- (B-cell depletion did not move the antibody response | No pronounced difference in anti-AAV9 antibody response existed with co-administration of prednisolone | PMID 37515322, Results, Immunogenicity against AAV9)
- (The field's strongest claim for immunosuppression says reduce, not eliminate, and is a citation to unpublished data | data from our group suggest that immunosuppression can greatly reduce but not eliminate the severity and/or incidence of DRG, spinal cord, and other adverse histopathology findings | PMID 42422766, Discussion, comparison-with-PR001 paragraph)
- (The study whose safety statement omits its own regimen states that regimen only in Methods | For immunosuppression, methylprednisolone acetate (Depo-medrol, Pfizer, 20 mg/mL or 40 mg/mL) was administered intramuscularly to the femoral or gluteal muscle weekly | PMID 41078870, Materials and methods, ICM administration and CSF collection)
- (And under it the ganglion pathology was almost absent despite uniformly high transgene positivity | Neuronal degeneration and necrosis with the presence of mononuclear cell infiltrate was detected only in a sacral DRG of one animal of the AAV5-treated group | PMID 41078870, Results, Toxicity endpoints)

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED — MERGED into DIS-031
**Batch:** `BATCH_20261003_005` · 2026-10-03 · ACTOR_ID `scientist` (Scientist J, batch integrator), under the operator's standing authorisation *«procedi sempre»*
**Operations applied:** 2
**Change class as judged by the batch:** MINOR (§7) — every target's live `Status` was read from the registry before judging.

**Deduplication verdict: same proposition family, disjoint sources, so one record and not two.** `DIS-031` already rejects *«AAV DRG toxicity is immune-mediated and can be prevented prophylactically»* on PMIDs 41404412 / 35331006 / 36700120; this candidate rejects the preventability side on PMIDs 36951961 / 37515322 / 41078870 / 42422766. Following the `DIS-033` precedent of `BATCH_20261003_004`, the negative was **merged into `DIS-031`** as its wave-6 arm, carrying all five premises and a second revival trigger, rather than written as `DIS-035`. Its discovery-ledger lead landed separately as `DL-METH-120`, **renumbered** from the provisional `DL-METH-118`, which `BATCH_20261003_004` had taken for a different proposition. 🔴 **Two blind-audit CONTRADICTED verdicts corrected premise 4:** the field's *«can greatly reduce but not eliminate»* sentence does **not** cite unpublished data — its reference 42 is a published article (Grubor 2025, doi 10.1016/j.omtm.2025.101643) — and it is not that paper's only immunosuppression statement. Only *reduce rather than eliminate* survives from that premise; the published source is now `FT-193`, HIGH priority. Premise 1's «abolished the measurable T-cell response» was also narrowed: the source says no response was *detectable* under the regimen and has no unsuppressed comparator arm.

**Nothing above this line was rewritten.**
