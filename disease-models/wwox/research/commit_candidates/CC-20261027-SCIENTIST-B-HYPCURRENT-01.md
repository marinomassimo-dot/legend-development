# CC-20261027-SCIENTIST-B-HYPCURRENT-01

- **Class:** ORDINARY (research layer; no consolidated baseline claim, no working-model change, no score changed).
- **target_wm_version:** none.
- **Source:** package W1.2 of `scientist-b` (task `SB-IT2-HYPCURRENT-20261027`, branch `task/sb-it2-hyp`). Reading depth, stated: **no primary paper was re-read.** Read in this package: the four ledger records (`therapeutic_hypotheses_ledger_current.md`), dossier `fulltext_dossiers/PMID25012504.md` (a full-text dossier made by others, receipt `FTR-20260814-25012504-01`) and `DL-MECH-095`, `DL-BIO-008`, `DL-BIO-009`, `CLAIM 042`, map records `R-05`, `N-06`, `N-08`, CHAIN E, and the two Lucas-Clarke reconciliation notes. Every correction below traces to one of those records.
- **What this does:** adds one `CURRENT READING` pointer line to `HYP-20260709-01`, `-05`, `HYP-20261026-10`, `-11`; marks the superseded formulations in `HYP-20260709-01` as historical in place (nothing deleted); withdraws the unjustified "only falsifier" wording. **No score, status or ranking is changed, and no second ranking is created**: the pointer names the existing ranking line.
- **Apply:** `python3 disease-models/wwox/research/drug_repurposing/hypcurrent_20261027/apply_ledger_edits.py <ledger> --write` (19 `old_str -> new_str` pairs in `ledger_edits.json`, each unique at application; dry run is the default). Verified on a copy of the ledger at baseline `d85d6a55`; `legend_lint.py`, `growth_anchors.py check` and `test_link_targets.py` give the same verdicts with the edits applied (lint WARN is the pre-existing baseline).

## Finding 1 - which value could be picked (13/15 versus 12/15)
`HYP-20260709-01` carries two ranking lines: the updated 2026-09-21 line (12/15, evidence 1/3) and the "precedente" 2026-07-10c line (13/15). **No script reads either**: `repurposing_join.py` and `repurposing_bridge.py` score nothing and read no hypothesis score; `session_self_eval.py` and `test_link_targets.py` only name the ledger path. The only 13/15 in an operational use was the iteration-1 prediction note (`gse156243/prediction_hif1a_pdk_chain_20261025.md`), now carrying an erratum. The cards cite the hypothesis by id and status only (`E04`: "ranked, proposed-to-L9"), no score. The edits label the 13/15 line `HISTORICAL, SUPERSEDED: DO NOT SELECT` and the 12/15 line `CURRENT Ranking`. Other 13/15 values in the ledger belong to other hypotheses (HYP-20260709-06).

## Finding 2 - the checks asked for
| Check | Result |
|---|---|
| Transcript not a flux | Held in the 09-21 and 10-25 bullets, but the 07-09b "key enzyme measured" bullet and the 07-10 "strengthened" bullet still read as if transcripts closed the chain. **Corrected in place** (qualifiers; dossier of `PMID 25012504`: PDH phosphorylation, PDK activity and flux through PDH not measured). |
| Non-significance not equivalence | The 09-21 bullet already says so for PDH activity. The 07-10c bullet's "normal" (clinical screens of one or two patients) is likewise absence of reported abnormality. Added the "non-significance, not equivalence" qualifier where Seahorse normal is said to make the hypothesis "fall". |
| Paediatric protocol not suitability | `Sicurezza: verde` and `Traslabilita: alta` of HYP-01 could be read as WWOX suitability. **Qualified**: they describe the generic monitored epilepsy protocol. `HYP-20261026-10`: the paediatric tolerability dataset is in a disease of eIF2B itself; stated as not suitability (already yellow). |
| Seahorse not PDH-specific, not the only falsifier | **Not held** in the ledger (HYP-01 said "unico" four times), the map (R-05, CHAIN E, E-3, tools row) and `DL-BIO-009`. PDH-specific alternatives were already recorded elsewhere (`DL-MECH-095`: phospho-PDH; `biological_needs.md`: PDH activity, phosphorylated PDHA1, labelled pyruvate/lactate/acetyl-CoA; the dossier: isotope tracing) but not in HYP-01. **Corrected**: Seahorse is a general screen (and the mouse MEF already shows reduced OCR); readouts listed: PDH activity in a phosphorylation-preserving lysate, phospho-PDHA1 (Ser293, ESPANSIONE, numbering to be checked), 13C-glucose or ketone tracing, pyruvate/lactate ratio, NADH/NAD+. `DL-BIO-009` is NOT edited here (discovery ledger; see "Left for the integrator"). |
| Non-neural datum not neural | The PDH-activity datum is a skin-fibroblast line; the PDK1 transcript is mouse MEF; marked non-neural. The organoid datum is neural but a transcript and age-confounded (already in the 10-25 bullet). |

