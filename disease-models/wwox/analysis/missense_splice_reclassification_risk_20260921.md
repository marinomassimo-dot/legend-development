# How much of PROTEIN-RESCUE survives the splice threat — a per-allele reclassification-risk audit of the reported WWOX missense alleles

**Scientist B · 2026-09-21 · READ-ONLY toward every canonical file and every ledger. No commit candidate. No receipt written. No canonical file modified. No ledger appended. `TX-001`–`TX-007` are NOT re-ranked here and the therapeutic-class census is NOT edited.**

🔴 **This is classification for research planning. It is NOT treatment advice, NOT a recommendation, and NOT a statement about any individual.** It reasons about a WWOX-DEE genotype class assembled from published literature, never about a person.

Bibliographic records and full text below are from **PubMed / PubMed Central**. DOI links are given per source.

---

## VERDICT

**Almost nobody has looked, and where the position can be checked almost nothing is at risk.** Of the **19 distinct WWOX missense alleles this repository can enumerate**, exactly **one has ever had RNA examined (`p.(Ser318Leu)` — a negative, in leukocytes, the lowest-WWOX tissue of the 54 in GTEx v8), one carries a published in-silico splice flag that was never tested (`p.(Ile136Val)` `c.406A>G`), and the remaining 17 are called missense purely because a DNA-level substitution changes an amino acid** — which is Piard's own finding about their own aggregate, stated in the indicative: *"All missense pathogenic variants but one (P3; p.[Ser318Leu]) are interpreted based on in silico studies without experimental evidence (no RNA or protein sequence analyzed)."* **Exactly one allele is unambiguously junction-adjacent** — `p.(Gly137Glu)`, which can only be `c.410G>A`, the **first nucleotide of exon 5** — while the therapeutically most consequential allele, `p.(Gln230Pro)` (8 patients, 6 families), sits **≥66 nt from any junction**, so the splice threat resizes PROTEIN-RESCUE from **28.4 % to a range of ≈19–28 % of classified alleles and the evidence supports the upper end**. Confidence: **MODERATE-HIGH** on the "nobody has looked" count (it is a first-hand quotation from an artefact on disk, re-matched programmatically), **MODERATE** on the exon positions (8 of 9 exon boundaries are anchored to published verbatim coordinates; the exon 7/8 boundary is undetermined and two alleles are therefore unratable), and **LOW** on any transfer of an at-risk fraction onto the census's 25, whose member alleles are not named by their source.

---

## 1 · METHOD and sources

### 1.1 · What was done, and what was not

A synthesis over LEGEND's own records and over three full-text artefacts **already on disk**. 🔴 **No new full text was read and nothing was fetched** — the one-full-text budget was deliberately **not** spent, because no reachable candidate would have changed a count:

- `PMID 39039877` (12 children, Peking University First Hospital — the only cohort that would add missense alleles in bulk) is *Zhonghua Er Ke Za Zhi*, DOI `10.3760/cma.j.cn112140-20240229-00135`, a Chinese-language journal with no PMC handle in LEGEND's records. Its six novel missense alleles are carried below **at abstract level**, exactly as the class census carries them.
- `PMID 29808465` (Johannsen 2018 — the Q230P functional paper) is recorded in `full_text_queue_current.md` as **`unrecoverable_by_these_routes`**, `pmc_id: null`, closed at Springer. Its qRT-PCR result is carried below **at abstract level and labelled as such on every line it touches**.
- `PMID 30853297`, `PMID 38407561`, `PMID 42721537` are splice-allele papers, not missense papers, and are already inventoried in the splice census.

🔴 **`NO RECORD MATCHED` ≠ `NOT HELD`, and it was checked both ways.** `registry_records.py get --pmid 39039877` and `--pmid 30356099` each returned only surface preambles — no record — while `grep -rn "39039877" --include=*.md disease-models/` returns hits in **`paper_registry_current.md` (line 1603), `literature_tracking_log_current.md` (line 3467), `full_text_queue_current.md`, `batch_queue.md`** and two analysis files. **Both papers are held.** The tool's surface list excludes `analysis/` and reads committed state only; it is not an authority on what the repository contains.

### 1.2 · Artefacts used, fingerprinted before analysis

