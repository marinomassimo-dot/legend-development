# COMMIT CANDIDATE — CC-20261003-C-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 2 2026-10-03, branch `task/sci-C-20261003`.
**context_policy:** `SOURCE_FIRST` for the six readings; registry comparison made after each first pass.
**Not medical advice.** Class-level statements about published models and genotypes only.

## Why this candidate exists

Wave 1 left eight PMIDs with no registry presence and LINT blocks `BATCH_COMMIT` with
`ORPHAN_COMPLETE_READ` until a record exists. This candidate states, for **each of the six PMIDs
of group C**, whether a structured landing already exists and what is owed.

| PMID | Existing landing | Owed |
|---|---|---|
| 34268881 | `PAPER 039` · `CORPUS P365` · `LIT-0365` | **nothing** — record exists and is processed |
| 31543760 | `PAPER 022` · `LIT-0024` | **nothing** |
| 25649963 | `CORPUS P318` · `LIT-0318` | **nothing** — a corpus placeholder plus a tracking record is a structured landing; promotion to a `PAPER` record is not required by this reading and is not proposed |
| 26302329 | `CORPUS P270` · `LIT-0270` | **nothing** — same |
| 28749468 | `CORPUS-STUB-126` · `LIT-0145` | **enrichment** — both are unscreened stubs (*"not yet extracted"*, *"not yet screened"*) that now declare a first-hand reading |
| **39952983** | **none in `paper_registry_current` or `literature_tracking_log_current`** (only `FT-016`, `DL-MECH-013` and `DIS-008`) | **create** `LIT-0433` and `PAPER 135` |

So the wave-1 failure mode recurs for exactly **one** of six PMIDs, and is repaired here.

## Target

- `registries/literature_tracking_log_current.md`: **create** `LIT-0433` (after `LIT-0431`; see numbering note); **replace-within**
  `LIT-0145`.
- `registries/paper_registry_current.md`: **create** `PAPER 135` (after `PAPER 132`; see numbering note); **replace-within**
  `CORPUS-STUB-126`.

**Numbers are provisional.** Next-free numbers measured 2026-10-03 with
`registry_records.py catalog` against `0ed6ad4` (main `eb01d5f` merged): `PAPER` max 132 → next 133; `LIT-` max 431 →
next 432 — but `CC-20261003-A-REGISTRY-01` (pending) already claims `PAPER 133`, `PAPER 134` and
`LIT-0432`, so this candidate takes **`PAPER 135`** and **`LIT-0433`**, re-measured 2026-10-03 after
merging `main` `eb01d5f`. Anchors are the highest **live** ids (`PAPER 132`, `LIT-0431`); if A's
candidate propagates first, the integrator re-anchors these inserts after `PAPER 134` / `LIT-0432`. Scientists A and B of the same wave may claim the same numbers; the integrator
renumbers in event order and updates every `LIT link` / `Registry record` wikilink inside these
ops.

## Change class

**MINOR** (§ 7) — one paper addition and two stub enrichments. No claim status, no working-model
block, no evidence boundary.

## Ordering

The six receipts `FTR-20261003-<pmid>-NN` must be appended **before** these records, so that no
record declares a reading whose receipt is not in the ledger. Both records below declare
`partial_fulltext_read` and say exactly what is missing; neither declares *full text reviewed*.

