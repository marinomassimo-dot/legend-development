# Adversarial review of BATCH_20261019_029 (CC-20261029-INTEGRATOR-IT7-REGISTRIES-01)

Reviewer (not the producer), 2026-10-29. Object: `git diff f26fe0d0..1d83b54c` on `task/it7-batch`. Read-only toward the batch. Exploratory, not medical advice. The reference genotype class is not named by allele.

## Gate results (run in the worktree)

| Check | Result |
|---|---|
| `legend_lint.py .` | WARN, 0 BLOCK |
| `growth_anchors.py check` | PASS |
| `scripts/public_release_gate.py` | PASS, BLOCKS 0 (REVIEW lines are older items, none in this diff) |
| `fulltext_receipts.py verify` | OK, 920 chained receipts |
| `candidate_ops_reconcile.py <candidate>` | MATCH, ops_parsed 18 = declared 18 |
| `test_repurposing_join.py` | 84 OK (includes RegistriesIT7) |
| `scripts/test_no_closed_world_assertions_on_live_state.py` | 4 OK (path is `scripts/`, not `framework/scripts/`) |
| R4 receipts | all 7 IT7 receipts exist in the ledger; section coverage checked below |
| R5 diff scan | no PMID or e-mail literal, no allele pair, no new hex fragment except the state-history anchor |

Sources re-checked: the ovarian paper (PMC full text: PERK antibody is the total-PERK reagent; phospho-specific antibodies only for eIF2A, IRE-1, JNK), the P0a, P3 and P4 verifier reports, the P3 and P4 READMEs, the P17 `key_genes.tsv`, and PubMed metadata for the three metabolic precedents.

## HIGH

None. No change of a Status, Type, Title or Summary was found; the working model WM_v7.29 is not contradicted (R7: the model has no PDK1, glycolysis-module or ISR-direction statement; claim 025 stays in observation, which an INCONCLUSIVE module transfer neither supports nor contradicts).

## MEDIUM

M1. R2, R3 — an unnarrowed absence sentence survives in the very record the batch narrowed.
`disease-models/wwox/analysis/mechanism_intervention_map.md:683` (R-10, row WWOX_DIRECT_EVIDENCE) still reads "none in any WWOX-deficient human system". The batch registers, two screens later, that a human WWOX-null ovarian line with add-back carries phospho-eIF2A blots (non-neural) and a TMT proteome exists for silenced endothelial cells. The row is about a neural/ISR measurement but says "human system". Test `RegistriesIT7` only checks the replaced sentence at line 699, so this passes.
Fix: "none found in a WWOX-deficient human neural system (non-neural examples exist in the discovery-ledger update of 2026-10-29 on the integrated stress response)".

