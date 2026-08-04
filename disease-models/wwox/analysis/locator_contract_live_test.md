# The locator contract, tested on a live reading — PMID 39507621

**Date:** 2026-08-04 · **Paper:** Teplyshova & Sharkov 2024, *Front Genet* 15:1477466 (PAPER 015)
**Receipt:** `FTR-20260804-39507621-01` · **Manifest:** [`PMID39507621.json`](../research/deepdive_manifests/PMID39507621.json)

## Why this paper

The contract added on 2026-08-04 requires a `complete_fulltext_read` to carry verbatim
locators. It had been propagated to thirteen instruction surfaces and guarded by a test, but
**never exercised on an actual reading**. A rule that has only been checked by the test that
checks it is not yet known to work.

PAPER 015 was chosen because it was the adversarial case, not the convenient one: the paper
registry declared `Evidence depth: full text reviewed (PMC open access)`, while the only
receipt in the ledger was a `legacy_reconstruction` carrying `unknown_legacy` on every
section. The system had honestly recorded that it could not vouch for its own declaration.
That is precisely the state the contract exists to drain.

## What the run produced

| | |
|---|---|
| Verbatim locators captured | **16**, live, while the document was open |
| Figures inspected | **3 of 3**, images opened — not captions |
| References enumerated | **19**, of which 16 gene-direct |
| Receipt | `partial` → **`complete_fulltext_read`**, chain verified at 40 |
| Registry-declaration ratchet | **21 → 20** — a real debt paid, not deferred |

The capture cost was what the protocol claims: seconds per locator, taken from a document
already open. Retro-extraction of fourteen locators from two papers, earlier in this session,
cost two full re-readings.

---

## 1. The gate had a defect, and only a real manifest could find it

Writing an actual manifest — rather than reasoning about the validator — surfaced a bug in
`deepdive_manifest.py`:

`"waived": false` is the idiomatic JSON for *"I am not waiving this section."* The helper
tested `waiver is None`, so `false` fell through to the waiver branch. Two consequences, the
second worse than the first:

1. the error read **"a waiver must state why in at least 40 characters"** — which argues the
   author into *writing a waiver reason for a section they meant to fill*. **A guard whose
   error message points at the omission is worse than no guard**, because it recruits the
   author into committing it.
2. `_waived` returned `True`, so the function **returned before validating the entries at
   all**. A manifest could carry `"waived": false` next to an empty or malformed locator list
   and never have it examined.

Fixed; two regression tests added. Falsified in both directions on isolated copies — bug
reintroduced → 3 failures, fix restored → 0.

## 2. Two references LEGEND had never seen

Enumerating the reference list — the slot that exists because a 2026-07-26 receipt declared a
complete read without ever listing its 28 references — found that **2 of the 16 gene-direct
references are absent from the paper registry, the full-text queue and the tracking log**:

- **PMID 32051108** — compound-heterozygous WWOX epilepsy, Chinese patient.
- **PMID 25716914** — biallelic WWOX epileptic encephalopathy, first described prenatally.

The second matters here specifically: this report records absent foetal movement in the last
month of pregnancy and attributes prenatal onset to the literature. A prenatal-presentation
case is the direct test of that attribution. Both are queued as reading debt.

An unenumerated reference list hides its own gaps, and it hides them silently.

## 3. The scientific finding: the paper contradicts the rule it cites

The Discussion states the field's genotype-phenotype rule verbatim:

> "premature translation termination due to biallelic null […] variants lead to more severe
> phenotypes of early epileptic encephalopathy, while **biallelic missense variants lead to a
> predominantly spinocerebellar ataxia phenotype**."

The patient reported is **homozygous for a missense allele** (p.Thr12Met) and has a full
WWOX-DEE phenotype: onset at 4 months, four decades of daily seizures, no expressive speech,
regression to absent independent motor activity. **Biallelic missense at the severe pole.**

The report does not flag this tension. It is nonetheless the most informative thing in the
paper, and it is consistent with two other statements it makes:

