# Repudi *et al.* 2021, *Brain* (PMID 33914858) — ingestion of the COMPLETE source bundle

**Actor:** SCIENTIST 2 (`scientist-2`) · **Date:** 2026-09-23 · **Class:** source-bundle ingestion + text-surface adjudication
**Target:** `PMID 33914858` — the primary behind `CLAIM 003` (`consolidated baseline`), which until today had
**zero receipts and zero full-text access** (publisher 403 / Cloudflare, reproduced 2026-09-11).

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every registry,
> every `*_current.md`, every queue, every ledger, the receipt chain and the state manifest. **Nothing
> promoted, nothing committed, no `BATCH_COMMIT`, no receipt recorded, no `git` command run.** Two files were
> written: this one, and an in-place correction to
> [`wwox_antibody_epitope_census_20260922.md`](wwox_antibody_epitope_census_20260922.md) (§ D.5 says exactly what changed).
>
> 🔴 **Nothing here is medical advice.** No molecule, dose, route or clinical framing appears below.
>
> 🔴 **No external contact and no download.** Network is blocked; every artefact was already staged locally by
> the Operator. No author, laboratory, foundation or vendor was approached. Vendor datasheets remain
> `EGRESS_BLOCKED` and no epitope, clone or host was inferred from a catalogue number.
>
> 🔴 **Alleles are never pooled.** `Wwox`-null (KO), Nestin-Cre `N-KO`, Synapsin1-Cre `S-KO`, `S-HT`,
> Olig2-Cre `O-KO`, GFAP-Cre `G-KO`, and the human `OS-WWOX-KO` oligocortical spheroid are different objects
> and are kept apart in every row below.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.

---

## 0 · WHAT WAS DONE, AND WITH WHAT

| Artefact staged by the Operator | Bytes | Role assigned here |
|---|---|---|
| `files/fulltext/PMID33914858_Repudi2021_OUP.html` | 532,805 | 🥇 **AUTHORITATIVE FOR TEXT** |
| `files/fulltext/PMID33914858_Repudi2021_OUP_browserprint.pdf` | 1,336,069 | 🔴 **NOT independent evidence** (print of the same HTML); **damaged text layer**, see § A |
| `files/fulltext/PMID33914858_Repudi2021_suppl_File009_methods_figures.pdf` | 7,912,498 | 🥇 **AUTHORITATIVE FOR SUPPLEMENTARY FIGURES** (the only surface that carries them) |
| `files/fulltext/PMID33914858_Repudi2021_suppl_File012.xlsx` | 4,741,267 | Supplementary Table 1 — see § E |
| `files/fulltext/PMID33914858_Repudi2021_suppl_File013.xlsx` | 5,294,747 | Supplementary Table 2 — see § E |
| `files/fulltext/PMID33914858_Repudi2021_suppl_File014_reagents.xlsx` | 16,697 | Supplementary Table 3 — see § D |
| `files/fulltext/PMID33914858_Repudi2021_suppl_File010.mp4` | 8,308,311 | Video — see § F |
| `files/fulltext/PMID33914858_Repudi2021_suppl_File011.mp4` | 2,066,761 | Video — see § F |

**Derivation of the text surfaces (reproducible).** The HTML was reduced to text with a stdlib-only
tag-stripper (scripts/styles/comments removed, block tags → newline, `html.unescape` applied **last** so that
`&lt;` becomes `<` rather than being eaten as markup). Both PDFs were read with
`framework/scripts/pdf_text_extract.py extract`, which is the only extractor this deployment has (no
`pymupdf`, `pdfplumber`, `poppler`). The Operator's pre-extracted `repudi_print.txt` and `repudi_suppl.txt`
were re-derived independently and came back **byte-identical** to my own extraction — so the damage recorded
in § A is a property of the artefacts, not of one extraction run.

🔴 **Every zero reported in this file was earned.** No count of 0 appears below without a positive-control
set from the same surface, same tool, same invocation, returning non-zero. The controls are printed inline.

---

## A · TEXT SURFACE FIDELITY — WHICH ARTEFACT IS AUTHORITATIVE, AND WHAT THE OTHERS DESTROY

### A.1 The inherited problem, restated so the test is falsifiable

`framework/eval/finding_20260809_text_surface_fidelity.md` is the repository's foundational text-fidelity
finding **and it was discovered on this exact paper**. It records that the *publisher PDF* (then held as
`files/fulltext/PMID33914858_Aqeilan2021.pdf`, sha256 `960569a9…`, now absent from the tree) extracts as:

> `Results were considered significant when P 5 0.05, otherwise they`

and lists four named casualties, with **0 occurrences of `<`, `>`, `≤`, `≥` in the whole document** against
14 of `P 5 0.0…`. That surface is `SUSPECT` and the reading of PMID 33914858 was formally **suspended**, not
merely incomplete.

The Operator acquired the HTML specifically to bypass that. **The test is therefore pre-specified:** take the
four casualties the 2026-08-09 finding names, and read them off each surface now held.

### A.2 🎯 THE FOUR-CASUALTY TEST — run first-hand, 2026-09-23

| Casualty (from the 2026-08-09 finding) | Publisher PDF, 2026-08-09 (inherited, artefact now absent) | 🥇 **OUP HTML** (read first-hand today) | Browser-print PDF (read first-hand today) |
|---|---|---|---|
| Methods, significance threshold | 🔴 `P 5 0.05` | 🟢 `Results were considered significant when P < 0.05, otherwise they were represented as ns` | 🟡 `Results were considered signiÞcant when P!<!0.05,otherwise they were represented as ns` |
| RNA-seq fold-change cutoff | 🔴 `fold change 41.5` | 🟢 `fold change >1.5; Supplementary Table 1` | 🟡 `fold change >1.5;)` — operator intact, **xref text dropped** |
| EEG delta band | 🔴 `delta (55 Hz)` | 🟢 `delta (<5 Hz)` | 🟡 `delta (<5!Hz)` |
| RNA-seq *P*-value cutoff | 🔴 `P-value 50.01` | 🟢 `P-value <0.01` | 🟢 `P-value <0.01` |

**`DATO`. The HTML restores all four. The browser-print PDF restores the `<` and `>` characters that the
publisher PDF destroyed — but introduces a different, narrower, and in one respect *worse* corruption.**

### A.3 Quantified damage, paired statement by statement

All 25 statistical statements in the article were enumerated on both surfaces with the permissive pattern
`\*{0,3}P[^0-9A-Za-z]{1,5}0\.[0-9]+`, which is deliberately agnostic about what sits between `P` and the
number. **Both surfaces return exactly 25** — so this is a true pairing, not a coverage difference.

| Operator, as the author wrote it | Count in 🥇 **HTML** | What the browser-print PDF returns | Survives? |
|---|---|---|---|
| `<` (U+003C) | **14 / 14** | `<` | 🟢 **14 / 14 intact** |
| `=` | **7 / 7** | `=` | 🟢 **7 / 7 intact** |
| `≤` (U+2264) | **4 / 4** | `"` (U+0022, double quote) | 🔴 **0 / 4 — total loss** |

🔴 **The browser-print PDF destroys every "less-than-or-equal" in the paper.** Verbatim pairs:

| 🥇 HTML | browser-print PDF |
|---|---|
| `***P ≤ 0.001` (Fig. 3 legend) | `***P " 0.001` |
| `***P ≤ 0.001` (Fig. 3 legend) | `***P" 0.001` |
| `*P ≤ 0.01` (Fig. 4G legend) | `*P!"!0.01` |
| `**P ≤ 0.001` (Fig. 4G legend) | `**P!"!0.001` |

**`INFERENZA`, and it is the operationally important one.** This is the *same failure class* as the 2026-08-09
finding, one notch less visible: `"` is not numerically plausible the way `5` was, so it will not silently
verify as a number — but it **is** a legal quotation character, so a quote lifted from the print surface reads
as if the author had opened a quotation, and a grep for `≤` on that surface returns an **unearned zero**.

### A.4 The whole-document glyph tally

