# NMD adjudication — reference-genotype acceptor allele `WWOX c.1057-2A>G`

**Actor:** Scientist P · **Date:** 2026-09-22 · **READ-ONLY.** No registry, ledger, queue or
canonical file was modified. No `BATCH_COMMIT` was run. This document **proposes**; the orchestrator
verifies and lands.

> **VERDICT — The NMD premise is not supported, and it never was.**
> Across **every** splice outcome that the reference sequence permits for this allele, the
> aberrant transcript is **not an EJC-dependent NMD substrate**. The surviving outcome
> (cryptic acceptor at `c.1063`) contains **no premature termination codon at all**, so the
> 50–55 nt rule has nothing to act on; and every other permitted outcome places its termination
> codon **downstream of the last remaining exon–exon junction**, which is the NMD-immune side.
> This is a statement about **the transcript**. It is **not** a statement about protein function,
> which remains `UNKNOWN AND STRUCTURALLY CONTESTED` (`D-30`).
> **And it is a PREDICTION.** Nobody has ever measured this allele's RNA, and **no WWOX allele of
> any class has ever been assayed with an NMD inhibitor.** The correct label for the empirical
> state is **`PREMISE: NOBODY_LOOKED`**, not "NMD does not occur."

**Nothing in this document is medical advice.** This is the public edition and reasons about a
WWOX-DEE reference genotype class, not about any individual.

---

## 1 · Where the NMD assertion originates

### 1.1 · It does not trace to nothing — it traces to a predictor run, and to the wrong branch of it

`therapeutic_hypotheses_ledger_current.md:216` (`HYP-20260709-02`, dated **2026-07-09**) states:

> *"L'allele di sito accettore del genotipo di riferimento (c.1057-2A>G) produce trascritto
> aberrante **destinato a NMD**: **up-regolarlo spinge solo più trascritto verso la degradazione**,
> senza proteina utile."*

🔴 **The clause carries no citation, no locator and no epistemic tag of its own.** The `Meccanismo`
and `Evidenza PRO` fields of that same hypothesis are sourced (miR-153, Kozak `rs11545028`, Sp1
`rs11644322`); the NMD clause, which is the load-bearing half of the asymmetry argument, is not.

The **only** upstream node in the repository that could support it is
`discovery_ledger_current.md:41–48`, **`DL-BIO-002`** (executed **2026-07-04**, five days earlier).
Its causal statement, verbatim:

> `c.1057-2A>G —disrupts→ exon9_acceptor`; (predetto) `→ exon9_skipping`;
> (predetto) `→ frameshift/PTC → **NMD or truncated_protein**`

and its own tag and belief, verbatim:

> **Tag**: `IPOTESI` … **Belief**: **ALTO sul disrupt dell'accettore** …; **medio sull'esito** …
> **Resta in-silico; DATO = RT-PCR wet**

**So the chain is:**

| step | what it says | strength |
|---|---|---|
| Ensembl VEP + SpliceAI + MaxEntScan, 2026-07-04 (raw output in the **private** `INBOX-005`, excluded from this edition) | acceptor loss `DS_AL 0.96`; cryptic acceptor gain `DS_AG 0.64` at `+8`; MaxEntScan Δ −7.95 | in-silico |
| `DL-BIO-002`, 2026-07-04 | *"NMD **or** truncated_protein"* — an **unresolved disjunction**, tagged `IPOTESI`, belief *medio* on the outcome | predicted, hedged |
| `therapeutic_hypotheses_ledger_current.md:216`, 2026-07-09 | *"**destinato a NMD**"* — **one branch of the disjunction, asserted categorically, with the hedge, the tag and the source dropped** | 🔴 **defect** |

🔴 **The defect is a disjunction collapsed into an assertion.** This is the same failure class the
repository has already named twice and refused twice: `Q230P`'s *"impaired translation **or**
premature degradation"* (baseline reversed 2026-07-14), and `PAPER 044`'s *"not expressed **or**
were degraded"* (`CC-20260922-SPLICE-ARM-01` §2). Here it was not caught.

### 1.2 · And the repository reversed the premise the very next day, without propagating it

`DL-MECH-045` was written on **2026-07-10** — **one day after** line 216 — and its entire point is
the opposite conclusion:

> *"la sorveglianza NMD degrada i trascritti con codone di stop prematuro **solo se il PTC si trova
> a monte dell'ultima giunzione esone-esone** (regola dei ~50-55 nt). Tutti gli esiti plausibili di
> questa variante … collocano il PTC **a valle dell'ultima giunzione**. → **NMD-escape**"*

**Line 216 was never updated.** The two contradicting loci named in the brief —
`paper_registry_current.md:6469` and `:6535` — are both **downstream restatements of `DL-MECH-045`**,
not independent sources; they are the reversal propagating into the paper registry while the
therapeutic ledger was left behind.

### 1.3 · What the assertion does **not** trace to

🔴 **It traces to no measurement of any kind.** Specifically:

- **No RNA from this allele has ever been examined** — patient, minigene, or otherwise. Confirmed
  independently below (§4.5) and consistent with `wwox_splice_transcript_census_20260921.md` §1d:
  *"Papers measuring a transcript from a canonical **ACCEPTOR** allele … **exactly one, PMID
  30853297**"* — and that one is the **other** acceptor, `c.517-2A>G`, a different exon and a
  different NMD regime.
- **No NMD assay has ever been run on any WWOX allele.** Re-measured this session (§4.5).
- **`DL-MECH-045`'s own predicted mechanism — `+8` → frameshift → truncated protein — is itself
  excluded** by the reference sequence (§3.3). Both the ledger clause and its reversal named the
  wrong molecular event; they simply disagreed about the label.

> ⚠️ **One honest qualification.** The raw `DP_AG` field the `+8` label was derived from lives in
> the **private-edition** `INBOX-005` quarantine log and is unreachable in this edition. §3 below
> therefore does **not** rely on it: the adjudication is re-derived from reference dinucleotides.

---

## 2 · Exon architecture, established from reference data

