# COMMIT CANDIDATE — CC-20261003W6-C-DRG-ATTRIBUTION-01 — which part of the CSF-route harm is dose, which is immune, which is route

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist`, Scientist C of intake wave 6, 2026-10-03.
**Change class:** **MINOR.** It adds one research-line record and one discovery-ledger lead, both
in the research layer. It narrows no `consolidated baseline` claim and reverses none. It does,
however, **bound the wording** of a transferable lesson already recorded in
`CC-20261003W3-C-RESTORATION-SPEC-01` (off-target-organ-risk row), and that bounding is set out
explicitly in §3 so a reviewer can refuse it separately.
`context_policy: SOURCE_FIRST`
**Not medical advice.**

---

## 1 · Sources

| PMID | Receipt (prepared, not appended) | Manifest |
|---|---|---|
| 37515322 | `FTR-20261003-37515322-01` | `.../deepdive_manifests/PMID37515322.json` — PASS |
| 42422766 | `FTR-20261003-42422766-01` | `.../PMID42422766.json` — PASS |
| 41078870 | `FTR-20261003-41078870-01` | `.../PMID41078870.json` — PASS |
| 42157962 | `FTR-20261003-42157962-01` | `.../PMID42157962.json` — PASS |
| 36951961 | `FTR-20261003-36951961-01` | `.../PMID36951961.json` — PASS (two artefacts) |
| 40301740 | `FTR-20261003-40301740-01` | `.../PMID40301740.json` — PASS |

**None of the six mentions WWOX** (zero occurrences of the string in every artefact). Every
statement is a transferable lesson with its limit stated.

## 2 · The finding in one sentence

Across six primate datasets, the sensory-ganglion harm of a CSF-route AAV dose separates into a
**mononuclear infiltrate** that appeared at every dose level in every study that used no
immunosuppression *and* in every animal of the one study that used full immunosuppression, and a
**neuronal degeneration** that appeared only above a dose threshold — so dose and immune state are
acting on two different endpoints, and the lever that moves one is not the lever that moves the
other.

## 3 · What this bounds in the existing record

`CC-20261003W3-C-RESTORATION-SPEC-01` records, in its off-target-organ-risk row, that "DRG
toxicity is an **AAV class effect**, not an STXBP1 effect, so it transfers to any AAV CNS
programme including a WWOX one", resting on a single source (PMID 40349107). Three bounds follow
from this wave, each sourced:

1. **It is a CSF-ROUTE effect, not an AAV effect.** PMID 42157962 measures 62-fold lower DRG
   transduction by the intravenous route than by intracisterna magna with the **same capsid**, and
   PMID 42422766 reports no AAV-related DRG toxicity after intraparenchymal dosing while the ICM
   arm of the same study had adverse DRG findings at every dose.
2. **Capsid is not the variable.** PMID 41078870 holds the route and the cassette fixed across
   AAV1, AAV5, AAV9 and AAVDJ and declines to rank them; sacral-DRG neuron transgene positivity was
   31–80% of cells in all three AAV1 animals and in two of three AAV9 animals, with DRG pathology
   in one animal only.
3. **It is not universal.** PMID 40301740 reports a clean primate DRG at 4.67 × 10^13 vg/animal by
   the intrathecal route. That paper's own Figure 7 legend disagrees with its Results text, so the
   counterexample is recorded as **live but weak**, not as refuting.

What is **untouched**: the usefulness of a DRG-detargeting element and of serum NfL as a toxicity
biomarker, both from PMID 40349107. None of these six measured NfL; PMID 36951961 cites the
miRNA-binding-site experiment as the field's own discriminating result and does not repeat it.

## 4 · Ops (provisional; anchors and next-free ids re-measured at commit time)

### 4.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `RL-C-20261003w6 — The CSF-route AAV harm, split into its dose-driven, immune-flavoured and route-driven parts, with the species of each measurement` |
| status | `open` |
| tag | `INFERENZA` |
| body | The three-part table of §5 below, carried verbatim, with: (a) the explicit statement that **every histological datum in the set is animal** and that the only two human facts in it are the onasemnogene liver-test record and a single ALS patient's transient sensory symptoms after intrathecal AAV, neither of them histology; (b) the bounds of §3; (c) the statement that **neonatal tolerisation is measured nowhere in this set**, and that the one early-postnatal arm (PMID 42422766, P0 ICV in mice) confounds age with species by the authors' own admission; (d) the falsifiers of §6. |

### 4.2 · `disease-models/wwox/research/discovery_ledger_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `DL-THER-117 — Two endpoints, two dials: a CSF-route AAV programme may be able to treat the ganglion infiltrate and the ganglion neuron loss as separately controllable` |
| status | `open` |
| tag | `INFERENZA` |
| causal statement | In the one primate dataset where the immunosuppressive regimen is constant across two dose levels (PMID 36951961), the lumbar-DRG mononuclear infiltrate is 100% at both doses while neuronal degeneration is 100% at the higher and 0% at the lower — so, in that dataset, dose moves the neuron loss and does not move the infiltrate. |
| counter-evidence | PMID 40301740 reports neither endpoint at a dose between the two; PMID 41078870 reports neither in 10 of 11 animals under weekly corticosteroid; both have n small and reporting thin. The separation rests on four dosed animals in one study. |
| falsifier | A primate study under one constant regimen in which neuronal-degeneration incidence does **not** change with dose while infiltrate does; or a matched immunosuppressed-versus-not comparison at a single dose in which infiltrate incidence is unchanged. |
| transfer limit | Cynomolgus macaque; cargoes GBA1, FXN, AP4M1, SMN1, ASPA and EGFP, none of them WWOX; promoters from a weak synthetic (UsP) to CMV-enhancer/CBA; doses 1 × 10^13 – 1.68 × 10^14 vg per animal by lumbar intrathecal or intracisterna-magna routes. No WWOX construct exists, so no dose in these units transfers to one. |

