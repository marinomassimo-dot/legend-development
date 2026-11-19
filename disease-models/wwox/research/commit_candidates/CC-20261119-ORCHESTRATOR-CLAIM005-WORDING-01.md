# COMMIT CANDIDATE — CC-20261119-ORCHESTRATOR-CLAIM005-WORDING-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-084 line) · **Date:** 2026-11-19
**Paper:** PMID 30290271 (Hussain et al. 2019; the CLAIM 005 anchor) and the organoid paper for G5
**Origin of the findings:** SCI's blind wording audit, `advisor_pilot_20261113/brainstorm_20261116/claim005_wording_audit_sci_20261119/CLAIM005_WORDING_AUDIT_VERDICT_SCI_20261119.md` (7 supported, 3 undershoot, 4 overshoot, 1 not in source, 2 unverifiable; data layer holds). G1–G9 are SCI's; the wording below is IT's and has NOT been audited.
**Status:** PROPOSED — REVISED once (section 4, 2026-11-19, after the blind audit: 4 SUPPORTED, 1 UNDERSHOOT, 1 OVERSHOOT, repaired); for `BATCH_COMMIT` ONLY after a second check of the section 4 sentences. The claim registry is NOT edited by this act.

> Public, disease-level, de-identified. Nothing here is medical advice.

## 1 · CHANGE CLASS
**MINOR.** Status, Type and the data layer are untouched; each change restores the source's limit or the unit a quantifier ranges over. One item is more than wording and is URGENT in ADV's ordering: **G8**, a quotation in the registry that drops «Il6» (see `generation_it59_20261119/TNF_SIGNIFICANCE_CHAIN_IT59.md`, which measured what rests on it: the IT10 outputs do not; text in three places does).

## 2 · Proposed wording (old = verbatim registry text, SCI §5)
* **G8 (URGENT).** In the Evidence boundary correction note replace the quoted «> 1.5 fold upregulation of both cytokines (significant at p < .05) in KO (n = 4)» by «We observed > 1.5 fold upregulation of both cytokines (Il6 significant at p < .05) in Wwox KO (n = 4) mice», and add «direction for Tnf-a is the source's; its significance is not stated (text silent, legend asterisk names no gene, figure not held); the earlier wording 'Only Il6, not Tnf-a, is significant' also said more than the text on Tnf-a».
* **G7.** «Il6 and Tnf-a transcripts are both more than 1.5-fold up by qPCR (p below 0.05, n=4/group).» → «Il6 and Tnf-a transcripts are both more than 1.5-fold up by qPCR (n = 4 per group); the text attaches p < .05 to Il6; no fold value is printed».
* **G6.** «Supports the glial axis as a modifier.» → «Supports a glial association; the authors leave cause or consequence open ('might play a role … further investigation is needed'), and a seizure-secondary reading fits at least as well».
* **G5.** «concordanza umana indipendente» → «direzione concorde per un gene (NPY; trascritto bulk di organoide) con il conteggio murino; la stessa pubblicazione sugli organoidi riporta marcatori GABAergici in aumento (GAD67, GAD1, GAD2), senso opposto alla riduzione murina di GAD65/67; l'indipendenza non è dimostrata dai due testi».
* **G4.** «non il padj più basso della lista, che è di DACT2 a 2,29e-15» → «non il padj più basso fra i geni downregolati (tabella EV2), che è di DACT2 a 2,29e-15; su entrambe le tabelle i più bassi sono HK2 (8,75e-34) e TCEAL5 (9,43e-21)».
* **G1.** After «PV-positive interneuron counts are lower in DG, CA1 and across the whole hippocampus (−44%)» add «the text also calls CA3 significantly low (the CA3 P value is on a panel not held)».
* **G2.** After «NPY-positive counts are lower in DG only» add «the authors' own summary and Abstract say 'in the various hippocampal subfields', and the whole-hippocampus panel is referenced but carries no number in the text».
* **G3.** After «Marker-positive abundance and area fraction — not cell loss, not glial cell number.» add «the authors read it as 'hypertrophy as well as hyperplasia' with activated-microglia morphology».
* **G9.** Hussain 2019 Figs 1–5 are not held; panel-level markers the record cites (NPY whole hippocampus, IBA1/GFAP in DG, qPCR asterisks) are unaudited; added to the supply list by ADV (decision page item 14).

## 3 · Order of work
(1) blind check of section 2 against the held text; (2) after SUPPORTED, `batch_commit.py propagate` ops on the claim registry in one MINOR `BATCH_COMMIT`, with dated lines on the verifier H1 and the IT22 seeds note (history is not rewritten); (3) regenerate derived pages in the documented sequence; ranking digest `ff38fcaa61295a5a` must not move.

**Not medical advice.**

## 4 · REVISION 1 (2026-11-19, after the blind audit of section 2)
Audit: `research/locator_audits/2026-11-19_claim005_wording_it59/` (6 triples, quotes verified verbatim by script, one fresh `legend-delegate`, asked sonnet/high; read back sonnet x5, effort high x5). Verdicts: T1–T4 SUPPORTED, T5 UNDERSHOOT, T6 OVERSHOOT. I checked both against the delegate's quoted source words; both hold. G4 and G5's organoid side rest on Steinberg 2021 EV tables and were verified by SCI on those tables, not in this audit.
* **G2 (T5).** After «NPY-positive counts are lower in DG only» add: «the CA1 and CA3 subfields 'did not exhibit any obvious difference' in NPY+ counts; the authors' Results summary says 'in the various hippocampal subfields' and the Abstract 'in different subfields'; the whole-hippocampus panel (Fig 2D) is referenced and carries no number in the text».
* **G3 (T6).** Replace the added clause by: «the authors write 'hypertrophy as well as hyperplasia' of astrocytes from area-fraction data without counting cells, so their wording says more than their measurement; for microglia they describe less ramified cells with shorter, thicker processes and larger soma, characteristic of activated microglia».
* **G1 (T4).** The CA3 clause reads: «the text also calls PV+ counts significantly low in CA1 and CA3 in a qualitative sentence; the stereological sentence gives P values for DG and CA1 only, and no CA3 P value is in the text».
* **Carried as limits:** whether the Tnf-a bar carries an asterisk in Fig 4E is not verifiable (figure not held); the legend asterisk names no gene.
**Next:** a second check of the section 4 sentences, then `BATCH_COMMIT` MINOR (class restated), G8 first.

## 5 · REVISION 2 (2026-11-19, after the second blind check of the section 4 sentences)
Check: `research/locator_audits/2026-11-19_claim005_wording_it59/AUDIT2_REPORT_AS_DELIVERED.md` (3 triples, one fresh `legend-delegate`, asked sonnet/high): all three SUPPORTED (T1 qualified: the DG-only reading rests on a qualitative sentence and the CA1/CA3 data are in figures not held). The G4 numbers (EV tables) were verified by SCI on the tables, not in a blind audit, and are written with that attribution.

## BATCH DISPOSITION — `BATCH_20261119_005` (2026-11-19, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED

8 record-scoped ops on `CLAIM 005` (G1, G2, G3, G4, G5, G6, G7 and the G8 correction note: the 2026-10-30 quotation dropped «Il6»; the true state is 'Tnf-a significance not stated'). **Change class restated: MINOR.** Dated lines on the verifier file (H1) and the IT22 README point to `generation_it59_20261119/TNF_SIGNIFICANCE_CHAIN_IT59.md`; `seeds.tsv` row S085 is an input and is not edited.
