# Report Y

## Decision
Arm L. Hypothesis level only; no dose, no clinical recommendation; not medical advice. Reference genotype class: WWOX loss of function in developmental and epileptic encephalopathy.

**Answer: (b), a distinct experiment, and not (a), a pharmacological comparison.**
- The only direct WW1-PPxY interaction I could confirm is WWOX with ERBB4. It was shown with recombinant human proteins and peptides, and in non-neural cells.
- Nothing I found shows a WWOX-ERBB4 interaction or a functional consequence in neurons or interneurons.
- NETO2 has a PPxY-like motif in its cytoplasmic tail. I found no study that tests it with WWOX.
- No compound acts through the WW1-PPxY interaction. A pharmacological comparison is therefore not yet justified.
- The measurement that would change this: show that WWOX WW1 binds ERBB4 or NETO2 in neurons by a PPxY-dependent assay, and that the P47T allele (WW1 PPxY-binding loss) changes the partner's state in vivo.
- Even if it did, the first leverage point would be a probe-level comparison on the partner's own pharmacology, not a repurposing drug.

## Q1 Direct versus only proposed
**Direct (defined domain, motif, species, assay):**
- **WWOX WW1 to ERBB4 PPxY motifs (human proteins and peptides, in vitro).**
  - Schuchardt 2013 used isothermal titration calorimetry (ITC) with human WWOX WW1 (residues 16-50), WW2 and the WW1-WW2 tandem, against 12-mer peptides from the ERBB4 intracellular domain (PY1, PY2, PY3).
  - WW1 bound all three motifs. PY3 affinity was "a little over 100 µM"; PY1 and PY2 were in the "hundreds of micromolar". WW2 showed no binding.
  - The tandem bound more than two-fold more strongly than WW1 alone.
  - Rotem-Bamberger 2022 (NMR, ITC, modelling) used ERBB4 peptides. Abstract only for this paper: WW2 raised the affinity for a dual-motif peptide about 10-fold.
  - These affinities are weak (hundreds of µM for peptides). The authors themselves question whether PY1 and PY2 are physiologically relevant, and caution that short peptides may not mimic the motif in context.
- **WWOX WW1 to full-length ERBB4 in cells.** Aqeilan 2005 (abstract only) reports association through WW1 in HeLa and MCF-7 cells; a mutant WWOX lacking the interaction had no effect. These are human cancer-type cell lines, not neural.
- **WW1 to peptides containing PPPY from Dvl2 and Wbp1 (mouse cerebellar lysate).** Hussain 2023 shows wildtype Wwox is pulled down and Wwox P47T is not. This confirms the loss of PPxY binding in the mouse model. It names neither ERBB4 nor NETO2.

**Only proposed or inferred:**
- **NETO2.**
  - A UniProt retrieval (secondary, via a web summary of Q8NC67) shows human NETO2 carrying a PPHY (PPxY-type) motif in its C-terminal cytoplasmic tail ("...FDPPHYELF...").
  - This is a motif scan only. I found no binding assay with WWOX.
  - Searches found no paper linking WWOX and NETO2 (see Search perimeter).
- **WWOX with ERBB4 in neurons or interneurons.** Not shown in anything I found.
- **Other WWOX partners.**
  - Reviews list AP2-gamma, p73, SIMPLE, Ezrin and WBP1/2 (Schuchardt 2013 introduction, secondary).
  - None of these is neural-specific in what I opened.
  - GSK3-beta (Wang 2012) and Tau bind through the SDR domain, not WW1-PPxY. Abstract only.

## Q2 Observed in pertinent neural systems
- **Direct WW1-PPxY binding in a neural preparation:** only the Dvl2/Wbp1 peptide pull-down in mouse cerebellum (Hussain 2023). This is a binding-capacity test, not a partner discovery.
- **Wwox with Tau, GSK3-beta and others in neuronal cell models:**
  - Wang 2012 used human SH-SY5Y neuroblastoma cells.
  - WWOX bound GSK3-beta through its SDR domain, so this is not a WW1-PPxY partner.
  - Abstract only.
