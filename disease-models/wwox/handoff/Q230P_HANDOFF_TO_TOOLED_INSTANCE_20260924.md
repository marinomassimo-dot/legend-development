# Q230P — HANDOFF BRIEFING for a tool-enabled instance
**From:** LEGEND Orchestrator (deployment with NO outbound egress to NCBI/Ensembl/UCSC/vendor sites)
**To:** an instance WITH sequence-database and web tools
**Repo checkpoint:** `1aeb6967482ce10fe1700f5c493db4a23a44bec6` (branch `main`)
**Date:** 2026-09-24

> 🔴 **Not medical advice.** This concerns a disease-level WWOX-DEE genotype class, not any individual.
> 🔴 **Public edition.** Do not introduce parent-of-origin, pedigree coordinates, or re-identifying
> variant+person combinations into anything you write back.

---

## 1 · OBJECTIVE

**`WWOX` `c.689A>C` / `p.(Gln230Pro)` ("Q230P") is a recurrent missense allele that behaves like a
null.** Patient fibroblasts show normal `WWOX` transcript and **no detectable WWOX protein**.

**The programme-level question:** *is there a WWOX protein population anywhere in a Q230P cell that a
proteostasis / pharmacological-chaperone strategy could rescue — or is there nothing to rescue?*

🔴 **This question is currently unanswerable, and the reason is not that the biology is hard. It is
that the two measurements which would settle it have never been made.** The purpose of this handoff
is to get one blocking fact checked so the first of those measurements becomes interpretable.

---

## 2 · WHAT WE KNOW, STEP BY STEP, WITH THE SOURCE FOR EACH

### 2.1 The allele and its clinical weight

| Fact | Source |
|---|---|
| `c.689A>C`, `p.(Gln230Pro)`, in the catalytic **SDR domain** | Johannsen 2018, PMID 29808465, DOI `10.1007/s10048-018-0549-5`, *Neurogenetics* 19(3):151–156 |
| **Most recurrent WWOX allele in the largest published compilation: 9 allele-observations**, ahead of `c.790C>T` p.Arg264Ter at 5 | Oliver 2023 **Supplementary Table S1**, PMID 36779245, DOI `10.1111/epi.17542`, *Epilepsia* 64(5):1351–1367 — read first-hand from the `.xlsx` |
| **Q230P = 9 of 28 missense allele-observations = 32.1 % of the whole "missense" class** in that compilation | same, computed from the sheet |
| Oliver's own abstract calls the comparator arm *"at least one **presumed hypomorphic** missense pathogenic variant"* — **`presumed` is the authors' word** | PMID 36779245 abstract |
| Unique-person count: **provisional 11 affected across 9 families; unresolved range 10–13** (+2 unaffected carriers ⇒ 13 carrying the allele) | reconciliation across Johannsen, Weisz-Hubshman, Piard 2019 (PMID 30356099), Oliver 2023 |
| The older repo figure *"8 patients / 6 families"* is **a Banne 2021 tally (PMID 33916893), arithmetically exact for its own cutoff** — superseded, not wrong | decomposes without residue: Johannsen 2/1 + Weisz-Hubshman 2/1 + Piard 4/4 |
| Clinical span is wide: one Q230P homozygote is the oldest in Oliver's cohort (**23 y 11 m, alive**); another **died at 8**; Q230P + deletion **alive at 4 y 7 m** | `CLAIM 019`, sourced to Oliver 2023 |

### 2.2 RNA — what was measured, and the window it was measured in

**Source: Johannsen 2018, read at full-body depth 2026-09-23 (`FTR-20260923-29808465-02`).**

Verbatim, Methods *"Quantification of WWOX transcription"*:

> *"Transcription of WWOX was ascertained for the core (**exons 4–6**) and the 3′ region (**exons 8–9**).
> This was done to ensure complete WWOX transcription as exon 9 is located about 730 kbp distant from
> exon 8. Two primer pairs were designed according to PrimerBank … spanning either **exon 4–6**
> (forward 5′-CCAACCACCCGGCAAAGATA-3′, reverse 5′-AATGCTGCACGCTACGGAG-3′) or **exon 8–9**
> (forward 5′-ATGTACTCCAACATTCATCGCAG-3′, reverse 5′-GTCTCTTCGCTCTGAGCTTCT-3′) of the major WWOX
> transcript (`NM_016373.2`)."*