| Probe | 🥇 HTML | browser-print PDF |
|---|---|---|
| `≤` (correct) | **4** | 🔴 **0** |
| `’` right single quote (correct) | **17** | 🔴 **0** |
| `–` en dash (correct) | **109** | 🔴 **0** |
| U+2009 thin space (correct) | **304** | 🔴 **0** |
| `significant` (spelt correctly) | **19** | 🔴 **2** |
| `Þ` — the `fi` ligature destroyed | 0 | 🔴 **112** |
| `ß` — the `fl` ligature destroyed | 0 | 🔴 **29** |
| `Õ` — the apostrophe destroyed | 0 | 🔴 **26** |
| `Ð` — the en dash destroyed | 0 | 🔴 **116** |
| `!` — the thin space destroyed | 1 | 🔴 **1,174** |
| non-printable characters | 420 (all legitimate: U+2009 ×304, U+00A0 ×114, U+2002 ×2) | 🔴 **12,025** (9.9 % of the file) |

🎯 **The single most dangerous line in this table is `significant`: 19 → 2.** Seventeen of the nineteen
occurrences of the word *significant* in this paper are **not findable by that spelling** in the browser-print
surface, because they read `signiÞcant`. A sibling actor grepping that surface for `significant` would
conclude the paper barely uses the word. The same applies to `signiÞcance`, `Þlter`, `ßuctuations`, `conÞrm`,
`Þgure`, `speciÞc`, `deÞcit` and every other `fi`/`fl` word in a neurobiology paper — which is most of them.

**`INFERENZA`.** The browser-print corruption is a **MacRoman-class mis-mapping** of the ligature and
punctuation block (`fi`→`Þ`, `fl`→`ß`, `’`→`Õ`, `–`→`Ð`, U+2009→`!`, `≤`→`"`), not the unmapped-subset-font
failure of 2026-08-09. 🔴 **The mechanism is not established** — the 2026-08-09 finding was corrected once for
asserting a mechanism as a datum and this file will not repeat that. The `DATO` is only: *these specific
character pairs differ between the rendered HTML and the print-derived text layer.*

### A.5 Two further defects of the browser-print surface, independent of glyphs

1. **Hyperlinked cross-reference text is dropped.** HTML: `fold change >1.5; Supplementary Table 1)`.
   Print: `fold change >1.5;)`. The empty parenthesis is the fingerprint. (Overall `Supplementary Table` counts
   are 3 on both surfaces, so this is *selective* loss, which is worse than uniform loss — it cannot be
   detected by a count.)
2. **Running headers, the URL and a capture timestamp are interleaved mid-sentence.** Print:
   `…therecording setup.Statistical analysis|23/09/26, 15!52Neuronal deletion of Wwox, associated with…
   https://academic.oup.com/brain/article/144/10/3061/6259140Statistical analysis…`. Word spaces are also lost
   at line joins (`therecording`, `nosignificance`, `579downregulated`). 🔴 **A verbatim locator taken from
   this surface can therefore contain text the authors never wrote in that order.**

### A.6 🔴 The supplement PDF is a THIRD, previously unrecorded damage class

`File009` is the **only** surface carrying the supplementary figure legends, so it cannot be discarded — but
it must be quoted with its damage declared. Its signature is **language-tag injection**: XML/Word language
attributes are emitted into the text stream *in place of* the Greek letters and symbols they annotated.

| Raw string in the extracted supplement | What it must be | Basis |
|---|---|---|
| `Tuj1 (Neuron-specific class III el-GR-Tubulin)` | `βIII-Tubulin` | `el-GR` = Greek language tag; the `β` is gone |
| `PDGFRel-GR` | `PDGFRα` | same mechanism (13 × `en-CA`, 2 × `el-GR` in the file) |
| `Error bar represents en-CA±SEM` | `Error bar represents ±SEM` | `en-CA` injected before `±` |
| `(* < 0.05, ** < 0.01, *** < 0.001,` | `(*P < 0.05, **P < 0.01, ***P < 0.001)` | 🔴 **the `P` itself is deleted** |
| `(*** < H)` · `(*** < 0.00E)` · `(**< A)` | truncated | 🔴 **legend text is lost mid-sentence, not merely mis-mapped** |
| `immunostained for CC1 (green) and anti-` | truncated | 🔴 Suppl. Fig. 7E: the second primary's name is **destroyed** |

🔴 **Consequence, binding on anyone quoting the supplement:** the `<` in the supplementary legends survives,
but the `P` preceding it does **not**, and at least four legend clauses are truncated. Supplementary
significance thresholds may be quoted; supplementary *P*-symbols may not be reconstructed silently, and
Suppl. Fig. 7E's second primary antibody is `NOT RECOVERABLE` from this surface.

### A.7 🥇 VERDICT — authority, per content class

| Content class | Authoritative artefact | Status of the alternatives |
|---|---|---|
| **TEXT** (abstract, introduction, methods, results, discussion, figure legends, references) | 🥇 `PMID33914858_Repudi2021_OUP.html` | Browser-print PDF: 🔴 **REFUSED as a locator source.** Publisher PDF (2026-08-09): 🔴 `SUSPECT`, artefact absent |
| **MAIN FIGURES** (images) | 🔴 **NEITHER.** The HTML carries the *legends* and thumbnails-by-reference only; the browser-print PDF renders whatever the browser rendered, at unrecorded effective ppi | 🔴 `SOURCE-DEPTH LIMITED` — see § A.8 |
| **SUPPLEMENTARY FIGURES** (images **and** legends) | 🥇 `…_suppl_File009_methods_figures.pdf` — the **only** surface that has them | Its text layer carries the § A.6 damage and must be quoted with it declared |
| **SUPPLEMENTARY TABLES 1–3** | 🥇 `…_File012.xlsx`, `…_File013.xlsx`, `…_File014_reagents.xlsx` | Structured; no text-layer question arises |

### A.8 The one thing the browser-print PDF *is* good for, and the bound on it

The browser-print PDF is **not independent evidence** — it is a rendering of the same HTML, so it can
corroborate nothing the HTML says. Its only legitimate use is **visual**: it is the only artefact in the
bundle that shows the main-text figure *images* at all, because the HTML references them rather than
embedding them. 🔴 **Bound:** its rendering ppi, its figure resolution and whether it captured full-resolution
or thumbnail assets are all `NOT STATED`, so it can support *"the panel exists and this is roughly what is in
frame"* and **cannot** support any measurement, any cell count, or any judgement about a structure at the
limit of resolution. Reading a Purkinje monolayer out of it would be exactly the overreach § C refuses.

### A.9 `INFERENZA` for the framework — the 5d rule is confirmed and needs one extension

`gold_is_in_the_details.md` § 5d already says *"prefer XML/HTML PMC over the PDF, always"*. This act confirms
it on the very paper that generated it, and adds a case the rule does not yet name: **a browser print-to-PDF
of a good HTML is not a rescue of that HTML — it is a new, independently damaged derivative.** Re-printing a
clean structured surface to PDF *manufactures* a `SUSPECT` artefact from a sound one. The correct handling is
the one taken here: keep the print PDF for visual adjudication, refuse it for text, and never normalise it.

⚪ Offered as a `capability-scout`-class observation for whoever owns that protocol; **not written to it by me.**

---

## B · IDENTITY

### B.1 Verified against `<meta name="citation_*">` in the publisher HTML