## Findings 3 - other corrections the record required
- **Digoxin "reverts the phenotype" (HYP-01 07-09b):** `DL-MECH-095`: the in-vivo readout is acute blood glucose 40 min after one injection, transcript panel n=2 and GLUT1/PHD3 not PDK1, dose ambiguous. Qualifier added.
- **HYP-05 safety wording** ("dose-dependent peripheral neurotoxicity in a child"): narrowed in map `N-08` on 2026-10-24 (no registry source for the old phrase) but the ledger kept it. Marked historical and pointed at the N-08 wording. "HYP-01 domina HYP-05" qualified as untested portfolio judgement (N-08).
- **"Four independent human sources normal"** (HYP-01 07-10c; map CHAIN E and R-05 risk row): `N-06` (2026-10-24, blind-audit adjudicated) and `DL-BIO-008` give one complete screen plus one opposite-direction MRS case; `DL-BIO-009` names four. **Not reconciled by me** (I did not read those papers): flagged as disputed in the ledger and the map, direct edits in the map.
- **Map R-05 "seizure improvement in 3/5 WOREE":** `CLAIM 042` states the exposed denominator is not stated (3/5 is not a response rate), responders carry splice-region or deletion alleles and none missense. Added in the map.
- **HYP-20261026-10 / -11:** no wording correction needed; pointer lines added.
- **Q-N-14 (antioxidants):** no hypothesis in the ledger depends on it; only map `N-14`. Nothing to mark. Q-N-06 reads HYP-01/-11, Q-N-08 HYP-05/-01, Q-R-05 HYP-01.

## Decisive scientific changes (scientist-d should verify independently; the producer cannot)
1. "Seahorse is the only falsifier / a normal Seahorse makes HYP-01 fall" replaced by "a general screen; PDH-specific readouts discriminate; normal in non-neural cells is non-significance and does not exclude a neural block". Verify: that Seahorse OCR/ECAR is not PDH-specific, and that listing the alternatives (including Ser293, which comes from general knowledge and not from this repository) is justified.
2. "PDK1 is measured, so the chain is no longer two-hop" qualified: transcript only; PDH step inferred (dossier lines on PDH phosphorylation/flux not measured).
3. Digoxin qualifier (from `DL-MECH-095`, not re-read at the paper).

The other edits are labelling (historical markers, pointers) or alignments to already-corrected records.

## Left for the integrator / not done
- `DL-BIO-009` still says "L'unico test che puo falsificare ... resta il Seahorse" and "quattro volte"; `DL-MECH-020` and `DL-BIO-008` item 2 say "l'endpoint corretto resta Seahorse". Same correction owed in the discovery ledger.
- Cards `E04` (generated by `build_cards.py`) name Seahorse as "the existing minimal falsifier" and do not say "only"; left unchanged. Adding the PDH-specific readouts to `next_measurement` needs a card regeneration.
- No deterministic check added: no existing tool parses hypothesis scores, so none can host one.
- `PAPER 567` note conflates text 1.19 with table 1.29 (reconciliation note section 0); a registry record, not touched here.