## Op list — `literature_tracking_log_current.md` (record-scoped; dry run 2026-10-03 against `0ed6ad4` (main `eb01d5f` merged))

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0431",
  "text": "\n## LIT-0433\n**Short title:** Kim 2025 Sci Rep — WWOX intronic SNVs and self-reported sleep duration in two Korean cohorts, with a Drosophila Wwox hypomorph\n**Authors:** Kim S, Kang SW, Kim SE, Kim HJ, Kim SA, Lee YW, Kim EY, Shin C, Lee HW\n**Year:** 2025\n**Source type:** primary research — genome-wide association study (n = 8,840) with an invertebrate functional arm\n**Journal/source:** *Sci Rep* 2025;15(1):5552\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 39952983 / DOI 10.1038/s41598-024-81158-8 / PMC11828923\n**Date discovered:** earlier (the PMID is addressed by `FT-016` and by `DL-MECH-013`); no record existed in this log or in the paper registry until now\n**Date processed:** 2026-10-03 (first-hand read, `FTR-20261003-39952983-02`, prior `FTR-20260811-39952983-01`)\n**Discovery window:** intake wave 2, 2026-10-03, group C\n**Discovery source:** `FT-016`\n**Discovery query:** models and metabolic/ER-stress axis in WWOX loss — which endpoint could serve as a rescue readout\n**Status:** processed\n**Status note:** `partial_fulltext_read` — body, Tables 1-3, both figure images and the supplementary DOCX read; Supplementary Figures 1 and 2 (Manhattan and Q-Q plots) not inspected as images; 58-item reference list enumerated and screened mechanically, not read. 🔴 **Record created 2026-10-03 by this candidate:** the PMID was addressed by a queue entry and a discovery lead but by no registry record, which is the `ORPHAN_COMPLETE_READ` shape LINT blocks on.\n**Primary pathway:** behavioural / network-state endpoints (non-seizure)\n**Genotype/model tag:** human common intronic SNVs `rs16948804` and `rs4887991` at 16q23.1-q23.2 (one LD block, distal gene body); *Drosophila* `Wwox^f04545` insertion hypomorph, mRNA at about 8 per cent of control, homozygous, males only\n**Transferability:** T3 — no WWOX-DEE allele, no patient, no measured WWOX expression in any human\n**clinical relevance:** LOW — a non-seizure behavioural endpoint exists in the fly; the human arm licenses nothing\n**Claim links:** none\n**Working Model impact:** none — `DL-MECH-013` is qualified by `CC-20261003-C-SLEEP-SUGGESTIVE-01`, no block is redefined\n**Report mentions:** `research/intake_wave_20261003_C.md` · `CC-20261003-C-SLEEP-SUGGESTIVE-01`\n**Next action:** none owed; Supplementary Figures 1-2 remain unviewed and are not blocking\n**Flags:** read — partial; human arm below conventional genome-wide significance **by the authors' own statement**\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-39952983-02`; manifest `deepdive_manifests/PMID39952983.json` (14 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID39952983.md`\n**Registry record:** [[paper_registry_current#PAPER 135]]\n**Note:** 🔴 The paper measures **no human WWOX expression**: the Results sentence *«The associations between WWOX expression and sleep parameters are presented in Table 2»* describes a genotype table, and the same conflation appears in the Abstract. ⚠️ The declared artefacts of this paper's deep-dive manifest were **absent from the corpus** at the start of this reading and the manifest was BLOCK; a Europe PMC re-fetch returned byte-identical files, which were restored under their declared names. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0145",
  "old": "**Status:** discovered",
  "new": "**Status:** processed\n**Status note:** 🟢 **Enriched 2026-10-03 by `CC-20261003-C-REGISTRY-01`** from the stub state (*«not yet extracted»*, *«not yet screened»*) on a first-hand reading: Janczar S, Nautiyal J, Xiao Y, Curry E, Sun M, Zanini E, Paige AJW, Gabra H, *Cell Death Dis* 2017;8(7):e2955, primary research — cell-line experimental plus two public microarray survival cohorts. `partial_fulltext_read` — receipt `FTR-20261003-28749468-01`; manifest `deepdive_manifests/PMID28749468.json` (9 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID28749468.md`. Body, all eight figure images and the full supplementary legend set read; the nine-page supplementary figure PDF not inspected panel by panel; 52-item reference list enumerated and screened mechanically (`SCREENED_CLEAN`), not read. Primary pathway: ER stress / UPR (oncological context). Genotype/model tag: human ovarian carcinoma lines, PEO1 being a WWOX-null by homozygous deletion of exons 4-8; no WWOX allele of the reference genotype class and no neural material. Transferability: T3. clinical relevance: BACKGROUND. 🔴 Every quantified endpoint measures WWOX as **pro-death under stress**, so a «rescue» in this system means restoring the cell's ability to die — recorded in `CC-20261003-C-APOPTOSIS-DIRECTION-01`, which also qualifies `DL-MECH-023` because Figures 5c-5e carry no significance marker and the KIRA6 viability increment is the same in the WWOX-expressing and WWOX-null clones. Not medical advice."
 }
]
```

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 against `0ed6ad4` (main `eb01d5f` merged))

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 132",
  "text": "\n## PAPER 135\n**Short title:** Kim 2025 Sci Rep — WWOX intronic SNVs and self-reported sleep duration (n = 8,840), with a Drosophila Wwox hypomorph\n**Full title:** Genome-wide identification and functional validation of the WW domain containing oxidoreductase gene associated with sleep duration\n**Authors:** Kim S, Kang SW, Kim SE, Kim HJ, Kim SA, Lee YW, Kim EY, Shin C, Lee HW\n**Year:** 2025\n**Source type:** primary research — genome-wide association study with an invertebrate functional arm\n**Journal/source:** *Sci Rep* 2025;15(1):5552\n**Identifier:** PMID 39952983 / PMCID PMC11828923 / DOI 10.1038/s41598-024-81158-8\n**Status:** processed\n**Record provenance:** created 2026-10-03 by `CC-20261003-C-REGISTRY-01` (intake wave 2, Scientist C). 🔴 **Why it did not exist:** the PMID was addressed by `FT-016` and by `DL-MECH-013` but by no registry record, so a reading of it would have been an `ORPHAN_COMPLETE_READ` for LINT. Provisional number: if `PAPER 135` is taken when this batch runs, the integrator renumbers and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-39952983-02` (prior `FTR-20260811-39952983-01`, `inadequate_prior_coverage`); manifest `deepdive_manifests/PMID39952983.json` (14 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID39952983.md`\n**Primary pathway:** behavioural / network-state endpoints (non-seizure)\n**Model/species:** human community cohorts (Ansan n = 4,635, Ansung n = 4,205) and *Drosophila melanogaster*\n**Genotype/model:** common intronic SNVs `rs16948804` and `rs4887991` at 16q23.1-q23.2, one LD block in the distal gene body; *Drosophila* `Wwox^f04545` insertion hypomorph (mRNA at about 8 per cent of control), homozygous, backcrossed six times, males only\n**Transferability:** T3 — no WWOX-DEE allele, no patient, no measured WWOX expression in any human\n**clinical relevance:** LOW — supplies a non-seizure behavioural endpoint in the fly; the human arm licenses nothing about the reference genotype class\n**Claim links:** none\n**Role:** The only source in the corpus with a quantified **non-seizure behavioural** endpoint for *Wwox* loss: daytime sleep falls from about 500 to about 300 minutes with daytime bout length shortened, while night-time sleep RISES from about 560 to about 650 minutes and the free-running period and rhythmicity are untouched — a day-to-night redistribution, not a uniform loss, with **no rescue arm, one allele, one control background and males only**. 🔴 The human arm is **suggestive by the authors' own statement** (*«the WWOX gene did not reach the conventional genome-wide significance level»*; *«the number of subjects in each cohort was not sufficient for GWAS»*), the reported Bonferroni values imply correction over about 1.8e5 tests rather than the 6.42 million imputed SNVs, and the effect — 12 to 18 minutes — co-moves with **time in bed** while habitual sleep efficiency and the Epworth score do not move at all.\n**LIT link:** [[literature_tracking_log_current#LIT-0433]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. ⚠️ The declared artefacts of this paper's deep-dive manifest were absent from the corpus at the start of this reading and the manifest was BLOCK; a Europe PMC re-fetch returned byte-identical files (sha256 match on all four), which were restored under their declared names, and the manifest now validates PASS with artefact verification on. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-126",
  "old": "**Status:** not_processed",
  "new": "**Status:** processed\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-28749468-01`; manifest `deepdive_manifests/PMID28749468.json` (9 verbatim locators, PASS with artefact verification); dossier `research/fulltext_dossiers/PMID28749468.md`\n**Primary pathway:** ER stress / UPR (oncological context)\n**Model/species:** human ovarian carcinoma cell lines; PEO1 is a WWOX-null by homozygous deletion of exons 4-8. No neural material anywhere in the paper\n**Transferability:** T3 — no WWOX allele of the reference genotype class; the stressor is a chemotherapeutic\n**clinical relevance:** BACKGROUND\n**Role:** 🔴 Every quantified endpoint measures WWOX as **pro-death under stress**: restoring it roughly halves survival under paclitaxel and tunicamycin, removing it roughly doubles it. A «rescue» in this system is the restoration of the cell's ability to die, which is the wrong sign for a neurodevelopmental disorder — recorded as a cross-species direction in `CC-20261003-C-APOPTOSIS-DIRECTION-01`. ⚠️ The paper's central IRE-1 claim is weaker than its prose: Figures 5c-5e carry **no significance marker and no P-value at all**, the absolute viability increment from KIRA6 is the same in the WWOX-expressing and WWOX-null clones (about 0.19 against about 0.18), Figure 7e is reported as positive and prints `p=0.13`, and the Figure 6 legend declares panels a-h for a six-panel figure\n**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record. 🟢 **Read first-hand 2026-10-03 (`CC-20261003-C-REGISTRY-01`, intake wave 2, Scientist C); the stub is enriched rather than promoted, and the placeholder is kept as history.** Not medical advice."
 }
]
```

## `### LOCATOR TRIPLES FOR BLIND AUDIT`