| Field | Value, verbatim from the HTML | Verdict |
|---|---|---|
| Title | `Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects` | 🟢 matches the task statement exactly |
| Journal | `Brain` · ISSN `0006-8950` | 🟢 |
| Volume / issue / pages | `144` · `10` · `3061`–`3077` | 🟢 |
| Publication date | `2021/11/29` (issue); the article is the 2021-04-28 advance publication indexed by PubMed | 🟢 |
| DOI | `10.1093/brain/awab174` | 🟢 |
| PMID | `33914858` | 🟢 (self-declared in the HTML's own metadata) |
| Keywords | `phenotype`, `epilepsy`, `oligodendroglia`, `organoids`, `brain` | — |

### B.2 Authorship — full byline in order

`Repudi, Srinivasarao` · `Steinberg, Daniel J` · `Elazar, Nimrod` · `Breton, Vanessa L` · `Aquilino, Mark S` ·
`Saleem, Afifa` · `Abu-Swai, Sara` · `Vainshtein, Anna` · `Eshed-Eisenbach, Yael` · `Vijayaragavan, Bharath` ·
`Behar, Oded` · `Hanna, Jacob J` · `Peles, Elior` · `Carlen, Peter L` · `Aqeilan, Rami I`

- 🟢 **First author: Repudi, Srinivasarao.** Confirmed.
- 🟢 **Senior/last author: Aqeilan, Rami I** (Hebrew University-Hadassah, The Lautenberg Center). Confirmed.
- Four institutions: Hebrew University-Hadassah (Jerusalem), Weizmann Institute (Rehovot), Krembil Research
  Institute / UHN (Toronto), and Hebrew University Dept. of Developmental Biology.

### B.3 🔴 The filename question, answered

The repository's acquisition route recorded this paper as `files/fulltext/PMID33914858_Aqeilan2021.pdf`
(`ledger/tasks/orchestrator/ORCH-SCIENTIST-IMPROVEMENT-20260911.json:114`;
`ledger/tasks/scientist-a/AQEILAN-FT-A-001.json:214`; `framework/eval/finding_20260809_text_surface_fidelity.md:122`).

**`DATO`. That filename attributes the paper to its LAST author, not its first. The correct short form is
Repudi 2021.** The Operator's newly-staged bundle is already named correctly (`PMID33914858_Repudi2021_*`).

🟡 **But this is a naming inconsistency, not a citation error, and the distinction matters:** nothing in the
repository *cites* this paper as "Aqeilan 2021" in prose — the string appears only inside acquisition
filenames and ledger entries that point at those filenames. Those ledger entries are **historical records of
an acquisition that failed**, and the artefact they name is absent from the tree. 🔴 **I did not edit them**
(ledgers are append-only through their validated writers, and rewriting a historical acquisition record would
falsify what that session actually did). **Recommendation, `HUMAN_REQUIRED` for whoever owns the queue:** when
PMID 33914858 is next written into the full-text queue or paper registry, it enters as **Repudi 2021**, and
the historical `Aqeilan2021` filenames are left standing as the record of the failed 403 route.

### B.4 🎯 A COLLISION HAZARD THIS BUNDLE CREATES — flagged, not resolved

🔴 **There are TWO "Repudi 2021" papers in this corpus and they are different objects.**

| | **PMID 33914858** (this bundle) | **PMID 34747138 / PMC8649866** |
|---|---|---|
| Journal | *Brain* 144(10):3061–3077 | *EMBO Molecular Medicine* 13:e14599 |
| Subject | Conditional `Wwox` deletion — `N-KO`, `S-KO`, `O-KO`, `G-KO`; epilepsy + myelin | Neonatal AAV9 gene therapy |
| Vector work | 🔴 **NONE** | `AAV9-hSynI-mWwox` / `-hWWOX` / `-EGFP`, ICV at P0 |
| Cited in the repo as | *(previously unread)* | "the 2021 paper" throughout `tx007_purkinje_frontier_20260922.md`, `purkinje_cheapest_path_and_community_followup_20260922.md`, `cerebellum_layer_localisation_20260922.md` |

**Earned zero, with positive controls, over the raw HTML of PMID 33914858:**

| Positive control | count | | Query | count |
|---|---|---|---|---|
| `Wwox` | 336 | | `AAV9` | 🔴 **0** |
| `myelin` | 227 | | `hSynI` | 🔴 **0** |
| `Brain` | 416 | | `NeuN` | 🔴 **0** |
| | | | `Purkinje` | 🔴 **0** |
| | | | `calbindin` | 🔴 **0** |

🟢 **No repository correction is required** — the frontier files are internally correct and cite
`PMID 34747138` / `PMC8649866` explicitly where it matters
([`cerebellum_layer_localisation_20260922.md:9`](cerebellum_layer_localisation_20260922.md),
[`purkinje_cheapest_path_and_community_followup_20260922.md:15`](purkinje_cheapest_path_and_community_followup_20260922.md)).
🔴 **The hazard is prospective:** the bare string *"Repudi 2021"* is now ambiguous in this corpus, and
`Fig. 2G`, `Fig. 2F`, `≈57 %`, `AAV9-hSynI-EGFP` and the whole transduced-fraction arithmetic belong to
**EMBO Mol Med 2021**, *not* to the paper ingested here. Anyone writing *"Repudi 2021"* without a PMID from
today forward should be assumed to have made an error until the PMID is supplied.

---

## C · SUPPLEMENTARY FIGURES vs THE CEREBELLAR / PURKINJE FRONTIER — the delta only

**Inherited and NOT re-derived.** `MAB377` is NeuN clone A60 and A60 does not label Purkinje cells
([`wwox_antibody_epitope_census_20260922.md`](wwox_antibody_epitope_census_20260922.md) § 3 `B3`;
[`tx007_purkinje_frontier_20260922.md:66`](tx007_purkinje_frontier_20260922.md) `A-s1`). That Purkinje cells
have never been measured with a Purkinje marker in any `Wwox` model
([`tx007_purkinje_frontier_20260922.md:73`](tx007_purkinje_frontier_20260922.md) `A-s8`;
[`ataxia_without_cerebellar_lesion_20260922.md:65`](ataxia_without_cerebellar_lesion_20260922.md)) is **HELD**.
Both are used below; neither is rediscovered.

### C.1 🎯 The cerebellum WAS imaged in this paper — five times, and nobody in the repository knew

Until today this paper was `SUSPECT`/unread and is described in
[`ataxia_without_cerebellar_lesion_20260922.md:37`](ataxia_without_cerebellar_lesion_20260922.md) as
*"SIBLING-ATTESTED, and flagged suspect … no PMCID … a `SUSPECT` local PDF whose reading is suspended."*
The supplement contains **five separate cerebellar imaging panels**, across **three genotypes**.

| Panel | 🔴 GENOTYPE | Age | MARKER / channel | What is actually shown |
|---|---|---|---|---|
| **Suppl. Fig. 1B** | 🎯 **`N-KO` vs `N-Control`** (Nestin-Cre) | P16 | 🎯 **anti-WWOX + anti-NeuN** | The only WWOX-channel cerebellar image in the paper |
| **Suppl. Fig. 5B** | `S-KO` vs `S-Control` | P18 | Luxol fast blue (histochemical) | Myelin, cerebellum is the magnified inset |
| **Suppl. Fig. 5D** | `N-KO` vs `N-Control` | P17 | anti-MBP (grey) | Myelin; cerebellum magnified |
| **Suppl. Fig. 5E** | `N-KO` vs `N-Control` | P17 | Luxol fast blue | Myelin; corpus callosum + cerebellum magnified |
| **Suppl. Fig. 6C–D** | `S-KO` vs `S-Control` | P17 | anti-CC1 + anti-NG2 | Oligodendrocyte-lineage **cell counts** in cerebellum |
| *(main text)* **Fig. 4D–E** | `S-KO` vs `S-Control` | P18 | anti-CNP + anti-MBP | Myelin intensity, quantified |
| *(main text)* **Suppl. Fig. 7C** | 🎯 **`Wwox`-null vs wild-type** | P18 | Luxol fast blue | Myelin; cerebellum magnified |

### C.2 The legend that matters, verbatim

> **Supplementary Fig 1.** *Validation of Cre (under the promoter of Nestin or Synapsin I or Olig2 or GFAP)
> recombinase mediated murine Wwox ablation in brain, neurons, oligodendrocytes and astrocytes. **(A and B)
> Immunofluorescence staining with anti-WWOX antibody showing the loss of WWOX expression in N-KO brain
> tissues. Representative images are shown from cortex (shown in A) and cerebellum (shown in B) regions in
> N-KO, N-Control at P16. Neuronal nuclei stained with anti-NeuN antibody.** (C) Immunofluorescence staining
> with anti-NeuN and anti-WWOX showing loss of WWOX expression (shown with white arrows) in neurons of S-KO
> brain compared to S-Control at P17. Representative images are shown from the cortex region. (D) Intact
> levels of WWOX are maintained in oligodendrocytes (stained with CC1) in S-KO compared to S-Control at P17.
> Representative images are shown from the corpus callosum. (E) Immunolabeling with CC1 antibody and
> anti-WWOX showing absence of WWOX in CC1 positive cells of O-KO (shown with arrow heads) compared to
> corresponding O-Control at P18. (F) Immunofluorescence images showing loss of WWOX expression in astrocytes
> (stained with anti-GFAP) of G-KO brain as compared to G-Control at P18. Magnified area is shown in a white
> square box. **Scale bars A) and B) 100 µm**, C) and D) 20 µm, E) and F) 25 µm.*
>
> — `PMID33914858_Repudi2021_suppl_File009_methods_figures.pdf`, *Supplementary Figure Legends*, Suppl. Fig. 1

