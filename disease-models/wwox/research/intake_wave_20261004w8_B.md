# Intake wave 8 — 2026-10-04 — Scientist B — the restoration spec

```yaml
context_policy: SOURCE_FIRST
actor: scientist (Group B of intake wave 8)
branch: task/sci-B-20261004w8
date: 2026-10-04
papers: 6
verdicts: 6 INGEST (0 DEFERRED, 0 duplicates)
```

> **Not medical advice.** Public edition: class level only, no individual-level record.

## The assigned question

> What does each source add to, or limit in, the claim that a WWOX restoration cassette can be
> specified in advance — which promoter, which capsid, which route — and that its effect could be
> *read out* by an assay that already exists?

## The short answer

**The cassette can be partly specified; the read-out cannot.** Five of the six papers are
engineering records that narrow the promoter, capsid and route choices with real numbers, and every
one of them narrows them *less* than its own summary suggests. The sixth — the only paper in the
group whose entire method is the measurement of WWOX — shows that the three direct WWOX read-outs
that exist are all relative, none is calibrated, none has a stated limit of detection, and the most
clinically deployable of them achieved only **fair** inter-rater agreement (weighted κ 0.264 and
0.273) in the hands of two board-certified pathologists with unlimited tissue. A pharmacodynamic
read-out must detect a *change*; nothing read here demonstrates the precision to do that for WWOX in
any matrix.

The asymmetry is the finding: **the delivery side of a restoration spec is instrumented and the
measurement side is not.**

## Per paper

| # | PMID | Verdict | WWOX hits | One line |
|---|---|---|---:|---|
| B1 | 33129329 | INGEST | 257 | Tier 1 modality demonstration; not a validated biomarker, not an endpoint; measured reliability ceiling κ 0.26–0.27 |
| B2 | 40952239 | INGEST | 5 | WWOX is one unquantified row of 283 in a murine proxisome; the selection premise is not supported |
| B3 | 41036104 | INGEST | 0 | Ten promoters head to head; a cell-restricted promoter put the **most** protein in the liver |
| B4 | 42137269 | INGEST | 0 | A 126 bp promoter; the capsid is **AAV-DJ, not AAV9**; route changes the ranking |
| B5 | 42136830 | INGEST | 0 | Lumbar IT reaches primate brain at 1–4 vg/DG; no expression measured anywhere |
| B6 | 41744777 | INGEST | 0 | Liver de-targeting ~127-fold, at 8× worse packaging and significantly fewer brain vector genomes |

Every paper is a first reading: `paper_packet.py packet` reported no manifest, no receipt and no
registry record for all six. No duplicates, no retractions, no expressions of concern, no errata;
all six dependency screens returned `SCREENED_CLEAN`.

## Three premises in the assignment that the sources do not support

1. **B4 is not an AAV9 record.** The selection note called it the counterpart that "buys cassette
   headroom in an AAV9 genome". Every in vivo experiment in it uses **AAV-DJ**. AAV9 appears only as
   a literature reference. A headroom claim for an AAV9 cassette cannot be sourced to this paper.
2. **B2 is not a WWOX–excitability bridge.** The note called it "the first mechanistic bridge
   between WWOX and excitability that is not transcriptional". The paper contains no excitability
   measurement involving WWOX, no excitable cell (the cells are murine pancreatic ductal
   adenocarcinoma epithelium), and no validated WWOX–channel interaction. WWOX is one row in a
   283-protein annotation table with **no numeric cell anywhere in the sheet**, plus two Discussion
   sentences. The paper's own co-immunoprecipitation arm confirmed **two of eight** candidates it
   tested; WWOX was not one of the eight.
3. **B1's "268 WWOX hits" is 257** by a count over the persisted JATS body, and the paper's
   "function" arm is an earned negative. The substance of the selection note was right —
   it is a pure WWOX-measurement protocol — but the number and the framing both needed correcting.

## B1 — what is actually measurable, and under §13

LEGEND_CORE §13 puts a direct gene read-out (protein, mRNA, splice, enzymatic activity, immediate
substrates) in Tier 1, and forbids calling any candidate *validated* without direct
sensitivity/specificity evidence **in the disease population**.

