# COMMIT CANDIDATE — CC-20261004W13-C-PHOSPHOCODE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 13 2026-10-04, branch `task/sci-C-20261004w13`.
**context_policy:** `QUESTION_DRIVEN` (the PAPER 150 sentence was held before the surfaces were opened).
**Not medical advice.**

## Target

`disease-models/wwox/registries/paper_registry_current.md` · `PAPER 150` (Liu 2018, PMID 30158849):
one phrase in the `Role` field.

## What is wrong now

The selection row asked whether the **negative** *"pT12 is ABSENT from this 2018 review"* survives the
full artefact. It does. A wave-13 FIND-X search found no WWOX threonine-12 token in any of these:

* the body;
* the cells of Table 1;
* Figures 1–5, all inspected as images. Figure 3's red "T212" is a tau site.
* the deposited spreadsheet, dumped cell by cell.

The same search also tests the **positive** phrase that precedes it in the same sentence, *"pY287 to
proteasomal turnover"*, and that phrase **fails**. No Tyr287, Y287 or pY287 token occurs on any surface;
the only "287" sits inside a reference DOI. The review names two WWOX residues, Ser14 and Tyr33. Its one
WWOX–proteasome sentence presents WWOX as a chaperone that prevents degradation by the
ubiquitin/proteasome system, then turns to Tyr33.

The phrase entered with `CC-20261003W3-B-REGISTRY-01`. It is not in this paper's Part 1 dossier. A Y287
phosphorylation–degradation link does exist elsewhere in LEGEND's research layer, in the discovery ledger
and in `analysis/peptide_intervention_audit_20260920.md`, attributed to other sources. This record simply
attributes it to the wrong paper. This candidate removes the attribution only; it says nothing about
whether the Y287 biology is true.

## Change class

**MINOR.** A paper-registry field. `Claim links: none`; no claim and no working-model block.

## Ordering

Receipt `FTR-20261004-30158849-03` (`scratchpad/receipts_pending_w13/sciC_30158849_1.json`) first.

## Op list — `paper_registry_current.md` (record-scoped; dry run EXECUTED, nothing written)

```json
[
 {
  "op": "replace-within",
  "id": "PAPER 150",
  "old": "pY287 to proteasomal turnover; pT12 is ABSENT",
  "new": "[pY287 struck 2026-10-04 by `CC-20261004W13-C-PHOSPHOCODE-01`: no Tyr287, Y287 or pY287 token occurs on any surface of this review — body, Table 1, Figures 1-5, deposited spreadsheet; its only WWOX residues are Ser14 and Tyr33, and its one WWOX-proteasome sentence frames WWOX as a chaperone against proteasomal degradation and then turns to Tyr33]; pT12 is ABSENT"
 }
]
```

Dry run: `record_scoped_edit.py replace-within --file disease-models/wwox/registries/paper_registry_current.md
--id "PAPER 150"` → `scope 'PAPER 150': span 744027→746578`, `DRY RUN — nothing written; 1 op(s)`, at
commit `b07016a0`. The `old` string occurs once in the record; the only other occurrence in the
repository is inside `CC-20261003W3-B-REGISTRY-01`, an already-propagated candidate that is not edited.

## Also recorded, no op proposed

The deposited file captioned *"TABLE S1 Functional comparison between ER and WWOX in neurodegeneration"*
actually holds 169 brain-structure expression z-scores plus a filtered sheet — the data behind Figure
2A. The ER/WWOX comparison is the in-body Table 1. This is a deposit mislabel in the source, carried in
the manifest and dossier; no registry record depends on it.

## Registry records for this PMID

None owed (`PAPER 150`, `LIT-0033` and `CORPUS-STUB-006` exist).

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The review ties Ser14 phosphorylation to differentiation and disease progression | During cell differentiation or disease progression (e.g., AD), WWOX is phosphorylated at Ser14 | PMID 30158849, section on Ser14, `files/fulltext/PMID30158849_Liu2018_PMC.xml`
2. The review ties Tyr33 phosphorylation to apoptosis under stress | Under stress conditions, WWOX is phosphorylated at Tyr33 to induce apoptosis. | PMID 30158849, section on Ser14, same artefact
3. The review's WWOX–proteasome statement is about chaperone function, not a residue | WWOX probably functions as a protein chaperone to prevent protein misfolding and degradation by the ubiquitin/proteasome system. | PMID 30158849, same artefact
4. The review's final residue-specific section concerns Tyr33 | A pTyr33-WWOX Peptide as an Agent for Blocking Neuronal Injury and Death | PMID 30158849, section heading, same artefact

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261004_007` · 2026-10-04 · ACTOR_ID `scientist` (Scientist Q, batch integrator)
**Working model:** WM_v7.19 -> WM_v7.20 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit (BEFORE propagation, auditor had not seen this candidate):** 4 triples — 4 SUPPORTED
**What landed, and what the audit changed:** Landed with three bounds the audit measured: the paper is a REVIEW with no Methods that measures and mutates nothing; it names only two WWOX residues and maps no residue to a functional outcome with a statistic; and its deposited supplementary table does not match its own caption, holding a brain-atlas expression sheet instead.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record, no geography and no parent-of-origin detail is carried.
