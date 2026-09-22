# The peripheral denominator — which analytes were measured in every WWOX intervention arm ever run, which could have been and were not, and which are gone

**Node:** `PERIPHERAL_DENOMINATOR_AUDIT` · **Actor:** Scientist G · **Date:** 2026-09-22
**Class:** analysis-only. **Answers node `G3`**, ranked first by Scientist F in
[`wwox_independent_downstream_rescue_20260922.md`](wwox_independent_downstream_rescue_20260922.md) §4,
and the surviving question of
[`DISCOVERY_TRACE_metabolic_gating_20260922.md`](DISCOVERY_TRACE_metabolic_gating_20260922.md) §7.4.

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every registry,
> every queue, every ledger, every receipt and the state manifest. **Nothing promoted, nothing committed,
> no `BATCH_COMMIT`, no receipt claimed, no git command executed, no external contact, no purchase.**
>
> 🔴 **Nothing here is medical advice.** Every clinical question is `HUMAN_REQUIRED` and belongs to a
> treating team. No dose, no route, no schedule, no clinical framing appears anywhere in this file.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **Alleles, drivers and species are never pooled.** `Wwox`-null (Aqeilan strain), `Wwox^ΔCre/ΔCre`
> (EIIA-Cre, Aldaz strain), the NCKU nulls (two independent targetings, exon 1 and exon 2/3/4),
> `gt/gt` hypomorph, `P47T` knock-in, Synapsin-Cre `S-KO`, Nestin-Cre `N-KO`, Alb-Cre `Wwox^hep−/−`,
> ACTA1 `Wwox^ΔSKM`, rat `lde/lde`, human WOREE and human SCAR12 are **different objects** and appear
> in different rows throughout.
>
> 🔴 **The `gt/gt` hypomorph has no published brain WWOX quantification and no neurological phenotyping;
> its "tissues examined" list has never included brain. That is a MISSING MEASUREMENT, never evidence of
> absent brain protein.** It therefore appears in no row of §1 and supports nothing here.

---

## 0 · How the baseline was enumerated, and the scope of every absence claim below

**Five actors failed this today by guessing filenames.** I listed first, then grepped across everything
listed, **unscoped by file type**, in **both languages this corpus is written in**.

| Step | What was done |
|---|---|
| Enumeration | `find` over the whole repository: **1 451 files**; `disease-models/wwox/` alone holds **613** — 427 `.md`, **102 `.json`**, **11 `.jsonl`**, 19 `.csv`, 5 `.tsv`, 25 `.py`, 15 `.png`, 2 `.pdb` |
| Sweep scope | 🔴 **UNSCOPED.** No `--include=*.md` anywhere in this audit. Failure mode (9) — a phrase inside a JSON string field is invisible to a file-type-scoped grep — was found in this repository **yesterday evening**, and every load-bearing number below lives in `.json` (`deepdive_manifests/`, `page_adjudications/`) or `.jsonl` |
| Language scope | 🔴 **BILINGUAL.** The registries and the hypotheses ledger are written in **Italian**; the analyses in English. Every term was swept as `EN|IT` (`acidosis\|acidosi`, `spleen\|milza`, `platelet\|piastrin`, `hypocalc\|ipocalcem`, `h[ae]matopoie\|emopoie\|ematopoie`) |
| Word boundaries | `\bbone\b` not `bone` (otherwise *backbone*); `\bBUN\b` not `BUN` (otherwise *abundance*); `\bALT\b` checked in context (otherwise *salt*, *alternative*) |
| Surfaces read in full for this act | `PMID19936220.md`, `PMID17803050.md` + `PMID17803050.json` (25 page-adjudicated locators), `PMID34747138_locators.md`, `PMID34747138_partial_locators.md`, `PMID25012504.md`, `PMID30755385.md`, `PMID24871327_locators.md`, `PMID42422765_partial_locators.md` (889 lines), `PMID32000863.json` (25 locators), `PMID29724996.json`, `downstream_wwox_independent_rescue_census_20260921.md` §3, `mechanism_intervention_map.md` (peripheral rows), `claim_registry_current.md` CLAIM 004/005/036/037/038/039/040, `therapeutic_strategies_current.md`, `therapeutic_hypotheses_ledger_current.md` |
| External fetches in this act | 🔴 **NONE.** No PubMed, no PMC, no web. Every value below is a **prior-session attestation** carried with its receipt. **No zero in this file is a PubMed count of mine**, and a PubMed count of zero would not be evidence in any case |

🔴 **The hardest bound on this whole audit, stated first.** **`files/fulltext/` does not exist in this
edition.** Every locator below names an artifact by SHA-256 — `PMID34747138_Repudi2021_PMC.xml`,
`EMMM-13-e14599-s001.pdf`, `PMID32000863_Cheng2020_supplementary.pdf` — and **none of those binaries is
on disk here.** So §2's "analysis-only on local material" means *analysis-only in cost class*, not
*a file I can open in this repository*. That difference is load-bearing and is carried into §5.

---

## 1 · THE DENOMINATOR TABLE

### 1.1 · The rows — every arm in which something was given to an animal in a WWOX system

Enumerated from `downstream_wwox_independent_rescue_census_20260921.md` §3 (12 rows, the field-density
limit measured there across five PubMed queries) plus an unscoped sweep of all 80 deepdive manifests and
54 dossiers for administration vocabulary (`i.p.`, `intraperitoneal`, `gavage`, `injected into`,
`administered`, `treated mice`, `ICV`), which returned exactly **six papers** and no seventh.

| # | Arm | Source | Model / allele — **never pooled** | What was given |
|---|---|---|---|---|
| **A1** | AAV9-hSynI-mWwox / -hWWOX | `PMID 34747138` (Repudi 2021) | **`Wwox`-null mouse (Aqeilan)**, ICV **P0**, free-hand | vector |
| **A2** | AAV9-hSynI-WWOX ± WPRE; promoter series; P0–P5 window; LD/HD | `PMID 42422765` (Obeid 2026) | **`Wwox`-null mouse (Aqeilan)**, ICV, stereotaxic | vector |
| **A3** | Ethosuximide `150 mg/kg` i.p. + PTZ | `PMID 32000863` (Cheng 2020) | **NCKU `Wwox`-null mouse**, exon-1 and exon-2/3/4 strains | drug |
| **A4** | LiCl `60 mg/kg` i.p. ×3 + PTZ | `PMID 32000863` | same | drug |
| **A5** | Digoxin i.p., 40 min | `PMID 25012504` (Abu-Remaileh 2014) | **`Wwox`-null mouse (Aqeilan)** | drug |
| **A6** | shHIF1α, transformed-KO-MEF xenograft | `PMID 25012504` | **host mouse is WWOX-replete** — included only so the row is not silently dropped | genetic |
| **A7** | High-fat diet, 7 months | `PMID 29724996` (Abu-Remaileh 2018) | **Alb-Cre `Wwox^hep−/−`** — hepatocyte-specific, NOT a null | diet |
| **A8** | Doxycycline induction + GTT + ITT | `PMID 30755385` (Abu-Remaileh 2019) | **ACTA1-rtTA `Wwox^ΔSKM`**, plus liver and adipocyte cKO — NOT a null | dox, glucose bolus, insulin |

**Deliberately excluded from the animal denominator, and why.** `PMID 34634460` (d-APV, carbenoxolone,
BB-FCF) is **acute neocortical slice** — nothing was given to an animal. `PMID 42397075` (A51) is
**human organoid** — no animal. `PMID 34015398` (toosendanin) raises WWOX and has nothing to raise in a
null. The Zfra / pTyr33 peptide line is given to animals but in **WWOX-replete** systems and by a
mechanism that *consumes* WWOX. All four are real arms; none is an arm in a WWOX-deficient animal.

### 1.2 · The grid — 8 arms × 10 analyte families = **80 cells**

Legend: 🟢 **measured** · ⚪ **EMPTY — measurable, material existed, not measured** ·
⬛ **not reconstructible** · ⚠️ **partial / adjacent, does not fill the cell**

