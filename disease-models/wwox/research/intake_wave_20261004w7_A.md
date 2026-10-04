context_policy: SOURCE_FIRST

# Intake wave 7 — 2026-10-04 — Scientist A: in which named cell type is WWOX actually assayed?

- **Actor:** ACTOR_ID `scientist` (Scientist A), branch `task/sci-A-20261004w7`, dispatched by the Orchestrator under the standing authorisation of 2026-09-28.
- **Assigned list (6):** `PPR960425` · `PPR1260670` · PMID 32368285 · PMID 42558002 · PMID 40937943 · PMID 33958783.
- **Read (4):** PMID 32368285 · PMID 42558002 · PMID 40937943 · PMID 33958783. **Two were duplicates of records LEGEND already holds** and were not re-read; the dedup evidence is in § 2.
- **Method:** all four acquired as JATS XML — three from Europe PMC, one (PMID 33958783) from NCBI efetch after Europe PMC returned HTTP 500. Figures were acquired where a number carried here lives in a panel: the publisher's CC BY PDF for PMID 32368285 (no image route resolved) and the PMC author-manuscript instance bin for PMID 33958783. First-pass notes were written before any registry record about a paper was opened.
- `FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON` — admitted afterwards: `registry_records.py get` for the four PMIDs and for `DL-MOL-003`, `CLAIM 005`, `CLAIM 019`, `CORPUS-STUB-132`; the wave-6 note and candidate `CC-20261003W6-A-WNT-01`; and the two held primaries used to check the review (PMID 34268881, PMID 33914858).
- **Not medical advice.**

## 1 · Question assigned

> What does each source add to, or limit in, the claim that loss of WWOX has a cell-autonomous, measurable consequence in a *named* cell type — human neural progenitor, astrocyte, oligodendrocyte — and in which of them is WWOX actually assayed rather than inherited from a gene list?

## 2 · Dedup first — two of the six were already held

### A2 · `PPR1260670` = PMID 42395553 — **DUPLICATE, confirmed byte-level**

The bioRxiv preprint assigned as A2 and the record LEGEND read in wave 1 are the same manuscript, same version:

| check | result |
|---|---|
| DOI | `10.64898/2026.06.24.734331` on both |
| title | *WWOX contributes to DNA damage, but not somatic instability in Huntington's disease* on both (`pdfinfo`) |
| pages | 39 on both |
| version banner | "this version posted June 26, 2026" on both |
| bytes | the two PDFs differ in **53 bytes** out of 8 883 738 |
| extracted text | `diff` of `pdftotext -layout -nopgbrk` output: **identical, zero lines** |

The 53 differing bytes are PDF object metadata; the page content is the same document. LEGEND already holds it as `PMID42395553_Petrozziello2026_bioRxiv.pdf` with a receipt on the ledger and the dossier `fulltext_dossiers/PMID42395553.md`. **Verdict: DUPLICATE — not re-read.**

**What a re-read could still add, if the Orchestrator wants it:** the held reading is `partial_fulltext_read` and its own receipt names what it owes — `figures: captions_only` and `supplementary: not_read`. A resumed reading of the figure panels and the supplement would close that gap; a re-read of the body would add nothing. Note also that the held artefacts are **declared-and-absent** in this checkout (`paper_packet.py packet --pmid 42395553` reports 0 present, 2 declared-and-absent), while the root corpus does hold the PDF and its text layer — the manifest's digest for the PDF (`90078770…`) is the copy on disk, and the copy fetched today has digest `81ebb9fc…`, so a resumed reading must use the declared artefact, not a fresh download.

### A1 · `PPR960425` = the preprint of PMID 42397075 — **DUPLICATE of a paper already read in full**

The brief's selection record states that no published version exists in MED ("title search, 0 hits"). **That premise is wrong.** The preprint *WWOX deficiency impairs neurogenesis and neuronal function in human organoids* (bioRxiv `10.1101/2024.12.22.630016`, posted 2024-12-25, 36 pages, Steinberg, Zonca, Rosh, Kustanovich, Maroun, Stern, Davila-Velderrain, Aqeilan) was published as **PMID 42397075**, *Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids*, Brain 2026, DOI `10.1093/brain/awag239` — same first authors, same corresponding authors, same cohort, same conclusions, with the CRISPR-edited isogenic knockout line named explicitly in the published abstract.

LEGEND **has read the published version in full**: `fulltext_receipts.py status --pmid 42397075` returns four receipts, depth `complete_fulltext_read`, chain ok, with a 30-locator schema-v2 manifest. **Verdict: DUPLICATE (earlier version of a completely-read record) — not read.**

