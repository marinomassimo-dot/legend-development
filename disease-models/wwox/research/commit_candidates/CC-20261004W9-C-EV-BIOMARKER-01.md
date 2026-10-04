# CC-20261004W9-C-EV-BIOMARKER-01 — WWOX protein is measurable in a blood-accessible neuronal vesicle fraction; what that is and is not, under §13

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist C of intake wave 9,
2026-10-04. **Change class: MINOR** (one research-line record; narrows no `consolidated baseline`
claim). **Nothing here is medical advice.**

Source: PMID 42738875 (`FTR-20261004-42738875-01`, manifest PASS).

## 1 · Finding

WWOX **protein** was measured in **L1CAM-captured plasma extracellular vesicles** from an adult
human cohort, as one analyte of a 41-plex proximity-extension panel. This is the first
blood-accessible, neuron-attributed WWOX protein measurement the model would hold. Everything else
it holds is tissue, cell line or post-mortem.

Two things immediately bound it:

1. **The readout is relative.** NPX is a log2 relative unit; the authors deliberately did not use
   the assay's quantitative values for WWOX. There is no concentration, no reference interval and
   no dynamic range.
2. **The statistics are thinner than the sentence.** The text says WWOX was "higher in men than in
   women for the same cognition group"; **the panel marks no male-versus-female comparison for
   WWOX**, and the sexes-combined WWOX panel carries no significance bracket at all. One bracket
   exists, between two male groups. The assay was run **in singlet**.

## 2 · §13 classification

| §13 tier | Verdict |
|---|---|
| Tier 1 (direct gene readout — protein) | **by kind, yes**: this is WWOX protein itself |
| "validated" | **no** — §13 forbids the word without direct sensitivity/specificity evidence in the disease population, and the population here is not WWOX disease |

**What is still missing for a WWOX-DEE pharmacodynamic endpoint** — the full specification, so a
later session does not re-derive it:

1. absolute quantification, not NPX;
2. a measurement in people carrying biallelic WWOX alleles, where the expected level is low or
   absent — **the floor problem**: if the assay cannot resolve a residual level, it cannot measure
   a rise from it;
3. evidence that the vesicle signal tracks brain WWOX dose rather than peripheral WWOX;
4. within-person repeatability and pre-analytical stability;
5. a demonstrated change under a dose intervention — otherwise there is no pharmacodynamics, only a
   cross-sectional difference.

Item 2 is the gating one and no published source satisfies it.

## 3 · Transfer limits

Adults with HIV and mild cognitive impairment; no WWOX genotype; cross-sectional; "neuronal
enrichment" is an immunocapture operation on L1CAM, not demonstrated neuronal origin. Nothing
transfers to any WWOX allele class, and the redox/tau mechanism the authors offer is cited from
older WWOX literature, not measured here.

## 4 · Ops (provisional)

### 4.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record after the current final research-line record) |
| record | `RL-C-20261004w9c2 — WWOX protein is measurable in L1CAM-captured plasma vesicles (relative NPX, singlet, one marked within-sex comparison); a Tier-1 readout by kind, unvalidated, with a five-item specification before it could be a pharmacodynamic endpoint` |
| status | `open` |
| tag | `DATO` for the measurement, `INFERENZA` for the endpoint specification |
| body | §1–§3 of this candidate verbatim |
| class | MINOR |

## 5 · What would change this

- **Would strengthen:** an absolute-quantification assay of WWOX in neuronal-enriched vesicles with
  a published lower limit of detection, run on samples from people with biallelic WWOX alleles.
- **Would falsify the endpoint idea:** vesicle WWOX shown to be unrelated to brain WWOX dose, or
  below the detection floor in the genotype of interest.

## 6 · Brief premise tested

The selection called this "a blood-accessible, neuron-attributed WWOX assay … precisely what a
restoration spec needs for a pharmacodynamic endpoint". **The first half holds; the second does
not** — a relative, singlet, cross-sectional group difference is not a pharmacodynamic endpoint, and
the paper's own WWOX sex statement is not the comparison its figure marks.

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`. The figure entry is an attestation of a panel
read at native resolution, not a string match.

- [PMID 42738875, artefact `files/fulltext/PMID42738875_Tang2026_PMC.xml`] (The reported unit is relative, on a log2 scale, not a concentration. | NPX is Olink's relative quantification unit, expressed on a log2 scale. NPX measures relative change. | Methods 2.7)
- [PMID 42738875, artefact `files/fulltext/PMID42738875_Tang2026_PMC.xml`] (The proximity-extension assay was run in singlet. | Proximity extension assays were performed on the nEV lysates in singlet per manufacturer's instructions | Methods 2.7)
- [PMID 42738875, artefact `files/fulltext/PMID42738875_Tang2026_PMC.xml`] (Neuronal enrichment is an L1CAM immunocapture step. | The second step entails purifying nEV using L1CAM antibodies for selective affinity capture. | Methods 2.2)
- [PMID 42738875, artefact `files/fulltext/PMID42738875_Tang2026_PMC.xml`] (The text states a sex difference for WWOX within cognition group. | and WWOX (WW domain-containing oxidoreductase) were higher in men than in women for the same cognition group | Results 3.4)
- [PMID 42738875, artefact `files/figures/PMID42738875/cells-15-01581-g005b.webp`] (PANEL: the WWOX panels carry no sexes-combined significance bracket and exactly one bracket in the sex-split panel, between two male groups. | [figure attestation - pixels cannot be quote-matched] Figure 5B, WWOX panels: upper panel shows no significance bracket; lower panel shows one bracket with a single asterisk spanning two male groups; all group means lie between about -0.25 and 0.0 NPX. | Figure 5B, WWOX panels)
- [PMID 42738875, artefact `files/fulltext/PMID42738875_Tang2026_PMC.xml`] (The authors call the study exploratory and not confirmatory for any single biomarker. | this exploratory study was not designed to provide confirmatory evidence for any single biomarker | Discussion, limitations)