```
(PMID 39952983's human association does not reach conventional genome-wide significance, by the authors' own limitations paragraph. | Firstly, the WWOX gene did not reach the conventional genome-wide significance level in the human GWAS results | PMID 39952983, Discussion, limitations paragraph; files/fulltext/PMID39952983_Kim2025_EPMC.xml)

(PMID 28749468's gain-of-function host line is a human WWOX-null by homozygous deletion of exons 4 to 8. | is homozygously deleted for WWOX exons 4 | PMID 28749468, Materials and methods, "Cell lines"; files/fulltext/PMID28749468_Janczar2017_PMC.xml)

(In PMID 28749468, removing WWOX increases survival under ER stress. | whereas WWOX siRNA knockdown increased survival | PMID 28749468, Results, "Paclitaxel induces ER stress response and WWOX determines cell fate in response to prolonged ER stress", para 1; files/fulltext/PMID28749468_Janczar2017_PMC.xml)

(PMID 28749468 states that PERK activation does not change with WWOX status. | No changes in activation of PERK were observed as a result of WWOX status | PMID 28749468, Results, same section, para 2; files/fulltext/PMID28749468_Janczar2017_PMC.xml)

(A PFS panel PMID 28749468 reports as showing an effect prints a non-significant P-value. | [figure attestation] Figure 7 panel e is titled "PFS by WWOX expression relative to normal, TCGA with Tax" and prints "n=333, p=0.13" in its header. | PMID 28749468, Figure 7 panel e; files/fulltext/PMID28749468_assets/cddis2017346f7.jpg)
```

---

## BATCH DISPOSITION — `BATCH_20261003_001` (2026-10-03, ACTOR_ID `scientist`, Scientist F), append-only

**Verdict:** PROPAGATED — RE-ANCHORED

Propagated record-scoped by `BATCH_20261003_001` (2026-10-03, ACTOR_ID `scientist`, Scientist F) — the ops below were read from this file by script, never retyped; every byte outside the addressed records was proven unchanged before anything was written. Post-propagation LINT: WARN, 0 BLOCK.

`paper_registry_current.md` 2 ops (**`PAPER 135` created**, `CORPUS-STUB-126` enriched) and `literature_tracking_log_current.md` 2 ops (**`LIT-0433` created**, `LIT-0145` enriched). The declared numbers were free and are unchanged; the inserts were re-anchored after `PAPER 134` / `LIT-0432`, which this candidate's numbering note asks for by name if A propagates first. Both new records declare `partial_fulltext_read` and say what is missing.
