# Second independent verification of needs.json (7 needs, 18 observations)

Actor scientist-d. Read-only toward needs.json; this file is the only output. The earlier verification file was not read before the verdicts were fixed. Sources opened: deepdive manifests, full-text files in files/fulltext, mechanism_intervention_map, splice_allele_rna_evidence note, cards_early packets, registry records via registry_records.py, live HGNC REST (read-only, no registration, no contact).

Needs audited: NEED-WWOX-SPLICE-CORRECTION, NEED-WWOX-MISSENSE-PROTEIN-RESCUE, NEED-WWOX-ENDOGENOUS-BOOST, NEED-INHIBITORY-HYPOFUNCTION, NEED-SEIZURE-CONTROL-SYMPTOMATIC, NEED-T-TYPE-CALCIUM, NEED-NEUROINFLAMMATION-GLIA.

## Counts (18 observations)

SUPPORTED 12 · OVERSHOOT 4 · UNDERSHOOT 1 · UNVERIFIABLE 1 · NOT_IN_SOURCE 0.

## Verdicts

| Need / obs | Verdict | Note |
|---|---|---|
| SPLICE O1 (c.517-2A>G, blood cDNA 504 vs 593/504) | SUPPORTED | Manifest entries 0-4 match; blood limit stated. |
| SPLICE O2 (c.1057-2A>G prediction only) | SUPPORTED | "SpliceAI 0.96" is DS_AL (acceptor loss); cryptic gain DS_AG is 0.64 at +8. State which score. |
| MISSENSE O1 (Q230P fibroblast) | SUPPORTED | Transcript comparison rests on manifest entries 3 and 4, not cited; only 6 and 7 are. |
| MISSENSE O2 (P252A/P282A) | OVERSHOOT | See C3, C4. |
| ENDOG O1 (fly CRISPRa) | SUPPORTED | Entries 71, 72, 82 match. |
| ENDOG O2 (Q230P) | SUPPORTED | Same locator gap as MISSENSE O1. |
| INHIB O1 (sIPSC 57.3 vs 27.5) | SUPPORTED | "Control" is pooled WT+HET (S-CTL); P13-17; IPSC frequency also reduced. |
| INHIB O2 (PV, GAD, NPY) | OVERSHOOT | Data right; limits wrong, see C5. NPY (30 percent reduction in DG only) is in the text but has no locator. |
| INHIB O3 (organoid GAD1/GAD67/NPY) | SUPPORTED | Entries 30 and 34 match. |
| INHIB O4 (P47T GO/KEGG) | SUPPORTED | Hippocampal KEGG "suppression" rests on running text (S11/S12 text) only; entry 32 panel covers cortex only. |
| INHIB O5 (GABRB2/3 panel) | SUPPORTED | Recomputed from the TSV: GABRB2 KO mean 2.71 vs WT 10.17 (0.27); GABRB3 18.5 vs 37.7 (0.49); GAD1 about 11.6-fold. WT n=2 and GAD1 WT values 3.46 vs 0.20: say so. |
| SEIZ O1 (ketogenic diet, 3 of 5) | OVERSHOOT | See C6, C7. |
| SEIZ O2 (vigabatrin) | UNDERSHOOT | See C8. |
| SEIZ O3 (CBD, ACTH, etc.) | UNVERIFIABLE | Only queried-not-read curated rows; no source-level text opened. |
| T-TYPE O1 (ethosuximide PTZ) | SUPPORTED | Manifest 1, 25, 26, 27, 30 match; hedges are accurate. |
| NEUROINF O1 (IBA1/GFAP, Il6) | OVERSHOOT | Limits import confounder, see C5. n=4 per group is in the source text but has no locator. |
| NEUROINF O2 (P47T) | SUPPORTED | Source says ">= 2-fold, n=6"; panel means are about 1.9x (Il1b) and about 3.3x (Tnfa): "at least twofold" is the authors' wording. |
| NEUROINF O3 (AAV9 GFAP) | SUPPORTED | S8I (WT 5, KO 44, treated 5) matches entry 9. |

## Corrections list

