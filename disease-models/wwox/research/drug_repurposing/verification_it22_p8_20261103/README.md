# IT22 P8 independent verification (2026-11-03)

Verifier, not producer. Candidate 4b52da0f. Non-canonical, not medical advice, public edition (WWOX-DEE reference genotype class). Zero spend; no e-mail address used or sent anywhere. Read-only on the repository: only this directory was written. Reading depth: local tables, code and raw files only; I did not re-open any paper (no PubMed or Europe PMC call); the 5,113 nM ChEMBL value for pracinostat and the PMID 29132376 reading were taken from the package's own records and could not be re-derived (the local ChEMBL cache has no activity table).

Files: `findings.tsv` (27 findings), `recomputations.tsv` (26 recomputations), `recomputations_all_rows.tsv` and `recompute_attr.py` / `recompute_all.py` (independent attribution code, standard library, written without importing the producer code; run with `LEGEND_CATALOG_CACHE` set).

## Verdict per claim

| Claim | Verdict | One line |
|---|---|---|
| A. decision transfer scoped | PARTLY TRUE, CORRECTED | counts reproduce (69 = 45 + 24); labels match sources except four; premises travel only inside one main-target cluster (F01), class facts tagged "molecule" (F02), work_done leaks across questions (F03), "refuted" overstated for BTK (F04) |
| B. same-type pharmacology | TRUE IN SUBSTANCE, THREE DEFECTS | 897/1000 rows reproduced, every disagreement explained; censoring rule asymmetric (F05), blank-type fallback bug (F06), no absolute floor for NOT_COMPARABLE (F09); boundary does not change a hand-over (F10) |
| C. unused observations connected and consumed | PARTLY TRUE | Q8 seed set, Q4 control and 1000/1000 guard columns confirmed; but guards are recorded, not consumed: they change no hand-over (F12); Q8 axis was already in card L01 (F18) |
| D. blind-first reverse test, general fixes | NOT FULLY CHECKED | only its outputs were examined (route class, deposit-derived annotation, co-potent counts); deposit-derived annotation works but is a text match (F15) |
| E. qualification of a few hypotheses | MOSTLY TRUE | dossiers are careful and carry their own corrections; stale GSK343 text remains in the tables (F16); one hand-over (0217) lacks a limit its own cluster-mate record created (F01) |

## Per check

**(1) Decision scope.** 17 components, 13 decision sources, all opened: labels agree with the source records except (i) CGI-1746 `premise_refuted` (the same row says "measured low, not a proof of absence"; NPY itself is 0.05-0.12 cpm, so a pseudobulk BTK of 0.07-0.5 cpm excludes nothing about the NPY cell), (ii) E-02 roxadustat: the decisive datum "acts through HIF stabilisation, not the EGLN2 -> FOXO3 chain" is a class fact tagged `molecule`, so desidustat is handed over without it, (iii) E-03 nirogacestat paediatric/embryo-foetal findings are gamma-secretase class effects, (iv) IOX1 target-in-context premise untagged. All 24 `shared_premise_refuted` rows are Q4 H_HARM with the same chain and seed S116, so none should be released on chain grounds; they should be relabelled contested, not refuted. Rows I would still block or limit among the 45: PHD inhibitors (0043-0046), gamma-secretase rows (0495/0497/0498/0499 and eligible 0503/0506), valproic acid 0019. `decision_scope_untagged` is never hit, but only because every row in the 12 unscoped decisions' clusters is already ineligible (identity, benefit, modality); it is dormant, not tested (F22).

**(2) Pharmacology.** Same-type pairs are really same-type in the raw file. The fallback from `Original Affinity Units` to `Affinity Units` works for '-' (2,682 rows) but not for the empty string (2,491 rows stay '?'). The censored rule handles main '>' correctly and wrongly drops best-target '<' (londamocitinib is WEAK, not NOT_COMPARABLE). NOT_COMPARABLE appears where no same-type partner exists (fedratinib, colchicine, umbralisib: correct) but also lets a 20 uM main target (colchicine Kd 20,000 nM) through. The 1,000 nM boundary is arbitrary in principle yet inert here: no row between 803 and 3,160 nM, no handed-over row in the secondary or weak states. Pracinostat is handed over as ATTRIBUTABLE although the package's own record says 47 v 5,113 nM is undecidable (F07).

**(3) Identity.** GSK2816126/GSK126, EPZ-6438/tazemetostat, tapinarof twin: handled; none counted twice in the hand-over. Cosmetic duplicate in an alternatives string (F23).

**(4) Consumption.** Q8 seeds: sha256 of seeds.tsv equals the adapter sha; one seed row, funnel seed_units 1. Q4 control: identical except the guard column (confirmed). Guard columns: recomputed 1000/1000. But removing the seed_support_limited term from the order changes no hand-over; only work_done changes one (and it leaks across questions). "Consumed" should read "recorded" for guards.

**(5) hNPC.** "WWOX not lower" is right for progenitors (TPM 3.35 v 2.90) and incomplete for neurons (2.54 -> 0.52). S045/S046/S048 are not annotated because they are not usable seed rows (justified); S049-S052 and S132 are annotated by a text match on GSE126075. "Q2 keeps 0 of 8" measures the construction, not dependence on the second system (F15).

**(6) Novelty and duplication.** Pracinostat, desidustat, AT-13148, rineterkib, Epz004777, TAK-901, GSK2816126: correctly "known thread re-emitted". Tapinarof/Q8: the NRF2 axis and its Step 0 were already card L01 (IT10); only the AHR/EZH2 routes and the generator input are new (F18). Origins: about four independent ones across 16 hand-overs; seven rest on one organoid deposit (F19). The ERK pair (ravoxertinib, rineterkib) is counted twice against the P4a record's own statement (F17).

**(7) Role flips.** Q4, Q6 and Q8 hand-overs (6 of 16) are single-arm and invert if the unknown role changes sign; Q2 and Q5 carry both arms, so the set is robust but each row is conditional. PB2 and PB3 flip with the Q5/Q8 role; PB1 does not. Attribution-based rejections do not flip (F24).

**(8) Overstatement.** One refuted sentence: "attached to every proposal built on it (146 rows)" is 71 (F25). Others: "refuted" BTK, "consumed" guards, "new relation" for Q8, stale GSK343 sentence, "mevrometostat new to this thread" (F04, F12, F18, F16, F27).

## What would change the selection

1. Apply edge premises to every chain match (F01): 0217 razuprotafib (and 0218) gain the tizaterkib limit; if the ERK route is read as opposing, 0217 should leave Q5 H_HARM and 0198 (GSK2816126, Q5) re-enters.
2. Merge MAPK1/MAPK3 into one cluster (F17): one of ravoxertinib/rineterkib is displaced; CEP-11981 returns.
3. Carry the PHD class mismatch (F02): desidustat stays handed over only with that limit, or is demoted.
4. Pracinostat as SOURCE_CONFLICT (F07): if the 5,113 nM value is accepted, the HDAC row is WEAK and Q2 H_HARM keeps ASTX-660 only.
5. Bound-aware censoring (F05): londamocitinib becomes blocked (no hand-over change).
6. Relabel BTK as contested (F04): one BTK row would compete in Q4 H_HARM.
7. Key work_done to the question (F03): the Q8 EZH2 hand-over loses its "not a discovery" line.
