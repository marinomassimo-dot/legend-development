# CC-20261003W5-A-TRANSGENE-IMMUNITY-01 — a recessive-null patient is CRIM-negative, so transgene immunity is the WWOX programme's problem and no preclinical package in this set has tested it

- `context_policy: SOURCE_FIRST`
- Sources (all first reads, all `partial_fulltext_read`, figure panels not rendered):
  PMID 41314141 (`FTR-20261003-41314141-01`), PMID 39358605 (`FTR-20261003-39358605-01`),
  PMID 41712282 (`FTR-20261003-41712282-01`), PMID 40809677 (`FTR-20261003-40809677-01`),
  PMID 41712149 (`FTR-20261003-41712149-01`). All five manifests validate
  (`deepdive_manifest.py --verify-artifacts --require-current-schema`, VERDICT: PASS).
  **None of the five mentions WWOX.** Every statement is a transferable lesson from another gene
  with its transfer limit stated.
- Change class: **MINOR**. It narrows no `consolidated baseline` claim; it adds one research-line
  record and one research-candidate record, both in the research layer, and both are statements
  about a risk that has not been measured.
- **Nothing here is medical advice.**

## The finding, in one sentence

A WWOX-DEE patient with two loss-of-function alleles makes no WWOX protein, and the clinical
literature has a name and a protocol for exactly that situation — **cross-reactive immunological
material (CRIM) negative**, which in the only first-in-human high-dose intrathecal AAV9 trial in
this set triggered a *third* immunosuppressant specifically to prevent an immune response to the
gene product — while the one complete IND-enabling package for a recessive loss-of-function CNS
disease tested transgene immunogenicity **only in wild-type animals**, i.e. only in animals that
already express the protein, and dosed them in the first days of life.

## Why this corrects a premise the wave-5 assignment carried

The assignment's note on PMID 40809677 reads: *"Cas9 is a bacterial protein and maximally
immunogenic — WWOX is a self protein, so the transfer is to vector and route immunity, not to
transgene immunity."* **The premise is false for a null.** "Self" is defined by what the patient's
immune system has seen, not by the species of the coding sequence. PMID 41314141 operationalises
this: patients with *"predicted null mutations (no residual endogenous MFSD8 protein)"* were
classified CRIM-negative and given prednisone **plus** sirolimus **plus** tacrolimus, where a
patient predicted to make some protein got two drugs. A biallelic WWOX null is in the first group.
Transgene immunity therefore transfers to a WWOX programme, and it is the parameter this group of
sources leaves least measured.

## What each source contributes, with its transfer limit

| Source | Contribution | Transfer limit to WWOX-DEE |
|---|---|---|
| **PMID 41314141** (human, phase 1, n = 4, CLN7, intrathecal AAV9, 5×10^14 and 1×10^15 vg) | The CRIM stratification itself, applied prospectively in children; three CRIM-negative patients on triple immunosuppression had no positive anti-capsid or anti-transgene ELISpot and normal CSF across 24 months | The protocol transfers (it is defined by residual protein, not by gene); the *result* does not — n = 4, open label, no transgene-expression measurement in any patient, and the regimen is confounded with the outcome, so it shows that triple immunosuppression was compatible with no detected response, not that a null tolerates the protein |
| **PMID 39358605** (AP4B1, the closest architectural analogue: recessive, loss-of-function, full IND package) | The gap. Safety study 1 used *wild-type* C57BL/6 mice dosed at P1–3; the GLP primates were wild type; the only immune assay is an IFN-γ ELISpot against a peptide library, with no antibody assay anywhere — although the Fig. EV5 title claims "no B cell response" | Methodologically the closest transfer available, and the omission transfers with it: a regulatory immunogenicity package assembled this way would not detect a response that only a protein-naive host can mount |
| **PMID 41712282** (SLC13A5, knockout mouse, human transgene) | The one setting in this group that *is* a protein-naive host receiving a foreign protein — and it reports **no immune endpoint at all**: no antibody, no T cell, no CNS inflammatory histology, no DRG | Confirms that the measurement is not merely unpublished for WWOX but routinely unmade for recessive nulls |
| **PMID 40809677** (Cas9 in mouse CNS, neonatal versus adult) | The mechanism and its four limits: early expression buys *cellular* tolerance (sustained transgene, no neuronal loss, MHC II "virtually absent", no CD3) but **not humoral** tolerance ("neither treatment time point circumvented eliciting a humoral immune response"); the protection does **not** transfer to a later dose (a redose after a neonatal prime still cost 25.3% of neurons); and it is antigen-specific — EGFP in the same compartment at the same age caused neither toxicity nor inflammation | Transfers as mechanism, not magnitude: the antigen is bacterial, the host wild type, and the adult arm received four times the vector, so age and antigen load are not separated. What transfers strongly is the **promoter warning**: tolerance is thought to need MHC II-dependent regulatory T cells, neurons do not express MHC II, and the authors suspect their neuron-specific promoter "may have hampered the development of Cas9-reactive Tregs" |
| **PMID 41712149** (review) | The paediatric CSF cost of repeated intrathecal dosing, quantified: transient CSF protein elevations above 50 mg/dL in approximately three-quarters of children in the extension studies of an antisense programme | Review-level and a different modality (oligonucleotide, not vector); it bounds what "asymptomatic CSF change" looks like at scale, against which PMID 41314141's single pleocytosis event is one patient |

