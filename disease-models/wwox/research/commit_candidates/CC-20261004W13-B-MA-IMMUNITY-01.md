# CC-20261004W13-B-MA-IMMUNITY-01 - PMID 40301740 re-read: the immunosuppression silence survives every prose surface, but the paper is not silent on immunity (pre-screen and per-animal antibody titres exist), and Figure 7 does not settle the legend-versus-text conflict

`context_policy: QUESTION_DRIVEN` (re-read of owed surfaces, intake wave 13, 2026-10-04, Scientist B). **Not medical advice. WWOX occurs zero times in the source.**
**Change class: MINOR.** DL-METH-120 is a research-layer lead tagged DATO; PAPER 188 is a corpus record. Neither is a `consolidated baseline` claim. The qualification adds measured detail and corrects one stale statement of what was not fetched.
**Target records:** `disease-models/wwox/registries/paper_registry_current.md` `PAPER 188` (one `replace-within`); `disease-models/wwox/research/discovery_ledger_current.md` `DL-METH-120` (one `APPEND`).
Receipt: `FTR-20261004-40301740-02` (prepared, not recorded) - manifest PASS - dossier part 2.

## 1 - The negative tested (FIND-X)
"No immunosuppression is reported anywhere in the paper." Surfaces searched (term list: immunosuppress*, steroid, dexamethasone, corticosteroid, methylprednisolone, prednis*, tacrolimus, cyclosporin, sirolimus, rapamycin, rituximab, eculizumab, suppress): JATS running text (abstract, introduction, methods, results, discussion, captions, table captions), Additional files 1 and 2 (all sheet XML), Additional file 3 (PDF text), Tables 1-2 (read by eye). Zero hits on each. NOT searched: pixels of Figures 1-6, the publisher PDF, the reference content. The quantifier "anywhere" ranges over those surfaces. **The negative survives.**

## 2 - What the owed surfaces add
- Methods state a pre-treatment AAV9 neutralising-antibody screen of "<= 1:50" (present; assay, cut-off rationale and per-animal values not given). DL-METH-120 check (ii) is therefore **present** for this paper, not absent.
- Additional file 2: per-animal anti-AAV9 and anti-SMN titres, 4 control and 8 treated. All 8 treated anti-AAV9 positive at day 14; anti-SMN negative in all at day 14 and positive in 7 of 8 treated at day 28; control all negative. The running text's "triggered two weeks after treatment" fits anti-AAV9, not anti-SMN. Transfer limit: a response to a human SMN transgene product in a primate; not a DRG finding; no WWOX construct is implied.
- Figure 7 panel A: two H&E fields (cervical, lumbar), no control field, no scale bar, no scoring; the panel cannot settle the legend ("minor detectable sign of toxicity") versus Results ("no signs of inflammatory cell infiltration or neuronal necrosis") disagreement. Check (iv) of DL-METH-120 (graded per animal?) is **absent**.
- Tables 1-2 (mouse serum chemistry) are now read: mean +/- SD, no n, no test.
- Check (iii): NHP one dose level, 8 treated (4 M, 4 F) and 4 control (2 M, 2 F) from the Figure 7 legend.

## 3 - Ops (record-scoped)

### Op 1 - `PAPER 188`, `replace-within` (Role field)
- `old` (verbatim, measured unique in PAPER 188 and in the file): `Tables 1-2 carry no body in the JATS and were not fetched`
- `new`: `Tables 1-2 carry no body in the JATS (read in wave 13 from the rendered images: mean +/- SD only, no n, no test)`

### Op 2 - `DL-METH-120`, `APPEND` (after the last bullet before Links, following the wave-12 append)
`- 🟢 **Append-only, 2026-10-04 (intake wave 13, \`CC-20261004W13-B-MA-IMMUNITY-01\`): the silence on immunosuppression in PMID 40301740 survives a term search over every prose surface (JATS text, both supplementary workbooks, the sequence PDF), but the paper is not silent on immunity.** Check (ii) is present (a pre-treatment AAV9 neutralising-antibody screen of "<= 1:50", no assay detail) and a per-animal antibody workbook exists (4 control, 8 treated: all treated anti-AAV9 positive at day 14, 7 of 8 anti-SMN positive at day 28); check (iv) is absent (representative images only, no control H&E field, no scale bar, no score), so Figure 7 does not resolve the legend-versus-text disagreement. Not searched: Figure 1-6 pixels and the publisher PDF. Transfer limit: SMN1 construct, one NHP dose, no WWOX datum.`

## 4 - Defaults taken
- File-to-table numbering (Additional file 1 = "Supplementary Table 1", file 2 = "Supplementary Table 2") is an inference from file order and from the sentences that cite them; file 2's animal counts match the NHP group sizes in the Figure 7 legend, which supports the NHP attribution.
- No claim is promoted; no `consolidated baseline` text is touched.

### LOCATOR TRIPLES FOR BLIND AUDIT
- (The antibody result is carried by one running-text sentence and cites a supplementary table | were triggered two weeks after treatment (Supplementary Table 2) and persisted at a stable level | Results, NHP safety and biodistribution, `files/fulltext/PMID40301740_Ma2025_PMC.xml`)
- (The Methods name an AAV9 neutralising-antibody screen before treatment | The nonhuman primates with a AAV9 neutralizing Ab of ≤ 1:50 were confirmed before treatment | Materials and methods, `files/fulltext/PMID40301740_Ma2025_PMC.xml`)
- (All 8 treated animals are anti-AAV9 positive at day 14 | `[spreadsheet attestation]` Anti-AAV9 Ab titer, Test group, D14 row: eight cells +(1:1600) to +(1:6400) | `files/supplement/PMID40301740/10020_2025_1207_MOESM2_ESM.xlsx`)
- (Seven of eight treated are anti-SMN positive at day 28 | `[spreadsheet attestation]` Anti-SMN Ab titer, Test group, D28 row: +(1:800) +(1:1600) +(1:800) +(1:6400) +(1:200) - +(1:100) +(1:1600) | `files/supplement/PMID40301740/10020_2025_1207_MOESM2_ESM.xlsx`)
- (Figure 7 legend states a minor sign of toxicity | Representative pictures showing minor detectable sign of toxicity | Figure 7 legend, `files/fulltext/PMID40301740_Ma2025_PMC.xml`)
- (Panel A has no control H&E field and no scale bar | `[panel attestation]` Figure 7 panel A shows two fields labelled Cervical and Lumbar | `files/supplement/PMID40301740/10020_2025_1207_Fig7_HTML.png`)

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261004_007` · 2026-10-04 · ACTOR_ID `scientist` (Scientist Q, batch integrator)
**Working model:** WM_v7.19 -> WM_v7.20 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit (BEFORE propagation, auditor had not seen this candidate):** 6 triples — 5 SUPPORTED, 1 NOT_SUPPORTED_AS_LABELLED
**What landed, and what the audit changed:** The adverse verdict: the pre-dose eligibility clause is NOT a described screen — no assay, no unit, no cut-off method and no per-animal pre-dose value exists on any of the seven surfaces, and the antibody table begins at day 14. Three further measurements landed: the titres RISE where the body says stable, only 6 of 12 animals carry the late timepoints, and the histology figure's legend contradicts itself inside one caption while the panel cannot adjudicate it.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record, no geography and no parent-of-origin detail is carried.