| | **C1** glucose | **C2** HCO₃⁻ / pH / acid-base | **C3** BUN · creatinine · renal | **C4** Ca · PO₄ · bone | **C5** haematology WBC·RBC·plt | **C6** liver enzymes | **C7** electrolytes Na·K·Cl | **C8** body composition | **C9** spleen · thymus | **C10** gonadal / steroidogenic |
|---|---|---|---|---|---|---|---|---|---|---|
| **A1** Repudi 2021 AAV9 | 🟢 **DATO** | ⚪ | ⚪ *(kidney harvested, S2B–C)* | ⚪ 🔴 *bone **asserted**, §4.3* | ⚪ | ⚪ *(liver harvested, S2B–C)* | ⚪ | ⚠️ weight only, `n=4` | ⚪ | 🟢 Leydig S4A + fertility |
| **A2** Obeid 2026 AAV9 | 🟢 **DATO** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ *(liver blotted S6H)* | ⚪ | ⚠️ weight only | ⚪ | 🟢 fertility S4C–D, `n≈3` |
| **A3** ethosuximide | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚠️ *(brain weight only)* | ⚪ | ⚪ |
| **A4** LiCl | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚠️ | ⚪ | ⚪ |
| **A5** digoxin | 🟢 acute, `n=3`, 40 min | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |
| **A6** shHIF1α xenograft | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |
| **A7** HFD, `Wwox^hep−/−` | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | 🟢 **serum ALT ≈2× at 7 mo** | ⚪ | ⚠️ weight only | ⚪ | ⚪ |
| **A8** dox + GTT/ITT, `Wwox^ΔSKM` | 🟢 fasting + GTT | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | 🟢 **fat / lean mass** | ⚪ | ⚪ |

### 1.3 · 🔴 THE COUNT — and the cell that matters is the empty one

| Denominator | Cells | 🟢 filled | ⚪ EMPTY | **empty fraction** |
|---|---:|---:|---:|---:|
| **All 8 animal arms × 10 families** | **80** | **8** | **72** | **90.0 %** |
| The 5 arms in a **WWOX-null animal** (A1–A5) | 50 | 5 | 45 | **90.0 %** |
| The **two gene-therapy arms** (A1, A2) | 20 | 4 | 16 | **80.0 %** |
| 🔴 **The six NON-glucose, NON-gonadal families** (C2, C3, C4, C5, C7, C9) **across all 8 arms** | **48** | **0** | **48** | **100 %** |

> 🔴 **That last row is the finding, and it is exact.** **Acid-base, renal function, calcium/phosphate/bone,
> haematology, electrolytes, spleen and thymus have been measured in ZERO of 48 opportunities — in every
> arm in which anything has ever been given to an animal in a WWOX system, across 17 years, four
> laboratories, two species, four drug classes, one diet and two gene-therapy papers.** Not thinly
> measured. Not measured with a small `n`. **Zero.**

**Reproduced independently of Scientist F's count, bilingually and unscoped.** Across the **7** `tx007_*`
analysis files, `acidos|bicarbonat|creatinin|hypocalc|ipocalcem|leukop|leucopen|h[ae]matopoie|emopoie|
milza|splen|thym|timic|osteo|bone volume|mineralis|platelet|piastrin|\bBUN\b` returns **0 files each**.
Across `mechanism_intervention_map.md` (R-01…R-09, N-01…N-16, E-1…E-10) the peripheral vocabulary
appears **twice**, and both times as something other than a target: once as the **design confounder**
(§ line 146, *"hypoglycaemic, acidotic, uraemic, hypocalcaemic, leukopenic, anaemic"*), once as a
**safety liability** (`KNOWN_MAJOR_SAFETY_CONSTRAINTS`: *"intestinal-crypt turnover and bone toxicity"*).

### 1.4 · ⚠️ A correction to Scientist F's portfolio count — right conclusion, wrong number

`wwox_independent_downstream_rescue_20260922.md` §2.3 reports **two** peripheral hits in the portfolio:
the `TX-004` bone-toxicity liability and the word *backbone*. **The conclusion survives intact; the
count does not.** That sweep was **English-only and without word boundaries** in a corpus whose
registries and hypotheses ledger are written in **Italian**. A bilingual sweep returns:

| File · line | Hit | What it actually is |
|---|---|---|
| `therapeutic_strategies_current.md:76` | *"Wnt inhibitors: intestinal/**bone** toxicity"* | **liability of a CNS lever** — as F reported |
| `therapeutic_hypotheses_ledger_current.md:90` | *"beneficio ipotizzato via **milza**"* (spleen) | inside `HYP-20260705-05`, the **rejected** Zfra entry — evidence *against* |
| `…ledger:185 · 187 · 189` | ***ipoglicemia*** ×3 | `HYP-20260709-01` (ketogenic diet): once as PRO rationale, once as the CONTRA contradiction, once as the primary-data upgrade |
| `…ledger:190` | ***acidosi*** | a **monitoring toxicity** of the ketogenic diet, not a target |

⇒ **Six hits, not two. And the conclusion is unchanged and now better founded:** the portfolio contains
entries keyed to the **glucose** limb (`HYP-20260709-01` ketogenic, `HYP-20260709-05` DCA, digoxin as the
HIF1α probe) and **not one entry**, in either language, keyed to bicarbonate, BUN/creatinine, calcium,
haematology, spleen, thymus, liver enzymes, electrolytes or body composition. Where the non-glucose
periphery appears at all, it appears as a **liability** or as a **confounder** — never as a target.

🔴 **ELEVENTH failure mode, added to this corpus's catalogue** (the tenth was added this morning):

> **A monolingual term sweep under-counts in a bilingual corpus.** This repository reasons in English in
> `analysis/` and in **Italian** in `claim_registry_current.md`, `working_model_current.md` and
> `therapeutic_hypotheses_ledger_current.md` — i.e. exactly in the canonical files an absence claim is
> most likely to be made *about*. `hypoglycemia` returns nothing where `ipoglicemia` returns three.
> **Standing rule proposed: a repository absence claim must state its LANGUAGE scope as well as its
> file-type scope, or be run in both languages.**

⚠️ **And I tripped a twelfth on myself, recorded rather than hidden.** My own first sweep for
`alkaline phosphatase` returned **0 files repo-wide** while **ALP is present**, in the rat's Table 2.
That is failure mode (8) — a quoted phrase not matching its own abbreviation — committed by the actor
writing the failure-mode section. The number was wrong for four minutes; it is corrected in §1.5.

### 1.5 · The untreated baselines — the "measurable" column, and what defines it

An empty cell in §1.2 is only a *finding* if the measurement was **possible on material that existed**.
These three rows establish that it was: each analyte below has been measured **in a WWOX animal, by
somebody, at an age overlapping the intervention windows**.