## The consequence that is actionable

The three design choices a WWOX cassette must make — **promoter breadth, age at dosing and
immunosuppression regimen** — are not independent, and the direction of two of them is opposite to
the intuition the repository has been carrying:

1. A **neuron-restricted** promoter is the safer choice for overexpression toxicity (PMID 41314141
   attributes dorsal-root-ganglion toxicity to transgene overexpression and credits its weak JeT
   promoter) but may be the **worse** choice for tolerance induction (PMID 40809677).
2. **Early dosing** buys cellular tolerance but not antibodies, and buys nothing for a second dose —
   so "treat neonatally" does not retire the immunosuppression question, it only changes which arm
   of it binds.
3. A WWOX null is **CRIM-negative**, so the regimen that the only human source in this set used for
   that class is three drugs, not two — and the one immune event it reports occurred in the single
   patient managed with two.

## Ops (provisional ids; anchors and next-free numbers re-measured at commit time)

### 1 · `disease-models/wwox/research/research_lines_current.md` — `append` (new record)

Exact text to append (the next free `RL-GT-` number measured 2026-10-03 is **RL-GT-002**;
`registry_records.py catalog` is re-run by the integrator before applying):

```
---

## RL-GT-002 — Transgene immunity in a protein-naive host: the unmeasured parameter of a WWOX gene-replacement programme
**Status:** emerging — the risk is named and unmeasured
**Primary pathway:** P7 (gene therapy design), immune interface
**Evidence base:** PMID 41314141 (`FTR-20261003-41314141-01`), PMID 39358605 (`FTR-20261003-39358605-01`), PMID 41712282 (`FTR-20261003-41712282-01`), PMID 40809677 (`FTR-20261003-40809677-01`), PMID 41712149 (`FTR-20261003-41712149-01`) — none of which mentions WWOX
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** a patient with two loss-of-function WWOX alleles makes no WWOX protein and is therefore cross-reactive-immunological-material (CRIM) NEGATIVE. In the only first-in-human high-dose intrathecal AAV9 trial read by this repository, that classification prospectively triggered a third immunosuppressant specifically against a response to the gene product. The inference that WWOX is "a self protein" and so poses only vector-and-route immune risk is therefore WRONG for a biallelic null, and was corrected here. Against that, the one complete IND-enabling package for a recessive loss-of-function CNS disease in this corpus tested transgene immunogenicity only in WILD-TYPE animals dosed in the first days of life, with an interferon-gamma ELISpot and no antibody assay; and the one study in this corpus that did put a foreign protein into a knockout host reported no immune endpoint at all. Three design choices interact and two run against intuition: a neuron-restricted promoter lowers overexpression risk but may impede MHC II-dependent regulatory T-cell tolerance; early dosing buys cellular but not humoral tolerance and buys nothing for a second dose.
**Next action:** before any WWOX cassette is specified, state which CRIM class the reference genotype falls in and design the immunogenicity experiment in a protein-NAIVE host at the intended age of dosing, with both a T-cell and an antibody readout. Do not inherit a wild-type-animal immunogenicity package as evidence of tolerance.
```

### 2 · `disease-models/wwox/research/research_candidates_current.md` — `append` (new record)

