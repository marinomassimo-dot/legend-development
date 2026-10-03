# CC-20261003W5-A-WINDOW-STATUS-01 — the wave-3 window negative survives six more sources, including the first human one, and gains two refinements

- `context_policy: SOURCE_FIRST` — first pass on all six sources was written before
  `CC-20261003W3-C-RESTORATION-SPEC-01` was opened; this candidate is the comparison that followed.
- Sources: PMID 39358605 (`FTR-20261003-39358605-01`), PMID 41712282 (`FTR-20261003-41712282-01`),
  PMID 40988338 (`FTR-20261003-40988338-01`), PMID 41314141 (`FTR-20261003-41314141-01`),
  PMID 41712149 (`FTR-20261003-41712149-01`), PMID 40809677 (`FTR-20261003-40809677-01`).
  All manifests validate (VERDICT: PASS). **None mentions WWOX.**
- Change class: **MINOR**. It does not narrow or reverse a `consolidated baseline` claim: it
  **corroborates** a negative that wave 3 proposed and that
  `CC-20261003W3-C-RESTORATION-SPEC-01` left DEFERRED, and it supplies the exact record text that
  deferral asked for.
- **Nothing here is medical advice.**

## What wave 3 proposed, and what this wave did to it

Wave 3 proposed `DIS-C-20261003w3`: *"A developmental window for WWOX restoration can be bounded
from the DEE gene-therapy literature"* → REJECTED, on the ground that the two results that look like
window results resolve to **delivery** and to **dose**. Its revival trigger was precise: *"a
published dosing study in which expression is matched across ages and efficacy still falls with
age."*

Six further sources, read without that text in hand, **meet the pattern and not the trigger**:

| Source | Looks like a window result | What it actually is |
|---|---|---|
| **PMID 41712282** (SLC13A5) | Benefit at P10 and at 3 months, but the neonatal arm is better | **Delivery.** At the *same dose and the same route*, cerebellar vector was 15.7×10^3 ± 3.1×10^3 vg per genome when dosed at P10 against 1.2×10^3 ± 7.4×10^2 at 3 months — about an order of magnitude. Changing the adult route to intracisterna magna recovered part of it (7.5×10^3). Expression is not matched; the trigger is not met |
| **PMID 39358605** (AP4B1) | Anatomical rescue neonatally, none in adults | **Dose and delivery.** The neonatal arm had 4×10^13 vg/kg; the adult dose-response ran at 2–5×10^12 vg/kg, about an order of magnitude lower. Expression is not matched; the trigger is not met |
| **PMID 40988338** (SYNGAP1) | Neonatal delivery fails behaviourally, juvenile succeeds | **Dose and distribution, stated by the authors.** The neonatal arm received only the lowest dose by a route giving forebrain-biased expression and reached ~70% of wild-type protein; the juvenile arms that worked used 3–10× more vector, achieved near-wild-type protein and brain-wide spread. Expression is not matched; the trigger is not met |
| **PMID 41314141** (CLN7, **human**) | "The timing of the intervention is likely to have a very large impact" | **An interpretation, not a measurement.** n = 4, open label, no natural-history comparator (the authors say so for imaging), no dose-response ("no noticeable difference is appreciated" between dose levels), no statistical testing at all, and no measurement of transgene expression in any patient. The first human source does not bound a window either |
| **PMID 41712149** (review) | Natural-history studies link early seizure burden to worse outcome; children dosed before two years acquire cognitive skills faster | **Association plus review-level clinical report.** Neither is an expression-matched age comparison, and the clinical figures are second-hand and sit inside the authors' declared sponsor relationships |
| **PMID 40809677** (Cas9) | Neonatal expression survives, adult expression is destroyed | **Not a therapeutic window at all** — an immune result, and one in which the adult arm received four times the vector, so age and antigen load move together |

**The negative therefore stands, and stands harder: six sources later, no therapeutic window has
been measured for any of these genes, and the revival trigger has not fired.**

## Refinement 1 — the window is endpoint-specific, which wave 3 could not see

