# P3-15 dichloroacetate: REFERENCE-ONLY (edge and valence question added; pharmacology reused)

Scientist-a3, 2026-10-30. Not medical advice; no dose, route or schedule recommended.

**Reused, not repeated.** Identity, per-isoform potency, matched comparator, exposure and cards: `../pharmacological_qualification_it8_p3_20261029/` and `../qualification_it9_p4a_20261030/` (PDK1-4 same-document profile, VER-246608 comparator, cards E03 and I01, work order NEED-PDH-PYRUVATE-AXIS). The ChEMBL pulls here (sodium salt CHEMBL306823, 97 of 97 rows; acid CHEMBL13960, 124 of 124 rows) are not interpreted again; the identity note stands: mechanism on the salt record, rows on the acid record. Trials: 27 studies for dichloroacetate; with seizure 1 (MELAS, NCT00068913); intellectual disability 2 (pyruvate dehydrogenase complex deficiency, NCT06931262, NCT02616484); 0 for epilepsy, DEE, hypomyelination, neurodevelopmental disorder, cerebral palsy.

## The added question: PDK1 is both a seed and the target, and the observations disagree in sign
| Observation (IT9 P1 seeds) | System | PDK transcript | Reading |
|---|---|---|---|
| S022 PDK1 | WWOX-KO organoid week 15 (4 KO v 2 WT) | centred log2 -0.385; mean CPM 14.5 vs 18.5 (ratio 0.78) | lower in sign; inside the single-gene null (p about 0.30) |
| S022 PDK1 | shWWOX hNPC (CAGE, one library per arm) | -0.674; TPM 3.56 vs 5.16 | lower in sign; Poisson interval spans zero |
| S022 PDK1 | neuron d14 library | +0.442 | higher; disagrees |
| S113 PDK family | non-neural fibroblast WWOX sgRNA line | higher, p<0.05 | higher; non-neural; isoform not stated |
| S024 PDHA1 | organoid / hNPC / neuron d14 | +0.968 / +0.145 / -0.091 | uncertain |
(The CPM ratio in the organoid was recomputed here from the counts file with the existing descriptive script `gse156243/gene_rows_cpm.py`; descriptive only, no test.)

**Edge side.** HIF1A -> PDK1 (+1) is a heavily referenced transcriptional record (102 reference tags; SIGNOR, CollecTRI, GEREDB, ExTRI), the references were not itemised or opened here, so its neural context is UNVERIFIED; it predicts PDK1 UP when a HIF-1 glycolytic program is up. The same samples show SLC2A1 (CPM ratio 2.67), LDHA (1.70) and PDHA1 (2.02) up with HIF1A transcript slightly lower (0.84): glycolysis transcripts up without the HIF1A transcript rising, PDK1 down in sign, PDHA1 up. The edge therefore predicts the opposite of two of the three PDK1 observations.

**Valence.** Dichloroacetate acts on PDK protein activity (inhibition). With the seed taken as "PDK1 transcript down" and protein activity following, dichloroacetate MIMICS the shift (more PDH flux); taken as "PDK1 up" it OPPOSES it. P2 test T3 reports exactly this: RECOVERED_ONLY_VIA_OWN_TARGET, the result flips with the assumed PDK1 direction. The engine output for dichloroacetate therefore contains no information beyond the seed itself, and a transcript is not an activity: three conditional statements are possible (H-down-mimics, H-up-opposes, H-no-protein-change-uninformative), none resolved here.

**What would discriminate** (already the registered premise test; restated as the readout): PDH E1alpha phosphorylation and PDH activity, pyruvate and lactate, 13C-glucose label into TCA intermediates versus lactate, in WWOX-deficient and control neural cells, with dichloroacetate and a nanomolar PDK inhibitor of different chemistry as orthogonal arms. Adaptive versus harmful valence: viability and network activity under normoxia and low O2 in the genotype-by-compound interaction. A null with dichloroacetate alone is not read as absence of a PDK effect (IT8 P3).

Decision: REFERENCE-ONLY. UNVERIFIED: PDK1 protein or activity in any WWOX-deficient neural system (none measured); human plasma Cmax (UNKNOWN since IT8 P3).