- Amplicons confirmed on gel: **277 bp** (core) and **200 bp** (3′).
- Result: *"almost identical transcript level"* vs three reference cell lines, normalised to `HPRT1` + `UBC`; `−RT` controls clean.
- Cells: **dermal fibroblasts from one homozygous patient**, forearm punch biopsy, within five passages, **two independent harvests**.

> 🎯 **THE CRITICAL STRUCTURAL FACT.** `c.689A>C` lies in **exon 7**. The core amplicon ends at the end
> of exon 6; the 3′ amplicon begins at the start of exon 8. **Both amplicons bracket the exon carrying
> the variant and cover neither.** An exon-7 event would leave **both** gel bands at their expected
> size, so the paper's own *"normal … length"* control is blind to it **by construction**.

⇒ **`H1a` (abundance of the assayed regions) is REFUTED. `H1b` (exon-7 architecture) is UNTESTED and
was never asked.** Neither exon-7 skipping nor a normal exon-7 junction may be inferred.

### 2.3 Protein — what was measured, and what the method structurally could not see

**Same source. Five predictions were preregistered on 2026-09-22 *before* the paper was obtained, and
scored 5/5 SUPPORTED against their own falsifiers.**

Verbatim, Methods *"Biomaterial sampling"*:

> *"The other pellet was resuspended in 100 μl ice-cold **RIPA buffer** supplemented with protease
> inhibitors and sonicated three times on ice. Upon 10 min centrifugation with 13.000 rpm at 4 °C,
> **the supernatant containing cellular proteins was collected.**"*

| Prediction | Outcome |
|---|---|
| `P1` no pellet / insoluble fraction examined | 🟢 **SUPPORTED** — the sentence ends at the supernatant. **No pellet lane anywhere** |
| `P2` buffer named without composition, no denaturant | 🟢 **SUPPORTED** — `RIPA` named; no detergents, percentages, salt, pH or denaturant stated |
| `P3` no quantified detection floor | 🟢 **SUPPORTED** — `detection limit` 0, `limit of detection` 0 (earned zeros) |
| `P4` no synthesis-rate measurement | 🟢 **SUPPORTED** — `pulse` / `puromycin` / `polysome` / `cycloheximide` / `MG132` all 0 |
| `P5` antibody by vendor at most, epitope not stated | 🟢 **SUPPORTED on its falsifier** — a catalogue number *is* given; **no epitope is** |

Western: **`sc-20528` (Santa Cruz), 1:200**, 20–40 µg, 12 % SDS-PAGE, PVDF, ECL `Luminata Forte`,
`ImageQuant LAS 4000 Mini`, band at ~46 kDa. Controls: **positive** = PaTu-8988t, SW620, **HEK293**
(all endogenous WT WWOX); **negative** = three CRISPR/Cas9 `WWOX` knock-out PaTu-8988t clones
(`sc-403070`).

Result, verbatim: *"Western blotting, however, did not elicit any detectable WWOX protein in the
fibroblast line of the index patient"*, replicated on a second harvest days later.

Authors' interpretation, verbatim: *"These results may point towards an impaired protein translation
or, more likely, premature degradation of the misfolded protein after transcription due to quality
control mechanisms in the **endoplasmic reticulum (ER)**."*
🔴 **No ER experiment of any kind was performed.** No ER marker, no ERAD inhibitor, no glycosylation,
no fractionation. Do not inherit the ER attribution at any strength.

### 2.4 Two things this repository itself got wrong and corrected — carry the corrections

| Was asserted | Corrected to | Why it matters |
|---|---|---|
| MeSH `HEK293 Cells` implies a **heterologous Q230P expression arm** | 🔴 **REFUTED.** Fig. 3c legend: HEK293 is a **positive control for endogenous WWOX**. No transfection exists in this paper | An index term was read as an experiment |
| MeSH `RNA Stability` implies transcript stability was assessed | 🔴 **REFUTED.** `stabilit*` = 0 across the body | Same failure mode |