**Reference transcript:** `NM_016373.4` (WWOX). Assembly `NC_000016.10` (GRCh38), **plus strand**.
**Source used here:** `disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv` (1,327
ClinVar records, HGVS on `NM_016373.4`, SPDI on `NC_000016.10`), read directly this session.

> ⛔ **Direct sequence egress (Ensembl, NCBI/eutils, EBI) is blocked in this deployment** — recorded
> as blocked, not glossed. Everything below is derived from the local reference export and from
> PubMed-retrievable bodies, and is marked as derived where it is derived.

### 2.1 · Method and its own quality control

Every coding SNV was binned on its `genomic − cDNA` offset. If the transcript has *N* exons on a
single strand with no coordinate slippage, exactly *N* offset classes must appear and every ClinVar
cDNA reference base must equal its SPDI deleted allele.

```
exonic coding SNVs binned      : 729
reference-base concordance     : 729 / 729     (⇒ plus strand, no slippage)
distinct offset classes        : 9             (⇒ NINE exons)
```

### 2.2 · The exon table

Boundaries are **pinned exactly** where a canonical splice-site record (`c.N-1`, `c.N-2`, `c.N+1`,
`c.N+2`) exists in ClinVar. Observed pins: exon **starts** at `c.108, 173, 231, 410, 517, 606, 1057`;
exon **ends** at `c.107, 172, 409, 605, 791`. Together these close **all eight introns**.

| exon | cDNA (CDS coords) | coding nt | nt mod 3 | boundary status |
|---:|---|---:|---:|---|
| 1 | (5′UTR…) 1–107 | 107 | 2 | end pinned (`c.107+1/+2`) |
| 2 | 108–172 | 65 | 2 | both pinned |
| 3 | 173–230 | 58 | 1 | start pinned; end = `231−1` |
| 4 | 231–409 | 179 | 2 | both pinned |
| 5 | 410–516 | 107 | 2 | start pinned; end = `517−1` |
| 6 | 517–605 | 89 | 2 | both pinned |
| 7 | 606–791 | 186 | **0** | both pinned |
| 8 | 792–1056 | 265 | 1 | start = `791+1`; **end = `1057−1` = c.1056** |
| **9** | **1057–1245 + 3′UTR** | **189** | **0** | 🎯 **start pinned by `c.1057-1`/`c.1057-2` records — including the allele itself** |

