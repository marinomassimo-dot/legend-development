# IT9 P6 / P5 Stage B: independent verification (branch task/it9-p6, head a420d721)

Verifier read-only except this report. Non-canonical. No receipt staged: sources were re-read as passages from the local full-text copies (files/fulltext, PMC), not as a complete read.

## Premise ratings (case_it9_p6_hif_axis_20261030/premises.tsv)

| # | Rating | Basis |
|---|---|---|
| P1 | confirmed, narrowed | PMC4211377 (Abu-Remaileh 2014): HIF1alpha readily detected in nuclei of KO MEFs in normoxia, barely in WT; KO MEFs lose hydroxylation (Fig 5f); HIF1A knockdown "completely rescued" glucose uptake in KO MEFs; the difference disappears under hypoxia (Fig 4c). Narrowing: the "mRNA unchanged" statement in the paper is for skeletal muscle (Supp Fig S4C), not MEFs; the case text (README sec 1, S028, packet DA-K01-001) attaches it to MEFs. The HIF1alpha MEF blot is qualitative nuclear-fraction detection. |
| P2 | confirmed, narrowed | PMC8955937 (Baryla 2022) sec 2.6.1: cytoplasmic HIF1alpha 2-fold lower in KO vs control in normoxia/normoglycaemia (p<0.01) and nearly 2-fold in hypoxia/normoglycaemia (p<0.001); "we didn't observe WWOX influence on HIF1alpha protein in nuclear fraction"; "one repetition is shown". Narrowings below (F2, F3, F4). |
| P3 | confirmed | Recomputed from files/geo/GSE156243 Salmon count table (CPM from column totals; KO cko1-4 v WT cwt1-2): EPAS1 3.80, HK2 4.73, SLC2A1 2.67, ARNT 1.46, HIF1A 0.84, PDK1 0.78; identical to organoid_target_gene_rows.tsv. Caveat (LOW): ratio of mean CPM; ratios of mean raw counts are larger (EPAS1 4.36, HK2 5.31, HIF1A 0.95) because WT libraries are smaller (30.0 and 37.3 M v 34.2-41.2 M). Per-library: HIF1A KO 33.5-43.6 v WT 43.0-49.5 (overlap, "flat" fair); EPAS1 KO 2.84-9.06 v WT 1.18-1.73 (3-fold spread within KO). No test statistic; n=4 v 2, one laboratory (already stated). |
| P4 | confirmed as a negative search, not re-run | Absence statement present in E-01 record and needs; consistent with both papers read (neither measures neural HIF protein). Not independently searched. |
| P5 | confirmed (table), primary not re-derived | edge_provenance_E.tsv rows 1-2: SIGNOR complex edge sourced to review PMID 27692180; primary CollecTRI record Bruick 2000 (PMID 10922063). The PMC copy returned here is abstract-only; the cell-line list (non-neural) was not re-derived. Row 4 (Abu-Remaileh) is correctly named as the real seed-to-lever link and graded non-neural. |
| P6 | confirmed | chembl_mechanism.tsv has no PX-478 row; identity.tsv CHEMBL4117516 max_phase 1; trials_summary.tsv: 1 registry study (NCT00522652), 0 in epilepsy/neurodevelopment/WWOX/paediatric; E-01 record sec 6 (adult, min age 18). Mustard alert is structural (SMILES N-oxide bis(2-chloroethyl) amine): confirmed by structure. |
| P7 | narrowed | Seizures (EU label 1.1% v 0.2% non-dialysis; 2.0% v 1.6% dialysis) and brain necrosis in rats are label statements. "Thyromimetic action" is NOT a label statement: the label lists secondary hypothyroidism; thyromimetic action is from Morita 2025 (passages) per E-02 record line 19. See F5. PH inhibitor raising HIF: confirmed (EGLN1 IC50 14-5740 nM). |
| P8 | confirmed, with a scope finding | guards.tsv IT7_READOUT6 as stated. See F1 (the "beyond the six" genes). |
| P9 | confirmed | repurposing_view.py positions: K01 x NEED-PDH-PYRUVATE-AXIS = F3, one signed row read beyond abstract. |
| P10 | confirmed, with gaps | See section on the experiment. |

