# CC-20261029-INTEGRATOR-IT5-P2-01
- **Class:** ORDINARY, working-model change MINOR (no consolidated baseline claim reversed, no `Status`, `Type` or `Summary` changed). **target_wm_version:** `WM_v7.28`. Not medical advice; nothing here is a clinical recommendation and the cautionary position on vigabatrin is unchanged.
- **Author:** ACTOR_ID `orchestrator` (by stated assumption), Integrator worker for mandate IT5 step P2, task branch `task/it5-p2`.
- **Source material (all independently verified before this batch; not re-enumerated here):** `drug_repurposing/closed_loop_it4_e1b_20261028/README.md` and cards `H02_gabaat_inactivator_myelin_exposure` (blind audit `h02_audit` by a second actor: no HIGH defect, MEDIUM and LOW repaired); `drug_repurposing/ptc_readthrough_it4_e1a_20261028/README.md` with `ptc_alleles.tsv` and `locator_audits/2026-10-28_it4_ptc_enumeration_independent_verification.md` (counts reproduced by an independent recomputation).

## What changes and why
1. **VABAM wording.** Before: «documented in WWOX-DEE (Choi 2026), a real safety signal», read as a WWOX-specific signal. Now: documented in two WWOX-DEE children (Choi 2026, abstract level, `PMID 41442931`), selected cases, no denominator of vigabatrin-exposed WWOX children. The vigabatrin prescribing information (openFDA label set id `082d818a-4f4e-4675-98c6-91db0294e63c`, effective 2026-06-15, sections 5.3 and 5.4) gives MRI changes in 22 percent of vigabatrin-treated against 4 percent of other-therapy infants with infantile spasms (retrospective, N=205, non-WWOX; the cited study not read). 22 percent is the exposed-arm prevalence in that population and is **not** a population background; two selected cases can be shown neither to exceed nor to fall below those figures; enrichment in WWOX is not supported by any source read; susceptibility in delayed myelination is left open by the Choi authors; the cautionary clinical position is unchanged.
2. **Nonsense-allele enumeration.** 32 single-nucleotide stop-gained alleles of NM_016373.4 in the repository ClinVar snapshot (undated): 23 predicted NMD-sensitive, 1 borderline (`p.Trp335*`), 8 predicted to escape, all in exon 9; the five census read-through-candidate alleles are all predicted NMD-sensitive. **NMD classes are predictions by the 50-55 nt rule, never measurements; no WWOX NMD or read-through measurement exists.**
3. **Read-through applicability.** Read-through needs a premature stop codon, so the reference genotype class (no stop-gained allele) has no applicable target: an inference from classification, **not** evidence that read-through fails. It stays an open question for nonsense alleles of other lesion classes; "no target in a class" is never generalised to "ineffective in all WWOX classes". The census nucleotide of `p.(Arg54*)` is corrected from `c.160G>T` to `c.160C>T` (RefSeq has C at c.160).

## Version rule (prompt_batch_commit section 7)
MINOR: a block update without policy change and no baseline claim reversed. The working-model sentence is narrowed (an unsupported excess is withdrawn), the claim, its status and the BLOCK 1 caution are untouched. Not MAJOR: no reversal, no policy change in the direct-clinical tier, no urgent commit.

## Op lists (record-scoped; dry run then `--apply` with `batch_commit.py propagate`)
In the embedded `old` text of the working-model Last update line, the existing relative link to `working_model_history.md` is shown as inline code (a relative link inside a candidate under `research/` breaks the publication gate); the file keeps its link. `ops_parsed` is declared per file below: working model 3, claim registry 1, paper registry 1, literature log 1. Written by `record_scoped_edit.py apply` because `batch_commit.py propagate` accepts only the four scientific current files (default recorded in the batch record): history 2, dismissal ledger 2.