| Read-out | §13 class | What this paper shows about it |
|---|---|---|
| WWOX mRNA, comparative Ct vs 18S | Tier 1 modality | Group separation only; **three tumour samples equal or exceed the higher normal control** on the panel. Relative, no calibrator — reports a batch comparison, never a patient's value |
| WWOX protein, immunoblot vs β-actin | Tier 1 modality | Target at ~47 kDa, loading control at 43 kDa on a **stripped and reprobed** membrane; the uncropped blots show **multiple immunoreactive species** with the reported band picked out by an arrow; a hand-annotated **three-hour exposure** |
| WWOX protein, tissue immunohistochemistry | Tier 1 modality | Two ordinal by-eye scales, two blinded pathologists, **κ = 0.264 and 0.273 — "fair"**. The metric that separated the two classes cleanly (percent positivity) is the one with the weaker agreement |
| WWOX enzymatic activity | Tier 1 modality | **Never attempted anywhere in the paper** |

**Verdict: Tier 1 modality demonstration; not a validated biomarker; not an endpoint.** No
sensitivity, no specificity, no limit of detection, no linear range, no calibrator, no disease
population. The sensitivity 78–94% / specificity 88–93% quoted in its Results belong to a **cited
copy-number study by other authors**, not to any WWOX measurement made there.

Two panel readings weakened the authors' own text, in the direction wave 4 predicted: the transcript
panel's case/control overlap, and the uncropped overexpression blot in which the empty-vector and
WWOX lanes carry bands of comparable intensity with two further unlabelled lanes comparable to both.

**Could any of it run on a living patient's sample?** Technically all three, on blood, biopsy or
fixed tissue. None as a *pharmacodynamic* read-out: a relative assay with no calibrator cannot
report a value, and an ordinal score with fair agreement cannot resolve a treatment-induced change.
Neither antibody in the paper is validated against a genetic negative — the immunohistochemistry
negative control is an isotype-matched irrelevant antibody, a reagent control, not a target control,
and the knockdown cells that existed in the same study were never used this way.

## B3–B6 — what the delivery side now bounds

**Promoter.** A neuron-restricted promoter (p546, 72% NeuN, 1.9% astrocyte) reached essentially the
same brain-area coverage as a ubiquitous one (41% vs 42%) at about a third of the intensity —
restriction cost intensity, not reach. But **"cell-specific" is not "peripherally silent"**: the
astrocyte-restricted gfa1405 gave the most hepatic protein of any promoter tested, by quantitative
western blot, while whole-organ fluorescence in liver showed almost nothing. The Discussion's liver
reassurance in that paper addresses the *ubiquitous* promoter instead. Any cassette whose safety
case rests on promoter restriction must measure hepatic **protein**.

**Promoter size.** 126 bp of all-human, non-viral sequence performed comparably to promoters an
order of magnitude larger and matched a neuron-restricted promoter in liver and kidney — roughly
1.5 kb of cassette recovered, and a regulatory property (no viral enhancer) against the FDA guidance
those authors cite. Separately, a 1,405 bp astrocyte promoter left a stated 2.3 kb for the transgene
inside a 4.8 kb single-stranded AAV capacity.

**Route.** Lumbar intrathecal reached cynomolgus macaque brain at **1–4 vector genomes per diploid
genome**, uniformly across regions, and only at doses ≥ 5.8 × 10^13 vg/animal. Spinal cord received
about ten times more; **cerebellum was the lowest brain region**, about five-fold below prefrontal
cortex. Dose scaling is **sublinear** (4× dose → ~2.5× brain vector). Those authors explicitly
forbid reading vg/DG as a transduced-cell fraction, and state that vector DNA detection gives no
assurance the genome is intact or nuclear.

**Capsid.** A five-mutation AAV9 variant cut hepatic vector genomes ~127-fold — but packaged
**eight-fold worse**, dropped whole-animal transgene signal about two orders of magnitude, and, by
its own Discussion, put **significantly fewer vector genomes into the brain** than the parent. Its
CNS equivalence rests on a per-tissue transcript *ratio*, measured once, in mouse, at one dose, with
a reporter. The dose-ceiling argument it is proposed for is never measured: the paper contains no
toxicity endpoint of any kind.