## Findings

### MEDIUM

F1. The "glycolytic genes BEYOND the six readout genes (PGK1, ALDOA, ENO1, PFKP, PKM)" (README sec 7 arm A) are the other five members of SET:GLYCOLYSIS_LACTATE_10 (build_seeds.py line 482: SLC2A1,HK2,PFKP,ALDOA,PGK1,ENO1,LDHA,PKM,BNIP3,LDHB), and that set is itself a guard scope member of IT7_READOUT6 (guards.tsv) and the seed S025 that generated the proposal. They are not the six, so reading them is permitted, but they are not independent of the seed. The decision table row "lowers lactate AND THE MODULE" never defines "the module"; if it means GLY10 it contains five of the six forbidden genes. Fix: define the deciding readout as lactate/acidification and glucose uptake plus the five named genes reported individually, and state that the seed-set co-membership means a gene change there confirms the seed, it does not independently validate a lever.

F2. Counter-evidence is shown (README sec 0 "Why not more", sec 1 S031, needs counter item 4, packet DA-K01-003, arm C) but is slightly stronger-sounding than the source supports, and one fact that weakens it is missing everywhere: the paper found NO effect on the nuclear HIF1alpha fraction, which is the transcriptionally active pool and the fraction that was measured in the MEFs. The fibroblast result is a cytoplasmic decrease; the MEF result is a nuclear increase. "Opposite sign" compares different compartments. The correct statement is: cytoplasmic lower in two of four conditions, nuclear unchanged, one blot repetition shown. This neither supports nor cleanly contradicts the MEF result. Equal weight is otherwise respected (the case does not discard it and uses it to keep the direction uncertain).

F3. Packet DA-K01-003 and needs counter item 4 state HIF1alpha is "equal or higher in the other two" conditions. The text of Baryla 2022 sec 2.6.1 reports only the two significant decreases and the nuclear null; "higher" in the other two is not stated in the text (the figure was not read here). Either cite the figure panel or write "no significant difference reported".

F4. Packet DA-K01-001 measured_result_note says "digoxin lowers glucose, GLUT1 and PHD3 effects in the knockout mice". The paper (Fig 5c, Supp S5B) reports that digoxin RAISED blood glucose in KO mice (reversing their hypoglycaemia) and lowered GLUT1 and PHD3 expression. As written the glucose direction is wrong or unreadable. README (sec 1 S028) says "changes glucose", which is correct but vague.

### LOW

F5. Roxadustat attribution: README sec 4 ("label: seizures common, thyromimetic action, ..."), premises P7, pertinence row DR-K01-004 (flags "label_statement ... thyromimetic_action") and qualification_E.tsv decision text put "thyromimetic action" under the label. It comes from Morita 2025 (passages); the label statement is secondary hypothyroidism. The DROP decision stands on seizures, brain necrosis in rats and the direction-by-construction reason. Arm C relies on "a PH inhibitor without thyromimetic action (molidustat)" which rests on that one report and is flagged "to be verified" in the E-02 record; the README should say so in sec 7.

F6. P1 mRNA tissue (see table): correct to "mRNA comparable in skeletal muscle of KO and WT mice".

F7. Ranking units.tsv: existing entry U27 (extracellular magnesium) has a changed M_mechanism text ("no catalogue identity ..." became "1 catalogue family(ies); L2 over 1 ... none") against main; groups and class unchanged. It follows the earlier P11 identity declaration, not K01, but README sec 11 says only "no existing group moved" and changes.tsv does not name this field change. Harmless; note it.

F8. Branch base: task/it9-p6 merge-base with main is e31d2908 while main is a1d5a945; integration needs a merge. The diff against main shows removals in two dossiers, ledger and state manifest that come from main's newer commits, not from this branch.

