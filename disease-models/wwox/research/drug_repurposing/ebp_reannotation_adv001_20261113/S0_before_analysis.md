# ADV-001 (IT51-Q05) — S0: the substrate, the categories and the stop rule, fixed before any join (2026-11-13)

Non-canonical research material. Not medical advice; no dose or recommendation; no compound nominated. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI. Task record `ledger/tasks/orchestrator/ORCH-ADV001-20261113.json`. Assigned by the pilot's Strategic Advisor via the Harness session (ADV-001, `advisor_pilot_20261113/assignments/ADV-001.md`); taken in charge as a request, authority relayed by a peer, not verified. Paths relative to `disease-models/wwox/research/drug_repurposing/`.

## 1 · The question (as assigned)
Of the IT29 case-1 signed rows reachable from committed files, how many "favourable" rows are attributable to documented EBP (sterol isomerase) inhibition rather than to their stated target, and does any consumer sentence about pro-myelinating agents have to change as a result? Decision it can change: whether the marker-level signed layer can serve as evidence for a target-specific pro-myelinating hypothesis or must carry an EBP-confound limit; whether the next myelination comparison needs a sterol-profile control arm per compound before any target attribution is read.

## 2 · The substrate, stated in writing before the work
* **Committed artefacts:** `phenotype_first_it29_20261105/signed_rows_case1_it29.tsv` (**31 hand-curated rows**, target-level: 11 are compound rows, 20 genetic) and `comparison_case1_it29.tsv` (**20 compounds**: 15 favourable, 5 adverse, with their evidence rows R01–R52 in `p3_A..E`), `withdrawn_rows_it30.tsv` (2 withdrawn rows). The IT29 README quotes a **216-row layer over 191 families** signed by the generator; **it is not a committed artefact** (the pilot's search found none; `generation_it29_p5_20261105/results_s10/` holds proposals, not the signed layer). **No number is reproduced on the 216 rows here; the "106 of 137 consistent rows are glucocorticoid-receptor agonists from one study" is IT29's statement, not re-derived.**
* **Denominators used:** (a) the 20 compounds of the comparison (15 favourable, 5 adverse); (b) the 11 compound rows of the 31-row layer; (c) the 20 genetic rows are out of scope (a genetic row has no compound to carry an EBP action).
* **Already represented in IT29 (read, not re-derived):** the muscarinic class was deliberately left `unresolved` (CHRM1/CHRM3 context_dependent; "muscarinic antagonists that lack EBP inhibition did not induce differentiation"); EBP (S1-06, S1-07), CYP51A1 (S1-05) and TM7SF2 (S1-08) are signed as sterol-pathway targets.

## 3 · Categories (kept apart; unmeasured is not inactive)
**EBP_DOCUMENTED** (activity shown in a primary or a database binding/functional row, with source and system); **STEROL_PATHWAY_NON_EBP** (a documented effect on another sterol enzyme, for example CYP51, not EBP); **EBP_ABSENCE_DOCUMENTED** (a measured negative in an EBP assay); **EBP_UNMEASURED** (no row in the sources reached: the stated perimeter is named); **NOT_APPLICABLE** (the stated target is not an enzyme-inhibitor route, e.g. receptor agonist, with no sterol claim). A compound can carry two labels (EBP_DOCUMENTED plus a stated-target action).

## 4 · Evidence route (zero spend; no contact)
ChEMBL REST (plain curl; answered HTTP 200 on 2026-11-13): activity rows on the four EBP-orthologue targets (CHEMBL4931, CHEMBL5525, CHEMBL3774293, CHEMBL2311238), cached as a TSV in this package; compound names resolved to ChEMBL parent molecules by name with the resolution table kept (ambiguity flagged); screening-deposit and panel rows flagged. Literature already read and verified: Hubler 2018 (clemastine, benztropine, tamoxifen, U50488 inhibit EBP in OPCs; four antimuscarinics inert, names not reached), Allimuthu 2019, Sax 2022 (quetiapine, GSK239512, donepezil, vanoxerine, fenspiride, bazedoxifene, clomifene inhibit EBP in mouse OPCs; abstract/targeted depth), SCI51's `output/activities.tsv`. A database row is a pointer; where a decisive statement rests on it, the primary is named.

## 5 · Priors (fixed now; scored afterwards; may fail)
* **E1.** Between 5 and 8 of the 15 favourable compounds have EBP_DOCUMENTED status (benztropine, clemastine, tamoxifen, ifenprodil, quetiapine, amorolfine as the likely ones), so a clear minority to a bare majority.
* **E2.** Atropine, ipratropium and oxybutynin (the favourable antimuscarinics from R08) are EBP_UNMEASURED, not EBP_ABSENCE_DOCUMENTED.
* **E3.** The adverse compounds (HDAC inhibitors, mevastatin, neostigmine) carry no EBP claim.
* **E4.** Most consumer sentences about pro-myelinating agents already carry the muscarinic-versus-EBP qualification; the result changes at most one sentence in one consumer.
* **E5.** The EBP share cannot be turned into a statement about the 216-row layer.

## 6 · Perimeter, depth and stop
The join and the counts are mechanical (script, tables kept); one blind verifier (sonnet, high) on the decisive per-compound statements and on the denominator; no recursion; no edit to IT29 files or any shared consumer, ranking, need, registry or the receipt ledger; consumer sentences are located by `git grep` (not the two large registries) and proposed, not edited. Stop when the 20 compounds and 11 compound rows carry a category with a source, or the reason a category cannot be assigned is stated.
