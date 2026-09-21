# Is the MAVE / VAMP-seq methodology portable to WWOX — and can the FUNCTION half be ported, or only the abundance half?

**Date:** 2026-09-21 · **Actor:** Scientist A · **Mode:** READ-AND-REPORT, read-only toward every
canonical file. No registry edited, no `*_current.md` touched, no `BATCH_COMMIT`, no commit
candidate, no receipt written.
**Assignment source:** [`missense_rescue_methodology_census_20260921.md`](missense_rescue_methodology_census_20260921.md)
(rows `M-1` and `M-4`), against
[`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md) rows 3, 4, 5.

**Papers read in full, from the persisted artefacts below.** According to PubMed:
Biar CG *et al.*, *Nat Commun* 2026, PMID 42425971, PMCID PMC13478581 —
[DOI](https://doi.org/10.1038/s41467-026-75442-6);
Voutsinos V *et al.*, *bioRxiv* 2025, PMID 40463067, PMCID PMC12132302 —
[DOI](https://doi.org/10.1101/2025.05.10.653233).

> ⚠️ **Paper 2 is a PREPRINT (bioRxiv), not peer reviewed.** Every conclusion below that rests on it
> is marked `[PREPRINT]` and must be carried with that weight.
> **Not medical advice. Non-canonical research-layer file. No therapy proposed, no programme proposed.**

---

## 0 · STEP 0 — ledger check, reported by method, separately

### 0.1 `registry_records.py get --pmid` — **BOTH PMIDs MATCHED A RECORD**

| PMID | Result | Where |
|---|---|---|
| `42425971` | **MATCH** — `[mention]`, `record_digest=4179795dde90` | `disease-models/wwox/research/full_text_queue_current.md:5237` → **`FT-115`** |
| `40463067` | **MATCH** — same record | `full_text_queue_current.md:5237` → **`FT-115`** |

🔴 **This is the opposite of what the census asserted.** § 2 of the census states
*"`registry_records.py get --pmid` returns **zero records** for all six PMIDs"*. That was true when
the census was written and is **false now**: the census's own queue entry `FT-115` was committed
afterwards, and it is the record that matches. The lesson from today's standing rule holds in both
directions — **a negative from this tool is a statement about a moment and a surface, never about
LEGEND in general.** Re-run it; do not cite an earlier run.

Both runs were made at commit `0ee3cf91a7db`, working tree clean for the files consulted.
Source digests at call time: `claim_registry_current=2c49432942a1` · `discovery_ledger_current=36e642c273f5`
· `dismissal_ledger_current=1a4c623e27b4` · `full_text_queue_current=8284730cc7a8`
· `literature_tracking_log_current=93e27e5193f2` · `paper_registry_current=990f62b8e3a0`
· `working_model_current=f2dff5afd8fe`.

### 0.2 The plain grep sweep — **agrees, and finds more surfaces**

`grep -rn "42425971\|40463067\|VAMP-seq\|deep mutational\|multiplexed assay" --include=*.md disease-models/`
returns **20 lines across exactly two files** (excluding this file itself):

- `disease-models/wwox/research/full_text_queue_current.md` — lines 5237, 5239, 5241, 5242, 5248, 5251, 5254, 5256, 5261, 5266, 5289 (the `FT-115` body);
- `disease-models/wwox/analysis/missense_rescue_methodology_census_20260921.md` — lines 43, 44, 47, 48, 50, 62, 65, 66, 102 (the census itself).

**Nothing else in `disease-models/` mentions MAVE, VAMP-seq, deep mutational scanning or either
PMID.** So: LEGEND holds these two papers as a **queue entry and a census**, and holds **no reading,
no receipt, no claim, no discovery-ledger lead and no therapeutic hypothesis** derived from either.
The two methods agree on substance; they differ in that `registry_records.py` reached the queue
record by identity while the grep also surfaced the analysis file, which is **outside the tool's
surface list**. Both were needed.

---

## 1 · ARTEFACT MANIFEST

🔴 **Both bodies were written to disk verbatim at the moment of retrieval, before any analysis**, as
`FT-114` requires. Neither reading exists only in a reader's context.

| Paper | Path | Bytes | Chars | sha256 |
|---|---|---|---|---|
| **1 · TSC2** (PMID 42425971 / PMC13478581) | `files/fulltext/PMID42425971_PMC_MCPtext.txt` | **46 849** | **46 589** | `e41bad155ff5d73084740cc9e114053c26c000e3de4948372fd71590074bc150` |
| **2 · degron map** (PMID 40463067 / PMC12132302) | `files/fulltext/PMID40463067_PMC_MCPtext.txt` | **63 969** | **63 726** | `a1fbcf30fc119516370bc95589fb2572838963000fd884cdf69da5bb94f36469` |

Abstracts were persisted separately as `PMID42425971_PMC_MCPabstract.txt` and
`PMID40463067_PMC_MCPabstract.txt`.

### 1.1 🔴 The retrievability flag was wrong again, and by the same mechanism

`get_copyright_status(["42425971"])` returned, today, **verbatim**:
`"license":{"type":null,"url":null,"is_open_access":false}`, `"source":"pubmed"`,
`"checked_sources":["pubmed"]`.

**PMC was never consulted.** The fetch was attempted anyway and `PMC13478581` delivered
**46 589 characters** of full text. That is the third time this repository has recorded the pattern
(`PMID 41124647` → 68 491 chars on the same flag). **`is_open_access:false` with
`checked_sources:["pubmed"]` records what was not checked.** Paper 2's flag, by contrast, did carry
`checked_sources:["pubmed","pmc"]` with CC BY-NC-ND 4.0 and `is_open_access:true`, and also fetched.

### 1.2 Extraction damage, measured before any count was offered

`extraction_damage_report.py` on both artefacts:

| Artefact | fused-token scars | empty cross-ref stubs | orphaned statistics | reference list |
|---|---|---|---|---|
| `PMID42425971_PMC_MCPtext.txt` | 4 (e.g. `forand`, `ofVUS`, `ofin`, `theLOVD`) | 32 | 20 | **ABSENT** |
| `PMID40463067_PMC_MCPtext.txt` | 0 | 136 | 3 | **ABSENT** |

**Verdict on both: ITALIC-CLASS COUNTS INADMISSIBLE, ROMAN-CLASS COUNTS ADMISSIBLE, REFERENCE LIST ABSENT.**
Every count below states its class. No figure image was inspectable (`D-14`); figure legends
reproduced in body text are quoted where used, and nothing is asserted from a panel.

---

## 2 · VERDICT

> ## 🟡 **CONDITIONAL — and the condition is unchanged by these two papers.**
>
> **YES, the function half of a MAVE is portable in principle, and paper 1 proves it in a
> neurodevelopmental epilepsy gene: TSC2 activity was measured, multiplexed, on 391 missense
> variants, by sorting cells on intracellular phospho-S6 — a pooled, antibody-based FACS readout of
> the pathway the protein regulates.** **NO, it is not portable to WWOX today, and the single fact
> that decides it is that the entire TSC2 function assay is built on one thing WWOX does not have —
> a validated, cell-autonomous, antibody-detectable downstream molecular consequence of the
> protein's activity.** TSC2 supplies `pS6`; the census records that WWOX's *"substrate and product
> … are yet to be discovered"*, and neither paper read today supplies a substitute.
> **Paper 1 therefore REDUCES the obstacle — it shows the missing piece need not be catalytic
> turnover, only a sortable downstream signal — but it does NOT remove it.**

And the quantified brake, which is new and which LEGEND did not have: in TSC2, **31 of 80 (38.75%)
ClinVar pathogenic/likely-pathogenic missense variants had NORMAL abundance** (`T15`). An
abundance-only MAVE would have scored two in five known-pathogenic alleles as unremarkable. That is
the P282A problem measured at scale, in a real gene, by the authors themselves.

---

## 3 · PAPER 1 — TSC2 (PMID 42425971), what was measured and how

### 3.1 🔴 Did they measure FUNCTION at all, or only abundance? — **FUNCTION, YES. Multiplexed. Pooled.**

**Three assays, two axes.**

| Axis | Assay | Construct / locus | Cell system | Readout | Sorting | n variants scored |
|---|---|---|---|---|---|---|
| **Abundance** | **VAMP-seq** | TSC2 ORF **cDNA**, C-terminally GFP-tagged, barcoded, single-copy Bxb1 landing-pad integration; IRES-mCherry internal normaliser | **HEK293T landing-pad line** (`HEK293T-LLP-iCasp9`), AP1903 selection against unrecombined cells | **GFP:mCherry ratio** | FACS into **4 bins** (0–25 / 25–50 / 50–75 / 75–100 %) | **9 812** total; **8 864 missense**, **364 synonymous**, plus nonsense/3-bp-deletion |
| **Function** | **SGE** (cloning-free saturation genome editing) | **endogenous `TSC2` locus**, Cas9 RNP + ssODN library, guide-blocking synonymous edits | **primary human CD4 T cells**, 2 healthy donors × 2 replicates | **intracellular phospho-S6 (pS6)** — antibody CST 5316S — after fix/permeabilisation | FACS, **highest and lowest 25 % of pS6 intensity** | 268 missense scored in SGE |
| **Function** | **cliPE** (curated-loci prime editing) | **endogenous `TSC2` locus**, epegRNA library + PEmax + nicking gRNAs | **HAP1** (haploid), serum-starved overnight | **intracellular pS6** | FACS, **upper-quartile pS6** vs unsorted | 153 missense scored in cliPE |

**Combined function totals:** *"We generated TSC2 activity scores for 522 variants, including 391
missense variants, 64 synonymous variants, and 67 PTC variants"* (`T6`).

**Is mTORC1 signalling what they used? Yes — and specifically S6 phosphorylation, not S6K.**
`pS6` occurs 14 times, `mTORC1` 10, `mTOR` 21, `phospho-S6` 1, **`S6K` 0** (roman-class, admissible:
these are method words and protein abbreviations, not italicised gene symbols). The authors state
the logic directly (`T3`).

**🔴 What made it poolable — the mechanically important answer, itemised.** Not a reporter
construct, not survival, not a selection:

1. **The readout is an epitope, not an activity.** pS6 is measured by **intracellular antibody
   staining of fixed, permeabilised cells**. No substrate is added, no turnover is measured, no
   enzymatic product is detected. The cell does the signalling; the antibody reports it.
2. **The signal is cell-autonomous and inverted.** TSC2 is a *negative* regulator, so loss of
   function raises pS6 — *"larger scores indicate low TSC2 activity (high pS6 level; mTORC1 active;
   TSC2 inactive)"*. A **gain** of signal on loss of function is the easy direction to sort.
3. **Genotype and phenotype stay in the same cell.** Editing is at the **endogenous locus**, so the
   variant's DNA is recoverable by amplicon sequencing **from the sorted cells themselves** — the
   fixed cells are lysed and sequenced (`T26`, Methods/Genomic DNA isolation for fixed cells). This
   is what converts a per-cell phenotype into a pooled score.
4. **Editing also captures splicing**, which the cDNA-based abundance assay cannot (`T22`).

### 3.2 🔴 Abundance and function reported as separate axes — and variants that DISSOCIATE

**Yes, on both counts — and this is the direct analogue of the WWOX P282A problem.**

The Results heading is *"TSC2 variant abundance and activity are strongly correlated"* — and the
same section carries the dissociation. **The headline and the dissociation are not in conflict; they
are two statements at different resolutions, and a reader who carries only the heading would carry
the wrong one.** Quoted in full:

> *"Abundance was strongly correlated with activity in primary T cells (Pearson correlation = −0.57)
> and in HAP1 cells (Pearson correlation = −0.69, Fig.)."* (`T11`)

> *"We observed 31 variants which exhibited normal abundance yet reduced activity, and we
> hypothesized that these variants directly impacted TSC2 catalytic activity."* (`T13`)

> *"Indeed, these were located near the active site of the Rheb GAP domain (Fig.). Only residues
> within an alpha helix, the beginning of the adjacent beta sheet, or the linker region between
> these two secondary structure elements resulted in reduced activity variants that retained normal
> abundance. Of these inactive yet abundant variants, all but one mapped to highly evolutionarily
> conserved residues."* (`T14`)

> *"For both abundance and activity scores, BLB and PLP controls minimally overlapped, with the
> exception of a proportion (31/80; 38.75%) of PLP variants with normal abundance."* (`T15`)

> *"Importantly, some ClinVar PLP variants retain normal abundance, which limits the VAMP-seq assay
> in terms of providing evidence exluding pathogenicity."* (`T16` — the misspelling *"exluding"* is
> the source's, reproduced verbatim.)

> *"Our data revealed that some variants in the Rheb GAP domain cause loss of TSC2 activity with no
> change in protein abundance. This suggests that TSC2 activity and abundance data are
> complementary, which argues that generating variant effect data for both abundance and activity is
> optimal for."* (`T20` — the trailing gene symbol is elided by the extractor.)

**The other direction — low abundance with normal function — is not reported as a class.** The
authors' decision tree treats low abundance as strong evidence of pathogenicity precisely because
*no ClinVar BLB variant was classified as low abundance*. So in TSC2 the dissociation is
**one-directional**: abundance-normal-but-dead exists and is common; dead-abundance-but-functional
does not appear.

### 3.3 Abstract vs Results — checked, and they agree

The abstract says *"we use massively parallel sequencing to measure the steady-state abundance of
almost 9000 missense variants and develop an mTOR pathway activity assay using genome editing and
cell sorting to generate activity scores for 391 missense variants"*, with 1256/8864 (14.17 %)
altered abundance and 69/391 (17.65 %) altered activity. **Every one of those numbers is reproduced
in the Results and Introduction** (`T4`, `T6`, `T8`, `T10`). **No inversion found in this paper.**
One asymmetry the abstract does *not* carry, and which the Results do: **the 31 normal-abundance /
reduced-activity variants**, and the **38.75 % of PLP controls with normal abundance**. The abstract
is not misleading here; it is simply coarser, and the finding that matters most to LEGEND is only in
the Results.

### 3.4 Controls, dynamic range, reproducibility

- **Abundance controls.** **Synonymous** variants (n = 364) as the functionally-normal control:
  *"distributed with a relatively narrow range of scores (mean = 0.992; standard deviation = 0.103)"*
  (`T7`). **Premature termination codon (PTC)** variants as the null control — the pilot separated
  WT-GFP from a PTC variant before scaling up. Scores min-max normalised so **WT = 1** and the median
  of the lowest 5 % of missense = **0**.
- **Activity controls.** 64 synonymous and 67 PTC variants across the activity assays:
  *"The activity scores of synonymous and PTC variants comprised distinct populations with
  non-overlapping distributions, showing these assays distinguished functionally normal from
  functionally abnormal variants"* (`T9`). Scores normalised **within region** to the mean of that
  region's synonymous variants. Pilot: frameshift indels raised pS6 above untransfected cells.
- **Truth-set controls** for calibration: ClinVar **BLB n = 54**, **PLP n = 80**; for the activity
  assays only **9 BLB / 10 PLP (cliPE)** and **6 BLB / 16 PLP (SGE)** — the authors name this as the
  limiting factor on evidence strength.
- **Thresholds** (ROC + Youden): abundance **< 0.25 abnormal**, **0.25–0.75 indeterminate**,
  **> 0.75 normal**; SGE activity **> 2 abnormal**; cliPE activity **> 0.25 abnormal**.
- **Dynamic range.** The string `dynamic range` occurs **0 times** (roman-class, admissible — the
  authors do not use the phrase). What is reported instead: abundance scores bimodal, missense mean
  0.755 ± 0.348 against synonymous 0.992 ± 0.103; activity distributions of SYN and PTC
  **non-overlapping**. **A numeric fold-range for either assay is not stated in the body text.**
- **Reproducibility.** Two technical PCR replicates per bin per library (abundance); **4 activity
  replicates** (2 donors × 2); *"The SGE and cliPE datasets correlate very strongly with a
  coefficient of 0.92, suggesting few if any cell-type-specific variant effects"* (`T12`).
  **Replicate scatterplots are in Supplementary Figures and were not inspectable here (`D-14`).**
- **Evidence strength achieved** (OddsPath, ClinGen framework): abundance-low → **PS3_strong**
  (OddsPath 33.1); abundance-normal → **BS3_supporting** (0.343) (`T17`); activity-abnormal →
  **PS3_moderate** (4.5 / 5.6); activity-normal → **BS3_moderate** (0.113 / 0.094) (`T18`).
  Specificity of the abundance assay for detecting pathogenic variants **98.18 %**, sensitivity
  **61.25 %** (`T21`).

### 3.5 How they handled variants the assays could not classify

**They were left unclassified, explicitly and by name.** A decision tree assigns an initial code from
abundance, then overrides it with activity where activity data exist. Of 276 clinical-cohort VUS
with functional data, **212 (76.8 %) were putatively reclassified and 64 (23.1 %) remained VUS**,
broken down as: *"Variants remaining VUS had indeterminate functional results (= 31), conflicting
functional and computational evidence (= 23), or insufficient evidence for reclassification (="*
(`T19`; the counts are elided at the end by the extractor — the abstract-level numbers 31/23/10 are
recoverable from the Introduction). **1 854 of 8 864 (20.92 %) missense variants were "indeterminate"
in the abundance assay** and simply carried no abundance evidence. Reclassifications are labelled
**"putative"** throughout, not delivered as clinical classifications.

### 3.6 Stated limitations, verbatim-anchored

1. *"VAMP-seq is a cDNA-based assay and therefore is not appropriate for examining potential
   splice-altering variants."* (`T22`)
2. *"Second, the TSC2 cDNA expressed in VAMP-seq may may not reflect endogenous levels of TSC2
   expression."* (`T23` — the doubled *"may may"* is the source's.)
3. *"Third, we did not measure every possible mechanism of TSC2 variant pathogenicity, including the
   effect of variants on the TSC1-TSC2 interaction."* (`T24`) **🔴 Read this one twice: the
   protein-protein interaction axis — the axis a WWOX assay would have to use — is exactly the one
   they did NOT multiplex.**
4. cliPE is **retrospective** (library built from variants observed at one point in time); SGE and
   VAMP-seq are saturation and therefore prospective.
5. HAP1 ploidy not selected for; a small effect on partial-LoF or dominant-negative variants cannot
   be excluded.
6. *"Our primary goal was developing a MAVE which could distinguish complete loss-of-function
   missense variants from variants retaining function. Future work will be necessary to develop
   assays that are calibrated to test for partial loss-of-function or dominant negative variants."*
   (`T25`) **🔴 A hypomorph is not resolved by this design** — and a partially destabilised SDR
   missense allele is a hypomorph by hypothesis.
7. Only two TSC2 regions were assayed for abundance (aa **554–754**, 187 sites QC-passed; aa
   **1512–1802**, 286 sites QC-passed) — **not the whole protein**; the authors call completing the
   map future work.

---

## 4 · PAPER 2 — the cytosolic degron map (PMID 40463067) `[PREPRINT]`

### 4.1 🔴 Does the map include WWOX? — **CANNOT BE ANSWERED FROM THE BODY TEXT, AND THE ZERO IS AN INSTRUMENT READING**

`grep -oi WWOX` on the artefact returns **0**. **That zero is INADMISSIBLE as a biological negative.**
`WWOX` is an italic-class token (a gene symbol) and `extraction_damage_report.py` returns
*ITALIC-CLASS COUNTS INADMISSIBLE* for this artefact. **A zero here measures the extractor.**

Separately and more decisively: **this paper names individual proteins only as worked examples**
(PRKN, ASPA, PTEN, PNPO, HSPB1, RARS1, KRTAP11-1, PABPC1L, RIC1, CENPF). It never enumerates its
5 672 genes in prose. **So even a perfect extraction would not tell us whether WWOX is in the
library.** The membership question is decided by one criterion only:

> *"Genes of cytosolic proteins were selected based on gene ontology annotation GO:0005829 ()."* (`D2`)

**Whether WWOX (UniProt Q9NZC7) carries GO:0005829 "cytosol" was not established by this reading and
is NOT asserted here in either direction.** WWOX's better-attested annotations in the repository's
own reading of `41124647` are Golgi/mitochondrial/cytoplasmic membrane-associated, which is a reason
for genuine doubt, not an answer. **This is a resolvable question and § 4.5 says exactly how.**

### 4.2 Coverage and resolution — would aa 187–191 be covered in principle?

| Property | Value |
|---|---|
| Tile length | **30 residues** (90 nt) |
| Step | **15 residues** (45-nt overlap) — every residue is in **two** tiles except at the termini |
| Tiles measured | **212 658** (218 770 synthesised, 213 261 unique) |
| Proteins covered | **5 672 genes → 5 321 unique → 5 129 non-redundant UniProt proteins**, **99.7 % coverage**, **22 % of the human proteome** (`D4`, `D5`) |
| Selection criterion | **GO:0005829 (cytosol)** only (`D2`) |
| Context | Each tile fused to the **C-terminus of GFP**, single-copy landing-pad integration in **HEK293T**, IRES-mCherry normaliser, FACS into 4 quartile bins |
| Replication | 3 biological × 2 FACS replicates; **average Pearson r = 0.98** between replicate pairs (`D9`) |
| Dynamic range | *"nearly three orders of magnitude in protein abundance as measured by the fluorescence intensity"* (`D11`) |
| Low-throughput validation | 164 tiles individually, **Spearman ρ = −0.968** (`D12`) |
| Classes by potency | **19.1 % strong / 30.4 % intermediate / 50.5 % non-degron** (`D10`) |

**Conditional answer on resolution:** **IF** WWOX is in the GO:0005829 set, **THEN** residues
187–191 are covered — at 30/15 tiling, aa 187–191 falls inside two overlapping tiles, and the paper
reports 99.7 % tile coverage of its protein set. **The resolution is 30 residues, not 5**, so the map
would report a degron score for a window *containing* `LRSVQ`, never for `LRSVQ` itself, and could
not attribute a score to the motif without the motif being mutated — the same missing experiment the
proteostasis matrix already records for `41124647`.

### 4.3 🔴 What classes of degron — and does any correspond to lysosomal/CMA targeting? — **NO. NONE.**

**Every class reported is ubiquitin–proteasome.** The classes found:

- **PQC (protein quality control) degrons, composition-driven** — the dominant class. Potency set by
  **exposed hydrophobicity**: Trp, Phe, Tyr strongest, then Ile, Cys, Leu, Val; Asp/Glu/Pro/Ser
  stabilising. *"We found that most of the tiles with high degron potency tended to be in structured
  (high pLDDT) and buried (low rASA) regions of the proteins"* (`D13`) — i.e. they become active only
  on unfolding/misfolding.
- **C-degrons**, confined to the last five residues: -GG\*, -GA\*, -RxxG-type, -EE\*, -EI\*, -EM\*,
  -ES\*; most are **cullin-RING E3** targets.
- **Ubiquitin-independent C-terminal degrons** (C-terminal Ala at −1/−2, Cys at −1 to −3) — still
  proteasomal.
- **C-terminal stabilising signals** — Lys, Gln and acidic residues *counter* degrons.
- **Internal degrons from the previously characterised set** scored highest on average (`D19`);
  several known motifs (SCF-βTrCP `D(S)G.{2,3}([ST])`, SPOP `[AVP].{1}[ST][ST][ST]`) scored as
  **poor** degrons here (`D18`).

**The route was tested pharmacologically, and the lysosomal arm is the negative:**

> *"To further characterize the library, we treated the cells with the proteasome inhibitor
> bortezomib (BZ), the ubiquitin E1 inhibitor MLN7243, or chloroquine (CQ), which inhibits
> autophagy."* (`D6`)
> *"Conversely, no substantial change was observed with chloroquine ()."* (`D7`)
> *"Based on these results we conclude that the majority of the low abundance fragments represent
> degrons targeting the GFP-fusion for ubiquitin-dependent proteasomal degradation, while the
> contribution from ubiquitin-independent degradation and autophagy is minor"* (`D8`)

**Roman-class counts on this artefact (admissible):** `lysosom*` **0** · `KFERQ` **0** ·
`chaperone-mediated` **0** · `CMA` **0** · `bafilomycin` **0** · `autophagy` **2** (both in the
passage above) · `bortezomib` **3**. **`LAMP2` / `LAMP2A` / `HSPA8` / `HSC70` return 0, but those are
protein-symbol tokens and their class is ambiguous on this surface — they are NOT offered as clean
negatives.** The roman-class zeros alone are sufficient: **this paper contains no CMA content.**

### 4.4 🔴 THE CMA / DEGRON ANSWER — **ORTHOGONAL**

> **Does this degron map bear on LEGEND's unvalidated `LRSVQ` (aa 187–191) KFERQ-like CMA
> hypothesis? — NO. It is ORTHOGONAL. It can neither confirm nor refute it.**

**The reason, in three steps, none of which is an inference beyond the text:**

1. **It is a UPS screen by construction and by conclusion.** The authors' own route test stabilised
   the low-abundance population with a proteasome inhibitor and an E1 inhibitor and **not** with
   chloroquine (`D6`–`D8`). The census records that in `41124647` the WWOX P252A route was the exact
   mirror image: **MG-132 produced no accumulation; CQ and NH₄Cl restored the band.** A screen whose
   positive signal is the arm that was negative for WWOX P252A is measuring a different pathway.
2. **A CMA substrate would score as a NON-degron in this assay, and that score would mean nothing.**
   A tile with a functional KFERQ motif but no exposed-hydrophobic PQC signal would sit in the
   stable 50.5 %. **So even a hypothetical WWOX tile-187–216 score of "no degron" is not evidence
   against CMA targeting** — it is evidence about proteasomal degradation of a 30-mer.
3. **The assay format is incompatible with the mechanism in question.** CMA requires HSC70
   recognition of the motif in the **cytosolic, unfolded full-length substrate** followed by
   LAMP2A-dependent translocation. This assay reads a **30-residue peptide fused to the C-terminus
   of folded GFP**, in HEK293T, scored by steady-state GFP:mCherry. Nothing in that design reports on
   lysosomal uptake.

**What it would take to make this paper bear on the question — and it is not this paper.** LAMP2A
loss-of-function, HSPA8 knockdown, or motif ablation of `LRSVQ` on full-length WWOX. The
proteostasis matrix row 3 already specifies exactly that experiment. **This reading does not move
row 3 one way or the other.**

### 4.5 Is the data publicly queryable for one protein?

**Yes, in principle, and by a route this session did not walk.** The paper states
*"An online accessible version of PAP is available via GitHub and Colab."* (`D17`) and repeatedly
cites its own repository paths in the Methods — `library/build_lib.r`, `counts/call_zerotol_paired.sh`,
`scores/merge_and_map.r`, `score/scores.r`, `models/model_data.r`, `models/regression_analysis.r`.
**🔴 The GitHub and Colab URLs themselves are elided by the extractor** (the citation parentheses come
back empty — 136 empty cross-ref stubs on this artefact), **so no URL is reproduced here and none may
be reconstructed.** A future session can recover them from the PMC record
(`https://pmc.ncbi.nlm.nih.gov/articles/PMC12132302/`) or the bioRxiv supplement, and then answer the
membership question in § 4.1 directly: **look up whether the WWOX transcript appears in
`library/build_lib.r`'s gene list, and if so read the tile scores spanning aa 187–191.** That is a
bounded, mechanical, zero-cost query. **It is not proposed as a work item here; it is recorded as
available.**

### 4.6 One adjacent finding worth recording, with its distance stated

The paper's experimental disease exemplar is **PNPO D33V**, *"which manifests as neonatal epileptic
encephalopathy"* (`D15`) — a variant that is *"enzymatically active and structurally stable"* yet
degraded, *"suggesting that the D33V variant operates by creating an exposed quality control degron,
that in turn results in insufficient cellular levels of the otherwise functional enzyme."*
**That is a published, experimentally supported instance of a neonatal-epileptic-encephalopathy
missense allele whose entire pathogenicity is loss of abundance of a functional protein.** `[PREPRINT]`
**The distance to WWOX, stated:** PNPO D33V is in a **highly solvent-exposed** N-terminal region, and
the authors bound their own claim — *"However, these are limited to regions that are exposed such as
highly solvent accessible loops and intrinsically disordered regions."* (`D16`). LEGEND's `DL-BIO-001`
places **Q230 completely buried (relSASA 0.000, on an α-helix)**. **The PNPO mechanism class is
explicitly stated not to extend to buried positions, so it does not transfer to a Q230P-class allele.**
It is recorded as a precedent that *"re-stabilise a functional protein"* is a real disease mechanism
in this phenotype space, not as evidence about WWOX. The statistical support — *"a significantly
(p = 5.4 × 10) lower ΔPAP"* (`D14`) — **has its exponent elided by the extractor**; the p-value is a
mantissa with no exponent and **is not reconstructed here**.

---

## 5 · VERBATIM LOCATORS

Anchors are byte-offsets into the saved artefacts (character offsets in the UTF-8 decoded text).
Empty `()` and elided gene symbols are the extractor's, reproduced as found.

| ID | Artefact | Section | Anchor | Quote |
|---|---|---|---|---|
| `T1` | PMID42425971_PMC_MCPtext.txt | Introduction | char 2973–3225 | "To measure TSC2 protein abundance, we employed variant abundance by massively parallel sequencing (VAMP-seq), which measures steady-state protein abundance by fusing variants to GFP followed by fluorescence-activated cell sorting (FACS) and sequencing." |
| `T2` | PMID42425971_PMC_MCPtext.txt | Introduction | char 3226–3372 | "To assess TSC2 activity, we used endogenous genome editing combined with FACS for pS6, similar to our previous work on another mTOR pathway gene,." |
| `T3` | PMID42425971_PMC_MCPtext.txt | Introduction | char 2809–2972 | "Additionally, TSC2 functions as a negative regulator of mTORC1 signaling, making phosphorylation of the mTORC1 effector S6 (pS6) a direct readout of TSC2 activity." |
| `T4` | PMID42425971_PMC_MCPtext.txt | Introduction | char 3875–4029 | "We measured the effect of 9812 missense, synonymous, and nonsense variants on abundance using VAMP-seq and 522 variants on pS6 levels using SGE and cliPE." |
| `T5` | PMID42425971_PMC_MCPtext.txt | Introduction | char 4215–4352 | "However, 31 variants reduced TSC2 activity but not abundance, and these variants clustered around the active site of the Rheb GAP domain." |
| `T6` | PMID42425971_PMC_MCPtext.txt | Results / Development of MAVEs | char 9971–10123 | "We generated TSC2 activity scores for 522 variants, including 391 missense variants, 64 synonymous variants, and 67 PTC variants (Supplementary Figs.,)." |
| `T7` | PMID42425971_PMC_MCPtext.txt | Results / Development of MAVEs | char 7144–7285 | "Synonymous TSC2 variants (= 364) were distributed with a relatively narrow range of scores (mean = 0.992; standard deviation = 0.103) (Fig.)." |
| `T8` | PMID42425971_PMC_MCPtext.txt | Results / Development of MAVEs | char 7616–7721 | "We observed that 1256 of 8864 (14.17%) missense variants had low abundance (<0.25) in the VAMP-seq assay." |
| `T9` | PMID42425971_PMC_MCPtext.txt | Results / Development of MAVEs | char 10381–10597 | "The activity scores of synonymous and PTC variants comprised distinct populations with non-overlapping distributions, showing these assays distinguished functionally normal from functionally abnormal variants (Fig.)." |
| `T10` | PMID42425971_PMC_MCPtext.txt | Results / Development of MAVEs | char 10879–11061 | "We observed that 52 of 268 (19.4%) missense variants exhibited abnormal activity in the SGE assay while 22 of 153 (14.38%) missense variants had abnormal activity in the cliPE assay." |
| `T11` | PMID42425971_PMC_MCPtext.txt | Results / abundance-activity | char 11958–12109 | "Abundance was strongly correlated with activity in primary T cells (Pearson correlation = −0.57) and in HAP1 cells (Pearson correlation = −0.69, Fig.)." |
| `T12` | PMID42425971_PMC_MCPtext.txt | Results / abundance-activity | char 12110–12391 | "The SGE and cliPE datasets correlate very strongly with a coefficient of 0.92, suggesting few if any cell-type-specific variant effects (Supplementary Fig.). Thus, the majority of variants have concordant effects on abundance and activity as well as on activity between cell types." |
| `T13` | PMID42425971_PMC_MCPtext.txt | Results / abundance-activity | char 12392–12553 | "We observed 31 variants which exhibited normal abundance yet reduced activity, and we hypothesized that these variants directly impacted TSC2 catalytic activity." |
| `T14` | PMID42425971_PMC_MCPtext.txt | Results / abundance-activity | char 12554–12954 | "Indeed, these were located near the active site of the Rheb GAP domain (Fig.). Only residues within an alpha helix, the beginning of the adjacent beta sheet, or the linker region between these two secondary structure elements resulted in reduced activity variants that retained normal abundance. Of these inactive yet abundant variants, all but one mapped to highly evolutionarily conserved residues." |
| `T15` | PMID42425971_PMC_MCPtext.txt | Results / VUS resolution | char 17376–17548 | "For both abundance and activity scores, BLB and PLP controls minimally overlapped, with the exception of a proportion (31/80; 38.75%) of PLP variants with normal abundance." |
| `T16` | PMID42425971_PMC_MCPtext.txt | Results / VUS resolution | char 19458–19608 | "Importantly, some ClinVar PLP variants retain normal abundance, which limits the VAMP-seq assay in terms of providing evidence exluding pathogenicity." |
| `T17` | PMID42425971_PMC_MCPtext.txt | Results / VUS resolution | char 19000–19222 | "Under this framework, reduced abundance variants receive strong evidence of pathogenicity (OddsPath 33.1; PS3_strong) and normal abundance variants receive supporting evidence of benignity (OddsPath 0.343, BS3_supporting)." |
| `T18` | PMID42425971_PMC_MCPtext.txt | Results / VUS resolution | char 19609–19888 | "Reduced activity variants in either the primary T cell or HAP1 activity assays received moderate evidence of pathogenicity (OddsPath 4.5,5.6; PS3_moderate) and normal activity variants in either assay received moderate evidence of benignity (OddsPath 0.113, 0.094; BS3_moderate)." |
| `T19` | PMID42425971_PMC_MCPtext.txt | Results / VUS resolution | char 21284–21457 | "Variants remaining VUS had indeterminate functional results (= 31), conflicting functional and computational evidence (= 23), or insufficient evidence for reclassification (" |
| `T20` | PMID42425971_PMC_MCPtext.txt | Discussion | char 22816–23108 | "Our data revealed that some variants in the Rheb GAP domain cause loss of TSC2 activity with no change in protein abundance. This suggests that TSC2 activity and abundance data are complementary, which argues that generating variant effect data for both abundance and activity is optimal for." |
| `T21` | PMID42425971_PMC_MCPtext.txt | Discussion | char 23869–24259 | "It is worth emphasizing that, from a clinical genetics standpoint, the greatest strength of the TSC2 abundance variant effect dataset is detecting pathogenic variants (specificity = 98.18%). While the assay generates evidence towards benignity at supporting evidence strength (sensitivity = 61.25%), appropriate care must be taken when using this benign evidence for variant classification." |
| `T22` | PMID42425971_PMC_MCPtext.txt | Discussion / limitations | char 25213–25367 | "Our work has several limitations. First, VAMP-seq is a cDNA-based assay and therefore is not appropriate for examining potential splice-altering variants." |
| `T23` | PMID42425971_PMC_MCPtext.txt | Discussion / limitations | char 25764–25865 | "Second, the TSC2 cDNA expressed in VAMP-seq may may not reflect endogenous levels of TSC2 expression." |
| `T24` | PMID42425971_PMC_MCPtext.txt | Discussion / limitations | char 25866–26010 | "Third, we did not measure every possible mechanism of TSC2 variant pathogenicity, including the effect of variants on the TSC1-TSC2 interaction." |
| `T25` | PMID42425971_PMC_MCPtext.txt | Discussion / limitations | char 27912–28188 | "Our primary goal was developing a MAVE which could distinguish complete loss-of-function missense variants from variants retaining function. Future work will be necessary to develop assays that are calibrated to test for partial loss-of-function or dominant negative variants." |
| `T26` | PMID42425971_PMC_MCPtext.txt | Methods / SGE sorting | char 37455–37594 | "Stained cells were analyzed on a BD FACSAria II flow cytometer and cells were sorted on the highest and lowest 25% of phospho-S6 intensity." |
| `T27` | PMID42425971_PMC_MCPtext.txt | Methods / cliPE | char 41016–41189 | "After selection for PEmax-expressing cells via FACS sorting for GFP+ cells, cells were serum starved overnight prior to trypsinization, fixation, and immunolabeling for pS6." |
| `T28` | PMID42425971_PMC_MCPtext.txt | Methods / VAMP-seq | char 31610–31724 | "Landing pad HEK 293T (HEK293T-LLP-iCasp9) cells were transfected using FuGene 6 with each barcoded variant library" |
| `T29` | PMID42425971_PMC_MCPtext.txt | Discussion | char 29127–29341 | "The methods utilized herein are generalizable and could be used to study mTORopathy genes with missense VUS such as,, or, perhaps increasing access to mTOR inhibitors and other forms of precise clinical management." |
| `D1` | PMID40463067_PMC_MCPtext.txt | Results / screen | char 4007–4122 | "We selected all protein-coding genes that are localized to the cytosol according to gene ontology (GO) database ()." |
| `D2` | PMID40463067_PMC_MCPtext.txt | Methods / library design | char 37937–38027 | "Genes of cytosolic proteins were selected based on gene ontology annotation GO:0005829 ()." |
| `D3` | PMID40463067_PMC_MCPtext.txt | Results / screen | char 4123–4276 | "The open reading frames of these proteins were then divided into 30 residue (90 bp) tiles, each overlapping by 15 residues with the neighboring tiles ()." |
| `D4` | PMID40463067_PMC_MCPtext.txt | Results / screen | char 5509–5662 | "Sequencing of the generated library revealed that we had successfully managed to measure 212,658 tiles covering 99.7% of the 5,672 cytosolic proteins ()." |
| `D5` | PMID40463067_PMC_MCPtext.txt | Methods / library design | char 39409–39647 | "The 5672 protein-coding genes from Ensembl (5321 unique; out of ~70,000 human protein coding genes) were mapped to 5129 non-redundant proteins from the UniProt human proteome (out of ~23,000) and thus represents 22% of the human proteome." |
| `D6` | PMID40463067_PMC_MCPtext.txt | Results / UPS dependence | char 6656–6843 | "To further characterize the library, we treated the cells with the proteasome inhibitor bortezomib (BZ), the ubiquitin E1 inhibitor MLN7243, or chloroquine (CQ), which inhibits autophagy." |
| `D7` | PMID40463067_PMC_MCPtext.txt | Results / UPS dependence | char 7008–7075 | "Conversely, no substantial change was observed with chloroquine ()." |
| `D8` | PMID40463067_PMC_MCPtext.txt | Results / UPS dependence | char 7203–7463 | "Based on these results we conclude that the majority of the low abundance fragments represent degrons targeting the GFP-fusion for ubiquitin-dependent proteasomal degradation, while the contribution from ubiquitin-independent degradation and autophagy is minor" |
| `D9` | PMID40463067_PMC_MCPtext.txt | Results / validation | char 8093–8375 | "We performed three biological replicates (separate library transfections) and two FACS replicates for each of the biological replicates. We successfully scored the abundance of 99.7% of the tiles with an average Pearson correlation of 0.98 between pairs of replicate experiments ()." |
| `D10` | PMID40463067_PMC_MCPtext.txt | Results / validation | char 9652–9897 | "Using the bortezomib treated and untreated library distributions to define degron potency strength, we found in total 19.1% of the tiles function as strong degrons, 30.4% as intermediate degrons, while 50.5% did not display degron properties ()." |
| `D11` | PMID40463067_PMC_MCPtext.txt | Results / UPS dependence | char 6081–6206 | "In total the library covered nearly three orders of magnitude in protein abundance as measured by the fluorescence intensity." |
| `D12` | PMID40463067_PMC_MCPtext.txt | Results / validation | char 8752–8912 | "The results correlated well with the degron scores obtained from the screen (Spearman’s ρ = −0.968) and show a good correlation also within individual peaks ()." |
| `D13` | PMID40463067_PMC_MCPtext.txt | Results / structure | char 19224–19366 | "We found that most of the tiles with high degron potency tended to be in structured (high pLDDT) and buried (low rASA) regions of the proteins" |
| `D14` | PMID40463067_PMC_MCPtext.txt | Results / disease variants | char 28873–29057 | "revealed a significantly (p = 5.4 × 10) lower ΔPAP for the pathogenic/likely pathogenic mutations, indicating thatdegron formation might be a cause of pathogenicity of some of them ()." |
| `D15` | PMID40463067_PMC_MCPtext.txt | Results / disease variants | char 29096–29334 | "we selected the D33V variant of the pyridoxine-5’-phosphate oxidase (PNPO) enzyme, which has been linked to the rare autosomal recessive disease known as PNPO deficiency (MIM: 610090), which manifests as neonatal epileptic encephalopathy." |
| `D16` | PMID40463067_PMC_MCPtext.txt | Results / disease variants | char 29790–29997 | "In conclusion, degron formation can explain some pathogenic gene variants. However, these are limited to regions that are exposed such as highly solvent accessible loops and intrinsically disordered regions." |
| `D17` | PMID40463067_PMC_MCPtext.txt | Results / PAP model | char 24120–24190 | "An online accessible version of PAP is available via GitHub and Colab." |
| `D18` | PMID40463067_PMC_MCPtext.txt | Results / known degrons | char 18472–18587 | "Possibly these degrons are only active in specific cell types or are dependent on post-translational modifications." |
| `D19` | PMID40463067_PMC_MCPtext.txt | Results / known degrons | char 17355–17446 | "The highest average degron scores from our library corresponded to the internal degrons ()." |

### Re-match check — programmatic

Every quote above was re-matched, character-for-character, against the saved artefact files by
`/tmp/claude-0/extract_quotes.py` (which **extracts** each quote from the artefact by start/end
anchor rather than transcribing it) and re-verified by an independent `str.count` pass.

> ## **48 / 48 quotes re-matched · ZERO mismatches · each quote unique in its artefact.**

---

## 6 · THE TRANSFER SPECIFICATION — what a WWOX MAVE would need, itemised

🔴 **This is a feasibility and cost statement. It is NOT a proposal, and opening a WWOX MAVE is an
Operator decision (census § 5.4).**

### 6.A The abundance half — **PORTABLE TODAY**, with three named compatibility risks

| # | Requirement | TSC2 had it | Can LEGEND / a lab supply it for WWOX? |
|---|---|---|---|
| A1 | A landing-pad reporter line (HEK293T-LLP-iCasp9 or equivalent) | ✅ | ✅ Commodity; same line used by **both** papers read today |
| A2 | Barcoded site-saturation cDNA library, C-terminal GFP fusion | ✅ (Twist; 2 regions, 473 sites) | ✅ WWOX is **414 aa** — a *full-length* saturation library is ~7 900 missense variants, **smaller than the two TSC2 regions combined** |
| A3 | Barcode–variant association by long-read sequencing (PacBio/Pacybara) | ✅ | ✅ Standard |
| A4 | 4-bin FACS on GFP:mCherry + amplicon sequencing + CountESS scoring | ✅ | ✅ Standard |
| A5 | Synonymous and PTC control sets | ✅ (364 syn) | ✅ Trivially designed |
| **RISK 1** | **The GFP fusion must not itself destroy the phenotype.** WWOX is partly **mitochondrial / Golgi / membrane-associated**; a C-terminal GFP on a tail-anchored or targeted protein can mislocalise it. | n/a — TSC2 is cytosolic | ❓ **Unresolved. Must be piloted.** Neither paper addresses it. |
| **RISK 2** | **cDNA over-expression from a heterologous promoter may not reflect endogenous levels** — the authors' own limitation 2 (`T23`) | acknowledged | ❓ Same exposure. The proteostasis matrix already flags this against `41124647`'s CMV-Flag constructs. |
| **RISK 3** | **The dominant WWOX degradation route in the one paper that measured it is LYSOSOMAL**, not proteasomal. VAMP-seq is route-agnostic (it reads steady state), so this does **not** break the assay — but it does mean a WWOX abundance map would **not** be interpretable through the UPS-degron framework of paper 2. | n/a | ⚠️ Recorded, not fatal. |

### 6.B The function half — **NOT PORTABLE TODAY.** The five requirements, and where each stands

Derived by decomposing what actually made the TSC2 pS6 assay work (§ 3.1):

| # | Requirement extracted from TSC2 | WWOX status | Who could supply it |
|---|---|---|---|
| **F1** | **A downstream molecular consequence of the protein's activity that changes in a single cell when the protein is lost.** TSC2 → pS6. | 🔴 **ABSENT.** `TX-003`: *"WWOX is an oxidoreductase with undefined physiological substrate/activity"*; the Adelaide review: *"the substrate and product of the enzyme reaction that it catalyses are yet to be discovered."* | **Nobody, today.** This is the binding item. |
| **F2** | **That consequence must be detectable by a flow-cytometry-compatible reagent** — an antibody to a post-translational mark, or a fluorescent reporter. TSC2 → CST 5316S anti-pS6, fixed/permeabilised. | 🔴 **ABSENT.** No validated WWOX-activity-dependent epitope exists. The candidates the matrix names (tau, GSK3β, POLE4 binding; WW1-partner binding as control) are **binding assays**, which are **co-IP/western readouts, not per-cell fluorescence readouts.** | Would require a new reporter — e.g. a split-fluorophore or FRET PPI sensor for an SDR-domain partner, **validated first at low throughput**. **This does not exist and building it is itself a research programme.** |
| **F3** | **The phenotype must be cell-autonomous in a cultured, editable, expandable cell type.** TSC2 → primary CD4 T cells and HAP1. | ❓ **UNKNOWN and plausibly adverse.** The disease phenotype is neuronal and developmental; `seizure` and `neuron` occur 0 times in `41124647`'s body. A WWOX function that only manifests in post-mitotic neurons cannot be pooled in an editable proliferating line. | Unresolved. |
| **F4** | **The direction of the signal should ideally be a GAIN on loss of function** (easier sorting). TSC2 is a negative regulator → pS6 **rises**. | ⚠️ **Adverse.** WWOX appears to act positively in its characterised interactions, so loss would most likely **remove** a signal. Sorting on signal loss is harder and more confounded by abundance. | Design constraint, not a blocker. |
| **F5** | **Endogenous-locus editing (SGE/cliPE) so genotype is recoverable from the sorted cells.** | ✅ **Available.** `WWOX` is editable; SGE and cliPE are published, generic methods. | A MAVE lab. **This is the one function-half item that IS supplied today.** |

### 6.C 🔴 The pooled-format problem, stated exactly

**The obstacle is not that WWOX has no measurable function. It is that every WWOX function LEGEND can
currently name is measured ONE SAMPLE AT A TIME.**

- The matrix's own chosen readout — *"an abundance-normalised, domain-resolved binding panel"* on
  immunopurified protein — is **co-immunoprecipitation**. Co-IP is intrinsically **per-sample**: one
  lysate, one pulldown, one blot. There is no way to read a pooled library of variants through it,
  because the pulldown destroys the cell-to-genotype link that pooled sorting depends on.
- The TSC2 trick is that **the phenotype stays inside the intact, fixed cell** as an antibody-stainable
  epitope, and the genomic DNA is recovered **from those same fixed cells**. **Any WWOX function assay
  must be reduced to a per-cell fluorescence signal or it cannot be multiplexed at all.**
- **Therefore the gate on a WWOX function MAVE is not the MAVE. It is the prior invention of a
  single-cell, fluorescence-readable WWOX activity sensor.** That is upstream work of unknown
  duration, and neither paper read today performs it or shows how.

### 6.D What LEGEND itself cannot supply, explicitly

LEGEND is a reasoning and evidence system with **no wet-lab capacity**. Of the items above it can
supply **none** experimentally. What it can supply is: the variant list, the structural priors
(`DL-BIO-001`), the domain-resolved readout logic (matrix row 5), the control design (WW1-dependent
partner must stay normal), and the epistemic brake (`P282A`; the TSC2 **38.75 %** figure). **Items
F1 and F2 are not gaps in LEGEND's records — they are gaps in the field.**

---

## 7 · NEGATIVE RESULTS — explicit

1. 🔴 **The degron map contains no chaperone-mediated-autophagy content at all.** Roman-class,
   admissible: `lysosom*` 0, `KFERQ` 0, `chaperone-mediated` 0, `CMA` 0, `bafilomycin` 0. `[PREPRINT]`
2. 🔴 **`WWOX` returns 0 in the degron-map artefact — and this is NOT a negative.** Italic-class token
   on an artefact certified *ITALIC-CLASS COUNTS INADMISSIBLE*. **Instrument reading only.** Whether
   WWOX is in the GO:0005829 library is **UNRESOLVED**, not answered.
3. **Neither paper mentions WWOX, WOREE, or any SDR-family oxidoreductase.** No transfer claim in this
   file is any author's; all are this reader's, and § 6 states the obstacle that limits them.
4. **`S6K` occurs 0 times in the TSC2 artefact** (roman-class, admissible). The readout is
   **phospho-S6**, not phospho-S6K — a distinction that matters if anyone later ports the design.
5. **`dynamic range` occurs 0 times in the TSC2 artefact** (roman-class, admissible). **No numeric
   dynamic range is reported for either TSC2 assay in the body text.**
6. **No "low abundance but normal function" class was reported in TSC2.** The dissociation runs one
   way only. **This is "not reported", not "shown absent".**
7. **TSC2's PPI axis was explicitly NOT multiplexed** (`T24`) — the very axis a WWOX assay would need.
8. **The TSC2 abundance map is not saturating over the whole protein** — two regions only (aa 554–754,
   aa 1512–1802).
9. **Neither reading produced a receipt.** This is a READ-AND-REPORT assignment; `fulltext_receipts.py
   record` was **not** run, per the assignment's read-only constraint. **Both artefacts are on disk and
   fingerprinted in § 1, so a later session can receipt them without re-fetching** — and must check the
   ledger for these PMIDs before dispatching any re-read.
10. **No figure panel was inspected** (`D-14`). Every replicate scatterplot, heatmap and flow histogram
    cited by both papers is a figure and is **not** evidence here.
11. **The degron map's key disease-variant p-value is unusable as reported**: *"p = 5.4 × 10"* with the
    exponent deleted by the extractor. **Not reconstructed.**

---

## 8 · INFORMATION GAIN

| Item | Gain | One line |
|---|---|---|
| **Mechanistic graph** | **NO** | Neither paper measures WWOX, its partners or its degradation. The degron map is UPS; the WWOX observation on record is lysosomal. Nothing attaches to the graph. |
| **Therapeutic hypothesis** | **NO** | Both papers are `MECHANISTIC PROBE ONLY`. No molecule, no intervention, no dosing, no window. `[PREPRINT]` for paper 2 regardless. |
| **Experimental roadmap** | **YES** | The function half of a MAVE is now specified rather than hypothetical: five named requirements (`F1`–`F5`), four of which WWOX fails, and the exact reason a co-IP-based readout cannot be pooled. The gate is a single-cell fluorescence-readable WWOX activity sensor, which must be invented **before** any MAVE, not by one. |
| **Genotype stratification** | **NO** | No WWOX allele is scored, ranked or re-classified by anything read today. |
| **Intervention ranking** | **NO** | Nothing here ranks or re-ranks any intervention; no intervention appears. |
| **Uncertainty** | **YES** | Three quantified reductions: (i) **38.75 %** of ClinVar PLP TSC2 variants have normal abundance — the P282A brake now has a number from a real gene, and it bounds how misleading an abundance-only WWOX MAVE would be; (ii) a pooled function MAVE is demonstrated in a **neurodevelopmental epilepsy gene**, so "MAVEs are for tractable enzymes" is retired as an objection; (iii) the CMA question is shown to be **untouched** by the one systematic degron resource in existence, closing a route LEGEND might otherwise have queued as promising. |

---

## 9 · DEFAULTS_TAKEN

1. **Fetched despite the negative flag.** `is_open_access:false` with `checked_sources:["pubmed"]` was
   treated as "not checked" and the fetch attempted. It returned 46 589 characters.
2. **Persisted before analysing.** Both bodies were extracted from the tool result on disk via a JSON
   read and written to `files/fulltext/` **before** any reading, so neither depends on session context.
   Abstracts persisted alongside.
3. **Quotes extracted, not transcribed.** Every locator was pulled from the artefact by start/end
   anchor in a script, so the 48/48 re-match is a property of the method, not a later check. Thin
   spaces (U+2009), the en-dash minus (U+2212), `ρ`, `Δ`, `’` and the source's own typos
   (*"exluding"*, *"may may"*) are preserved exactly.
4. **Count classes declared individually.** Roman-class zeros offered as evidence; italic-class zeros
   (notably `WWOX`) declared inadmissible; ambiguous protein-symbol zeros (`LAMP2A`, `HSC70`) withheld
   from the argument entirely.
5. **The elided p-value exponent was left elided.** No arithmetic reconstruction was attempted, so no
   `INFERENCE` label was needed.
6. **`registry_records.py` was re-run rather than cited from the census.** The census's "zero records"
   is reported as *superseded*, with the matching record named.
7. **No receipt, no canonical edit, no commit candidate, no queue entry.** Per assignment.
8. **No WWOX MAVE programme is proposed.** § 6 is a feasibility and cost specification. The
   recommendation question is left entirely to the Operator.
9. **The GO:0005829 membership of WWOX was left UNRESOLVED rather than guessed**, with the exact
   mechanical query that resolves it recorded in § 4.5.
10. **Paper 2 is marked `[PREPRINT]` at every load-bearing use**, including in § 4.6 and § 7.

---

*Not medical advice. Non-canonical research-layer analysis file. READ-AND-REPORT only.*