PMID 39358605 is the first source in this corpus to split its endpoints by age of dosing rather than
reporting one verdict. Treating adults left **brain structure** unrescued ("in contrast to treatment
of neonates, treatment in adults did not show any significant improvement") while still rescuing
**motor function** ("significant functional recovery of motor phenotypes was observed"). The honest
general statement is therefore not "the window is unmeasured" but the stronger and more useful
"**a single window does not exist to be measured** — structural endpoints and functional endpoints
behave differently, and any WWOX window claim must name which endpoint it is about." PMID 41712282
shows the same shape from the other side: its adult-treated animals recovered seizure resistance and
delta-wave abnormality but recovered sleep architecture and theta/alpha power less well, which the
authors attribute either to power or to "a neurodevelopmental feature of the disorder that is not
rescued with adult vector administration" — and decline to choose.

## Refinement 2 — a counter-datum that pushes the window later, not earlier

PMID 41712149 reports a conditional knock-in in which the gene is **reactivated on demand**. This is
the only design in the corpus in which expression is matched across ages *by construction*, because
the endogenous locus is switched on rather than a vector dosed. Reactivation after symptoms (P30)
gave "complete rescue of both spontaneous and thermally induced seizures", normalised interneuron
firing and reversed widespread expression abnormalities including astrogliosis — and **reactivation
at P90, in adulthood, also restored protein levels and rescued seizures "despite months of prior
seizures"**. If that primary holds, it is close to the inverse of the revival trigger: efficacy did
*not* fall with age under matched expression. It does not revive the dismissal; it makes the
dismissal's direction of error asymmetric — the risk is of closing the window **too early**, not too
late.

Three limits bind this datum hard: it is **review-level** and its primary was not retrieved; the
model is a **dominant haploinsufficiency** with one intact allele, so reactivation restores a
physiological level that a biallelic null cannot reach by the same mechanism; and seizure rescue is
not developmental rescue — the same review's clinical section argues the opposite way about cognition.

## Ops (provisional ids; `DIS-031` is the next free number measured 2026-10-03)

### 1 · `disease-models/wwox/research/dismissal_ledger_current.md` — `append` (new record)

Exact text to append:

```
### DIS-031 — «The developmental window for WWOX restoration can be bounded from the 2024–2026 gene-replacement literature» → ❌ **REJECTED — corroborated across six further sources, including the first human one**
- **PREMISE: DATO** (2026-10-03, intake wave 5, Scientist A, `context_policy: SOURCE_FIRST`; six first reads, all `partial_fulltext_read` with figure panels not rendered). This entry **corroborates and supersedes the proposal of `CC-20261003W3-C-RESTORATION-SPEC-01`** rather than replacing its reasoning. Every result in these six sources that looks like a window result resolves to delivery, to dose, or to immunity. PMID 41712282 (`FTR-20261003-41712282-01`) dosed the same vector at the same dose by the same route at P10 and at 3 months and measured cerebellar vector at *«15.7 × 103 ± 3.1 × 103»* against *«1.2 × 103 ± 7.4 × 102»* vg per genome — an order of magnitude of delivery, partly recoverable by switching the adult route. PMID 39358605 (`FTR-20261003-39358605-01`) treated neonates at 4 × 1013 vg/kg and adults at 2–5 × 1012 vg/kg, an order of magnitude lower. PMID 40988338 (`FTR-20261003-40988338-01`) gave its neonatal arm only the lowest dose by a forebrain-biased route and reached ~70% of wild-type protein, against near-wild-type protein and brain-wide spread in the juvenile arms that worked, and the authors attribute the difference to level and distribution themselves.
- **The human source does not change it.** PMID 41314141 (`FTR-20261003-41314141-01`), the only first-in-human high-dose intrathecal AAV9 trial in the corpus, states that *«the timing of the intervention is likely to have a very large impact on the treatment efficacy»* — but it is n = 4, open label, with no matched natural-history cohort (*«we cannot comment on whether the rate of progression was altered in the treated cohort»*), no dose-response, no measurement of transgene expression in any patient, and *«no formal statistics were performed on this cohort»*. That is an interpretation, not a measurement.
- **§13 / epistemic status:** the claim fails on **confounding**, not on plausibility. In every design available, age of dosing is entangled with achieved exposure, and no source holds exposure constant across ages. A statement of the form "after age X, WWOX restoration cannot work" has no source behind it.
- **Two refinements that survive the rejection.** (i) **A single window does not exist to be measured.** PMID 39358605 is the first source here to separate endpoints by age: adult treatment left brain structure unrescued (*«In contrast to treatment of neonates, treatment in adults did not show any significant improvement»*) while still rescuing motor function (*«significant functional recovery of motor phenotypes was observed»*). Any future WWOX window claim must name its endpoint class. (ii) **A counter-datum points later, not earlier.** PMID 41712149 (`FTR-20261003-41712149-01`) reports a conditional knock-in in which reactivation of the endogenous gene in adulthood still worked: *«reactivation at P90 (adulthood) also restored physiological Na»v1.1 levels and rescued seizures, despite months of prior seizures*. That is the only design in the corpus with expression matched across ages by construction — and efficacy did not fall. ⚠️ It is **review-level**, its primary was not retrieved, the model is a **dominant haploinsufficiency with one intact allele**, and seizure rescue is not developmental rescue.
- **Confine:** this does not say early treatment is not preferable, and it does not say the window is open. It says the window has not been measured, that its direction of error is more likely to be "closed too early" than "closed too late", and that it cannot be stated without naming an endpoint class.
- **`REVIVAL_TRIGGER`:** unchanged from the wave-3 proposal and still unfired — a published dosing study in which **brain expression is matched across two ages** and efficacy still falls with the later age. A second, now-named trigger: retrieval of the conditional-reactivation primary behind PMID 41712149's P90 statement, which would either harden the counter-datum or remove it.
```

### 2 · `disease-models/wwox/research/research_candidates_current.md` — `append` (new record)

```
### RC-A-20261003w5-02 — Retrieve the conditional-reactivation primary behind the adult-rescue claim

**Why:** it is the only study design in the corpus in which transgene expression is matched across
ages by construction, and therefore the only one that can address the standing window question
without the delivery confound. It is currently held only as a sentence inside a narrative review
(PMID 41712149, reference 87 of that review), and the review's own search window closes on
31 March 2025.

**What to check at source:** whether rescue at P90 was measured on seizure endpoints only or also on
behaviour and development; whether the comparison is to age-matched untreated animals; whether
protein level was quantified against wild type; and whether one intact allele was required for the
rescue — the last being the limit that decides whether the result can transfer to a biallelic null
at all.
```

## What would change the model if true, and what would falsify it

**Would change it:** either trigger above firing. **Would falsify the central claim here:** a source
in this set that does hold expression constant across ages — none does, and that is a checkable
statement about six artefacts on disk.

### LOCATOR TRIPLES FOR BLIND AUDIT

(Delivery at the same dose and route fell by about an order of magnitude when the age of dosing rose. | IT delivery of AAV9 in KO mice at P10 resulted in markedly higher brain transduction | Results, biodistribution, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(Changing the adult route recovered part of the lost brain exposure. | ICM delivery resulted in greater brain expression as compared with IT injection | Discussion, route paragraph, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(Structural endpoints were rescued only by neonatal treatment while motor endpoints were rescued at both ages. | In contrast to treatment of neonates, treatment in adults did not show any significant improvement | Results, adult dose-response, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(Adult treatment still rescued motor function despite leaving the anatomy unchanged. | significant functional recovery of motor phenotypes was observed | Discussion, window paragraph, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(The authors attribute the neonatal failure to expression level and distribution rather than to age. | more robust behavioral rescue likely requires higher doses or improved delivery strategies | Discussion, window paragraph, `files/fulltext/PMID40988338_Quinlan2025_PMC.xml`)

(Neonatal delivery reduced epileptiform activity but failed on every behavioural endpoint. | did not mitigate this hyperactivity phenotype | Results, P2 arm, `files/fulltext/PMID40988338_Quinlan2025_PMC.xml`)

(The authors state that intervention timing is expected to dominate efficacy and that patients should be found earlier. | the timing of the intervention is likely to have a very large impact on the treatment efficacy | Discussion, disease modification, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(The trial cannot say whether progression was altered, for want of a matched natural-history cohort. | we cannot comment on whether the rate of progression was altered in the treated cohort | Results, secondary endpoints, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(No statistical testing was performed on any outcome. | no formal statistics were performed on this cohort | Methods, statistics, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(Restoring the gene in adulthood, after months of seizures, still rescued the phenotype. | reactivation at P90 (adulthood) also restored physiological Na | Gene-regulation strategies, `files/fulltext/PMID41712149_Balestrini2026_PMC.xml`)

(Restoring the gene after symptoms had appeared gave complete rescue of both seizure types. | led to complete rescue of both spontaneous and thermally induced seizures | Gene-regulation strategies, `files/fulltext/PMID41712149_Balestrini2026_PMC.xml`)

---

## BATCH DISPOSITION — `BATCH_20261003_004` (2026-10-03, ACTOR_ID `scientist`, Scientist I), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED — **MERGED**. Its dismissal record and the dismissal op of `CC-20261003W3-C-RESTORATION-SPEC-01` state the same proposition from **disjoint** source sets, so the batch wrote **one** record, `DIS-033`, carrying both (wave-5: 41712282, 39358605, 40988338, 41314141, 41712149, 40809677; wave-3: 39847501, 42181696, 40349107, 40263630, 42521212), rather than two records of one negative. Class **MINOR**: no claim is edited.

**Renumbered.** The declared `DIS-031` was taken — `DIS-031` and `DIS-032` landed with `BATCH_20261003_003` (the DRG and SMA-dose rejections) — so the record is **`DIS-033`**; `RC-A-20261003w5-02` kept its id.

**Three integrator amendments, from the blind locator audit (five independent auditors, 148 triples, 0 NOT_SUPPORTED, 0 UNVERIFIABLE).** (1) The structural-versus-functional split of PMID 39358605 is not clean: adult treatment did significantly reduce calbindin-positive deep-cerebellar-nucleus spheroids, and the motor rescue is stated *«with our high dose»* — so the record now says a window claim must name its endpoint **and its dose**. (2) PMID 40988338's authors name **three** contributors to the age difference, isoform choice among them, and do not exclude age; the record says so. (3) The route recovery in PMID 41712282 is stated as greater brain expression by ICM than IT in adults; the **fraction** of the age deficit recovered is nowhere quantified, and the deficit itself is cited from the group's prior work.

**Not medical advice.**