> **Supplementary Fig 6.** *… **(C) Representative images of cerebellum immunostained with CC1 and anti-NG2
> showing reduced number of both CC1 and NG2 positive (shown with white arrows) cells in S-KO compared to
> S-Control at P17. (D) Graph represents the average number of CC1 and NG2 positive cells from three
> identical sections of the cerebellum (area 0.5 mm2) from each genotype (S-Control, n = 3; S-KO, n = 3).**
> Error bar represents ±SEM (\**< 0.01). … Scale bars A) right, 200 µm, middle 100 µm, left 20 µm, B) left
> 200 µm, right 25 µm and **C) 50 µm**.*
>
> — ibid., Suppl. Fig. 6. ⚠️ The `P` before `**< 0.01` is deleted by the § A.6 damage; restored here as
> `**P < 0.01` by the same forced-restoration logic as `wwox_antibody_epitope_census_20260922.md` § 1.2, and
> flagged rather than silently corrected.

> **Figure 4.** *… **(D) Representative images of brain sections immunostained with anti-CNP and anti-MBP are
> shown from cerebellum. (E) Quantification of fluorescence intensity of CNP and MBP display reduced intensity
> in S-KO compared with S-Control.** … Error bar represents ±SEM (\*P ≤ 0.01, \*\*P ≤ 0.001). Scale bars = 50 µm
> (A), 2 µm (B) and 50 µm (C).*
>
> — `PMID33914858_Repudi2021_OUP.html`, Figure 4 legend. 🔴 **Note: no scale bar is given for D, E, F or G**,
> and the `2 µm` assigned to (B) — a cortical CNP/MBP overview — is anomalous on its face. Recorded as read;
> not corrected.

### C.3 🔴 The earned zero

`pdf_text_extract.py search` over `…suppl_File009_methods_figures.pdf`:

```
positive controls:          query:
  OK  32  Wwox                0  Purkinje
  OK   7  cerebellum          0  calbindin
  OK  13  CC1                 0  Calb1
  OK  17  S-KO                0  parvalbumin
  OK  12  N-KO                0  Pcp2
  OK   2  NeuN                0  molecular layer
                              0  granule
                              0  Nissl
                              0  cresyl
```

All six positive controls non-zero on the same surface, same tool, same invocation. **The nine zeros are
earned.** The same nine terms are zero in the main-text HTML against the § B.4 controls.

### C.4 THE DELTA — answering (i)–(iv) exactly

**(i) Does the supplement change what was actually IMAGED?** 🎯 **YES, substantially.**
The repository's cerebellar picture for the `Wwox` conditionals was built entirely from
`PMID 34747138` (EMBO Mol Med) and from the untreated-null/rat literature. This paper adds **seven**
previously-unknown cerebellar panels across **four genotypes** (`Wwox`-null, `N-KO`, `S-KO`, plus `N-Control`/
`S-Control`/WT), including the first cerebellar **anti-WWOX immunofluorescence in a Nestin-Cre conditional**,
and the first cerebellar **oligodendrocyte-lineage cell count** (`CC1`/`NG2`, per 0.5 mm², n=3 vs n=3) in any
`Wwox` model. [`ataxia_without_cerebellar_lesion_20260922.md:148`](ataxia_without_cerebellar_lesion_20260922.md)
records *"What stain? — not recorded. No calbindin, no PCP2/L7, no Car8, no parvalbumin, no NeuN, no MBP is
recorded anywhere"* for the cerebellar look; that statement was about `PMID 17803050` (the *lde* rat) and
remains true there, but for the mouse conditionals it is now **superseded by named stains**.

**(ii) Which GENOTYPE?** 🔴 **The cerebellar WWOX channel exists in exactly ONE genotype: `N-KO` (Nestin-Cre),
at P16, in Suppl. Fig. 1B.** Every other cerebellar panel is myelin or oligodendrocyte-lineage only:
`S-KO` (Fig. 4D–E, Suppl. Fig. 5B, Suppl. Fig. 6C–D), `N-KO` (Suppl. Fig. 5D–E), `Wwox`-null (Suppl. Fig. 7C).
🎯 **There is no cerebellar WWOX image of the `S-KO` (Synapsin1-Cre) animal** — Suppl. Fig. 1C, the S-KO
WWOX+NeuN panel, is explicitly *"from the cortex region."* This matters because `S-KO` is the genotype
carrying the paper's ataxia, seizure and myelin phenotypes.

**(iii) Which MARKER / channel?** Suppl. Fig. 1B is **anti-WWOX + anti-NeuN**. The reagent table (§ D)
identifies that NeuN as `MAB377, Millipore, 1:500` — 🔴 **the same catalogue number, and therefore the same
clone A60, that `B3` already establishes is Purkinje-negative.** So the paper's only cerebellar WWOX image is
counterstained with a marker that is blind to Purkinje cells *by construction*. The cerebellar
oligodendrocyte panels use `CC1` (mouse, `OP80`) and `NG2` (rabbit, `AB5320`); the cerebellar myelin panels
use `CNP` (mouse, Peles lab) and `MBP` (rabbit, `Ab65988`), or Luxol fast blue, which is a histochemical
myelin stain with no cell-identity information at all.

**(iv) What can and cannot be inferred about Purkinje cells specifically?**

| | |
|---|---|
| 🔴 **CANNOT be inferred** | Purkinje **number**, Purkinje **WWOX abundance**, Purkinje **WWOX presence or absence**, whether the Purkinje monolayer is affected in any genotype, and whether `Wwox` deletion is cell-autonomously required in Purkinje cells. No Purkinje marker was used. `A-f14` — *"a cerebellar WWOX measurement at cell-type resolution in a WWOX-DEFICIENT cerebellum"* — is **NOT closed by this paper** |
| 🟡 **CAN be inferred, weakly and only about the sheath** | That cerebellar **myelination** is reduced in `S-KO`, `N-KO` and `Wwox`-null, by three independent modalities (CNP/MBP intensity, LFB, CC1/NG2 counts). Purkinje **axons** are myelinated, so a cerebellar white-matter deficit is *consistent with* a Purkinje-axon deficit — but LFB and MBP cannot say which axons, and the paper never claims they can |
| 🎯 **NEW, and it is the one genuine narrowing** | `A-f1` asked whether the Purkinje monolayer is *in frame* in a published cerebellar WWOX+NeuN panel and called it **SOURCE-DEPTH LIMITED** because no full text existed. A structurally identical panel now exists and is held locally: **Suppl. Fig. 1B, N-KO vs N-Control, P16, WWOX + NeuN, 100 µm scale bar.** `A-f1`'s *class* therefore changes from `SOURCE-DEPTH LIMITED` to `READABLE — NOT YET READ`, for a **different genotype** than `A-f1` specified |

### C.5 🔴 Four bounds that travel with that narrowing, and they are severe

1. **It is `N-KO`, not `S-KO` and not the AAV arm.** Nestin-Cre deletes in neural stem/progenitor cells, so it
   removes `Wwox` from Purkinje cells *and* granule cells *and* Bergmann glia *and* oligodendrocyte lineage.
   The question `A-f1` was built to answer — *is the `hSynI` promoter active in Purkinje cells* — **cannot be
   asked of this panel at all**, because there is no vector and no promoter here.
