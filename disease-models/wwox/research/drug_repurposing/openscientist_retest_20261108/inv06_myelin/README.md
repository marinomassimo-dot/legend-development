# INV-06 myelination: full-input repeat of the OpenScientist report (actor os-06, receipt suffix 34), 2026-11-08

Non-canonical research, not medical advice; WWOX-DEE reference genotype class only; no dose or regimen. Producer model Sonnet 5.5, effort value 5 (scale not stated). The report is external AI-generated material to assess, not validated biology. Tables here: `extraction.tsv`, `sources_cited.tsv`, `chains.tsv`, `reconcile.tsv`, `decisive.tsv`, `evidence.tsv`, `queries.tsv`, `receipts/INDEX.tsv`, `phase1_note.md`. Source cap: at most 5 newly read; 5 read (see (i)).

## Answer first
1. DATO. The report's only two WWOX myelin-relevant data are real and identity-matched: neuronal deletion gives fewer mature oligodendrocytes, fewer myelinated axons and slower conduction (33914858), and the germline knockout shows raised GSK-3beta activation with lithium abolishing the onset of PTZ-induced seizure (32000863; the paper shows a Ser9 correlate in a germline knockout, not a restraint mechanism). Everything that links GSK-3beta, clemastine, T3 or neuregulin to WWOX myelin is a transfer from another system. INFERENZA: no WWOX datum shows a drug acting on myelin.
2. INFERENZA. The "decisive, non-cell-autonomous" reading (L9, L19) is stronger than the report's own Finding 7 and Limitations (L63-64, L142), and it overlooks that the source paper already holds an oligodendrocyte-lineage deletion (Olig2-Cre), a GFAP-Cre deletion and a DRG-OPC co-culture. "OPCs genetically wild-type" is assumed, not shown: intact WWOX is shown only in CC1 cells, and "mosaic" Cre is an inference (no efficiency in the main text; an independent reporter study held in `nb4_delta_20261107` supports incomplete recombination for the same line). The co-culture is a real test of non-cell-autonomy but separates neither contact, substrate nor a soluble product.
3. DATO. The GSK-3beta lead is mixed, not simply weak (read this phase): the naringin paper's abstract and Results state opposite directions for phospho-GSK-3beta and beta-catenin and it has no GSK-3beta manipulation; the review the report quotes says continuous Wnt/beta-catenin signalling reduces differentiation but also (section 3) that lithium inhibition of GSK-3beta promotes oligodendrocyte differentiation in experimental models, and that lithium trials in patients show immunomodulation, not remyelination; the Foxg1 paper (read earlier) has the inhibitor lowering the mature-cell share. LEGEND already holds GSK3 as undetermined and abstained (gsk3_inv09).
4. INFERENZA. Most of the report is already in LEGEND (28 of 66 items `already_present_and_used`); the new contributions are the PPARalpha/lipid wording, the naringin and glycyrrhizic acid compounds (abstract-level) and a drug x deletion-site factorial, whose Arm B partly exists.

## (a) Coverage
- Items per kind (extraction.tsv, 67 after the audit added the header identifier E67): observation 23, inference 12, compound 6, experiment 6, limit 5, hypothesis_favourable 4, recommendation 4, mechanism_step 3, counter_evidence 1, open_question 1, other 2. Sources cited 19 rows; chains 9.
- Per `legend_class` (67 items, one row each in reconcile.tsv): already_present_and_used 28, verified_or_corrected 19, unverified 8, superseded_or_contradicted 5, new_to_legend 4, present_not_used 3.
- Per `prior_brief_fate`: kept 18, modified 20, narrowed 3, omitted 26.

## (b) What the previous brief (`myelin_inv06_20261107/BRIEF.md`) kept, narrowed, modified, omitted
- Modified: the WWOX base (it states the report "neglects Olig2-Cre and GFAP-Cre and the co-culture"); GSK3 ("conditional direction or precise uncertainty, not a mandatory preference"); activity ("do not settle by labelling one study adult and the other neonatal"); T3/clemastine/Pdk1 as comparators. Narrowed: "no new animal colonies before clarifying what these experiments already answer". Kept: levels (maturation, sheath, conduction, network), the premise that WWOX restoration is not the only solution. Omitted (26 items): the compounds named in passing, KB annotations, the supporting remyelination papers, the diagram, SDR/lipid route, cross-disorder mining, uncited safety statement, gene-therapy-as-control argument. The brief also said the report was "not needed"; that choice is why items such as E08-E10, E16-E17, E27, E29-E31 and E57-E58 had no earlier reading.

## (c) Sustainable favourable reasons
- DATO: a neuron-side contribution to the maturation deficit (co-culture and neuronal deletion) is supported; the Olig2-Cre arm showed no major P17 MBP change (qualitative).
- IPOTESI: T3 (liothyronine) and GSK-3beta inhibitors remain legitimate cell-level probes of receptor- or pathway-responsive maturation; early excess activity remains a candidate (LEGEND H2). All need genotype x drug arms with a wild-type comparator.

