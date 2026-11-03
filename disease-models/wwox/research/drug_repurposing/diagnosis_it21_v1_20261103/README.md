# IT21 V1: does LEGEND use what it holds when it generates candidates? Vorinostat as a retrospective case (2026-11-03)

Non-canonical research material. Actor `orchestrator-delegate`, package V1, branch `task/it21-v1`. Producer only: nothing here is self-ratified; the handoff list for an independent reviewer is section 7. Public edition, WWOX-DEE reference genotype class. Not medical advice. Zero spend, no external contact, no e-mail address sent anywhere. The four scientific current files, registries, ledger, ranking, queue and view are untouched. Unravel's selection of vorinostat is an external reference that is **not examined** (no record of it in the repository) and is not a WWOX label.

## 1. Decision first

**Vorinostat: conditional, narrowly, and not for the reason it was generated.**

* The proposal LEGEND generated (IT9, IT10, IT21 P2: lower glycolysis through HDAC5) is **unfavourable as written**. Vorinostat inhibits HDAC1/2/3/6 at 1 to 5 nM and HDAC5 at 3,600 nM (2,769-fold weaker, local Guide to Pharmacology release 2026.3.1). The sign of the HDAC5 action came from a record of that same file, whose affinity column nobody read. At the concentration that half-occupies HDAC1, HDAC5 is occupied 0.04 percent.
* One reason survives as a conditional research question: a pan-HDAC/HDAC6 arm in a stability test of the Q230P-class missense protein (card A01, section 4 R3). LEGEND's own card defers it until the fate of the lesion is known. That deferral is scientifically justified and stays.
* Two other reasons are insufficient and one is contrary: WWOX-expression boosting (the only curated direction is a decrease; Q230P-class transcript is already comparable to controls), the MYC question (the potent-target path points to the opposite side), LINCS reversal (single genotype contrast, frequent-hitter control not shown).
* **Where the path broke (general, not about vorinostat).** (1) The listed target of a compound was never compared with the compound's measured targets, although the table that supplied the sign held the number (P4a found this by hand for nanatinostat and wrote it as limit 3; nothing in code used it). (2) A substance present twice in the catalogue (ChEMBL record plus a DGIdb-only twin) lost its identity link between IT9 P3 and IT21 P2, and the stored reconciliation never joined 1,423 such twins because it reads the ligand id from the concept id and ignores the same id in the claim name. (3) The hand-over re-emitted clusters that P4a had already examined, because P4a records were not a decision source. (4) A lever marked `NAMED_ALREADY` says nothing about whether the card closed, deferred or left it un-run.
* **What the fix did.** Generated rows are unchanged (0 of 980 rows differ in status, qualified, z or main target; 0 qualified). The hand-over changed (figures after the independent review, section 8): eligible 141 to 154, handed over 13 to 11; identity blockers 659 to 555; 5 previously eligible rows are now stopped for attribution (nanatinostat 66.7-fold, SGI-1776 twice, two JAK2 rows); the Q2 H_HARM universe has 4 eligible rows before and 2 after. The previous exclusion of the HDAC5 cluster was correct in outcome and wrong in its stated reasons ("promiscuous" counted 11 paralogs as off-target; "identity not resolved" was an artefact).

## 2. Order of work (the forward path was frozen first)

`forward_snapshot_20261103.md` and its three TSVs were committed alone, before any reverse analysis (commit `532d5004`, the first commit of this directory). It records the question, seeds, universe, paths run, filters, destinations, the stage record of vorinostat and the four contrast cases with a prediction written before any change. Nothing below changes that file.

## 3. Trace of vorinostat, stage by stage (details: `forward_snapshot_vorinostat_trace.tsv`)