C1. SPLICE direction rationale ("A null-like splice allele predicts..."): the same repository note shows the +8 cryptic acceptor gives opposite frame outcomes under two coordinate conventions. Reading A is an in-frame 6 nt deletion, which would be a hypomorph, not a null. Add this to INFERRED and counter_evidence. The note also records that M-3 sequenced the exon-6-skipped product, so NMD is not absolute.
C2. SPLICE counter_evidence N-10: the 5 bp rule is expert consensus, not an experiment. The map itself says the guideline notes faint wild-type bands can still make a case suitable, and that membership of the "destroyed" class is unmeasured for this allele. Add that qualifier to "out of scope regardless of a transcript test".
C3. MISSENSE O2: "dead in every functional assay" is a universal. The paper reports complete loss of tumour-suppressive activity and loss of POLE4 interaction, not every assay. Rewrite as "loss of tumour-suppressive activity and POLE4 binding". "Mrna normal" is "not decreased" in stably overexpressing CAL-62 constructs (non-neural, thyroid carcinoma line); say so.
C4. MISSENSE O2 "at 35": age is in Results (a 35-year-old at admission) and not in the cited Discussion locator. Add a locator. Also MG-132 did not accumulate even wild type, so the proteasome negative is weakly informative; add it as a limit.
C5. INHIB O2 and NEUROINF O1 limits cite CLAIM 036 (decompensation) for PMID 30290271. CLAIM 036 was measured in an EIIA-Cre null at P18 (Ludes-Meyers 2009), and the claim itself notes the 30290271 knockout uses a different Cre (BK5-Cre, mice 2 weeks old). Reword: "a systemic null is expected to be metabolically compromised (CLAIM 036, other knockout, P18); not measured in this paper". Same in INHIB counter_evidence item 3.
C6. SEIZ O1 "no count, score or instrument": manifest entry 0 was repaired (OVERSHOOT) to assert this of the delivered surface only; narratives (chunks 3-17) are not covered. Restate with that scope. Add manifest entries 4 and 9 to the locators of the limits and track basis.
C7. SEIZ O1 limit "two of the three responders are previously published": patient 4 is explicit (exon 6 deletion, "published in figure S2; Dharmadhikari"). For patient 2 it rests on a Table 1 row of "variants reported in other studies", which also lists Shaukat (patient 3) and BenSalem (patient 5), more than the two previously published patients the paper declares. Soften to "at least one, probably two".
C8. SEIZ O2 and counter_evidence: omit the other vigabatrin reports in CLAIM 001 (You 2024 visible-seizure reduction in one child; Riva 2022 ineffective in one null/null child; Chong 2023 one vigabatrin-resistant). Add them; the efficacy picture is mixed, not "resolved in one of two".
C9. SEIZ O3: Riva 2022 (CLAIM 001) records CBD, ACTH and ketogenic diet without effect in one severe case; add to counter_evidence.
C10. T-TYPE label "dependence" overshoots: one drug, no T-type measurement in Wwox tissue; ethosuximide's T-type action is the paper's Methods wording only. Relabel "ethosuximide sensitivity of provoked seizure". Track A "allele-blind" is asserted, not tested (null allele only). Track justified only as a classification of the lever.
C11. NEUROINF INFERRED "rather than an independent driver": neuron-restricted rescue also normalises seizures and health, so the lowering is indirect; soften to "at least partly secondary". NLRP3 target has no observation in the need (R-06 class only); mark as class-level.
C12. INHIB O1 add age "P13-17", the S-CTL pooling, and the authors' own caution that this age may mimic late-stage disease. INHIB O4 and the need's O3 attribution are fine.
C13. ENDOG O1: model_type "drosophila_rnai_amyloid_model" is wrong for CRISPRa (not RNAi); age "days 14-28": climbing data cited are days 14 and 21.
C14. Targets: PVALB collision_note is reversed. HGNC (live) gives MB alias_symbol PVALB; PVALB alias is D22S749 only. Field also_alias_or_previous_symbol_of: MB is right, the note text is not. XBP1 prev_symbol is XBP2 (HGNC); the XBP1P1 entry is the pseudogene direction and should be explained. Other hgnc_ids checked against memory only, not live.
C15. Locator completeness: add MISSENSE/ENDOG manifest 29808465 entries 3 and 4; INHIB O2 NPY and n; NEUROINF O1 n=4.

## Track and goal

Splice B/deep_recovery, missense B/deep_recovery, inhibitory A/partial_benefit, seizure A/partial_benefit, neuroinflammation A/partial_benefit: justified by their bases. Endogenous-boost Track B is arguable (the lever is allele-blind, applicability is allele-dependent); the basis is explicit, acceptable. T-type: see C10.

## Scope labels

All scope labels follow the bridge definition. Non-neural systems carry the non-neural limit in the Q230P and blood observations. P252A/P282A constructs in a thyroid-cancer line as OTHER_CONTEXT is correct; the proband part is a human case inside a cell_line model_type.
