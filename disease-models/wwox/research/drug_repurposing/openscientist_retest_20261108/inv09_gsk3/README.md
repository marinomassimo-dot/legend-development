# INV-09 GSK3: full-input repeat of the OpenScientist assessment (os-09, 2026-11-08)

Not medical advice. No dose, schedule or route appears. Source cap for Phase 2: at most 5 newly read sources; 5 read, all `abstract_only` (no overrun). Staged receipts (suffix 37, not recorded) are in `receipts/`, validated with `staged_receipt_check.py`.

## Answer first

1. DATO: the report contains one WWOX datum on GSK3, the lithium PTZ score in Wwox-null mice (PMID 32000863, read completely earlier in LEGEND), which also falls in wild type and heterozygote and rests beside a single-lane Ser9 blot. Everything else is transfer from kinase pharmacology, DISC1 progenitors, LTD, cuprizone and EAE. The report states "cannot be attributed to GSK-3 beta alone" (Summary, F001) and "firmly attributable" (Conclusion); neither version is supported (`decisive.tsv` D01).
2. DATO (abstracts read this session): the report's two main myelin citations do not say what it needs. PMID 38123002 is a solifenacin (M3 antagonist) paper in cuprizone mice with Wnt inhibition as a downstream observation; PMID 42274605 is a 2026 review that states both directions: its Wnt sentences support the report's Wnt-negative premise (sec. 3), but every sentence about GSK-3 beta inhibition (abstract, sec. 3 lithium, sec. 4 neural progenitors) goes the other way, and none says GSK-3 beta inhibition impairs oligodendrocyte differentiation (D05; abstract by me, full text by the verifier). The previous package already held the divided GSK3 sign in oligodendroglia.
3. DATO: the "inositol-depletion mimic with no GSK-3 action" arm is not secured. PMID 25345501 (abstract) shows inhibition of inositol synthesis inactivating GSK-3 alpha in SK-N-SH cells; PMID 27922641 mentions GSK-3 once, in its Introduction, so it does not support the report's convergence sentence as cited; the convergence is one paper, one isoform (GSK-3 beta was not significantly altered) (D02).
4. INFERENZA: an S9A knock-in is not a drug-resistance control (already shown in `gsk3_inv09_20261107`: E01, E02, E05); the report's "proves on-target" does not follow (D03). "Demonstrates" and "proven" for dissociability overreach (D09).
5. NON RISOLTO: the perinatal-window and "maturation deficit already in WWOX" statements have no source in the report; the module holds neuronal-migration, cortex-development and neural-progenitor papers on WWOX (titles only here) and a P13-P17 snapshot of oligodendrocyte maturation (D07, D08).

## (a) Coverage

* Items: 85 (E84 and E85, two hedge rows, added after the audit). By kind: observation 15, experiment 15, inference 14, compound 7, limit 7, hypothesis_favourable 5, mechanism_step 5, target 5, link_proposed 4, other 3, recommendation 2, alternative_explanation 1, counter_evidence 1, open_question 1.
* By `legend_class` (per item, from `reconcile.tsv`): already_present_and_used 42, unverified 16, verified_or_corrected 8, superseded_or_contradicted 9, present_not_used 8, new_to_legend 2.
* By `prior_brief_fate` (per item): kept 28, modified 26, omitted 21, narrowed 10.
* Sources: 19 rows in `sources_cited.tsv`; identity check run on 15 cited PMIDs (`queries.tsv` Q01).

## (b) What the previous brief kept, narrowed, modified, omitted

Kept: the PTZ/Ser9 limits (premise C), lithium as reference, the PI4KIIalpha-NMDAR branch (item 4), partial inhibition as a prediction, GSK3 alpha role in LTD. Modified: S9A (premise A: not conclusive), CT99021 (premise B: not isoform-selective), Cre driver (premise D: Syn1-Cre, not Nex/Nestin), "post-development phase without risk", no presupposed useful/harmful branch split, smaller experiment than six arms. Narrowed: WWOX restoration (biological control only), hypomyelination as non-automatically intrinsic. Omitted from the brief: inositol-depletion arm, EAE counter-evidence, the DISC1 progenitor argument, L803-mts and 23369789, the ranked hierarchy, the 95 percent ASM statement, the 19442155 review.

## (c) Sustainable favourable reasons

* DATO: lithium lowers a PTZ score in the Wwox-null mouse and the d-APV-sensitive burst exists in the neuronal-deletion slice (both held). IPOTESI: a GSK3-route reduction of NMDAR current (PI4KIIalpha branch, rat CA1) is a testable second route to the same burst endpoint; the previous package's X2 and X3 already carry it.
* IPOTESI: a dose window may exist (report admits it is unmeasured); the report's proposal to include per-isoform engagement against beta-catenin is compatible with X1/X2.
* DATO: restoring WWOX corrects excitability and myelination in the Wwox-null mouse (PMID 34747138, held), useful as a biological control.

## (d) Errors and counter-evidence found

* Internal: attribution said both ways (E06, E63); isoform-selectivity "cannot help" versus isoform separation offered (E16, E55); inositol mimic "no GSK-3 action" versus its own sentence on inactivation (E05, E38); "partial agonists" for inhibitors (E57).
* Source fit: PMID 38123002 is a drug paper (E12); PMID 42274605 reverses direction (E13); PMID 39901291 is a dental pulp stem cell study (identity only); PMID 27922641 does not state GSK3 inactivation; PMID 25345501 concerns alpha. Nex-Cre is not the neuronal driver of the cited model (Syn1-Cre). EAE: lithium reduces demyelination and an active GSK3 allele worsens EAE (abstract), so the non-transfer caveat is an inference.
* Not examined by anyone: the quotes attributed to PMID 23369789 and 19303846 (identity only), the 95 percent figure, the L803-mts attribution.