2. **The identification is asymmetric, and in the opposite direction from `A-f1`.** `A-f1`'s asymmetry was
   *"in a `Wwox`-null host under a neuron-restricted promoter a positive reading is informative, a negative
   one is not."* Here the informative arm is the **`N-Control`**, not the `N-KO`: a large WWOX-positive soma
   at the NeuN-bright/NeuN-dark boundary in the *control* cerebellum would be the first evidence that
   Purkinje cells express WWOX in mouse. In the `N-KO`, WWOX is expected to be absent everywhere, so a
   negative there carries no cell-type information.
3. **100 µm scale bar, "representative images", n unstated.** Suppl. Fig. 1 is a **Cre-validation** figure.
   Its stated purpose is to show that recombination happened, not to quantify anything. No n is given for
   panels A/B, no quantification is offered, and at a 100 µm bar over a whole-cerebellum region the panel may
   or may not resolve a Purkinje soma. 🔴 **Whether the monolayer is in frame is `NOT YET READ` and this file
   does not assert it either way** — reading it requires the *supplementary figure image*, at measured
   effective ppi, which is an act I did not perform and which § A.8 bounds for the print PDF.
4. **12–14 µm sagittal cryosections, 2 % PFA.** Methods, verbatim: *"brains were incubated in 30% sucrose at
   4°C overnight then embedded in O.C.T. and sectioned (12–14 µm) using a cryostat."* 🎯 This is the **same
   protocol constraint** `tx007`'s proposal `P4` already flagged — *"a 12–14 µm cut is thinner than a Purkinje
   soma"* — now confirmed first-hand in a **second, independent archive**. It is a limit on counting, not on
   looking.

### C.6 🎯 What genuinely changed for the frontier, in one table

| Frontier item | Was | Is now | Why |
|---|---|---|---|
| `A-f1` (Purkinje monolayer in frame in a published WWOX+NeuN cerebellar panel) | `SOURCE-DEPTH LIMITED` | 🟡 **`READABLE — NOT YET READ`, in a different genotype** | Suppl. Fig. 1B is held locally; § C.5 bounds apply |
| `A-f14` (cell-type-resolved WWOX in a WWOX-deficient cerebellum) | `TRUE EXPERIMENTAL GAP` | 🔴 **UNCHANGED** | No Purkinje marker; NeuN is A60 |
| `A-f6` (does a Purkinje cell need WWOX cell-autonomously — `Pcp2`/`L7`-Cre) | `TRUE EXPERIMENTAL GAP · NEW ANIMALS IRREDUCIBLE` | 🔴 **UNCHANGED, and REINFORCED** | The paper proves this laboratory builds Cre×`Wwox^fl/fl` crosses routinely — four drivers in one figure (Nestin, Synapsin I, Olig2, GFAP). 🎯 `Pcp2`-Cre is the fifth driver they did not make |
| *"No cerebellum-resolved measurement exists in any Wwox model"* | asserted for **function** | 🟡 **holds for function; NARROWED for structure** | Cerebellar CC1/NG2 counts per 0.5 mm², n=3 vs n=3, now exist for `S-KO` |
| `P4` (calbindin + WWOX on existing sections) | proposed against the EMBO/2026 archives | 🎯 **a THIRD archive now qualifies** | `N-KO`/`N-Control` P16 cerebellar cryosections, same 12–14 µm protocol. ⚠️ Same mouse-vs-mouse collision: calbindin (mouse) cannot share a section with NeuN `MAB377` (mouse) — see § D.4 |

---

## D · REAGENT GEOMETRY — `…suppl_File014_reagents.xlsx` = Supplementary Table 3

Assignment is stated by the authors: *"All antibodies and primer sequences used in this study and the related
details are provided in **Supplementary Table 3**."* (Methods, Immunofluorescence). The workbook has two
sheets, `Primer Squence` [*sic*] and `Antibodies`; the antibody block is duplicated verbatim in both.

### D.1 Primary antibodies — verbatim, all columns as printed

| Name of the antibody | Dilution used | Catolog No [*sic*] | Source |
|---|---|---|---|
| Mouse anti-CC1 | 1:50 | `OP80` | Millipore |
| 🎯 **Rabbit anti-WWOX** | **1:5000** | 🔴 **`N.A`** | 🔴 *(column empty)* |
| Rat anti-PDGFRα | 1:500 | `558774` | BD Pharmingen |
| 🎯 **Mouse anti-NeuN** | 1:500 | 🎯 **`MAB377`** | Millipore |
| Mouse anti-CNP | 1:1000 | `N.A` | Peles lab |
| Rabbit anti-MBP | 1:100 | `Ab65988` | Abcam |
| Mouse Anti-Tuj1 | 1:1000 | `801202` | Bio legend |
| Rabbit anti-NG2 | 1:500 | `AB5320` | Millipore |
| Rabbit anti-GFAP | 1:1000 | `MAB360` | Millipore |
| Rat anti-Neurofilament H | 1:100 | `MAB5448` | Millipore |

### D.2 Secondary antibodies — verbatim, and this is the finding

| Name of the antibody | Dilution used | Catolog No | Source |
|---|---|---|---|
| Goat anti-Mouse IgG, alexa fluor 488 | 1:1000 | `A11029` | Invitrogen |
| Goat anti-Mouse IgG, alexa fluor 647 | 1:1000 | `A21244` | Invitrogen |
| Donkey anti-Rat IgG, conjugated with Cy5 | 1:500 | `712-175-150` | Jackson Immuno Research |

🔴 **That is the entire secondary list. There is no anti-rabbit secondary of any kind.**

**`DATO`.** Four of the ten primaries are **rabbit** — anti-WWOX, anti-MBP, anti-NG2, anti-GFAP — and every
one of them is imaged in a published panel of this paper (Suppl. Fig. 1A/B/F, Fig. 4B/D, Suppl. Fig. 5A/D,
Suppl. Fig. 6A/C). **No secondary in the table can detect any of them.**

🎯 **`INFERENZA`. Supplementary Table 3 is incomplete, and the incompleteness is demonstrable from the paper's
own figures rather than from an outside expectation.** This is a strictly stronger statement than the usual
*"the Methods do not say"*: it is not that the reagent is unnamed, it is that the published images **prove a
reagent was used which the table omits**. It is the same authorial-omission class as `B2`, in the same
laboratory, in a third paper. 🔴 **I did not guess which anti-rabbit secondary it was, and no vendor page was
consulted** (`EGRESS_BLOCKED`).

### D.3 🔴 Three host/catalogue concordance flags — raised, NOT resolved

Millipore's `MAB` prefix denotes a mouse monoclonal. The table assigns:

| Row | Host as printed | Catalogue as printed | Flag |
|---|---|---|---|
| anti-NeuN | Mouse | `MAB377` | 🟢 concordant |
| anti-GFAP | 🔴 **Rabbit** | `MAB360` | 🔴 **prefix–host mismatch** |
| anti-Neurofilament H | 🔴 **Rat** | `MAB5448` | 🔴 **prefix–host mismatch** |

🔴 **This is a flag, not a finding, and it is NOT used anywhere below.** Resolving it requires a vendor
datasheet; every vendor datasheet is `EGRESS_BLOCKED` in this deployment (`B7`), and this laboratory has
already had to quarantine one instance of asserting what an unreachable datasheet "should" contain. 🔴 **If
either mismatch is real, the host assignment in the table is wrong and the secondary arithmetic in § D.4
changes.** Recorded as `HUMAN_REQUIRED`: one person, one browser, three minutes.

⚠️ There is an internal cross-check that is *suggestive* and still not decisive: a `Rat anti-PDGFRα` and a
`Rat anti-Neurofilament H` would both be served by the single `Donkey anti-Rat Cy5`, which is consistent — so
the `Rat` assignment on `MAB5448` is at least self-consistent within the table. `MAB360`'s `Rabbit`
assignment has no such internal support, because no anti-rabbit secondary exists at all.

### D.4 Channel arithmetic — what this table permits and forbids

Taking the table **as printed**, and adding the anti-rabbit secondary the figures prove exists:

