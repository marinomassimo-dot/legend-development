# PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1

**Non-canonical learning artifact.** Nothing here modifies the claim registry, the paper
registry, the Pathograph, the DisMech export, the Scientist role or governance. Canonical
corrections are *proposed* in §15 and are not applied.

**Paper:** Repudi S, Steinberg DJ, Elazar N, Breton VL, Aquilino MS, Saleem A, Abu-Swai S,
Vainshtein A, Eshed-Eisenbach Y, Vijayaragavan B, Behar O, Hanna JJ, Peles E, Carlen PL,
Aqeilan RI. *Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and
myelin defects.* **Brain** 2021;144(10):3061–3077. PMID 33914858 · DOI 10.1093/brain/awab174.

---

## 1 · Source-state / worktree

| Item | Value |
|---|---|
| ACTOR / worktree | `lettore-c` · `<REPO_ROOT>/.claude/worktrees/lettore-c` |
| Branch | `lettore-c` |
| HEAD at session start | `908197b` — **65 commits behind `main`, 0 ahead** |
| HEAD used for every measurement | `788c357` (fast-forwarded to `main` before measuring) |
| Framework / working model | `v3.3.1` · `WM_v4.3` · manifest `READY` |
| Canonical files modified | **none** (`git status` shows only untracked `learning/scientist/`) |
| Receipt ledger | 128 chained receipts, tail anchored, `verify` OK — unchanged by this session |

**Why the fast-forward came first.** At `908197b` every number I could have produced would
have been internally consistent and would have described a tree nobody has. The measurements
below are all taken at `788c357`.

### Local full-text surfaces

| Surface | Location | Present in this worktree? |
|---|---|---|
| `PMID33914858_Aqeilan2021.pdf` | `files/fulltext/` in the **main checkout** | **No** — `files/` is gitignored, so it exists only in `<REPO_ROOT>/` |
| `PMID33914858_Aqeilan2021.fitz.txt` | `staging/fulltext_txt_20260808/` (main checkout) | No — `staging/` gitignored |
| `PMID33914858.fitz.txt` | `staging/fulltext_text_20260809/` (main checkout) | No — `staging/` gitignored |
| `PMID33914858_Repudi2021.handoff.md` | `~/Desktop/Claude Workspace/files/fulltext/` | Outside this repository entirely |

- PDF sha256 `960569a9c0d4e7634a53e3b829fc29145767f9df0ce620cf827b891c6708d559`, 5 350 109 bytes,
  17 pages, PDF 1.3, producer *Acrobat Distiller 8.0.0 (Windows); modified using iTextSharp*.
- The article is the version of record: page range 3061–3077 matches the PDF's internal title
  `OP-BRAI210177 3061..3077`.

**Consequence to record:** every text surface for this paper is gitignored and local to one
machine. CI sees none of them. A reader on a fresh clone has nothing.

---

## 2 · Prior-reading state — measured, not assumed

Plan v2's four assertions were checked independently. **All four are correct**, and one is
correct for a reason worth stating precisely.

| Plan v2 says | Verified? | Evidence |
|---|---|---|
| PAPER 004 marked integrated | ✅ | `paper_registry_current.md` line 102 region: `**Status:** integrated` |
| CLAIM 003 consolidated baseline | ✅ | `claim_registry_current.md`: `**Status:** consolidated baseline`, `**Type:** DATO` |
| Zero valid full-text receipt events for this PMID | ✅ | see below |
| FT-044 suspended since 2026-08-09 for text-surface invalidity | ✅ | `full_text_queue_current.md` line 907 ff. |

### The receipt measurement, done the way the task demanded

The ledger holds **128** events. `grep 33914858` returns **5** of them. Parsing `study_id`
rather than grepping the line:

- events whose `study_id` **is** PMID 33914858: **0**
- events that merely **mention** the PMID inside another paper's `evidence_basis`: **5** —
  `FTR-20260809-42397075-01`, `FTR-20260810-34747138-01`, `FTR-20260810-42422765-05`,
  `FTR-20260810-34634460-02`, `FTR-20260811-16061658-01`.

All five mention it as a *comparator* — the surface-fidelity finding — not as a reading of it.
A line-level grep would have reported "5 receipts" for a paper with none.

### Two further facts Plan v2 did not report

1. **PAPER 004 has no `Evidence depth:` field at all.** PAPER 005 and PAPER 006 both carry
   one. PAPER 004's provenance line says only *"abstract/key-findings verificati via PubMed
   2026-07-05"* and *"arricchimento quantitativo del claim rimandato al PDF"*. So the record
   is `integrated` on abstract-level verification, and the registry does not claim otherwise —
   it simply has no field in which to say so.

2. **CLAIM 003's entire "Evidence boundary" paragraph is derived from PAPER 005**
   (PMID 34747138, the EMBO gene-therapy twin), which *was* read in full. The claim's own
   declared `**Source:** Repudi et al., 2021, *Brain*` has never been read. The consolidated
   baseline is anchored to a paper the system has never opened, and qualified by a different
   paper it has.

3. **`CORPUS-STUB-087` is still `not_processed`** and carries the same DOI as PAPER 004 — the
   duplicate flagged in the PAPER 004 note is unresolved at `788c357`.
   `LIT-0110` in the tracking log is likewise still `**Status:** discovered`.

---

## 3 · Group / paper context

- **Senior author Rami I. Aqeilan** (Lautenberg Center, Hebrew University) is the central WWOX
  laboratory; the paper is a continuation of that program, not independent confirmation of it.
  PAPER 005 (EMBO Mol Med 2021, gene therapy) shares first author Repudi and the same lab and
  the same year.
- **Co-senior Peter L. Carlen** (Krembil, Toronto) supplies the electrophysiology; **Elior
  Peles** (Weizmann) supplies myelin/node biology — both are established independent groups in
  their own domains. The electrophysiology and the myelin ultrastructure are therefore not
  in-house-only measurements even though the genetic models are.
- **Primary experimental work**, not a review.
- **Relevance:** this is the paper that introduced the conditional Cre series (Nestin, Synapsin
  I, Olig2, GFAP) into WWOX biology. That series, not the hypomyelination phenotype, is its
  most transferable contribution.

**Context adjusts attention; it does not substitute for evidence.** In practice the
Aqeilan-lab continuity means that PAPER 004 and PAPER 005 are *not* two independent
observations of non-cell-autonomy — they are one program. §13 uses that.

---

## 4 · Surface preflight

Performed **before** any evidence extraction, as the task required.

| ROUTE | RESULT | SURFACE QUALITY | VERBATIM? | FIGURES? |
|---|---|---|---|---|
| PMC / Europe PMC structured XML | **Absent.** Europe PMC: `pmcid: None`, `inPMC: N`, `inEPMC: N`, `isOpenAccess: N`, `hasPDF: N` | n/a | NO | NO |
| NCBI `elink` pubmed→pmc | Only `pubmed_pmc_refs` (30 articles *citing* this one). **No deposit linkset** | n/a | NO | NO |
| Unpaywall | `is_oa: true`, `oa_status: **bronze**`, `has_repository_copy: **false**`, 1 OA location = publisher PDF | n/a | NO | NO |
| Crossref | Lists only the two publisher PDF URLs; `relation: {}` | n/a | NO | NO |
| Publisher HTML / supplementary | **HTTP 403** on both the article page and the Silverchair supplementary ZIP | blocked | NO | NO |
| **Local PDF text layer** (PyMuPDF 1.26.5) | Retrieved | 🔴 **SUSPECT** — see below | **NO, unrepaired** | n/a |
| **Rendered page @600 dpi** (adjudication surface) | Retrieved | **Authoritative** | **YES** | YES |
| **Embedded figure images** | Retrieved at native resolution | 1000 px wide → **≈150 ppi effective** | n/a | **YES, with a stated ceiling** |