- **ERBB4 and Neto2 in interneurons:**
  - Mennesson 2020 (abstract) reports that Neto2 knockout mice have altered parvalbumin-interneuron maturation in adult amygdala, with increased glutamatergic and reduced GABAergic transmission.
  - Mennesson 2019 (abstract) reports Neto2 in excitatory and inhibitory neurons, and reduced synaptosomal GluK2/3 and GluK5 in Neto2 knockout mice.
  - These show a role for NETO2 in neurons. They say nothing about WWOX.
  - I did not retrieve or open a paper on ERBB4 in parvalbumin interneurons in this session. Any ERBB4-interneuron statement here comes from background knowledge and is unverified.
- **Interneuron relevance of WWOX itself:** Hussain 2019 (abstract only; Wwox knockout mouse, 2 weeks old, both sexes, hippocampus) reports fewer parvalbumin and neuropeptide-Y interneurons and lower GAD65/67. This links WWOX loss to interneurons but not to any partner.

## Q3 Functional consequences
**Measured:**
- **ERBB4 in cells.**
  - Aqeilan 2005 (abstract): in HeLa cells, coexpressed WWOX plus TPA retained ERBB4 in the cytoplasm.
  - Coexpression suppressed YAP-driven co-activation by the ERBB4 C-terminal fragment in a dose-dependent manner. WWOX also inhibited YAP co-activation of p73.
  - Effect sizes and n were not seen at abstract level.
  - Aqeilan 2007 (abstract): in breast cancer, 556 tumours, Wwox expression correlated with membranous ERBB4 (P = 0.0003). Wwox expression in vitro and in vivo led to accumulation of full-length membrane ERBB4.
- **Allele effect in mouse.**
  - Hussain 2023 (full text, results section on seizures): Wwox P47T homozygous mice, n = 3 per genotype, recorded 21-53 h by video EEG.
  - Mutants showed interictal spikes of 0-3098/hour versus 0-68/hour in wildtype, with 11-22 generalised seizures in 43-53 h and no seizures in wildtype.
  - Transcriptome data also showed suppression of GABAergic and glutamatergic synapse pathways in cortex and hippocampus.
  - This links loss of WW1-PPxY binding to epilepsy. It does not say which partner is responsible.

**Only claimed or untested:**
- That WWOX regulates ERBB4 or NETO2 in neurons.
- That the loss of interneurons in the Wwox knockout comes through ERBB4. No study I found tests this.

## Q4 Pharmacological lever
- **No lever exists on the WW1-PPxY interaction itself.**
  - No small molecule against WW1 was found. Affinities are in the micromolar to hundreds-of-micromolar range, a hard target.
  - The only engineering suggestion I opened is the Y85W WW2 variant, a protein-engineering idea, not a drug (Schuchardt 2013).
- **Upstream of ERBB4:** pan-ErbB kinase inhibitors exist (a repurposing-class lever), but they act on the kinase and would reduce signalling. The WWOX loss-of-function hypothesis would instead predict altered ICD handling, so the direction is unclear. I did not retrieve any source on selectivity or alternative actions in this session, so no further claim is made.
- **NETO2:** this is a kainate-receptor auxiliary subunit (Han 2016 review, abstract; Griffith 2015, abstract). A lever, if one exists, would be on kainate receptors (GluK-selective probes), and NETO2 modulation changes kainate receptor desensitisation and agonist sensitivity. This acts downstream of NETO2, not on any WWOX interaction. I have no source on specific compounds, so none is proposed.
- **Repurposing drug versus experimental probe:** at present everything here would be a probe-class tool (kainate-receptor probes, ERBB4 genetic or antibody tools). I found no approved drug whose action maps onto the WW1-PPxY branch.

