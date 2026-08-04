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

## Verification

```
deepdive_manifest.py --pmid 39507621   → PASS (2 declared gaps)
deepdive_manifest.py --pmid 36779245   → PASS (3 declared gaps)
fulltext_receipts.py verify            → OK: 41 chained, tail anchored
test_deepdive_manifest.py              → 12 tests, falsified both directions
legend_lint.py .                       → PASS; ratchet lowered 21 → 20
```

The four canonical current files were not modified.