`elink` deserves a note: it *does* return a PMC linkset, and a careless read of it would have
concluded a PMC copy exists. The linkname is `pubmed_pmc_refs` — articles in PMC that cite
this one. There is no `pubmed_pmc` link. Three services independently agree: **no structured
surface exists for this paper.** FT-044's `pdf_only` is confirmed.

### The text-layer defect: reproduced, then measured further than FT-044 measured it

FT-044's claims, checked:

| FT-044 claim | Verified | Correction |
|---|---|---|
| `Results were considered significant when P 5 0.05` in Methods | ✅ exactly | — |
| zero `<`, `>`, `≤`, `≥` in the whole document | ✅ (0/0/0/0) | — |
| "14 of `P 5 0.0…`" | ⚠️ | the true count is **18**, and there are **two** substitute digits (`5` *and* `4`), which FT-044 did not distinguish |
| `fold change 41.5`, `delta (55 Hz)` | ✅ | — |
| three extractors agree on the wrong character | ✅ | — |
| mechanism not established | ✅ at the time | **now established — see below** |

**The mechanism is font provenance, and it is fully determinate.** Extracting per-character
with `rawdict` shows the corrupted glyphs are drawn in *pi/symbol subset fonts*, where the
byte that reaches the text layer is the font's own code point, not Unicode:

| Font | Byte extracted | True glyph | n | Adjudicated on |
|---|---|---|---|---|
| `AdvPi1` | `5` | `<` | 16 | p.5 Methods, p.5 delta band, p.9 |
| `AdvPi1` | `4` | `>` | 1 | p.9 `fold change > 1.5` |
| `AdvPi2` | `4` | **`≤`** | 4 | p.10, p.11 figure legends |
| `AdvPi1` | `m` | `µ` | 25 | p.3, p.10 scale bars |
| `AdvPSMP13` | `l` | `µ` | 7 | p.3 `0.22 µm filter` |
| `AdvPSMP13` | `a` | `α` | 6 | p.9 `PDGFRα` |
| `AdvPSMP13` | `b` | `β` | 2 | p.13 `Wnt/β-catenin`, `TGFβ` |
| `AdvP4C4E74` | `\x02` | `∼` | 10 | p.3, p.7, p.9 |
| `AdvP4C4E74` | `\x03` | `°` | 13 | p.3 `37°C` |
| `AdvP4C4E74` | `\x04` | `×` | 1 | p.3 `37°C ×3` |
| `AdvP80516` | `V` | `©` | 4 | p.1 footer |
| `AdvTT5843c571` | `±` | `±` | 15 | already correct |

**89 corrupted glyph instances, 0 unresolved.** Every row was adjudicated by rendering the
glyph's own bounding box at 600 dpi and reading it — not inferred from expected content.

🔴 **The single most important result of this preflight:** `AdvPi2`'s `4` is **`≤`, not `<`**.
A content-expectation would have written `P < 0.01` into four figure legends, because that is
what a significance legend "obviously" says. The authors wrote `P ≤ 0.01`. Guessing from
meaning would have misreported the authors' own stated threshold in Fig. 4G and Fig. 5B/C.
Two pi fonts in one document use different bytes for different comparators; a per-document
mapping would also have been wrong.

🔴 **The defect is much broader than "comparators".** FT-044 recorded only the `P`-value
damage. It also destroys **`µ`** — so *"Scale bars = 50 mm (A), 2 mm (B)"* extracts as
millimetres where the page prints **micrometres**, a 1000× unit error that reads as a
perfectly plausible number — and **`∼`**, so *"(∼3.5–4-fold)"* extracts as an exact
`(3.5–4-fold)`. Both survive any sentinel that looks for missing comparators.

### What was and was not repaired

A page-adjudicated surface was built at
`scratchpad/PMID33914858.adjudicated.txt`, sha256
`36ae29ada523bd770a9839982cfb5688ebe693cc61385a622756665a047c7f55`, with a per-character
provenance record. This is **not** a silent repair: every substitution is (font, byte) →
glyph, backed by a rendered crop, and the artefact is in the scratchpad, **not** in the
repository and **not** proposed as a canonical surface. Residual sentinel on the corrected
text: `(P <digit>` pattern = 0, C0 controls = 0, U+FFFD = 0.

**FT-044 should not be closed on this basis.** What this read demonstrates is that the
suspension was correct *and* that a lawful route through it exists. Turning that route into a
gate is a separate, canonical piece of work (§15).

---

## 5 · Reading budget — and how each denominator was derived

| Unit | Count | Derivation |
|---|---|---|
| Pages | **17** | `doc.page_count`; corroborated by printed range 3061–3077 |
| Top-level sections | **9** | lines set in `AdvOT3c584a2f.B` @12.0 pt: Introduction, Materials and methods, Results, Discussion, Acknowledgements, Funding, Competing interests, Supplementary material, References |
| Methods subsections | **13** | lines in `AdvOT1ab0d708.B` @9.5 pt between *Materials and methods* and *Results* |
| Results subsections | **6** | same font/size run inside Results |
| Main figures | **7** | line-initial `^Figure \d` captions; corroborated by 7 embedded images, one per figure page (6,7,8,10,11,12,14) |
| Main-figure panels | **45** | `(A)`…`(Z)` labels per caption, kept only as a contiguous run from A. F1=9, F2=6, F3=6, F4=7, F5=4, F6=4, F7=9 |
| **Main tables** | **0** | ⚠️ see below |
| Supplementary figures | **9** | distinct `Supplementary Fig. N`, N∈{1..9} |
| Supplementary tables | **3** | `Supplementary Table 1,2,3` |
| Supplementary videos | **2** | `Supplementary Video 1`, `Supplementary Video 2` |

⚠️ **The table denominator is where a parser lies.** `grep -o 'Table [0-9]'` returns
`Table 1`, `Table 2`, `Table 3` — three plausible integers. Every one is the tail of
*Supplementary* Table N. Constraining the match to a preceding word shows **zero** main
tables. Had the count been taken at face value, this read would have carried a three-table
debt against tables that do not exist.

**Panel-count caveat, stated rather than padded.** 45 is the count of *labelled* panels.
Figure 5D contains sub-panels (i), (ii), (iii) that the letter-run does not count, and
Figure 3F is a single label over two UMAP plots. The true inspectable-unit count is higher
than 45; 45 is the reproducible lower bound from the caption grammar.

**Figure resolution ceiling.** All seven figures are embedded at 1000 px width, placed
≈480 pt wide ⇒ **≈150 ppi effective**. Rendering above 150 ppi upsamples and adds nothing.
Fine ultrastructural detail in Fig. 5A and Fig. 7H is at the limit of what this surface can
support, and no claim below is made from features at that limit.

**Coverage actually achieved:** Introduction, all 13 Methods subsections, all 6 Results
subsections, Discussion, and all 7 figure captions were read in full. All 7 figures were
inspected as images. **Supplementary: 0 of 9 figures, 0 of 3 tables, 0 of 2 videos** (§9).

---

## 6 · Neutral first pass

An observation freeze was written **after** the complete text read and **before** figure-image
inspection, the DisMech crosswalk and all synthesis:

`scratchpad/OBSERVATION_FREEZE.md`, sha256
`08162dac95b7b38ddc6ecc024216eead4fb2d65928b07136e64cd141d727bc31`, frozen
2026-08-25T08:37:59Z. It records 35 observations (O1–O35) in paper order. Every finding in
§7–§14 traces to one of them; nothing in §7–§14 introduces an observation absent from the
freeze.