## 5 · The table the record carries

| Part | Best measurement | Species | Transfer limit |
|---|---|---|---|
| **Dose-driven** | Lumbar-DRG neuronal degeneration 100% at 1.68 × 10^14 vg/NHP in both sexes, 0% at 8.40 × 10^13 vg/NHP, under identical immunosuppression; sural nerve conduction velocity and amplitude fell at the top dose, peroneal nerve spared (PMID 36951961) | NHP, n = 2 per cohort | Cassette- and promoter-specific; a self-complementary AAV9 under a deliberately weak promoter. Vector-genome numbers do not transfer between genes or capsids. |
| | Systemic lethality at ~2 × 10^14 vg/kg IV against asymptomatic enzyme changes at 1.1 × 10^14 vg/kg IV (PMID 37515322) | NHP | Liver endpoint, self or reporter transgene, IV route. |
| | Efficacy and CNS protein both saturating below the highest dose tested (PMID 40301740); an over-expression ceiling stated as >20-fold endogenous (PMID 42157962) | mouse; mouse + NHP | The **units** transfer (fold-of-endogenous); the numbers do not. |
| **Immune-flavoured, partly suppressible** | Prednisolone prevented periportal CD3+ infiltration and reduced hepatocyte ADAR1 at 6 weeks — and prevented neither the transaminase rise nor the microscopic findings; all differences gone by 26 weeks (PMID 37515322) | NHP | Liver, not ganglion. |
| | Methylprednisolone + rapamycin abolished the measurable T-cell response and left a lumbar-DRG infiltrate in **every** dosed animal (PMID 36951961) | NHP | Ganglion, one regimen, no unmedicated arm. |
| | Rituximab + everolimus depleted peripheral B cells and did not change anti-AAV9 titre or prevent the injury (PMID 37515322) | NHP | The humoral arm is not the lever for this endpoint. |
| **Route-driven** | ICM gave cord/DRG transgene RNA up to ~10^6 with adverse findings and no significant brain GCase change; intraparenchymal gave brain expression, no AAV-related DRG toxicity, and adverse **brain** findings with early euthanasia of a whole dose group (PMID 42422766) | NHP | Route relocates the harm rather than removing it. Secreted cargo. |
| | Same capsid, i.v. versus ICM: 62× less DRG, 25× less cerebellar dentate, 10× more heart (PMID 42157962) | NHP | The ratio transfers as a design fact; the fold-changes are capsid-specific. |
| | Four capsids, one ICM route, one dose: no significant biodistribution difference, deep brain below one copy per cell for all four (PMID 41078870) | NHP, male only | Capsid is not a lever on this route. Under weekly corticosteroid cover. |
| | Liver 721 vg/dg after IV versus 19 vg/dg after IT, injury at day 3–4 versus ~2 weeks (PMID 37515322) | NHP | Route sets hepatic magnitude and timing. |

## 6 · What falsifies the record

- The dose/immune separation falls if a primate study under one regimen shows neuronal-degeneration
  incidence flat across dose while infiltrate varies.
- The route attribution falls if an intraparenchymal or intravenous primate study at matched CNS
  exposure shows DRG pathology equal to a CSF route.
- The "not universal" bound strengthens into a refutation of the class-effect wording if PMID
  40301740's Figure 7 panels, graded, confirm a clean DRG at 4.67 × 10^13 vg/animal.

## 7 · Verification items before propagation

1. Confirm all six artefacts on disk with matching sha256 (`deepdive_manifest.py --verify-artifacts`
   returned PASS for all six at commit `d66d642168b6`).
2. Confirm the receipts are appended before this record cites them.
3. Confirm `CC-20261003W3-C-RESTORATION-SPEC-01` is still `PROPOSED` or has landed; if it landed,
   §3's bounds apply to the landed record and the op list must name it.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (After a CSF-route dose, the liver injury requires a transducing and expressing genome rather than the capsid alone | Those findings support the premise that the full vector is necessary in the transaminase activity elevations noted and that transduction and/or expression of transgenes may be involved in asymptomatic liver injury after IT administration of scAAV9 | PMID 37515322, Discussion, empty-capsid and promoterless-vector paragraph)