## (d) Errors and counter-evidence found
- E47/E37: "oligodendrocyte-intrinsic loss untested, Arm B not performed" is wrong in part (O-KO and G-KO exist).
- E56: the Foxg1/SB216763 paper is used as support but shows the opposite direction.
- E10: naringin abstract versus Results contradict each other; association only (EV01-EV04).
- E08: the review quoted for GSK-3beta says beta-catenin signalling restrains differentiation (EV05, EV07).
- E44: adult/early-development label used to reconcile two activity papers; LEGEND found they differ in level and mode.
- E51: "every downstream level reachable" contradicted by clemastine's conduction slowing in wild-type neonates.
- E29: PDGFRa called a "proliferation marker"; E31: T3 replaced an insult-lowered hormone, WWOX shows no deficit.
- E07: "induced seizures" is PTZ-induced onset in a germline knockout; the neuron-specific model is not that paper. E23: the "WWOX-null cortex" paper (34634460) is a neuronal deletion by its abstract.
- E36/E35: the neuron-restricted vector control is not non-probative (INFERENZA); 34747138 quantifies its treated arms (Fig 4C, Fig 5, n = 3 per arm); the "unquantified" phrase in LEGEND's ranking text belongs to a different paper (42422765).
- E23/E43: 34634460 and 33914858 use the same Synapsin-Cre line, one origin; "same animals" (L59) is unsupported.
- Internal: SDR/lipid branch is neuronal in the diagram and OL-intrinsic in Finding 7; SDR-domain and lithium-safety statements are uncited; one identity note: 28469664 AUTHOR_MISMATCH is a bibliographic first-author difference (title and DOI match).

## (e) Hypotheses still explorable; what would weaken them
- Neuron-side signal/substrate: weakened if the deficit tracks activity arms or disappears with fixed null neurons removed (prior X1/X2).
- GSK-3beta route: weakened by no GSK-3beta activation in null-neuron OPCs, by a genetic OL-lineage test without differentiation change, or by inhibitor lowering differentiation as in the Foxg1 arm.
- T3 route: weakened by equal effect in both genotypes or no effect once medium T3 is measured (premises step 0).

## (f) Priority question and experiment
Which of contact/substrate, soluble product or activity carries the null-neuron deficit, before any drug (existing X1 then X2 arms in the existing co-culture). A genotype x drug design needs a wild-type drug arm (E39) and conduction/EM readouts.

## (g) Consequence for drug repurposing (novelty class)
- Selective GSK-3beta inhibitor / lithium for myelin: already_in_legend (abstention stands); literature-novel not assessed.
- Clemastine as universal comparator: already_in_legend, narrowed (conduction discordance).
- T3 / liothyronine: already_in_legend (INV-12, CARD-H1-01); PPARalpha wording new_to_legend.
- Naringin, glycyrrhizic acid: new_to_legend, abstract/association level, no priority change.
- Cross-disorder GSK3/hypomyelination mining: new_to_legend, not assessed.
No ranking change is proposed.

## (h) Consumers to update
None edited here. Proposed: the INV-06 evidence table could add EV01-EV07 as GSK3 counter/context rows and the neuron-specific wording for 34634460 (EV13); the cards need nothing.

## (i) Not reached / read
Newly read (5, cap respected): 28469664 and 42274605 (partial full text, figures not viewed, references not read); 31808502, 40246008, 26725831 (abstract_only). Abstracts of 34634460 and 32000863 were re-viewed for one decisive detail each; both already hold deeper receipts and are not counted as new reads, no new receipt written. Not opened: 21319221 full text (subscription, earlier stop), 16112266, 38289861, 38423189, 39733800, 33015737, 24391468, 42334020, 41980417, 33914858 (reused), the DisMech entry (so the annotation text, the 55+ figure and GO ids in E03/E34/E55 are unverified). No figure viewed. No access challenge met.

## (j) Queries run
See `queries.tsv` (8 rows; times reconstructed to the minute).

## Audit appendix (blind verifier vf-06, 2026-11-08)
Verdicts on the 14 decisive propositions: 12 SUPPORTED (P01, P02, P03, P05, P06, P07, P08, P09, P10, P11, P13, P14), 2 PARTLY (P04: the 21319221 abstract does not say wild-type and its optic-nerve arm is ex vivo, and the review also contains a favourable lithium sentence; P12: 34747138 does quantify its treated arms), none NOT SUPPORTED, none UNVERIFIABLE. Coverage check of the first extraction: 12 points sampled, 10 PRESENT, 1 PRESENT_NARROWED (the L142 sentence "Arm B ... has not been performed", now in E47), 1 MISSING (the header identifier MONDO:0014533, now E67); E38 now flags that MBP labelling is not an EM measure. Reconciliation sample: 8 rows, pointers exist; E35 repeated the mix-up between 34747138 and 42422765 and is corrected; E55 had a weak pointer (the DisMech README has no "55+") and now says so; E36 lost its unsourced "mosaic and partial" for the vector. Evidence sample: 15 quotes verbatim; EV16 to EV22 added (EV16 is the favourable lithium sentence from the review; EV17 to EV22 use only quotes given in `verify/audit.md`, read by the verifier, not reopened by the producer).
Narrowings applied: "mosaic" Cre is an inference for 33914858; O-KO and G-KO show no growth, weight or survival phenotype and Nestin-Cre reproduces the S-KO hypomyelination; MK-801 reduced myelination by 82% (not removed) and the authors say the mode "may dominate later in development"; S-KO seizure onset at P9; 34634460 and 33914858 are one mouse line; the 32000863 GSK-3beta datum is a correlate in a germline model; the Foxg1/SB216763 reversal and the O-KO/G-KO arms were confirmed.
Not reached (by the verifier or the producer): full text of 21319221 (no open route); figure images for every source; whether Synapsin-Cre is mosaic in OPCs (answerable from the authors' reporter material); 41980417 read by keyword search only; `myelin_premises` media rows and B27 T3 content not rechecked; 42422765 not read; verbatim Fig 4C and Fig 5 legend quotes for 34747138 are an open need (a new read, not made because the producer cap of 5 is used).