---

## 7 · Experiment-by-experiment reconstruction

### E1 — Conditional Cre series (Fig. 1)

| | |
|---|---|
| **Question** | Which CNS cell type's WWOX loss reproduces the Wwox-null phenotype? |
| **Model / genotype** | `Wwox^flox/flox` × Nestin-Cre (**N-KO**, E10.5, stem/progenitor), Synapsin I-Cre (**S-KO**, E12.5, mature neurons), Olig2-Cre (**O-KO**, oligodendrocytes), GFAP-Cre (**G-KO**, astrocytes); plus systemic Wwox-null |
| **Assay** | Weight curves to day 16; Kaplan–Meier survival; hind-limb clasping; video |
| **Controls** | Cre⁺ littermate controls per line; heterozygotes (`Wwox^+/flox`) for Nestin and Synapsin |
| **Result** | N-KO and S-KO phenocopy the null: growth retardation, seizures (S-KO from P9, 68.5 ± 13.4 s, n = 6), ataxia, death by 3–4 weeks. **O-KO and G-KO: no abnormality at all** — weight curves superimposed, survival 100% to ~150 days, log-rank **P = 1.0** |
| **Statistics** | Student's *t*-test on weights; log-rank Mantel–Cox on survival. N-KO n = 14 vs 12; S-KO n = 15 vs 13; O-KO n = 10 vs 11; G-KO n = 9 vs 8 |
| **Authors' reading** | WWOX's function *in neurons* is what matters for survival and CNS homeostasis |
| **Limitation** | O-KO/G-KO negative rests on gross phenotype and survival. Cre efficiency in O-KO/G-KO is validated only by immunofluorescence in Supplementary Fig. 1E/F, **which was not available to this read**. An incompletely recombining Olig2-Cre would produce the same null result |

**This is the strongest experiment in the paper** and the one that most directly licenses
"non-cell-autonomous". Figure 1J–O is unambiguous on inspection: no significance marks
anywhere, and survival curves flat at 100% out to a 150-day axis while N-KO/S-KO die inside
30 days.

### E2 — Neocortical hyperexcitability (Fig. 2)

| | |
|---|---|
| **Question** | Is the S-KO neocortex hyperexcitable? |
| **Model / tissue** | S-KO, S-HT, S-Control, P13–P17; in vivo LFP under anaesthesia + craniotomy; acute neocortical slices |
| **Result** | Large-amplitude bursting in superficial neocortex, **absent subcortically**. Burst duration 350 ms, amplitude 2.06 mV, inter-burst 8.62 s at 300 µm. Slice bursting 0% / 17% / 86% (S-Control / S-HT / S-KO). Evoked responses larger in S-KO |
| **Statistics** | Student's *t* on band power; Wilcoxon rank sum on evoked amplitudes |
| **Limitation** | Recordings under anaesthesia — between-group contrast holds, absolute rates are not those of a waking brain. Two internal inconsistencies and one over-general statement, all in §8 |

### E3 — Bulk RNA-seq and snRNA-seq (Fig. 3)

| | |
|---|---|
| **Result** | 730 up / 579 down (P < 0.01, fold change > 1.5) in S-KO cortex+hippocampus at P17; myelination and ensheathment GO terms down; 20 named oligodendrocyte/myelin genes down. Null, N-KO and S-KO hippocampi cluster **by WWOX status, not by Cre driver**. snRNA-seq: mature myelinating oligodendrocytes 15%, COPs 68%, OPCs 150% |
| 🔴 **Limitation** | **snRNA-seq is n = 1 versus n = 1.** The 15% / 68% / 150% figures come from one animal per genotype and carry no dispersion and no test. The clustering-by-genotype result (bulk) is the robust one |
| **Limitation** | Authors' own: snRNA-seq *"limited to abundant nuclear transcripts"*. No accession number is given — data are "available from the corresponding author upon reasonable request" |

### E4 — Myelin markers and oligodendrocyte counts (Fig. 4)

| | |
|---|---|
| **Result** | CNP and MBP reduced in S-KO cortex and cerebellum. Corpus callosum: CC1⁺ ≈155 → ≈72 (`***`), PDGFRα⁺ ≈43 → ≈70 (`*`). Text's "2-fold reduction in CC1" matches the panel (2.15×). **No significant oligodendrocyte cell death** (CC1 + cleaved caspase 3) |
| 🔴 **Limitation** | Fig. 4G plots ~10 points per group, and the caption says they are *"three independent sections of S-Control (n = 3) and S-KO mice (n = 3)"*. **The test is run over sections; the biological n is 3.** Sections within an animal are not independent replicates |

### E5 — Electron microscopy and axonal conduction (Fig. 5)

| | |
|---|---|
| **Result** | Corpus callosum myelinated axons/FOV 180 ± 40 → 55 ± 35; optic nerve unmyelinated axons/FOV 55 ± 20 → 270 ± 60. G-ratio significantly higher in S-KO in both structures. Conduction: N1 latency longer (`*P = 0.0104`), N1/N2 amplitude ratio reduced (`**P = 0.0030`) |
| **n** | 3 mice per genotype; 300 axons per genotype per structure for g-ratio |
| 🔴 **Limitation** | The headline fold-changes do not follow from the numbers in the same paragraph (§8). **N2 latency is explicitly n.s.** (§8). Statistics again over fields of view with biological n = 3 |

### E6 — DRG–OPC co-culture (Fig. 6)

| | |
|---|---|
| **Question** | Do WWOX-deficient *neurons* impair the differentiation of *wild-type* OPCs? |
| **Design** | Wild-type OPCs seeded on wild-type vs Wwox-null DRG neurons. WWOX confirmed present in WT-DRG, absent in KO-DRG (Fig. 6A) |
| **Result** | Pre-myelinating OLs ≈30% → ≈47% (`**`); myelinating OLs ≈46% → ≈28% (`**`); degraded OLs ≈21% → ≈22% (**n.s.**) |
| **n** | 4 per condition, two independent experiments |
| 🔴 **Limitation 1** | **The measure is compositional.** The three categories sum to ~100% in each group, so an increase in pre-myelinating *necessarily* depresses myelinating. The design cannot separate "fewer cells mature" from "the same cells redistribute", and the authors' "compensatory effect" reading is not separable from the constraint |
| 🔴 **Limitation 2** | **The neurons are DRG sensory neurons** — peripheral, not the neocortical/hippocampal neurons carrying the in vivo phenotype. The in vitro cell-non-autonomy is demonstrated in a PNS-axon/CNS-glia hybrid system |
| **Limitation 3** | Degraded-OL n.s. is consistent with E4's no-cell-death finding — a genuine internal corroboration |

### E7 — Olig2-Cre myelination test (Supplementary Fig. 8)

| | |
|---|---|
| **Question** | Does deleting Wwox *in oligodendrocytes* affect myelination? |
| **Result** | MBP staining in O-KO vs control littermates at P17 showed *"no major changes"* |
| 🔴 **Status** | **This is the decisive cell-autonomy control, and it lives entirely in a supplementary figure this read could not obtain.** The main text gives no quantification, no n, no statistic — only the phrase "no major changes". It is a qualitative negative at a single age with a single marker |

### E8 — Human oligocortical spheroids (Fig. 7)

