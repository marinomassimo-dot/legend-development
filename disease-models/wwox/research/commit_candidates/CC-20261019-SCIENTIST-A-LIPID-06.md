# CC-20261019-SCIENTIST-A-LIPID-06 — review-level transferables of group G1 (cholesterol turnover, VLCFA and neuroinflammation, ELOVL family)

`context_policy: QUESTION_DRIVEN`. **Author:** ACTOR_ID `scientist-a`, metabolic batch G1, 2026-10-19, task `METAB-G1-A-20261019`.
**Status:** `PROPOSED — NOT PROPAGATED`. **Change class: MINOR** (identity records of non-WWOX reviews; no claim touched). `target_wm_version`: next MINOR after the integrator's current value.
**Nothing here is medical advice.** Numbering is provisional. Every source has the word WWOX zero times unless stated; records are comparators and must carry that fact.

## 1 · Landings (this file grows by section as the lot proceeds)

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 39963730 (Kondo 2025, Epilepsia, review of soticlestat mechanisms; sponsor-authored) | `FTR-20261019-39963730-01` | New `PAPER` record (none exists), narrative review, T3, relevance LOW (WWOX absent) |
| 2 | PMID 41704776 (Sahu 2026, iScience, review: VLCFA as regulators of neuroinflammatory pathways) | `FTR-20261019-41704776-01` | New `PAPER` record (none exists), narrative review, T3, relevance LOW (WWOX absent); pointer line on DL-MECH-012 (section 4) |
| 3 | PMID 36969404 (Siddiqui 2023, ACS Omega, review: ELOVL elongases in neurological disease) | `FTR-20261019-36969404-01` | New `PAPER` record (none exists), narrative review with a flagged internal contradiction, T3, relevance LOW (WWOX absent) |

## 2 · Record content (source 1)

What it measures: nothing new; a sponsor-authored narrative review of preclinical data on a brain cholesterol-catabolism enzyme inhibitor. WWOX: zero occurrences.

Note text to carry:
🔴 **A framing source for selection question 4, not evidence about WWOX.** The review's premise is that brain cholesterol is held constant (enzyme knockout leaves total brain cholesterol unchanged) and that more than 95 percent is made in the brain. Efficacy in mice is model-dependent (positive in Dravet, kainate, kindling and audiogenic models; negative in electroshock, subcutaneous pentylenetetrazol and 6-Hz, eight animals per arm), the mechanism is stated undetermined, and the three proposed mechanisms are labelled hypotheses. Authors are employees and stockholders of the drug developer. Whether the route is reachable in WWOX loss of function is open for lack of a measurement; the measurement is a sterol and oxysterol profile plus CH24H expression in Wwox-null and P47T brain.

### LOCATOR TRIPLES FOR BLIND AUDIT (source 1)

1. Sponsor authorship | S.K. and K.N. are employees of, and stockholders in, Takeda Pharmaceutical Company Limited. | Conflict of interest statement, `files/fulltext/PMID39963730_Kondo2025_PMC.xml`
2. Cholesterol held constant | For example, when CH24H was deleted in mice, total brain cholesterol remained unchanged. | Introduction, paragraph 2, same
3. Model-dependent efficacy | Soticlestat was ineffective in the maximal electroshock model of generalized tonic–clonic seizures, a “gold standard” in epilepsy drug screening | Soticlestat section, paragraph 5, same
4. Mechanisms are hypotheses | These potential mechanisms of action, especially the second and third, warrant future studies to gain further insights into the antiseizure effects of soticlestat. | Conclusions, same

## 3 · Record content (source 2)

What it measures: nothing new; a review by a Drosophila lipid group whose own fly study is the central source of its VLCFA to S1P to inflammation mechanism. WWOX: zero occurrences.

Note text to carry:
🔴 **A framing source for the lipid-to-glial-inflammation question, not WWOX evidence.** The review proposes very-long-chain ceramide conversion to sphingosine 1-phosphate in glia and NF-kB or IMD activation as the link between lipid dysmetabolism and neuroinflammation, and itself states that direct causative evidence is lacking, that the trigger and the microglial sensor are unknown, that some X-ALD patients with raised VLCFA stay asymptomatic, and that a severe fly and human but mild mouse ACOX1 phenotype is unexplained. The excess-VLCFA lesion it models (ACOX1, ABCD1) is the opposite of the very-long-species loss in the CerS2 and ELOVL1 papers of this lot, and both are reported to inflame; the direction of any WWOX lipid change is therefore not given.

### LOCATOR TRIPLES FOR BLIND AUDIT (source 2)