### working_model_current.md (3 ops)
```json
[
 {
  "op": "replace-within",
  "heading": "WWOX loss-of-function (WOREE / WWOX-DEE) — disease-level working model",
  "old": "**Version:** WM_v7.27_2026-10-21",
  "new": "**Version:** WM_v7.28_2026-10-29"
 },
 {
  "op": "replace-within",
  "heading": "WWOX loss-of-function (WOREE / WWOX-DEE) — disease-level working model",
  "old": "**Last update:** 2026-10-21 — `BATCH_20261019_008` (**MINOR** — MANUAL, ACTOR_ID `orchestrator` by stated assumption, operator authorisation): three candidates propagated (`CC-20261020-SCIENTIST-A-AMLEXANOX-01`, `CC-20261020-SCIENTIST-B-KETO-ENDPOINT-01`, `CC-20261021-SCIENTIST-C-CLAIM011-DOSE-ADJUDICATION-01`). **No claim created or reversed, and no `Status`, `Type` or `Summary` changed anywhere.** (1) **Amlexanox is qualified and NOT promoted:** two registry identity records (`PAPER 427`, `PAPER 428`; `LIT-0699`, `LIT-0700`), both **NOT WWOX EVIDENCE**, and one dismissal record (`DIS-41`) that marks the WWOX side `NON_TROVATO_NELLA_RICERCA` with its queries, its sources and its date — never `MAI_TENTATO`. The two measured points that record exists to carry: an independent, comparator-controlled test in patient-derived cells found amlexanox **did not relieve NMD and improved neither survival under genotoxic challenge, nor chromosomal aberrations, nor micronuclei, while the comparator improved all three**, and the action it could attribute was ascribed by those authors to **TBK1/IKKε inhibition rather than read-through**; and read-through requires a premature termination codon, which the Q230P missense substitution does not have. **Protein quantity does not prove function** (`D-39`). (2) `CLAIM 042` gains one **evidence boundary** and nothing else: the benefit in that series is a clinician-reported improvement in seizure control with no count, frequency, scale or latency on the surface this repository holds; the developmental row is identical in all five columns and two of the three responders had died; and the source **names patients 2 and 4 as previously published AND both are diet responders**, so a pooled count across WOREE series double-counts them and must name which individuals it counts. ⚠️ The artefact gap is carried, not discharged: **no PDF and no page render exists for that article**, so every signed or ranged value from it stays `PENDING_RE_ACQUISITION`. (3) `CLAIM 011`'s dose flag is **ADJUDICATED — verdict NARROW, change class unchanged** and `Status` still `flagged for review`: *dose-dependent* is true of this study's expression, P20 glycaemia and motor measures and false of its survival, weight, ECoG, myelination and gliosis measures, and the Title (rewritten here) no longer binds the word to the three domains where it is weakest. Leg 3 lands in its narrowed form — the body-weight equality at both doses is **survivor-conditioned on the low-dose side only**, an equality between unequal denominators, and therefore **neither evidence of dose grading nor evidence of its absence**. The four-asterisk bracket of the oligodendrocyte panel runs the wild-type arm to the treated bar, so that arm sits **significantly below wild type as well as not significant against untreated**, and the oligodendrocyte question is **unanswered rather than answered negatively** (different cassette, different dose, essentially no detectable protein). Both audited candidates travel with their blind audits (4 adverse of 12 and 3 adverse of 8, all repaired at source) and with the declared limit that those repairs are themselves unaudited. No intervention is recommended or discouraged for a child with WWOX-related disease. The narrative of this batch is in `working_model_history.md`.",
  "new": "**Last update:** 2026-10-29 — `BATCH_20261019_025` (**MINOR** — MANUAL, ACTOR_ID `orchestrator` by stated assumption, operator authorisation): one candidate propagated (`CC-20261029-INTEGRATOR-IT5-P2-01`). **No claim created or reversed, and no `Status`, `Type` or `Summary` changed anywhere.** (1) **The VABAM bullet of BLOCK 1 DATA is rewritten.** It no longer calls the finding a safety signal that distinguishes WWOX: VABAM is documented in two WWOX-DEE children (Choi 2026, abstract level, `PMID 41442931`), selected cases, with no denominator of vigabatrin-exposed WWOX children; the vigabatrin prescribing information (openFDA label set id `082d818a-4f4e-4675-98c6-91db0294e63c`, effective 2026-06-15, sections 5.3 and 5.4) gives MRI changes in 22 percent of vigabatrin-treated against 4 percent of other-therapy infants with infantile spasms (retrospective, N=205, non-WWOX, the cited study not read; 22 percent is the exposed-arm prevalence in that population, not a population background). Enrichment of VABAM in WWOX is therefore **not supported by any source read**, two selected cases can be shown neither to exceed nor to fall below those figures, susceptibility in delayed myelination is left open by the Choi authors, and **the cautionary clinical position is unchanged**. `CLAIM 001` gains a wave note (its `Status: conflicting evidence` is unchanged); the `PAPER 003` and `LIT-003` notes are qualified. (2) **Research layer, no working-model sentence:** the nonsense-allele enumeration (32 single-nucleotide stop-gained alleles of NM_016373.4 in the repository ClinVar snapshot, undated: 23 predicted NMD-sensitive, 1 borderline, 8 predicted to escape, all in exon 9; the five census read-through-candidate alleles are all predicted NMD-sensitive) is carried as a **prediction by the 50-55 nt rule, never a measurement**, and read-through applicability is stated by lesion class: the reference genotype class carries no stop-gained allele, so read-through has no applicable target there — an inference from classification, not evidence that read-through fails, and open for nonsense alleles of other lesion classes. Propagated to the cards, the needs register, `DIS-41` and the census; the census nucleotide of `p.(Arg54*)` is corrected to `c.160C>T`. The narrative is in `working_model_history.md`."
 },
 {
  "op": "replace-within",
  "heading": "DATA (WWOX literature)",
  "old": "- **VABAM** (vigabatrin-associated brain abnormalities on MRI) documented in WWOX-DEE (Choi 2026) — a real safety signal; **conflicting** with You 2024 (seizure reduction, no documented VABAM) and with Shaukat 2018 (*\"the spasms resolved\"*).",
  "new": "- **VABAM** (vigabatrin-associated brain abnormalities on MRI) documented in two WWOX-DEE children (Choi 2026, abstract level; selected cases, no denominator of vigabatrin-exposed WWOX children). The vigabatrin prescribing information gives MRI changes in 22 percent of vigabatrin-treated against 4 percent of other-therapy infants with infantile spasms (retrospective, N=205, non-WWOX; the cited study not read; 22 percent is the exposed-arm prevalence in that population), so enrichment of VABAM in WWOX is **not supported** by any source read and two selected cases can be shown neither to exceed nor to fall below those figures; the Choi authors leave susceptibility in delayed myelination open. The cautionary clinical position is unchanged. **Conflicting** with You 2024 (seizure reduction, no documented VABAM) and with Shaukat 2018 (*\"the spasms resolved\"*)."
 }
]
```
### claim_registry_current.md (1 op)
```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 001",
  "old": "**The WWOX VABAM anchor (PAPER 003) still has no receipt in the ledger, so whether the WWOX reports involved concurrent hormonal therapy is unknown to this repository; no status change.**",
  "new": "**The WWOX VABAM anchor (PAPER 003) still has no receipt in the ledger, so whether the WWOX reports involved concurrent hormonal therapy is unknown to this repository; no status change.** **Wave note (2026-10-29, `BATCH_20261019_025`, `CC-20261029-INTEGRATOR-IT5-P2-01`):** the Choi 2026 report (abstract level, [[paper_registry_current#PAPER 003]]) documents VABAM in two WWOX-DEE children selected for the finding; there is no denominator of vigabatrin-exposed WWOX children, so no rate can be read from it. The vigabatrin prescribing information (openFDA label set id `082d818a-4f4e-4675-98c6-91db0294e63c`, effective 2026-06-15, sections 5.3 and 5.4) gives MRI changes in 22 percent of vigabatrin-treated against 4 percent of other-therapy infants with infantile spasms (retrospective, N=205, non-WWOX; the cited study not read; 22 percent is the exposed-arm prevalence in that population, not a population background). Enrichment of VABAM in WWOX is therefore not supported by any source read, and two selected cases can be shown neither to exceed nor to fall below those figures; the Choi authors leave open whether children with genetic epilepsy related to the GABAergic pathway or delayed myelination are more susceptible. Status (`conflicting evidence`) and the cautionary clinical position are unchanged. Not medical advice."
 }
]
```
### paper_registry_current.md (1 op)
```json
[
 {
  "op": "replace-within",
  "id": "PAPER 003",
  "old": "**Note:** direct human safety signal; CLAIM 001 now conflicting evidence",
  "new": "**Note:** two case-selected WWOX-DEE children, abstract level, no denominator of vigabatrin-exposed WWOX children, so no rate and no enrichment claim (wave note of `BATCH_20261019_025` on CLAIM 001); CLAIM 001 now conflicting evidence"
 }
]
```
### literature_tracking_log_current.md (1 op)
```json
[
 {
  "op": "replace-within",
  "id": "LIT-003",
  "old": "Safety anchor. VABAM in 2 WWOX-DEE children on vigabatrin.",
  "new": "Safety anchor. VABAM in 2 WWOX-DEE children on vigabatrin (case-selected, abstract level, no denominator of exposed WWOX children; no rate or enrichment claim)."
 }
]
```
### working_model_history.md (2 ops, record_scoped_edit.py)
```json
[
 {
  "op": "replace-within",
  "heading": "Last update notes (newest first)",
  "old": "**Last update:** 2026-10-21 — `BATCH_20261019_008` (**MINOR**",
  "new": "**Last update:** 2026-10-29 — `BATCH_20261019_025` (**MINOR** — MANUAL, ACTOR_ID `orchestrator` by stated assumption, operator authorisation): one candidate propagated (`CC-20261029-INTEGRATOR-IT5-P2-01`). **No claim created or reversed, and no `Status`, `Type` or `Summary` changed anywhere.** (1) **The VABAM bullet of BLOCK 1 DATA is rewritten.** It no longer calls the finding a safety signal that distinguishes WWOX: VABAM is documented in two WWOX-DEE children (Choi 2026, abstract level, `PMID 41442931`), selected cases, with no denominator of vigabatrin-exposed WWOX children; the vigabatrin prescribing information (openFDA label set id `082d818a-4f4e-4675-98c6-91db0294e63c`, effective 2026-06-15, sections 5.3 and 5.4) gives MRI changes in 22 percent of vigabatrin-treated against 4 percent of other-therapy infants with infantile spasms (retrospective, N=205, non-WWOX, the cited study not read; 22 percent is the exposed-arm prevalence in that population, not a population background). Enrichment of VABAM in WWOX is therefore **not supported by any source read**, two selected cases can be shown neither to exceed nor to fall below those figures, susceptibility in delayed myelination is left open by the Choi authors, and **the cautionary clinical position is unchanged**. `CLAIM 001` gains a wave note (its `Status: conflicting evidence` is unchanged); the `PAPER 003` and `LIT-003` notes are qualified. (2) **Research layer, no working-model sentence:** the nonsense-allele enumeration (32 single-nucleotide stop-gained alleles of NM_016373.4 in the repository ClinVar snapshot, undated: 23 predicted NMD-sensitive, 1 borderline, 8 predicted to escape, all in exon 9; the five census read-through-candidate alleles are all predicted NMD-sensitive) is carried as a **prediction by the 50-55 nt rule, never a measurement**, and read-through applicability is stated by lesion class: the reference genotype class carries no stop-gained allele, so read-through has no applicable target there — an inference from classification, not evidence that read-through fails, and open for nonsense alleles of other lesion classes. Propagated to the cards, the needs register, `DIS-41` and the census; the census nucleotide of `p.(Arg54*)` is corrected to `c.160C>T`. The narrative is in `working_model_history.md`.\n\n**Last update:** 2026-10-21 — `BATCH_20261019_008` (**MINOR**"
 },
 {
  "op": "replace-within",
  "heading": "Changelog",
  "old": "| 2026-10-21 | **WM_v7.27** |",
  "new": "| 2026-10-29 | **WM_v7.28** | **`BATCH_20261019_025` (MINOR — MANUAL, ACTOR_ID `orchestrator` by stated assumption, operator authorisation).** One candidate (`CC-20261029-INTEGRATOR-IT5-P2-01`), propagated. No claim created or reversed, no Status/Type/Summary changed (receipts in the ledger: untouched). The BLOCK 1 VABAM bullet is rewritten from a safety signal that distinguishes WWOX to: documented in two case-selected WWOX-DEE children (abstract level, no denominator), enrichment not supported by any source read, label figures 22 against 4 percent in non-WWOX infants quoted with their provenance, cautionary position unchanged; CLAIM 001 wave note, PAPER 003 and LIT-003 notes. Research layer: nonsense-allele enumeration (32 alleles; 23 predicted NMD-sensitive, 1 borderline, 8 predicted to escape; predictions only) and read-through applicability by lesion class carried to the cards, needs, DIS-41 and the census (p.Arg54* nucleotide c.160C>T). MINOR by the version rule: no baseline claim reversed. | integrator IT5 P2 | high |\n| 2026-10-21 | **WM_v7.27** |"
 }
]
```
### dismissal_ledger_current.md, DIS-41 (2 ops, record_scoped_edit.py; the unenumerated-class sentence and revival condition (d) updated; the other lines of the record and the rest of the file proven unchanged by the editor)
```json
[
 {
  "op": "replace-within",
  "id": "DIS-41",
  "old": "are a different, **unenumerated** class: there is no count of WWOX PTC alleles and no PTC-context\n  annotation (stop-codon identity, +4 nucleotide), and no published cohort separates nonsense from\n  splice from frameshift from CNV.",
  "new": "are a different class, **enumerated only as a prediction** (update of `BATCH_20261019_025`, 2026-10-29: 32 single-nucleotide stop-gained alleles of NM_016373.4 in the repository ClinVar snapshot, undated; 23 predicted NMD-sensitive, 1 borderline, 8 predicted to escape; the classes are predictions by the 50-55 nt rule, never measurements, and no WWOX NMD or read-through measurement exists). No published cohort separates nonsense from\n  splice from frameshift from CNV."
 },
 {
  "op": "replace-within",
  "id": "DIS-41",
  "old": "(d) an enumeration of WWOX PTC alleles with stop-codon identity and the +4\n  nucleotide, which would at least make the eligible class countable.",
  "new": "(d) a transcript-level NMD measurement on a recorded WWOX nonsense allele (the enumeration with stop-codon identity and the +4\n  nucleotide exists since 2026-10-28 as a sequence prediction only), which would at least make the eligible class measurable."
 }
]
```