## Q5 Not supported
- **Species and cell transfer.** The ERBB4 interaction evidence is human recombinant protein or human and monkey cell lines (HeLa, MCF-7, COS), plus breast cancer tissue. Nothing is shown in rodent or human neurons.
- **Direction.** The cytoplasmic retention and YAP-suppression effects come from epithelial or cancer cells. Their direction in neurons or interneurons is unsupported.
- **Age.** The Wwox knockout interneuron findings are from 2-week-old mice, a stage with early lethality in knockouts. The P47T mice survive past one year. Do not transfer either to older or human ages.
- **NETO2.** A motif is not a partner. Do not transfer the NETO2 kainate-receptor findings (amygdala, fear conditioning, adult mice) to WWOX-related epilepsy.
- **Disease.** The ERBB4 data come mostly from breast cancer. They do not show relevance to developmental and epileptic encephalopathy.
- **Absence claims.** No paper found linking WWOX and NETO2, and none linking WWOX and ERBB4 in neurons, within the perimeter below. This is an absence of retrieved evidence, not proof that no such study exists.

## Q6 Improving a comparison or generating an experiment
**Hypothesis kept (partner branch via ERBB4 or NETO2 in interneurons):**
- **Observation:**
  - WW1 binds ERBB4 PPxY motifs in vitro.
  - Wwox P47T abolishes PPxY binding (mouse cerebellar lysate) and causes epilepsy in mice.
  - Wwox knockout mice lose parvalbumin interneurons (2 weeks, hippocampus).
  - NETO2 has a PPHY motif and is expressed in interneurons.
- **Relation:** WWOX WW1 binds ERBB4 and perhaps NETO2 through PPxY in interneurons. Proposed, not established.
- **Hypothesised action:** loss of WW1 binding changes ERBB4 intracellular-domain localisation or turnover, or NETO2 kainate-receptor regulation, in interneurons. This would give an interneuron excitability defect.
- **Context:** Wwox P47T and knockout mouse brain, parvalbumin interneurons in hippocampus and cortex, at ages before and after seizure onset.
- **Distinct experiment (not a drug comparison):**
  1. Do a co-immunoprecipitation or proximity-ligation test of Wwox with Erbb4 and with Neto2 in wildtype versus P47T mouse brain or interneurons, with a PPxY-mutant control for each partner. Use the Dvl2/Wbp1 pull-down as positive control.
  2. In parallel, measure Erbb4 intracellular-domain localisation and Neto2/kainate-receptor currents in parvalbumin interneurons of wildtype versus P47T mice.
- **Pharmacological comparison, only after step 1 is positive:** compare ERBB4 pathway tools against kainate-receptor probes for rescue of interneuron excitability in P47T slices.
- **Prediction:** P47T disrupts Wwox-Erbb4 (or Wwox-Neto2) binding in brain, and the partner readout shifts in the direction opposite to a gain of partner function.
- **Result that would reject it:** the partner binds Wwox equally in wildtype and P47T brain, or the interaction is absent in interneurons, or partner readouts are unchanged in P47T mice.
- **If rejected:** "no compound is justified yet" stands, and the branch is closed for these two partners.

## Search perimeter
- **PubMed (searches run 2026-11-19, no date limit):**
  - `WWOX ERBB4 WW domain PPxY` (2 hits)
  - `WWOX ErbB4 interaction` (8)
  - `WWOX NETO2` (0)
  - `Neto2 PPxY OR "WW domain" OR WWOX` (no WWOX-Neto2 hit among the first 10 returned)
  - `WWOX WW domain binding partners neurons` (2)
  - `WWOX interneuron OR hippocampal OR synapse ErbB4 OR Neto2 OR kainate` (too broad, scanned only the first 15)
  - `Wwox ErbB4 parvalbumin interneurons epilepsy` (0)
  - `Wwox knockout mouse brain hippocampal neurons interneurons GABAergic` (1)
  - `WWOX AND (neurons OR brain) AND (interacts OR binds OR co-immunoprecipitation) AND (WW domain)` (25, first 20 reviewed by title)
  - `Neto2 interneuron OR "kainate receptor auxiliary" OR KCC2 NETO2` (80; first 10 returned, 5 reviewed)
  - `Repudi Aqeilan neuronal deletion Wwox epilepsy brain malformations` (0; this paper was not retrieved by this query, so it is not assessed)