| | |
|---|---|
| Mouse primaries | CC1, NeuN, CNP, Tuj1 — **four**, served by **two** anti-mouse secondaries (AF488, AF647) |
| Rabbit primaries | WWOX, MBP, NG2, GFAP — **four**, served by **zero** listed secondaries |
| Rat primaries | PDGFRα, NF-H — **two**, served by **one** (Cy5) |
| Nuclear counterstain | 🔴 **NONE.** No DAPI, no Hoechst, no TO-PRO in the table, and the IF Methods name none |

🔴 **Two mouse secondaries in different channels is a real difference from the EMBO/2026 archive**, where
`B4` records *"three channels exist, ever"* with **one** anti-mouse and **one** anti-rabbit. Here, two mouse
primaries **can** be separated (one at 488, one at 647) — but only if they are applied sequentially, and the
table gives no sequential protocol. 🟡 Taken at face value, the table as printed cannot produce the published
`CC1 (green) + NG2 (magenta)` panel of Suppl. Fig. 6A (mouse + rabbit, and no anti-rabbit exists), nor the
`CNP (green) + MBP (magenta)` panel of Fig. 4B (same problem). **The table is under-specified relative to its
own figures, and that is the honest summary.**

🎯 **What it DOES settle, and settles cleanly:** the § C.4(iii) question. Suppl. Fig. 1B is
`Rabbit anti-WWOX` + `Mouse anti-NeuN MAB377`. `MAB377` is A60. **The paper's only cerebellar WWOX image is
Purkinje-blind in its identity channel, by the same reagent, for the same reason, as the EMBO/2026 archive.**
`B3` is confirmed in a second, independent paper.

🔴 **And the `P4` collision survives unchanged.** Calbindin-D28k's workhorse clone (CB-955) is a **mouse**
monoclonal; NeuN `MAB377` is a **mouse** monoclonal. They cannot share a section. The cross-calibration from a
calbindin stain back to the existing NeuN-gated panels still costs a **third** measurement — exactly as
[`tx007_purkinje_frontier_20260922.md:348`](tx007_purkinje_frontier_20260922.md) `P4` already states. 🟢 **That
is a confirmation of the repository's prior arithmetic, not a correction of it.**

### D.5 🔴 WHAT I CHANGED IN `wwox_antibody_epitope_census_20260922.md`, AND WHY

Four edits, all additive, all in place, none removing or rewriting a prior row's verdict.

| # | Edit | Why |
|---|---|---|
| **1** | **Row `A14`** — source column now also cites this paper's Supplementary Table 3, and the catalogue cell now records that the authors themselves print **`N.A`** | `A14` previously rested on `repo-held` secondary attestations from two *other* papers. The Brain 2021 reagent table is a **third, independent, primary-source** attestation of the same reagent at the same IF dilution (**1:5000**, matching `A14`'s recorded `1:5,000`), and — decisively — it shows the authors writing `N.A` in a `Catolog No` column they filled in for nine other antibodies. The absence is now **declared by the source laboratory**, not inferred by us |
| **2** | **Blocker `B2`** — upgraded from inference to authorial declaration, with the new locator | `B2` argued the omission was *"the authors', not the extractor's"* from the shape of the damage. That argument is now unnecessary: the authors print `N.A`, in a structured `.xlsx` with no text layer to corrupt. `B2` gets stronger and stops depending on a forensic inference |
| **3** | **Blocker `B3`** — second independent confirmation added (`MAB377`, 1:500, Millipore, Supplementary Table 3), with its new consequence: Suppl. Fig. 1B, the cerebellar WWOX panel of `PMID 33914858` | `B3` was sourced to `full_text_queue_current.md:6723` and bore only on the EMBO/2026 transduced-fraction arithmetic. It now bears on a *second* paper's cerebellar panel |
| **4** | **New blocker `B14`** — *the secondary-antibody list of `PMID 33914858` cannot account for four rabbit primaries that appear in its own published figures* | This is a new blocker class and it has no home in the existing table. It is the § D.2 finding |

🔴 **What I did NOT change:** no row `A1`–`A20` verdict, no count in § 1.1, no epitope cell, no § 2 design
verdict, no `≤`/`<`, no §§ 4–7. The anti-WWOX of this paper is `A14` and is **not** a new census row — same
laboratory, same host, same clonality, same IF dilution, and adding a row would inflate the `17` denominator
that §§ 2.1 and 4.2 are built on. 🔴 **No epitope was gained.** `A14` remains `UNSTATED` on epitope, and the
`0 / 17 wholly C-terminal to 230` headline is **untouched**.

### D.6 Primers — `Primer Squence` sheet, 19 pairs

