# Science batch 2 (2026-11-08): delivery record for IT36

Non-canonical research, not medical advice; WWOX-DEE reference genotype class only. Written for the IT36 integrator. Nothing shared was edited (no need, card, ranking, dashboard, registry, ledger of receipts, protocol). Task record: `ledger/tasks/orchestrator/ORCH-IT37SCI-20261108.json`. Two packages, each audited blind (proposition, source, locator).

## What decision changes

1. **ISRIB cannot be read as a GSK3-site test, and its "one clean pattern" is withdrawn.** The first decisive fork of any GSK3/ISRIB comparison is the phospho-eIF2alpha route; GSK3 arms follow only conditionally.
2. **INV-12's depleted-hormone arm is not runnable as written**: B27 (and, undetermined, N2) is in the medium throughout, so the hormone baseline of the medium must be measured first; a null agonist result in complete medium could be a ceiling effect.
3. **The re-analyses EX1 and EX5 are not worth running on the deposit** (one pooled library per arm); the module's bulk tables already hold the usable description.

## Package A: `isrib_discrim_20261108/` (audit `isrib_discrim_20261108/verify/audit_a.md`)

- Site: the "S539" blot of PMID 23741617 is undetermined, and not a GSK3-site test. Human residue 539 of EIF2B5 is Asp (GSK3 serine 540, priming serine 544); rat 535 and 539; mouse 536 and 540; rabbit 540 and 544. Missing: antibody catalogue number, immunogen and validation. The reply letter says the band shows "no differences in the presence or absence of ISRIB" and the phospho-S539 and total-epsilon rows exist only in the tunicamycin panel although the caption names thapsigargin; no quantification (`phosphosite.tsv`). The image is a visual impression only (viewed by the auditor from the publisher host at 2000 px).
- Four evidence levels assigned to every result (`evidence_levels.tsv`); corrected interpretation grid, 12 patterns (`grid.tsv`); the earlier "phospho-eIF2alpha not raised, GSK3 route likely, ISRIB gives little" pattern does not discriminate (little ISRIB response is expected when phospho-eIF2alpha is absent). Two GSK3 chemotypes do not remove other substrates (mTOR/TSC2 route sourced at commentary-abstract level only). A missing ISRIB response without an engagement control or effective exposure is uninformative.
- Minimal design: step 0 readout and engagement qualification in one plate; step 1 asks only whether phospho-eIF2alpha is raised and ISRIB-reversible in deficient versus corrected cells; GSK3 arms, epistasis with phospho-resistant and catalytic-dead epsilon, function and viability only conditionally (`design.tsv`). A phospho-mimetic is not assumed to reproduce a phosphorylation (the Ser-to-Asp form did not restore the effect in the 2012 TLR paper).
- WWOX: the module already holds GSK3 observations (phospho-Ser9 in null brain, E01/E02; lithium seizure score, E03); the gap is the chain and its experiment, not the whole GSK3 literature (the wording change is in `consumer_delta.md`).
- Card: CARD-A1 ISRIB as a probe (`new_qualification`); CARD-A2 abstains (the module qualifies only lithium).

## Package B: `myelin_premises_20261108/` (audit `myelin_premises_20261108/verify/audit_b.md`)

- Media (`media.tsv`, 17 rows): B27 is in the DRG plating, co-culture (with N2), spheroid neural (2%) and oligo maturation media (1%); only the added T3 supplement stops (Days 60 to 70 in the scheme). The current vendor formulation of B-27, including Minus Vitamin A, lists T3 (concentration confidential); it is the current formulation, not the 2021 lot. Thyroid-hormone exposure after Day 70 is undetermined, not zero, so INV-06 row E12 ("withdrawn from Day 71") is not documented. N2: `composition_not_determinable`.
- Feasibility (`feasibility.tsv`): GSE158684 is public (six small files held; raw reads still `hup`), one pooled library per arm, hippocampus P17, too few oligodendroglial nuclei. Descriptive counts only; neuron-like Hr, Klf9 and Thrb flat. The module's bulk tables (independent animals) already list Hr, Dio3, Dio2 lower in several contrasts, unlinked so far to a thyroid reading, and these readouts cannot separate a thyroid-type response from oligodendrocyte depletion, activity or delayed maturation. Energy genes move with mixed signs; a transcript is not flux.
- Cards (`cards.tsv`): tiratricol/liothyronine (H1), lactate as a process probe (H2), PDK inhibition (INV-07): all `already_in_legend`, none favourable, no new intervention for the module. INV-12 stays conditional, rank unchanged.

## Consumers (proposals; nothing applied)

`isrib_discrim_20261108/output/consumer_delta.md` and `myelin_premises_20261108/output/consumer_delta.md` (each: consumer, change, reason). Receipts: 8 staged (suffix 81, `receipt_staging/it37a/`) and 5 staged (suffix 82, `receipt_staging/it37b/`), all validated with `staged_receipt_check.py --check-doi`; two carry a prior receipt (23741617, 33914858). The earlier batch's receipts (suffixes 96 to 99) are separate and I did not check whether IT36 has recorded them.

## Open items for IT36 (not acted on here)

- Claims left by producers without an opening: PMID 19641107 (abstract viewed, not used) and 37856222 (never opened); package A opened 7 sources against a cap of 6 (18160716, context only); package B read 7 against 6 counting vendor pages. Query times in package B are reconstructed to the minute.
- Unverified by anyone: the Brewer 1993 B27 composition, any lot-specific formulation, DMEM and Neurobasal glucose values, the antibody catalogue number; the mouse-numbering issue (26974342 writes Ser535 for mouse where the mouse GSK3 serine is 536) touches evidence E15 to E17 and the G02 control and was not tested.
- The old worktrees `it36sci` and `isrib-identity` remain (removal was refused by the permission classifier).
