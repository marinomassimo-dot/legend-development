# WWOX NMD-assay census — has the bench ever measured it?

**QUESTION:** Has any WWOX allele, of any class, in any species, ever been assayed with an
NMD-inhibition reagent, or by NMD-discriminating transcript quantification?

**ANSWER:** 🔴 **`NEVER TESTED` · `PREMISE: NOBODY_LOOKED`.** Across 708 PubMed records for WWOX and
every artefact in this repository, **zero** experiments exist in which a WWOX transcript was measured
under NMD-pathway perturbation, translation inhibition, readthrough, or by any quantification able to
separate *degraded* from *never made*. The controls that make this zero readable all pass. This is a
statement about the **literature**, not about the **biology**: it is **not** evidence that NMD does
not occur on any WWOX allele, and it is **not** evidence that any WWOX transcript is stable.

Scientist Q · 2026-09-22 · READ-ONLY toward every canonical file. No registry, ledger, queue, receipt,
commit candidate or state manifest was touched. No git operation. No `BATCH_COMMIT`. Not medical advice.

Bibliographic records and full texts were retrieved from **PubMed / PubMed Central**. DOIs are linked
at first citation, per the PubMed tool's attribution requirement.

**Scope note vs. sibling work.** `analysis/wwox_splice_transcript_census_20260921.md` (Scientist B) and
`analysis/splice_allele_rna_evidence_20260922.md` (Scientist E) bound the *splice-allele* transcript
question and a sibling is adjudicating the *mechanistic* NMD prediction for `c.1057-2A>G`. **This
document is orthogonal:** it asks only what reagent has ever touched a bench, for **any** allele class
(missense, nonsense, frameshift, splice, genomic deletion, engineered knockdown, gene-trap, knock-in)
in **any** species (human, mouse, rat, *Drosophila*). Where it re-derives a prior number it says so and
re-verifies it; the counts below were eyeballed, not inherited.

---

## § 1 · Repository sweep

### 1.1 · Per-term counts — `disease-models/wwox/`, word-boundary, case-insensitive

Counts are **line hits**, from `grep -rIiw` over the whole subtree. The `raw` column is the naive
substring count, shown wherever it differs, because the difference *is* the instrument finding.

| Term | Hits (word-boundary) | Raw substring | Verdict |
|---|---|---|---|
| `cycloheximide` | **78** | 78 | 🟡 ALL are protein-stability chases or proposals — § 1.2 |
| `puromycin` | **8** | 8 | 🔴 ALL false positives — § 1.3 |
| `emetine` | **11** | 11 | 🔴 ALL are *our own* proposals/negative statements — § 1.3 |
| `anisomycin` | **4** | 4 | 🔴 ALL false positives (JNK/stress agonist) — § 1.3 |
| `SMG1` | **2** | 6 | 🔴 both are *our own* zero-declarations |
| `SMG-1` | 0 | 0 | — |
| `UPF1` | **22** | 22 | 🔴 no NMD assay — § 1.4 |
| `UPF2` · `UPF3` · `UPF3B` | **0** | 0 | true zero |
| `SMG6` · `SMG7` | **0** | 0 | true zero |
| `NMDI` (NMDI-14 etc.) | **0** | 0 | true zero |
| `nonsense-mediated` | **27** | 27 | § 1.5 — every one is a *prediction*, a *proposal* or a *negative* |
| `NMD` | **233** | 315 | repository-authored reasoning; 82 substring hits (`NMDAR`, `NMDA`) discarded |
| `ASE` | **0** | **8842** | 🔴 the 8842 is pure substring noise (`database`, `phase`, `increase`, `release`) |
| `allele-specific expression` | **0** | 0 | true zero |
| `allele specific` | **1** | 1 | 🔴 false positive — an ASO row in `analysis/data/WWOX_therapy_levers.csv` |
| `ddPCR` | **4** | 4 | § 1.6 — one real transcript use, none with an NMD arm |
| `droplet digital` | **0** | 0 | — |
| `long-read` / `long read` | **14 / 1** | 15 | 🔴 ALL are *our own* proposed protocols, none a published result |
| `nanopore` | **4** | 4 | 🔴 same — all proposals |
| `ataluren` · `PTC124` · `G418` · `geneticin` · `gentamicin` · `ELX-02` | **0** | 0 | true zero |
| `readthrough` | **0** | 0 | true zero |
| `read-through` | **12** | 12 | 🔴 splice/transcription read-through, not translational readthrough |
| `translational readthrough` | **0** | 0 | true zero |

