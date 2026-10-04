# COMMIT CANDIDATE — CC-20261004W7-A-NEURONSPEC-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 7 2026-10-04, branch `task/sci-A-20261004w7`.
**context_policy:** `SOURCE_FIRST` — the paper was read and the panel inspected before any LEGEND record about WWOX expression was opened.
**Not medical advice.**

## The proposition, and why it is worth a record

Reading PMID 33958783 produced a sentence that will travel: *"TMEM108 and WWOX are both expressed in human brain … and specifically in dopamine and pyramidal neurons."* It is in a *Nature Genetics* paper, it is the only cell-type statement about WWOX in that paper, and it is the kind of clause reviews copy without opening the panel.

The panel it cites (Extended Data Fig. 5, laser-capture RNA-seq from the BRAINcode consortium) does not support it for WWOX. On a shared log₁₀(FPKM+0.01) axis:

| Gene | dopamine neurons (n = 86) | motor-cortex pyramidal (n = 3) | temporal-cortex pyramidal (n = 10) | PBMC (n = 4) | fibroblast (n = 3) |
|---|---|---|---|---|---|
| RIMS2 | ≈ 1.55 | ≈ 1.25 | ≈ 1.7 | ≈ −1.9 | ≈ 0.45 |
| TMEM108 | ≈ 0.3 | ≈ −0.05 | ≈ 0.65 | ≈ −1.0 | ≈ −0.9 |
| **WWOX** | ≈ 0.35 | ≈ 0.2 | ≈ 0.1 | **≈ 0.5** | **≈ 0.35** |

For the two companion loci the panel shows two to four log units between neurons and blood. For WWOX the two non-neural classes sit **at or above** the neuronal medians. The word "specifically" is carried by the sentence's two other subjects and is false of its third.

**No LEGEND record asserts WWOX neuronal expression specificity** — searched 2026-10-04 with `registry_records.py get --theme "expressed in" --theme espress --match any` over all seven surfaces; nothing claims it. So this is not a correction to LEGEND. It is a **negative worth holding before it is imported**, which is what the dismissal ledger is for, and it bears directly on the wave-7 question about cell-type-resolved WWOX measurement: the one human cell-type-resolved expression panel in this wave's sources shows WWOX as *not* neuron-enriched.

## Target
- `dismissal_ledger_current.md` — **create** `DIS-035` after `DIS-034`.

## Change class
**MINOR** — a research-layer dismissal record; no canonical claim, no working-model block, no status change. Provisional number measured 2026-10-04 with `registry_records.py catalog` (highest landed `DIS-034`); the integrator renumbers if taken.

## Ordering
Independent of the other wave-7 candidates. `CC-20261004W7-A-REGISTRY-01` should land first if both are in the batch, so that the wikilink to `PAPER 186` resolves.

## Op list — `dismissal_ledger_current.md` (record-scoped)