- **Europe PMC REST:** `WWOX AND NETO2` (11 hits, first 10 titles are unrelated bioinformatics and cancer papers); `WWOX AND (ERBB4 OR ErbB4) AND (neuron OR interneuron OR brain OR hippocamp*)` (110 hits, first 15 titles scanned; none is a WWOX-ERBB4-neuron primary study).
- **UniProt REST:** NETO2 human entries, PPxY scan.
- **Not searched:** BioGRID or other interaction databases, preprint servers directly, patents, non-English literature.

## Pivotal claims
| claim | source | locator | depth |
|---|---|---|---|
| WW1 binds all three ERBB4 PPxY peptides (PY3 a little over 100 µM; PY1/PY2 hundreds of µM); WW2 does not; tandem more than 2-fold stronger | Schuchardt, 2013, Biochemistry | Results (ITC), conclusions | full text |
| WW2 raises WWOX affinity for a dual-motif ERBB4 peptide about 10-fold | Rotem-Bamberger, 2022, J Biol Chem | abstract | abstract only |
| WWOX binds full-length ERBB4 through WW1 in HeLa and MCF-7 cells; cytoplasmic retention; YAP co-activation suppressed | Aqeilan, 2005, Cancer Res | abstract | abstract only |
| Wwox expression associated with membranous ERBB4 in 556 breast cancers | Aqeilan, 2007, Cancer Res | abstract | abstract only |
| P47T Wwox fails to bind Dvl2/Wbp1 PPPY peptides (mouse cerebellar lysate); P47T mice have spontaneous seizures, interictal spikes 0-3098/h vs 0-68/h (n = 3 per genotype) | Hussain, 2023, Prog Neurobiol | Results 2.1 and 2.3 | full text |
| Wwox knockout (2-week mouse hippocampus) has fewer PV and NPY interneurons and lower GAD65/67 | Hussain, 2019, Neurobiol Dis | abstract | abstract only |
| NETO2 human C-terminal tail carries a PPHY motif | UniProt Q8NC67 (via web summary) | sequence tail | secondary |
| Neto2 knockout: altered PV interneuron maturation in adult amygdala; lower synaptosomal GluK2/3, GluK5 | Mennesson, 2020, eNeuro; Mennesson, 2019, Neuropsychopharmacology | abstracts | abstract only |
| WWOX binds GSK3-beta through its SDR domain (SH-SY5Y) | Wang, 2012, Cell Death Differ | abstract | abstract only |
| No retrieved study tests WWOX with NETO2 | own searches | Search perimeter | absence, perimeter stated |

## Limits
- Most claims rest on abstracts. Only Schuchardt 2013 and Hussain 2023 were opened as full text, and for Hussain 2023 I read only selected passages found by keyword search, not the whole paper or its figures and legends.
- The NETO2 motif comes from a web summary of UniProt, not from my own inspection of the sequence.
- The ERBB4-in-interneuron background (neuregulin signalling and parvalbumin synapses) was not verified in this session, and I did not open the ERBB4 or ErbB4-in-brain reviews that Europe PMC returned.
- I did not identify other neural PPxY partners from the literature beyond those named; a systematic partner list (for example from interaction databases or a Wwox P47T versus wildtype brain pull-down mass spectrometry) was not found and not searched for outside PubMed and Europe PMC.
- Pharmacology (Q4) is thin because I retrieved no source on specific compounds, selectivity or off-target actions; no compound is named for that reason.
- Effect sizes and n for the cell-line ERBB4 findings were not visible at abstract level.