## (e) Hypotheses still explorable and what would weaken them

* IPOTESI: the GSK3-PI4KIIalpha branch contributes to WWOX bursts; weakened if matched-current d-APV does as well (no extra), if knock-down does not occlude, or if wild-type slices respond equally.
* IPOTESI: beta-catenin rise under GSK3 inhibition impairs oligodendrocyte maturation in the WWOX context; weakened by divided GSK3 sign in oligodendroglia (R05, R06), by EV03, and by non-cell-autonomy of the S-KO phenotype.
* IPOTESI: partial inhibition separates benefit from harm; weakened if per-isoform engagement curves of the two read-outs coincide.
* Not carried: time-gating as a safe window (no timing source, D07).

## (f) Priority question and experiment

Unchanged from the previous package: X1 (is substrate phosphorylation or per-isoform GSK3 activity different in WWOX-deficient neurons at matched stage) then X2 with the arms the previous audit repaired (dual depletion or dual inhibitor at verified engagement). New from this repeat: if an inositol arm is wanted, it needs its own measure of GSK-3 phosphorylation (EV01), and an S9A arm is a separate genetic question, not an attribution control.

## (g) Consequence for drug repurposing, novelty class per proposal

* Lithium as reference only; no GSK3 compound nominated: already_in_legend.
* Inositol-depletion arm with GSK-3 readout: new_to_legend; literature novelty not assessed.
* Time-gated dosing after a developmental window: new_to_legend as an arm; support absent; literature novelty not assessed.
* DISC1/progenitor maturation read-out in the arms: new_to_legend (source not read).
* S9A cross as attribution proof: already_in_legend as a correction (not usable).
* WWOX restoration comparator: already_in_legend as biological control.
* Ranked hierarchy and medicinal-chemistry recommendation: new_to_legend, not endorsed.

## (h) Consumers to update

None edited. Proposals: `needs/needs.json` entry `NEED-GSK3B-DEREPRESSION` counter_evidence could add that the report-style inositol-mimic arm is not GSK-3-free (PMID 25345501, alpha, abstract); `gsk3_inv09_20261107/output/separation.tsv` row 1 could add EV01/EV02 as the inositol distinction; the INV-06 myelin package could add EV03/EV04 (direction in a review; drug paper). Reason for no more: no new WWOX datum was read.

## (i) What was not reachable or not done

Full texts of all five new sources (abstracts only, by decision; cap 5). Not read: 19442155, 23369789, 19303846, 39901291, 33197065 (only prior abstract), the three WWOX papers found by search (32581702, 31543760, 42397075, 31340538) beyond titles and existing receipts. No search for Nex-Cre; absence of timing windows is bounded in D07 and Q05-Q08. PMID 42274605 was also claimed by `os-06`; only its abstract was used. No access challenge was met.

## (j) Queries run

`queries.tsv` Q01 to Q08 (identity check of 15 PMIDs; receipt status; claims; abstracts; two PubMed strings; git grep for the nine new identifiers; manifest keyword read).

## Audit appendix (blind verifier vf-09, 2026-11-08; `verify/audit.md`)

Verdicts on the 14 decisive propositions: 11 SUPPORTED (5 with additions: D02, D04, D06, D10 and D03 with one sub-claim, the 15791206 muscle inhibitor experiment, unreachable by the verifier), 1 PARTLY (D08: the neuronal half is resolved by the cited 32000863), and D07 SUPPORTED as an absence statement while the report's window claim is not supported and the cited constitutive null leans against it (mice survive under a month; seizure tests preweaning; DCX/NeuN at P14-P20). Coverage check of the first extraction: 12 points sampled, 10 present, 2 narrowed (the L22 heading hedge "partly intrinsic"; "crossed where relevant onto S9A"), 0 missing; both are now rows E84 and E85. Errors repaired: E35 note (L141 does name the substrate-competitive partial arm), E10 (one peptide, L803-mts, 100 uM, human dental pulp stem cells; the quoted words are a Methods sentence), E50 fate wording.

Narrowings applied: D04 separation holds for the alpha-selective compound, for genetic single-isoform loss, and for both selective compounds only in HEK293T at one concentration (BRD3731 raised beta-catenin from 20 uM in HL-60 and TF-1; cell selectivity 4-6-fold); D02 convergence is one paper, one isoform, with GSK-3 beta unchanged and the synthesis block, not depletion, credited by the authors; D06 the knock-in is a double S21A/S9A line, n = 6 per group, histology for lithium only, "immune-mediated" is the report's inference; D08 neuronal differentiation markers are a WWOX datum in the constitutive null (32000863) not cited by the report for that line; D09 anchors now include L55 and L144; D10 the L803-mts tension with arm 3; D03 lithium acts by direct competition as well as by raising inhibitory phosphorylation. Thirteen new evidence rows (EV06 to EV18) carry the verifier's readings, labelled verifier-read; the producer's own five readings stay abstract only (receipts unchanged).

Not reached: the 15791206 muscle inhibitor experiment; the primary text of 33914858 (counts via the module manifest, validation image unseen); the primary studies behind the review sentences (references stripped); 19303846, 17850214 and the kinome-panel claims; blots of 25345501 and other panels of 32000863. A reading of the 42274605 reference list would settle whether its lithium and Wnt sentences rest on primary data: open need, not read (cap reached).