**External check, and it is a published measurement, not an inference.** According to PubMed,
PMID **22071891** (White 2011, [DOI](https://doi.org/10.1038/ejhg.2011.204)) reports a germline
deletion of **exons 6–8** and states: *"cDNA analysis confirmed that the deletion **maintained the
reading frame**, with **exon 5 being spliced directly onto exon 9**."*
My table gives exons 6+7+8 = 89 + 186 + 265 = **540 nt**, and **540 mod 3 = 0**. ✅ An independent,
published cDNA measurement agrees with the arithmetic derived here.

### 2.3 · Which exon is last — established, not assumed

- **No coding SNV anywhere in ClinVar exceeds `c.1245`.**
- **All 29 3′UTR SNVs (`c.*1` … `c.*385`) fall in a SINGLE genomic offset class**, and that class is
  **contiguous with exon 9's coding class**: exon 9 coding maps `g = c + 79,210,551`, so
  `c.1245 → 79,211,796`; the 3′UTR class maps `g = n + 79,211,796`, so `c.*1 → 79,211,797`. The
  3′UTR continues exon 9 **with no gap**.
- **Zero ClinVar splice-site records of the form `c.*N±1/±2`** — i.e. **no intron is annotated
  anywhere in the 3′UTR** out to at least `c.*385`.

> 🎯 **Exon 9 is the last exon. There is no exon 10, and there is no intron in the 3′UTR out to
> `c.*385`.** ⚠️ `UNKNOWN`: the **total** 3′UTR length of `NM_016373.4` (only ≥385 nt is observed
> here), and therefore whether any intron exists beyond `c.*385`. Nothing in the reference data
> suggests one.

### 2.4 · The final exon–exon junction, and where `c.1057` sits relative to it

> ## 🎯 **Final EEJ = the `c.1056 | c.1057` boundary.**

Both flanking bases are directly observed: `c.1056` is the maximum of exon 8's offset class,
`c.1057` the minimum of exon 9's, and they are **adjacent in cDNA with no gap**; independently,
`c.1057` is pinned as an exon start by the `c.1057-1`…`c.1057-292` intronic record series,
which includes the allele under adjudication.

- **`c.1057` is the FIRST nucleotide 3′ of the final exon–exon junction — distance 0 nt.**
- **`c.1057-2` (the variant) is 2 nt inside intron 8**; it does not exist in any spliced mRNA.
- **Intron 8 length = 79,211,608 − 78,432,752 − 1 = 778,855 nt (~779 kb).**
  (The repository elsewhere carries 778,856; the difference is an endpoint convention, not a datum.)

### 2.5 · The normal termination codon — needed for the 50–55 nt arithmetic

Reconstructed from the ClinVar multi-base deleted allele of `c.1240_*36del` (SPDI
`NC_000016.10:79211788:CCGGCTAAGTGGAGCTCAGAGCGGATGGGCACACACACCCGCCC:CC`), which places
`c.1238` at 79,211,789:

```
c.1238 1239 1240 1241 1242 | 1243 1244 1245 | *1 *2 ...
   C    C    G    G    C   |   T    A    A   |  G  T
                  Gly414   |   TAA  = STOP  |   3'UTR
```

Cross-checked three ways: ClinVar `c.1240G>A → p.Gly414Ser`, `c.1242C>T → p.Gly414=`,
`c.1244A>C → p.Ter415Ser`, `c.1245A>C → p.Ter415Tyr`; and the local
`WWOX_Q9NZC7_AlphaFold.pdb` terminates at **GLY 414**.

> **Normal stop codon: `TAA` at `c.1243–1245`. Protein length 414 aa. CDS length 1,245 nt.**
> The normal stop lies **1243 − 1057 = 186 nt DOWNSTREAM** of the final EEJ — i.e. the **wild-type**
> WWOX transcript is itself comfortably NMD-immune, which is the sanity check this arithmetic needs.

### 2.6 · The exon-9 5′ sequence, reconstructed base by base

Derived from ClinVar deleted alleles **and**, independently, from ClinVar's **protein-consequence
column**, which is blind to any splicing prediction:

| record | cDNA | protein | what it forces |
|---|---|---|---|
| `VCV001381570` | `c.1057C>T` | **`p.Gln353Ter`** | codon 353 begins at `c.1057` = `C`; `C→T` gives a stop ⇒ codon 353 ∈ {CAA, CAG} |
| `VCV002022047` | `c.1059A>C` | **`p.Gln353His`** | third base `A→C` gives His ⇒ codon 353 = **`CAA`** ⇒ `c.1058 = A`, `c.1059 = A` |
| `VCV002438615` | `c.1060C>T` | **`p.Gln354Ter`** | codon 354 = `C,?,?`; `C→T` gives stop ⇒ **`CAG`** ⇒ `c.1061 = A`, `c.1062 = G` |
| `VCV003756655` | `c.1062G>A` | **`p.Gln354=`** | mutant `C,?,A` still Gln ⇒ `CAA` ⇒ **`c.1061 = A`** — *different submitter, opposite direction, same answer* |
| `VCV001016765` / `VCV001334431` | `c.1063G>A` / `c.1063G>C` | **both `p.Gly355Arg`** | Gly = `GGN`; `G→A` at base 1 gives Arg only as `AGA`/`AGG` ⇒ **`c.1064 = G`**; `G→C` gives `CGN` = Arg ✓ ⇒ **`c.1063 = G`** |
| `VCV000391689` / `VCV002103855` | `c.1066G>A` / `c.1067C>T` | `p.Ala356Thr` / `p.Ala356Val` | ⇒ `c.1066 = G`, `c.1067 = C` |

```
intron 8 3' end                     |  exon 9 ->
c.  ... -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 | 1057 1058 1059 1060 1061 1062 1063 1064 ...
      G   G   A   T   T   ?   C   C   A   G(*)|   C    A    A    C    A    G    G    G
                                  variant ^          Q353 ------   Q354 ------   G355 --
(*) c.1057-1 is not covered by any ClinVar record; it is G by necessity — a functioning
    canonical acceptor requires AG, and this one functions in wild type.
```

🔵 **Independent confirmation of the reading frame:** residues 353–358 derived above are
**Q, Q, G, A, A, T** — and `WWOX_Q9NZC7_AlphaFold.pdb` reads **GLN 353, GLN 354, GLY 355, ALA 356,
ALA 357, THR 358**. Two channels that share no upstream step agree residue by residue, which also
confirms that `c.1057` is the first base of codon 353 (`(1057 − 1) / 3 = 352` exactly).

### 2.7 · Marked `UNKNOWN` — not filled in

| item | status |
|---|---|
| **Transcript (r.) coordinates of the final EEJ** | 🔴 **UNKNOWN.** Requires the 5′UTR length of `NM_016373.4`; only **≥460 nt** is observed here (5′UTR SNVs reach `c.-460`, contiguous with exon 1). The EEJ is at transcript position `L + 1056 / L + 1057` with `L` unestablished. **Its position relative to the CDS is exact; its absolute transcript coordinate is not.** |
| `c.1057-1` and `c.1057-5` | not covered by any record; `c.1057-1 = G` by functional necessity only |
| `c.1065`, `c.1068`, `c.1071` | not established (third bases of degenerate codons) |
| Total 3′UTR length; any intron beyond `c.*385` | UNKNOWN (§2.3) |
| Whether `NM_016373.3` (used by older papers, e.g. Davids 2019) has the same exon structure as `.4` | 🔴 **UNKNOWN — not checked, and not assumed.** Every coordinate here is on `.4`. |
| Internal sequence of intron 8 (the first ~778,820 nt) | UNKNOWN — only the last ~31 nt are reconstructed |

---

## 3 · Per-event adjudication — each outcome separately

### 3.0 · The rule being applied, stated once

A termination codon triggers **EJC-dependent NMD** when it lies **≥ 50–55 nt upstream of the last
exon–exon junction** of that transcript. A stop located in the last exon, or within ~50–55 nt of the
final junction, or with **no** junction downstream of it, is **NMD-immune**.

**Threshold in this gene, for the normal junction structure:** the final EEJ is at `c.1056 | c.1057`.
A PTC is NMD-triggering only if it **ends at or before**

```
c.1056 − 50 = c.1006      (50-nt version)
c.1056 − 55 = c.1001      (55-nt version)
```

Any termination codon ending at **`c.1007` or later** is NMD-immune under the 50-nt reading, and at
**`c.1002` or later** under the 55-nt reading. **`c.1057` is 51 nt past even the looser threshold** —
and every outcome of this allele terminates at or beyond it.

### 3.1 · The adjudication table

| # | event | can it occur? | PTC created? | PTC position | last EEJ in that transcript | 50–55 nt arithmetic | **NMD substrate?** |
|---|---|---|---|---|---|---|---|
| **a** | **Exon 9 skipping** | 🔴 **NO — not a definable outcome.** Exon 9 is terminal (§2.3); exon 8's donor has no downstream acceptor to ligate to. No exon 10; no intron in the 3′UTR to `c.*385` | **N/A** | N/A | N/A | **rule not reached** | ⛔ **N/A — event excluded by architecture.** Not "no"; *undefined* |
| **b** | **Intron 8 retention / read-through** | mechanically possible; ~779 kb | **yes, somewhere in intron 8** | 🔴 **UNKNOWN position** — intron 8's internal sequence is not established here. Bounded: **at or after `c.1057`-equivalent**, i.e. ≥ 1 nt past `c.1056` | **`c.791 \| c.792`** (exon 7/8) — the intron 8/exon 9 junction is *not spliced*, so it is not an EEJ | PTC lies **≥ 1056 − 791 = 265 nt DOWNSTREAM** of the last EEJ. **There is no junction downstream of the PTC at all.** Rule requires ≥50–55 nt *upstream* | 🟢 **NO** (for EJC-dependent NMD) — see caveats 3.2 |
| **c** | **Cryptic acceptor at `c.1063`** (the `+8` site; **the only reading the reference sequence permits** — §3.3) | predicted, `DS_AG 0.64` | 🎯 **NO PTC AT ALL** | none — the **normal** `TAA` at `c.1243–1245` is retained and is not premature | **`c.1056 \| c.1063`** | **Rule is inapplicable: there is no premature stop.** For completeness, the normal stop sits `1243 − 1063 =` **180 nt DOWNSTREAM** of the new junction | 🟢 **NO — and the question does not arise** |
| **d1** | **Upstream cryptic acceptor inside intron 8** | ⛔ **excluded within the last 31 nt** — the reconstructed intron-8 3′ end contains **exactly two adenines** (`−8`, followed by `T`; and `−2`, the canonical one). **No `AG` other than the canonical.** UNKNOWN beyond −31 | if it occurred: possible, frame-dependent | would lie downstream of the new junction | **`c.1056 \| (c.1057−k)`** | any PTC in the added intronic sequence is **downstream** of that junction | 🟢 **NO**, in every variant of this event |
| **d2** | **Intronic polyadenylation / alternative terminal exon in intron 8** — *documented in this gene* (Schirmer 2016, *"transcripts terminating within intron 8"*, per `paper_registry_current.md` `PAPER 050`; **body not read by me**) | plausible | yes, in intron-8 sequence | UNKNOWN | **`c.791 \| c.792`** | termination is downstream of the last EEJ | 🟡 **NO for EJC-dependent NMD; `UNKNOWN` for long-3′UTR NMD** — see 3.2 |
| **e** | **Exon skipping of an *internal* exon** — the outcome actually MEASURED for the other WWOX acceptor allele | **N/A here** — that is a CONTRAST case, not this allele | — | — | — | — | ⛔ **does not transfer** (§4.4) |

### 3.2 · Two caveats that must travel with row (b) and row (d2)

1. 🔴 **"Not an NMD substrate" ≠ "stable and abundant."** A **778,855-nt** retained intron is very
   unlikely to be exported as a mature mRNA; such species are typically nuclear-retained and cleared
   by the **nuclear exosome**, which is **not NMD** and is **not blocked by cycloheximide**. A
   cycloheximide-insensitive loss of transcript is therefore an *expected* result for row (b) and
   **must not be scored as evidence of NMD**.
2. 🟡 **Long-3′UTR NMD is the one branch the 50–55 nt rule cannot decide.** A transcript that
   terminates within intron 8 and polyadenylates far downstream carries an abnormally long 3′UTR,
   and EJC-independent, UPF1-density-dependent decay is a real if variable phenomenon.
   **Status: `UNKNOWN`, not `NO`.** It is the only route by which this allele could still be
   degraded by an NMD-family pathway.

### 3.3 · Why row (c) is the only surviving acceptor-shift, re-derived from sequence

A gained acceptor requires an **`AG`** immediately 5′ of the new first exonic base. Applying the
spliceosome's first-`AG`-downstream scanning rule to the sequence reconstructed in §2.6 — with the
canonical `AG` at `c.1057-2/-1` destroyed by the `A>G` substitution (`AG → GG`):

| new exon starts at | nt lost | frame | required `AG` at | reference bases | verdict |
|---|---:|---|---|---|---|
| `c.1059` | 2 | frameshift | `c.1057`,`c.1058` | **`C`**, `A` | ⛔ first base is `C` |
| `c.1060` | 3 | in-frame | `c.1058`,`c.1059` | `A`, **`A`** | ⛔ second base is `A`, not `G` |
| `c.1061` | 4 | frameshift | `c.1059`,`c.1060` | `A`, **`C`** | ⛔ second base is `C` |
| `c.1062` | 5 | frameshift | `c.1060`,`c.1061` | **`C`**, `A` | ⛔ first base is `C` |
| **`c.1063`** | **6** | **in-frame** | `c.1061`,`c.1062` | **`A`**, **`G`** ✅ | 🟢 **survives — and it is the FIRST `AG` reached by downstream scanning** |
| `c.1064` | 7 | frameshift | `c.1062`,`c.1063` | **`G`**, `G` | ⛔ first base is `G` |
| `c.1065` | 8 | frameshift | `c.1063`,`c.1064` | **`G`**, **`G`** | ⛔ **both** bases wrong |

> 🎯 **`c.1063` is the first and only `AG` in the window. Loss = `c.1057`–`c.1062` = 6 nt = codons
> 353 and 354 exactly ⇒ `p.Gln353_Gln354del`, in-frame, 414 → 412 aa. No frameshift. No PTC.**
>
> 🔴 **The 8-nt frameshift reading — `DL-MECH-045`'s own predicted mechanism — is now dead at BOTH
> required bases** (`c.1063 = G` **and** `c.1064 = G`, the latter newly established here from the
> paired `c.1063G>A`/`c.1063G>C` → `p.Gly355Arg` records). It is excluded by reference sequence,
> not by a convention argument, and **not conditionally** on any unestablished base.

⚠️ **`c.1061 = A` is derived, not read** — from two independent ClinVar protein-consequence records
by different submitters, in opposite directions, each leaving exactly one possible base. Direct
sequence egress was blocked throughout.

### 3.4 · The architecture-level result — why every row lands the same way

> 🔴 **Because the lesion destroys the acceptor of the *terminal* exon, every transcript this allele
> can produce places its termination codon DOWNSTREAM of that transcript's own last exon–exon
> junction.** Shifting the acceptor moves the final junction with it (row c, d1); losing the
> junction entirely promotes the exon 7/8 junction to last (rows b, d2). In **neither** case can a
> stop codon end up ≥50–55 nt *upstream* of a *downstream* EJC.
>
> **The only configuration that could produce an EJC-dependent NMD substrate** would be the creation
> of a **new downstream exon–exon junction** — i.e. a cryptic *donor* in exon 9 or the 3′UTR splicing
> to a further downstream acceptor. §2.3 finds **no annotated intron in the 3′UTR out to `c.*385`**
> and nothing in the reference data predicts one. **Status: no such configuration found;
> `UNKNOWN` beyond `c.*385`.**

Note that this holds **independently of the frame call**: even under the now-excluded 8-nt
frameshift reading, the PTC would sit downstream of the final EEJ. **`DL-MECH-045` reached the right
NMD verdict from the wrong molecular event.** The frame call changes the *protein*, not the *NMD*
answer.

### 3.5 · What §3 does **NOT** license

- ❌ **It is not a measurement.** `DS_AG 0.64` is a **moderate** score, and a predicted acceptor gain
  is not a used site. The confident half is the acceptor **loss** (`DS_AL 0.96`, MaxEntScan Δ −7.95,
  two orthogonal methods); *what happens instead* is the uncertain half.
- ❌ **It is not a claim about protein function.** `D-30`: **in-frame is a statement about the
  reading frame, not about the fold.** `p.Gln353_Gln354del` sits **inside an α-helix (351–363)**
  whose next turn is buried core; the repository's own adversarial review
  (`CC-20260922-SPLICE-ARM-01` §9c) leaves it **CONTESTED**, with AlphaFold pLDDT 60.5–76.4 exactly
  where the answer lives. The exon-7 case in the same session is the cautionary precedent: in-frame,
  and lethal. **The correct label is `PREDICTED at transcript level — PROTEIN CONSEQUENCE UNKNOWN
  AND STRUCTURALLY CONTESTED`.**
- ❌ **It does not license "NMD does not occur."** No one has looked. See §6.

---

## 4 · Literature classification — MEASURED / INFERRED / INTERPRETATION / ABSENT

All searches run this session. **Every `query_translation` was read before any count was believed**
(`D-28`), and a **positive control** was carried: `WWOX AND "606-1G"` → `total_count 1`
(PMID 26345274), translation expanded with the gene symbol resolved. According to PubMed.

### 4.1 · The classification table

| # | verbatim quote | locator | source / where in the paper | allele | **classification** |
|---|---|---|---|---|---|
| **L1** | *"mRNA expression analysis revealed that the deletion led to **nonsense-mediated decay** of the NM_016373.3 transcript; the exon 6 of an alternative transcript (NM_130791.3), lacking the short-chain dehydrogenase, was utilized."* | PMID **30362252**, Davids 2019, **abstract** ([DOI](https://doi.org/10.1002/humu.23675)) | **abstract only** — verified by me: the words *nonsense-mediated* appear **nowhere in the retrieved body** | exon-6 microdeletion — **CONTRAST** | 🔴 **AUTHOR INTERPRETATION.** Methods are qPCR junction assays + western + ddPCR. **No NMD inhibitor anywhere in the paper.** A junction ratio does not demonstrate NMD without a translation block |
| **L2** | *"The exon 1–2 junction, however, was detected and was only slightly reduced in our patient, whereas the exon 7–8 junction was barely detectable, **suggesting that the two longer transcripts were not expressed or were degraded**."* | PMID **30362252**, **body** (retrieved in full this session, PMC6296882) | body — the sentence L1 is the abstract's paraphrase of | exon-6 deletion — **CONTRAST** | 🔴 **AUTHOR INTERPRETATION**, and an **explicitly unresolved disjunction**. This, not L1, is what the paper actually reports |
| **L3** | *"Minigene product sequencing demonstrated that the wild-type minigene formed normal mRNA … but the c.172+1G>C substitution … abrogated the intron 2 canonical splice site and **led to a loss of exon 2**."* | PMID **39101447**, You 2024, body + Fig. 8 legend ([DOI](https://doi.org/10.1002/mgg3.2500)) | heterologous minigene, HEK293T, shortened intron 1 | `c.172+1G>C` — **donor**, exon 2 — **CONTRAST** | **NOT PRESENT** for NMD. `cycloheximide`, `emetine`, `SMG1`, `puromycin`, `actinomycin`, `nonsense-mediated`, `NMD` = **0 occurrences**. The paper's *"protein truncation"* is a **SnapGene in-silico translation**, not an assay |
| **L4** | *"Complementary DNA sequencing demonstrated that the WWOX c.517-2A>G splice-site variant **causes skipping of exon six**."* | PMID **30853297**, Weisz-Hubshman 2019, abstract ([DOI](https://doi.org/10.1016/j.ejpn.2019.02.003)) | patient cDNA sequencing | `c.517-2A>G` — **the other canonical acceptor**, exon 6 — **CONTRAST** | **NOT PRESENT** for NMD in the abstract. ⛔ **Body unreachable — no PMCID. `PREMISE: UNREAD_PRIMARY` for its Methods/Results.** The *splicing outcome* is `DIRECTLY MEASURED`; the *NMD question* is not addressed |
| **L5** | *"The WWOX mRNA sequencing using **peripheral blood RNA** confirmed that **exon 5 was homozygously deleted**."* | PMID **38407561**, Nishino 2024, abstract ([DOI](https://doi.org/10.1002/ajmg.a.63575)) | patient blood mRNA sequencing | `c.516+1G>A` — **donor**, exon 5 — **CONTRAST** | **NOT PRESENT** for NMD. ⛔ Body unreachable — no PMCID. `PREMISE: UNREAD_PRIMARY` |
| **L6** | *"cDNA analysis confirmed that the deletion **maintained the reading frame**, with exon 5 being spliced directly onto exon 9."* | PMID **22071891**, White 2011, abstract ([DOI](https://doi.org/10.1038/ejhg.2011.204)) | patient cDNA | exons 6–8 deletion, heterozygous — **CONTRAST** | **NOT PRESENT** for NMD — correctly, since the product is in-frame. Positively reports a **detected** in-frame aberrant junction |
| **L7** | UPF1 appears only as a node: *"the core network containing **UPF1**, ZC3H12A, LINC01137, WWOX, and miR-186-5p"* | PMID **37519886**, Kołat 2023, abstract ([DOI](https://doi.org/10.3389/fgene.2023.1214968)) | bladder-cancer RNA interactome | none (no patient allele) | **NOT PRESENT.** This is the **only** WWOX paper in PubMed containing any NMD-machinery term, and it is a co-expression network node, not an NMD assay |
| **L8** | *"W44X non è mai stata validata funzionalmente (**NMD solo predetta**)."* | `paper_registry_current.md:6513` (repository annotation of PMID 27495153) | repository, not the paper | `p.Trp44Ter`, exon 2 — **CONTRAST** | **INFERRED** — and correctly self-labelled. The repository already knows this defect class by name |
| **L9** | *"l'esone 9 è l'**ultimo**, e un PTC nell'ultimo esone **sfugge all'NMD**"* | `paper_registry_current.md:6469` and `:6535` | repository, restating `DL-MECH-045` | `c.1057-2A>G` | **INFERRED** — the 50–55 nt rule applied to verified premises. §3 **confirms the verdict and corrects the mechanism** |
| **L10** | *"produce trascritto aberrante **destinato a NMD**"* | `therapeutic_hypotheses_ledger_current.md:216` | repository | `c.1057-2A>G` | 🔴 **AUTHOR INTERPRETATION** — no rule shown, no assay, no citation, and it selects one branch of `DL-BIO-002`'s explicit disjunction (§1.1) |

### 4.2 · 🔴 The `DIRECTLY MEASURED` row is empty

> **No paper anywhere in PubMed reports an NMD assay — cycloheximide, emetine, puromycin, SMG1
> inhibitor or UPF1 knockdown — on any WWOX allele of any class.** Not on this allele; not on any
> other acceptor allele; not on a nonsense allele; not on a deletion.

### 4.3 · The searches behind that statement, with translations

| query | `total_count` | `query_translation` — gene symbol resolved? | reading |
|---|---:|---|---|
| `WWOX AND "606-1G"` *(positive control)* | **1** (PMID 26345274) | ✅ `("wwox protein human"[Supplementary Concept] OR … OR "wwox"[All Fields]) AND "606-1G"[All Fields]` | the instrument works |
| `WWOX AND "nonsense-mediated"` | **1** (PMID 30362252) | ✅ expanded | a **sound** count |
| `WWOX AND "nonsense mediated decay"` | **1** (PMID 30362252) | ✅ expanded | same single record |
| `WWOX AND (cycloheximide OR emetine OR puromycin OR UPF1 OR SMG1)` | **1** (PMID 37519886) | ✅ expanded, all five drug/gene terms MeSH-mapped | **the one hit is a bladder-cancer network node (L7)** ⇒ effectively **zero** |
| `WWOX AND ("last exon" OR "escape" OR "premature termination codon" OR "truncated transcript")` | **6** | ✅ expanded | all six are *immune escape*, *senescence escape*, *tumor escape*. **Zero WWOX papers discuss last-exon NMD escape** |
| `WWOX AND "1057-2"` | **0** | ✅ expanded — **`"1057-2"[All Fields]`**, gene symbol resolved | 🟢 **a SOUND zero**, same query shape as the positive control ⇒ **no paper indexes this allele** |

⚠️ **Two known blind spots that these counts cannot see past**, both already proven in this
repository: PubMed `[All Fields]` **does not index Methods, supplements or data-availability
sections**; and a bare number becomes `NNNN[UID]`. So *"no paper mentions NMD in its abstract or
title"* is what is established. A cycloheximide arm buried in an unindexed Methods section of an
unreachable body is **not excluded** — it is `UNREAD_PRIMARY` (L4, L5).

### 4.4 · 🔴 The contrast cases — what they say, and what they must not be made to say

| paper | allele | exon position | measured outcome | frame | NMD regime |
|---|---|---|---|---|---|
| PMID 30362252 | exon-6 deletion | **internal** | junction loss | frameshifting | **NMD plausible** — the lesion is far upstream of the final EEJ. *Asserted in the abstract, never assayed* |
| PMID 30853297 | `c.517-2A>G` **acceptor** | **internal** (exon 6) | **exon 6 skipping** | 89 nt, mod 3 = 2 ⇒ **frameshift** | NMD **predicted** for that allele — *opposite* regime |
| PMID 38407561 | `c.516+1G>A` donor | **internal** (exon 5) | **exon 5 skipping**, in patient blood RNA | 107 nt, mod 3 = 2 ⇒ frameshift | NMD predicted — yet **the transcript was detectable** by mRNA-seq. A datum, not a quantification |
| PMID 39101447 | `c.172+1G>C` donor | **internal** (exon 2) | **exon 2 skipping** (minigene) | 65 nt, mod 3 = 2 ⇒ frameshift | NMD never addressed; the minigene has **no downstream junction and is blind to NMD by construction** |
| PMID 22071891 | exons 6–8 deletion | internal | **exon 5→exon 9** junction detected | 540 nt, **in-frame** | no PTC ⇒ NMD not applicable; transcript **present** |
| 🔴 **`c.1057-2A>G`** | **acceptor** | 🔴 **TERMINAL (exon 9 of 9)** | 🔴 **never measured** | — | 🔴 **opposite regime from all of the above** |

> ⛔ **None of these transfers.** An NMD statement about an exon-6 deletion says **nothing** about an
> exon-9 acceptor allele. The two published acceptor/donor measurements both produced **exon
> skipping** — which is precisely the outcome that **cannot occur** here, because exon 9 is terminal
> (§3.1 row a). **The field's empirical prior for WWOX splice alleles is architecturally
> inapplicable to the one allele that matters most.**

### 4.5 · Withdrawn: the field's only citable instance of measured WWOX NMD

L1 vs L2, verified by me in the retrieved body of PMC6296882: the abstract says *"nonsense-mediated
decay"*; the body says *"not expressed **or** were degraded"*; **no NMD inhibitor was used anywhere
in the paper**. With L1 withdrawn to `AUTHOR INTERPRETATION`, **the count of `DIRECTLY MEASURED` NMD
in WWOX, across all alleles and all of PubMed, is zero.** This confirms
`CC-20260922-SPLICE-ARM-01` §2 by an independent retrieval.

---

## 5 · The therapeutic consequence — does the line-216 asymmetry argument survive?

### 5.1 · What the argument is

`HYP-20260709-02` concludes that non-allele-specific WWOX upregulation is of uncertain sign, on a
two-step asymmetry:

> **Premise A** — the acceptor allele's transcript is *destinato a NMD*, so boosting transcription
> *"spinge solo più trascritto verso la degradazione, senza proteina utile."*
> **Premise B** — therefore a non-allele-specific boost amplifies **predominantly `Q230P`**, and the
> sign of any benefit depends **entirely** on `Q230P`'s folding fate.

### 5.2 · Verdict

> ## 🔴 **Premise A does not survive. The asymmetry argument, as written, collapses.**

Under **every** outcome the reference sequence permits, the acceptor allele's transcript is **not an
EJC-dependent NMD substrate** (§3). Under the **only surviving cryptic-acceptor reading** it carries
**no premature termination codon at all** and retains the normal `TAA` at `c.1243–1245`. Transcript
produced from that allele is therefore **not predicted to be routed to NMD**, and a
non-allele-specific boost would be expected to raise its abundance roughly in proportion — not to
feed a degradation pathway.

**The consequence for the therapeutic axis is that it reopens.** The reasoning that *"a boost only
amplifies the Q230P allele"* rested on the assumption that the other allele's output disappears.
That assumption is not supported.

### 5.3 · 🔴 But state it as the conditional it is — the evidence is conditional

> **IF** the cryptic acceptor at `c.1063` is the event that actually occurs *in vivo*
> (`PREDICTED`, `DS_AG 0.64` = moderate; **never measured in any system**),
> **THEN** the acceptor allele yields an mRNA that is **not an NMD substrate** and encodes a
> **near-full-length 412-aa protein** (`p.Gln353_Gln354del`);
> **AND THEREFORE** Premise A is false and a non-allele-specific boost raises output from **both**
> alleles, not predominantly one.
>
> **BUT** whether that 412-aa protein **folds, localises or functions** is **`UNKNOWN` and
> structurally contested** (`D-30`; §3.5). **A boost of a non-functional protein is not a benefit** —
> it is the *same* proteotoxic question `HYP-20260709-02` already raises for `Q230P`, now applying to
> **both** alleles instead of one.
>
> **AND** if the outcome is instead intron-8 retention or intronic polyadenylation (§3.1 rows b, d2),
> the transcript is still **not** an NMD substrate, but is likely nuclear-retained and cleared by the
> **exosome** — a *different* degradation route that Premise A's wording would accidentally
> describe correctly **for the wrong reason**, and which a cycloheximide arm would **fail to detect**.

### 5.4 · What changes and what does not

| item | status |
|---|---|
| **Premise A** (*"destinato a NMD"*, line 216) | 🔴 **NOT SUPPORTED — proposed for withdrawal.** Replace with: *transcript fate `UNKNOWN`/unmeasured; NMD not predicted under any permitted outcome; degradation, if any, is predicted to be non-NMD* |
| **Premise B** (*boost amplifies predominantly `Q230P`*) | 🔴 **falls with Premise A** as stated. The `Q230P` folding question survives **on its own merits** and is untouched |
| **The safety flag (🟡 giallo, proteotoxic risk)** | ✅ **UNCHANGED — and now applies to BOTH alleles.** More synthesis of a possibly-misfolded protein is the risk, whichever allele produces it |
| **`HYP-20260709-02` status** | 🔴 **Proposed:** remains `stress-tested`; **its stated reason for being conditional is wrong and must be rewritten**, not its conditionality. **FLAG FIRST.** Any re-score waits for mechanism + reagent + allele verification, i.e. for `TX-001` |
| **`DL-MECH-045`** | verdict (NMD-escape) ✅ **upheld and strengthened**; predicted mechanism (`+8` frameshift → truncated unstable protein) 🔴 **excluded by reference sequence at both required bases** |
| **`DL-BIO-002`** | causal statement `→ frameshift/PTC → NMD or truncated_protein` 🔴 **both branches now excluded** for the surviving outcome. Proposed replacement: `→ cryptic acceptor c.1063 → in-frame p.Gln353_Gln354del → no PTC → no NMD` (PREDICTED) |
| **`TX-001` headroom** | 🔵 **rises.** If the allele already makes a near-full-length protein, splice correction recovers 2 residues, not a whole protein — **which lowers TX-001's ceiling while raising the value of measuring it**. This is a real tension and it is not resolved here |
| **Medical status** | ⚠️ **None of this is medical advice**, and none of it is a prognosis |

---

## 6 · What could NOT be established — as prominently as what could

### 6.1 · The empirical floor, stated in the repository's own required vocabulary

> ## 🔴 `PREMISE: NOBODY_LOOKED`
> **No RNA from `WWOX c.1057-2A>G` has ever been examined, in any tissue, in any system, by anyone.**
> PubMed indexes **zero** records for the allele (`WWOX AND "1057-2"` → 0, sound zero, §4.3).
>
> ## 🔴 `PREMISE: NOBODY_LOOKED`
> **No NMD assay has ever been performed on any WWOX allele of any class** — no cycloheximide, no
> emetine, no puromycin, no SMG1 inhibitor, no UPF1 knockdown (§4.2).
>
> ## 🔴 `PREMISE: UNREAD_PRIMARY`
> **PMID 30853297** (the only measurement of a WWOX **acceptor** allele's transcript) and
> **PMID 38407561** (the only patient-RNA measurement) have **no PMCID and unreachable bodies**.
> Their Methods sections are unread. Their abstracts do not mention NMD; **their bodies are unknown.**

⛔ **None of the above may be re-voiced as "NMD does not occur."** §3 establishes what the reference
sequence **permits**; it does not establish what a cell **does**.

### 6.2 · The specific unknowns

| # | not established | consequence | cost to close |
|---|---|---|---|
| U1 | **Whether the `c.1063` cryptic acceptor is used at all** | the entire §5 conditional hangs on it. `DS_AG 0.64` is moderate; competing outcomes (intron retention, intronic poly(A)) are not excluded | the wet assay — `TX-001` |
| U2 | **Relative flux between outcomes (c), (b), (d2)** | determines whether "not an NMD substrate" describes 5% or 95% of the allele's output | same assay, quantified |
| U3 | **Transcript (r.) coordinates of the final EEJ** | 5′UTR length of `NM_016373.4` unestablished (only ≥460 nt observed). CDS-relative position is exact; absolute is not | one RefSeq record — **egress blocked** |
| U4 | **Intron 8's internal sequence** (first ~778,820 nt) | PTC position for the retention outcome is UNKNOWN — though its *side* of the junction is not | reference FASTA — **egress blocked** |
| U5 | **Whether long-3′UTR NMD applies to an intron-8-terminating transcript** | the only surviving route to NMD-family degradation | not decidable by the 50–55 nt rule; needs UPF1 knockdown, not cycloheximide |
| U6 | **`c.1061`, `c.1064` are DERIVED, not read** (from ClinVar protein consequences) | each derivation leaves exactly one possible base and two independent records agree; still not a sequence read | one RefSeq lookup — **egress blocked** |
| U7 | **Whether `NM_016373.3` shares `.4`'s exon structure** | Davids 2019 and other older papers use `.3`. **Not checked and not assumed** | one RefSeq comparison — **egress blocked** |
| U8 | **Protein consequence of `p.Gln353_Gln354del`** | `UNKNOWN AND STRUCTURALLY CONTESTED`; mid-helix deletion at pLDDT 60–76 | wet: expression + localisation + partner binding |
| U9 | **Bodies of PMID 30853297 and 38407561** | `UNREAD_PRIMARY`; Methods could contain unindexed NMD arms | inter-library loan / author contact — not achievable from this deployment |

⛔ **Tool blocks recorded, not retried:** direct sequence egress (Ensembl, NCBI/eutils, EBI) returns
**403 at CONNECT** throughout. Two paywalled bodies have **no PMCID**, so no fetch target exists.
**A tool block is not a scientific stop** — the adjudication was completed from local reference data
and retrievable bodies, and every place the block bites is named above.

### 6.3 · 🎯 The single experiment that settles it

> **One RT-PCR, on RNA from cells carrying the allele, across the exon 8 → exon 9 junction, with
> Sanger sequencing of every band — including the apparently-normal one.**

Four design constraints that this adjudication makes non-negotiable, each of which would otherwise
produce a **false negative**:

1. 🔴 **The aberrant product is 6 nt SHORTER than normal, not longer.** `+8` is a genomic offset from
   the variant, not an amplicon size change. On a ~271 nt amplicon that is **2.2%**. **Not agarose,
   and not native PAGE** (a 6-nt heteroduplex migrates anomalously): **capillary electrophoresis /
   GeneScan, denaturing, ±1 nt, with a 6-nt indel sizing standard on the same run.** *A laboratory
   running the obvious gel would report wild-type splicing and be wrong.*
2. 🔴 **An intron-8-anchored reaction plus 3′ RACE is mandatory.** A transcript terminating in intron
   8 **has no exon 9**, so the exon-9 reverse primer has no site and the species is **absent from the
   trace** — where its absence would be silently misread as support for the cryptic-acceptor outcome.
3. 🟡 **The ±cycloheximide arm has LESS power than the current packet implies**, because under the
   surviving outcome **there is no PTC**. Retain it — but retain it to *catch a competing
   PTC-containing species* and to test U5, with a **vehicle twin and an endogenous NMD-sensitive
   positive control**, not as the primary readout. **A cycloheximide-insensitive loss of transcript
   is expected for the retention outcome and must not be scored as NMD.**
4. ⚠️ **Do not normalise to the exon 4–6 "core" amplicon.** Davids measured why: the short isoform's
   own exon 5–6 junction **rises when the long isoform is lost**, so that denominator moves with the
   lesion. Use a long-transcript-specific amplicon (exon 7–8) and report isoform composition.

**And the single record that would settle the architecture half at zero cost:** the RefSeq
`NM_016373.4` sequence itself, which would convert U3, U4, U6 and U7 from derived to read in one
retrieval — currently blocked at CONNECT.

---

## 7 · Provenance

- **Local reference data read directly this session:**
  `disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv` (1,327 records) and
  `disease-models/wwox/analysis/data/WWOX_Q9NZC7_AlphaFold.pdb`. The exon table, the 729/729
  concordance, the splice-site boundary pins, the exon-9 5′ sequence, the stop codon and the
  intron-8 3′ end were **re-derived independently**, not inherited from any prior document.
- **Bodies retrieved this session:** PMC6296882 (PMID 30362252) in full; PMC11298992 (PMID 39101447)
  via the census artefact plus fresh retrieval. According to PubMed.
- **Repository documents read before any external search**, as the brief requires:
  `therapeutic_hypotheses_ledger_current.md:216`; `paper_registry_current.md:6469` and `:6535`;
  `discovery_ledger_current.md` `DL-BIO-002` and `DL-MECH-045`;
  `analysis/wwox_splice_transcript_census_20260921.md`;
  `research/tx001_experiment_decision_packet_20260921.md`;
  `research/commit_candidates/CC-20260922-SPLICE-ARM-01.md`;
  `analysis/recovery_and_dpag_rederivation_20260922.md`.
- **Agreements and disagreements with prior session work, stated:** §3.3 **confirms**
  `CC-20260922-SPLICE-ARM-01` §7/§9 and adds one new exclusion (`c.1064 = G`, making the 8-nt reading
  dead unconditionally rather than conditionally). §4.5 **confirms** its §2 by independent retrieval.
  §1 **adds** the origin trace, which was not previously drawn. §3.1 rows (b) and (d2) and §3.2
  **add** the exosome/long-3′UTR distinctions, which no prior document in this repository makes.
- **No canonical file, registry, ledger or queue was modified. No `BATCH_COMMIT` was run.**

---

**END OF DOCUMENT — complete run.**