```
### RC-A-20261003w5-01 — Design the WWOX transgene-immunogenicity experiment in a protein-naive host, not in a wild-type animal

**Gap:** every immunogenicity measurement in the 2024–2026 recessive-CNS gene-replacement sources
read in intake wave 5 was made in an animal that already expresses the orthologue of the delivered
protein, or was not made at all.

**Shape of the experiment:** a WWOX-null host, dosed at the intended clinical age rather than at
P1–3, with (i) a T-cell readout against a WWOX peptide library, (ii) an anti-WWOX antibody readout,
(iii) an anti-capsid readout, and (iv) CNS histology for MHC II and CD3 — the four readouts that
PMID 40809677 shows can dissociate, since early expression suppressed (i), (iii as presented) and
(iv) while leaving the antibody response intact.

**Limits carried from the sources:** PMID 40809677's antigen is bacterial and its host wild type,
and its adult arm received four times the neonatal dose, so it bounds mechanism and not magnitude;
PMID 41314141's negative ELISpots were obtained under triple immunosuppression, so they are not
evidence that an unsuppressed null tolerates the protein; PMID 39358605's clean ELISpot was obtained
in wild-type mice and cannot be read across to a null.
```

## What would change the model if true, and what would falsify it

**Would change it:** a published immunogenicity study of any gene-replacement product in a
**null** animal, at a non-neonatal age, with both cellular and humoral readouts — that converts this
from a named gap into a measured parameter and sets the immunosuppression requirement. **Would
falsify the central claim here:** evidence that WWOX protein is presented to the immune system of a
biallelic-null patient as self (for example, a truncating allele that still yields an epitope-complete
fragment across the relevant HLA space), which would move the reference genotype into the CRIM-positive
class and reduce the requirement to the two-drug regimen.

### LOCATOR TRIPLES FOR BLIND AUDIT

(Immunosuppression intensity was assigned by whether the patient was predicted to make any of the protein. | would be considered CRIM positive and placed on immune modulation with enteral prednisone and sirolimus | Methods, study design, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(Patients predicted to make no protein were given a third immunosuppressant. | would be considered CRIM negative and placed on enteral prednisone, sirolimus, and tacrolimus for immune modulation | Methods, study design, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(The only immune event occurred in the one patient managed with two rather than three immunosuppressants, after the steroid taper. | experienced a clinically asymptomatic CSF pleocytosis after weaning off corticosteroids at six months post-injection | Discussion, immunosuppression paragraph, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(The authors attribute dorsal-root-ganglion toxicity to transgene overexpression and name the weak promoter as a mitigation. | recent studies suggest this is due to transgene overexpression | Discussion, dose paragraph, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(The immunogenicity study was run in wild-type animals, which already express the orthologue. | Safety studies in WT mice included study 1: ELISpot reactivity | Results, non-GLP safety, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(Those animals were dosed in the first days of life, when tolerance is most readily induced. | Wild-type mice C57BL/6 (P1-3) were administered control vector | Methods, ELISpot safety study, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(The only immune assay measures T-cell interferon release; no antibody assay is reported. | This assay detects INF-γ secretion from activated T cells in response to a stimulant | Results, non-GLP safety, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(Early expression did not prevent an antibody response at either age. | neither treatment time point circumvented eliciting a humoral immune response | Discussion, `files/fulltext/PMID40809677_DubaKiss2025_PMC.xml`)

(Neonatal priming reduced but did not abolish the harm of a later dose. | lowers, but does not entirely eliminate, the neurotoxic and inflammatory effects of administering this construct to the adult CNS | Results, redosing, `files/fulltext/PMID40809677_DubaKiss2025_PMC.xml`)

(A different foreign protein in the same compartment at the same age caused neither toxicity nor inflammation. | indicating that EGFP did not elicit neurotoxic or neuroinflammatory responses | Results, EGFP comparison, `files/fulltext/PMID40809677_DubaKiss2025_PMC.xml`)

(A neuron-restricted promoter may itself impede tolerance induction. | the use of the SynI promoter may have hampered the development of Cas9-reactive T | Discussion, `files/fulltext/PMID40809677_DubaKiss2025_PMC.xml`)

(The adult arm received four times the vector of the neonatal arm, so age and antigen load are not matched. | the doses administered to adult mice were four times higher than to neonatal mice | Results, expression and neurotoxicity, `files/fulltext/PMID40809677_DubaKiss2025_PMC.xml`)

(The antibody does not detect the endogenous mouse protein, so there is no wild-type reference for expression level. | the NaCT antibody does not recognize endogenous mouse NaCT protein | Results, functional NaCT, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(Transient cerebrospinal-fluid protein elevation affected about three-quarters of children on long-term intrathecal dosing. | occurred in approximately three-quarters of patients in the extension studies | RNA therapies, STK-001, `files/fulltext/PMID41712149_Balestrini2026_PMC.xml`)
