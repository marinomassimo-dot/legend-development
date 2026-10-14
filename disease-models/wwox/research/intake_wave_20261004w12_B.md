# Intake wave 12, 2026-10-04 - Scientist B - re-read of six gene-therapy safety papers

`context_policy: QUESTION_DRIVEN` (every paper was already held with a partial receipt; each re-read was made against the named landed records)
Branch `task/sci-B-20261004w12`. Nothing here is medical advice. WWOX occurs zero times in any of the six sources (articles and every supplement text layer read): earned nulls for the gene, read only for the transferable question, each datum with its transfer limit.

**Assigned question.** What do the owed panels and supplements add to or limit in the two standing negatives: that the developmental window for restoration cannot be bounded (DIS-033), and that DRG toxicity is not established as immune-mediated and preventable (DIS-031)?

**Short answer.** Neither negative moves. Both are strengthened or sharpened by measurement, and four wordings in landed records need correction or qualification (five MINOR candidates, none touching a `consolidated baseline` claim):

1. DIS-031 carries a wrong denominator for PMID 41078870 (1 of 11 dosed animals; the source supports 1 of 9).
2. DL-METH-118 says PMID 35229008 lacks a graded per-arm DRG incidence; its supplement holds one, and the control-versus-treated increment is large (1/4 against 3/4 to 4/4).
3. DIS-033's delivery contrast (PMID 41712282) is reproduced exactly from per-animal data but carries an unnamed confound (the same absolute dose is about 3.6-fold higher per kilogram at P10) and is an untested cross-cohort comparison.
4. PAPER 214 (PMID 42511902) carries a text-carried 4- to 6-fold DRG figure that its own Figure 5B does not support, a too-narrow liver-enzyme scope, and an "internally consistent" volume statement that is not.

The wave-5 flattened-table risk for PMID 42511902 does not apply: the article has no table at all (counts measured below).

## Per paper

| PMID | Paper | Owed sections read | Verdict | Records that wait, and what the reread does to them |
|---|---|---|---|---|
| 42422766 | Amaral 2026, intra-CSF AAV9 cargo in mouse and cynomolgus | supplement (Document S1, Data S1 workbook cell-wise), main Figures 4 and 5, Figure S6 | INGEST (supplement) | DL-METH-120 rule check (ii): "not pre-screened" confirmed ("naive" is experimental, not serology); check (iv) graded per animal exists in the supplement. DIS-031 wave-6 arm: "adverse findings at every dose" holds and is now measured (3/3 animals per dose level, 0/3 vehicle). Wording holds; sharpened in candidate DIS031-DENOMINATOR-01 |
| 41078870 | Okai 2025, four capsids ICM, steroid in every animal | supplement tables (S2, S4 as rendered page, S7, S8, S10, S11 cell-wise), Figure 5, Tables 1-3 cell-wise from JATS markup | INGEST (supplement) | DIS-031 premise (4): **denominator wrong** (1 of 11 -> 1 of 9; the four dosed animals of the one-month study were not examined in detail). DL-METH-120 worked example: headline holds; pre-screen is two-sided; regimen dose is not resolvable (per-weight dose beside per-body preparation); dose unit label differs (VG/body against VG/brain). Candidates DIS031-DENOMINATOR-01 and DL120-PRESCREEN-01 |
| 37515322 | Hudry 2023, liver injury in cynomolgus, IV and IT scAAV9 ("reference 10") | Figure 1, supplement Tables S1-S4, S6, whole-body string search | INGEST (supplement) | DL-METH-118 / DIS-031 / wave-6 `DO_NOT_CITE` for any DRG finding: **confirmed** (DRG and "dorsal root ganglia" occur once, in an abbreviation list; no DRG histopathology; Methods do not list tissues). New detail: Figure 1A plots lumbar-DRG vector genomes for both routes (exposure, not lesion), so DRG was sampled for vector and the silence is about histology. DL-METH-120 (ii): pre-dose titres measured, not an entry filter. Candidate DL120-PRESCREEN-01 |
| 35229008 | Buss 2022, AAV9 DRG ganglionopathy, cynomolgus ICM | supplement Tables S2 and S5 and Figure S2 as rendered pages | INGEST (supplement) | **DL-METH-118 two sentences overtaken by measurement**: the supplement does hold the graded per-arm incidence; control 1/4 (grade 1) against 3/4-4/4 (grades up to 3); "same order as treated" fails for this study; no incidence gradient between the two doses, extent and severity do. Candidate DL118-BUSS-CONTROL-01 |
| 42511902 | Gao 2026, four capsids neonatal IV (mouse) | all seven figures as images; table census; every registry number against the source | INGEST (figures) | **Flattened-table risk: none (no table).** PAPER 214: Figure 5B contradicts the text's 4- to 6-fold (about 8- to 18-fold for retro, more than 25-fold for PHP.eB); ALP-2c elevated in all four groups (scope of "liver enzymes raised by one capsid"); volume statement; n. DL-METH-117 wave-7 arm: arithmetic exact, volume scalar ambiguous. Candidate GAO-NUMBERS-01 |
| 41712282 | Bailey 2026, SLC13A5 knockout, P10 versus 3-month AAV9 | all eight figures, supplement PDF, Supporting Data Values (27 sheets) recomputed | INGEST (supplement and data) | DIS-033: numbers reproduced exactly (15,694 +/- 3,070, n = 14, against 1,162 +/- 742, n = 4; ratio 13.5), status unchanged; confound added (about 3.6-fold per kg); cross-cohort, untested. RL-GT-004: citrate numbers reproduced (64.9 +/- 8.0; 87.1 +/- 7.6; knockout vehicle 121.5), individual high-dose range 28-111 %, tolerability chemistry exists for the low dose only. RL-GT-002 unaffected. Candidate WINDOW-BAILEY-01 |