| | |
|---|---|
| **Model** | WiBR hESC, CRISPR WWOX-KO; oligocortical spheroids |
| **Result** | Week 15 RMP −52.1 ± 0.90 mV (n = 3) vs −21.28 ± 6.91 mV (n = 4), `*P < 0.01`. LFP AUC 0.5–7.9 Hz higher in KO (`*P < 0.05`). Week 14 CC1⁺ down, OPC proportions similar; Week 20 CNP⁺ down, NG2⁺ not apparently changed; Week 30 MBP/CNP reduced; Week 37 EM more myelinated axons in WT |
| 🔴 **Limitation 1** | **Panels E, F and G carry no quantification whatsoever** — representative images only, no bar graph, no n-per-field, no test. The text nevertheless says Week 30 showed *"significantly reduced staining"* (§8) |
| 🔴 **Limitation 2** | **Panel I (the EM myelination quantification) has no error bars and no statistical test**, with n = 2 (WT) vs n = 3 (KO) organoids |
| **Limitation 3** | The KO is a **single clone**; no isogenic replicate clone is reported. Off-target and clone effects are not controlled |
| 🔴 **Limitation 4** | Authors state the RMP shift implies *"delayed development"*. A −21 mV RMP is also simply an immature/unhealthy neuron. The "hyperexcitability" and the "developmental delay" readings are not separated by any experiment here |

---

## 8 · Figures as primary evidence — panel/text relationships

All seven figures inspected as images at native 1000 px (≈150 ppi). Below, only relationships
that are actually present. The task asked me to search for `text_contradicted_by_panel` and
`panel_qualifies_text`; I did, and I report what the search found, including where it found
nothing.

### `text_contradicted_by_panel` — 2 instances

**T1 · Fig. 5D(ii) — N2 latency.**
Running text: *"the amplitude ratio of N1 and N2 showed a longer response latency of axonal
propagation [Fig. 5D(ii and iii)]"*. Panel (ii) plots N1 and N2 latency and marks N2
explicitly **`n.s`**; the caption gives **`N2 = 0.5737`**. The cited panel states the opposite
of what the sentence citing it asserts. **The conduction delay is confined to N1.**
*Statistics shown: yes. Absence of a mark: here the mark is present and reads `n.s` — NOT
SIGNIFICANT, not untested.*

**T2 · Fig. 2B caption vs running text — bursting rates.**
Text: S-HT **17%** (4/23), S-KO **86%** (36/42). Caption: S-HT **∼20%**, S-KO **∼84%**.
4/23 = 17.4% and 36/42 = 85.7%, so the *text* is arithmetically correct and the caption's two
figures match neither ratio. Minor in consequence, but it is a genuine numeric disagreement
between two surfaces of the same experiment.

### `panel_qualifies_text` — 5 instances

**Q1 · Fig. 5B — the headline fold-changes.**
Text asserts *"(∼3.5–4-fold)"* reduction in myelinated axons and *"(∼6-fold)"* more
unmyelinated axons. From the per-field averages in the same paragraph: 180/55 = **3.27×** and
270/55 = **4.91×**. From the caption's total axon counts: 2500/1200 = **2.08×** and
3000/500 = **6.0×**. So `∼6-fold` reproduces *only* the total-axon ratio, and
`∼3.5–4-fold` reproduces **neither**. Because the number of fields differs between genotypes,
the per-field ratio is the meaningful one — and it is the smaller one. The headline overstates
the panel in both directions of the comparison.

**Q2 · Fig. 5C — optic nerve g-ratio.**
Text: significantly higher g-ratio *"in S-KO corpus callosum and optic nerve"*. The corpus
callosum panel shows two clearly separated clouds and divergent regression lines. The optic
nerve panel shows **heavily overlapping clouds with near-coincident regression lines**. With
n = 300 axons a small shift reaches `P ≤ 0.001`; the panel qualifies the *magnitude*, not the
direction. The two structures are not equally affected, and the sentence reads as if they are.

**Q3 · Fig. 2D — which comparison is significant.**
Text: broad-band elevation *"encompassing delta (<5 Hz), theta (5–9 Hz), alpha (10–15 Hz), and
beta (15–30 Hz) rhythms both in vivo and in vitro"*. Caption: *"For 0–4.9Hz and 5–9Hz, S-KO
power was significantly elevated as compared with **S-Control only**"*. The delta/theta
elevation is **not** significant against the heterozygote.

**Q4 · Fig. 2F — evoked responses.**
Text: responses *"larger in the S-KOs as compared with the S-Controls and S-HTs"*. The panel
draws **one** bracket for the 1st peak (S-Ctrl↔S-KO, `*`) and **two** for the 2nd
(S-Ctrl↔S-KO `**`, S-HT↔S-KO `*`). The caption's P-values match: one value for the first peak,
two for the second. *"and S-HTs"* holds only for the second peak. For the first peak the S-HT
comparison is **NOT TESTED**, not non-significant.

**Q5 · Fig. 7G — "significantly".**
Text: OS-WWOX-KO *"displayed significantly reduced staining of both MBP and CNP (Fig. 7G)"*.
Panel G is images only; its caption gives n = 5 vs n = 5 and **no P-value and no test**. No
statistic is displayed anywhere for 7E, 7F or 7G. The word "significantly" has no visible
support on the cited panel.

### Where the search found nothing

Figures 1, 3, 4 and 6 show **no** contradiction and no qualification beyond what the text
already states. Fig. 1J–O in particular is a cleanly presented negative — the absence of
significance marks there means *tested and not significant* (log-rank P = 1.0 is printed in
the caption), not *untested*. I record this explicitly because the task asked me to search for
two states and not to manufacture them: four of seven figures yielded neither.

### Absence-of-mark semantics, per figure

| Figure | Unmarked comparison means |
|---|---|
| Fig. 1 K/N, L/O | **NOT SIGNIFICANT** — P = 1.0 printed |
| Fig. 2F 1st peak, S-HT vs S-KO | **NOT TESTED** — no bracket, and only one P-value given |
| Fig. 5D(ii) N2 | **NOT SIGNIFICANT** — `n.s` printed, P = 0.5737 |
| Fig. 6D degraded OLs | **NOT SIGNIFICANT** — `n.s` printed |
| Fig. 7E, 7F, 7G | **NOT TESTED** — no statistics displayed at all |
| Fig. 7I | **NOT TESTED** — no error bars, no test, n = 2 vs 3 |

---

## 9 · Supplementary material

**Recovered: none. 0 of 9 supplementary figures, 0 of 3 supplementary tables, 0 of 2 videos.**

| Route | Outcome |
|---|---|
| OUP article page `#supplementary-data` | **HTTP 403** |
| Silverchair supplementary ZIP (constructed path) | **HTTP 403** |
| Europe PMC supplementary API | n/a — article not in PMC |
| Crossref `link` / `relation` | no supplementary entries |
| PDF embedded attachments | `embfile_count = 0` |
| Local disk (whole `~/Desktop` sweep) | only the PDF and two `.fitz.txt` extractions |

The main text depends on the supplement, so this is not an optional gap. **Claims whose
verification is affected:**

| Supplement | Claim it carries | Consequence of absence |
|---|---|---|
| 🔴 **Supp. Fig. 8** | O-KO myelination unchanged at P17 | **The single most load-bearing item for cell-autonomy.** "Non-cell-autonomous" rests on it and it cannot be inspected |
| 🔴 **Supp. Fig. 1E/F** | Validation that Olig2-Cre and GFAP-Cre actually delete WWOX | Without it, the O-KO/G-KO null phenotype cannot be distinguished from **failed recombination** |
| **Supp. Fig. 1A–D** | N-KO and S-KO deletion validation; WWOX intact in S-KO oligodendrocytes | S-KO neuron-specificity unverified |
| **Supp. Fig. 6A–E** | NG2/CC1 double-positive counts; absence of oligodendrocyte apoptosis | The "differentiation block, not death" reading is unverified |
| **Supp. Fig. 5D–H, Fig. 7** | Hypomyelination in N-KO and Wwox-null | Generalisation beyond S-KO unverified |
| **Supp. Fig. 3** | Bursts absent subcortically | Neocortical-origin claim unverified |
| **Supp. Fig. 4A–D** | Cross-model clustering by WWOX status | Unverified |
| **Supp. Fig. 9A–D** | Spheroid protocol; LFP peak; WWOX in Tuj1⁺; Week 30 transcripts | Organoid claims partly unverified |
| **Supp. Tables 1–3** | Full DE gene lists | The 730/579 counts cannot be checked |
| **Supp. Videos 1–2** | N-KO and S-KO seizures | Seizure phenotype is video-documented and unviewed |

