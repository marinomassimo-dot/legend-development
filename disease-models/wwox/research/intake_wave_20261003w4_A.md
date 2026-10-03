# Intake wave 4 2026-10-03 — Scientist A

**context_policy:** `SOURCE_FIRST` for five of six papers; **`QUESTION_DRIVEN` for PMID 36271927** — `fulltext_receipts.py status` printed the prior receipt's conclusions before the source was opened. The first pass for all six was written down (07:33Z) before any registry record was opened.
**Actor:** ACTOR_ID `scientist` (Scientist A), branch `task/sci-A-20261003w4`. **Public edition:** class-level only. **Not medical advice.**

## Assigned question
*What does each source add to, or limit in, the claim that the published WWOX phenotype record is an independently counted series — case descriptions, the review tables that aggregate them, and the "WWOX does X to pathway Y" statements — each traceable to one primary observation; and where a debt is paid, does the primary say what the citing source said?*

## 1 · Per paper
| PMID | Verdict | Depth (receipt prepared) | What is new against the corpus |
|---|---|---|---|
| 30361190 Shaukat 2018 | **INGEST** | complete (`FTR-20261003-30361190-01`; prior was a legacy reconstruction) | Table 1 is partly a **re-description** (one author added features from other papers' images); its families column sums to 14 against a printed 13; each new child had **one** MRI at 2 months, so "progressive" is not observed here; child 2's "microcephaly" is −1.62 SD; parents genotyped, not examined; `CLAIM 031` dropped the authors' "in some of these cases" |
| 28721938 Tarta-Arsene 2017 | **INGEST** | complete (`FTR-20261003-28721938-01`) | **Same patient as Piard 2019 P8** (both alleles and every compared attribute); Piard counts him as novel and does not cite this report; first MRI had normal myelination for age; normal head circumference throughout |
| 33300063 Zhao 2020 | **INGEST** (research layer; T3) | complete (`FTR-20261003-33300063-01`) | Concordant with `24008736` on steady-state abundance (WWOX up → Beclin-1/LC3 down); flux never clamped on a WWOX arm; p-mTOR tracks WWOX dose; "mTOR/p70S6K" asserted with p-p70S6K undetected; abstract contradicts Results on basal WWOX in the resistant line |
| 32389029 Kośla 2020 (review) | **INGEST** as background | partial (`FTR-20261003-32389029-01`; figure images unobtainable) | Table 1 citations do not match its own text; WOREE defined as biallelic stops with complete loss; heterozygous-animal memory sentence cited to a Zfra/3xTg paper |
| 36271927 Baryła 2022 (review) | **INGEST** as background | complete (`FTR-20261003-36271927-01`, `inadequate_prior_coverage`) | Bibliography and figure now read: HIF1A arc resolved to identifiers; myelination "usually" contradicted by its cited aggregate (2/34) and its evidence list cites one patient twice |
| 24520212 Li 2014 (review) | **INGEST** as background | complete (`FTR-20261003-24520212-01`) | Moves the heterozygote 10/58 vs 2/60 figure under ENU; "mice" sentence cites a rat paper; metabolic-disease statement rests on homozygous knockouts only |

Dossiers `research/fulltext_dossiers/PMID<pmid>.md`; manifests `research/deepdive_manifests/PMID<pmid>.json` (all six PASS `--verify-artifacts --require-current-schema`).

## 2 · The answer to the assigned question, with its limits
1. **Case series are not independently counted, and the corpus can now show one instance at source.** Tarta-Arsene 2017's patient is Piard 2019 P8. Inside Piard he is counted once; Piard's "20 additional" is at most 19 new; any aggregate that adds both counts him twice, and one review in this wave (PMID 36271927, refs 13 and 66) already double-cites him. Limit: identity is the reader's inference (`PREMISE: INFERENZA`) — neither paper states it — though two private variants plus a dozen attributes leave little room.
2. **Review tables are re-descriptions, sometimes declared.** Shaukat's Table 1 states that it adds features one author read from other papers' images and inferred ages; its families total is off by one. Kośla 2020's Table 1 points to reference numbers that are not the primaries its text cites. These tables are not count sources.
3. **"WWOX does X to pathway Y" statements weaken at each relay.** The autophagy title becomes "suppresses autophagy" in the stub, though the measurement is steady-state protein; "mTOR/p70S6K" is asserted over an undetected p70S6K; a heterozygote tumour figure changes condition (spontaneous → ENU) in a review; osteopenia from knockout mice sits beside human disorders in an abstract; "usually reduced myelination" contradicts the cited aggregate.
4. **Where debts were paid, the primary mostly supports the record, with two precise exceptions:** `CLAIM 031` drops the authors' qualifier; `CLAIM 032` uses Shaukat for clinically well carrier parents it never examines.

**What would change the model if true:** a pooled cohort (e.g. `PAPER 018`, PMID 40875931) listing both Tarta-Arsene 2017 and Piard P8 would inflate the null/null survival denominator by one — small, but the class is small. **What would falsify the identity:** any discordant field between the two reports, or a statement by either group that they are different children.

## 3 · Registry statements that now have a primary behind them
| Record | Primary now read | Wording holds? |
|---|---|---|
| `PAPER 045` | 30361190 | mostly; "review of 23 reported cases" corrected; depth now receipted → `CC-20261003W4-A-SHAUKAT-01` |
| `CLAIM 001` (efficacy side), `DL-MECH-038` | 30361190 | **holds** |
| `CLAIM 031`, `DL-MECH-039` | 30361190 | **qualifier dropped** ("in some of these cases") → corrected in `CLAIM 031`; `DL-MECH-039` (ledger, not edited) carries the same truncated quote |
| `CLAIM 032` (carrier side) | 30361190 | **not supported** for "clinically well" parents → corrected |
| `DL-MECH-040`, `DL-MECH-045` | 30361190 | **hold** |
| `FT-121` | 28721938 | **holds and sharpened** (co-authorship → same patient) |
| `CC-20261003-A-PIARD-01` item (6) (open) | 28721938 + Piard S1 | **confirmed** from both primaries |
| `FT-074`, `CORPUS-STUB-056` | 33300063 | the "concordant" placement holds on abundance; amended on mTOR |
| `FT-111`, `DL-MECH-020` (review strand) | 36271927 | the quoted review sentences verified verbatim against the XML; bibliography debt paid |
| `CLAIM 032` (heterozygote tumour figure) | 24520212 is a citing review, not the primary | review misstates the primary → `DO_NOT_CITE` line |

## 4 · Group B hand-off (carrier question)
Nothing in these six measures a heterozygote's neurology. PMID 32389029 asserts a heterozygous-animal memory decline cited to a Zfra/3xTg paper (its ref 60, unread); PMID 24520212 must not be used for the heterozygote tumour figure.

## 5 · What the brief/selection said that the sources did not
- "two unrelated children … homozygous null alleles" (A1): the null status is by class (deletion, canonical acceptor), not measured.
- "Tarta-Arsene O is a co-author on the Piard cohort — first chance to test double counting": confirmed, and stronger than co-authorship.
- A3 "reports WWOX activating mTOR … with flux markers … confocal and TEM vesicle counts": confocal and TEM are on the **paclitaxel** arms only; no flux marker was applied to a WWOX manipulation.
- A6 "states … the heterozygous knockout mouse tumour-incidence observation": it states it under the wrong condition.
- A5 "supplies the prior for group B's carrier question": it contains nothing on heterozygous animals.

## 6 · Method notes
- A2's text layer is derived with PyMuPDF, not pdftotext: pdftotext emitted the end-of-article glyph as C0 control U+0002 and the verifier refuses such a surface. Declared in the manifest.
- Locators were sliced programmatically from the verifier's own normalised surface, so they are byte-exact by construction; two-column layouts constrain them to single-column fragments.
- A4 figures: Europe PMC 403, PMC challenge page (twice, minutes apart), Sage 403 → captions only, receipt partial.