## The flattened-table check (PMID 42511902), measured

- `table-wrap` elements in the JATS: 0; `table` elements: 0; the word "Table" in the body text: 0 occurrences; the article declares no supplement. The wave-5 mechanism (a flattened table concatenating adjacent cells) therefore cannot produce any number carried from this paper.
- Every registry number was compared against the source instead: 1e10 vg per pup, ~2.0 g, 5.0e12 vg/kg (exact), ALT/AST only with MacpnS1: hold. The 4- to 6-fold DRG figure holds as text and fails against the panel it cites. n and volume statements: qualified. See the dossier's part-2 table and `CC-20261004W12-B-GAO-NUMBERS-01`.

## What would change the model, and what would falsify it

- **Window (DIS-033):** unchanged revival trigger (a dosing study with brain expression matched across two ages in which efficacy still falls with later age). The Bailey supplement is not that study and cannot be made into one: it lacks matched expression, a per-mass dose, an age-by-treatment test and a common follow-up time.
- **DRG immune-mediation (DIS-031):** unchanged revival trigger (a calcineurin-inhibitor versus steroid-only comparison with dose, route and sampling held constant and a power statement). Wave-12 adds measurement, not a new design: the unmedicated study (PMID 42422766) has 0/3 vehicle against 3/3 per dose level; the steroid-covered study (PMID 41078870) has 1/9 examined; neither is a controlled comparison.
- **DL-METH-118 (concurrent-control increment):** one more counter-instance to its "same order" generalisation (PMID 35229008, 1/4 against 3/4-4/4, n = 4 per arm). It would be refuted as a lead by a primate study powered for DRG incidence by arm with two or more doses and a vehicle arm that shows a treated-only lesion with a dose gradient; this paper has the vehicle arm and the lesion but no incidence gradient.

## Anything in the brief or selection that was wrong or needed qualification

- Selection row for 42511902 asked whether the per-kilogram conversion is "a table value or a flattened-text artefact": it is neither. It is a running-text sentence and the article has no table.
- Selection row for 41078870 said "whether the regimen is dose-resolved enough to bound DRG risk": it is not (single fixed regimen in every animal, no comparator, internally inconsistent dose clause), and the registry's own DRG denominator was wrong.
- Selection row for 35229008 asked for "a concurrent-control incidence, if the supplement holds one": it does (Tables S2 and S5).
- The first dossier of 41078870 said "all pre-screened as neutralising-antibody negative"; that holds only at the screening bleed (two of three AAV5 recipients crossed the threshold on the pre-dose day, and the vehicle arms include sero-positive animals).
- The first dossier of 41712282 carried "2 of 8" adult wild-type vehicle deaths from the text; the supplement lists 7 analysed animals.
- Two supplement PDFs (PMID 41078870 and PMID 35229008) have text layers that substitute a digit for the multiplication sign; the manifest verifier refuses quotes from such layers, so the tables were read from rendered pages and no locator quotes those layers.

## Registry presence

All six PMIDs already have registry landings (PAPER 184, 185, 183, 232, 214, 168 and their LIT records); this wave adds none (brief item 35). No `CC-...-REGISTRY-01` candidate is owed.

## Acquisition notes

Supplements came from Europe PMC supplementaryFiles (zip as served), stored beside the existing artefacts under `files/fulltext/` in the root checkout and hardlinked into this worktree (the corpus directory is gitignored). Per-file digests are in each manifest. No paywall, no payment, no author contact. PMID 42422766: Document S2 (an article-plus-supplement copy) was fetched and used only to confirm methods wording. PMID 41078870 and PMID 37515322: the combined PDFs were not re-read.

## DEFAULTS_TAKEN

- Derived text layers of PDFs and workbook dumps are declared as derived artefacts with extractor and call; where a PDF text layer is untrustworthy (digit-for-sign substitution) it is not quoted and the rendered page is the surface.
- Panel values read from images are labelled approximate; ratios recomputed from per-animal workbook cells are labelled as this reader's arithmetic and are not attributed to the authors.
- Candidates carry corrections and qualifications only; no op edits a baseline claim; `old` strings were measured unique in their records.
- Figure coverage is declared `read` only for papers where every main-figure image was inspected (PMID 42511902, 41712282); otherwise `captions_only` or a stated partial (see each receipt).

## DECISIONS_TAKEN

- Skipped re-reading the two combined article-plus-supplement PDFs that duplicate the JATS body.
- Did not re-derive per-animal tables other than those that gate a landed record (Tables S2 and S5 of Buss; Table S2 and Figure S6 of Amaral; Table 1 to 3 and S2, S4 of Okai; Tables S1 to S4 and S6 of Hudry; Figures 2B-C, 8A, 8B and body weights of Bailey).

## STOP_LOG

No stop. No safety-classifier halt occurred in this run; the instruction was followed anyway (one paper at a time, narrow script slices, small writes, commit after each artefact).