### 2.5 The detection reagent — and a documented discrepancy

🎯 **`sc-20528` is the SAME catalogue antibody used in the *lde*-rat study** (Suzuki 2009,
*Genes Brain Behav* 8(7):650–660, DOI `10.1111/j.1601-183X.2009.00502.x`), verbatim:
*"goat anti-Wwox polyclonal antibody (1:100; **sc-20528**, Santa Cruz Biotechnology)"*.

In that study Wwox products were reported **"undetectable"**. A later study of the same model using
**`HPA050992`** (immunogen **aa 32–110**) detected ***"a very weak band of slightly lower mobility."***

> 🔴 **State this precisely: `ASSAY-CONDITIONED DETECTION DISCREPANCY`, not a verdict on the antibody.**
> It is strong evidence that *"not detected"* is a property of the **whole detection architecture**, and
> **no evidence** that `sc-20528` is intrinsically poor in any other context. Both lysis buffers were
> real, recipe-stated RIPA, so **lysis class is not the difference**; antibody, sonication and
> ECL-vs-infrared detection all differ. The sensitivity attribution is the later authors' and **nobody
> has tested it.**

`sc-20528`'s only epitope information is a **negation**, sourced to a **2009 vendor personal
communication**: *"did not contain the region altered by the `lde` mutation"* — this excludes roughly
the last ~44 residues and **says nothing about residue 230**.

### 2.6 Reagent availability — measured, not assumed

Across the repository's WWOX antibody census (17 distinct anti-WWOX primaries):

| | |
|---|---|
| Orderable (catalogue number in hand) | **7** — `HPA050992`, `sc-20528`, `ab238144`, `ab189410`, `ABN413`, CST `4045S`, `ab216660` |
| Of those, with **any** epitope statement | **2** |
| With an epitope **placed relative to residue 230** | **1** — `HPA050992`, N-terminal (aa 32–110, ends 120 residues before Q230) |
| 🔴 Wholly **C-terminal to 230** | **0 / 17. Never moved.** |
| With a stated epitope but **NO catalogue number** (⇒ not orderable, ⇒ not reagents) | `A5` ProteinTech exons 1–7 · `A6` Abcam exons 1–5 |

⇒ **A flanking antibody pair is not purchasable today at any price.**
🟢 Useful accident: `HPA050992` is **rabbit**, `sc-20528` is **goat** ⇒ one membrane, two infrared
channels, no stripping — a pairing Suzuki 2009 already published.

---

## 3 · 🔴 THE CONDITIONAL DERIVATION — treat every number here as provisional

From `CC-20260922-EXON7-NATURAL-EXPERIMENT-01` §2, boundaries **read from ClinVar**:

```
exon 6  c.517–605      exon 7  c.606–791  (186 nt)      exon 8  c.792–1056      exon 9  c.1057–1245 (stop)
```

Derived arithmetic (codon `n = (c+2)//3`; base `= c − 3(n−1)`):

- `c.606` = codon **202**, base **3** · `c.791` = codon **264**, base **2** ⇒ neither boundary is a codon edge
- `186 mod 3 = 0` ⇒ **in-frame**
- Junction fuses `c.605` to `c.792` ⇒ **new chimeric codon 202 = `c.604` + `c.605` + `c.792`**
- Residues **203–263 deleted outright (61 aa)**; residues **202 and 264 fuse into one**; net **62 aa**
- `414 − 62 = 352 aa` product · **`Q230` is inside 203–263 ⇒ deleted outright**

> # 🔴 ALL OF THE ABOVE IS `CONDITIONAL DERIVATION`, NOT SETTLED FACT.
> **The exon-7 boundary came from ClinVar, whose HGVS is on `NM_016373.4`. Johannsen's primers and his
> 277 bp / 200 bp amplicons are on `NM_016373.2`. The arithmetic therefore mixes two transcript
> versions, and whether their CDS numbering is identical is `UNVERIFIED`.**
>
> If the versions differ only in UTR length, `c.` coordinates are unchanged and everything above stands.
> If the CDS changed, **every number moves together**, because they all derive from the same two
> boundary coordinates. **Do not quote 186 nt / 352 aa / "residues 203–263" as established.**