**Mouse, 13 pairs (F/R):** `Sox10` · `Pdgfra` · `Cspg4` · `Olig1` *(the reverse primer is labelled
`m-Oilg1-R` — transposition in the authors' own sheet, recorded as read)* · `Olig2` · `Nkx2-2` · `Myrf` ·
`Mbp` · `Cnp` · `Mag` · `Mal` · `Mobp` · `Plp1`.

**Human, 6 pairs (F/R):** `SOX10` · `CSPG4` · `PDGFRA` · `MYRF` · `MBP` · `CNP`.

Sequences are held verbatim in the workbook and are not reproduced here in full; two representative rows, as
printed: `m-Mbp-F  TCACAGCGATCCAAGTACCTG` / `m-Mbp-R  CCCCTGTCACCGCTAAAGAA`.

🔴 **Two gaps in the primer table, both earned zeros against the sheet's own contents as positive control
(19 pairs enumerated, 38 oligo rows read):**

1. **There is no `Wwox` primer pair.** The paper's qPCR panels are oligodendrocyte/myelin genes only. Any
   `Wwox` transcript quantity in this paper comes from RNA-seq (§ E), not from qPCR.
2. **There are no housekeeping primers**, although the Supplementary Methods state *"All measurements were
   performed in triplicate and were standardized to the levels of either **HPRT or UBC**."* The normaliser is
   named; its primers are not given. 🟡 Minor, but it means the qPCR panels are not fully reproducible from
   the supplied table — and *"either HPRT or UBC"* does not say which panel used which.

---

## E · EXPRESSION DATASETS `File012` / `File013` — IDENTIFICATION ONLY

🔴 **NO differential-expression mining was performed.** Headers, sheet names, sample-column names and row
counts were read; no fold change was ranked, no gene list was derived, no enrichment was run. The single
numeric value quoted below (`Wwox` log2FC in `File013`) is read off the identification pass as a
**sanity/orientation check on the cohort**, and is flagged as such.

### E.1 Assignment to the published supplementary tables — stated by the authors

| Local artefact | Sheet name, verbatim | = | Authors' own words |
|---|---|---|---|
| `…_suppl_File012.xlsx` | `SKO_vs_S_Crtl_6_6_Crtx,hippo` | **Supplementary Table 1** | *"we performed bulk RNA sequencing (RNA-seq) from whole cortex and hippocampi of S-KO and S-Control mice at P17. Our analysis revealed a total number of 730 upregulated and 579 downregulated genes (P-value <0.01, fold change >1.5; **Supplementary Table 1**)"* |
| `…_suppl_File013.xlsx` | `KO_WT_7_vs_7_unBatch` | **Supplementary Table 2** | *"we performed bulk RNA-seq on whole hippocampal tissues from the Wwox-null and N-KO models and compared them with the S-KO model (**Supplementary Table 2**)"* |
| `…_suppl_File014_reagents.xlsx` | `Primer Squence` / `Antibodies` | **Supplementary Table 3** | *"All antibodies and primer sequences … are provided in **Supplementary Table 3**"* |

### E.2 `File012` — Supplementary Table 1

| | |
|---|---|
| **Comparison** | `S-KO` vs `S-Control` — Synapsin1-Cre conditional only. **No `N-KO`, no `Wwox`-null** |
| **Tissue** | Cortex **and** hippocampus, pooled into one contrast (`Crtx,hippo`), with Limma batch correction (*"Where batch effect is expected (in case of two different tissues) the Limma tool is applied"*) |
| **Age** | 🟢 **P17**, stated in the Results |
| **n** | 🔴 **6 vs 6, and the tissue split is ASYMMETRIC.** `S-KO`: 3 cortex + 3 hippocampus. `S-Control`: **4 cortex + 2 hippocampus**. This is visible only in the column names and is not stated anywhere in the paper |
| **Rows** | **16,054** genes (+ 1 header) |
| **Columns** | **30**: `ensg`, `symbol`, `EntrezID`, `pvalue`, `padj`, `log2FoldChange`, `l2fcShrink`, `description`, `type`, `chr`, `start`, `end`, `strand`, `baseMean`, **12 per-sample `*_NrmlCount` columns**, `lfcSE`, `stat`, `ENStID`, `RefSeqID` |
| **Sample columns, verbatim** | `S-KO1_Cortex` · `S-KO2_Cortex` · `S-KO3_Cortex` · `S-KO1_Hippo` · `S-KO2_Hippo` · `S-KO3_Hippo` · `S-Ctrl1_Cortex` · `S-Crtl2_Cortex` [*sic*] · `S-Ctrl3_Cortex` · `S-Crtl4_Cortex` [*sic*] · `S-Ctrl1_Hippo` · `S-Ctrl2_hippo` — all suffixed `_NrmlCount` |

### E.3 `File013` — Supplementary Table 2

| | |
|---|---|
| **Comparison** | 🎯 **All three mutant models pooled vs all three control sets**, 7 vs 7 |
| **Mutants (7)** | `KO1_Hippo`, `KO2_Hippo` (`Wwox`-null) · `N-KO1_hippo`, `N-KO2_Hippo` (Nestin-Cre) · `S-KO1/2/3_Hippo` (Synapsin1-Cre) |
| **Controls (7)** | `WT1/2/3_Hippo` · `N-Crtl1_Hippo`, `N-Ctrl2_Hippo` · `S-Ctrl1_Hippo`, `S-Ctrl2_Hippo` |
| **Tissue** | 🟢 **Hippocampus ONLY** (single tissue ⇒ `unBatch`, no Limma correction needed) |
| **Age** | 🟢 **P17** — Suppl. Fig. 4A legend: *"from hippocampi (total n = 14) collected at P17"* |
| **Rows** | **17,042** genes (+ 1 header) |
| **Columns** | **30**: as `File012` but with **14 per-sample `*_NrmlCount` columns** and **without** `ENStID` / `RefSeqID` |
| **Cross-check** | 🟢 The 14 columns match the Suppl. Fig. 4A legend exactly: *"wildtype (n = 3), N-Control (n = 2), S-Control (n = 2) with Wwox null (n = 2), N-KO (n = 2), S-KO (n = 3) … (total n = 14)"* |
| **Orientation check** | `Wwox` is the **2nd-ranked row** by *P*-value: `log2FoldChange −3.14`, `padj 2.51E-28`. 🟢 The contrast is doing what it says |

### E.4 Platform — identical for both, from the Supplementary Methods, verbatim

> *"Multiplex samples Pool (1.5pM including PhiX 1%) was loaded in **NextSeq 500/550 High Output v2 kit
> (75 cycles)** cartridge (Illumina) and loaded on **NextSeq 500 System** (Illumina), with 75 cycles and
> **single-Read** Sequencing conditions. Raw FASTQ files are filtered and trimmed with **trim_galore** …
> applying min quality of 20. Reads shorted [sic] than 20 are discarded. Reads are next mapped to **mm10**
> transcriptome with **Salmon**. Differential genes are analyzed with **DESeq2**. Prior to analysis, genes
> are filtered for minimum of 10 reads … Both Log2 Fold Change (L2FC) and a conservative shrinked-L2FC are
> calculated with default parameters. Where batch effect is expected (in case of two different tissues) the
> **Limma** tool is applied. **Alpha parameter (FDR) is set at its default of 0.1.** A maximum Log2 fold
> change of 1.1 is applied to lfcSE…"*

Library prep: KAPA Stranded mRNA-Seq Kit with mRNA Capture Beads (`KK8421`). Sequencing performed by the
Genomic Applications Laboratory, Hebrew University.

### E.5 🎯 NO DATA-AVAILABILITY STATEMENT AND NO ACCESSION — earned zero

| Positive control (raw HTML, `grep -o -F`) | count | | Query | count |
|---|---|---|---|---|
| `Wwox` | 115 | | `Data availability` / `data availability` | 🔴 **0** |
| `Funding` | 1 | | `accession` | 🔴 **0** |
| `Acknowledg` | 2 | | `GSE` | 🔴 **0** |
| `Competing interests` | 1 | | `Gene Expression Omnibus` / `GEO` | 🔴 **0** |
| | | | `SRA` / `ArrayExpress` | 🔴 **0** |

**`DATO`. This paper deposited nothing and says nothing about depositing.** 🎯 **These two `.xlsx` files are
therefore the ONLY public form of this RNA-seq dataset in existence** — there is no accession to fetch, no
FASTQ, no count matrix anywhere else. That raises their value sharply and makes their local retention a
standing asset rather than a convenience. 🔴 It also caps what they can ever yield: **per-sample normalised
counts and DESeq2 summary statistics, and nothing below that**. No re-alignment, no isoform analysis, no
alternative model, no cell-type deconvolution from raw data.

### E.6 THREE cheap, high-value queries these tables could answer — `DATASET AVAILABLE / NOT YET MINED`

> 🔴 **Each of the three is a specification of a step, never a report of having taken it. None was run.**

| # | Query | The existing open question it serves | Why it is cheap | Bound |
|---|---|---|---|---|
| **Q1** 🥇 | Read the **`Wwox` row of `File013`** across its 14 per-sample columns and report residual `Wwox` transcript **per genotype separately** — `Wwox`-null vs `N-KO` vs `S-KO`, each against its own control | 🎯 **The allele-severity ladder.** This repository's cardinal rule is that these three are different objects; the paper pools all seven mutants into one contrast and reports a single `log2FC −3.14`, which is a statement about none of them. The per-sample columns **un-pool it for free** | One row, 14 cells, already parsed. Zero compute | 🔴 It is *transcript*, not protein, and a floxed-exon deletion can leave a stable truncated transcript. A residual count is **not** residual WWOX |
| **Q2** | Read the **same myelin gene panel in `File013` split by genotype** — `Mbp`, `Plp1`, `Cnp`, `Mobp`, `Mag`, `Mal`, `Myrf`, `Sox10`, `Pdgfra`, `Cspg4`, `Olig1`, `Olig2`, `Nkx2-2` (the exact 13 the authors qPCR'd, § D.6) — and ask whether the hypomyelination signature is **equally deep in `N-KO` and `S-KO`, or graded** | 🎯 Whether the myelin phenotype tracks the *breadth* of deletion (Nestin ⊃ Synapsin) or is saturated in both. Bears directly on `CLAIM 003`'s mechanism limb and on whether a neuron-restricted intervention could be sufficient | 13 rows × 14 columns from a parsed sheet. The gene list is **given by the authors' own primer table**, so it is not a fishing expedition | 🔴 n = 2 or 3 per genotype. This can rank, it cannot test. Any result is `IPOTESI`, never `DATO` |
| **Q3** | Cross-tissue check in **`File012`**: for the same 13-gene panel, compare the 6 cortex columns against the 6 hippocampus columns **within `S-KO`** | 🎯 The repository holds no cortex-vs-hippocampus contrast for the myelin programme in any `Wwox` model, and the paper deliberately erased it with Limma. The per-sample columns **restore what the batch correction removed** | Already-parsed columns; no model refit | 🔴 The control arm is **4 cortex + 2 hippocampus** (§ E.2), so the hippocampal control is n = 2. And these are `_NrmlCount` values *after* DESeq2 normalisation on a Limma-corrected design — using them for a contrast the design was corrected to remove is **methodologically loaded** and must be declared if ever run |

🔴 **STATUS: `DATASET AVAILABLE / NOT YET MINED`.** No mining is proposed as an action of mine and no result is
claimed. `Q1` is the only one that is close to free and close to decisive; `Q2` and `Q3` both run into n ≤ 3.

---

## F · VIDEOS — caption mapping

### F.1 The two captions exist, verbatim from the main text

> *"Furthermore, **N-KO** mice showed tremors/seizures (**Supplementary Video 1**) and ataxia (lack of
> coordination in hind limb clasping test) as observed in Wwox-null mice (Supplementary Fig. 2A and B)."*

> *"**S-KO** mice also exhibited uncontrolled spontaneous tonic-clonic seizures beginning at P9 and ranging
> from several seconds to a few minutes (**68.5 ± 13.4 s; n = 6 of P14–18**) (**Supplementary Video 2**)."*

Methods: *"Mice undergoing spontaneous seizures were recorded using a mobile camera, when monitoring the mice
at the animal facility. Spontaneous seizures or abnormal activity (wild running) were observed in Wwox mutant
mice (Supplementary Videos 1 and 2). Duration of spontaneous seizures (in seconds) was calculated and
presented, n = 6."*

### F.2 🔴 The file-to-caption mapping is NOT stated anywhere in the bundle

The HTML exposes the supplement as a **single archive** — one link, `awab174_supplementary_data.zip`,
repeated in every supplementary widget. 🔴 **There is no per-file caption, no per-file label and no manifest**
in the HTML, and the supplement PDF's legend block contains no video legends (its legends run
Fig 1, 2, 4, 5, 6, 7, 8, 9 — see § F.4).