| Analyte family | `Wwox^ΔCre/ΔCre` **EIIA-Cre mouse, P18** (`PMID 19936220`, `CLAIM 036`) | rat **`lde/lde`, 28 d** (`PMID 17803050`, `CLAIM 038`) | other |
|---|---|---|---|
| **C1** glucose | 🟢 **143.5 vs 250.6 mg/dL**, `p=0.000131` | 🟢 GLU **not significant**, both sexes | 🟢 `Wwox^ΔSKM` fasting hyperglycaemia + impaired GTT |
| **C2** acid-base | 🟢 **Total CO₂ 14.50±3.5 vs 21.67 mEq/L**, `p=0.006227`. ⚠️ KO SEM is 10× the WT one | ⬛ **never measured** | — |
| **C3** renal | 🟢 **BUN 37.25 vs 17.67 mg/dL**, `p=0.01086`; ⚪ **creatinine never measured** | 🟢 **BUN ×3.2 ♀ / ×3.5 ♂**; **CRE 0.48→0.64 ♀, 0.45→0.58 ♂**, both `P<0.01`; kidneys **histologically normal**, no proteinuria | — |
| **C4** Ca · PO₄ · bone | 🟢 **Ca 10.18 vs 11.13 mg/dL**, `p=0.000385`; 🟢 **BV/TV 13.35→5.8 %**, Md.V/TV 13.3→5.7 %, microCT + Von Kossa, `KO n=3` vs **pooled WT+HET n=5**; ⚪ phosphate never measured | 🟢 Ca **ns**; 🟢 **inorganic phosphate significant in ♀ only** (`n=4` normal, `5` mutant per sex); ⬛ bone never imaged | 🔴 osteosarcoma **contested within mouse**: 0/9 here, 4/13 in `PMID 17360458`, **86 % (19/22, Fig. S1 legend) asserted as 100 %** in `PMID 20530675` |
| **C5** haematology | 🟢 **WBC 4.2 vs 9.45 ×10³/µL** — `n=2` per genotype, 🔴 **no test run**; 🟢 3 % nucleated RBC in **1 of 2** KO examined; ⚪ **RBC, Hb, platelets never counted** | ⚪ "no anaemia" asserted in Discussion, no CBC printed | 🔴 **`platelet\|piastrin\|thrombocy` returns 0 files across the ENTIRE repository, unscoped, all file types.** Platelets have never been counted in any WWOX animal, ever |
| **C6** liver enzymes | ⬛ never measured | 🟢 **GPT, GOT, ALP, CPK** all in Table 2 — 🔴 **carrying sample-size footnotes, not significance footnotes**; ♀ CPK ~8.5× higher **with no marker**, *"non importabile in nessuna direzione"* | 🟢 serum **ALT ≈2×** in `Wwox^hep−/−` under HFD (A7) |
| **C7** electrolytes | ⬛ never measured | 🟢 **Na⁺, K⁺, Cl⁻ all comparable** | — |
| **C8** body composition | ⬛ never measured (⚠️ body weight yes: 4.2 g vs 6.82/7.07 at P14, **growth arrest from day 10**) | ⬛ never measured (⚠️ ~56 % of normal weight at 21 d) | 🟢 fat ↑ / lean ↓ in `Wwox^ΔSKM` |
| **C9** spleen · thymus | 🟢 **spleen 0.21 % vs 0.53 % body weight**, `p=0.0015`, red-pulp hypocellularity; 🟢 **thinned thymic cortex** (Fig. 4, read as image) | ⬛ never measured | — |
| **C10** gonadal | 🟢 Leydig cells absent (`Aqeilan 2009`, cited by Repudi — ⚠️ **a citation in this repository, not a first-hand read**) | 🟢 **testis relative weight 288.1 → 159.4**; apoptotic germ cells, no spermatocytes, **immature spindle-shaped Leydig cells** | — |
| lipids *(outside the brief's ten)* | 🟢 HDL-C markedly ↓, ApoA-I −80 % in the whole-body null (`PMID 24871327`) | 🟢 TG comparable | 🟢 `Wwox^ΔSKM`: HDL/LDL ↓, TG + cholesterol ↑ |

**So every one of the ten families has been measured in a WWOX animal by somebody.** The empty cells of
§1.2 are not empty because the measurement is impossible. They are empty because **nobody ran the panel
on a treated animal.**

### 1.6 · The three classes of empty cell, kept separate

🔴 **A denominator audit is worthless if "not measured", "not reported" and "not readable here" are
merged.** They license opposite next moves.

| Class | Meaning | Cells |
|---|---|---|
| ⚪ **EMPTY — never measured** | The analyte was not assayed in that arm. Next move: **measure it** | 72 of 80, subject to the read-depth bound below |
| ⬛ **NOT RECONSTRUCTIBLE** | The measurement cannot be recovered from any surviving material at any cost short of new animals. Bicarbonate/pH is the type case: **total CO₂ is destroyed by sample handling and cannot be recovered from banked frozen serum**; a CBC needs fresh anticoagulated whole blood; body composition needs a live animal | C2 and C5 in every arm; C7 on any thawed sample |
| 🟡 **NOT ESTABLISHED FROM THIS REPOSITORY'S READ DEPTH** | The arm's paper may report it; LEGEND has not read the section. **This is not an absence and must never be counted as one** | See below |

🔴 **The read-depth bound, stated so no cell in §1.2 is over-read:**

| Arm | Read depth | Can "⚪ not measured" be asserted? |
|---|---|---|
| **A3 / A4** `PMID 32000863` | **`complete_fulltext_read`** — all 7 main figures **and all 9 supplementary figures** inspected, Methods read, 25 locators, 22 audited character-for-character against the local XML | 🟢 **YES, at high confidence.** Zero occurrences of glucose, serum, plasma, blood chemistry, spleen, liver, bone across all 25 locators |
| **A1** `PMID 34747138` | **`complete_fulltext_read`** 2026-08-10 — discussion, methods, all six figures, references (62, all 36 gene-directed already known). ⚠️ **Appendix S1 figures read as captions, never opened as images**; Review Process File **refused** (`U+0000`) | 🟡 **Mostly** — but any peripheral endpoint hiding in Appendix Figs S1–S6 is **unexcluded** |
| **A2** `PMID 42422765` | 🔴 **`partial`** — *"Introduction, all seven results sections and Materials and Methods: not read."* All 7 main figures inspected; S8 recovered; **S5, S6 and the rest of the supplementary unreachable, five retrieval routes failed** | 🔴 **NO.** A2's ⚪ cells are **`NOT ESTABLISHED`**, not absences, and are marked ⚪ in §1.2 only because no evidence of measurement exists — the count in §1.3 is an **upper bound on emptiness for this row** |
| **A5** `PMID 25012504` | dossier-level, 98 lines, structured | 🟡 the digoxin arm is described as *"a single acute digoxin experiment (`n=3/group`, 40 minutes)"* — a single-analyte design |
| **A7 / A8** | `complete_fulltext_read` (A8: all sections, 8/8 supplementary pages, 54/54 references) | 🟢 YES |

⇒ **Of the 72 empty cells, 62 rest on a complete or near-complete read and 10 (row A2) rest on a
declared partial.** The 100 % figure for the six non-glucose families survives this correction: even
discarding row A2 entirely, it is **0 of 42**.

---

## 2 · OBTAINABILITY AND COST — for every empty cell, what would fill it

**Ranking rule, fixed before the ranking: prefer `NEW ANALYSIS ONLY`, then existing material, then new
animals — and within each tier, prefer the move that fills the most cells.**

### Tier 0 — `NEW ANALYSIS ONLY`. No material, no animal, no purchase.

| # | Move | Cells it could fill | Cost | 🔴 What blocks it here |
|---|---|---|---|---|
| **T0-a** | 🥇 **Re-extract `PMID 19936220` Table 3 in full.** LEGEND's dossier carries **four rows** — glucose, Total CO₂, BUN, calcium. A veterinary chemistry analyser returns a **panel**, typically 10–14 analytes. If Table 3 prints phosphorus, Na⁺, K⁺, Cl⁻, albumin, ALP or creatinine and LEGEND extracted four of them, **those cells are already filled and nobody noticed** | C3 (creatinine), C4 (phosphate), C7 (Na/K/Cl), C6 — in the **baseline**, which re-anchors the whole comparison | **zero** | 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — *"an analyser returns a panel"*. It is **exactly the kind of obvious premise this framework exists to tag**. The table may genuinely have four rows. **The premise is the reason to look, never a substitute for looking.** Surface is PLOS ONE, open access; **not on disk in this edition** |
| **T0-b** | 🥈 **Open `PMID 34747138` Appendix S1 (`EMMM-13-e14599-s001.pdf`, 11 pp, sentinel **PASS**) at panel level.** S2B–C = peripheral-tissue westerns (liver, pancreas, kidney, testis, ovary, P17 and 9 months); S3 = hindlimb clasping; S4A = Leydig | Converts A1·C10 from running-text `INFERENZA` to panel `DATO` or refutes it; **establishes whether a bone panel exists in this paper at all** (§4.3) | **zero** | CC BY 4.0, in the OA package. **Not on disk here.** The receipt itself flags these three panels as the unopened basis of the strongest finding in that reading |
| **T0-c** | **Re-attempt `PMID 42422765` supplementary S5/S6** by the route that recovered S8 | A2·C6 (whether any liver *function* readout exists beside the S6H WWOX blot); A2 read depth | **zero** | Five routes already failed; S8 fell to a sixth. **Not a guaranteed win** |
| **T0-d** | **`PMID 17803050` Table 2 full row set.** The only ALP/CPK/GPT/GOT/electrolyte panel in any WWOX rodent. Already **page-adjudicated** — crops exist with `image_sha256` + `source_pdf_sha256` | C6, C7, C4 in the **rat** baseline | **zero** | 🔴 Paper has **no DOI and no PMCID** and `CLAIM 039` records it as **not obtainable in this environment**. The adjudicated crops are the only surface, and they cover BUN/CRE/GLU rows — **not** the enzyme rows |
| **T0-e** | **Page-adjudicate `EMMM-13-e14599-s002.pdf`** (Review Process File). Three peer reviews + point-by-point response. Reviewers asked for what the authors did not show | Nothing directly; but a reviewer request for a peripheral endpoint would be **first-hand evidence that the field considered and declined it** | low | Surface is **refused** (`U+0000` at offset 63 867) — quotable only through adjudication, which is the correct route and not the cheap one |

### Tier 1 — EXISTING MATERIAL. Banked tissue, no new animal.

| # | Move | Cells | 🔴 Honest status of the material |
|---|---|---|---|
| **T1-a** | **μCT of archived hindlimbs from any treated cohort.** microCT on fixed bone is **retrospective and non-destructive** | **C4 (bone) in A1 and A2** — the one peripheral system the brief says was rescued and that has no anchor | 🟡 **This route is already named in this repository for a different question**: `CLAIM 036`'s `BATCH_20260909_001` qualification opens `REVIVAL_TRIGGER` *"μCT re-imaging of archived limbs from either negative cohort"*. **The transfer is exact.** Whether treated limbs were fixed and kept is **unknown and unknowable from here** |
| **T1-b** | **Histology on the peripheral tissues Repudi 2021 demonstrably harvested** — liver, pancreas, **kidney**, testis, ovary, at P17 **and 9 months**, from treated and control animals (they were blotted for S2B–C) | C3 (renal histology), C6 (liver histology), C10 (steroidogenic-enzyme IHC) | 🟢 **These tissues provably existed**, in treated animals, at two ages. Lysates may be gone; FFPE blocks outlive everyone |
| **T1-c** | **Obeid 2026 banked tissue** — liver (S6H), sciatic nerve, spinal cord, four brain regions, at P30, **P240 and P300** | C6; long-term safety | 🟡 The programme is **sponsored** (*"supported by Mahzi Therapeutics"*, three sponsor-employed authors). A sponsored programme plausibly banks serum for safety. **Plausibly is not evidence** |
| **T1-d** | **Serum chemistry on any banked serum** | C3 (BUN, creatinine), C4 (Ca, PO₄), C6 | 🟡 Stable on frozen serum. 🔴 **C2 is NOT** — see T2-a |

### Tier 2 — NEW ANIMALS. The irreducible floor.

| # | Move | Cells | Why nothing cheaper works |
|---|---|---|---|
| **T2-a** | 🔴 **Blood gas / total CO₂ on fresh blood** | **C2** | **Bicarbonate cannot be recovered from banked material at any price.** It is destroyed by handling and time. **C2 is `NOT RECONSTRUCTIBLE` in all 8 arms — 8 cells that no analysis can ever fill.** And C2 is the analyte the field's own death hypothesis (renal tubular acidosis) turns on |
| **T2-b** | 🔴 **CBC with platelet count on fresh EDTA whole blood** | **C5** | Same class. **Platelets have never been counted in any WWOX animal in the entire literature this repository holds — 0 files, unscoped.** Not recoverable retrospectively |
| **T2-c** | **EchoMRI / DEXA body composition** | **C8** | Requires a live animal |
| **T2-d** | ⭐ **One extra tube at terminal bleed in any rescue cohort already being generated** | C2 + C3 + C4 + C5 + C7 **simultaneously** | **Zero extra animals** if attached to a cohort already running. This is the only move that fills the `NOT RECONSTRUCTIBLE` cells without adding a single animal to the world |

### 2.1 · The ranking

> **T0-a → T0-b → T1-a → T1-b → T2-d.** The first two cost nothing and fix the **denominator and the
> provenance**; T1-a and T1-b fix **bone and kidney** if the material survived; **T2-d is the only route
> to C2/C5/C7 and it is free if and only if someone else's cohort is already being terminated.**
>
> 🔴 **And the honest headline of §2: 8 of the 72 empty cells (C2, every arm) can never be filled by any
> analysis, and a further 8 (C5) cannot either. Sixteen cells are already permanently gone.** Every animal
> that could have answered them is long dead. That is what a denominator audit is for — an empty cell
> that is *recoverable* is a task, and an empty cell that is *gone* is a loss, and only counting
> distinguishes them.

---

## 3 · THE CROSS-MODEL BOUND — and it is the hard part

### 3.1 · The rule this section enforces on itself

🔴 **An analyte is adjudicable as model-invariant or model-specific only if it was MEASURED IN BOTH
MODELS.** Measured in one and absent from the other is **UNDETERMINED** — it is a statement about who
ran an assay, not about biology. Pooling the two is how *"WWOX loss causes a metabolic crisis"* became a
sentence nobody can source to a single animal.

### 3.2 · 🔴 A cross-model hazard nobody in this repository has flagged, and it is in the units

| Model | BUN as printed | Glucose as printed |
|---|---|---|
| mouse `Wwox^ΔCre/ΔCre` P18 | 17.67 → **37.25 mg/dL** | 250.6 → **143.5 mg/dL** |
| rat `lde/lde` 28 d | 12.6 → **40.3 mg/ml** ♀ | **169.0 mg/ml** ♀ normal |

> 🔴 **The two papers print different units, and the rat's are almost certainly misprinted.** 169 mg/**ml**
> of glucose is 16 900 mg/dL, which is not a number any animal survives. `CLAIM 038` reproduces
> `mg/ml` verbatim — correctly, it is quoting — and then compares the values directly with the mouse's
> `mg/dL`. **Nothing downstream flags it.**
>
> ⇒ **No numeric cross-model comparison is licensed in this audit. Only DIRECTION and SIGNIFICANCE.**
> Every statement in §3.3 is therefore about sign and test, never about magnitude.
>
> This is not a new class for the repository — `superior_node_search_20260922.md` `G-5` flags
> *"0.2 mg/l"* tubulin as ~5 000× below workable, and `CC-20260922-TAU-DIRECTION-01` flags an
> `mg/ml` scale the same way. **The class was known; it was never pointed at CLAIM 038.**

⚠️ **Extraction damage visible in the very locators this section rests on, recorded per rule 5d:**
`"(P  0.05)"` — the comparator **deleted**, leaving a double space, exactly the `P 5 0.05` class;
`"(Ca2, Na, K, and Cl–)"` — the superscript **²⁺ deleted**; `"12.6 q 4.3"` — `±` rendered as `q`.
🟢 All three sit on **page-adjudicated** locators with `crop_pdf_points`, `dpi`, `image_sha256` and
`source_pdf_sha256`, so the rendered page is the reference surface and the damage is bounded.
**E-notation is the only exponent-safe form and none of these values needs one.**

### 3.3 · The model-by-model comparison — only where both measured

| Analyte | mouse `Wwox^ΔCre/ΔCre` P18 (EIIA-Cre) | rat `lde/lde` 28 d | **Verdict** |
|---|---|---|---|
| **BUN** | 🔺 significant, `p=0.01086` | 🔺 significant, `P<0.05` ♀ / `P<0.01` ♂ | 🟢 **MODEL-INVARIANT — the only chemistry analyte elevated in both species** |
| **Gonadal / Leydig** | 🔺 Leydig cells absent | 🔺 testis relative weight ~55 % of normal, immature Leydig | 🟢 **MODEL-INVARIANT** ⚠️ the mouse limb is a **citation** (`Aqeilan 2009`), not a first-hand read here |
| **Growth failure / body weight** | 🔻 growth **arrest** from day 10 | 🔻 ~56 % of normal at 21 d | 🟢 **MODEL-INVARIANT** — and it is the denominator of every "relative" measure in both papers |
| **Glucose** | 🔻 `p=0.000131` | ⚪ **not significant, both sexes** | 🔴 **MODEL-SPECIFIC — discordant** |
| **Calcium** | 🔻 `p=0.000385` ⚠️ but the effect is **−8.5 %**: statistically strong, biologically small | ⚪ **not significant** | 🔴 **MODEL-SPECIFIC — discordant** |

**Adjudicable: 4 of the brief's 10 families** (C1, C3, C4-calcium, C10). **Six are undetermined** — and
undetermined **because of a missing assay, not because of a disagreement**:

| Undetermined | Measured only in | Missing in |
|---|---|---|
| **acid-base (C2)** | mouse | rat — **never measured** |
| **creatinine (C3b)** | rat | mouse — **never measured** |
| **electrolytes (C7)** | rat (all ns) | mouse |
| **phosphate (C4b)** | rat (♀ only) | mouse |
| **haematology, spleen, thymus (C5, C9)** | mouse (WBC `n=2`, **untested**) | rat |
| **bone (C4c)** | mouse (`KO n=3` vs **pooled** WT+HET `n=5`) | rat — **never imaged** |
| **liver enzymes (C6)** | rat (**unmarked**) | mouse null |

### 3.4 · What this does to the "peripheral phenotype"

> 🔴 **"The peripheral phenotype of WWOX loss" is not one object, and the audit shows it is not even one
> object's worth of measurement.** What is invariant across the two species is **uraemia, gonadal failure
> and growth arrest**. What is *demonstrably* model-specific is **hypoglycaemia and hypocalcaemia**. And
> what the field's own death hypothesis rests on — **metabolic acidosis — has been measured in exactly
> one model, once, in three animals, with an SEM ten times the wild type's.**

Three consequences, each with its premise tagged:

1. **Hypoglycaemia is species-specific, not strain-specific.** Two **independently derived** mouse nulls
   are hypoglycaemic — the Aldaz EIIA-Cre (`p=0.000131`) and the Aqeilan null (Repudi: *"hypoglycemic
   from the second week until they succumbed"*) — and the rat is not. ⚠️ **The NCKU nulls have never had
   glucose measured at all.** `PREMISE: DATO` on the two mouse nulls; `PREMISE: NOBODY_LOOKED` on NCKU.
2. **The uraemia is the invariant, and it has two competing untested explanations that survive the
   invariance.** `CLAIM 038` holds both: renal insufficiency (against: kidneys histologically normal, no
   proteinuria) **or** seizure-driven hypercatabolism and muscle disruption, with a named precedent in
   the SER rat. 🔴 **Invariance across species does not choose between them** — it is equally compatible
   with a conserved renal role and with *both animals convulsing and wasting*. `PREMISE: IPOTESI` ×2.
3. 🔴 **The acidosis cannot be called mechanistic and cannot be called background.** It is the only limb
   of the death hypothesis that no second model has ever tested. Calling it "likely mechanistic" because
   it is severe would be exactly the inference `CLAIM 036`'s own `REVIVAL_TRIGGER` warns against, since
   **brain WWOX ablation was never shown in the very model the acidosis comes from.**

### 3.5 · 🔴 And the driver is not the allele

`CLAIM 036` (EIIA-Cre) and `CLAIM 005` (BK5-Cre) **share the floxed allele and differ in the Cre**.
The peripheral chemistry belongs to **EIIA-Cre**; the hippocampal gliosis belongs to **BK5-Cre**; the
gene-therapy arms are in the **Aqeilan** null; the ethosuximide/lithium arms are in the **NCKU** nulls;
the E/I bursting is **Synapsin-Cre**. 🔴 **No two of these five are the same animal, and the audit's
empty cells are therefore empty in five different animals, not in one.** That is the strongest single
argument for the §5 experiment being a *measurement inside one arm* rather than a cross-paper synthesis.

---

## 4 · THE CNS-REVERSIBILITY QUESTION, STATED PRECISELY

### 4.1 · What a brain-restricted vector demonstrably does to the periphery

Repudi 2021 establishes the design that makes the question askable at all:

> `L3` — *"we also tested expression of the transgene in peripheral tissues, including liver, pancreas,
> kidney, testis, and ovary… no WWOX expression was detected in `Wwox`-null tissues in P17 and
> 9-month-old rescued mice."*

⇒ **The vector is not in the periphery.** Anything that changes there changes **through the brain**.

### 4.2 · The three peripheral systems said to respond — and they are at three different evidence grades

| System | Evidence | Grade | Bound |
|---|---|---|---|
| **Blood glucose** | `L4` verbatim: *"`Wwox`-null and AAV9-hSynI-EGFP-injected mice were hypoglycemic from the second week until they succumbed… while AAV9-hSynI-mWwox- or AAV9-hSynI-hWWOX-injected mice had **normal blood glucose levels** when compared to the wild-type mice"* — **and independently reproduced in A2** with arm-separating statistics at P20 (`*` WT-vs-LD, `**` LD-vs-HD, **`ns` WT-vs-HD**) and at P14 across all five P1–P5 treatment days (`ns` vs WT) | 🟢 **`DATO`** — two papers, two doses, panel-level | Measured at P14/P20 only; no adult value |
| **Leydig cells / fertility** | `L4` verbatim: *"found **intact Leydig cells** in P17 AAV9-hSynI-WWOX-treated mice (Appendix Fig S4A)"*; *"both males and females were fertile"*. A2 adds fertility at S4C–D | 🟡 **`INFERENZA`** — running text; **the panel has never been opened**, and the receipt says so. A2's fertility panel carries **≈3 observations per group and NO untreated-KO comparator** | The 2021 receipt's own `evidence_basis` carries this as `PREMISE: INFERENZA` *pending panel inspection, never as DATO* |
| **Cortical bone** | 🔴 **none** | 🔴 **UNANCHORED** — see §4.3 | — |

### 4.3 · 🔴 The cortical-bone assertion has no verbatim locator anywhere in this repository

The brief states — and Scientist F's file, the cerebellar census and the recursive re-read all repeat —
that Repudi 2021 reports **cortical bone comparable to wild type** in treated animals. **I looked for the
sentence. It is not there.** An unscoped grep for `bone` across every surface this repository holds for
`PMID 34747138` returns **four hits, and all four are LEGEND's own prose**:

| Where | Text |
|---|---|
| `PMID34747138_partial_locators.md:81` | *"…and gives cortical bone comparable to wild-type"* — in the **interpretive paragraph under L4**, not in the quoted block |
| `PMID34747138_locators.md:205` | *"rescues peripheral phenotypes — glucose, fertility, bone —"* — LEGEND's synthesis |
| `PMID34747138.json:213` | the same sentence inside a locator's `proposition` field, tagged **`INFERENZA, not DATO`** |
| `recursive_reread_repudi2021_20260922.md:171` · `cerebellar_functional_readout_census_20260922.md:249` | two further paraphrases, both marked `NO NEW INFORMATION` |

🔴 **`L4`'s quoted block covers Leydig cells and fertility. It does not mention bone.** So a third
peripheral system entered this repository's working vocabulary through a **paraphrase in an interpretive
paragraph**, was repeated four times, and reached an Operator brief as an established report — **without
one quoted sentence and without one inspected panel behind it.**

This is not a claim that the finding is false. Repudi 2021 may well report it; I cannot see the paper.
It is a claim about **provenance**: `COULD NOT ESTABLISH` `CNE-1`, §7.2. It is also, structurally, the
**same failure the repository has logged twice before** — a running-text statement resting on an
unopened Appendix panel (Wang 2012's caption; `PMID 42397075` Fig. 6's missing brackets) — and the
2026-08-09 receipt for this very paper **predicted it in advance**, naming S2B–C, S3 and S4A as the
unopened basis of its strongest finding.

### 4.4 · 🔴 THE STATEMENT, for the record

> **For blood glucose, CNS-restricted WWOX restoration is established to correct a peripheral phenotype
> — two papers, two doses, arm-separating statistics inside the lethal window.**
>
> **For gonadal/Leydig, it is reported in running text and never verified at panel level.**
>
> **For cortical bone, it is asserted in this repository with no quoted source.**
>
> 🔴 **For metabolic acidosis, renal function, calcium, phosphate, haematology, spleen, thymus,
> electrolytes, liver enzymes and body composition — the direction is UNKNOWN IN BOTH DIRECTIONS.
> Nobody has shown they are CNS-reversible. Nobody has shown they are not. They have never been
> measured in a treated animal: 0 of 48 cells.**
>
> **And the two readings this leaves open are the ones the `DISCOVERY_TRACE` named, unchanged and still
> cheap to separate:** either neuronal WWOX restoration **corrects** them — which would make the entire
> systemic collapse a brain phenotype, turn `CLAIM 036`'s confounder into a **mediator**, and re-read a
> decade of systemic-null neuropathology — or it **rescues survival despite them**, which would mean
> those derangements were never the lethal limb and would narrow the field's own *"succumb to metabolic
> defects"* framing. 🔴 **Nothing in this repository favours either.**

### 4.5 · What would settle it, and at what cost

| To settle | Minimum sufficient measurement | Cost class | 🔴 Bound |
|---|---|---|---|
| **Gonadal (C10)** | Open Appendix S4A at measured ppi | `NEW ANALYSIS ONLY` | Converts `INFERENZA`→`DATO` or refutes. **Cannot** tell whether steroidogenesis is restored — Leydig *presence* is not Leydig *function*; testosterone has never been assayed in any WWOX animal |
| **Bone (C4c)** | Open Appendix S1 for a bone panel; if none, μCT of archived treated limbs | `NEW ANALYSIS ONLY` → existing material | Retrospective μCT gives BV/TV and cortical thickness. **Cannot** give the mineralisation-*rate* measure (Md.V/TV needs in vivo labelling) that was the EIIA-Cre paper's actual conclusion |
| **Renal (C3)** | BUN + creatinine on banked serum from treated vs untreated | existing material | 🔴 **Cannot discriminate `CLAIM 038`'s two explanations.** That needs **creatine kinase and muscle mass in parallel**, which the authors themselves named, together with why they did not do it |
| **Acid-base (C2)** | Blood gas on fresh blood at P14–P18 | 🔴 **NEW ANIMALS — irreducible** | Free only if attached to a cohort already being terminated (T2-d). **No analysis, at any price, recovers it from the past** |
| **Haematology (C5)** | CBC with platelets on fresh EDTA blood | 🔴 **NEW ANIMALS** | Same |
| **The whole question at once** | One clinical-chemistry + CBC panel on terminal blood, treated vs untreated, same cohort, same day | one extra tube per animal | This is `DISCOVERY_TRACE` §7.5 and Scientist F §4's step 2. **This audit's contribution is that it is now a justified request rather than a speculative one** |

---

## 5 · THE ONE COMPRESSED EXPERIMENT

> ## 🥇 **The existing-panel denominator recovery**
>
> **One act, three local-class surfaces, no material, no animal, no purchase, no external contact.**
>
> 1. **`PMID 19936220` Table 3, re-extracted row by row** as an image at measured ppi — not as text, and
>    not trusting LEGEND's four-row transcription. **Question: how many analytes does that table
>    actually print?**
> 2. **`PMID 34747138` Appendix S1, Figures S2B–C, S3 and S4A**, opened as images at measured effective
>    ppi (the route matters: for this paper the **article PDF** holds the figures at 186–202 ppi against
>    the OA bundle's 93–102). **Question: does a bone panel exist, and does S4A show what the running
>    text says?**
> 3. **`PMID 17803050` Table 2 enzyme rows**, if and only if the existing page-adjudication crops can be
>    extended — the BUN/CRE/GLU crop exists at `dpi 500`; the ALP/GPT/GOT rows sit in the same table.
>
> **Cost class: `NEW ANALYSIS ONLY`.** Zero animals. Zero spend. Two of the three surfaces are open
> access (PLOS ONE; EMBO Mol Med CC BY 4.0); the third is already adjudicated in this repository.
>
> ### Why this and not the blood panel
>
> The clinical-chemistry panel on treated animals is the **better experiment** and it is already named,
> twice, by two prior actors. 🔴 **Re-proposing it would be this file claiming someone else's
> experiment.** What no one has done is the thing that makes it *fundable*: establish that the cells are
> empty **in the papers**, not merely empty in LEGEND. T0-a is the only move that can tell those two
> apart, and it is the discriminator I fixed in §6 before running anything.
>
> ### What it decides
>
> | Outcome | Consequence |
> |---|---|
> | Table 3 prints **four** rows | 🔴 The absence is the **field's**, the denominator stands at 0/48, and the blood panel becomes a justified request backed by a measured denominator rather than an impression |
> | Table 3 prints **ten to fourteen** rows | 🟢 **The better outcome, and it costs nothing to discover.** Creatinine, phosphate, electrolytes and possibly ALP **already exist unextracted** in the baseline; three to five cells in §1.5 move from ⚪ to 🟢 at zero cost; and LEGEND has a **reading defect** to log, not the field |
> | Appendix S1 contains a **bone panel** | `CNE-1` closes; the brief's third peripheral system gets an anchor |
> | Appendix S1 contains **no bone panel** | 🔴 A four-times-repeated assertion in this repository has **no source**, and every downstream file carrying it needs the qualification |
> | S4A shows intact Leydig cells | A1·C10 → `DATO` |
> | S4A shows something else, or no panel | The repository's **strongest** peripheral-rescue finding after glucose is **withdrawn** |
>
> ### 🔴 What it cannot settle — stated so the result cannot be over-read
>
> 1. **It cannot tell whether ANY non-glucose peripheral component is CNS-reversible.** No treated animal
>    has ever had one measured; no re-reading of any paper can create a measurement that was not made.
>    **That question is `T2-d`-bound and nothing cheaper touches it.**
> 2. **It cannot recover bicarbonate or platelets — ever, in any arm.** Those 16 cells are permanently
>    gone (§2, Tier 2).
> 3. **It cannot resolve `CLAIM 038`'s renal-versus-hypercatabolism fork.** That needs CK and muscle mass
>    measured in parallel, in the same animals, and the authors said so in 2007.
> 4. **It cannot cross models.** Filling the EIIA-Cre baseline does not fill the Aqeilan-null treated
>    arms. `MECHANISM_TRANSFER_FIREWALL` applies to every row of §1.2 and is why §1.2 has eight rows.
> 5. 🔴 **It is blocked in this environment.** `files/fulltext/` does not exist in this edition; all
>    three surfaces must be re-acquired first. **The cost class is `NEW ANALYSIS ONLY`; the prerequisite
>    is a retrieval, and I am recording that rather than describing a read I cannot perform.**

---

## 6 · THE PROSPECTIVE TRACE, WITH SCORES

> 🔴 **§§ OBSERVATION → DISCRIMINATOR were written to disk and persisted BEFORE the confirmatory searches
> P1–P3 were run.** The baseline enumeration (§0) preceded the trace, as the brief requires, and three
> things it turned up are listed in the trace **as already-known, explicitly not as predictions** — the
> unanchored bone sentence, the bilingual undercount, and the rat's liver enzymes. **Nothing below was
> predicted after the fact, and the two places where I got it wrong are graded against me.**

### OBSERVATION
Two neuron-restricted AAV arms rescue survival in an animal whose recorded cause-of-death framing is
multi-system and peripheral. The rescue papers score neurological endpoints plus blood glucose. The
peripheral chemistry that names the death lives in a **different mouse** (EIIA-Cre, P18) and a
**different species** (rat `lde/lde`), and the two disagree on glucose.

### DIVERGE — five readings of why the peripheral cells are empty
| | reading | distinct because |
|---|---|---|
| **D1** | `NOBODY_LOOKED` — never measured in any treated animal | makes the absence the **field's** |
| **D2** | `MEASURED_NOT_REPORTED` — an analyser returns a panel; the paper printed a subset | makes it a **reporting** gap |
| **D3** | `EXTRACTION_GAP` — reported in the paper, never extracted by LEGEND | makes it **LEGEND's** defect |
| **D4** | `NOT_OBTAINABLE_BY_CONSTRUCTION` — a moribund P18 pup yields microlitres | makes it a **physics** limit, not neglect |
| **D5** | `WRONG_DOCUMENT_CLASS` (failure mode 10) — the endpoints live in supplements and sponsor safety packages, not the main text LEGEND read | makes it a **search-surface** artefact |

### CONNECT
Regulatory safety pharmacology (supplies the *expectation* that a panel exists, and nothing more) ·
clinical-chemistry pre-analytics (supplies the hard `NOT RECONSTRUCTIBLE` boundary for bicarbonate) ·
neonatal-rodent micro-sampling (supplies D4's falsifier) · bone densitometry (supplies T1-a: μCT on
fixed archived limbs is retrospective and non-destructive).

### HYPOTHESIS
**H-G1:** the empty cells are dominated by **D1**, not D3 — a real field-level absence, not a LEGEND
reading defect. · **H-G2:** exactly one analyte family (glucose) is filled in more than one animal arm. ·
**H-G3:** at least one peripheral analyte **is** already measured in an animal intervention arm and has
never been surfaced in any therapeutic analysis in this repository.

### PREDICTION → RESULT → GRADE

| # | Prediction, written before the search | Result | Grade |
|---|---|---|---|
| **P1** | In an 8-arm × 10-family grid (80 cells), the empty fraction **exceeds 80 %** | 🟢 **90.0 %** (72/80). And the sharper cut nobody had: **0 of 48** for the six non-glucose, non-gonadal families | 🟢 **A — supported, and the sub-count is the real finding** |
| **P2** | Glucose is the only family filled in **≥3** arms; **every other family in at most 1** | 🟡 **SPLIT.** Main clause 🟢 — glucose 4 arms, nothing else ≥3. Sub-clause 🔴 **REFUTED** — **gonadal is filled in 2** (A1 Leydig+fertility, A2 fertility). I had not counted A2's supplementary S4C–D | 🟡 **C — half right, and the half I got wrong was the half I had not looked for** |
| **P3** | Serum ALT (A7) appears in **no** therapeutics/portfolio file | 🟢 **SUPPORTED.** Unscoped, whole repo: `serum ALT` returns the `PMID29724996.json` manifest and its derived `pathograph_export.jsonl`. **Zero** hits in `therapeutics/`, in any `TX-*`, any `HYP-*`, `mechanism_intervention_map.md` or any portfolio analysis | 🟢 **A — supported** |
| **P4** | Of analytes measured in **both** models, **BUN alone** is concordant; glucose and calcium discordant | 🟢 **SUPPORTED exactly** | 🟢 **B — supported, but I had most of this from §0 enumeration and say so** |
| **P5** | **≤4 of 10** families were measured in both models and are therefore adjudicable at all | 🟢 **Exactly 4** — glucose, BUN, calcium, gonadal | 🟢 **A — supported at the boundary** |

### 🔴 The branch my DIVERGE did not contain — and it is the one that won a cell

`P3` came back supported, and **the reason it is supported is a mechanism none of D1–D5 describes.**
Serum ALT was measured (not D1), reported (not D2), **and extracted by LEGEND into a locator** (not
D3) — and then **never routed to any file that scores an intervention.** That is a sixth class:

> **D6 · `EXTRACTED_NEVER_ROUTED` — the datum is in the repository, correctly captured, and no portfolio
> artefact has ever read it.**

🎯 **This is the `DISCOVERY_TRACE` lesson of this morning, inverted.** There, the DIVERGE step *saved*
the cycle by containing the branch the evidence promoted. Here it **failed** to contain the branch the
evidence promoted, and only a prediction aimed at a *specific named datum* (`serum ALT`) found it — a
prediction aimed at "is the portfolio blind to the periphery?" would have returned the same
reassuring zero and I would have filed D1. **Generic predictions cannot discriminate D1 from D6.
Prediction P3's value came entirely from naming one analyte in advance.**

### HYPOTHESIS GRADES
| | grade | justification |
|---|---|---|
| **H-G1** (D1 dominates) | 🟡 **QUALIFIED.** True for 71 of 72 cells; **false for the one cell that is filled**, which is D6 | the dominance is real, the mechanism is not uniform |
| **H-G2** (one family in >1 arm) | 🔴 **REFUTED as stated** — two families are | recorded, not smoothed |
| **H-G3** (a measured, never-routed analyte exists) | 🟢 **CONFIRMED** — serum ALT | and it produced D6 |

### DISCRIMINATOR (fixed in advance, and §5 is what it selects)
*Does any intervention paper report a peripheral analyte that no LEGEND file carries?* If yes → the
first move is an **extraction**, not a request for measurement. If no → the absence is the field's.
🔴 **This is unresolved and it is exactly what §5 T0-a tests** — I can read LEGEND's transcription of
Table 3, and I cannot read Table 3. **Naming the discriminator I cannot run is the honest output; running
a different one and reporting it as this one is not.**

---

## 7 · `REVIVAL_TRIGGER`s AND `COULD NOT ESTABLISH`

### 7.1 · `REVIVAL_TRIGGER`s opened by this file

| ID | What is parked | What would reopen it |
|---|---|---|
| **RT-G1** | **Bicarbonate/pH and platelets are `NOT RECONSTRUCTIBLE` in all 8 arms** (16 cells) | Discovery of **banked fresh-frozen plasma with a documented pre-analytic chain**, or any WWOX cohort currently being terminated to which one tube could be attached |
| **RT-G2** | **The `Wwox^hep−/−` serum-ALT datum is not routed to any portfolio artefact** | Any therapeutic analysis that scores a liver endpoint, or a second liver-enzyme measurement in **any** WWOX animal — at which point C6 becomes adjudicable across models |
| **RT-G3** | **Hypoglycaemia is classed species-specific on two mouse nulls versus one rat** | A glucose measurement in the **NCKU nulls**, the **`P47T` knock-in**, the **`gt/gt` hypomorph** or **any second rat line**. A hypoglycaemic rat, or a normoglycaemic mouse null, moves this immediately |
| **RT-G4** | **`CLAIM 038` compares mouse `mg/dL` with rat `mg/ml` without flagging the unit** | Re-adjudication of `PMID 17803050` Table 2's column header at the rendered page, or an erratum |
| **RT-G5** | **The `PMID 19936220` Table 3 row count is assumed to be four** | T0-a. A table with more rows retroactively moves cells in §1.5 from ⚪ to 🟢 **and makes this audit's denominator wrong in the direction that helps** |
| **RT-G6** | **The cortical-bone rescue is unanchored** (`CNE-1`) | Appendix S1 inspection, **or** any verbatim sentence from `PMID 34747138` naming a bone measurement in treated animals |
| **RT-G7** | **Gonadal invariance rests on a citation for the mouse limb** | A first-hand read of `Aqeilan 2009` on Leydig cells in the `Wwox`-null mouse |
| **RT-G8** | **Row A2's ten ⚪ cells are `NOT ESTABLISHED`, not absences** | Completion of `PMID 42422765`'s Results and Methods, or recovery of S5/S6 |

### 7.2 · `COULD NOT ESTABLISH`

| ID | Statement | Why not, and what was tried |
|---|---|---|
| **CNE-1** | 🔴 **That `PMID 34747138` reports cortical bone comparable to wild type in treated animals** | Unscoped grep for `bone` across all four surfaces this repository holds for that PMID returns **only LEGEND prose** (§4.3). The `L4` quoted block covers Leydig cells and fertility and **does not mention bone**. Carried in the 2021 manifest as `INFERENZA, not DATO`. **The paper may well report it; this repository cannot show that it does** |
| **CNE-2** | Whether `PMID 19936220` Table 3 prints more than four analytes | The surface is not on disk; `files/fulltext/` does not exist in this edition. **This is the audit's own discriminator and it is the one thing I could not run** |
| **CNE-3** | Whether any banked serum, plasma or fixed limb from **any** WWOX treated cohort still exists | Unknowable from a repository. No external contact was made and none is authorised. **Every Tier-1 route in §2 is conditional on this and says so** |
| **CNE-4** | Whether the rat's `GPT`/`GOT`/`ALP` values are normal | Table 2's enzyme rows carry **sample-size footnotes, not significance footnotes**; ♀ CPK is ~8.5× higher **with no marker**. `CLAIM 038` already records this as *"non importabile in nessuna direzione"*, and it remains so |
| **CNE-5** | Whether `PMID 42422765` measured any peripheral analyte beyond glucose | Its Results and Methods are **declared unread**; S5/S6 unreachable after five retrieval routes. 🔴 **Its ten ⚪ cells are an upper bound on emptiness, not a measured absence** |
| **CNE-6** | Whether the `Wwox^hep−/−` HFD arm measured glucose | Unscoped grep of `PMID29724996.json` for `glucose\|insulin\|glycemi` returns **zero**; the manifest is a partial surface for that paper. **Recorded as unestablished, not as zero** |

---

## 8 · SELF-GRADE

| Axis | Grade | Justification — and nothing here restates the brief as a finding |
|---|---|---|
| **The denominator itself** | 🟢 **A** | 80 cells defined before filling, three classes of emptiness kept apart, read depth bounded per row, and the headline is an exact count — **0 of 48** — not an impression. The 90 % figure survives discarding the one partially-read row |
| **The empty cells as the product** | 🟢 **A−** | The audit's most useful output is the **16 cells that are permanently gone** (C2, C5). No prior file in this repository had separated *recoverable empty* from *lost empty*, and that distinction is what makes T2-d the only route rather than one option among several |
| **Cross-model discipline (§3)** | 🟢 **A−** | Nothing pooled; the invariant/specific split is offered for **4 of 10** families and the other six are labelled `UNDETERMINED` **because an assay is missing, not because models disagree** — which is the distinction the brief called the hard part. The unit hazard (`mg/ml` vs `mg/dL`) is new to this repository and bounds every number in the section |
| **The CNS-reversibility statement (§4)** | 🟢 **B+** | Three systems separated into three evidence grades rather than asserted together, and the third turned out to have **no source**. 🔴 Marked down because I cannot open the Appendix and therefore cannot close `CNE-1` — I can only show that this repository never did |
| **Corrections to prior work** | 🟢 **B+** | Scientist F's conclusion reproduced and **its count corrected** (2 → 6) with the mechanism named as failure mode (11); the DISCOVERY_TRACE's zero-count reproduced bilingually and unscoped across all 7 `tx007_*` files and confirmed |
| **The trace (§6)** | 🟡 **C+** | Persisted before the confirmatory searches, and **P2's sub-clause was refuted against me**. 🔴 Marked down hard for a real defect: **my DIVERGE step did not contain D6**, the branch that actually explains the only filled cell my hypotheses were about. The `DISCOVERY_TRACE` this morning was saved by its diverge step; mine was not, and only a prediction naming one analyte in advance caught it |
| **The experiment (§5)** | 🟡 **B−** | `NEW ANALYSIS ONLY`, and it declines to re-propose the blood panel that two prior actors already own. 🔴 But it is **blocked in this environment** — `files/fulltext/` does not exist here — so it is a specified experiment, not an executed one, and §5 says so rather than describing a read I did not perform |
| **Discipline** | 🟢 **A** | One file written. No git. No `*_current.md`, registry, queue, ledger, receipt or manifest touched. No `BATCH_COMMIT`. No external contact, no fetch, no purchase. No clinical framing. `DATO`/`INFERENZA`/`IPOTESI` separated throughout; extraction damage recorded per rule 5d rather than normalised; **no zero in this file is a PubMed count of mine** |
| **Own errors, recorded** | — | (i) My first `alkaline phosphatase` sweep returned 0 while **ALP** is present — failure mode (8), committed while writing the failure-mode section. (ii) My first pattern `timo\b` matched *Ultimo*, a self-inflicted false positive from a missing leading boundary. Both corrected in place |
| **Overall** | 🟢 **B+** | A defensible denominator with an exact empty-cell count and a permanent-loss count, a cross-model split that refuses to over-claim, one provenance failure found in a four-times-repeated assertion, one new failure mode, one correction to a prior actor's count — and a trace that failed in a way worth writing down |

---

**End.** Not medical advice. Read-only toward every canonical file, registry, queue, ledger, receipt and
the state manifest. Nothing promoted, nothing committed, no receipt claimed, no git command run. Every
clinical question is `HUMAN_REQUIRED` and belongs to a treating team.

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · 🔴 CNE-1 is HALF RIGHT, and I can close it rather than withdraw it

The file reports that *"cortical bone comparable to wild type"* has **no verbatim locator** in this
repository and reached my brief as an established report. 🟢 **The provenance complaint is correct.**
🔴 **The conclusion that it is unsupported is not** — I hold the primary and the sentence is there.

Repudi 2021, `PMC8649866`, Results, *Effect of neuronal WWOX restoration on ataxia, fertility, and
bone phenotypes*. According to PubMed, [DOI](https://doi.org/10.15252/emmm.202114599):

> *"Bone growth defects were also formerly documented in [Wwox] mutant mice …, and hence, we
> **examined bones of rescued mice and observed that cortical bones were of comparable size and
> thickness to WT mice** (Appendix Fig S4B)."*

🟢 **The locator is hereby supplied**, and the gap the file found was real: the repository carried
this as **paraphrase in interpretive prose** while the verbatim sentence sat unrecorded. That is
exactly the configuration this laboratory has been burned by twice (the Wang 2012 caption, the
42397075 brackets), and the 2026-08-09 receipt predicted it in advance.

⚠️ **The bound survives the closure and matters more than the quote**: the panel is
`Appendix Fig S4B`, which **nobody here has opened**, and the sentence is an *"observed … comparable"*
with **no quantification and no statistical test reported in the body**. So the correct grade is
**`DATO` that the authors state it**, `PREMISE: METHODS_INVISIBLE` on the measurement behind it.
Finding a quote does not upgrade an unquantified visual comparison.

## V2 · 🟢 Two measured claims verified at first hand

| Claim | Verdict |
|---|---|
| `platelet` \| `piastrin` \| `thrombocy` → **zero files** before this audit | 🟢 **VERIFIED** — an unscoped sweep returns exactly **one** file, this one. **Platelets have never been counted in any WWOX animal recorded here** |
| `CLAIM 038` carries rat chemistry in **`mg/ml`** while the mouse claim uses **`mg/dL`** | 🟢 **VERIFIED** — `claim_registry_current.md:707` reads *"BUN 12.6 → **40.3** mg/ml"*; `:666` reads *"BUN 37.25 vs 17.67 mg/dL"*. **40.3 mg/ml is 4,030 mg/dL**, which is not a survivable value. The rat figures are certainly `mg/dL` |

🔴 **A gated commit candidate is raised for the unit defect** —
`CC-20260922-CLAIM038-UNIT-CLASS-01`. It is **not** propagated. The scientific content of `CLAIM 038`
is untouched: the rat is uraemic and not hypoglycaemic, which is a statement about **direction and
significance** and does not depend on the unit. What the defect forbids is any **numeric**
cross-model comparison, and the file obeys that throughout its §3 — correctly, before the defect was
named.

## V3 · 🟢 The ELEVENTH failure mode, and it is the most embarrassing one yet

> *"A monolingual sweep under-counts in a bilingual corpus — an absence claim must state its
> LANGUAGE scope as well as its file-type scope."*

🟢 **Endorsed without reservation, and independently obvious once stated**: this repository's
registries and ledgers are written substantially in **Italian**. `ipoglicemia`, `acidosi` and
`milza` are invisible to an English sweep, which is why Scientist F's portfolio count of 2 was
really **6**. F's conclusion is unchanged and now better founded.

**Three of the eleven modes were found today**, and all three are about the **corpus**, not the
query: (9) a phrase in a JSON string field is invisible to a `--include=*.md` grep; (10) a census
returns a uniform zero because the question was asked of the **wrong document class**; (11) a
monolingual sweep under-counts a bilingual corpus. 🔴 **The standing form of an absence claim is
now: state the file-type scope, the language scope, and the document class — or run it unscoped.**

🟢 And the file then **tripped mode 8 on itself** (`alkaline phosphatase` → 0 while `ALP` is present)
and recorded it. An audit that catches itself is worth more than one that does not.

## V4 · What the audit actually established

🎯 **72 of 80 cells empty — 90 %.** And the row that carries it: **the six non-glucose, non-gonadal
families are 0 filled of 48**, across two gene-therapy papers, four drug arms, a diet arm, a GTT/ITT,
a xenograft, 17 years, four laboratories and two species.

🎯 **16 of the 72 are permanently gone** — bicarbonate is not recoverable from banked frozen serum
at any price, and platelets need fresh EDTA whole blood. 🟢 **No prior file separated *recoverable
empty* from *lost empty***, and that distinction is what converts an audit into a plan.

🔴 **And the sentence that should travel:** *the acidosis — the limb the field's own death hypothesis
rests on — has been measured in one model, once, in three animals, with an SEM ten times the wild
type's.*

**Model-invariant:** elevated **BUN/uraemia**, gonadal failure, growth arrest. **Model-specific
(discordant):** hypoglycaemia and hypocalcaemia. **Undetermined in six families because an assay is
missing, not because models disagree.** 🟢 Keeping the eight rows apart by driver and allele — *"no
two of the five mouse models are the same animal"* — is the discipline this question needed.

## V5 · The one experiment, endorsed with its blocker

**Existing-panel denominator recovery** — re-extract `PMID 19936220` Table 3 row-by-row, and open
Repudi 2021 `Appendix S1` at measured ppi. 🟢 **The right first move, because it decides whether the
absence is the FIELD's or LEGEND's** — a distinction no other file in this session has drawn and one
that changes who the next request goes to. 🔴 **Blocked here**: `files/fulltext/` does not exist in
the public edition, so all three surfaces need re-acquisition. Stated rather than glossed.

🟢 **New defect class `D6 EXTRACTED_NEVER_ROUTED`** — serum ALT in the `Wwox^hep−/−` HFD arm was
measured, reported **and extracted by LEGEND**, then never routed to any portfolio artefact. The
delegate found it in the branch its own DIVERGE step had **failed to contain**, and says so.

## V6 · Information gain and grade

**INFORMATION GAIN: HIGH.** A 90 % empty denominator, a permanent/recoverable split nobody had made,
an eleventh search failure mode, a unit-class defect in a canonical claim, and a new defect class.

**Grade: B+ endorsed; trace C+ endorsed** — the trace is correctly graded low because the winning
branch was outside its own divergence.

**No row is canonical; none is proposed for `BATCH_COMMIT`.** Nothing here is medical advice.