| Stage | Present | Generated | Qualified | Visible |
|---|---|---|---|---|
| Catalogue (ChEMBL record + DGIdb twin, 85 target rows on the twin) | yes | | | |
| IT9 P2 v3 / P3 (Q2 opposes rank 34; CONFLICT; `not_taken:promiscuous`) | yes | yes | no | no |
| IT9 P4c-e (HDAC5 cluster "not taken for diversity") | yes | | no | no |
| IT10 v4 + dispositions (`CONDITIONAL_IF_HARMFUL`, DOMINANT_CHAIN) | yes | yes | no | no |
| IT21 P2 (`IT21P2-0031`, `identity_not_resolved`) | yes | yes | no | no |
| P3b path B lever table (HDAC6, `NAMED_ALREADY`) | yes | | no | no |
| Ranking, investigations, dashboard | catalogue listing only | | no | no |

A mention, a catalogue row, a generated proposal and a qualified candidate are four different states; vorinostat reached the third and never the fourth.

## 4. Reverse analysis: the reasons that could justify investigating vorinostat (`reverse_reasons_v1.tsv`)

One origin counts once: R1 and R2 rest on the same generic network and seed derivation; R3, R4, R5 are different origins. Depth: internal artefacts and the local affinity tables only. **No primary paper was opened in this package, so no read receipt was recorded**; statements about papers are those of the existing cards, ledger and verification files. Statements about HDAC-inhibitor toxicity and brain exposure below are general background, not sourced in this repository, and are labelled so.

| Reason | Measured / inferred / hypothesised | Decisive assumption | Classification |
|---|---|---|---|
| R1 metabolic, HDAC5 to SLC2A1 (Q2 H_HARM) | seed and affinities measured; edge inferred (one muscle-cell knockdown); benefit hypothesised (role unknown) | vorinostat acts on HDAC5 in neural cells: occupancy 0.04 percent; local HDAC5 0.81x where SLC2A1 is 2.67x | insufficient (attribution fails) |
| R2 class I chains (Q5, Q6) | inferred chains | the potent-target path predicts the seed: Q5 z 1.9 to 2.2 (below 3); Q6 on the mimics side (z -2.7 to -7.1) | insufficient; contrary sign kept |
| R3 HDAC6/HSP90 stability of a destabilised missense protein | precedent measured outside WWOX (PAH F263S, selective HDAC6 inhibitor); vorinostat HDAC6 1.6 nM | the Q230P-class lesion is a turnover step an HDAC6 lever reaches; a pan-HDAC arm also brings class I action, which card A01 records as not reproducing the soluble mutant gain and as worsening one EEG count | **conditional** |
| R4 raise WWOX expression | curated direction contrary (CTD: decreases); paper text inverted relative to its data | transcript up gives protein up; S002 says the bottleneck is after transcription | insufficient, contrary |
| R5 LINCS reversal, NPC 4 uM 24 h, z_sum -17.6 | measured in non-WWOX cells | reversal is specific; LEGEND's own frequent-hitter control (33 of 76 S1 reversers also in a null) and reopening condition (second independent genotype contrast) not met | insufficient |
| R6 Unravel | not examined | | inconclusive |

Counter-evidence kept: pan-HDAC action in neurons is not selective; HDAC inhibitors have dose-limiting haematological and gastrointestinal toxicity and variable brain exposure (background, unsourced here, to be verified before any use); LEGEND's earlier decisions: the HDAC5 cluster was not taken for diversity (P4c-e), 4-PBA's chaperone rationale was withdrawn once and left live with a revival trigger partly answered (card A01), nanatinostat's chain was rejected as informative (NEG-03). No WWOX-system HDAC datum exists in the repository; the HDAC3 to WWOX relation in breast cancer cells is a title only. Unknown stays unknown.

## 5. The actual path for each reason (`path_table_v1.tsv`)

| Reason | Available at start? | Actual path | Interruption or exclusion | Intervention and outcome |
|---|---|---|---|---|
| R1 | yes | seed to engine (twin family) to P3 promiscuity to P4c-e diversity to IT10 conditional to IT21 identity blocker | affinity at the listed target never read (data in the sign-supplying file); twin identity lost (IT9 P3 name-exact, unverified, then strict); "promiscuous" counted paralogs | identity bridge + attribution screen: blocker is now `main_target_weak_attribution`; sibling potent-target family z_reach 0.13, action mimics |
| R2 | yes | engine rows for the ChEMBL family existed | correct filter; sibling rows never shown with the twin's | sibling columns added; decision unchanged |
| R3 | yes | card A01 to lever table (HDAC6, `NAMED_ALREADY`) to no proposal | represented, not explored; the card defers it (fate first): **justified**; the lever table did not carry the card's state | `named_already_card_state_v1.tsv` (8 levers; HDAC6: card A01, trigger live, 13 attributable compounds); deferral kept |
| R4 | yes (ledger) | reading debt; not representable in a seed-graph generator | available, not represented | not fixed (L2) |
| R5 | yes | IT7 pilot scored it; signature arm not re-run in IT21 | tool available, not used; adds nothing without a second genotype contrast | none |
| R6 | no | | not acquired | none |