| Source | PMID | Artefact | bytes | chars | sha256 |
|---|---|---|---:|---:|---|
| Piard J *et al.* **"The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature."** *Genet Med* 2019;21(6):1308–1318. [DOI](https://doi.org/10.1038/s41436-018-0339-3) | **30356099** | `files/fulltext/PMID30356099_PMC_MCPtext.txt` | 33,419 | 33,357 | `5dbb1c2fb85706d9e0b62ca71a0c10c1d0f2bea5b6ccaac3569a89592c7533e3` |
| **"Novel Mutation With Literature Review: WW Domain-Containing Oxidoreductase (WWOX) Gene"** (registry title) — consanguineous Saudi family, homozygous `c.406A>G`. *Cureus* 2022. [DOI](https://doi.org/10.7759/cureus.25003) | **35712340** | `files/fulltext/PMID35712340_PMC_MCPtext.txt` | 15,396 | 15,270 | `777ca3f956db0e0bf7a28893b159793a9eaf9e641c2d9c58a02db921d616355e` |
| **"Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome"** (registry title) — WGS + gap PCR. *BMC Med Genomics* 2023. [DOI](https://doi.org/10.1186/s12920-023-01731-4) | **37974179** | `files/fulltext/PMID37974179_PMC_MCPtext.txt` | 17,775 | 17,590 | `50a6174ff75ee6aded57a5f4715a1a4d5ca43dfeea7c8ec5c945612d2ef979fb` |

**The sha256 of the Piard artefact matches the value the class census recorded this morning, to the character.** The artefact was not re-fetched and was not modified.

**Instrument check on the Piard artefact, before any count was relied on.** The italic-deletion failure is active (`thegene` ×7). Word-boundary counts in the roman class, where the zeros and the ones ARE admissible: `minigene` **0** · `SpliceAI` **0** · `MaxEntScan` **0** · `Human Splicing Finder` **0** · `NMD` **0** · `RT-PCR` **1** · `cryptic` **1** · `ESE` **1** · `ESS` **1** · `exon` **7** · `intron` **2** · `splic*` **9**. 🔴 **`References` occurs 0 times: the reference list is absent from the extraction.** Citation superscripts were elided throughout — the signature is machine-detectable as 28 occurrences of `[a-z]\.[A-Z][a-z]` (a sentence-final period fused to the next sentence's first word, which is where the superscript stood). **This is the fact that decides § 5.** HGVS is roman-class and survived: `p.` tokens — 17 distinct, all intact; `c.[0-9]` — only **2** (`c.1228G>T`, `c.600T>A`), because this paper names its variants at the protein level in prose and puts the cDNA table in **Supplemental Tables 1–4, which are named in the body and absent from the extraction. They are UNAVAILABLE, not empty.**

Per **D-14**, no figure image is inspectable and nothing below is drawn from one.

### 1.3 · The ANNOTATED / MEASURED line — reused, not reinvented

Taken verbatim from [`wwox_splice_transcript_census_20260921.md`](wwox_splice_transcript_census_20260921.md) § 0 and applied unchanged:

- **ANNOTATED** — called "splice-affecting" by position, by a diagnostic pipeline, or by a predictor. **A prediction. No RNA was looked at.**
- **MEASURED** — RNA or cDNA from that allele was actually run. **An observation.**

This file adds **one** distinction the splice census did not need, because it never arises for a canonical ±1/±2 allele:

- 🔴 **A transcript-ABUNDANCE measurement is not a splice assessment.** A qRT-PCR showing "normal WWOX transcript" tells you the message was not grossly destroyed; it does **not** tell you the junctions are correct, because the amplicon position is usually unstated and an aberrant isoform that escapes NMD is quantified as message. Abundance readouts are held in their **own column** and are never counted as MEASURED splice assessments.

### 1.4 · The exon map — how it was anchored, and where it fails

🔴 **This is the load-bearing derivation of the file and it is set out in full so it can be attacked.** Distances are meaningless without exon boundaries, and no exon/intron coordinate below was invented.

**Convention.** Distances are in nucleotides of the **coding sequence** of the canonical 9-exon transcript (`NM_016373.4` / `ENST00000566780.5`, 414 aa), **1-based with the terminal exonic nucleotide counted as 1** — so "donor 1" means the variant is the last nucleotide of the exon, and "acceptor 1" means it is the first.

**Boundaries anchored to published verbatim coordinates in artefacts on disk:**

| Boundary | Anchor | Internal consistency check |
|---|---|---|
| **exon 6 = c.517–605** | PMID 37974179, verbatim: *"The exon 6 deletion (: c.517_605del, His173AlafsTer67) is a common deletion predicted to cause a frameshift mutation resulting in a truncated protein with loss of function."* | 605 − 517 + 1 = **89 nt**, not a multiple of 3 → frameshift, which is the consequence the paper itself states. Codon 173 spans c.517–519 → **His173** is exactly the first residue removed ✓ |
| **exon 8 ends c.1056 · exon 9 starts c.1057** | PMID 37974179, verbatim: *"The exon 6-8 deletion (:c.517_1056del, His173_Met352del) theoretically produces a protein with normal WW domains"* | 1056 − 517 + 1 = **540 nt = 180 codons**, in-frame, and 352 − 173 + 1 = **180 aa** ✓. Codon 352 spans c.1054–1056 → **Met352** is exactly the last residue removed ✓. Independently corroborated by `discovery_ledger_current.md`: *"`c.1057` corrisponde al codone 353"* and exon 9 encodes *"gli ultimi ~62 amminoacidi"* (414 − 353 + 1 = 62 ✓) |
| **exon 4 ends c.409** | PMID 35712340, Table 3, verbatim: `c.406A>G` at `Chr16:78149048` and `c.409+1G > T` at `Ch16:78149052`. **The two genomic positions are 4 bp apart and the two cDNA positions are 4 nt apart counting through c.409** — so the exon runs contiguously to c.409 and the intron begins at +1 | The `+1` HGVS itself is the second, independent statement of the same boundary |

**Boundaries derived from the HGVS of canonical ±1/±2 splice alleles already inventoried by LEGEND** (the allele's published HGVS string is the anchor; the exon assignment is arithmetic on it):

`c.107+1G>A` → exon 1 CDS ends **c.107** · `c.172+1G>C` → exon 2 ends **c.172** · `c.229_230+2delGAGT` → exon 3 ends **c.230** · `c.516+1G>A` and `c.517-2A>G` → exon 5 ends **c.516** (which re-derives the exon 6 start already anchored above) · `c.605+5G>A` and `c.606-1G>A` → exon 6 ends **c.605** (same) · `c.1057-2A>G` → exon 9 starts **c.1057** (same).

**The one boundary that could NOT be determined, and it costs two alleles:**

🔴 **The intron 7 donor — the exon 7 / exon 8 boundary — is UNKNOWN.** It is bracketed, and only bracketed, by PMID 41124647's IGV statement quoted in [`wwox_missense_cma_degradation_audit_20260921.md`](wwox_missense_cma_degradation_audit_20260921.md): *"the variant was located on exon 7 … (:c.C754G:p.P252A) … the other homozygous variant … located on exon 8 … (:c.C844G:p.P282A)"*. **Therefore `c.754 ≤ (end of exon 7) ≤ c.843`, a 90-nt window, and nothing in this repository narrows it further.** Any allele falling inside that window has an **UNKNOWN** exon and an **unratable** boundary distance. **No genomic coordinate was computed for it and none is presented.**

**Resulting map (8 of 9 boundaries determined):**

```
exon 1  c.1–107      exon 2  c.108–172    exon 3  c.173–230
exon 4  c.231–409    exon 5  c.410–516    exon 6  c.517–605
exon 7  c.606–B      exon 8  c.B+1–1056   exon 9  c.1057–1245 (stop)
                     where  754 ≤ B ≤ 843   — UNDETERMINED
```

🔴 **Exon 1's 5′ end and exon 9's 3′ end are not splice junctions** (transcription start upstream of the ATG; stop codon and 3′UTR downstream). Alleles in those exons are given **one** distance, not two.

### 1.5 · Derived nucleotides — declared as derived

Most WOREE missense alleles are published **at the protein level only**. Where a c. position is needed, it is derived two ways, both declared:

1. **Codon span** — codon *n* spans `c.(3n−2)` … `c.3n`. Arithmetic, not a source.
2. **Variant nucleotide** — where the amino-acid substitution has a **unique single-nucleotide route**, the codon position is forced and the nucleotide follows.

🔴 **The codon arithmetic was validated against nine independent published c./p. pairs before it was relied on, and all nine pass:** `c.140`/p.47 · `c.406`/p.136 · `c.689`/p.230 · `c.716`/p.239 · `c.911`/p.304 · `c.1114`/p.372 · `c.1228`/p.410 · `c.517`/His173 · `c.1056`/Met352. 🔴 **A derived nucleotide is marked `‡` in the table and is never presented as the paper's.** Where the route is ambiguous (`p.(Arg156Ser)`: position 1 of a CGN codon or position 3 of an AGR codon), only the codon span is given.

### 1.6 · Quote verification

Every verbatim quotation in this file was re-matched programmatically against its artefact under whitespace-and-dash normalisation. **Piard (PMID 30356099): 12 of 12 matched. PMID 35712340: 6 of 6 matched. PMID 37974179: 2 of 2 matched. Total 20 of 20, zero misses.**

🔴 **Three of the Piard quotations were then re-verified a second time, independently and on a separate run, after an Orchestrator steer supplied them with a matching count.** The count was **not** taken on trust: the two long sentences (§ 3.1 and § 2.4) and the **full contiguous 10 % / 3 % block of § 5.1** each returned **exactly 1** occurrence against the same sha256, the block matched as one continuous span rather than in pieces, and the sole occurrence of *"its causal role is questionable"* was traced to its subject — **`p.(Gly410Cys)`**, which is where § 2.3 already attributes it. **Independent re-derivation, same result.**

---

## 2 · The per-allele table

**Splice assessment** uses three values and only three: **NONE** (nobody looked) · **IN-SILICO** (a predictor was run; a prediction) · **MEASURED** (RNA or cDNA was run). The **Abundance** column is separate and is *not* a splice assessment (§ 1.3).
`Ev.` — **FT** = from a full text on disk · **DOS** = from a LEGEND dossier over a complete full-text read · **ABS** = 🔴 abstract-level.

### 2.1 · WOREE / WWOX-DEE missense alleles

| # | Allele (p., as published) | c. (‡ = derived) | Exon | nt to nearest junction | Splice assessment | Abundance readout | Source PMID | **RISK-OF-RECLASSIFICATION** | Ev. |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | **p.(Thr12Met)** | `c.35C>T` ‡ (also assumes an ACG codon) | 1 | donor **73** | **NONE** | — | 39507621 | **LOW** | repo FT record |
| 2 | **p.(Glu17Lys)** | `c.49G>A` ‡ | 1 | donor **59** | **NONE** | — | 30356099 | **LOW** | **FT** |
| 3 | **p.(Pro47Arg)** | `c.140C>G` | 2 | acceptor 33 · donor 33 → **33** | **NONE** | — | 30356099 · 33916893 | **LOW** | **FT** + **DOS** |
| 4 | **p.(Ile136Val)** | `c.406A>G` | 4 | **donor 4** | 🔴 **IN-SILICO** — the only WWOX missense allele in the literature with a published splice prediction. Body mood: *"The in silico predicted that the position of the identified variant **might lead** to significant alterations in mRNA splicing owing to an altered splice site."* ⚠️ The **abstract re-voices the same sentence in the indicative** (*"led to"*). **The body's hedge is the paper's mood and it stays.** Never tested by RNA | — | 35712340 | 🔴 **HIGH** — 4 nt from the exon-4 donor **and** predictor-flagged; the paper itself cannot say whether this behaves as a missense allele at all | **FT** |
| 5 | **p.(Gly137Glu)** | `c.410G>A` ‡ — **the codon position is forced**: Gly (GGN) → Glu (GAR) is only reachable at codon position 2 | 5 | 🔴 **acceptor 1 — the FIRST nucleotide of exon 5** | **NONE** | — | 30356099 (**3 families**) | 🔴 **HIGH — the highest-risk allele in the set.** The first exonic nucleotide is part of the 3′ splice-site consensus. **Nobody has looked** | **FT** |
| 6 | **p.(Ala149Thr)** | `c.445G>A` ‡ | 5 | acceptor 36 · donor 72 → **36** | **NONE** | — | 39039877 | **LOW** | 🔴 **ABS** |
| 7 | **p.(His150Pro)** | `c.449A>C` ‡ | 5 | acceptor 40 · donor 68 → **40** | **NONE** | — | 30356099 | **LOW** | **FT** |
| 8 | **p.(Arg156Ser)** | codon `c.466–468` (route ambiguous — no nucleotide derived) | 5 | **49–51** | **NONE** | — | 39039877 | **LOW** | 🔴 **ABS** |
| 9 | **p.(Leu186Val)** | `c.556C>G` ‡ | 6 | acceptor 40 · donor 50 → **40** | **NONE** | — | 39039877 | **LOW** | 🔴 **ABS** |
| 10 | **p.(Lys200Glu)** | `c.598A>G` ‡ | 6 | **donor 8** | **NONE** | — | 30356099 | **MODERATE** — inside the 3′ end of the exon, outside the core donor consensus. Also one of the two alleles the paper itself could not disentangle in P19 | **FT** |
| 11 | **p.(Gln230Pro)** 🔴 *the most recurrent WWOX allele of any class: 8 patients / 6 families* | `c.689A>C` | **7** | acceptor 84 · donor 66–155 → **66–84** | **NONE** | ⚠️ **qRT-PCR: normal WWOX transcript levels** in donor-derived fibroblasts; Western: protein not detected; authors leave *"impaired translation or premature degradation"* undiscriminated. 🔴 **ABSTRACT-LEVEL — LEGEND has never read this paper and records it as `unrecoverable_by_these_routes`.** Amplicon position unstated → **not a splice assessment** | 29808465 · 33916893 · 30356099 · 40875931 | **LOW** — deep exonic on both sides of the undetermined boundary, and the one indirect readout points away from loss of expression. 🔴 **This is the most decision-relevant row in the file: the biggest allele-specific constituency in the disease is the least exposed to the splice threat** | **DOS** + **FT**; 🔴 **ABS** for the abundance readout |
| 12 | **p.(Leu239Arg)** | `c.716T>G` | **7** | acceptor 111 · donor 39–128 → **39–111** | **NONE** — 🔴 no Western, no fibroblast work, no transcript of any kind | — | 41153369 · 42092735 | **LOW** | LEGEND partial FT reads |
| 13 | **p.(His263Arg)** | `c.788A>G` ‡ | 🔴 **UNKNOWN — 7 or 8** | 🔴 **UNKNOWN** — c.788 lies inside the undetermined intron-7 bracket (c.754–c.843), so junction adjacency **cannot be excluded or established** | **NONE** | — | 39039877 | 🔴 **UNDETERMINED — not rated.** Resolving one exon boundary would rate it | 🔴 **ABS** |
| 14 | **p.(Ser304Tyr)** | `c.911C>A` **or** `c.991C>A` — 🔴 the source contradicts itself between its text/abstract and its Table 1/Discussion | 8 (if c.911) | acceptor 68–157 · donor 146 → **≥68** (if c.911) | **NONE** | — | 39039877 + repo | 🔴 **UNDETERMINED on nomenclature.** Codon arithmetic settles which string is internally consistent — codon 304 spans c.910–912, so only `c.911C>A` encodes Ser304 — **but that is LEGEND's arithmetic, not the paper's correction, and the allele is not normalised here** | 🔴 **ABS** |
| 15 | **p.(Ser318Leu)** | `c.953C>T` ‡ | 8 | acceptor 110–199 · donor 104 → **104** | 🔴 **MEASURED — the ONLY missense RNA readout in the WWOX literature, and it is a NEGATIVE.** Verbatim: *"In P3, total RNA analysis by Sanger sequencing of reverse transcription PCR (RT-PCR) products **failed to detect any splicing anomaly in leukocytes**."* **First-hand in Piard** (their own patient P3) and **first-hand in LEGEND** (the artefact is on disk and the sentence re-matched). Bounded — see § 2.4 | — | 30356099 (**2 families**) | **LOWEST** — deep exonic *and* the one allele with an experimental discriminator. Also the only missense in the 2019 series **not** called probably damaging by PolyPhen-2 | **FT** |
| 16 | **p.(Met326Arg)** | `c.977T>G` ‡ | 8 | acceptor 134–223 · donor 80 → **80** | **NONE** | — | 39039877 | **LOW** | 🔴 **ABS** |
| 17 | **p.(Thr358Ile)** | `c.1073C>T` ‡ | 9 | **acceptor 17** (exon 9 is terminal — one junction only) | **NONE** | — | 30356099 | **MODERATE** — and independently UNASSIGNABLE: the authors state *"It is not possible to determine whether one or both of these variants are the disease-causing missense variant in P19"* and that Thr358 *"is not located in a known functional domain"* | **FT** |

### 2.2 · SCAR12 missense alleles (same gene, different phenotype pole — counted separately)

| # | Allele | c. (‡ = derived) | Exon | nt to nearest junction | Splice assessment | Source | **RISK** | Ev. |
|---:|---|---|---|---|---|---|---|---|
| 18 | **p.(Pro47Thr)** | `c.139C>A` ‡ | 2 | acceptor 32 · donor 34 → **32** | **NONE** (a WW1 **peptide-binding** loss was measured — a protein assay, not an RNA one) | 24369382 | **LOW** | **ABS** + **DOS** |
| 19 | **p.(Gly372Arg)** | `c.1114G>C` | 9 | **acceptor 58** | **NONE** | 24369382 · 35712340 Table 3 | **LOW** | **ABS** |

### 2.3 · Listed but excluded from every count

| Allele | Why excluded | Position note |
|---|---|---|
| **p.(Gly410Cys)** `c.1228G>T` | Excluded by the reviewing authors themselves: mild phenotype, *"its causal role is questionable"*, homozygous in two gnomAD individuals | exon 9, acceptor 172 |
| **p.(Ser200Arg)** `ENST00000402655:c.600T>A` | Affects only a non-RefSeq 311-aa isoform; authors declined to consider the genotype causative | not on the canonical transcript |
| **p.(Pro252Ala)** `c.754C>G` · **p.(Pro282Ala)** `c.844C>G` | 🔴 **Not WOREE alleles** — germline homozygous in a cancer proband who at 35 *"did not suffer from WWOX-related nervous system disease"* | 🔴 **These two are the bracket.** By the paper's own IGV assignment, c.754 is the *last* named position on exon 7 and c.844 the *first* on exon 8 — so **each could be a terminal exonic nucleotide (donor 1 / acceptor 1) and neither can be rated.** Noted because it is exactly the geometry that would matter if they were WOREE alleles. P252A's measured **normal mRNA** is an abundance readout, not a splice assessment |
| **p.(Leu291Pro)** | Annotated *"Esophageal squamous cell carcinoma, somatic"* — not a germline WWOX-disorder allele | — |

### 2.4 · The one measured negative, and exactly what it bounds

🔴 **Verified first-hand.** The sentence is in the Piard artefact on disk, at the character level, and it is **Piard's own patient P3, not a citation to another group.** It is preceded in the same paragraph by the general statement that generates this whole file, and followed by the reason there is only one: *"RNA studies were not performed for other patients because appropriate blood samples were not available at the time of the molecular diagnosis."*

🔴 **Read that second sentence for what it says: the other patients went untested for a LOGISTICAL reason — sample availability — and not because anyone judged that they did not need testing.** This is an absence of evidence **with a named, mundane cause**, which is the strongest possible form of "nobody has looked": it carries no implicit reassurance whatsoever. **The 17 NONE rows in § 2 are not 17 quiet negatives. They are 17 tubes that were never drawn.**

**What it excludes:** a splicing anomaly in `p.(Ser318Leu)` large enough to be visible as a Sanger trace anomaly in RT-PCR product from peripheral leukocytes.

**What it does NOT exclude — four bounds, the first of which is LEGEND's own datum and is the strongest:**

1. 🔴 **It was run in the worst possible tissue, and this repository already knows it.** `biomarker_candidates_current.md` records **whole blood at 0.71 TPM — "the lowest of the 54 GTEx v8 tissues (~10 % of brain), near the detection floor"** — and **demoted blood from primary proxy** on exactly that ground: *"expression too low for reliable direct quantification of the WWOX product."* A qualitative RNA readout in the lowest-expressing tissue of 54 has poor sensitivity by the repository's own standard. LCL (3.17 TPM, 46 % of brain) is the proxy LEGEND actually endorses, and it was not used.
2. **A tissue-specific effect.** Splicing regulators differ between leukocyte and neuron; a leukocyte-negative does not transfer to brain. WWOX's relevant tissue is brain.
3. **A minor aberrant isoform.** Sanger sequencing of a mixed RT-PCR pool reports the majority species; a subpopulation below roughly a fifth of the pool is not resolvable. *(Methodological bound, general knowledge, labelled as mine — the paper makes no sensitivity statement.)*
4. **The other 18 alleles.** It is a result about one allele. It says nothing about any other.

**Net:** the negative is real, it is first-hand, and it is **bounded**. It is enough to keep `p.(Ser318Leu)` in PROTEIN-RESCUE at LOWEST risk. It is **not** enough to generalise to the class, and Piard does not generalise it either — their very next sentences argue the opposite direction.

---

## 3 · The headline count

### 3.1 · Over LEGEND's enumerable set

**Denominator: 19 distinct missense alleles** — 17 WOREE/WWOX-DEE (§ 2.1) + 2 SCAR12 (§ 2.2). Excluded alleles (§ 2.3) are not in it.

| Splice assessment | Alleles | Share | Which |
|---|---:|---:|---|
| **MEASURED** | **1** | **5.3 %** | `p.(Ser318Leu)` — **negative**, leukocyte RNA, bounded |
| **IN-SILICO** | **1** | **5.3 %** | `p.(Ile136Val)` `c.406A>G` — hedged (*"might lead"*), predictor **unnamed** by the paper, never tested |
| **NONE** | **17** | **89.5 %** | everything else |

🔴 **17 of 19 reported WWOX missense alleles are classified as missense for one reason only: a DNA-level substitution changes an amino acid.** That is not an inference from silence — **the paper that aggregates most of them says it in its own indicative voice**, twice:

> *"In most cases reported here and published in the medical literature, [WWOX] sequence variations are described at the basic DNA level."*

> *"All missense pathogenic variants but one (P3; p.[Ser318Leu]) are interpreted based on in silico studies without experimental evidence (no RNA or protein sequence analyzed)."*

### 3.2 · Over Piard's own internal denominator — the same answer, first-hand

Piard's aggregate covers *"All missense variants identified in individuals with [WWOX]-related encephalopathy (**11 aa changes in 12 families**)"*. Against that denominator: **1 of 11 with experimental evidence, 10 of 11 without — 90.9 % NONE.** 🔴 Only **8** of those 11 are nameable from the retrievable text (`Gln230Pro`, `Glu17Lys`, `Gly137Glu`, `Lys200Glu`, `Pro47Arg`, `Ser318Leu`, `Thr358Ile`, `His150Pro`); the remaining **3 are in Supplemental Tables 1–4, which are UNAVAILABLE, not empty.**

**Two independent routes to the same number, 89.5 % and 90.9 %, one of them the source's own count.**

### 3.3 · Does the denominator match the census's 25?

🔴 **No, and it cannot — they are different objects, and conflating them would be exactly the error this file exists to prevent.**

| | This file | The class census |
|---|---|---|
| Unit | **distinct missense variants**, across the whole published literature | **missense allele copies** (13 + 2×6) within **one** 2025 cohort of 44 classified individuals |
| Size | **19** | **25** |
| Members named? | yes, all 19 | 🔴 **no — the source publishes genotype-class percentages and does not name its alleles** |

The two numbers are close by coincidence. **A fraction computed on the 19 cannot be validly transferred onto the 25**, because the 25's composition is unknown and a cohort weights recurrent alleles by how many copies it happens to contain. Every transfer below is flagged as a declared default, not a derivation.

---

## 4 · The resized class, as a range

### 4.1 · The at-risk set, on the evidence

| Rating | Alleles | Of 19 |
|---|---|---:|
| 🔴 **HIGH** | `p.(Gly137Glu)` (exon-5 acceptor, +1) · `p.(Ile136Val)` (exon-4 donor, −4, predictor-flagged) | **2 — 10.5 %** |
| **MODERATE** | `p.(Lys200Glu)` (donor −8) · `p.(Thr358Ile)` (acceptor +17) | 2 — 10.5 % |
| 🔴 **UNDETERMINED** | `p.(His263Arg)` (inside the intron-7 bracket) · `p.(Ser304Tyr)` (contradictory nomenclature) | 2 — 10.5 % |
| **LOW / LOWEST** | the other 13 | 13 — 68.4 % |

**At-risk fraction: 10.5 % firm (2/19); 31.6 % (6/19) if every MODERATE and every UNDETERMINED allele went the wrong way.**

### 4.2 · PROTEIN-RESCUE, as a range

Applying that fraction to the census's 25 of 88 — **a declared default, not a derivation (§ 3.3, DEFAULTS_TAKEN 6)**:

| Scenario | Missense alleles surviving | **PROTEIN-RESCUE, % of 88 classified alleles** |
|---|---:|---:|
| **All missense alleles survive** (nothing is reclassified) | 25 | **28.4 %** ← *the census's current figure* |
| **HIGH-risk fraction reclassified** (10.5 %) | ≈22 | **≈25 %** |
| **Worst case — MODERATE and UNDETERMINED also reclassified** (31.6 %) | ≈17 | **≈19 %** |

> ### 🔴 **PROTEIN-RESCUE = 19 %–28 % of classified alleles (≈17–25 of 88). The evidence supports the UPPER end.**

**Four reasons, each checkable above:**

1. **Exactly one allele of 19 is unambiguously junction-adjacent** (`p.(Gly137Glu)`). Every other allele whose position is determinable lies **≥8 nt** from the nearest junction, and 13 of them lie **≥30 nt**.
2. 🔴 **The therapeutically decisive allele is the safest one.** `p.(Gln230Pro)` — 8 patients across 6 families, the most recurrent WWOX allele of any class — is **66–84 nt from any junction** and its one indirect readout (abstract-level) is **normal transcript abundance**. The largest single constituency inside PROTEIN-RESCUE is where the splice threat reaches least.
3. **The one measurement that exists is a negative**, and although bounded it is a negative rather than a positive.
4. **Even the generic upper bound is small.** Transferred at face value, "up to 10 %" moves 2–3 alleles of 25, i.e. from 28.4 % to ≈25 % — inside the range above, not below it.

**Why the lower end cannot be excluded:** nobody has looked at 17 of 19; ESE/ESS disruption is **not** predictable from boundary distance and Piard names that mechanism explicitly; two alleles cannot be rated at all because one exon boundary is undetermined; and a deep-exonic position is a weak defence, not a proof.

### 4.3 · Individuals — more fragile than alleles, and say why

The census gives **6 of 44 individuals served by PROTEIN-RESCUE alone** (missense/missense). Those need **both** alleles to survive, so the individual figure falls as the square: at 10.5 % it is ≈5/44; at 31.6 % it is ≈3/44. **Range: 3–6 of 44 individuals (6.8 %–13.6 %).** 🔴 **Illustrative propagation only** — it assumes independence between the two alleles of a person and transfers a fraction onto unnamed alleles. It is not a count and no source states it.

### 4.4 · The finding that resizes nothing but reframes everything

🔴 **Splice reclassification is not the binding constraint on PROTEIN-RESCUE, and saying so is the honest reading.** The class census already records that the class has **zero demonstrated members for a different reason**: no function-at-matched-abundance measurement has ever been made on any WWOX missense protein, and the TSC2 comparator says **31/80 = 38.75 %** of known-pathogenic missense alleles have *normal* abundance, so an abundance-only criterion misclassifies about two in five. **The splice threat moves the class from 28 % to ~19–28 % of alleles. The abundance-versus-function problem already makes 100 % of it conditional.** The splice threat is real, it is worth the cheap test in § 6, and it is **second-order**.

---

## 5 · The generic-vs-WWOX ruling on "up to 10 %"

### 5.1 · What Piard actually wrote, in order, with the mood preserved

> *"Exonic SNVs could affect physiological acceptor/donor splice sites, but also exonic splicing enhancer (ESE) and exonic splicing silencer (ESS)."* — **modal, "could"**
>
> *"Moreover, the activation of cryptic splice sites by SNVs is a well-understood pathological mechanism in many genetic disorders"* — **a general statement about other genes**
>
> *"Up to 10% of known disease-associated missense variants, but only 3% of common SNPs, alter pre-mRNA splicing."* — **an upper bound, about disease-associated missense variants IN GENERAL.** 🔴 **The "but only 3% of common SNPs" clause is not decoration and must travel with the figure: it is a case–control contrast, and it is the authors' argument that the 10 % is disease-ENRICHED rather than a background rate.** Quoting the 10 % without it makes the sentence weaker than the paper's, which is its own kind of distortion. **It also does not make the figure any less generic — the contrast is between two classes of variant across all genes, and neither class is WWOX.**
>
> *"It is likely that a fraction of predicted missense variants identified in patients with [WWOX]-related encephalopathy results in loss of expression due to abnormal splicing."* — 🔴 **a hedged expectation. "It is likely that a fraction" is not a finding and not a rate.**
>
> *"This is all the more probable for a gene with pathogenic loss-of-function alleles."* — **a plausibility argument, not evidence**

### 5.2 · The ruling

🔴 **IMPORTED PREMISE. It is not Piard's finding, it is not a measurement on WWOX, and it was never tested on a single WWOX allele.**

**The evidence that it carries a citation is machine-detectable in the artefact.** The sentence before it ends *"…also impact on mRNA stability."* and is fused directly to *"Up to 10%…"* with no space; the 10 % sentence itself ends *"…alter pre-mRNA splicing."* and is fused directly to *"It is likely that a fraction…"*. **Those fusions are where superscript citation numbers stood before the extractor deleted them** — the signature occurs **28 times** across this artefact. 🔴 **And `References` occurs 0 times: the bibliography is absent from the extraction, so the cited source cannot be named from the artefact.** It is UNAVAILABLE, not absent from the paper.

**Piard measured splicing exactly once in this entire paper — one RT-PCR, one patient, one negative.** The 10 % is borrowed; the WWOX-specific sentence that follows it is explicitly hedged; and the paper's own data point runs the other way.

### 5.3 · Tracing it — attempted, partial, and labelled as such

🔴 **The trace could not be completed from LEGEND's evidence and the result below is NOT verified against Piard's reference list.** Two web searches (no fetch, no new artefact, no paper read) return a single dominant candidate for a ~10 % figure over disease-causing exonic variants:

**Soemedi R *et al.* (Fairbrother WG lab). "Pathogenic variants that alter protein code often disrupt splicing." *Nat Genet* 2017 (PMID 28416821)** — 🔴 *title, year and PMID from a web-search result; the full author list and page range were not verified and are therefore not reproduced* — a massively parallel splicing assay (MaPSy) over **4,964 exonic disease-causing mutations**, of which **~10 % altered splicing**.

**Status: CANDIDATE, unverified.** LEGEND cannot check it, because the reference list is not in the artefact and the paper was not re-fetched. 🔴 **This attribution must not be recorded as Piard's citation.**

**And the ruling does not depend on it.** Two things hold either way:

1. 🔴 **Possible scope drift in the transfer.** The candidate source's denominator is *exonic disease-causing mutations* (a class that includes nonsense and synonymous changes); Piard renders it as *"disease-associated **missense** variants"*. **If the candidate is right, the figure has already been narrowed once in the retelling, before ever reaching WWOX.** Not asserted — flagged.
2. 🔴 **A generic rate is a prior over a whole variant class; it is not a per-allele probability, and the at-risk fraction is not uniformly distributed.** Splice-disrupting exonic variants concentrate near junctions and in splicing regulatory elements — which is precisely why § 2's position column exists. **For WWOX the positional distribution is the more informative datum than the imported rate: 1 of 19 alleles is junction-adjacent, and it is not the one carrying the patients.**

**What may NOT be written, in any file, on this evidence:** *"10 % of WWOX missense alleles are splice alleles."* **"Up to 10 %" is an upper bound on a different gene set, and "it is likely that a fraction" is a hedged expectation. Neither becomes a rate for WWOX.**

---

## 6 · What would settle it — concretely, and cheaply

**Tier 0 — free, today, zero samples, and it would move 17 alleles off NONE.**
Run **SpliceAI + Pangolin + MMSplice** over all 19 alleles (and over the 3 unnamed ones, once the Piard supplement is acquired). LEGEND has done exactly this before — `NS-008` in `discovery_ledger_current.md` records SpliceAI DS_AL 0.96 / DS_AG 0.64 and MaxEntScan Δ −7.95 for `c.1057-2A>G`, marked **`done (in-silico)`** — so the capability and the reporting convention already exist in-repo. 🔴 **It produces PREDICTIONS. It moves alleles from NONE to IN-SILICO and never to MEASURED,** and it would leave `p.(Gly137Glu)` and `p.(Ile136Val)` exactly where they are: flagged and untested.

**Tier 1 — the measurement. One reaction per allele.**
Junction-spanning RT-PCR across the flanking junctions, ± NMD block (cycloheximide or emetine), with **band quantification and amplicon sequencing**, on RNA from carriers. Priority order is given by § 4.1: `p.(Gly137Glu)` first (3 families, exon-5 +1), then `p.(Ile136Val)`, then `p.(Lys200Glu)` and `p.(Thr358Ile)`.
🔴 **Do it in LCL, not whole blood.** LEGEND's own proxy ranking is unambiguous — whole blood 0.71 TPM (floor, demoted), fibroblast 2.24, **LCL 3.17 (46 % of brain)**. Repeating Piard's leukocyte design would reproduce Piard's sensitivity problem.

**Tier 2 — no patient needed at all.** A heterologous minigene, the design PMID 39101447 already ran for `c.172+1G>C` (exons 1–3, shortened intron, HEK293T, RT-PCR + Sanger). For `p.(Gly137Glu)` the construct is an exon 4–5–6 cassette. **This answers the question with synthetic DNA and no sample**, and it is the only tier that can be started without finding a single family.

### 6.1 · Does the census's banked-RNA assay answer this question too?

🔴 **NO — same assay, different samples, and the distinction matters.**

| | The census's Tier-1 experiment | This question |
|---|---|---|
| Whose RNA | patients on the two recurrent **canonical splice** alleles `c.107+1G>A` (5 patients) and `c.606-1G>A` (5 patients) | patients on **missense** alleles — `p.(Gly137Glu)`, `p.(Ile136Val)`, `p.(Lys200Glu)`, `p.(Thr358Ile)` |
| Overlap | 🔴 **none.** The ten patients in the census's cohort do not carry these missense alleles | — |
| Junctions interrogated | intron 1 donor · intron 6 acceptor | exon 4/5 junction · exon 6 donor · exon 8/9 acceptor |

**What DOES transfer, and it is not nothing:**
- **The method, wholesale** — junction-spanning primers, NMD block, band quantification, amplicon sequencing. No new assay development.
- **A validated instrument for one of the three junctions** — the published Schirmer exon 8→9 vs core (exons 4–6) RT-qPCR (`DL-BIO-003`) already quantifies the exon 8/9 junction, which is the one `p.(Thr358Ile)` sits 17 nt inside.
- **The protocol, the ethics and the shipping** — any laboratory already drawing blood for the splice-allele cohort can draw from missense carriers under the same protocol. **The marginal cost of answering this question alongside that one is a few extra tubes, not a new study.**

**Bottom line for planning: one experiment, two cohorts, three primer pairs — but it is two recruitments, not one.**

---

## 7 · NEGATIVE RESULTS

🔴 **Read this before any number above is used.**

1. **The central result of this file is an absence.** 17 of 19 reported WWOX missense alleles have had **no splice assessment of any kind** — not RNA, not minigene, not even a predictor. **That is an absence of evidence and is written as one. It is not evidence that they splice normally.**
2. **The exon 7 / exon 8 boundary is UNKNOWN**, bracketed only to a 90-nt window (c.754–c.843) by one paper's IGV statement about two non-WOREE alleles. 🔴 **Two alleles — `p.(His263Arg)` and, if one accepts the c.911 reading, part of the reasoning for `p.(Ser304Tyr)` — therefore cannot be rated at all.** No genomic coordinate was invented to close the gap.
3. **Most c. positions in the table are DERIVED from the protein change**, marked `‡`, and are not the papers'. The arithmetic was validated against nine published c./p. pairs, but a derived nucleotide remains a derivation. For `p.(Arg156Ser)` the route is ambiguous and no nucleotide is given.
4. **`p.(Ser304Tyr)` is not normalised.** Its source writes `c.991C>A` in text and abstract and `c.911C>A` in Table 1 and Discussion. Codon arithmetic is consistent with only one of them; **that is LEGEND's observation, not the paper's correction**, and the allele stays UNDETERMINED.
5. **The single measured negative is bounded four ways** (§ 2.4), the strongest bound being LEGEND's own: it was run in the tissue this repository has already demoted as unfit for direct WWOX quantification.
6. **The Q230P transcript readout is abstract-level and is not a splice assessment.** LEGEND has never read PMID 29808465 and records it as unrecoverable; the qRT-PCR amplicon position is unknown; an NMD-escaping aberrant isoform is counted as message.
7. **Nine of the 19 alleles rest on abstract-level sources** (six from PMID 39039877, two from PMID 24369382, one contested). Their exon positions are derived from a protein change reported in an abstract.
8. **Three of Piard's 11 aa changes cannot be named** — they are in Supplemental Tables 1–4, **UNAVAILABLE, not empty.** The true distinct-missense denominator is therefore **≥19**, not 19, and the 2025 registry's 25 novel variants are unnamed by their source.
9. **The at-risk fraction cannot be validly transferred onto the census's 25** (§ 3.3). Every figure in § 4.2 and § 4.3 is a declared default.
10. **The provenance of "up to 10 %" could not be closed.** Piard's reference list is absent from the extraction; the candidate source identified by web search is **unverified against it** and must not be recorded as Piard's citation.
11. **No figure image was inspected** (D-14), and no supplementary table was read.
12. **Boundary distance is a weak predictor and is not a mechanism.** ESE/ESS disruption and cryptic-site creation occur deep inside exons; Piard names both. **A LOW rating in § 2 means "not junction-adjacent and never tested", not "safe".**
13. **Nothing here re-ranks `TX-001`–`TX-007`, edits the class census, or proposes a therapy.** Nothing here is a genotype–phenotype prognosis for any individual, and nothing here is medical advice.

---

## 8 · INFORMATION GAIN

| Axis | Verdict | One line |
|---|---|---|
| **Mechanistic graph** | **NO** | No new mechanism, partner, pathway or causal edge. The splice-versus-missense mechanism question was already open; this file measures how open it is. |
| **Therapeutic hypothesis** | **NO** | Explicitly out of scope. No strategy proposed, none re-ranked, no allele promoted. |
| **Experimental roadmap** | **YES** | Three costed tiers, a priority order over named alleles, the tissue corrected from leukocyte to LCL on LEGEND's own GTEx ranking, and the crisp answer that the census's banked-RNA assay is **the same method on different samples** — so it is two recruitments, not one, but only a few extra tubes at the margin. |
| **Genotype stratification** | **YES** | First **positional** stratification of the WWOX missense set in this repository: a 9-exon cDNA map anchored to published verbatim coordinates (8 of 9 boundaries), per-allele boundary distances, and the finding that `p.(Gly137Glu)` is the first nucleotide of exon 5 while `p.(Gln230Pro)` — the largest allele-specific constituency in the disease — is 66–84 nt from any junction. |
| **Intervention ranking** | **YES — as an input, not as a decision** | Converts a named threat to PROTEIN-RESCUE from an adjective into a bounded range (19 %–28 % of alleles; 3–6 of 44 individuals) and shows the threat is **second-order** to the abundance-versus-function problem the class already carries. The ranking decision stays with the Orchestrator and the Operator. |
| **Uncertainty** | **YES** | Separates NONE / IN-SILICO / MEASURED and adds a third column for abundance readouts that are not splice assessments; rules the 10 % figure an **imported, uncloseable** premise; bounds the one measured negative four ways using LEGEND's own demoted-tissue record; and marks two alleles **UNDETERMINED** rather than rating them on an exon boundary that does not exist in the repository. |

---

## 9 · DEFAULTS_TAKEN

1. **No new full text was read.** The one-text budget was not spent, because the only candidate that would have changed a count (PMID 39039877, six novel missense alleles) is a Chinese-language journal with no PMC handle in LEGEND's records, and the other candidates are splice papers or documented-unrecoverable.
2. **The exon map is derived, and the derivation is shown rather than asserted** (§ 1.4). Three boundaries are anchored to published verbatim coordinates in artefacts on disk; five more follow arithmetically from the HGVS of canonical ±1/±2 splice alleles already inventoried by LEGEND; **the ninth is declared UNKNOWN and bracketed, not guessed.**
3. **Distance convention:** coding-sequence nucleotides, 1-based, terminal exonic nucleotide = 1. Exon 1's 5′ end and exon 9's 3′ end are **not** treated as junctions.
4. **c. positions for protein-only alleles are derived** from the codon span and, where the substitution has a unique single-nucleotide route, from the forced codon position. Marked `‡` throughout. Validated against nine published c./p. pairs. Ambiguous routes get a codon span only.
5. **The at-risk threshold is "within ~3 nt of a junction, or predictor-flagged", exactly as briefed.** `p.(Ile136Val)` at −4 is rated HIGH on the second criterion (its own paper's untested prediction), not the first.
6. 🔴 **§ 4.2 and § 4.3 transfer a fraction computed over 19 distinct variants onto 25 unnamed allele copies in a different cohort.** That transfer is **not licensed by any source**; it is done to produce a range rather than a silence, and it is flagged here, in § 3.3 and in NEGATIVE RESULTS 9.
7. **Individual-level propagation (§ 4.3) assumes allele independence** within a person. It is illustrative, not a count.
8. **Abundance readouts are never counted as splice assessments** (§ 1.3), which is why `p.(Gln230Pro)` is scored NONE despite having a reported qRT-PCR.
9. **SCAR12 alleles are counted in the 19 but kept in their own sub-table**, because they are the same gene and the same question but a different phenotype pole.
10. **The 10 % source attribution is recorded as an unverified CANDIDATE** and is excluded from every count and every ruling that does not explicitly name it as unverified.
11. **Two web searches were run** (provenance of the 10 % figure only). **No paper was fetched, no artefact was created, no PubMed full text was retrieved.**
12. **All 20 verbatim quotations were re-matched programmatically** against their artefacts under whitespace-and-dash normalisation: **20 of 20 matched, 0 misses.**
13. **No receipt was written, no ledger appended, no canonical file modified, no commit candidate created, and the therapeutic-class census was not edited.** This file is non-canonical analysis.

---

*Bibliographic data and full text from **PubMed / PubMed Central**. Principal DOIs: [10.1038/s41436-018-0339-3](https://doi.org/10.1038/s41436-018-0339-3) · [10.7759/cureus.25003](https://doi.org/10.7759/cureus.25003) · [10.1186/s12920-023-01731-4](https://doi.org/10.1186/s12920-023-01731-4) · [10.1002/mgg3.2500](https://doi.org/10.1002/mgg3.2500) · [10.3390/cells10040824](https://doi.org/10.3390/cells10040824) · [10.1007/s10048-018-0549-5](https://doi.org/10.1007/s10048-018-0549-5) · [10.1212/WNL.0000000000213883](https://doi.org/10.1212/WNL.0000000000213883) · [10.1093/brain/awt338](https://doi.org/10.1093/brain/awt338). Candidate (unverified) source of the 10 % figure: [10.1038/ng.3837](https://doi.org/10.1038/ng.3837).*

🔴 **Classification for research planning. Not treatment advice, not a recommendation, not a statement about any individual. Therapeutic output from this system supports discussion with a treating clinical team; it never substitutes for one.**