## Normal edits (files that are not scientific current files or ledgers)
| File | Edit |
|---|---|
| `disease-models/wwox/disease_model.md` | narrative VABAM bullet, same content as the working model |
| `analysis/mechanism_intervention_map.md` | N-04 heading and body, summary-table row (no "real safety signal"; documented, case-selected, no denominator) |
| `analysis/woree_therapeutic_class_census_20260921.md` | `p.(Arg54*)` row `c.160C>T`; READ-THROUGH row gains the dated update (prediction, applicability by class) |
| `analysis/ft116_cohort_triage_20260921.md` | the Arg264 read-through remark gains the NMD-prediction update |
| `analysis/anchor_papers_without_readings_20260921.md` | dated note: the quoted working-model phrase is superseded (the note keeps its original wording as a dated record) |
| `drug_repurposing/cards/{B01_amlexanox,B02_readthrough_class,H02_gabaat_inactivator_myelin_exposure}` and `cards_early/EB-VGB-01` | packets edited, cards rebuilt with `repurposing_bridge.py` (EB-VGB-01 card edited in the same string only, see the batch record) |
| `drug_repurposing/needs/needs.json` | NEED-WWOX-PTC-READTHROUGH observed O1, inferred and VGB statement |
| `drug_repurposing/closed_loop_it4_e1b_20261028/README.md`, `ptc_readthrough_it4_e1a_20261028/README.md` | superseded quotation reworded; nucleotide correction recorded |
| regenerated | `join/*`, `coverage/coverage_matrix.json`, `p5/*`, `view/index.html`, `view/index_shareable.html`, `analysis/pathograph_inventory.md`, `analysis/data/pathograph_export.jsonl`, `research/repurposing_batch_selection_20261029_module.md` |