**The cross-cutting result that changes how a spec is written:** in B4, the same promoter in the
same capsid at the same dose in the same strain was the best of four by the intrathecal route and
among the worst of four by the intracerebroventricular route. **Promoter and route must be specified
together.** A promoter chosen on ICV data cannot be carried to an IT protocol.

**And the route is not only a distribution parameter.** B5 reports, inside its own limitations, a
canine study in which — at comparable biodistribution — intracerebroventricularly dosed animals
developed strong and in one case fatal encephalitis driven by T cells specific to the transgene
product, while intracisternally dosed animals did not.

## What would change the model if true, and what would falsify this reading

| If this were shown | The model would change by |
|---|---|
| A calibrated WWOX assay (recombinant standard, stated LOD and linear range) in an accessible matrix | The restoration spec would acquire a pharmacodynamic read-out it does not have; a dose-ranging trial could have an interim measure |
| WWOX protein measurable in CSF or blood at all | The whole read-out problem moves from biopsy to fluid, which is the difference between one measurement and a time course |
| Promoter ranking reproducing across routes in a second laboratory | "Specify the cassette in advance" becomes defensible; at present B4 falsifies it for its own four promoters |
| A liver-de-targeted capsid with unchanged brain vector genomes **and** unchanged packaging yield | The dose ceiling genuinely moves rather than trading places with a manufacturing ceiling |

**What would falsify the reading above:** (i) the supplementary western-blot figure of B3 showing
that the astrocyte promoter's hepatic protein is not in fact the highest — that panel was not
retrieved and the finding rests on the authors' own Results sentences describing it; (ii) a per-protein
enrichment statistic for WWOX in B2's dataset, which would move it from an unquantified row to a
ranked hit; (iii) an inter-rater agreement above κ 0.6 for WWOX immunohistochemistry in any
published cohort, which would lift the measurement ceiling this note rests on.

## Effect on canonical records — checked, and it is additive

Searched `claim_registry_current` (44 records) for `biomarker` and for `biomarcatore`: **zero
matches**. There is no consolidated baseline claim about a WWOX biomarker to narrow or reverse, so
the §13 classification above **adds** a record rather than changing one, and the candidate is MINOR.

The design-principle text that B3–B6 bear on lives in `working_model_current` BLOCK 3 ("Design
principles (Obeid 2026 review): human synapsin promoter (neuron-specific); WPRE removed; controlled
dose; critical early postnatal window") and in the adjacent safety caveat about dose-limiting
peripheral toxicity. None of the six papers contradicts those; they bound them. The restoration-spec
candidate is therefore also MINOR, and says so with its reasoning.

## Candidates produced

- `CC-20261004W8-B-REGISTRY-01` — registry landing for all six PMIDs (PAPER + LIT), numbers
  provisional.
- `CC-20261004W8-B-BIOMARKER-01` — the §13 classification of the three direct WWOX read-outs and
  their measured ceilings.
- `CC-20261004W8-B-RESTORATION-SPEC-01` — the promoter / capsid / route bounds, each with its
  transfer limit.

## Artefacts

Six manifests, six dossiers, six receipts (all prepared, none recorded — the ledger is hash-chained
and three scientists ran in parallel). Every manifest verifies PASS with **0 gaps** under
`deepdive_manifest.py --verify-artifacts --require-current-schema`. All six receipts dry-check
`RECORDED` against throwaway ledger and manifest copies.

Persisted into the root `files/` tree: six Europe PMC JATS bodies, one uncropped-blot supplement
(its served MD5 matching the digest the article's own JATS declares), six publisher figure rasters,
and two supplements for B2. SHA-256 in full in each manifest.

## Honest gaps

- **B3 and B4 supplements were not retrieved.** For B3 this touches the hepatic-protein finding
  (Figure S1) and the full pairwise promoter comparison (Table S1); for B4 it touches the
  transcription-factor-site map and the per-region image panels. Both are declared in the dossiers
  and in `coverage.supplementary: not_read`.
- **Figure panels were adjudicated only for B1.** For the other five the legends were read in full
  and no number carried from them lives in a panel, so `coverage.figures` is `captions_only` and
  every receipt declares `partial_fulltext_read`. None claims a complete read.
- **B5's figure alt-text is publisher-generated with AI**, as that article's own Generative AI
  statement declares. It was read and explicitly not used as a source for any number.