- (Neither a corticosteroid nor B-cell depletion with an mTOR inhibitor prevented the transaminase rise after intrathecal dosing | Co-administration of prednisolone (1 mg/kg) or rituximab plus everolimus with scAAV9-CBA-SMN1 did not prevent the increase in transaminases | PMID 37515322, Results, impact-of-immunosuppression section)
- (The correlate of hepatocyte death was vector load rather than peak transgene expression | the affected hepatocytes were not necessarily the cells expressing the transgene at the highest expression concentrations | PMID 37515322, Discussion, molecular-localisation paragraph)
- (After intracisterna-magna dosing the sensory-ganglion and cord findings were present at every dose level | AAV9-GBA1-related histopathology findings were present at all dose levels and affected the DRG, TG, spinal cord, cauda equina, dorsal nerve roots, and peripheral nerves | PMID 42422766, Results, distinct-safety-findings section, ICM paragraph)
- (Those animals received neither an antibody screen nor immunosuppression | we did not pre-screen for neutralizing antibodies or utilize immunosuppression in the reported results | PMID 42422766, Discussion, comparison-with-PR001 paragraph)
- (That study's only statement about immunosuppression is a citation to the authors' own unpublished data, and it says reduce rather than eliminate | data from our group suggest that immunosuppression can greatly reduce but not eliminate the severity and/or incidence of DRG, spinal cord, and other adverse histopathology findings | PMID 42422766, Discussion, final sentence of the same paragraph)
- (The CSF route bought no measurable brain effect in that study | no significant changes in GCase activity were detected in any brain region analyzed when compared with aCSF control animals | PMID 42422766, Results, IPa-but-not-ICM section)
- (Total vector per brain region does not explain the difference in harm between the species | suggest that the total amount of vector delivered to a brain region is not the primary driver, but perhaps species and/or route of administration | PMID 42422766, Discussion, second paragraph)
- (The four-capsid comparison declines to rank the capsids | these differences are not robust, and we could not conclude which AAV would be superior | PMID 41078870, Discussion, serotype-comparison paragraph)
- (No capsid reached the deep brain by that route | No HA immunoreactivity was detectable in deep brain region such as substantia nigra or striatum for any of the AAVs | PMID 41078870, Results, Immunohistochemistry section)
- (Sensory-ganglion pathology occurred in one animal only, despite uniformly high transgene positivity | Neuronal degeneration and necrosis with the presence of mononuclear cell infiltrate was detected only in a sacral DRG of one animal of the AAV5-treated group | PMID 41078870, Results, Toxicity endpoints)
- (Those authors refuse the transgene-load explanation on their own data | we conclude that there is no clear evidence linking the transgene overexpression/increased vector genome transduction to the DRG findings | PMID 41078870, Discussion, first paragraph)
- (A design built to lower vector burden still left sensory-ganglion degeneration while brain and cord were spared | Histopathology analysis revealed no evidence of neuronal degeneration in the brain or spinal cord and minimal to mild degeneration in the DRG | PMID 42157962, Results, extended 12-week NHP study paragraph)
- (There is a measured upper bound on transgene product expressed as fold-of-endogenous | levels exceeding 20-fold above normal can impair mitochondrial function | PMID 42157962, Discussion, over-expression paragraph)
- (Every dosed primate had a lumbar sensory-ganglion infiltrate under corticosteroid plus mTOR immunosuppression | there were minimal mononuclear cell infiltrates in lumbar DRG in all AAV9/AP4M1-dosed animals | PMID 36951961, Results, rat-and-NHP DRG comparison section)
- (The regimen did suppress what it was aimed at | the AAV9/AP4M1 vector did not generate a detectable T cell immune response to either AAV9 or the human AP4M1 protein in WT NHPs under the immunosuppressant protocol | PMID 36951961, Results, NHP ELISpot paragraph)
- (The histology acquired a functional correlate only at the top dose and only in the sensory modality | consistent with dose-dependent damage to sensory but not motor neurons | PMID 36951961, Discussion, toxicology-summary paragraph)
- (Silencing the transgene in the ganglion resolved the histopathology in the field's own discriminating experiment | incorporation of a miRNA binding site specific to DRG resolved this histopathology, suggesting that high transgene expression was driving the toxicity in DRG | PMID 36951961, Discussion, DRG-risk paragraph)
- (One primate intrathecal study reports no sensory-ganglion pathology at all | Hematoxylin and eosin (H&E) staining revealed no signs of inflammatory cell infiltration or neuronal necrosis in the treated monkeys | PMID 40301740, Results, intrathecal cynomolgus section)
- (That paper's own figure legend states something weaker than its running text | Representative pictures showing minor detectable sign of toxicity | PMID 40301740, Figure 7 legend)
- (More vector bought no further efficacy above a saturating dose | increasing the dose to 1.6E+14 vg/kg did not result in additional therapeutic benefit compared to the 8.0E+13 vg/kg group | PMID 40301740, Results, dose-dependent rescue section)