## Proof the module no longer uses the superseded wording
`framework/scripts/test_repurposing_join.py::SupersededWordingGone` (3 new tests in an existing file, no new gate): no consumer surface contains «a real safety signal» or a «background rate» next to VABAM/vigabatrin; the working-model bullet states selected cases, no denominator, 22 and 4 percent, not supported; CLAIM 001 keeps its status and carries the wave note; needs.json calls the enumeration a prediction; the census nucleotide reads `c.160C>T`.

## Needs a verifier
None for the propagated sentences: each restates the independently verified material. Owed to a later actor: the 22 and 4 percent figures are the label's statement of a study not read.

## BATCH DISPOSITION

**Verdict:** PROPAGATED (working model `WM_v7.28`, MINOR)
**Batch:** `BATCH_20261019_025` (2026-10-29, MINOR, MANUAL, ACTOR_ID `orchestrator`, task `ORCH-ROADMAP-IT5-20261029` step P2)

- **VABAM wording:** propagated to the working model (BLOCK 1 DATA), `CLAIM 001` (wave note), `PAPER 003`, `LIT-003`, the narrative view, the mechanism map N-04, cards H02 and EB-VGB-01, needs, and the regenerated join, coverage, p5, both views and the handoff.
- **Nonsense-allele enumeration and read-through applicability:** propagated to cards B01 and B02, needs, `DIS-41`, the census and the cohort-triage note; predictions stay predictions.
- **Unchanged:** `CLAIM 001` `Status` (`conflicting evidence`), the BLOCK 1 vigabatrin caution, every other claim, `LD-006` (already on main).