5. Causation is not shown | Several studies have now consistently demonstrated the relationship between VLCFA accumulation and neurological disorders, although direct causative evidence is still lacking. | Concluding remarks, `files/fulltext/PMID41704776_Sahu2026_PMC.xml`
6. Trigger unknown | The precise molecular triggers that convert VLCFA accumulation into runaway neuroinflammation are not fully established, including the specific receptors or danger signals sensed by microglia. | Mechanisms, VLCFA-induced oxidative stress, same
7. Asymptomatic carriers of raised VLCFA | Although elevated VLCFA levels are observed across all ALD subtypes, some individuals remain asymptomatic despite biochemical abnormalities. | same
8. Species discrepancy | The discrepancy between severe human/fly phenotypes and relatively mild mouse phenotypes also remains unexplained, raising the possibility of species-specific compensation by ACOX2/3 or alternative β-oxidation pathways. | Insights from disease models in Drosophila, same

## 4 · Op list for `discovery_ledger_current.md` (record-scoped; NOT dry-run by this actor)

The dry-run call of the editing tool against the shared registry was refused by the auto-mode classifier in this session, and was not retried. The `old` string was checked by a word count in this branch's copy of the ledger: it occurs once in the file and inside DL-MECH-012. The integrator should dry-run before applying.

```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-012",
  "old": "**Possibile passo successivo**: NS-020/021;",
  "new": "**Possibile passo successivo**: NS-020/021; 🔵 pointer attached by `CC-20261019-SCIENTIST-A-LIPID-06` (source: PMID 41704776, a 2026 narrative review read in full, WWOX absent): a lipid-derived danger signal (very-long-chain ceramide converted to sphingosine 1-phosphate, then NF-kB or IMD signalling) is the review's proposed link between lipid dysmetabolism and glial inflammation, from one group's fly work, stated by the review as causally unproven. No S1P or sphingolipid measurement exists in any WWOX system; the direction of any WWOX lipid change is not given by it (the mouse CerS2 papers of the same lot show the opposite lesion, loss of very-long species, also with a glial response (astrocytic GFAP rise or an expanded microglial subset)). IPOTESI, not a claim;"
 }
]
```

Status, tag, belief and the existing append-only notes of DL-MECH-012 are unchanged; the pointer is an `IPOTESI`, not a claim, and does not alter the recorded direction of DL-REPO-002.

## 5 · What must NOT be written

- No statement that WWOX loss changes VLCFA, ceramide or S1P levels in any tissue.
- No statement that a lipid change explains the glial or cytokine findings recorded for P47T or other models.
- No medication recommendation (the review's therapeutic classes are listed, untested for WWOX).

## 6 · Record content (source 3)

What it measures: nothing new; a narrative review of the ELOVL elongase family. WWOX: zero occurrences.

Note text to carry:
🔴 **A map of names, with a conclusion the body does not support.** The conclusion says disruption of very-long-chain saturated fatty acid synthesis causes seizures in ELOVL1-deficient humans and mouse models; the body and Table 1 place human seizures with ELOVL4 and list none for ELOVL1, and the recessive ELOVL1 human series read in this lot records none (the mouse knockout has startle-epilepsy deaths). Do not cite this review for human ELOVL1 epilepsy. It states that the brain lipid consequences of ELOVL1 deficiency are unknown, glosses a hippocampal field as caudate amygdala, and is not a source for quantitative statements.

### LOCATOR TRIPLES FOR BLIND AUDIT (source 3)

9. Conclusion overreaches | disruption of VLC-SFA synthesis results to seizures and neurodegeneration in both ELOVL1-deficient humans and ELOVL1 mutant models. | Conclusion, `files/fulltext/PMID36969404_Siddiqui2023_PMC.xml`
10. Seizures attributed to ELOVL4 in the human recessive disease | The seizure activity seen in recessive human ELOVL4 neuro-ichthyotic disease and this pattern are likewise comparable. | ELOVL: Additional Family Members, same
11. Brain lipid consequences unknown | How ELOVL1 deficiency impacts the lipid composition and specific pathological disorders in the brain remains unknown. | Hypomyelination, High-Frequency Deafness, and Spastic Paraplegia, same
12. Anatomical gloss error | The CA3 (caudate amygdala) and CA4 regions of the hippocampus exhibit the highest levels of ELOVL4 expression in neurons | ELOVL: Additional Family Members, same

## 7 · What must NOT be written (whole file)

- No statement that WWOX loss changes very-long-chain fatty acids, sphingolipid chain length, cholesterol, oxysterols or sphingosine 1-phosphate in any tissue.
- No statement that human ELOVL1 disease includes epilepsy on the strength of source 3's conclusion.
- No medication recommendation; the review classes are untested for WWOX.
- No individual-level content; the human ELOVL1 series are cited at class level only.