**Version census across this repository's own surfaces:** `NM_016373.4` ×37 (ClinVar) ·
`NM_016373.3` ×14 (e.g. Tabarki 2015 `c.606-1G>A`) · **`NM_016373.2` ×5 (Johannsen — the version `E1`
depends on)**.

🔴 **And one further bound, which matters more than the frame arithmetic:** *in-frame* means exon-7
skipping does **not** introduce a frameshift or PTC and therefore does **not** predict NMD by that
mechanism. **It does not predict that a protein is produced or that it survives.** An internal
deletion of ~62 residues from the SDR domain could compromise folding, translation, stability,
solubility or clearance. **Actual protein production and stability remain untested.**

---

## 4 · THE STATE OF THE MODEL

| Layer | State |
|---|---|
| RNA — abundance, exons 4–6 and 8–9 | 🟢 Substantially normal, one fibroblast line, one donor |
| RNA — architecture, exon 7 | 🔴 **UNKNOWN. Never interrogated by any published assay** |
| Protein — RIPA-soluble supernatant | 🟢 **Not detected**, replicated |
| Protein — pellet / insoluble | 🔴 **Not interrogated.** The pellet was discarded |
| Protein — total denatured pool | 🔴 **Not interrogated** |
| Protein — quantitative LOD | 🔴 **Absent** |
| Detection architecture | 🟡 Warrants caution (§2.5) |
| Mechanism — impaired synthesis · cotranslational disposal · rapid degradation · insoluble sequestration · detection artefact | 🔴 **All five open** |

**Nothing has been added to the theory. What changed is that the questions which could not have been
answered have been removed.**

---

## 5 · THE TWO EXPERIMENTS, IN ORDER

### `E1` — exon-7 RT-PCR · FIRST
🎯 **Neither Johannsen pair can see exon 7 — but the FORWARD of the exon 4–6 pair crossed with the
REVERSE of the exon 8–9 pair spans it entirely.** Zero new oligonucleotide design; both sequences are
published (§2.2). Expected shift on skipping: **exactly 186 bp** (conditional per §3). Estimated
absolute amplicon **729–1015 bp** — a range only because the primers' positions within their exons are
not published as coordinates. Sanger-sequenceable for the junction.

Preferred over Weisz-Hubshman's own published pair (`5′TGGTTGTGGTCACTGGAGCTA3′` /
`5′AGGATGCACTGCGTTCGAC3′`, PMID 30853297), whose reverse primer is provably 3′ of exon 6 — because the
same pair amplifies both the 593 bp WT and the 504 bp Δexon-6 products — but whose **exact exon is
`UNKNOWN`**. If it sits *in* exon 7, skipping gives a **dropout**, indistinguishable from PCR failure.
The cross-pair's reverse is in exon 9 by construction ⇒ always a **shift**, never an absence.

**Outcome branches, fixed in advance:**

| `E1` result | Consequence for `E2` |
|---|---|
| **WT size only** | 🟢 `E2` proceeds as designed. Q230P really is in the transcript |
| **Δ186 only** | 🔴 **`E2` must be REDESIGNED before it is run** — the ~46 kDa window and the antibody choice are both wrong for an uncharacterised shorter product. Confirm the junction by Sanger against **`NM_016373.2`**, never the current RefSeq |
| **Both bands** | 🟡 Quantify proportion and confirm identity of both first. **A long-amplicon size ratio is NOT an isoform ratio** |
| **No product** | 🔴 Assay failure or RNA quality. **Never a biological negative.** Re-run with an independent amplification control in the same tube |

⚠️ **Only the first branch leaves `E2` untouched — running `E2` first risks executing the wrong
experiment in three cases out of four.**

### `E2` — S/P/T + real LOD + orthogonal detection · SECOND
Classified **`MINOR ADAPTATION`** (nothing must be invented; the flanking pair must be dropped).

- **Fractions** from one lysate: `S` RIPA-soluble supernatant (reproduces Johannsen **by class, never
  by identity** — his RIPA composition is unrecoverable, `P2`), `P` pellet resolubilised in SDS/urea,
  `T` no-spin total. `S + P ≈ T` in the WT lane is the design's own validity control.
