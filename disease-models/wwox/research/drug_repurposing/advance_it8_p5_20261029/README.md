# IT8 P5: scientific advance with two completed loops

Scientist-b, task `ORCH-ROADMAP-IT8-20261029`, branch `task/it8-p5`, 2026-10-29. Non-canonical research material; changes none of the four scientific current files, the receipt ledger or any registry. **Not medical advice.** Reference genotype class only; no individual-level record. Association is not modulation and modulation is not rescue. Laboratory experiments are PROPOSED, never run. No registration, contact, spend or access-control bypass (two publisher PDF routes answered 403 and were not pursued; Europe PMC and NCBI open-access XML and supplement packages were used).

## 1. Two directions, one loop each

| Direction | Question | Decision | Next experiment (proposed) | Folder |
|---|---|---|---|---|
| Partial benefit | If a stress response is compensatory or harmful, which kinase, endpoints and window? Do the AFG3L2/HRI (PMID 37804316) and mGluR/ATF4 (PMID 41706892) leads resolve an open WWOX question? | **Neither resolves it; transfer UNVERIFIED.** They change the design: the ISR sign is lesion-dependent (two opposite precedents), the E01 attenuation-only framing is incomplete, and neuronal activity is an unaddressed confound for ATF4 protein in hyperexcitable WWOX systems | isogenic WWOX-null against corrected neural lines: ATF4 protein / P-eIF2a with and without activity silencing, sampled around the first hyperexcitability, kinase attribution by genetics, optional potentiation arm with target-engagement control | `loop1_partial_benefit/` |
| Broad recovery | Is restoration after onset shown, and how does it depend on residual function and lesion? Shank3 (34253921), Meis2 (42587157), Csnk2b (42190665) | **Two of three show post-onset restoration of circuit/behaviour endpoints (Shank3 same gene; Meis2 bypass), Csnk2b has no post-onset arm; transfer UNVERIFIED.** Supports an endpoint-class hypothesis (function recoverable, prenatal progenitor composition not) for WWOX | post-onset add-back in organoids with same-organoid baseline, vector control, persistence and variant-class contrast; slower-onset allele after EEG-defined onset | `loop2_broad_recovery/` |

Both loops carry observation, inference, hypothesis, need, intervention search, comparison, next experiment and regenerated queue in their own README. Rectangular tables: `loop1_partial_benefit/loop1_readings.tsv`, `interventions.tsv`, `loop2_broad_recovery/loop2_recovery.tsv`.

## 2. Receipts staged (`disease-models/wwox/research/receipt_staging/scientist-b/`)

Next free sequence per PMID is `-01` (no ledger event, no staged file in any worktree for these PMIDs on 2026-10-29). All validated with `staged_receipt_check.py --artifact-root <root> --check-doi` (OK). All `partial_fulltext_read`, closed coverage vocabulary, understated; the recorder was not run (integrator records them in event-ID order).

`FTR-20261029-37804316-01`, `-41706892-01`, `-42587157-01`, `-42190665-01`, `-34253921-01`. Sources on disk (gitignored root `files/`): `files/fulltext/PMC10907083_PMID37804316_europepmc_fulltext_2026-10-29.xml` and siblings; supplements and figures under `files/supplement/PMID37804316/`, `PMID42587157/`, `PMID41706892/`. `paper_packet.py rank` reported no figure-bearing surface before acquisition (so figures were acquired); the Brain Figures 1, 4, 5 and the Meis2 Figure 5 were opened as images.

## 3. Queue changes (and why that far)

Applied by `apply_queue_edits.py` (idempotent). Needs: `NEED-ISR-ATTENUATION` O9, O10 + 3 inferred + 1 counter-evidence; `NEED-WWOX-GENE-ADDITION` O4 to O6 + 1 inferred + 1 counter-evidence. Cards (packets edited, cards rebuilt by the bridge): `E01`, `C01`, `C04`. `view/work_order.json`: two entries and a docs id. Positions before and after are compared in section 4. No new need and no new card: no WWOX observation justifies one.

## 4. Propagation and checks

See section 8 (filled after the run).

## 5. Registry, ledger and hypothesis edits NOT mine (for the batch path)

1. Receipts above (integrator, event-ID order).
2. Discovery ledger leads: (a) "ISR sign is lesion-dependent: AFG3L2 protective (HRI/DELE1 loss worsens, GADD34-targeted compound benefits) against PARS2 harmful; falsifier: a WWOX-null versus corrected neural contrast with kinase attribution"; (b) "ATF4 protein rises with mGluR activity without mRNA change; activity-silencing control required in hyperexcitable WWOX systems"; (c) "post-onset restoration of circuit endpoints in Shank3 (same gene) and Meis2 (bypass); endpoint-class hypothesis R1 for WWOX".
3. Therapeutic hypothesis ledger: HYP-20261026-10 and -11 (ISR): add the potentiation arm and the activity control to Stage 1; no status or score change proposed.
4. Paper registry: five new PMIDs read in part; the three non-WWOX recovery papers and the two ISR papers are OTHER_DISEASE_PRECEDENT, not WWOX evidence.
5. Scout note: `scout_it7_20261029.md` row for PMID 37804316 says "the benefit came from Sephin-1 ... which inhibits GADD34"; PMID 28447936 disputes that target (abstract level) - annotate on the next scout revision.

## 6. UNVERIFIED (union)

See the last section of each loop README. Headline: no kinase is known in any WWOX system; the activity route was shown for Atf4 mRNA/protein only, not for canonical targets; the ChEMBL PPP1R15A row's primary assay; Meis2 Methods and supplementary tables; Shank3 neuron tracking identity; existence of a restorable Wwox allele.