Container metadata read from the `mvhd` atom of each file (stdlib, no decode, no frame inspected):

| File | Size | `ftyp` | timescale | duration | seconds |
|---|---|---|---|---|---|
| `…_File010.mp4` | 8.31 MB | `mp42` | 48,000 | 354,302 | **7.38 s** |
| `…_File011.mp4` | 2.07 MB | `mp42` | 48,000 | 717,822 | **14.95 s** |

🔴 **Durations do not disambiguate.** The only published duration is `68.5 ± 13.4 s`, which is a **mean
seizure duration across n = 6 animals**, not the length of either clip; neither 7.38 s nor 14.95 s matches it
and neither is expected to. Note also that the **larger file is the shorter clip**, so size is not a proxy
for content either.

**`INFERENZA`, weak, and labelled as such.** OUP's supplementary files are served in sequence
(`File009` = supplementary methods + figures, `File012`/`File013`/`File014` = Supplementary Tables 1/2/3 in
order — a mapping § E.1 confirms independently against the authors' own text). By that ordinal alone,
`File010` → **Supplementary Video 1** (`N-KO`) and `File011` → **Supplementary Video 2** (`S-KO`).

🔴 **This is an inference from filename ordinal, not a datum. It is UNVERIFIED and must not be cited as the
mapping.** Verifying it requires opening the clips, which § F.3 declines.

### F.3 Stopped, as instructed

🔴 **No video analysis was performed.** No frame was decoded, no seizure was scored, no behaviour was
assessed, no duration was measured from content. Only the ISO-BMFF container header was read.

### F.4 One supplement-integrity finding, surfaced by the same pass

🔴 **The legend for Supplementary Fig. 3 is MISSING from `File009`.** The legend block runs
`Supplementary Fig 1` → `Fig 2` → **`Fig 4`** → `Fig 5` → `Fig 6` → `Fig 7` → `Fig 8` → `Fig 9`.
Earned zero: `grep -o -a "Supplementary Fig 3"` returns 0 against a positive control of 9 for
`Supplementary Fig` on the same surface and the same invocation.

Supplementary Fig. 3 **is** cited in the main text, once, and it is load-bearing for the paper's central
electrophysiological claim:

> *"These bursts were not observed in subcortical structures, suggesting a neocortical origin of burst
> generation (**Supplementary Fig. 3**)."*

🔴 **Consequence:** the figure asserting that hyperexcitability is *neocortical in origin* rather than
subcortical has **no legend in the supplementary bundle we hold** — so its n, its ages, its recording depths
and its genotypes are all `NOT STATED` in every surface available here. ⚠️ Whether the *image* is present in
`File009` was not determined: the PDF uses compressed object streams that this deployment cannot enumerate
(no `pymupdf`/`poppler`), so page-level inspection is 🔴 `TOOLING-BLOCKED`, not absent. Recorded as an open
item, not as an accusation of omission by the publisher.

---

## G · WHAT THIS FILE DOES AND DOES NOT CLAIM

### G.1 Not claimed

1. 🔴 **No receipt was recorded and no `complete_fulltext_read` is asserted.** This is a bundle ingestion and a
   surface adjudication. It reads the whole main text and the whole supplementary legend block, but it does
   **not** perform the locator-by-locator deep read that `CLAIM 003` would need, and it does not touch
   `fulltext_receipts.py`.
2. 🔴 **Nothing about `CLAIM 003` is revised, narrowed, reversed or confirmed here.** The claim is a
   `consolidated baseline`; per `legend-locator-audit`, a reading that touches one requires a blind
   adversarial audit of its locator triples, which has not been run.
3. 🔴 **No supplementary figure IMAGE was examined.** Every § C statement rests on legends and the reagent
   table. Whether the Purkinje monolayer is in frame in Suppl. Fig. 1B is **`NOT YET READ`** (§ C.5).
4. 🔴 **No differential expression was computed** (§ E).
5. 🔴 **No video content was examined** (§ F.3).
6. 🔴 **No vendor datasheet was consulted**; the § D.3 host/catalogue flags are unresolved by design.

### G.2 `REVIVAL_TRIGGER`

| Trigger | What it would reopen |
|---|---|
| A reader opens **Suppl. Fig. 1B** at measured effective ppi | § C.4(iv) row 3 and § C.6 `A-f1` — becomes a reading, not a specification |
| The **anti-rabbit secondary** of `PMID 33914858` is identified (author correspondence, or a vendor page) | § D.2 / new blocker `B14` |
| `MAB360` or `MAB5448` host is confirmed from a datasheet | § D.3, and the § D.4 arithmetic if either flips |
| **Supplementary Fig. 3**'s legend is obtained (publisher, author, or a page-level read of `File009` once a PDF page-enumerator exists in this deployment) | § F.4 — the neocortical-origin claim's parameters |
| A **PDF page-level tool** (`pymupdf`/`poppler`) becomes available | § F.4 `TOOLING-BLOCKED`; and § A.8's ppi bound on the browser-print PDF |
| `PMID 33914858` is next written into a queue or registry | § B.3 — it enters as **Repudi 2021** |

### G.3 `HUMAN_REQUIRED`

- Correcting the short-form attribution at the point of next queue/registry entry (§ B.3). **I edited no queue,
  no registry, no `*_current.md` and no ledger.**
- Any vendor-datasheet lookup (§ D.3).
- Any contact with the authors regarding the missing Suppl. Fig. 3 legend or the missing secondary antibody.
  🔴 **No correspondence was drafted, prepared or sent.**

---

## H · SOURCES READ IN THIS ACT

🟢 **Read first-hand, in full or at the cited section, this act:**
`files/fulltext/PMID33914858_Repudi2021_OUP.html` (whole article body + all metadata) ·
`…_OUP_browserprint.pdf` (text layer, whole) · `…_suppl_File009_methods_figures.pdf` (text layer, whole) ·
`…_suppl_File012.xlsx` · `…_suppl_File013.xlsx` · `…_suppl_File014_reagents.xlsx` (all sheets, all rows) ·
`…_suppl_File010.mp4`, `…_File011.mp4` (container headers only) ·
`framework/eval/finding_20260809_text_surface_fidelity.md` (whole) ·
`framework/master/gold_is_in_the_details.md` § 5d ·
`disease-models/wwox/analysis/tx007_purkinje_frontier_20260922.md` ·
`disease-models/wwox/analysis/ataxia_without_cerebellar_lesion_20260922.md` ·
`disease-models/wwox/analysis/wwox_antibody_epitope_census_20260922.md` ·
`framework/state/state_manifest_current.md` (`current_state: READY` confirmed at line 159).

🔴 **SIBLING-ATTESTED, not re-derived:** `MAB377` = NeuN clone A60 and A60's Purkinje-negativity (`B3`) ·
the EMBO Mol Med 2021 / `PMID 34747138` vector and transduced-fraction material · every `A-s*` and `A-f*`
row of `tx007_purkinje_frontier_20260922.md`.

🔴 **NOT consulted:** PubMed, PMC, Europe PMC, any vendor page, any external host. **Network blocked; nothing
was downloaded.**