M2. R3 — replace-within on a previous iteration's text, mislabelled as "this iteration's own".
`discovery_ledger_current.md:4484`, `therapeutic_hypotheses_ledger_current.md:509`, `mechanism_intervention_map.md:699` are the IT6 updates (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`), edited in place. The candidate (What changes, item 1), the batch record and the test docstring all say "inside this iteration's own earlier text"; it is the previous iteration's. Consequence: a reader of the IT6-labelled bullet now sees IT7 findings (non-neural examples, the "not found by that search" rule) attributed to `BATCH_027`.
Fix (a): reword the three provenance statements to "inside the BATCH_20261019_027 update, replaced on the P0a verdict list (C1, C2, C18)". Fix (b): add to each replaced bullet a short tag "(perimeter wording narrowed by BATCH_20261019_029)". The edit itself is defensible (it narrows a false global), but the append-only carve-out should be named, not assumed.

M3. R1, R2 — DL-MECH-174 quotes a figure the batch says it does not quote, and one the verifier did not reproduce.
`discovery_ledger_current.md:4510`: "inside the decile-matched null band (95th percentile 0.389)". The candidate (last bullet of "What was deliberately NOT registered") and the batch record (DEFAULTS_TAKEN) state that neither 0.389 nor 0.396 is quoted. The verifier's independent draw gives 0.396 (p 0.0595); the conclusion is the same.
Fix: "inside the decile-matched null band (95th percentile about 0.39 on the producer's and on the verifier's draw)".

M4. R2 — J01 card keeps an unqualified negative on the organoid that the P4 verifier contradicts at assay level.
`cards/J01_glial_reactivity_modulation.packet.json:213` and `.card.json:249`, item (3): "In the human organoid, without microglia or behavioural seizures, no reactive-astrocyte programme appears (descriptive, 4 v 2 libraries)". P4 verifier item 1 (and D5): the source organoid paper reports GFAP and S100B immunofluorescence astrocytosis at weeks 15 and 24 (GFAP also marks radial glia), qPCR of astrocytic markers and an immunoblot; only the bulk-transcript deposit is flat. As worded, a transcript null reads as a biological negative; the batch touched this same field (item 1) and left item 3.
Fix: "In the deposited week-15 organoid transcripts (4 v 2 libraries) no reactive-astrocyte programme appears, whereas the source paper reports higher GFAP and S100B by immunofluorescence at weeks 15 and 24 (GFAP also marks radial glia); an assay and marker difference, not a settled absence".

M5. R4, R2 — registry sentences state "no ... readout / no statement" where the receipt shows the relevant sections were not read.
- `paper_registry_current.md` PAPER 567 update (receipt `FTR-20261029-42909904-04`: methods, discussion, abstract `not_read`): "The main text has no knockdown-efficiency statement". Add "in the Results paragraphs and the data-availability paragraph read (Methods and Discussion not read)". Same softening for the matching literature-log note.
- `paper_registry_current.md` PAPER 039 update (receipt `FTR-20261029-34268881-12`: methods, discussion not read): "no proteome, phospho-protein or flux readout of the integrated stress response or of the metabolic pathways" should read "none in the legends and Results read".
This is the "not found as absent" class the batch itself polices.

M6. R8 — RegistriesIT7 is partly self-referential and the mutation test is not recorded.
`framework/scripts/test_repurposing_join.py` (class RegistriesIT7): the HYP checks assert that the update bullet contains the words "Status `parked`" / "`generated`" and "no support is added", i.e. the bullet's own claim, not the record's Status or score field (a status change elsewhere in the block passes). The docstring says "Positive checks only" but five `assertNotIn` exist (they are justified; reword). The batch record and candidate do not state that the class was mutation-tested (each `assertIn` phrase deleted or altered must fail).
Fix: assert on the block's actual `Status:` line before and after (read from the `f26fe0d0` copy or a stored literal); record the mutation run (one phrase flipped per test) in the batch record.

## LOW

L1. R2 `discovery_ledger_current.md:4510` — "no added value for the network and for the WWOX-enriched condition at a minimum detectable effect of about rho 0.157". 0.157 is the detection limit for a signal rho at n=256; the WWOX-enriched comparison is a paired difference with interval -0.004 to +0.0002, far tighter. Say: "NET: MDE about rho 0.157; enriched minus external-only: difference -0.0015, 90 percent interval -0.004 to +0.0002 (four HIF1A edges only)". Also add the verifier's point that NET-EXT (upper bound 0.15) is the better-supported negative and the signature route is not.

L2. R2 `discovery_ledger_current.md:4510` — the lead presents the P47T test as a plain transfer; P1 states the module was chosen after the mouse P17 deposit had already been seen as discordant for LDHA/LDHB (P17 `key_genes.tsv`: Ldhb log2 -0.51, -0.48, -0.20, -0.11 in the four contrasts), and the neuron library agreed on only two of six genes (so "two human systems" is a two-system observation). Add one clause: "the module was chosen with the P17 mouse already seen as discordant for LDHA and LDHB; the neuron library agreed on 2 of 6 genes".

L3. R2 `therapeutic_hypotheses_ledger_current.md:530` — "names no LDH agent as a candidate": the README reports no compound-level list at all, so this is unverifiable either way. Say "reports no compound-level result, so no LDH agent is named or excluded".

L4. R2 `discovery_ledger_current.md:4485` — "13 contexts (human organoid, shRNA progenitors and neurons, four mouse contrasts, fly, rat, the P47T knock-in and two patient-line organoid classes)" lists 12 groups; the matrix counts the fly twice (with and without amyloid). Add "(fly with and without amyloid)". Also say that 89 of the 182 cells are UNKNOWN (P4 README) and that "ISR protein measured only in the fly" means Atf4 immunofluorescence, unchanged without amyloid.

L5. R2 `discovery_ledger_current.md:4484` — "glycolysis and respiration in Wwox-deficient fibroblasts (abstract level, PAPER 024)": the abstract says "Wwox-deficient cells"; MEF is registry-level, not abstract-level. Say "Wwox-deficient cells (mouse embryonic fibroblasts per the registry record; abstract level)".

L6. R6 `needs/needs.json:198` — "found" and the vector-control note are right, but the sibling surfaces from the P0a verifier (L2, M3) are not edited: `rescue_window_it6_20261029.md:142` still says "all conditional alleles ... are constitutive-from-development Cre lines (... Alb, BK5, Cd19, Osterix)" with no neural qualifier (the endothelial inducible Cdh5-CreERT2 allele contradicts it as written), and `rescue_window_it6_20261029.md:230` repeats the needs sentence without "found". Both are research-layer notes, outside the registry perimeter, but they feed the join. Apply the P0a verdict list (C-row P2b) there, or record the omission in the batch record.

L7. R6 J01 wording "no study in the P10 reading set was found that reads ..." is correct and bounded; "P10 reading set" is not defined in the card. Add "(the papers read for the P10 cycle, listed in `partial_benefit_it6_p10_20261029`)".

L8. R1 `paper_registry_current.md` PAPER 004 update: "link to GSE158681 rests on identical numbers per arm and on Supplementary Table 2" — the receipt marks supplement as captions_only; the sentence says "headers and dimensions only", which fits, but "identical numbers per arm" derives from the P4 cycle, not this receipt. Add "(matched in the P4 cycle)".

## What held up (checked and supported)

- Ovarian paper: total-PERK antibody (CST 3192), phospho-eIF2A and phospho-IRE-1 blots, band shift read as activation, PEO1 WWOX-null with stable add-back: matches the PMC text; "non-neural" and "no deposit" correct; no phospho-PERK claim anywhere in the live state.
- DL-MECH-174: verdict words INCONCLUSIVE, NO ADDED VALUE, "effect NOT DETECTED, NOT EXCLUDED" for the signature route match the P3 README and verifier (rho 0.143 vs 0.15, interval 0.039 to 0.243); numbers 0.329, p 0.060, 5 of 6, LDHB -0.10, PDK1 -0.08, 256 families, NET rho 0.047 reproduce; Status open, falsifier present; no hypothesis ranking, status or support changed (three HYP updates).
- Narrowed absences: neural perimeter, "deposited", "not found by that search is not shown absent", non-neural examples as examples, nearest neural metabolic readout named as a dye readout: all consistent with the P0a verifier (M1 to M5 of that report applied).
- Atf4 note: "lower in sign in all four, partly a control-group effect, only the germline-null against wild type is free of it" matches P4 verifier D6 and raw TPM; the WOREE and SCAR12 contrast is stated as source-reported, confounded, unreplicated, three and two individuals, no subgroup.
- Receipts: all seven named receipts exist and the registry text stays inside what each read (see M5 for two softenings); ledger append-only respected; no Status/Type/Title/Summary change; no e-mail, contact, spend or access bypass.