```json
[
 {
  "op": "insert-after",
  "id": "DIS-034",
  "text": "\n### DIS-035 — «WWOX is expressed specifically in dopamine and pyramidal neurons (PMID 33958783)» → ❌ **REJECTED by the panel the sentence itself cites**\n- **PREMISE: DATO** (2026-10-04, `CC-20261004W7-A-NEURONSPEC-01`, intake wave 7, Scientist A; read at source under `context_policy: SOURCE_FIRST`, receipt `FTR-20261004-33958783-01`, artefact `files/fulltext/PMID33958783_Liu2021_assets/nihms-1684407-f0008.jpg`). The genome-wide survival study [[paper_registry_current#PAPER 186]] ends its progression-loci section with *«TMEM108 and WWOX are both expressed in human brain (Extended Data Fig. 4) and specifically in dopamine and pyramidal neurons (Extended Data Fig. 5)»*. It is the only cell-type statement about WWOX in that paper.\n- **What the cited panel shows.** Extended Data Fig. 5 plots laser-capture RNA-seq (BRAINcode) on a shared log10(FPKM+0.01) axis over substantia-nigra dopamine neurons (n = 86), motor-cortex pyramidal neurons (n = 3), temporal-cortex pyramidal neurons (n = 10), peripheral blood mononuclear cells (n = 4) and fibroblasts (n = 3). RIMS2 and TMEM108 separate neurons from blood by about three and about one and a half log units respectively. **WWOX does not separate at all**: medians of about 0.35, 0.2 and 0.1 in the three neuron classes against about 0.5 in PBMC and about 0.35 in fibroblasts. The adverb is true of the sentence's two other subjects and false of WWOX.\n- **What this does and does not establish.** It establishes that this source does not show neuronal enrichment of WWOX, and that a sentence asserting it should not be imported from this paper. It does **not** establish that WWOX is uniformly expressed across brain cell types: the panel is bulk laser-capture from small donor numbers (three and ten for the two pyramidal classes), it holds no astrocyte or oligodendrocyte class at all, and transcript is not protein.\n- **Why it is recorded as a negative rather than a correction.** No LEGEND record asserts WWOX neuronal expression specificity (searched 2026-10-04 across all seven registry surfaces). This record exists so that the sentence is not imported later from a review that copied it.\n- **`REVIVAL_TRIGGER`:** a cell-type-resolved WWOX measurement in human brain with astrocyte, oligodendrocyte and neuron classes in the same assay and donor-level replication — single-nucleus or sorted-cell, protein or transcript — showing neuronal enrichment. The ancestry panel read in the same wave ([[paper_registry_current#PAPER 185]]) shows the complementary fact that WWOX transcript is readily detected in oligodendrocyte-lineage cells.\n- **Transfer limit:** this is a statement about an expression panel in an adult Parkinson's cohort paper. It says nothing about WWOX function, about any allele class, or about which cell type matters in WWOX-DEE. P47T, Q230P, G372R, A141T and P252A are not interchangeable, and a heterozygote is neither a demonstrated negative nor a positive for haploinsufficiency.\n- **Not medical advice.**\n"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT

- (The paper asserts neuron-specific expression for both loci, citing one panel | `TMEM108 and WWOX are both expressed in human brain (Extended Data Fig. 4) and specifically in dopamine and pyramidal neurons` | Results, progression loci, final sentence, `files/fulltext/PMID33958783_Liu2021_PMC.xml`)
- (The panel contradicts it for WWOX while supporting it for the other two | `[figure attestation — pixels cannot be quote-matched] Extended Data Fig. 5 (nihms-1684407-f0008.jpg), three panels on a shared log10(FPKM+0.01) axis over SNDA (n = 86), MCPY (n = 3), TCPY (n = 10), PBMC (n = 4) and FB (n = 3). RIMS2: neuron medians about 1.5-1.7 against PBMC about -1.9. TMEM108: neuron medians about 0.3-0.65 against PBMC about -1.0 and FB about -0.9. WWOX: SNDA about 0.35, MCPY about 0.2, TCPY about 0.1, PBMC about 0.5 and FB about 0.35 — the two non-neural classes sit at or above the neuronal medians.` | Extended Data Fig. 5, WWOX panel, `files/fulltext/PMID33958783_Liu2021_assets/nihms-1684407-f0008.jpg`)
- (The panel's own legend names the cell classes and the donor numbers | `Cell type-specific transcriptomes were assayed using laser-capture RNA sequencing (lcRNAseq) as reported47.` | Extended Data Fig. 5 legend, `files/fulltext/PMID33958783_Liu2021_PMC.xml`)
- (The WWOX association that frames the sentence is called suggestive by its own authors | `These loci achieved genome-wide significance (P < 5 × 10−8) in the combined analysis of discovery and replication populations with suggestive P < 5 × 10−5 in discovery and P < 0.05 in the replication cohort` | Results, progression loci, `files/fulltext/PMID33958783_Liu2021_PMC.xml`)


---

## BATCH DISPOSITION

**Verdict:** `PROPAGATED` by `BATCH_20261004_001` (2026-10-04, MINOR, WM_v7.13 → WM_v7.14; ACTOR_ID `scientist`, Scientist K, batch integrator).
**Surfaces written:** dismissal_ledger_current.md

Created as **`DIS-035`** after `DIS-034`, the number the candidate proposed; it kept it because A was applied first in event order, and the peer candidate that also proposed `DIS-035` took `DIS-036`.
🔴 **One triple came back `NOT_SUPPORTED`, and the record was repaired by re-sourcing rather than withdrawn** — the same repair `BATCH_20261003_005` made for a figure-legend locator. The candidate offered the Extended Data Fig. 5 legend's *«Cell type-specific transcriptomes were assayed using laser-capture RNA sequencing»* sentence for the five cell classes and their donor counts. That sentence names the **assay only**. The legend **does** name the classes, in its *«SNDA, indicates dopamine neurons …»* sentence, and states only that *«n indicates the number of individuals assayed for each cell type»*: **the counts exist nowhere in the text and only as the figure's x-axis labels**, which a second, independent auditor read on the rendered image and confirmed exactly (86 / 3 / 10 / 4 / 3). The landed record cites the legend for the classes, the image for the counts, and says in terms which surface carries which.
The small-donor caveat now names fibroblasts (n = 3) as well as the two pyramidal classes, and the two stale wikilinks (`PAPER 186`, `PAPER 185`) became `PAPER 204` and `PAPER 203`.
**An arithmetic screen on the candidate's prose, not on the record:** its § 20 says the two companion loci separate neurons from blood by *«two to four log units»*, which does not recompute from its own table for TMEM108 (1.3 to 1.65). The **op text** already said *«about three and about one and a half log units»*, which does recompute and which an auditor confirmed, so nothing landed wrong and no amendment was needed.