## 6. The fix, what it transfers to, and its effect

Code (all general; the name vorinostat appears in no rule, list or exception):

* `generation_it21_p2_20261103/attribution_screen_it21.py` (new). **Identity bridge**: a DGIdb-only record whose Guide-to-Pharmacology claim name is `IUPHAR.LIGAND:<id>` is reconciled by the same rule as `catalog_build.reconcile_gtopdb_ligands` (ChEMBL id in the catalogue, equal standard InChIKey, not labelled, no contradicting identifier, one family). 1,630 DGIdb-only entries carry such a claim name and no concept id; of their 1,701 ligand records 1,423 are mergeable, 66 related-not-merged, 9 rejected on structure, 63 unresolved, 140 out of selection. The V1-fix adds a name check (section 8). The stored catalogue is **not** rewritten (its family ids would change for every consumer); the bridge is applied at hand-over. **Attribution screen**: measured affinity of the family's ligand(s) at the main target against the best measured human target; WEAK at 10-fold or more with a main target above 100 nM (occupancy under 9 percent when the best target is half occupied; V1-fix: a potent main target is BORDERLINE, not blocked); unmeasured or unassessable rows are not blocked (unknown is not negative).
* `run_generation_it21.py`: new `--out-dir` and `--no-v1`; `eligible()` gains one reason; P4a records are a decision source; exact first-token name match from 4 characters (IOX1 was missed at 6). `propose --no-v1` reproduces the committed IT21 P2 tables byte for byte (checked on proposals, hand-over, clusters, summary). The committed P2 results were **not** rewritten (a decoy job reads them); the v1 tables are in `results_v1/`.
* `named_already_card_state_v1.py`: a view, not a registry.

Measures (`measures_it21_v1.json`, from the committed tables):

| Measure | Before | After |
|---|---|---|
| Generated rows changed (status, qualified, z, main target) | | 0 of 980; 0 qualified |
| Eligible rows | 141 | 154 (first V1 pass 151) |
| Handed over | 13 | 11 (first V1 pass 10; see section 8) |
| `identity_not_resolved` | 659 | 555 (110 rows bridged; first V1 pass 551 and 114) |
| Attribution states over 980 rows | | not assessable 737, attributable 99, single measured target 87, weak 25, borderline potent main target 8, unmeasured 24 |
| Sensitivity (fold at or above; blocked WEAK + BORDERLINE) | | at 3-fold 59 (34 + 25), 10-fold 33 (25 + 8), 30-fold 23 (19 + 4) |
| Q2 H_HARM universe (34 rows) eligible | 4 | 2 |
| Vorinostat | not eligible, `identity_not_resolved` | not eligible, `main_target_weak_attribution` (2,769-fold), sibling z_reach 0.13 |

Contrast cases (registered before the change, `forward_snapshot_contrast_cases.tsv`): C1 GSK343 and C2 tizaterkib stay `CONDITIONAL_*`, unqualified; they leave the hand-over only because P4a already decided them (consumed output), not because of the screen (both attributable, 1.0-fold). C3a nanatinostat is stopped by the screen at 66.7-fold, in the direction P4a had taken by hand. C3b pomalidomide: no CRBN row among the 980 proposals; the glue abstention holds. Threshold sensitivity: nanatinostat and vorinostat are blocked at every threshold from 3 to 30; at 100 only vorinostat of the two. ASTX-660 (12.7; XIAP 2.8 nM) and xevinapant (34.9; XIAP 66 nM) were blocked at 10-fold in the first pass; with the absolute-potency floor both are now BORDERLINE_POTENT_MAIN_TARGET and no longer blocked (section 8). Where the previous exclusion was correct: the HDAC5 cluster (single non-neural edge reference, one origin) and the HDAC6 deferral.