**What a re-read could add:** only a version diff. The published paper adds the MYC mechanism to the title and names the isogenic knockout; a preprint-versus-published comparison would show what the review process changed, which is a harness question (claim stability across versions), not a WWOX question. I did not do it, because the wave's priority is allele-class function measured, and the published version is already read at full depth.

**Time released by the two dedups went to the other four**, including figure-panel work on two of them.

## 3 · Per paper

| PMID | Verdict | Is WWOX *measured*, and in what? | What is new versus held | Receipt (prepared) | Candidates |
|---|---|---|---|---|---|
| 32368285 (Celebi 2020) | **INGEST** | Yes — transcript and protein in **human epithelial cells**; siRNA knockdown. No neural cell. | The assay behind LEGEND's Dvl direction, read at last: it measures **no Wnt output at all**, the silencing is in a non-cancer oesophageal line, and the blot behind the title is not shown. | `sciA_32368285_1.json` (partial) | DVL-01, REGISTRY-01 |
| 42558002 (Lange 2026) | **INGEST** (background) | No — a review; every WWOX row re-describes a held primary. | An independent group marks **all four** WWOX models `Unclear` on cell autonomy and states the astrocyte phenotype is downstream of neuronal dysfunction. | `sciA_42558002_1.json` (complete) | ASTROCYTE-01, REGISTRY-01 |
| 40937943 (Ramirez 2025) | **INGEST** | Yes — transcript in **named human oligodendrocyte-lineage cells** (iOPC, iOL), by snRNA-seq. | The model's first quantified WWOX datum in that lineage; but what varies is donor ancestry, not WWOX dose, and the statistics are nucleus-level. | `sciA_40937943_1.json` (partial) | REGISTRY-01 |
| 33958783 (Liu 2021) | **INGEST** | Yes — transcript in **laser-captured human dopamine and pyramidal neurons** (cited panel), plus GTEx bulk. | Wave 6's named reading debt, discharged. The authors call the WWOX signal **suggestive**; and the panel contradicts the paper's own "specifically in … neurons" sentence. | `sciA_33958783_1.json` (partial) | NEURONSPEC-01, REGISTRY-01 |

Receipt files are in the Orchestrator's scratch `receipts_pending_w7/`; none is appended to the real ledger. All four were dry-recorded **in event order** into a throwaway copy of the ledger together with a copy of the state manifest taken from `main`: four `RECORDED`, exit 0 each, `verify` OK at 379 chained receipts, and `git status` empty for `framework/state/` and `disease-models/wwox/registries/` afterwards.

## 4 · Patients counted once

No patient-level record is added by any of the four: one epithelial cell paper with an anonymous 98-pair tumour series (no individual data), one review, one iPSC panel and one adult Parkinson's cohort. The review re-describes patient-derived organoid lines LEGEND already holds through their primaries; no new WWOX-DEE patient enters the census, and no overlap check was needed.

## 5 · Answer to the question, with its limits

**Where WWOX is actually assayed in a named cell type, across this group:**

| Named cell type | assayed here? | by what | what it supports |
|---|---|---|---|
| human neural progenitor / radial glia | **no source in this group** | — | nothing; the organoid evidence is in the duplicate (PMID 42397075), already read |
| astrocyte | **no** | the review carries no astrocyte-intrinsic WWOX experiment; it marks all four rows `Unclear` | the cell-autonomy question is open, and an independent group says so |
| oligodendrocyte / OPC | **yes, transcript only** | snRNA-seq of iPSC-derived iOL and iOPC (PMID 40937943) | a baseline-abundance and baseline-variance fact (≈1.3-fold between donor backgrounds), not a consequence of WWOX loss |
| dopamine and pyramidal neuron | **yes, transcript only** | laser-capture RNA-seq panel (PMID 33958783) | WWOX is detectable but **not** neuron-enriched — PBMC and fibroblast medians sit at or above the neuronal ones |
| epithelial cell (non-neural) | **yes, transcript and protein** | qPCR and fractionation immunoblot after siRNA (PMID 32368285) | the only perturbation experiment in the group, and it is epithelial |

**So the answer is uncomfortable and specific:** in this group of sources, WWOX is *perturbed* only in an epithelial cell line, and it is *measured* in neural cell types only as baseline transcript abundance. **Not one source here measures a consequence of WWOX loss in a named neural cell type.** The cell-autonomy question is carried, for the whole corpus, by one conditional-knockout experiment (PMID 33914858) whose astrocyte and oligodendrocyte arms are negative on three gross organismal measures — developmental delay, weight loss, postnatal lethality — and were not tested for astrocyte function, seizures or network behaviour. An independent review reading the same material reaches the same open verdict and marks it `Unclear` four times.