- 🔴 **NORMALISATION RULE: load by input-equivalents (equal cell-equivalents), NEVER by equal total
  protein per fraction.** The hypothesis is that Q230P has *moved* from `S` into `P`; normalising each
  lane to the same µg re-scales every fraction to a common denominator and **divides out exactly the
  redistribution being measured** — it can even invert its direction. Total-protein stain is a
  transfer control, never the normaliser.
- 🔴 **Urea at ≤ 50 °C.** The existing protocol file specifies 95 °C; 8 M urea above ~50 °C
  **carbamylates lysines** and shifts/smears the very band the experiment exists to detect.
- 🔴 **Null lane: a knockdown, not Johannsen's CRISPR-KO clones** (those are his freezer, not a
  catalogue) — and **a knockdown is reduced, not null**.
- **Antibodies: the smallest configuration that exists** — `HPA050992` (rabbit, aa 32–110) beside
  `sc-20528` (goat), one membrane, two IR channels. **This is NOT a flanking pair and must not be
  called one.** It does test the untested sensitivity attribution of §2.5 for free.
- **LOD:** ≥5-point dilution series on the same membrane; report *"below X, N = 3"*, in
  **cell-equivalents** unless a quantified recombinant WWOX standard is sourced (existence `UNKNOWN`).
- **Binding constraint: Q230P patient fibroblasts. `HUMAN_REQUIRED`, and it always was.**

🔴 **No `E2` branch converts to FUNCTION.** Abundance is not function. Branch (a) — pellet-positive,
soluble-negative — **raises rather than lowers the proteostasis safety bar**, and no branch transfers
to neurons.

---

## 6 · WHAT IS MISSING — THE CONCRETE ASKS FOR A TOOL-ENABLED INSTANCE

🔴 **This deployment measured its own blocks today, first-hand:** `eutils.ncbi.nlm.nih.gov`,
`rest.ensembl.org`, `scbt.com`, `ptglab.com`, `sigmaaldrich.com`, `ebi.ac.uk`, `ucsc` — **all return
`curl (56) CONNECT tunnel failed, response 403`.** Correct classification of everything below is
**`AUTONOMOUSLY_ACQUIRABLE`** (public reference data) and **`NETWORK_BLOCKED` here** —
**not `HUMAN_REQUIRED`.**

### 🥇 ASK 1 — THE BLOCKING ONE (minutes)
1. Retrieve **`NM_016373.2`** (the *historical* version Johannsen used) — **not** `.4`, and do not
   silently substitute it.
2. Report whether **CDS numbering is identical between `NM_016373.2` and `NM_016373.4`** (i.e. do the
   versions differ only in UTR, or did the CDS change?).
3. Confirm or correct the **exon 7 boundaries `c.606–791`** *on `.2`*, and its length.
4. Build the Δex7 transcript and annotate the chain: **junction nucleotide → junction codon → exact
   translated protein sequence → exact theoretical MW**.
5. Report the **amino-acid identity of the chimeric residue** at position 202.

⇒ This converts §3 from `CONDITIONAL DERIVATION` to fact (or refutes it), and supplies the MW that
`E1`'s Δ186 branch and `E2`'s gel window both need.

### 🥈 ASK 2 — makes `E1` fully lab-ready (minutes)
BLAT/BLAST Johannsen's four published primers against **`NM_016373.2`** and report exact positions, so
that:
- the **exact expected cross-pair amplicon size** replaces the 729–1015 bp estimate;
- the exact **Δex7 product size** is fixed;
- and, separately, place Weisz-Hubshman's reverse primer `5′AGGATGCACTGCGTTCGAC3′` — **exon 7 or
  exon 8?** (exon 8 ⇒ clean shift; exon 7 ⇒ ambiguous dropout).

Also: check annealing-temperature compatibility of the cross-pair (they come from two different
PrimerBank pairs and their Tm were never reported together).

### 🥉 ASK 3 — reagent reality (minutes)
Current 2026 catalogue status of **`sc-20528`** (Santa Cruz) and **`HPA050992`** (Sigma/Atlas):
still listed or discontinued? And the **stated immunogen/epitope** of `sc-20528` — the only thing on
record is a 2009 phone call. If `sc-20528` is discontinued, `E2` loses its second channel and its
commensurability with the founding negative.