**Retrieval route that remains open and was not taken:** the handoff card records that a
residential-IP browser session (Zotero "Find Available PDF", or the operator's own browser)
obtained the article PDF where server-side requests were blocked. The same route is the
plausible way to the supplement. That is an operator action, not one I should take
unilaterally against a publisher bot-block.

---

## 10 · Verbatim locators

30 locators captured while the source was open. Each was verified programmatically against the
adjudicated surface, and each is classified by whether its span crosses a page-adjudicated
glyph.

**Result: 30/30 verified — 20 `STRICT`, 9 `HYPHEN_VARIANT`, 1 `SKELETON`; 25 `CLEAN`,
5 `ADJUDICATED`.**

- **`CLEAN`** = the span contains no adjudicated glyph. Verified against *both* the adjudicated
  surface and the original unrepaired PyMuPDF extraction. These 25 would have been capturable
  under FT-044's suspension.
- **`ADJUDICATED`** = the span crosses a page-adjudicated glyph. **All 5 fail against the raw
  extraction** — L05, L07, L11, L28, L30. These are exactly the locators the suspension made
  impossible, and exactly the ones that required rendering the page.

| ID | Proposition | Verbatim (abridged) | Anchor | Class |
|---|---|---|---|---|
| L01 | Four Cre models incl. oligodendrocyte- and astrocyte-specific | "…either neural stem and progenitors (using Nestin-Cre; N-KO), mature neurons (Synaspin I-Cre; S-KO), oligodendrocytes (Olig2-Cre; O-KO) or astrocytes (GFAP-Cre; G-KO)" | Introduction, p.3062 | CLEAN |
| L02 | O-KO/G-KO have no phenotype | "…ablating WWOX expression in oligodendrocytes…and astrocytes…and observed no phenotype abnormalities" | Results, p.3065 | CLEAN |
| L03 | O-KO/G-KO survival not different | "P-value 1.0, no significance, log-rank Mantel-Cox test" | Fig. 1 caption, p.3066 | CLEAN |
| L04 | Slice bursting, running text | "…17% of slices from S-HT…(4 of n = 23 slices across 14 animals) and 86%…(36 of n = 42 slices across 24 animals)" | Results, p.3065 | CLEAN |
| L05 | Fig. 2 caption disagrees | "four slices from three S-HT animals showed bursting (∼20%), and 36 slices from 20 S-KO animals showed bursting (∼84%)" | Fig. 2B caption, p.3067 | **ADJUDICATED** |
| L06 | Delta/theta vs S-Control only | "For 0–4.9Hz and 5–9Hz, S-KO power was significantly elevated as compared with S-Control only" | Fig. 2D caption, p.3067 | CLEAN |
| L07 | RNA-seq thresholds | "730 upregulated and 579 downregulated genes (P-value <0.01, fold change >1.5…)" | Results, p.3068 | **ADJUDICATED** |
| L08 | snRNA-seq n = 1 vs 1 | "snRNA-seq of S-Control (n = 1) and S-KO (n = 1) at P17" | Fig. 3F caption, p.3068 | CLEAN |
| L09 | OPC markers increased | "early OPC marker genes, such as Pdgfra and Cspg4 were slightly higher…" | Results, p.3068 | CLEAN |
| L10 | No oligodendrocyte death | "no significant oligodendrocyte cell death was observed in S-KO tissues when stained for CC1 and cleaved caspase 3" | Results, p.3069 | CLEAN |
| L11 | EM fold-changes as stated | "substantial reduction (∼3.5–4-fold)…significantly a greater number (∼6-fold) of unmyelinated axons" | Results, p.3069 | **ADJUDICATED** |
| L12 | Per-field EM averages | "(S-Control, average = 180 ± 40, S-KO, average = 55 ± 35)…(S-Control, average = 55 ± 20, S-KO, average = 270± 60)…per field of view" | Results, p.3069 | CLEAN |
| L13 | EM biological n = 3 | "compared with S-Control (n = 3) at P17" | Fig. 5A caption, p.3071 | CLEAN |
| L14 | N2 latency n.s. | "N1 *P = 0.0104; N2 = 0.5737 Wilcoxon rank sum test" | Fig. 5D caption, p.3071 | CLEAN |
| L15 | Stats over sections | "Data-points represent number of cells counted in the area (0.5 mm2) from three independent sections of S-Control (n = 3) and S-KO mice (n = 3)" | Fig. 4G caption, p.3070 | CLEAN |
| L16 | Co-culture result | "OPCs that were cultured with Wwox-null DRGs displayed significantly reduced differentiation into myelinating oligodendrocytes…" | Results, p.3070 | CLEAN |
| L17 | Co-culture is compositional | "Quantification of pre-myelinating, myelinating and degraded oligodendrocytes counted" | Fig. 6D caption, p.3072 | CLEAN |
| L18 | **O-KO myelination unchanged** | "we examined MBP staining in O-KO and control littermates at P17 and found no major changes (Supplementary Fig. 8)" | Results, p.3070 | CLEAN |
| L19 | Organoid RMP | "OS-WT RMP = –52.1 ± 0.90mV, OS-WWWOX-KO RMP = –21.28± 6.91 mV" | Fig. 7B caption, p.3073 | CLEAN |
| L20 | Organoid EM n = 2 vs 3 | "…percentage of myelinated and unmyelinated axons in OS-WT (n = 2) and OS-WWOX-KO (n = 3)" | Fig. 7I caption, p.3073 | CLEAN |
| L21 | Hyperexcitability precedes myelin | "the neuronal changes were observed as early as Week 15, a time point that was described in the literature to be still lacking myelin" | Discussion, p.3074 | CLEAN |
| L22 | Crosstalk mechanism unknown | "In-depth analysis of the molecular mechanism driving this impaired crosstalk…remains to be investigated further" | Discussion, p.3073 | CLEAN |
| L23 | Cell-autonomous roles not excluded | "we cannot exclude the cell autonomous functions of WWOX in oligodendrocytes or astrocytes in other neurological disorders" | Discussion, p.3073 | CLEAN |
| L24 | Activity vs alternative open | "It remains to be seen if neuronal WWOX impacts oligodendrocyte differentiation by neuronal activity or by an alternative mechanism" | Discussion, p.3074 | CLEAN |
| L25 | Hypomyelination→excitability unexplained | "Why hypo- or demyelination should cause local hyperexcitability remains unclear" | Discussion, p.3073 | CLEAN |
| L26 | E/I not quantified | "Further studies are needed to specify and quantify the imbalance between excitatory and inhibitory neuronal circuits" | Discussion, p.3073 | CLEAN |
| L27 | snRNA-seq limitation | "snRNA-seq, the latter limited to abundant nuclear transcripts" | Discussion, p.3073 | CLEAN |
| L28 | Significance threshold | "Results were considered significant when P < 0.05" | Methods, p.3065 | **ADJUDICATED** |
| L29 | No data accession | "The data and code that support the findings of this study are available from the corresponding author upon reasonable request" | Data availability, p.3065 | CLEAN |
| L30 | Fig. 4G uses ≤ thresholds | "Error bar represents ±SEM (*P ≤ 0.01, **P ≤ 0.001)" | Fig. 4G caption, p.3070 | **ADJUDICATED** |

**A method note paid for on the field.** The locator matcher first reported 5 false negatives.
None were surface defects — they were my normaliser. A line-break hyphen has **three** valid
reconstructions (`S-\nControl` → `S- Control`, `SControl`, or `S-Control`), and a fourth case
exists where one quote spans two hyphens needing *opposite* treatment (`S-\nControl` and
`cal-\nlosum` in the same sentence). Applying one rule uniformly produces silent misses. The
matcher now reports its **match tier** rather than a boolean, so a weak match is visible as a
weak match. `READ RECEIPT ≠ CLAIM SUPPORT`, and a matcher that hides its own tier is a receipt
pretending to be support.

---

## 11 · Observation / Author interpretation / LEGEND interpretation

### M1 — Neuronal, not glial, WWOX loss drives the disease phenotype

- **OBSERVATION.** N-KO and S-KO phenocopy the null (growth arrest, seizures, ataxia, death
  3–4 weeks). O-KO and G-KO are indistinguishable from controls on weight and survival to
  ~150 days, log-rank P = 1.0. [L01, L02, L03; Fig. 1]
- **AUTHOR INTERPRETATION.** WWOX's function in neurons is crucial for survival and CNS
  homeostasis.
- **LEGEND INTERPRETATION.** Supported, and this is the paper's most robust result — a
  four-arm comparison with concordant weight and survival read-outs and a printed negative
  statistic. **The one thing that would break it is not in view:** the Cre-efficiency
  validation for O-KO and G-KO is Supplementary Fig. 1E/F, unavailable. A poorly recombining
  Olig2-Cre yields exactly this result. Confidence high on the S-KO/N-KO positive arm;
  **conditional** on the O-KO/G-KO negative arm.

### M2 — Hypomyelination with an OPC differentiation block, not oligodendrocyte death

- **OBSERVATION.** Myelin transcripts down; CC1⁺ ≈2.15× fewer; PDGFRα⁺ ≈1.6× more; NG2/CC1
  double-positives down; no caspase-3 signal; EM shows fewer myelinated axons, more
  unmyelinated axons, higher g-ratio. [L07–L13; Figs. 3–5]
- **AUTHOR INTERPRETATION.** Myelination fails because mature oligodendrocytes are reduced,
  and that reduction is a differentiation defect.
- **LEGEND INTERPRETATION.** The *direction* is solidly supported and convergent across four
  independent modalities (transcriptome, immunofluorescence, EM, conduction) — that
  convergence is what carries it, not any single measurement. The *magnitudes* are not: the
  headline fold-changes are unreproducible from the paper's own numbers (Q1), the optic-nerve
  g-ratio effect is far weaker than the corpus callosum one (Q2), and the significance tests
  treat sections and fields as replicates when the biological n is 3 (L13, L15). **Treat the
  phenotype as established and every stated effect size as provisional.**

### M3 — The effect on OPCs is non-cell-autonomous

- **OBSERVATION.** (i) O-KO shows no myelin change at P17 [L18, Supp. Fig. 8, unseen];
  (ii) wild-type OPCs on Wwox-null DRG neurons shift from myelinating to pre-myelinating
  [L16, L17; Fig. 6].
- **AUTHOR INTERPRETATION.** Neuronal WWOX positively regulates OPC differentiation
  non-cell-autonomously; cell-autonomous roles are not excluded [L23].
- **LEGEND INTERPRETATION.** **This is the weakest link in the paper carrying the most
  downstream weight.** Both legs are compromised: leg (i) is a qualitative,
  single-marker, single-age negative reported only in an inaccessible supplement with no n and
  no statistic; leg (ii) is a *compositional* measure in a **PNS-axon/CNS-glia** hybrid whose
  categories are constrained to sum to 100%. Neither leg supplies a mediator — no molecule,
  no signal, no contact. The authors say so themselves in three separate sentences [L22, L24,
  L25]. **"Non-cell-autonomous" is best read as a description of where the *trigger* is, not
  as a mechanism.** It is `DATO` that neuronal deletion suffices and oligodendrocyte deletion
  (as tested) does not; it is `IPOTESI` that the route is a neuron→OPC instructive signal.

### M4 — Human relevance via oligocortical spheroids

- **OBSERVATION.** WWOX-KO spheroids: depolarised RMP at Week 15, higher low-frequency LFP
  power, fewer CC1⁺/CNP⁺ cells, less MBP/CNP at Week 30, fewer myelinated axons at Week 37.
  [L19, L20; Fig. 7]
- **AUTHOR INTERPRETATION.** The human model reproduces both phenotypes and supports
  translation.
- **LEGEND INTERPRETATION.** Directionally consistent, evidentially thin. A single KO clone;
  no isogenic replicate; panels E/F/G unquantified; panel I untested with n = 2 vs 3. And a
  −21 mV RMP is equally readable as an immature or unhealthy neuron — the authors' own
  "developmental delay" gloss says as much [Discussion], which sits awkwardly with reading the
  same measurement as epileptiform hyperexcitability. **Corroborative, not confirmatory.**

### M5 — Hyperexcitability and hypomyelination are not in a demonstrated causal order

- **OBSERVATION.** In spheroids the neuronal changes appear at Week 15, *"a time point…still
  lacking myelin"* [L21]. In mice, seizures start P9 and myelin/EM phenotypes are measured
  P17–P18.
- **AUTHOR INTERPRETATION.** The two phenotypes *"are not necessarily mutually exclusive"*;
  why hypomyelination should cause hyperexcitability *"remains unclear"* [L25].
- **LEGEND INTERPRETATION.** 🔴 **The organoid timing is a genuine dissociation and it points
  against the intuitive chain.** If excitability changes precede the existence of myelin, then
  hyperexcitability cannot be downstream of hypomyelination in that model. Both are more
  plausibly parallel consequences of neuronal WWOX loss. **Any model that routes
  WWOX-loss → hypomyelination → hyperexcitability is asserting an order this paper does not
  demonstrate and partially contradicts.**

---

## 12 · Negative evidence

Recorded with the same care as the positive findings.

| # | Negative | Locator |
|---|---|---|
| N1 | **O-KO and G-KO have no phenotype whatsoever** — weight, development, survival, log-rank P = 1.0 | L02, L03 |
| N2 | **O-KO myelination unchanged** at P17 | L18 |
| N3 | **No oligodendrocyte cell death** — CC1 + cleaved caspase 3 negative | L10 |
| N4 | **N2 conduction latency not significant** (P = 0.5737) despite the text | L14 |
| N5 | **Degraded oligodendrocytes unchanged** in co-culture (n.s.) | Fig. 6D |
| N6 | **Delta/theta power elevation not significant vs heterozygote** | L06 |
| N7 | **First-peak evoked amplitude: S-HT vs S-KO not tested** | Fig. 2F |
| N8 | **OPC proportions similar** in Week 14 spheroids; NG2⁺ not changed at Week 20 | Results |
| N9 | **Heterozygotes are phenotypically normal** in both Nestin and Synapsin lines | Results |
| N10 | **Optic-nerve g-ratio separation is visually marginal** despite P ≤ 0.001 | Fig. 5C |
| N11 | **No molecular intermediate identified** between neuron and OPC | L22, L24 |
| N12 | **E/I balance never measured** | L26 |
| N13 | **Fig. 7E/F/G carry no statistics at all**; Fig. 7I no test | Fig. 7 |
| N14 | **No data accession** — RNA-seq/snRNA-seq available "on request" only | L29 |

**Alternative explanations the paper does not exclude**

1. **Failed recombination** in O-KO/G-KO (validation supplementary, unseen) — would nullify N1
   and N2 and with them the cell-autonomy argument.
2. **Seizure-driven secondary hypomyelination.** Seizures begin P9; myelin is assayed P17–P18.
   Chronic seizure activity is itself capable of disrupting myelination. No seizure-suppressed
   arm exists, so a downstream-of-epilepsy account of the myelin phenotype is not excluded.
3. **Developmental arrest as a common upstream cause** — the −21 mV RMP and the OPC-stage shift
   are both compatible with generalised immaturity rather than a specific myelination program.
4. **Compositional artefact** in Fig. 6D (§7 E6).
5. **Clone effect** in the single hESC KO line.

**Human translation limits.** Mouse conditional deletion is not the human compound-heterozygous
genotype class; the reference genotype retains partial function whereas these models are
complete deletions in a cell type. The spheroid model is a complete `WWOX` knockout. Nothing
here addresses residual-function biology, which is where WOREE/SCAR12 severity actually varies.

---

## 13 · DisMech crosswalk

The task instructed me to measure the current DisMech WWOX YAML myself and not to trust
Plan v2's counts. I did. **The counts cannot be reproduced because the object they describe
does not exist.**

### What was measured, at `788c357`

| Search | Result |
|---|---|
| A DisMech WWOX **YAML** anywhere in the repo | **None.** `git ls-files '*.yaml' '*.yml'` returns 5 files: 3 skill `openai.yaml`, 1 GitHub workflow, 1 conda env |
| Any WWOX/WOREE `.yaml` anywhere on disk | **None** |
| `_external_repos/` | Contains **only** `MANIFEST.md` — no DisMech clone |
| `33914858` under `disease-models/wwox/analysis/` | **0 files** |
| `awab174`, `10.1093/brain`, `Repudi` | **0 files each** |
| `PAPER 004` / `PAPER_004` | **0 files** |
| `CLAIM 003` / `claim_003` | **0 files** |
| Claim scope of the Phase-2 sidecar | **`016`, `024`, `035` only** (14 / 21 / 14 records) — the filename `dismech_sidecar_016_024_035.jsonl` states it |
| Source scope of the sidecar | **PAPER 019, PAPER 055, PAPER 056 only** |
| Phase-3 dry run | Emitted **2 nodes**, both from one proposition (the WWOX 388–407 region), routed to MONDO:0014533 and MONDO:0013687 |

And the export specification says so in its own words:

> "**No node has been emitted and no YAML written, so nothing is in any output.** Renamed
> `ELIGIBLE_FOR_EXPORT`; `EXPORTED` is reserved for a Phase-3 dry run that actually writes."

### Verdict

**Number of current DisMech objects that depend on PMID 33914858: ZERO.**

Plan v2's report — "three pathophysiology nodes, two experimental/model objects, and a
substantial part of the controversy section" — is **not measurable against this repository**.
There is no WWOX YAML, no emitted node from this paper, and no DisMech record referencing it
by PMID, DOI, author, PAPER id or CLAIM id. The DisMech pipeline has never been pointed at
CLAIM 003.

**The assertion-by-assertion crosswalk the task requested therefore has an empty left-hand
column**, and filling it would mean inventing DisMech assertions in order to have something to
cross-walk. I decline to do that; the correct output is this measurement.

### What *is* true, and is the finding worth carrying

The dependency Plan v2 was probably reaching for is real, but it runs through LEGEND, not
DisMech:

```
PMID 33914858 (never read)
   └── PAPER 004  [integrated, no Evidence depth field]
          └── CLAIM 003  [consolidated baseline, DATO]
                 ├── evidence boundary written entirely from PAPER 005 (a different paper)
                 └── "Impact on Working Model: surveillance logic integrated"
                        └── MRI + DTI surveillance rationale  (WM_v4.3)
```

**A `consolidated baseline` `DATO` claim, whose source has zero receipts, is propagating into
working-model surveillance logic.** That is the actual exposure, and it is larger than a
DisMech node count would have been.

### Crosswalk against CLAIM 003 as written

| CLAIM 003 element | Primary evidence in this paper | Verdict |
|---|---|---|
| "Neuronal WWOX deletion induces…hypomyelination" | Figs. 3–5; L07–L13 | ✅ **Supported.** Convergent across 4 modalities |
| "…despite presence of OPCs" | PDGFRα⁺ increased; Pdgfra/Cspg4 up | ✅ **Supported** — and stronger than "presence": OPCs are *increased* |
| "non-cell-autonomous" | O-KO negative (Supp. Fig. 8, unseen) + DRG co-culture | ⚠️ **Partially supported.** Trigger localisation yes; mechanism no; one leg unavailable |
| "Justifies MRI + DTI before discussing myelination adjuncts" | g-ratio ↑, myelinated axons ↓, conduction N1 delayed | ⚠️ **Supported in direction only.** N2 n.s.; optic nerve marginal; magnitudes unreproducible |
| 🔴 Boundary note: *"Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici"* | **The Olig2-Cre deletion exists in this very paper** | ❌ **Factually wrong.** See §15 |

---

## 14 · Candidate atomic mechanistic propositions

Typed against DisMech/Pathograph semantics only where the evidence justifies it.

| # | SOURCE | RELATION | TARGET | EVIDENCE | LOCATOR | MODEL | TYPE | LIMITATION |
|---|---|---|---|---|---|---|---|---|
| P1 | Neuronal *Wwox* deletion | causes | postnatal lethality by 3–4 weeks | Kaplan–Meier, n = 15 vs 13 | L01, Fig. 1I | mouse S-KO | `DIRECT` | conditional deletion ≠ human hypomorphic genotype |
| P2 | Neuronal *Wwox* deletion | causes | neocortical epileptiform bursting | in vivo + slice LFP, 86% vs 0% | L04, Fig. 2A/B | mouse S-KO | `DIRECT` | anaesthetised; caption/text % disagree |
| P3 | Neuronal *Wwox* deletion | causes | reduced mature (CC1⁺) oligodendrocytes | IF, ≈2.15×, `***` | Fig. 4G | mouse S-KO | **`INDIRECT_UNKNOWN_INTERMEDIATES`** | no mediator identified [L22] |
| P4 | Neuronal *Wwox* deletion | causes | accumulation of PDGFRα⁺ OPCs | IF ≈1.6× `*`; qPCR | L09, Fig. 4G | mouse S-KO | **`INDIRECT_UNKNOWN_INTERMEDIATES`** | same |
| P5 | Reduced oligodendrocyte maturation | results in | hypomyelination (↓myelinated axons, ↑g-ratio) | EM | L11–L13, Fig. 5 | mouse S-KO | `DIRECT` | magnitudes unreproducible (Q1); optic nerve marginal (Q2) |
| P6 | Hypomyelination | results in | delayed axonal conduction | evoked N1 latency `*P = 0.0104` | L14, Fig. 5D | mouse S-KO | **`INDIRECT_UNKNOWN_INTERMEDIATES`** | **N1 only; N2 n.s.** Correlational — no myelin rescue |
| P7 | *Wwox*-null neurons | fail to promote | wild-type OPC → myelinating OL transition | co-culture, `**P < 0.01` | L16, L17 | mouse DRG+OPC in vitro | **`INDIRECT_UNKNOWN_INTERMEDIATES`** | compositional; PNS axons |
| P8 | Oligodendrocyte-restricted *Wwox* deletion | does **not** cause | myelin deficit or any phenotype | MBP at P17; survival P = 1.0 | L02, L03, L18 | mouse O-KO | *negative* | Supp. Fig. 8 unseen; Cre validation unseen |
| P9 | Human *WWOX* KO | causes | ↑low-frequency LFP power in oligocortical spheroids | AUC `*P < 0.05` | L19 | hESC organoid | `DIRECT` | single clone; n = 3 vs 4 |
| P10 | Human *WWOX* KO | causes | reduced CNP/MBP and fewer myelinated axons | IF Wk14/20/30; EM Wk37 | L20 | hESC organoid | **`INDIRECT_UNKNOWN_INTERMEDIATES`** | **no statistics on E/F/G/I** |
| P11 | Neuronal WWOX loss | produces | hyperexcitability **before** myelin exists | Week-15 changes pre-myelination | L21 | hESC organoid | *dissociation* | organoid timing only |

**Not proposed, deliberately.** No `hypomyelination → hyperexcitability` edge. The paper
states the mechanism is unclear [L25], and P11 is evidence *against* that ordering. Inventing
the edge would complete the graph and misrepresent the source.

---

## 15 · Scientific limitations, and proposed canonical corrections

### Limitations of this read

1. **0 of 9 supplementary figures obtained**, including the two most load-bearing
   (Supp. Fig. 8, Supp. Fig. 1E/F).
2. **Figure surface capped at ≈150 ppi.** No claim is made from features at that limit.
3. Five locators depend on page adjudication; the adjudicated surface is in the scratchpad and
   is **not** a canonical artefact.
4. Panel value estimates (≈155, ≈72, ≈30%, ≈47%) are read off plots, not tabulated data, and
   are recorded as approximations.
5. The panel denominator (45) is a reproducible lower bound, not the true inspectable-unit
   count.

### Proposed canonical corrections — **not applied**

| # | Target | Proposed change | Why |
|---|---|---|---|
| C1 | `claim_registry_current.md#CLAIM 003` | Correct the boundary note. It reads *"Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici"* — **an Olig2-Cre deletion exists in PAPER 004 itself** (L02, L18). The condition the note sets as absent is present, though it is reported only in an unobtained supplement | The note misstates the evidence base of its own source paper |
| C2 | `paper_registry_current.md#PAPER 004` | Add an `Evidence depth:` field stating `metadata_and_abstract_only — no receipt` | Every other read paper carries one; its absence makes an abstract-level record indistinguishable from an unexamined one |
| C3 | `full_text_queue_current.md#FT-044` | Append: the defect **mechanism is now established** (pi-font byte passthrough, 6 fonts, 89 glyphs, table in §4); the corruption is **broader than comparators** — it destroys `µ`, `°`, `∼`, `α`, `β`, `×`; `AdvPi2` `4` = **`≤`**, not `<`; the true `P [45] 0.0…` count is **18**, not 14 | FT-044 records the symptom and explicitly says the mechanism is unknown; it now is |
| C4 | `full_text_queue_current.md#FT-044` | Record that **25 of 30** load-bearing locators are capturable **without** touching an adjudicated glyph — the suspension need not have blocked the whole paper | The suspension was correct about the surface and over-broad about the reading |
| C5 | Text-surface sentinel | Add a **font-provenance** check: any glyph drawn in a pi/symbol subset font whose extracted byte is alphanumeric is suspect. This catches the `µ`/`∼` class that a comparator-shaped sentinel cannot | The current sentinel `\([Pp]\s+\d` would miss "50 mm" for "50 µm" entirely |
| C6 | `paper_registry_current.md` | Resolve `CORPUS-STUB-087` against PAPER 004 (same DOI), and advance `LIT-0110` from `discovered` | Flagged in the PAPER 004 note; still open |
| C7 | Locator verifier | A line-break hyphen has three reconstructions, and one quote can need two of them at once. Report a **match tier**, never a boolean | Produced 5 false negatives in this session (§10) |
| C8 | Plan v2 record | Correct the DisMech premise: there is no WWOX YAML and no DisMech object referencing this PMID | §13 |

**Receipt status.** This read has **not** been recorded as a receipt event. Whether an
adjudicated surface may back a `contemporaneous_receipt` is exactly the gate FT-044 says does
not yet exist, and issuing one here would decide that question by doing it.

---

## 16 · LEGEND BRAINSTORMING

Everything below is `INFERENCE` or `HYPOTHESIS` and none of it entered §1–§14.

- **`HYPOTHESIS` — the ordering is parallel, not serial.** WWOX loss in neurons produces
  hyperexcitability and a myelination deficit as two independent branches. Support: organoid
  excitability precedes myelin [L21]; authors cannot explain a causal link [L25]. **Testable:**
  suppress seizures in S-KO from P7 and re-measure P17 myelin. If myelin normalises, the
  myelin phenotype is downstream of epilepsy; if not, the branches are independent. This single
  experiment would discriminate two models the paper leaves entangled.
- **`INFERENCE` — the therapeutic window is narrower than "myelin".** If hypomyelination is
  parallel rather than causal, a remyelinating adjunct would not be expected to touch seizures.
  PAPER 005's neuron-only AAV rescue improving myelination is consistent with the trigger
  being neuronal in both branches.
- **`HYPOTHESIS` — activity-dependent myelination is the obvious mediator and is untested.**
  Neuronal activity and glutamate drive OPC differentiation (the authors' own refs 52–53). A
  WWOX-deficient neuron that is *hyperexcitable but developmentally immature* may fail to emit
  the right activity pattern. **Testable:** optogenetic pacing of Wwox-null DRGs in the Fig. 6
  co-culture — if physiological patterning rescues OPC maturation, the mediator is activity,
  not a secreted factor.
- **`HYPOTHESIS` — an oligodendrocyte-autonomous component may still exist.** N2/N3 are
  qualitative and single-age. PAPER 005's authors attribute residual post-rescue deficit to
  *"an oligodendrocyte-specific WWOX function"*. Two papers from one lab both gesture at it and
  neither tests it. **Testable:** O-KO at P30–P60 with g-ratio and EM, not MBP staining at P17.
- **`INFERENCE` — biomarker.** g-ratio/DTI is the read-out the mouse data most directly
  license, but the optic-nerve panel (Q2) suggests structure-dependence. If translated,
  corpus callosum should be the primary index and optic nerve a weak secondary — which is a
  refinement of the CLAIM 003 surveillance rationale rather than a change to it.
- **`HYPOTHESIS` — organoids as a screening platform.** The authors propose exactly this. The
  Week-15 electrophysiological phenotype arrives ~15 weeks earlier than the Week-30 myelin
  phenotype, so RMP/LFP is the practical screening end point — *if* the developmental-delay
  confound (M4) is resolved first with isogenic clones.
- **Connection to the corpus.** PAPER 005 (34747138) and PAPER 004 are **one research
  program**, not two independent confirmations. Any confidence weighting that treats them as
  independent replication of non-cell-autonomy is double-counting a single lab. Genuine
  independent replication of the Olig2-Cre negative does not exist in this corpus.

---

### Success condition

> **What does PMID 33914858 actually demonstrate, experiment by experiment and figure by
> figure?** — Answered in §7 and §8 for all 7 figures, 45 labelled panels and 8 experiments.

> **Which current DisMech WWOX assertions are genuinely anchored to that primary evidence?** —
> **None**, and §13 shows the measurement rather than an abstract-derived substitute. The real
> anchoring runs PAPER 004 → CLAIM 003 → working-model surveillance logic, and §13 crosswalks
> CLAIM 003 element by element.

**Unresolved evidence gap, stated rather than papered over:** the non-cell-autonomous claim's
decisive control (Supplementary Fig. 8) and the Cre-validation that makes the O-KO negative
interpretable (Supplementary Fig. 1E/F) were not obtainable. Until they are, "non-cell-
autonomous" is supported as a statement about where the trigger sits and unsupported as a
mechanism.