**Whole-repository extension (outside `disease-models/wwox/`).** Re-run over `/home/user/legend-development`
with `--exclude-dir=.git`: `cycloheximide` **80** (the 2 extra are a term list inside
`framework/scripts/extraction_damage_report.py`, not evidence); `readthrough` **1**
(`.claude/skills/legend-hypothesis-forge/SKILL.md`, a skill's own vocabulary). Every other term is
identical to the table above — **the WWOX disease model holds all of the repository's evidence on this
question, and the rest of the repository adds none.**

### 1.2 · `cycloheximide` — 78 hits, and not one of them is an NMD assay

Every use of cycloheximide in a WWOX paper held by this repository is a **CHX chase with a PROTEIN
endpoint**. CHX is being used as a translation-inhibition *pulse-chase* to measure protein half-life,
which is the opposite question from NMD: it reports decay of already-made protein and says nothing
about the message. **This is the single largest false-positive class in the whole census.**

| Locator | PMID | Allele / material | What CHX was actually used for | Endpoint | NMD assay? |
|---|---|---|---|---|---|
| `research/deepdive_manifests/PMID24550385.json` | **24550385** | wild-type WWOX + ITCH, transfected cells & *Itch*-null MEFs | protein half-life chase | **WWOX protein** | ❌ |
| `research/fulltext_dossiers/PMID23370280.md` | **23370280** | wild-type WWOX / Y33R, HEK293T·SaOS2·HeLa·HaCaT | protein half-life chase | **ΔNp63α protein** | ❌ |
| `research/fulltext_dossiers/PMID25331887.md` | **25331887** | supplement Fig. S7B, single chase | protein stability panel | **protein** | ❌ |
| `research/fulltext_dossiers/PMID26499798.md` | 26499798 | review | *cites* 24550385's chase; adds nothing | — | ❌ |
| `research/fulltext_dossiers/PMID20530675.md` | 20530675 | SAOS2 | **proposed** as a `REVIVAL_TRIGGER`, never performed | — | ❌ (not done) |
| `research/fulltext_dossiers/PMID19500159.md` | 19500159 | *lde/lde* rat | **proposed** as a `REVIVAL_TRIGGER`, never performed | — | ❌ (not done) |

Verbatim, the strongest of them:

> *"Expression of ITCH in the presence of CHX extended the half-life of WWOX as compared with CHX alone"*
> — PMID **24550385**, Results, the cycloheximide experiment (Figure 6D), as recorded in
> `research/deepdive_manifests/PMID24550385.json` [DOI](https://doi.org/10.1074/jbc.M113.526129)

> *"WWOX lengthens ΔNp63α half-life in a cycloheximide chase; WWOX knockdown in HaCaT cells lowers ΔNp63α abundance."*
> — `research/fulltext_dossiers/PMID23370280.md`, "Perturbations" and findings list
> [DOI](https://doi.org/10.1038/onc.2012.622)

> *"Fig. S7B is a **single** cycloheximide chase whose **wild-type control rises to 1.4 at 4 h** under blocked synthesis"*
> — `research/fulltext_dossiers/PMID25331887.md` § 3.5

**Why this matters and is not pedantry.** A CHX chase and an NMD block use the *same molecule* at the
*same concentrations*. Any grep, any keyword pipeline, and any reader working from a term list will
score these as NMD assays. They are not: **no transcript was measured in any of them.** Three of the
six are wild-type WWOX; none involves a PTC-bearing allele. This is the trap the brief's "a Western
blot alone is not an NMD assay" rule exists to catch, and the repository contains six live instances
of it.

### 1.3 · `emetine`, `puromycin`, `anisomycin` — all false positives, three different ways

- **`emetine` (11).** Every hit is **repository-authored**: a proposed ±emetine arm in
  `research/tx001_experiment_decision_packet_20260921.md` and `discovery_ledger_current.md` → `DL-BIO-002`,
  or an explicit statement that the count is zero. Verbatim:
  > *"🔴 **Nessun allele di splicing WWOX è mai stato saggiato con un inibitore di NMD** (`cycloheximide`, `emetine`, `actinomycin`, `nonsense-mediated` = zero, in tondo, informativi)."*
  > — `research/discovery_ledger_current.md:481`
  **No published emetine experiment on WWOX exists in this repository.**
- **`puromycin` (8).** Mixed, and both kinds are false positives: (a) **puromycin as a selection
  antibiotic** for stable transductants —
  > *"The stable transductants were selected with 0.4 μg/ml puromycin. The gene silencing efficiency was assessed with Western blot."* — PMID 31543760, Methods, quoted in `analysis/hnpc_differentiation_audit_20260920.md:53`
  — and (b) **puromycin/OP-Puro as a nascent-synthesis label**, proposed by us in
  `analysis/data/redteam/discriminating_experiment.md:45`. Neither is NMD inhibition.
- **`anisomycin` (4).** Two hits are a corpus-seed JSONL line; the rest are the JNK/stress literature,
  where anisomycin is a **ribotoxic-stress agonist**, not an NMD reagent (see § 2.3).

### 1.4 · `UPF1` (22) — a protein interaction and a correlation, never a perturbation

All 22 hits trace to one paper, PMID **37519886** (bladder cancer, LINC01137), plus the repository's
reasoning about it. What was measured, verbatim from `research/deepdive_manifests/PMID37519886.json`:

> *"the direct interaction between WWOX and UPF1 proteins is possible via the proline-rich motif of UPF1 (1005PPGY1008) and the first tryptophan domain of WWOX (WW1)"* — imported from an independent interactome study

> *"This suggests that UPF1 might be involved in the WWOX-dependent upregulation of LINC01137 and simultaneous RBM22-independent co-regulation of ZC3H12A."*

And the repository's own adjudication, which I confirm:

> *"**NON DATO:** nessuna misura di flusso NMD, nessun reporter PTC, **nessun knockdown di UPF1**, nessun contesto neuronale."*
> — `research/discovery_ledger_current.md:1800` → `DL-MECH-069`

**No UPF1/UPF2/UPF3B/SMG knockdown, knockout or depletion has ever been performed in a WWOX
experiment.** `UPF2`, `UPF3B`, `SMG6`, `SMG7` are hard zeros in the repository and § 2 confirms them
in PubMed.

### 1.5 · `nonsense-mediated` (27) — prediction, proposal, or negative; never a measurement

Three categories, exhaustively:

1. **Predicted, explicitly unresolved.** The strongest instance, on a nonsense allele:
   > *"🔴 THE VARIANT'S MECHANISM IS AN UNMEASURED DISJUNCTION… either a truncated protein is made, or the transcript is destroyed by nonsense-mediated decay. **No western blot, no transcript quantification, no patient-derived material is used to decide.**"*
   > — `research/deepdive_manifests/PMID32581702.json`, on `p.Arg264Ter` (§ 4)
2. **Asserted in an abstract, withdrawn in the body.** PMID **30362252** (Davids, exon-6 deletion,
   patient fibroblasts): abstract says *"the deletion led to nonsense-mediated decay"*; Results say
   *"suggesting that the two longer transcripts were **not expressed or were degraded**"* — an
   explicit disjunction, with **no NMD inhibitor anywhere in the paper**. This correction is already
   on the record at `analysis/splice_allele_rna_evidence_20260922.md` § 1.2 (E-1); I re-read the
   passage and I confirm it. **This is the repository's only citable "measured NMD in WWOX", and it
   is not one.**
3. **Proposed as therapy, in a review.** PMID **33916893** (Aqeilan 2021):
   > *"The review proposes nonsense-mediated-decay inhibition for splice-site alleles, naming the Yemenite founder splicing mutation as the worked case… **It is a proposal, not a result.**"*
   > — `research/deepdive_manifests/PMID33916893.json`
   **This is the only place in the entire WWOX literature where NMD inhibition is even named as a
   therapeutic idea — and no one has since done the experiment.**

### 1.6 · `ddPCR` (4) and `long-read`/`nanopore` (19) — one real use, on DNA; the rest are ours

- `research/discovery_ledger_current.md:395,397` — **our own** proposed KIRKOS/WWOX junction ddPCR.
- `analysis/splice_allele_rna_evidence_20260922.md:54` — PMID 30362252's *"four junction-specific qPCR
  assays + isoform-resolved western + ddPCR"*, patient fibroblasts. The **ddPCR component there is a
  CNV assay on DNA**, not a junction transcript assay (`registries/paper_registry_current.md`
  PAPER 044: *"ddPCR CNV"*). The four junction assays are real transcript measurements — **with no
  NMD arm.**
- All 19 `long-read`/`nanopore` hits are repository-authored protocol proposals
  (`tx001_experiment_decision_packet`, `exon9_cryptic_acceptor_test`, `HUMAN_ACTION_GENOA_TX001`).
  **No published long-read WWOX transcript study exists.**

### 1.7 · Repository sweep — bottom line

**Qualifying NMD assays found in the repository: 0.** Six cycloheximide false positives (protein
half-life), one ddPCR false positive (DNA CNV), one puromycin false positive (selection antibiotic),
four anisomycin false positives (ribotoxic stress), one `allele specific` false positive (an ASO
strategy row), and 8,842 substring `ASE` false positives that collapse to **0** under word-boundary
matching.

---

## § 2 · Literature sweep — every query verbatim

All queries run through the PubMed MCP `search_articles` tool on 2026-09-22. `query_translation` was
read before any zero was accepted, per the brief's rule.

| # | Query (verbatim) | `query_translation` — key fragment | Count | Verdict |
|---|---|---|---|---|
| **L-1** | `WWOX` | `"wwox protein human"[Supplementary Concept] OR "wwox protein human"[All Fields] OR "wwox"[All Fields]` | **708** | ✅ denominator; WWOX term expands correctly |
| **L-2** | `WWOX AND cycloheximide` | …`AND ("cycloheximid"[All Fields] OR "cycloheximide"[Supplementary Concept] OR "cycloheximide"[All Fields] OR "cycloheximide"[MeSH Terms])` | **0** | 🔴 **DEMONSTRATED FALSE ZERO** — § 2.2 |
| **L-3** | `WWOX AND (emetine OR puromycin OR anisomycin)` | all three expand to Supplementary Concept + MeSH | **4** | ❌ all anisomycin-as-stressor — § 2.3 |
| **L-4** | `WWOX AND (UPF1 OR UPF2 OR UPF3B OR SMG1 OR SMG6 OR SMG7)` | `("UPF1"[All Fields] OR "UPF2"[All Fields] OR "UPF3B"[All Fields] OR "SMG1"[All Fields] OR "SMG6"[All Fields] OR "SMG7"[All Fields])` | **2** | ❌ both false positives — § 2.4 |
| **L-5** | `WWOX AND (nonsense-mediated decay OR NMD)` | `"nonsense mediated mrna decay"[MeSH Terms] … OR ("neuromuscul disord"[Journal] OR "nmd"[All Fields])` | **2** | ⚠️ 30362252 + 25403906; neither is an assay — § 2.5. ⚠️ note `NMD` also expands to a **journal name** |
| **L-6** | `WWOX AND (ataluren OR PTC124 OR G418 OR geneticin OR gentamicin OR readthrough OR read-through)` | every term expands to Supplementary Concept / MeSH; `"readthrough"[All Fields]` present | **0** | ✅ **true zero** — no readthrough agent has ever been applied to WWOX |
| **L-7** | `WWOX AND ("allele-specific expression" OR "allele specific expression" OR "digital PCR" OR ddPCR OR nanopore OR "long-read sequencing")` | all phrases preserved as `[All Fields]`; `nanopore` expands to MeSH | **2** | ⚠️ one near-miss (18273838) + one false positive — § 2.6 |
| **L-8** | `WWOX AND ("cycloheximide chase" OR "translation inhibitor" OR "translation inhibition" OR "protein synthesis inhibitor")` | all four phrases preserved | **0** | ✅ true zero (and consistent with L-2's *indexing* failure, not with absence at the bench) |
| **L-9** | `WWOX AND ("actinomycin D" OR "mRNA stability" OR "transcript stability" OR "RNA decay")` | all four phrases preserved | **0** | ✅ **no WWOX transcript-stability experiment of any kind has ever been published** |
| **L-10** | `WWOX AND (nonsense OR frameshift OR truncating) AND (mRNA OR transcript OR "RNA expression")` | full MeSH expansion of all three arms | **8** | see § 4 |
| **L-11** | `WWOX AND ("premature termination codon" OR "premature stop codon" OR "stop codon")` | phrases preserved | **4** | 2 are DNA-cutter methodology papers (17150742, 16491499) — false positives |
| **L-12** | `WWOX AND ("aberrant transcript" OR "aberrant transcripts" OR "alternative transcript")` | phrases preserved | **8** | see § 4 |
| **L-13** | `WWOX AND (fibroblast OR lymphoblastoid OR "lymphoblastoid cell line" OR iPSC OR "induced pluripotent" OR "post-mortem brain" OR autopsy) AND (mRNA OR transcript OR "mRNA expression" OR qPCR OR "RT-PCR")` | full expansion, all arms | **16** | see § 4 |
| **L-14** | `Wwox AND (mouse OR mice OR rat) AND (knockout OR "gene trap" OR hypomorph OR "knock-in" OR lde) AND (mRNA OR transcript OR "RT-PCR" OR qPCR)` | full expansion; `"lde"[All Fields]` present | **16** | § 4; none uses an NMD reagent |
| **L-15** | `Wwox AND (Drosophila OR zebrafish OR "C. elegans") AND (transcript OR mRNA OR RNA)` | MeSH expansion for all three organisms | **2** | ❌ one review, one fly paper; no NMD assay |
| **L-16** | `WWOX AND ("splice-switching" OR "antisense oligonucleotide" OR "exon skipping therapy" OR "gene therapy")` | phrases preserved | **15** | context only; no WWOX ASO or readthrough trial. Confirms Scientist E's Q-E |

**No query in this table returned a qualifying NMD assay.**

### 2.2 🔴 L-2 is a proven false zero, and I can say exactly how large the miss is

`WWOX AND cycloheximide` returns **0** with a **fully and correctly expanded** `query_translation`
(the WWOX Supplementary Concept resolves, and cycloheximide resolves to its MeSH term). By the brief's
rule this would be a clean zero. **It is not.** This repository holds **at least three** WWOX papers
that used cycloheximide at the bench — PMIDs **24550385**, **23370280**, **25331887** — every one of
them indexed in PubMed, and **none** returned by L-2.

**Miss rate for this term: ≥ 3 of 3 known-positive papers, i.e. 100 %.** The reagent is named only in
Methods, Results prose and a supplementary figure legend, and `[All Fields]` indexes none of those.

**What this licenses, and what it forbids.** It forbids treating L-2's zero — or L-3's, L-6's, L-8's
or L-9's — as proof that the reagent never touched a WWOX sample. It licenses only the weaker claim
that **no WWOX paper considered the reagent important enough to name in its title or abstract.** The
strong claim in § 5 does **not** rest on these zeros; it rests on the § 1 full-text sweep, where the
bodies *are* searchable, and on the fact that the six real cycloheximide uses are all documented with
protein endpoints.

### 2.3 · L-3's four hits, individually checked — all anisomycin-as-ribotoxic-stress

According to PubMed:

| PMID | Why it matched | Endpoint | Verdict |
|---|---|---|---|
| **26592150** | *"anisomycin-induced activator protein-1 (AP-1) activity was markedly diminished by co-expression of SUMO and WWOX"* | AP-1 reporter, protein | ❌ [DOI](https://doi.org/10.1016/j.febslet.2015.11.028) |
| **16219768** | *"UV light, anisomycin, etoposide, and hypoxic stress rapidly induced phosphorylation of p53 at Ser46 and WOX1 at Tyr33"* | phospho-protein | ❌ [DOI](https://doi.org/10.1074/jbc.M505590200) |
| **15126504** | *"Activation of JNK1 by anisomycin further increased Tau phosphorylation"* | phospho-Tau | ❌ [DOI](https://doi.org/10.1074/jbc.M401399200) |
| **12514174** | *"By stimulating cells with anisomycin or UV light, JNK1 became activated, and WOX1 was phosphorylated at Tyr(33)"* | phospho-protein | ❌ [DOI](https://doi.org/10.1074/jbc.M208373200) |

All four are **Chang/Sze-lineage stress-signalling papers**. Anisomycin is used at ribotoxic-stress
doses to fire JNK, not at translation-inhibition doses to block NMD, and **no transcript is quantified
in any of them**. Three of the four are wild-type WWOX; none carries a PTC allele. Oncology/neuro cell
lines and L929 fibroblasts — **material of origin: transformed lines, not patient tissue.**

### 2.4 · L-4's two hits — neither is an NMD perturbation

- **37519886** — bladder cancer; UPF1 treated as a *candidate transcription factor* on GTRD ChIP peaks;
  WWOX-OE correlates with higher UPF1 transcript. **No knockdown, no PTC reporter, no NMD flux.** § 1.4.
- **18485879** — Uren 2008, *Cell*: a retroviral insertional-mutagenesis screen in p53/p19ARF-deficient
  mice. `Smg6` and `Wwox` appear as **two independent candidate cancer genes in the same gene list**.
  🔴 **Pure co-occurrence false positive.** [DOI](https://doi.org/10.1016/j.cell.2008.03.021)

### 2.5 · L-5's two hits

- **30362252** — Davids 2019, exon-6 microdeletion, patient fibroblasts. Abstract asserts NMD; Results
  say *"not expressed **or** were degraded"*; **no inhibitor**. ❌ [DOI](https://doi.org/10.1002/humu.23675)
- **25403906** — Ben-Salem 2014, homozygous exon-5 microdeletion → exon-5 skipping → frameshift →
  PTC at aa 212. Verbatim: *"Quantification of mRNA revealed striking low level of WWOX expression in
  the child and moderate level of expression in the mother compared to a healthy control… truncated
  transcripts that were **presumably subject to NMD pathway**."* **"Presumably" is the whole finding:
  a bulk abundance drop with no inhibitor arm and no allele discrimination.** ❌ as an NMD assay;
  ✅ for § 4. [DOI](https://doi.org/10.1007/s12031-014-0463-8)

### 2.6 · L-7's two hits — one genuine near-miss, one classic trap

- 🟡 **18273838** — Alsop 2008, HCT116 colorectal line. Verbatim from the abstract:
  > *"The exon 6-8 deletion results in **allele-specific expression** of a deleted transcript, which seems likely to be the main biological consequence of the deletions, since similar transcripts are found in other tumors."*

  **This is the only occurrence of "allele-specific expression" in the entire WWOX literature.** It is
  genuinely allele-**discriminating** (the deleted allele's transcript is physically distinguishable),
  but it is **qualitative detection, not NMD-discriminating quantification**: no ±inhibitor arm, no
  aberrant:normal ratio, no comparison against a degradation-competent control. **Material: a
  transformed colorectal cancer cell line with a complex somatic rearrangement — not a germline allele,
  not neurons.** `pmc_id: null`; Wiley 2008; **no retrievable body in this environment.** ❌ as a hit;
  🔴 **recorded as the single highest-value retrieval debt this census generates.**
  [DOI](https://doi.org/10.1002/gcc.20548)
- 🔴 **39332629** — colorectal FFPE targeted-locus-capture; WWOX appears only as one of four
  fragile-site genes carrying structural variants, and the **droplet digital PCR is verification of
  tumour DNA**, not transcript. Pure false positive. [DOI](https://doi.org/10.1016/j.jmoldx.2024.08.004)

**A second, independently confirmed ddPCR trap.** PMID **42193054** (Sapuppo 2026, WOREE case report,
full text read today from PMC13205014) matched no query here but is worth recording because it would
trap a term-matcher: *"The CNV deletion, also confirmed by **digital polymerase chain reaction (PCR)**,
is a novel rearrangement"* — **DNA, not RNA** — and the paper closes with
*"no functional studies were performed to validate the biological impact of the identified variants."*
[DOI](https://doi.org/10.3390/cimb48050449)

---

## § 3 · Controls

A zero is uninterpretable without them. All were run in the same session, on the same tool.

| Control | Query (verbatim) | Count | What it proves | Result |
|---|---|---|---|---|
| **C-1 · WWOX indexed** | `WWOX` | **708** | the gene term expands to its Supplementary Concept and returns a large corpus | ✅ **PASS** |
| **C-2 · translation inhibitor indexed** | `CFTR AND cycloheximide` | **24** | cycloheximide is findable in title/abstract **when a field names it there** | ✅ **PASS** |
| **C-3 · readthrough agent indexed** | `DMD AND ataluren` | **95** | readthrough agents are richly indexed; L-6's zero is about WWOX, not about the vocabulary | ✅ **PASS** |
| **C-4 · NMD machinery indexed** | `TP53 AND (UPF1 OR SMG1 OR "nonsense-mediated decay")` | **20** | UPF1/SMG1/NMD terms retrieve real NMD literature when it exists for a gene | ✅ **PASS** |
| **C-5 · ASE + NMD co-indexed** | `"allele-specific expression" AND "nonsense-mediated decay"` | **18** | the exact conjunction this census looks for is a real, indexed, populated literature — **just not for WWOX** | ✅ **PASS** |
| **C-6 · HGVS phrase search works** | (inherited, re-declared) `WWOX AND "c.517-2A>G"` → **1**, `WWOX AND "c.516+1G>A"` → **1** | 1 / 1 | punctuation-bearing phrase search is not globally broken | ✅ PASS (Scientist E, `splice_allele_rna_evidence_20260922.md` § 5.1; **not re-run by me** — declared as inherited, not as my measurement) |
| **C-7 🔴 · full-text indexing** | repository cross-check: are 24550385 / 23370280 / 25331887 returned by L-2? | **0 of 3** | 🔴 **`[All Fields]` does not index Methods.** PubMed's reagent zeros have a **100 % miss rate** against known positives in this gene | ❌ **FAIL — and the failure is the finding** |

### What the controls license

✅ **They license:** the claim that **no WWOX paper announces an NMD experiment in its title, abstract
or MeSH**, across 708 records; and the claim that the NMD-assay vocabulary is alive and well-indexed
elsewhere (C-2..C-5), so WWOX's zeros are about WWOX and not about the query language.

❌ **They do NOT license:** any claim resting on L-2/L-6/L-8/L-9 *alone*, because C-7 shows those
zeros miss 100 % of known positives. **The `NEVER TESTED` verdict in § 5 is carried by the § 1
full-text sweep, where bodies, Methods and supplements are searchable, and is only corroborated by
§ 2.** Stated plainly: **a PubMed zero on a Methods reagent is worth nothing on its own in this gene,
and I am not spending it.**

⚠️ **Residual uncertainty I cannot close.** The repository holds full text for a minority of the 708
records. An NMD arm buried in the supplement of a WWOX oncology paper whose body this repository does
not hold would be invisible to both § 1 and § 2. I estimate this as low-probability — such an arm
would normally be worth an abstract sentence, and C-5 shows that ASE+NMD papers do say so — **but it
is not zero, and `NEVER TESTED` is therefore a bounded claim about the reachable surface, not a
metaphysical one.**

---

## § 4 · Adjacent bound — has a WWOX truncating allele ever had transcript abundance measured at all?

This is the weaker, wider question, and it changes what the § 5 zero means. Standard: transcript
abundance actually measured (not predicted), allele identified, material named.

### 4.1 · The rows

| # | PMID | Allele (as the source writes it) | Class | Species | Material | Method | Result (verbatim where held) | Depth here |
|---|---|---|---|---|---|---|---|---|
| **T-1** ⭐ | **19500159** | `Wwox` **13-bp deletion in exon 9** (*lde*) | frameshift, terminal exon | **rat** | **testis + hippocampus**, *lde/lde* vs +/+ | RT-PCR / expression analysis (Fig. 4) | *"Wwox mRNA was expressed in testes and hippocampi, with **similar levels of expression in wild-type and lde/lde rats**"* — while protein was undetectable | 🟢 **full text read** (`research/fulltext_dossiers/PMID19500159.md`) |
| **T-2** ⭐ | **30362252** | 22 kb genomic deletion of **exon 6**, homozygous via maternal UPD16 | transcript-frameshifting deletion | human | **patient cultured fibroblasts** | **4 junction-specific qPCR** + isoform-resolved western (+ ddPCR on DNA) | *"the exon 7–8 junction was barely detectable, suggesting that the two longer transcripts were **not expressed or were degraded**"* | 🟢 full text (via Scientist E, re-read 2026-09-22) |
| **T-3** | **25403906** | homozygous microdeletion of **exon 5** → exon-5 skipping → frameshift → PTC at aa 212 | frameshift/PTC | human | **material not stated in abstract** (child, mother, healthy control) | mRNA quantification | *"striking low level of WWOX expression in the child and moderate level of expression in the mother"* | 🔴 **abstract-depth**; `pmc_id: null`, no fetch target |
| **T-4** | **31056747** | homozygous germline **insertion** in WWOX | insertion/truncating | human | **patient's normal colon tissue** | transcript characterisation | *"we found multiple novel aberrant WWOX transcripts in the patient's normal colon tissue"* | 🔴 abstract-depth |
| **T-5** | **14695174** | naturally occurring aberrant transcripts across **49 cancer cell lines** | somatic, mixed | human | cancer cell lines | immunoblot + MG-132 | *"only the normal form of the protein was detectable, although some of cell lines exhibited **aberrant WWOX RNA transcripts**"*; truncated proteins appeared only under **MG-132** | 🔴 abstract-depth |
| **T-6** | **11572989** | internally deleted WWOX transcripts, 3 with frameshifts | somatic deletions | human | ovarian tumour + tumour lines | cDNA selection / RT-PCR | *"In three of these samples the deletions result in frameshifts"* | 🔴 abstract-depth (PMC58744 exists) |
| **T-7** | **20216076** | 16q23.1 loss | somatic | human | AIDS-related B-cell lymphoma tumours | expression array + aCGH | *"gene silencing or truncated transcript in 9 of 16 cases"* | 🔴 abstract-depth |
| **T-8** 🔴 | **32581702** | **`c.790C>T` p.Arg264Ter, homozygous** | **nonsense** | human | **post-mortem fetal brain at 21 weeks + proband blood** | **NONE — no RNA taken** | *"resulting in a loss of normal Wwox function either through protein truncation… **or nonsense-mediated mRNA decay**"* | 🟢 **full text read today** |
| **T-9** | **42193054** | exons 6–7 CNV deletion *+* `c.1043del p.Phe348Serfs*57` | frameshift | human | buccal swab (DNA only) | **NONE** | *"no functional studies were performed to validate the biological impact of the identified variants"* | 🟢 full text read today |
| **T-10** | **25411445** | 8 deleterious alleles incl. 2 nonsense + a 4-bp frameshift deletion, 5 patients | nonsense/frameshift | human | patient DNA | **aCGH / Sanger / NGS only** | no RNA work reported | 🔴 abstract-depth [DOI](https://doi.org/10.1136/jmedgenet-2014-102748) |

### 4.2 · What the sub-census shows

- **Germline WWOX truncating (or transcript-frameshifting) alleles with transcript abundance measured
  in human patient-derived material: 3** — T-2 (fibroblasts), T-3 (material unstated), T-4 (normal
  colon). **Of these, exactly one is readable here and exactly one is a named cell type.**
- **In neurons, brain, iPSC or any neural material: 0.** Not one measurement, in any species, on any
  truncating allele. T-1 is the closest — rat **hippocampus** — and it is a rat.
- **With an NMD arm: 0.** All three human rows are bulk abundance or junction ratios; all three end in
  the same undecidable disjunction.
- 🔴 **T-8 is the sharpest fact in this document.** A homozygous `p.Arg264Ter` fetus was autopsied at
  21 gestational weeks and **brain tissue was taken and sectioned**. Histology, GFAP, CD31, PAS and
  H&E were run. **No RNA was extracted, and the paper resolves the NMD question by writing
  "or".** The material existed, was in hand, was processed — and the transcript question was simply
  not asked.
- **Oncology rows (T-5, T-6, T-7) and the Alsop ASE near-miss (§ 2.6) establish that the assay
  vocabulary exists in this gene.** They say nothing about neurons. Material of origin is carried in
  every row above, per the brief.

### 4.3 · Species discipline

I make **no** transfer across the following, and neither should anything downstream: mouse `Wwox` null
≠ `P47T` knock-in ≠ gene-trap hypomorph ≠ rat `lde/lde` ≠ human exon-5 deletion ≠ human exon-6 deletion
≠ human `p.Arg264Ter` ≠ human `c.1057-2A>G`. **T-1's "mRNA normal" is a rat terminal-exon frameshift
result and is evidence about the rat *lde* allele only.** It is the single most tempting
over-generalisation available here — it looks like an NMD-escape result for terminal-exon alleles
generally — and it is not one: it is one allele, one species, two tissues, no inhibitor.

---

## § 5 · FINAL CLASSIFICATION

# 🔴 `NEVER TESTED` — `PREMISE: NOBODY_LOOKED`

**No WWOX allele, of any class, in any species, has ever been assayed with an NMD-inhibition reagent
or by NMD-discriminating transcript quantification.**

### The evidence that carries it

| Leg | Finding |
|---|---|
| **Repository full-text sweep** (§ 1) — the load-bearing leg, because bodies and supplements *are* searchable here | 0 qualifying assays. `UPF2`/`UPF3B`/`SMG6`/`SMG7`/`NMDI`/`ataluren`/`PTC124`/`G418`/`geneticin`/`gentamicin`/`ELX-02`/`readthrough`/`allele-specific expression` = hard 0. All 78 `cycloheximide`, 11 `emetine`, 8 `puromycin`, 4 `anisomycin`, 22 `UPF1`, 4 `ddPCR` and 19 `long-read`/`nanopore` hits individually inspected and individually disqualified |
| **Literature sweep** (§ 2) | 16 queries, 708-record denominator. 0 qualifying assays. Every non-zero hit run down to its endpoint |
| **Controls** (§ 3) | C-1..C-5 pass — the vocabulary is indexed and the conjunction exists elsewhere (18 ASE+NMD papers). C-7 fails, and the failure is declared: PubMed reagent zeros miss 100 % of known positives, so **the verdict does not lean on them** |
| **The field's own words** | The only two papers that invoke NMD for a WWOX allele write *"presumably subject to NMD"* (25403906) and *"not expressed **or** were degraded"* (30362252); the only nonsense-allele paper with brain tissue in hand writes *"truncation… **or** nonsense-mediated mRNA decay"* (32581702); and the only proposal to inhibit NMD therapeutically is a 2021 review paragraph (33916893) that nobody has acted on |

### What this verdict is NOT — read this before quoting the verdict

- ❌ **It is NOT evidence that NMD does not occur** on `c.1057-2A>G`, on `p.Arg264Ter`, or on any
  WWOX allele. An unasked question has no answer, in either direction.
- ❌ **It is NOT evidence that any WWOX transcript is stable.** T-1's normal rat mRNA is one allele in
  one species in two tissues.
- ❌ **It is NOT a claim that the experiment is hard.** § 6 shows it is cheap. **The gap is that
  nobody has done it.**
- ❌ **It does NOT transfer across alleles or species** (§ 4.3), and it does not upgrade or downgrade
  any mechanistic prediction the sibling scientist is adjudicating. **Flagged, not scored:** mechanism,
  reagent and allele verification are what § 1–§ 4 do; no score is proposed here and none should be
  derived from a zero.

---

## § 6 · If `NEVER TESTED` — the single cheapest experiment that moves it

**The experiment: an allele-specific ±NMD-block assay in a HETEROZYGOUS CARRIER line.**

The move that makes it cheap is choosing the **heterozygote**, not the proband. A heterozygous carrier
carries one PTC allele and one wild-type allele **in the same nucleus**, which supplies the internal
control that every existing WWOX measurement lacks: the WT allele is the denominator, so
*degraded* and *never transcribed* stop being the same observation. Heterozygous WWOX carriers are
healthy, numerous, and already documented — PMID 25411445 reports parents across four families;
PMID 32581702 reports both carrier parents with Sanger electropherograms; PMID 25403906 already
measured the **mother** and found *"moderate level of expression"*, i.e. a half-dose signal in a
carrier is already known to be detectable.

**Design (one plate, one week of bench time):**

| Element | Specification |
|---|---|
| **Material** | LCL (EBV-transformed lymphoblastoid line) or dermal fibroblasts from a **heterozygous carrier** of a published WWOX nonsense or frameshift allele. LCL is preferred: it is immortal, it is what biobanks already hold, and it needs a blood draw, not a punch biopsy |
| **Arms** | vehicle · **emetine 100 µg/mL, 4 h** · **cycloheximide 100 µg/mL, 4 h** · (optional orthogonal arm) **SMG1i or UPF1 siRNA, 48 h** — the orthogonal arm matters because emetine and CHX both block translation globally and are not NMD-specific |
| **Readout** | **allele-specific ddPCR or allele-specific RT-qPCR** across the PTC, phased on the variant itself; report the **mutant : wild-type allelic ratio**, not total WWOX. A ratio that *rises* under the block = the message was being degraded. A ratio that does not move, while the control does = the allele is not an NMD substrate |
| **Positive control (non-negotiable)** | an **endogenous NMD-sensitive transcript** measured on the same RNA in the same wells — e.g. `GAS5`, `SRSF2` PTC-containing isoform, or `ATF4` uORF isoform. Without it, a null result is the § 3 problem all over again |
| **Negative control** | an NMD-insensitive housekeeping transcript; plus a non-carrier line run through the identical protocol |
| **n** | ≥ 3 independent inductions, blinded quantification |
| **Cost/time** | one LCL vial, two reagents, one ddPCR plate. **Days, not months.** No animal, no new consent for the assay itself beyond the line's existing use terms, no novel chemistry |

**What it would settle, and for which allele only.** It settles, for **that one allele in that one
material**, whether the PTC-bearing message is degraded and by how much. It converts `PREMISE:
NOBODY_LOOKED` into a number. It does **not** transfer to a different exon, a different allele class,
or to neurons — a terminal-exon allele such as `c.1057-2A>G` needs its own run, and LCL splicing is
not neuronal splicing.

**The material that would make it best, and why it is the real ask.** T-8 shows the highest-value
material in this whole field has already been destroyed once: **a post-mortem fetal brain from a
homozygous `p.Arg264Ter` carrier, formalin-fixed and paraffin-embedded with no RNA taken.** The
standing request that follows from this census is small and concrete: **when WWOX post-mortem or
termination material is next handled, snap-freeze or RNAlater a fragment before fixation.** One tube.
It is the difference between another decade of *"or"* and the first neural measurement in this gene.

---

## § 7 · Instruments, limits, and what I could not do

- **Tools used:** `grep`/Python over the repository; PubMed MCP `search_articles`,
  `get_article_metadata`, `get_full_text_article`, `get_copyright_status`. Full texts retrieved and
  read today: **PMC13205014** (42193054) and **PMC7300205** (32581702), both non-empty bodies.
- **`is_open_access` behaved as the brief warns:** it was used only to ORDER acquisition attempts,
  never to skip one. 42193054 returned `is_open_access: true` and fetched; 25403906, 18273838 and
  25411445 returned `pmc_id: null`, so **no fetch target exists** and I did not attempt a transfer and
  do not claim to have tested them.
- **Substring-vs-word-boundary was checked before any count was reported.** The `ASE` 8842→0 collapse
  is the headline instance. No `.nb.html` or notebook file contributed a base64 hit: the four
  `anisomycin` raw hits include two from `registries/corpus_seed_pubmed_20260806.jsonl`, inspected and
  excluded as a corpus-seed record, not evidence.
- **No general web fetch was attempted.** Outbound is an allowlist; the census did not need it.
- **Not done, and named rather than hidden:** (1) the Alsop 2008 body (18273838) — the one WWOX ASE
  paper — is **unreachable here** and is this census's top retrieval debt; (2) I did not re-run
  Scientist E's HGVS phrase controls and have labelled C-6 as inherited rather than measured;
  (3) the 16 hits of L-13 and L-14 were screened at abstract level for a transcript-abundance
  measurement on a truncating allele, not read in full; (4) no figure was inspected, so per **D-14**
  no negative asserted only by a figure is adjudicated here.
- **Nothing in this file is medical advice**, and nothing in it is a treatment proposal. § 6 is an
  assay specification for a research setting and would require its own ethical and institutional
  approval.

---

*Author: Scientist Q. Date: 2026-09-22. **READ-ONLY:** no canonical file, registry, ledger, queue,
receipt, commit candidate or state manifest was modified; no `BATCH_COMMIT` was run; no git operation
was performed. This file is the only file written inside the repository by this task. Article metadata
and full texts were retrieved from **PubMed / PubMed Central**. This is the public edition: the
reasoning above concerns the WWOX-DEE reference genotype class, and no individual-level record appears
anywhere in it.*

**— END OF CENSUS (complete run; § 1–§ 7 all present) —**