### ASK 4 — optional, only if cheap
Does a **quantified recombinant human WWOX standard** exist commercially? Without one the LOD is in
cell-equivalents rather than ng.

---

## 7 · RULES FOR WHATEVER YOU WRITE BACK

1. 🔴 **Do not substitute `NM_016373.4` for `.2`.** Three versions are already in simultaneous use in
   this corpus; version drift is the specific hazard being guarded against.
2. 🔴 **Do not infer exon-7 skipping, and do not infer a normal exon-7 junction.** Both are `UNKNOWN`.
3. 🔴 **Do not convert in-frame into "stable protein expected".**
4. 🔴 **Do not call `sc-20528` an unreliable antibody.** The finding is assay-conditioned (§2.5).
5. 🔴 **Report an earned zero as a zero only after positive controls pass.** A query returning nothing
   from a blocked or misconfigured tool is an instrument reading, not a finding.
6. 🔴 **Public edition:** no parent-of-origin, no pedigree coordinates, no sex/anthropometrics, no
   re-identifying two-variant + person combinations.
7. 🟢 **State every UNKNOWN as UNKNOWN.** A precise gap is more useful here than a confident guess.

---

## 8 · STATUS LABEL OF RECORD

```
Q230P: TARGETED EXPERIMENTAL FRONTIER
  prerequisite (technical): retrieve/verify NM_016373.2 and its CDS compatibility with .4
    -> E1  exon-7 architecture
    -> if interpretable, E2  protein fate (S/P/T + input-equivalents + real LOD + orthogonal detection)
    -> only then  proteostasis / chaperone rescue
```

🔴 **The prerequisite does not block RUNNING `E1`. It blocks INTERPRETING a Δ186 junction.**
🔴 **Proteostasis / chaperone work does not resume until `E1` and `E2` report** — every such strategy
presupposes an entity to rescue, and that entity is currently unidentified in **two independent ways
at once**: the transcript may not contain the exon carrying the variant, and no protein population has
been shown to exist anywhere in the cell.

---

## 9 · PRIMARY SOURCES, WITH READ DEPTH

| PMID | Citation | DOI | Read depth in LEGEND |
|---|---|---|---|
| **29808465** | Johannsen J, Kortüm F, Rosenberger G, Bokelmann K, Schirmer MA, Denecke J, Santer R. *Neurogenetics* 2018;19(3):151–156 | `10.1007/s10048-018-0549-5` | `partial_fulltext_read` (figures captions_only) — `FTR-20260923-29808465-02` |
| **30853297** | Weisz-Hubshman M, … Heimer G. *Eur J Paediatr Neurol* 2019;23(3):418–426 | `10.1016/j.ejpn.2019.02.003` | `partial_fulltext_read`, figures read — `FTR-20260923-30853297-01`, corrected by `-02` |
| **36779245** | Oliver KL, Trivisano M, … Scheffer IE. *Epilepsia* 2023;64(5):1351–1367 | `10.1111/epi.17542` | body `complete_fulltext_read`; supplement `read` — `FTR-20260923-36779245-04` |
| **30356099** | Piard J, … Philippe C. *Genet Med* 2019;21(6):1308–1318 (online 2018-10-25) | `10.1038/s41436-018-0339-3` | partial — `FTR-20260811-30356099-01`; **Tables 1 + S1–S4 UNAVAILABLE** |
| **33916893** | Banne E, et al. *Cells* 2021 — review, source of the "8 patients / 6 families" tally | — | read |
| Suzuki 2009 | *Genes Brain Behav* 8(7):650–660 — the `lde` rat, `sc-20528` | `10.1111/j.1601-183X.2009.00502.x` | Methods read (passage retrieval) |

**Canonical claims touched by this node (none modified):** `CLAIM 019` (*consolidated baseline* —
Q230P pathogenic in severe context), `CLAIM 030` (*in observation* — severity tracks residual
**function**, not abundance; carries `PREMISE: DETECTION_FLOOR`).