What transfers: any compound whose chain runs through a target the compound hardly touches (25 blocked and 8 borderline of the assessed rows), any DGIdb-only twin of a ChEMBL substance (1,365 catalogue-wide after the name check), any cluster already examined by P4a. Rows the screen cannot assess (737 of 980, no local ligand) are unchanged and flagged, not cleared.

Tests: `generation_it21_p2_20261103/test_attribution_it21.py` (26): bridge decisions on a synthetic cache (merged, conflict, labelled, stereo, two ChEMBL ids, other source, name only, already reconciled), screen states and boundary at 10-fold, the gate and its order, P4a as decision source only when asked, the closed status vocabulary, and on the committed v1 tables: rows unchanged, none qualified, conditional probe and plausible proposal stay conditional, glue abstention, vorinostat blocker, no weak row and no P4a-decided row in the hand-over. Existing suites pass (generation 41, edge-ref 16, P4a 17 with 1 skip, ranking 71, `ranking_it8.py check` OK).

## 7. Remaining limits and independent-review handoff

Limits. L1 The screen reads one source (Guide to Pharmacology) of enzyme or binding affinity, not occupancy, exposure or cell activity; 733 rows are not assessable; the 10-fold threshold is a convention with sensitivity shown. L2 No compound-level store of contrary WWOX-level evidence (the CTD direction audit sits in the ledger); a generator cannot see it. L3 The catalogue still holds the twins; the join is applied at hand-over only; a catalogue-level repair (read claim-name ligand ids in `catalog_build.py`, rebuild) is a follow-up that changes family ids. L4 The signature arm was not re-run; no frequent-hitter control for vorinostat exists. L5 Brain exposure, toxicity and obtainability are not assessed here. L6 Unravel's rationale unknown.

Handoff, the decisive links a different actor must verify: (1) GtoPdb 2026.3.1 ligand 6852 rows (HDAC1 1.3, HDAC5 3,600 nM) and that its ChEMBL id is CHEMBL98 with an equal InChIKey; (2) that the DGIdb twin's claim name `IUPHAR.LIGAND:6852` is in the raw DGIdb export (it is, with a correction: section 8); (3) that `propose --no-v1` reproduces P2 byte for byte and v1 changes only hand-over fields; (4) the 110 bridged rows (114 before the name check): sample the merged decisions against structure; (5) the choice of 10-fold and the two borderline IAP antagonists; (6) that R3 is correctly classed conditional and the card's deferral is read as written; (7) that R1's sign provenance holds in `family_actions` (two sources, section 8); (8) that no part of this package is a ranking of vorinostat or an efficacy statement.

Files here: `forward_snapshot_*` (frozen first), `reverse_reasons_v1.tsv`, `path_table_v1.tsv`, `measures_it21_v1.json` and `.py`, `named_already_card_state_v1.*`, `results_v1/` (propose tables with the new columns).

## 8. Corrections after the independent review (IT21 V1-fix, 2026-11-03)

Non-canonical. Generated rows are still unchanged (0 of 980; 0 qualified); `propose --no-v1` is byte-identical to the committed P2 tables (now a test). Tables regenerated in `results_v1/`; figures in `measures_it21_v1.json` (`v1_fix`).

**Source statements, corrected.**
* DGIdb serves nine Guide-to-Pharmacology rows on the twin of ligand 6852, but with **wrong genes** (GDF2, GART, MSTN ...): a Guide to Pharmacology *target id* was read as an NCBI gene id. The catalogue corrects it (target id 2660 is HDAC5). The identity bridge uses only the claim name, so it is unaffected; no number in this package comes from the DGIdb gene column of those rows.
* The HDAC5 sign has two sources, not one: the Guide to Pharmacology row and a TALC row labelled "inhibitor". A DTC row for the same pair carries no action. Neither source carries a usable potency; the potency comes from the local affinity table only.
* R3 (HDAC6/HSP90 stability) is conditional on a pan-HDAC or HDAC6-selective arm, and **a pan-HDAC arm also brings class I action; card A01 records that class I action did not reproduce the soluble mutant gain and worsened one EEG count.**

