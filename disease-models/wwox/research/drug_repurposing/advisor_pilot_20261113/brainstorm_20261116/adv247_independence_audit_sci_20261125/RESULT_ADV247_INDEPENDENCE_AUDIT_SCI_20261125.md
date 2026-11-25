# ADV-247 result: independence audit of the carried small-n transcript inferences (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; nothing here is medical advice. Held papers and files plus free GEO sample records; no spend, no contact, no delegate. Pre-registration: `PREREG_ADV247_SCI_20261125.md` (committed before any source was reopened for this task). Full table: `independence_adv247.tsv` (built by `build_adv247.py` from the ADV-239 ranking).

## 1. Answer

Of 35 carried inferences:

| Disposition | Inferences | Share | Which |
|---|---|---|---|
| non-independent | 13 | 0.37 | every organoid row (O1 to O13) |
| independent | 15 | 0.43 | the eleven P47T rows (T), M3, C1, S1, H2 |
| not stated | 7 | 0.20 | M1, M2, M4, M5, M6, M7 (hippocampal libraries), H1 (neurosphere RNA-seq) |

1. **The inflated n is in one deposit, and it is the most used one.** Only the organoid rows count units that are not independent: the stated 4 v 2 is **one CRISPR clone against one parental line** (ADV-244). They are 8 of the 12 most consumed rows.
2. **"Independent" does not mean adequate.** C1 and S1 are independent only because their n is already 1 per arm. Of the 12 most consumed rows, 8 are non-independent, 3 independent, 1 not stated.
3. **P47T regions are the same animals.** Each region has its own mice as units (5 v 5; cerebellum 4 v 3), but hippocampus, prefrontal cortex, parietal cortex and cerebellum come from the same mice. "In all four regions" is one set of animals seen four times.
4. **The single-nucleus and hippocampal unit gaps were already on record**, in IT's identity audit of 1 November (`drug_repurposing/gse158684_identity_it14_p1a_20261101/identity_table.tsv`, rows 15 and 20) and my own amendment 4B.1 of 16 November: four GEO records per genotype against n = 1, with three readings the deposit cannot separate (one library registered four times; four animals pooled into one load; four libraries merged); one sample per animal assumed in the bulk deposit but not stated. This audit adds nothing to those facts. It corrects ADV-239's short form "one pool per genotype", which picks one reading: say "one dataset per genotype; number of animals not stated".

## 2. Unit statements, two reads each

| Deposit | First read | Second read | Unit |
|---|---|---|---|
| GSE156243 organoid (PMID 34268881) | methods and review file: two clones "selected for the organoid generation"; 4 KO and 4 WT organoids sequenced | ADV-244 reads: all four KO libraries carry one clone's alleles | one clone v one line |
| GSE215425 P47T (PMID 36828035) | paper and GEO extract protocol: "n=5 mice/group (2 males, 3 females)" | GEO sample titles carry the mouse id, repeated across regions | mouse |
| GSE158682 cortex (PMID 33914858) | GEO: "Cortices were collected from S-Control (n=4) and S-KO (n=3) mice at P17" | paper, Figure 3 legend: "cortex (total n = 7, S-Control, n = 4; S-KO, n = 3)" | mouse |
| GSE158681 hippocampus | GEO: "hippocampi were collected at P17" | same legend: "hippocampus (total n = 5, SControl, n = 2; S-KO, n = 3)" | **not said to be one mouse each** |
| GSE158684 single nucleus | paper, Figure 3 legend: "S-Control (n = 1) and S-KO (n = 1)" | GEO series design (3182 and 2920 nuclei) and barcode suffix `-1` only in both matrices | one dataset per genotype; animals not stated |
| GSE126075 CAGE (PMID 31543760) | paper: shRNA-transduced progenitor line, control "scrambled shRNA" | GEO series design: H9-derived neural stem cells, silenced v native, before and after differentiation; one record per condition | one population per arm |
| Hussain 2019 qRT-PCR (PMID 30290271) | results: "Wwox KO (n = 4) mice in comparison to Wwox WT (n = 4) mice" (Il6) | Figure 6 legend: qRT-PCR 4 v 4 hippocampi | mouse |
| Hussain 2019 neurosphere RNA-seq | Figure 6 legend: "KO mice (n = 2) relative to Wwox WT (n = 3)" | methods: neurospheres generated from newborn hippocampi; no per-library animal | **not stated** |

For GSE158681 the likely reading is one mouse per library; the sources read here do not say it, so the pre-registered code is "not stated". Litter is not stated for any deposit.

## 3. Predictions

| | Prediction | Outcome |
|---|---|---|
| P1 | non-independent share between 0.35 and 0.55 | Met (0.37), and entirely from one deposit |
| P2 | no animal-deposit inference is non-independent | Met; but six of them are "not stated" |
| P3 | the Hussain neurosphere unit is not stated | Met |
| P4 | at least one "not stated" that streaming cannot settle | Met (germline mice: no edit to read) |

The rejecting observation (nothing but the organoid rows differs) is **partly met**: no further inflated n was found. What the generalisation adds is the same-animal structure across P47T regions, seven unstated units and the correction in point 4.

## 4. Proposed wording for IT

| Where | Wording |
|---|---|
| organoid rows (K01, D01, D02, M01, E02, I01, INV-16, RP-008, CLAIM 002) | as already placed from ADV-244: one clone against the parental line |
| any card citing P47T "all three / four regions" (K01 and others in the table) | "in regions taken from the same mice" |
| S1 consumers (INV-15, RP-019, RP-038, RP-017) | "one single-nucleus dataset per genotype; number of animals not stated; nuclei are not replicates" |
| M1, M4 and the hippocampal part of M2, M5, M6, M7 | "hippocampal arms of 2 or 3 libraries; one mouse per library is not stated" |
| H1 (trigger T19) | add "neurosphere libraries not tied to individual pups" |
| C1 consumers (INV-02, I01, RP-038, RP-033, CLAIM 014) | "one shRNA population per arm in one cell line; the two stages are not independent knockdowns" |

CLAIM text changes only through a candidate. Nothing was edited outside this folder.

## 5. Limits and what was not done

* **Streaming-read method not used:** no open unit question turned on a published edit.
* **Not established:** what the four GEO records per genotype of GSE158684 are. No run exists to read: IT's audit records the eight SRA experiments as held until publication. Before finding that audit I queried ENA (no run row) and NCBI's E-utilities, which answered 429 after my requests came too close together; I stopped using that service.
* Seven unit statements rest on one article each (and its deposit); no author was asked.
* "Independent" is about the stated n only: not litter, batch, sex balance or power.
* Secondary-tier (non-WWOX comparator) deposits are outside the 35 rows.
* No second reader.

## 6. DREAM

Not yet consumed: the same-animal wording for P47T regions. Re-check trigger already on record: release of the GSE158684 SRA experiments.

Process: my duplicate check was again too narrow (as in ADV-242): I treated the eight records as new and had drafted that no file mentioned them; a search by sample accession, run before committing, found three that did.
