# CC-20261019-SCIENTIST-A-LIPID-02 — oleate and WWOX knockdown in HCC (PMID 39500530) and the lead that rested on it

`context_policy: QUESTION_DRIVEN`. **Author:** ACTOR_ID `scientist-a`, metabolic batch G1, 2026-10-19, task `METAB-G1-A-20261019`.
**Status:** `PROPOSED — NOT PROPAGATED`. **Change class: MINOR** (a source-note correction on a research-layer lead plus identity records; no baseline claim is touched). `target_wm_version`: next MINOR after the integrator's current value; no working-model line is edited here.
**Nothing here is medical advice.** PAPER, LIT and FT numbers are provisional and are renumbered by the integrator.

## 1 · Landings and notes

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 39500530 (Liu S 2024, J Immunother Cancer, WWOX tuning of oleic acid signalling in HCC) | `FTR-20261019-39500530-01` | Promote `CORPUS-STUB-015` / `LIT-0042` to a full `PAPER` record, depth `complete_fulltext_read`, T3, relevance LOW; correct the source note of `DL-MECH-015` (section 3) |

## 2 · PAPER record content

What it measures: shRNA knockdown or lentiviral overexpression of WWOX in four human HCC lines; conditioned-medium oleic acid by one untargeted metabolomics run (n = 5 versus 5) and by ELISA (about 1.3-fold up with knockdown, 0.6 to 0.8-fold with overexpression); SCD5 and NME2 expression, co-IP and DNA pulldown; humanized-mouse orthotopic tumours; a 57-patient serum and 176-patient tissue-array series. No germline loss, no neural cell, no tissue or serum lipid measurement in any WWOX-reduced animal.

Note text to carry:
🔴 **A tumour-cell-line knockdown result in conditioned medium; do not read as a WWOX-null lipid phenotype.** Oleate dose used on macrophages is not stated in the text or supplementary methods; the supplementary ELISA method describes only the WWOX kit; shWWOX tumours are about 2.6-fold heavier without PD-1, so the PD-1 resistance arm is confounded with growth; the clophosome arms are all under anti-PD-1 (no IgG plus clophosome arm); the SCD inhibitor (dual SCD1/5) was tested in Huh7 models with no shWWOX arm; Supplementary Table 2 gives WWOX-expression counts (6/23 and 22/6) that sum to 29 and 28 against header totals of 28 and 29. WWOX residues 106-414 (SDR-containing) are required for NME2 binding in this system (co-IP, one cell type). Human SCD5 has no mouse or rat orthologue in Ensembl (REST query, 2026-10-19).

## 3 · Op list for `discovery_ledger_current.md` (record-scoped; dry run executed at this branch's base, nothing written)

```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-015",
  "old": "(già integrato; riletto nel batch)",
  "new": "(🔴 **source note corrected by `CC-20261019-SCIENTIST-A-LIPID-02`:** no receipt and no PAPER record existed for this PMID before 2026-10-19 (CORPUS-STUB-015, not_processed); the first full-text reading is `FTR-20261019-39500530-01`, complete, 22 locators. What it measured: WWOX knockdown or overexpression in four human HCC lines, in conditioned medium, about 1.3-fold more oleic acid with knockdown and 0.6 to 0.8-fold with overexpression, by ELISA and one untargeted metabolomics run, n = 5 versus 5; no germline loss, no neural cell, no tissue or serum lipid measurement; the oleate dose used on macrophages is not stated; the PD-1 resistance arm is confounded with 2.6-fold faster shWWOX tumour growth; the macrophage-depletion arms are all under anti-PD-1; the SCD inhibitor is dual SCD1/5 and was tested in Huh7 models with no shWWOX arm. Human SCD5 has no mouse or rat orthologue in Ensembl (REST query 2026-10-19), so the SCD5 arm of the minimal experiment needs human cells, not a Wwox-null mouse.)"
 }
]
```

Dry run: `scope 'DL-MECH-015': span 99252→100835`, `DRY RUN — nothing written; 1 op(s)`. The `old` string occurs once in the record. The lead's Status, causal statements, belief and minimal experiment are unchanged; the minimal experiment's SCD5 step is flagged by the species note.

## 4 · Queue entries proposed (no Scientist mints FT identifiers; the queue is a registry surface)

Three WWOX-direct references of this paper are in neither the receipt ledger nor a per-paper queue entry: the 2018 report on a WWOX polymorphism and HCC prognosis (PMID 29675105), the 2021 report on toosendanin activation of WWOX in HCC (PMID 34015398), and the 2004 report of Wwox and AP-2gamma (PMID 15548692, already in the surface-absent PDF-font group of the queue). Priority MEDIUM, parent PMID 39500530.

## 5 · What must NOT be written

- No statement that WWOX loss raises oleate in vivo, in neural tissue or in any animal.
- No promotion of `DL-MECH-015` to a claim; no therapeutic statement about SCD inhibitors.
- No individual-level content (none in the source).

## 6 · Registry statements to re-check at integration

`CORPUS-STUB-015` and `LIT-0042` (not processed). `DL-MECH-015` source note ("già integrato; riletto nel batch") is unsupported by any receipt before this reading.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. OA is named as the most upregulated metabolite in knockdown supernatants | The results of difference analysis suggested that OA was most significantly upregulated in the supernatants of HCC cells in the shWWOX group compared with the control group (figure 4B). | Results, section 4, `files/fulltext/PMID39500530_LiuS2024_PMC.xml`
2. The macrophage-clearance experiment shows anti-PD-1-treated groups only | Remarkably, PD-1 treatment significantly reduced tumor growth in the huh7-shWWOX group of mice after macrophage clearance compared with the control group (figure 3F,G). | Results, section 3, same artefact
3. The inhibitor experiment is described as Huh7 cell-derived | For further drug sensitivity experiments, Huh7 cell-derived humanized orthotopic HCC mouse models were first constructed. | Supplementary file 1, Animal experiments, `files/fulltext/PMID39500530_LiuS2024_supplement/jitc-12-11-s001.DOCX`
4. The supplementary ELISA method covers the WWOX kit only | We measured WWOX levels in serum from HCC patients using the Human WWOX ELISA Kit (Biorbyt, orb1146837). | Supplementary file 1, ELISA, same artefact
5. WWOX residues 106-414 are needed for NME2 binding | We mapped the structural domains involved in the interaction between WWOX and NME2 and found that the WWOX (106-414) and NME2 (67-152) domains were necessary for their interaction (figure 5C). | Results, section 6, `files/fulltext/PMID39500530_LiuS2024_PMC.xml`


---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_001` · 2026-10-19 · ACTOR_ID `orchestrator` (stated assumption, batch integrator)
**Working model:** WM_v7.20 -> WM_v7.21 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit:** not run — no baseline claim is narrowed and no MAJOR contingency is declared; the candidate's locator triples are carried for a later audit.
**What landed:** 1 PAPER record(s) (PAPER 250) with their LIT records. Source note of `DL-MECH-015` corrected (op dry-run and applied). Three queue entries minted (FT-195, FT-196; the third reference is already queued).
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record is carried.