**Finding 1, attribution screen.** WEAK now needs fold >= 10 AND a main target above 100 nM (`POTENT_MAIN_NM`, a stated convention: an enzyme or binding affinity at or below 100 nM is potent on its own). Fold >= 10 with a main target at or below 100 nM is `BORDERLINE_POTENT_MAIN_TARGET`: annotated in the hand-over note, not blocked. Effect: 8 rows moved WEAK to BORDERLINE (ASTX-660 XIAP 2.8 nM, quisinostat HDAC5 3.7, BI-2536 BRD4 37 twice, progesterone PGR 2.5, tretinoin RARB 6.2, xevinapant XIAP 66, amdizalisib PIK3CB 87); 25 remain WEAK. Pooled medians: a (ligand, gene) median can mix Ki, IC50 and EC50 rows; the types are now reported (`attribution_main_measure`, `attribution_best_measure`) and a pool of more than one type is `attribution_mixed_measure = yes` (24 rows; informational, never blocks alone). Among WEAK or BORDERLINE rows 9 table rows are mixed (belinostat and givinostat HDAC5, Hg-10-102-01 JAK2, molibresib BRD4 twice, BI-2536 twice, progesterone, tretinoin); the vorinostat verdict is not among them (single measure type on both sides). Hand-over before and after: first V1 pass 10 rows, now 11. Entered: ASTX-660 (borderline), tretinoin (borderline), razuprotafib (single measured target), CEP-11981; left: estradiol valerate, TO-901317, vitamin A (all three by the name check below). Sensitivity with the floor: see the measures table.

**Finding 2, identity bridge.** Equal structure is necessary, not sufficient: the twin's name must now equal the ligand's or its ChEMBL record's name after dropping counter-ion and hydration words (`SALT_WORDS`, general vocabulary). The twin name that is the parent name plus another word (ester, prodrug) is `related_not_merged`; no name match is `unresolved`. Estradiol valerate is no longer joined to estradiol (regression test with that fixture). Among the 114 bridged rows: 6 lost the bridge (estradiol valerate; vitamin A and TO-901317 whose names do not match the ligand's, a conservative loss since no synonym list exists; two DYRK1A and MAPKAPK2 rows of long chemical names), 2 gained it (triamcinolone, beclomethasone dipropionate: a twin that named two ligands, one a derivative, now joins the name-matched one); 114 to 110. Catalogue-wide decisions: merged 1,423 to 1,365, related-not-merged 66 to 100, unresolved 63 to 87.

**Finding 4, states.** A family with one measured target has nothing to be compared with: `SINGLE_MEASURED_TARGET` (87 rows; 86 were counted as ATTRIBUTABLE with fold 1.0 in the first pass, which overstated them). Rows whose main target is unmeasured while the compound is measured elsewhere (`UNMEASURED_AT_MAIN_TARGET`, 24 rows) are handed over with a note that starts with "UNMEASURED AT MAIN TARGET" and a separate `attribution_state` column, and rank after every other row in the per-group cap (`order_key`, first element). One such row is handed over now (sorafenib, ZHX2), because its group has no more measured clusters to fill the cap.

**Finding 5, contrast case for abstention.** The glue abstention (pomalidomide, lenalidomide, thalidomide CRBN rows) is **upstream** (P8-fix guard, withheld rows) and V1 does not exercise it; the test now says so. The V1 abstention is tested on rows it blocks: vorinostat and nanatinostat (weak main target, floor not met, blocked, or stopped earlier by a preceding gate) against progesterone (potent main target, not blocked).

Tests: `test_attribution_it21.py` 39 (was 26); generation 41, edge-ref 16, P3b 19, P4a 17 (1 skip) pass. Limits unchanged except: the 100 nM floor is a convention, the name check can drop true twins whose names are synonyms, and SALT_WORDS is a closed vocabulary that will need additions.