## Experiment (section 7)

Sound in structure. Step 0 is the right gate: the whole axis rests on a non-neural protein observation, mRNA is flat, so protein is the missing premise; the falsifier is correct and also covers a LOWER protein (the fibroblast pattern). Gaps (LOW-MEDIUM):
- Step 0 does not specify compartment (nuclear v cytoplasmic fractions; see F2) or oxygen condition. In the MEFs the difference vanishes under hypoxia, and week 8-15 organoids develop hypoxic cores, so organoid HIF protein can be raised in both genotypes. Specify normoxic 2D/hNPC as primary, or a hypoxia marker (pimonidazole) co-stain for organoids.
- Adaptive v harmful valence: the two decisive rows are well separated, but a mixed or null outcome (lactate and module fall, viability/network/differentiation unchanged or discordant) has no row; add "neither: undefined, the shift is HIF-dependent but its valence is not resolved". "Improve/worsen" should be stated relative to the untreated KO cell and to corrected cells.
- Arm C: the genotype design is implicit. The saturation test needs the PH inhibitor in BOTH WT (does it phenocopy the KO seeds) and KO (any further rise) cells; sec 7 table does not say so (the E-02 record does). The genetic VHL/EGLN1 alternative is a good guard against off-target 2-oxoglutarate oxygenase effects.
- Arm A drives HIF1A+EPAS1 knockdown in cells that may need basal HIF for viability: the WT-parallel control is present, good.
- Six IT7 genes: not used to decide in the table (see F1 for the module wording). Result-to-decision table and falsifier are otherwise coherent, and no outcome is assumed (P10 confirmed).

## Ranking Stage B

- All 32 records of it9_records.tsv checked (not a sample) against their qualification tables (P4b-a q2_metabolism, P4b-b qualification_b, P4b-c Q6_group, P4c-d D, P4c-e E). Decisions match 32 of 32. Mapping applied correctly: KEEP -> class ORD and group G4b (U28-U31); INCONCLUSIVE -> INSUFF and group GU (U32-U35; JTE-151 has two records P3-09 and P4CD-02, one unit U33); DROP (16) and REFERENCE (7) -> EXCL, group n/a (U36-U58).
- Counts reconcile: 61 units = 30 pre-existing + 31 distinct IT9 compounds (32 records; E-01 enters as U28 via K01). Classes recomputed from units.tsv: ORD 14, weak pertinence 5, INSUFF 16, EXCL 26 (3 axes + 16 DROP + 7 reference). Origin: 30 known / 24 IT9 / 7 reference. README sec 11 says "30 entries from qualification records" (31 distinct minus E-01): consistent. Task text said 30 mapped; the artefacts hold 32 records, 31 compounds, 30 proposal entries plus U28.
- No existing group moved: compared U01-U30 old v new units.tsv on class, general/broad/partial group, lead, next-priority and evidence fields: identical except U27 M_mechanism text (F7).
- Language: no efficacy statement or probability in new unit labels, class_reason, caveats or reasons. Matches for "likely/promis" are only "never ranked below an item shown unpromising" (GU rule) and "a mechanism experiment, not a treatment" (U28).

## Card K01 language

packet.json: "proposed, not performed" stated (predictions: None; "nothing here is a treatment proposal"); no dose, route or schedule; roxadustat is a direction control, PX-478 an experiment arm; route BENEFICIO_PRECOCE justified as "partial benefit at best, only if the shift is harmful". No efficacy claim found. The two factual slips are F3/F4.

## UNVERIFIED by me
hNPC GSE126075 values (S023/S025/S022 centred figures); Bruick 2000 cell lines (abstract-only copy); SIGNOR record; Koh 2008 and Welsh 2004; supplement figures of both papers; whether the Baryla line is knockout or knockdown (the paper calls it both); the label text for EU roxadustat (taken from the committed record, not re-fetched).