- **`INFERENZA`** — the missense→ataxia direction is a **population tendency, not an
  allele-level prediction**. Convergent support: this paper's own Introduction states
  *"no specific region within the gene has been conclusively linked to WWOX-DEE"*; Oliver 2023
  independently showed both phenotypes arising from biallelic missense; the survival statistic
  it cites is itself probabilistic (*"at least one missense variant increasing the probability
  of 5-year survival from <50% to >75%"*) — a shifted distribution, not a determined outcome.
- **`DATO`** — a homozygous missense genotype is compatible with acquiring sitting, crawling
  and supported walking, and with losing all of it from adolescence.

**Bearing on the operator's spectrum reading.** The severity gradient toward null/null holds
as a gradient. What this case removes is the inference that runs the other way: *observed
missense/missense does not license predicting the milder pole for an individual.* The
mechanism that discriminates the poles is not allele class alone, and it is not yet known.

**Tension recorded against CLAIM 017.** Its Summary reads that survival into adulthood
attaches to *"milder phenotypes such as SCAR12"*. This is survival to 40 at the **severe**
pole. The claim's framing ties an outcome to a pole that this source separates from it.
Recorded as a commit candidate — not applied; canonical files change only under
`BATCH_COMMIT`.

## 4. What only opening the images gave

Both EEG figures carry **dedicated ECG (250 µV/mm) and EMG (200 µV/mm) polygraphic channels**
alongside the 18-channel bipolar montage. Neither caption nor body text mentions them. The
distinction matters because the EMG trace is what separates a myoclonic seizure from a
non-motor discharge in this record — the paper's seizure-type claims are checkable against the
figures only because that channel is there.

**Figure 1 — a correction made mid-run.** The first pass abstained from the clinical
photograph on privacy grounds. That was wrong, and the reasoning was lazy: **the privacy risk
lives in what LEGEND records, not in what it looks at.** Abstaining protected nothing and left
the D-14 failure mode — a caption that misdescribes its own image — unchecked on the one
figure where the text carries the whole burden. Inspected; the image is publisher-redacted
across the lower face; the three dysmorphic features named lie in the visible region and are
not contradicted; no feature is visible that the text omits. Resolution does not support
independent grading of fissure slant, so the caption is **uncontradicted, not confirmed**. No
description of the individual is recorded anywhere.

---

## Three defects in the instrument, not in this run

These are limits found by using the machinery, and none is fixed here.

**a. A receipt cannot say *why* a coverage value is what it is.** The schema sets
`additionalProperties: false` at both the top level and inside `coverage`. Had Figure 1
stayed uninspected, the honest value was `captions_only` — and a future reader would see
`partial_fulltext_read` and queue a re-read to close a gap that LEGEND had *decided* to leave
open. **An unexplained `captions_only` manufactures permanent, unpayable debt.**

**b. Coverage is graded per section; figures are read per item.** With three figures and one
uninspected, `read` overclaims and `captions_only` underclaims. Both are false, and the
protocol forces the choice without recording that it was forced.

**c. Section-level waivers, field-level impediments.** Two `group_assessment` integers were
unmeasurable here (the PubMed connector is unauthorized). Waiving rather than inventing them
also discarded `research_type`, `is_primary_group_for_disease` and `weighting` — all three
determined from the Methods. They were preserved inside the waiver prose, which works but is
not a slot a machine can read. Related: `reread_reason` is a closed enum with no free-text
companion, so the argument for this re-read is not in the ledger.

---

## 5. The run unblocked the session's top pending item, by accident

Retrieving the EEG figures here required finding a working image route. The one that worked —
`pmc.ncbi.nlm.nih.gov/articles/instance/<PMCID>/bin/<file>.jpg`, with the PMCID resolved via
`elink.fcgi` — had **never been tried on Oliver 2023** (PMID 36779245), whose figures were
recorded as unobtainable after four failed attempts and had been standing as the single
blocker on `complete_fulltext_read` for PAPER 018, and therefore on exporting CLAIM 017.

It works. All four figures retrieved and inspected. What they gave, none of it in the captions:

- **Fig. 4A** — survival orders **null/missense > missense/missense > null/null**. The best
  survival is *not* the missense/missense group. Confidence bands between the top two overlap
  heavily, and **`p = .0085` is a three-group log-rank, not a pairwise test** — so it supports
  "null/null is worse", not a monotonic ranking. CLAIM 033 cites this p-value.
- **Fig. 4B** — `p = .65` for seizure onset. **Genotype group does not predict age at onset.**
  Survival severity and epilepsy-onset timing are different axes.
- **Fig. 3** — the two SCAR12-associated missense variants sit at opposite ends of the protein
  (p.Pro47Thr, exon 2; p.Gly372Arg, exon 9), and p.Pro47**Thr** carries the SCAR12 marker while
  p.Pro47**Arg** does not — same codon, different disease pole.
- **Fig. 1C** — a lateralizing focal semiology (behavioural arrest → left eye deviation →
  asymmetric limb stiffening R>L → cyanosis → right arm clonic jerks).
- **Fig. 2** — fronto-temporal and hippocampal atrophy, optic-nerve atrophy, white-matter
  abnormality, thin corpus callosum.

Supplementary S1/S2 confirmed genuinely unavailable: both return HTTP 200 serving HTML rather
than the documents. `unavailable` does not block a complete receipt.

**The reusable lesson is the failure, not the fix.** A 301 or 404 on one image route had been
recorded as *"the figures are unobtainable"* — a retrieval outcome written into the record as a
property of the document. That is the false-negative shape the discipline names: silent,
self-reinforcing, and it stood for the rest of the session as a blocker requiring an
institutional subscription. It required no subscription. **Record what was tried, not what
exists.**

---

## 6. Oliver 2023 completed

`FTR-20260804-36779245-02` · `complete_fulltext_read` · **20 verbatim locators** ·
manifest [`PMID36779245.json`](../research/deepdive_manifests/PMID36779245.json).
Coverage: text, Tables 1–3 and all four figures `read`; supplementary `unavailable`
(HTTP 200 serving HTML, verified twice). Ledger at 41, chain and tail anchored.

**A correction to what §5 implied.** The reading did *not* discover that Oliver refutes the
intermediate phenotype. **CLAIM 033 already carried that sentence verbatim**, as the second of
four mandatory reservations, together with the observation that the reference genotype's class
(`null/missense`) is not resolved separately but aggregated with `missense/missense`. LEGEND
knew. What did not exist was the **locator** — which is the entire point of the contract, and
a smaller claim than the one I made. Stated plainly because the difference matters: the
system's science was ahead of my summary of it.

What the completed reading does add:

**a. A registered paper asserts what the registry flags as unsupported.** Teplyshova 2024
(PAPER 015) states that null/missense phenotypes *"fall in an intermediate range"*, attributing
it to the literature, in the paragraph immediately after it cites Oliver 2023 for the mortality
statistic. Oliver 2023 is the paper that found **no evidence** for that intermediate class.
Both are now in the registry, both with complete receipts and locators, and they disagree.
→ commit candidate: **CLAIM 033 status `in observation` → `conflicting evidence`**, with
PAPER 015 named as the conflicting source.

**b. CLAIM 017 conflates mildness with survival.** Its Summary ties *"survival into later
childhood/adulthood"* to *"milder phenotypes such as SCAR12"*. Two independent sources now say
otherwise: Oliver's **oldest living patient, 23 y 11 m — Patient 2, homozygous p.Gln230Pro,
missense/missense — is a full DEE**, profoundly impaired and non-ambulant; Teplyshova's
40-year-old is likewise homozygous missense with full DEE. Adult survival in this disease
tracks **the presence of a missense allele**, not phenotypic mildness. → commit candidate:
qualify CLAIM 017's Summary. **Not** a reversal — the WOREE↔SCAR12 spectrum stands.

**c. A precision the working model should not lose.** `p = .65` on seizure onset (Fig. 4B) is a
comparison **between genotype classes within WWOX-DEE**. It is *not* a statement about DEE
versus SCAR12, where Oliver separately reports SCAR12 onset at 9–12 months against weeks for
DEE. Reading it as the latter would manufacture a contradiction with CLAIM 017 that does not
exist.

**d. Patient 2 is a natural-history datum on the reference-genotype axis.** Homozygous Q230P,
21 years of follow-up, EEG evolving to *"a diffuse low-voltage background without epileptiform
abnormalities"*. Q230P is the allele CLAIM 033's first reservation names as missense that
**abolishes the protein** — so the longest-followed survivor carries a missense allele with
null-like protein consequence. That is the sharpest single case against reading the genotype
classes as a functional gradient, and it is one patient, in one cohort.

**e. Seven more unread gene-direct references**, 27% of the list of a paper already supporting
three claims. Two of them were queued hours earlier from Teplyshova's list: **two independent
papers cite them and LEGEND had seen neither.** Queued as FT-030/031/032.

Three commit candidates recorded. **None applied** — the four canonical current files change
only under an operator-authorized `BATCH_COMMIT`.

---

## 7. Gao 2025 (PAPER 014) — a paper that contradicts its own table

`FTR-20260804-40875931-02` · **`partial_fulltext_read`** · 20 verbatim locators ·
manifest [`PMID40875931.json`](../research/deepdive_manifests/PMID40875931.json).
Operator-supplied PDF; *Neurology*, all rights reserved, not retained. Prior record was a
`legacy_reconstruction` with `unknown_legacy` on every section.

**What LEGEND already had, and I did not discover.** CLAIM 013 already records the three
significant associations with their exact figures, the survival bias, *and* the sentence
*"case ID 11 (N/M: null+Q230P) è l'unico deceduto nel cohort"*. The registry was accurate before
this reading. Saying so first, because this is the third time in this session the system's
prior work was ahead of my summary of it.

### The finding: the Discussion asserts what Table 2 refutes

> **Discussion, p. e213883(11):** *"…the more severe phenotypes such as seizures, hypertonia,
> respiratory complications, **and higher mortality** are significantly associated with null/null
> genotypes."*

> **Table 2, 'Premature death' row:** N/N **0 (0.0%)** · N/M **1 (7.7%)** · M/M 0 (0.0%) ·
> χ² 2.44 · **p = 0.432**

In this cohort there were **zero deaths among null/null**, the single death was **null/missense**,
and the association is **not significant**. The paper's own Results section states this correctly
— it lists only hypertonia, seizures and respiratory complications as significant. The
overstatement is confined to the Discussion, where a result imported from Oliver 2023 (ref. 6) is
absorbed into a sentence whose grammar attributes it to *"these genotype-phenotype correlations"*,
i.e. to this study.

**Why it matters more than a wording slip.** CLAIM 033 is `in observation` and rests on Oliver's
`p = .0085`. If Gao 2025 were read as independently replicating the mortality gradient, that claim
would look corroborated by two cohorts. It is not: **Gao's mortality data are underpowered
(one death in 44) and point the other way.** One paper, read carelessly, would have converted a
single-source finding into a false convergence — and convergence is precisely what LEGEND uses to
promote `INFERENZA` toward `DATO`.

### The detail that closes the loop

The cohort's only death — case ID 11 — carries **p.(Gln72\*) + p.(Gln230Pro)**. CLAIM 033's first
reservation already records that **Q230P is a missense variant that abolishes the protein**
([[paper_registry_current#PAPER 041]]).

`PREMISE: DATO` (Q230P abolishes protein) → **`INFERENZA`**: on a *functional* rather than
*syntactic* classification, case ID 11 is null/null. The syntactic scheme placed the cohort's
only death in the wrong class, and correcting it would move the single death from N/M to N/N —
the direction the Discussion asserts. **The Discussion may be right about the biology and wrong
about its own evidence**, which are different failures and must not be merged. Not applied:
n = 1, and Gao performed no functional assay on any variant (Methods: classification is
in-silico throughout).

### A counting discrepancy in the paper

Seizures are reported in **45/50**, which implies **five** seizure-free individuals. The
Discussion names **four** (IDs 12, 13, 14, 18). Two of those four were excluded from the
correlation analysis, so among the 44 analysed, the named cases give one N/M and one M/M —
while Table 2's counts imply one N/M and **two** M/M. The arithmetic is consistent with a fifth,
unnamed seizure-free individual in the missense/missense group. With **M/M at n = 6**, that one
individual is 17 percentage points of the class carrying the `p = 0.016` seizure association.
Resolvable only from eTable 1 or Figure 2B → queued as **FT-035**.

### Commit candidates

1. **CLAIM 013** — add that the paper's mortality sentence is not supported by its own Table 2,
   and that its genotype-phenotype signal is *specific* (hypertonia, seizures, respiratory) while
   global severity is flat at `p = 1` for walking, talking, sitting and developmental delay.
2. **CLAIM 033** — record Gao 2025 as **non-replication** of the mortality gradient, not as
   corroboration; and record the functional-reclassification inference on case ID 11 with its
   n = 1 caveat.

Neither applied.

### Why this receipt is `partial`, deliberately

`figures: captions_only`. The page renderings were seen, but Figure 2B is the 44 × 18 per-case
grid from which Table 2 is computed, and it could not be resolved at the available resolution.
Claiming `read` would assert a verification I cannot back — and Figure 2B is exactly what would
settle the counting discrepancy above. This is defect **(b)** from §"Three defects" biting in
practice: the vocabulary offers no value for *"inspected but not resolvable"*, so the conservative
choice costs PAPER 014 its ratchet reduction. Correct direction, visible cost.

### Reference audit, and a correction to my own method

47 references, 40 WWOX-direct, **7 unknown to LEGEND** — including **Gribaa 2007**, the original
SCAR12 linkage study. LEGEND has been using SCAR12 as a category without having read the paper
that constitutes it (→ FT-033).

The first pass reported **12** unknown. Five of those had been queued hours earlier from Oliver
and Teplyshova and recorded **by PMID**, while my check keyed on **DOI**. Re-run on both keys: 7.
**A reference audit keyed on one identifier over-reports its own findings, and over-reports in
the direction that flatters the audit.**

---

## 8. Cheng 2020 (PAPER 019) — read to discharge the export blocker, and what it found instead

`FTR-20260804-32000863-01` · **`complete_fulltext_read`** · **22 verbatim locators** ·
manifest [`PMID32000863.json`](../research/deepdive_manifests/PMID32000863.json).
All seven main figures and all nine supplementary figures inspected. CC BY 4.0.

Read for one reason: the two `ELIGIBILITY_DEBT` records in the DisMech sidecar sat on CLAIM 016,
whose only unbacked source was this paper.

### The prediction was wrong, and the way it was wrong is the point

I predicted the sidecar would go **17 → 19 eligible**. It did not.

```
ELIGIBILITY_DEBT        2 → 0      the reading debt was discharged
LINK_ROLE_NON_SUPPORTING 0 → 2      ← they moved here
ELIGIBLE_FOR_EXPORT     17 → 17    unchanged
```

The eligibility gate had been **masking a second, independent blocker**. The state precedence
puts `ELIGIBILITY_DEBT` ahead of `LINK_ROLE_NON_SUPPORTING`, so until the receipt landed, the
link defect was invisible. This is the fail-closed ordering working: one gate at a time, and no
record advances until every prior gate is genuinely clear.

**The defect is in the registry, not the pipeline.** CLAIM 016 reads:

```
Source:    Cheng et al. 2020 · [[paper_registry_current#PAPER 056]] (Wang 2012 …)
Wikilinks: [[paper_registry_current#PAPER 019]] · [[PAPER 056]] · [[CLAIM 035]]
```

The `Source` field **names Cheng 2020 in prose but wikilinks the other paper**. PAPER 019 — which
*is* Cheng 2020 — appears only in the generic `Wikilinks` line, so the derivation reads the
CLAIM 016 → PAPER 019 relation as `wikilink_only` → `UNQUALIFIED_REFERENCE`, not `SUPPORTING`.
Correctly: an unqualified mention is not an assertion of support.

→ **commit candidate: CLAIM 016 `Source` must wikilink PAPER 019 alongside PAPER 056.** A one-line
correction to a canonical file, so it needs `BATCH_COMMIT` and the operator. Once applied, the two
records should clear to `ELIGIBLE_FOR_EXPORT` with nothing else changing. **Not applied.**

### What the figures gave that the text did not

**a. Lithium is not shown to be genotype-specific.** The text says only *"lithium chloride
significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice"*. **Figure 7d has three
panels — +/+, +/− and −/− — and lithium suppresses seizures in all three.** The experiment
therefore does not separate *"corrects the WWOX lesion"* from *"raises seizure threshold in any
mouse"*.

**b. The inversion.** Ethosuximide, the comparator the paper says lithium beats, **is**
genotype-specific: Figure 7b marks it non-significant in +/+ and +/− and significant only in −/−.
The drug with the specificity is the one the paper treats as the also-ran.

**c. "Elevated" is the wrong word.** Figure 7c prints its densitometry: **total GSK3β is flat**
(2.2–2.6 in every genotype and region); what falls is inhibitory Ser9 phosphorylation
(cerebellum 2.7 → 1.3). GSK3β is **dis-inhibited, not more abundant.** CLAIM 016's Summary says
*"GSK3β is elevated"*, which reads as abundance. → commit candidate: correct to *activation*.

**Premise tagging.** The inference *"GSK3β mediates the Wwox-null seizure hypersusceptibility"*
rests on `PREMISE: DEFAULT_FROM_TEXTBOOK` — **"lithium is a GSK3β inhibitor"**. Lithium is not
selective, and this paper's own Discussion supplies the alternatives: lithium *"rescue[s]
Wnt-dependent cerebellar midline fusion and neurogenesis deficits"* and *"induce[s]
β-catenin-mediated myelin gene expression in mouse Schwann cells"* — both of which are lesions
this mouse has. No selective GSK3β inhibitor and no genetic epistasis was tested.

`REVIVAL_TRIGGER` for the stronger causal reading: a **selective** GSK3β inhibitor, or Gsk3b
epistasis on the Wwox-null background, showing rescue **in the null and not in controls**.

This does not refute CLAIM 016 — it *sharpens* it in the direction the claim already leans.
GSK3β as amplifier of a structurally malformed network survives; GSK3β as the demonstrated
mediator does not, and was never demonstrated.

### A carrier signal, and it is specific

Across every quantified developmental measure the heterozygote is **indistinguishable from
wild-type** — brain weight (S1f, n.s.), cortical Ki67 at birth (S6b, n.s.), DCX densitometry
(S7: 2.60/2.38, 2.21/2.82, 2.47/2.43 for +/+ vs +/−), Tc-MEP amplitude (Fig. 2b, n.s.).

**One measure breaks the pattern.** Tc-MEP **latency** is significantly prolonged in +/− and —
read from Figure 2c — is **not significantly different from the homozygous null**. The single
haploinsufficient readout in the entire paper is a conduction-latency measure, i.e. a myelin
readout, and motor evoked potentials are routine in humans.

`INFERENZA` — a candidate Tier 1/2 carrier readout on the myelin axis. One study, one species,
n = 5 heterozygotes. Recorded as a locator, **not** promoted to the biomarker file.

### Also worth having

Brain water content is flat across genotypes (S1g), which excludes oedema as the explanation for
the smaller brain. Cortical thinning is measurable at **E16.5, in utero, before any seizure**
(S5c). Brain-wide apoptosis is quantified at 0.19% vs 0.89% (S9c). Peripheral nerve shows
Schwann-cell apoptosis and **onion-bulb degeneration** — a Charcot-Marie-Tooth-like PNS lesion in
a disorder framed as central. Two independently targeted knockout strains, built specifically to
exclude an aberrant product of the retained exon 1, agree on every behavioural measure.

### A retrieval note that keeps recurring

The supplementary was reachable only from the publisher's static-content endpoint; PMC returned
**HTTP 200 serving HTML**, the same false negative that hid Oliver's figures in §5. **Three times
in one session a "200" or a "404" has been mistaken for absence.** A retrieval outcome is a
property of the route, not of the document.

## Verification

```
deepdive_manifest.py --pmid 39507621   → PASS (2 declared gaps)
deepdive_manifest.py --pmid 36779245   → PASS (3 declared gaps)
deepdive_manifest.py --pmid 40875931   → PASS (3 declared gaps)
deepdive_manifest.py --pmid 32000863   → PASS (3 declared gaps)
fulltext_receipts.py verify            → OK: 43 chained, tail anchored
test_deepdive_manifest.py              → 12 tests, falsified both directions
test_export_dismech_dryrun.py          → 20 tests
legend_lint.py .                       → PASS; ratchet lowered 21 → 20
```

Four readings, four receipts, **78 verbatim locators**. Three reached
`complete_fulltext_read`; one is `partial` on purpose and says why.

Two DisMech blockers moved. The routing basis is now measured and backed
(§6). The CLAIM 016 eligibility debt is discharged and has exposed a
registry link defect behind it (§8) — a one-line correction that only
`BATCH_COMMIT` may apply.

The four canonical current files were not modified.