**Limits of this answer:**
- Three of the four readings are `partial_fulltext_read`, each for a stated reason (one unresolvable gene-direct hop; figure panels as captions; supplementary data not fetched).
- The strongest human-cell functional evidence for the question is in the record that was a duplicate (PMID 42397075) and was therefore not re-read here.
- Two of the three cancer-cell primaries behind the Dvl direction remain unread and closed access (PMID 19465938, PMID 23030478).

## 6 · What would change the model, and what would falsify it

**Would change it:**
- A cell-type-conditional WWOX knockout assayed for *function* rather than for gross phenotype — astrocyte calcium or potassium buffering, oligodendrocyte myelination, in the G-KO and O-KO animals that already exist. The negative LEGEND relies on is a negative for weight and survival, and nothing stops that experiment being done on the same lines.
- A WWOX perturbation in any neural cell type with a Wnt transcriptional readout (β-catenin or TCF/LEF). Every source in this wave that touches the Dvl axis infers that step; none measures it.
- A cell-type-resolved human WWOX expression dataset holding neurons, astrocytes and oligodendrocytes in one assay with donor-level replication. Two of this wave's sources each supply one cell class and neither can be compared with the other.

**Would falsify the direction LEGEND carries:**
- For the Wnt lever: a WWOX-null neural system with nuclear DVL and *reduced* TCF/LEF activity — the pattern wave 6 already found under a different perturbation.
- For the glial axis as a modifier: astrocyte-conditional WWOX deletion producing a measurable astrocyte functional deficit would turn the "downstream of neuronal dysfunction" reading, which this wave's review states and this wave's evidence does not establish, into an error.

## 7 · Premises in the brief found wrong

1. **A1 is not unpublished.** "No published version exists in MED (title search, 0 hits)" — the published version is PMID 42397075 (Brain 2026), and LEGEND has read it at `complete_fulltext_read` with four receipts since 2026-08-10. The selection's own criterion ("unread by construction") is false for this item.
2. **A4's attribution is wrong in two places.** The selection writes "`Wwox^P47T/P47T` (Steinberg 2021)"; in the review's Table 1 the P47T model belongs to **Hussain 2023**, and the Steinberg 2021 row is the human organoid model. The selection also says the review has "no oligodendrocyte arm" — its Repudi row does list the Olig2-Cre knockout, although the narrative never discusses oligodendrocytes.
3. **A5's effect sizes need their rows.** "−1.33 to −1.34" are paired in Table 1 with an "increased in" column naming AF and EU, so the sign cannot be read without the comparison; and the paper's own sentence introducing them miscounts, saying "only five AD GWAS hits" before naming six genes.
4. **A2's "same record?" question resolves to yes, byte-for-byte on the text layer.** The brief treated it as a possibility; it is a certainty.

## 8 · Two harness observations (not candidates)

- **`paper_packet.py` reported "identity: DOI (none recorded) · (no title recorded) [none]" for PMID 32368285**, while `registry_records.py get --pmid 32368285` returns `CORPUS-STUB-132`, which carries that PMID, the DOI and the full title. The packet's identity line and the registry disagree for stub-only records; a reader trusting the packet would conclude LEGEND had never heard of the paper.
- **`deepdive_manifest.py` refuses `text_contradicted_by_panel` without `contradicts` *and* `contradicts_needle`**, and the relation belongs on the **panel** entry pointing at the text entry, not on both. The diagnostic names the first requirement and not the second, which cost two validator rounds here. Both manifests that carry a contradiction in this wave are now in the passing form.

## 9 · Artefacts produced

| kind | path |
|---|---|
| dossiers | `research/fulltext_dossiers/PMID32368285.md` · `PMID42558002.md` · `PMID40937943.md` · `PMID33958783.md` |
| manifests | `research/deepdive_manifests/PMID32368285.json` (PASS, 1 declared gap) · `PMID42558002.json` (PASS) · `PMID40937943.json` (PASS) · `PMID33958783.json` (PASS) |
| candidates | `CC-20261004W7-A-REGISTRY-01.md` · `CC-20261004W7-A-DVL-01.md` · `CC-20261004W7-A-ASTROCYTE-01.md` · `CC-20261004W7-A-NEURONSPEC-01.md` |
| receipts (prepared, not appended) | `receipts_pending_w7/sciA_32368285_1.json` · `sciA_42558002_1.json` · `sciA_40937943_1.json` · `sciA_33958783_1.json` |
| corpus additions (gitignored) | `files/fulltext/PMID32368285_Celebi2020_PMC.xml` · `PMID32368285_Celebi2020_publisher.pdf` · `PMID32368285_Celebi2020_assets/` (3 page renders) · `PMID42558002_Lange2026_PMC.xml` · `PMID40937943_Ramirez2025_PMC.xml` · `PMID33958783_Liu2021_PMC.xml` · `PMID33958783_Liu2021_assets/` (9 figures) |
