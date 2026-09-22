# What the field has MEASURED about WWOX splice-allele transcripts — a stress-test of the prior census, and the exon arithmetic done from a named source

**VERDICT — `PREMISE: NOBODY_LOOKED` survives, and I can now say it with harder numbers. Across the whole published WWOX literature there are still exactly THREE instances in which a *cis* splice-site allele was put in front of an RNA method, and only one of them is readable here. But the arithmetic underneath the axis was wrong in one place and unresolved in another: exon 7 — the exon whose acceptor is destroyed in a five-patient cohort — is the ONE internal exon whose skipping is IN-FRAME, and the repository's "cryptic +8 ⇒ frameshift" call for the reference genotype's own allele rests on an unstated coordinate convention whose two readings give OPPOSITE frame outcomes. Neither is a measurement. Both change what the experiment must be able to see.**

Scientist E · 2026-09-22 · READ-ONLY toward every canonical file. No registry, ledger, queue, receipt or state manifest was touched. No git operation. Not medical advice.

Bibliographic records and full texts in this document were **retrieved from PubMed / PubMed Central**. DOIs are linked at first citation.

---

## § 0 · What the repository ALREADY held — read before anything was searched

The brief required this section first. Everything below was read in the repository before a single external query was issued, and none of it is re-reported as new.

| Artefact | What it already contains |
|---|---|
| `analysis/wwox_splice_transcript_census_20260921.md` (Scientist B, 2026-09-21) | The census proper: **20 splice-relevant records**, of which **3 measured** a transcript from a *cis* splice-affecting allele (PMIDs 39101447, 38407561, 30853297), **1 boundary case** (22071891, genomic deletion of exons 6–8), **2 annotated-only** (42721537, 21983861), **14 context** (oncology / *trans*-acting). One full read: PMID 39101447, a HEK293T minigene of exons 1–3 showing **exon 2 skipping** from `c.172+1G>C`, with **no NMD block, no quantification, no protein, no correction arm**. Instrument checks (`thegene` ×9), the informative roman-type zeros, the D-14 figure abstention, and the abstract-vs-Discussion mood upgrade on vigabatrin. Four verbatim queries and their counts. The retrievability asymmetry: `is_open_access` carried no information in either direction; only the fetch did. |
| `analysis/tx001_public_rna_data_feasibility_20260921.md` (Scientist A) | That public data cannot answer this. `GSE156243` is **WT n=2 vs engineered KO n=4** and contains **zero molecules** of any splice-allele transcript; the WSM patient line appears in that paper only in Wnt qPCR. The 2021 chemistry (KAPA stranded, poly-A, 75 bp SE). No accession establishable for the 2026 *Brain* paper. The allele boundary on `DL-MOL-011`. The **exon 6 = 89 nt** figure and its derivation by acceptor-to-acceptor arithmetic from Battaglia's variant list, with the explicit declaration that **RefSeq `NM_016373.4` could not be consulted**. Corrections C-1 (PAPER 025 is Weisz-Hubshman, not Piard), C-2 (`c.517-2A>G` is exon 6, `c.1057-2A>G` is exon 9 — opposite NMD regimes), C-3, C-4. |
| `research/tx001_experiment_decision_packet_20260921.md` (Orchestrator) | The whole experiment: donor fibroblasts/LCL, four controls including an endogenous NMD-sensitive positive control, exon-8-forward / exon-9-reverse junction amplicon, **exon 4–6 "core" normaliser**, ±cycloheximide with vehicle twins, capillary electrophoresis + junction qPCR + **Sanger of every band**, escalation to long-read, n≥3, blinded quantification. The Schirmer template (`PMID 26857392`, exon 8→9 vs core, ratio ~67 %, r=0.68). Intron 8 given as **778,856 bp**, retention declared undetectable with that primer pair. §F's four residual unknowns. |
| `research/full_text_queue_current.md` → **FT-110** | `42721537` (`c.107+1G>A`, five patients, no PMCID) and `38902482`, both declared **debt, not reading**. The ten-patients-across-two-canonical-alleles argument. |
| `research/full_text_queue_current.md` → **FT-122** | Oliver 2023 `TABLE S1` — the survival-stratification supplement. **Unrelated to the splice axis**; it concerns `CLAIM 033` and the `Q230P` denominator, not transcripts. Recorded here only so the brief's pointer is answered. |
| `research/discovery_ledger_current.md` → **DL-BIO-002** | The reference genotype's acceptor allele `c.1057-2A>G`, chr16:79211606 A>G, SpliceAI **DS_AL 0.96**, cryptic **acceptor gain DS_AG 0.64 at +8**, MaxEntScan 7.28→−0.67 (Δ−7.95), ClinVar **VUS**. Status `in-silico done (wet open)`. Proposed assay: RT-PCR on donor fibroblasts ± emetine/cycloheximide. |
| `research/discovery_ledger_current.md` → **DL-BIO-003** | The Schirmer exon 8–9 vs exon 4–6 assay as a ready template; alternative transcripts terminating inside intron 8; the caveat that Schirmer measured **expression, not aberrant splicing**. |
| `research/discovery_ledger_current.md` → **DL-MECH-045** | WWOX has nine exons; exon 9 is the last; `c.1057` = codon 353; exon 9 encodes the last ~62 aa; therefore **NMD-escape** and a truncated unstable protein rather than a silent null; the *lde* rat corroboration (`c.1190_1202del`, mRNA present, 46.2 kDa band barely detectable). Belief: high on premises, **medium on the splicing outcome, "which nobody has measured in the reference genotype."** |
| `research/discovery_ledger_current.md` → **DL-MOL-011** | An SSO cannot rebuild a destroyed invariant AG; U1 snRNA corrects donors not acceptors; ADAR runs the wrong direction; a cytosine base editor on the antisense (or prime editing) is the mechanistically valid lever. **Parked pending external verification; `TX-001` not demoted.** |
| `registries/paper_registry_current.md` → **PAPER 044** | PMID 30362252 / PMC6296882 (Davids 2018, *Hum Mutat*) is **already held and already read**, with the transferable finding quoted, the 46 kDa / 19 kDa western detail, and the note that its triple assay is *"il template pronto"* for the acceptor allele. |
| `analysis/data/WWOX_clinvar_all_variants.csv` | **1,327 ClinVar records** on `NM_016373.4` with `NC_000016.10` SPDI coordinates. Present in the repository since 2026-09-18 and, as far as I can tell, never used to derive exon boundaries. |

**The delta this document adds is in § 1.2, § 2, § 3.2, § 3.3 and § 5.** Everything else is confirmation.

---

## § 1 · The measurement census — verified, and the number it should be

### 1.1 · Independent verification of "three"

Query 1 of the prior census was re-run verbatim today and returned the **identical 19 PMIDs**, in the same order. The census's Q1 is reproducible and its splice-relevant set is stable.

I then ran eight queries the prior census did not run (§ 5.1). **None of them surfaced a fourth measurement on a *cis* splice-site allele.** The number is **3**. I can neither raise it nor lower it.

| # | PMID | Allele (exact HGVS, as the source writes it) | Site class | Method | Cells / construct | What was measured | Verbatim result | Status | Depth here |
|---|---|---|---|---|---|---|---|---|---|
| **M-1** | **39101447** | `c.172+1G>C` | canonical **donor**, intron 2 | minigene + RT-PCR + Sanger | HEK293T, exons 1–3, intron 1 artificially shortened | the spliced product of a plasmid | *"the c.172+1G>C substitution of<sub>[WWOX]</sub> caused a splicing abnormality, which abrogated the intron 2 canonical splice site and led to a loss of exon 2"* | **MEASURED** | 🟢 **full-text** (prior session; artefact fingerprinted) [DOI](https://doi.org/10.1002/mgg3.2500) |
| **M-2** | **38407561** | `NM_016373.4:c.516+1G>A` | canonical **donor**, intron 5 | *"WWOX mRNA sequencing"* | **patient peripheral-blood RNA** | a patient transcript | abstract reports exon 5 deleted | **MEASURED (reported)** | 🔴 **abstract-depth.** `pmc_id: null` re-confirmed today; no fetch target exists [DOI](https://doi.org/10.1002/ajmg.a.63575) |
| **M-3** ⭐ | **30853297** | `c.517-2A > G` (the source spaces the `>`) | canonical **ACCEPTOR**, intron 5 → exon 6 | *"Complementary DNA sequencing"* | patient material, tissue unstated in abstract | a patient transcript | *"Complementary DNA sequencing demonstrated that the WWOX c.517-2A > G splice-site variant causes skipping of exon six."* | **MEASURED (reported)** | 🔴 **abstract-depth.** `pmc_id: null` re-confirmed today [DOI](https://doi.org/10.1016/j.ejpn.2019.02.003) |

**M-3 remains the only measurement of any kind on a canonical acceptor allele, and it is still unreadable here.** Both PubMed and the copyright tool agree there is no PMC handle.

### 1.2 🔴 The boundary cases — the census counts one; there are two, and the second is open, read, and the closest thing to the experiment TX-001 needs

| # | PMID | Lesion | Method | Cells | What was measured | Status | Depth |
|---|---|---|---|---|---|---|---|
| **B-1** | 22071891 | genomic deletion of exons 6–8 | cDNA analysis | patient | *"exon 5 being spliced directly onto exon 9"* | MEASURED (reported) | abstract-depth; PMC3283189 returned a **zero-length body** when tested |
| **B-2** ⭐ | **30362252** | **22 kb genomic microdeletion of exon 6**, homozygous via maternal UPD16 | **four junction-specific qPCR assays + isoform-resolved western + ddPCR** | **patient cultured fibroblasts** | transcript junctions AND protein isoforms | MEASURED | 🟢 **full-text retrieved and re-read today** [DOI](https://doi.org/10.1002/humu.23675) |

**B-2 is already in the repository as `PAPER 044` and is not a discovery.** What *is* new is where it sits: **it is absent from the splice census entirely.** It appears in none of the census's four tables, and therefore in none of its totals. The reason is mechanical and worth recording as an instrument finding: **PMID 30362252's title and abstract contain no splice word**, so `WWOX AND (splicing OR "splice site" OR "exon skipping")` cannot return it — and it does not. The census's denominators are complete *for its queries* and incomplete relative to the repository's own registry.

**What B-2 actually measured, verbatim from the body retrieved today:**

> *"Since there are three distinct transcripts for<sub>[WWOX]</sub>(), mRNA expression levels were analyzed with four different assays, covering exon 1–2, exon 5–6 and exon 7–8 junctions of transcript, and exon 5–6 junction of transcript(exon 5–6\*), respectively ()."*

> *"As expected, the assay spanning the deleted exon 6 was not detected in the proband. The exon 1–2 junction, however, was detected and was only slightly reduced in our patient, whereas the exon 7–8 junction was barely detectable, suggesting that the two longer transcripts were not expressed or were degraded."*

> *"Protein expression analysis (and) also showed the loss of the longer isoform (/), which contains the short-chain dehydrogenase/reductase domain, and the increased expression of the shorter isoform (/), which only contains the WW-domains."*

🔴 **And here is the correction. The abstract says NMD was demonstrated. The Results section says it was not.**

> Abstract: *"mRNA expression analysis revealed that the deletion led to nonsense-mediated decay of the<sub>[WWOX]</sub> transcript"*
> Results: *"suggesting that the two longer transcripts were not expressed or were degraded."*

*"Not expressed **or** degraded"* is an explicitly undecided disjunction. **No NMD inhibitor was used anywhere in this paper** — see the negative-control ledger in § 5.2. The repository's `PAPER 044` note carries the abstract's indicative — *"qui l'NMD **avviene**"* — and that is one mood stronger than the source's own Results sentence supports. This is the same abstract-vs-body upgrade the prior census caught in PMID 39101447, caught here in a paper the repository already treats as settled.

**The consequence is exact:** the repository's only citable instance of measured NMD in WWOX is **an inference from a qPCR ratio without a translation block**, i.e. it is precisely the ambiguity the ±cycloheximide arm exists to resolve. The census's standing statement — *"no WWOX splice allele has ever been assayed with an NMD inhibitor"* — **survives intact and is now stronger**: no WWOX allele of **any** class has.

⚠️ **Extractor state on this artefact.** The italic-deletion fault is active: `WWOX` is deleted throughout (*"exon 6 of()"*, *"three distinct transcripts for()"*), and **the isoform molecular weights were deleted inside the parentheses** — the body I read says *"the longer isoform (/)"* and *"the shorter isoform (/)"* with the kDa values gone. Only `33kDa` survived. **I therefore could NOT re-verify the 46 kDa / 19 kDa figures the registry holds**; they must come from a prior surface with figures. I record that as unverified-by-me rather than repeating them as read.

### 1.3 · Annotated-only, and the patients behind the annotations

| PMID | Allele | Patients | Status | Retrievable |
|---|---|---|---|---|
| 42721537 | `NM_016373.4:c.107+1G>A` | **5** (proposed founder) | **ANNOTATED ONLY** — NGS + ACMG | `pmc_id: null` re-confirmed today; Elsevier all rights reserved |
| **26345274** | `NM_016373.3:c.606-1G>A` | **5** (two families, shared haplotype) | **ANNOTATED ONLY** — whole-exome; the abstract describes no RNA work | `pmc_id: null` re-confirmed today [DOI](https://doi.org/10.1002/ajmg.a.37363) |
| 21983861 | intron 6 splice site `+1 G-A`, breast tumour DNA | — | ANNOTATED ONLY — genomic sequencing | not tested |

**FT-110 is partly resolvable and I resolve it here.** Its second PMID, `38902482`, is **not a splice paper at all** — metadata retrieved today shows it is *"Molecular Mechanism of WWOX Inhibiting the Development of Esophageal Cancer by Inhibiting Hippo Signaling Pathway"* (Chen Z *et al.*, Xuzhou, *Biochem Genet* 2024) [DOI](https://doi.org/10.1007/s10528-024-10856-9), an ESCC cell-line study with RT-qPCR of WWOX expression and no variant transcript work. **FT-110's reading debt on `38902482` can be closed as not-applicable.** Its debt on `42721537` stands, and so does its argument, which I confirm: **ten patients across two canonical alleles whose RNA nobody has examined.**

### 1.4 · Final census arithmetic

- Measurements on a *cis* **splice-site** allele: **3** (M-1, M-2, M-3). **Unchanged. Independently verified.**
- Of those, on a **canonical acceptor** — the reference genotype's class: **1** (M-3), abstract-depth, unreachable.
- Measurements of a WWOX transcript from a **transcript-destroying lesion of any kind**: **5** (M-1..M-3 + B-1 + B-2). The prior census counted 4; **B-2 raises the boundary count from 1 to 2** and is the only one with patient cells, isoform-resolved protein, and a full text I can read.
- Papers using an **NMD inhibitor** on any WWOX allele: **0**.
- Papers reporting an **aberrant:normal ratio** for any WWOX allele: **0**.
- Papers with an **ASO / splice-switching / correction arm** in WWOX: **0**.
- Papers applying **long-read or nanopore** sequencing to WWOX: **0**.
- PubMed records for the reference genotype's own allele `c.1057-2A>G`: **0**. ClinVar holds it as **VUS** with no supporting publication.

---

## § 2 · 🔴 The arithmetic — from a named source, checked, and wrong in one place

### 2.1 · Source and method, stated before the numbers

The prior work derived exon 6 = 89 nt by reading HGVS boundary markers out of a published variant list and declared, honestly, that **RefSeq `NM_016373.4` exon coordinates could not be consulted** in this environment. That is still true of direct egress: `rest.ensembl.org`, `eutils.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov` and `www.ebi.ac.uk` all return **403 at CONNECT** through the agent proxy (verified today; the proxy's own `recentRelayFailures` log records these denials). **I did not reach a sequence database and I do not claim to have.**

I used a different named source that is already inside the repository:

> **`disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv`** — 1,327 ClinVar records, each carrying an HGVS expression on transcript **`NM_016373.4`** and an SPDI genomic expression on assembly **`NC_000016.10`** (GRCh38).

The derivation is mechanical: for a purely exonic SNV, `genomic − cDNA` is constant within an exon and jumps at every exon boundary. Its reliability is not assumed, it is measured:

- **729** exonic SNVs parsed. They fall into **exactly 9 distinct offsets** — no outliers, no tenth group. This independently reproduces *"WWOX contains nine exons"* (Shaukat 2018, PMID 30361190) from coordinate data alone.
- **729 / 729** reference-base concordance between the cDNA HGVS reference allele and the SPDI genomic reference allele ⇒ **WWOX is transcribed from the plus strand** of chr16. Not assumed; measured.
- **191** intronic variants give boundary markers (`c.N+x` fixes an exon end at `c.N`; `c.N−x` fixes an exon start at `c.N`). **Every one of the eight boundaries implied by the offset jumps is confirmed by at least 9 independent intronic records, with zero contradictions.**

⚠️ **What this is and is not.** It is ClinVar's transcript annotation, read as data. It is **not** a direct read of the RefSeq exon table, and if ClinVar's own `NM_016373.4` mapping were wrong the error would propagate. Given 729 concordant records and 191 concordant boundary markers, I treat it as a source of record and say so, rather than treating it as proof.

### 2.2 · The exon table

Transcript **`NM_016373.4`**, assembly **`NC_000016.10`** (GRCh38), plus strand. Lengths are **coding** nucleotides; exon 1 additionally carries ≥460 nt of 5′UTR and exon 9 ≥385 nt of 3′UTR (both established from UTR variants in the same file, sharing the same offsets).

| Exon | cDNA span | Coding nt | `mod 3` | Skip ⇒ frame | Genomic (1-based) | Flanking splice alleles in ClinVar |
|---|---|---|---|---|---|---|
| 1 | c.1–c.107 | 107 | 2 | n/a — carries the ATG | 78,099,779–78,099,885 | donor `c.107+1G>A` (**5 patients**, PMID 42721537), `c.107+1G>C`, `c.107+2T>G` |
| 2 | c.108–c.172 | 65 | **2** | **FRAMESHIFT** | 78,108,423–78,108,487 | acceptor `c.108-2A>T`; donor `c.172+1G>C` (**M-1, measured**), `c.172+2T>G` |
| 3 | c.173–c.230 | 58 | **1** | **FRAMESHIFT** | 78,109,778–78,109,835 | acceptor `c.173-1G>C`, `c.173-1G>T` |
| 4 | c.231–c.409 | 179 | **2** | **FRAMESHIFT** | 78,114,976–78,115,154 | acceptor `c.231-1G>C`; donor `c.409+1G>C`, `c.409+1G>T`, `c.409+2T>C` |
| 5 | c.410–c.516 | 107 | **2** | **FRAMESHIFT** | 78,164,183–78,164,289 | acceptor `c.410-1G>A`, `c.410-2A>G`; donor `c.516+1G>A` (**M-2, measured**) |
| 6 | c.517–c.605 | **89** | **2** | **FRAMESHIFT** | 78,386,860–78,386,948 | acceptor `c.517-1G>T`, **`c.517-2A>G` (M-3, measured)**; donor `c.605+2T>C`, `c.605+5G>A` |
| **7** | **c.606–c.791** | **186** | **0** | 🔴 **IN-FRAME** | 78,424,870–78,425,055 | acceptor **`c.606-1G>A` (5 patients, PMID 26345274)**; donor `c.791+1G>A/C/T` |
| 8 | c.792–c.1056 | 265 | **1** | **FRAMESHIFT** | 78,432,488–78,432,752 | — (no ±1/±2 record) |
| 9 | c.1057–c.1245 | 189 | 0 | **last exon — see § 2.4** | 79,211,608–79,211,796 | acceptor **`c.1057-2A>G` (reference genotype, VUS)**, `c.1057-3C>T` |

**Introns**, from the same map — relevant because retention is only detectable for short ones:

| Intron | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| nt | 8,537 | 1,290 | 5,140 | 49,028 | 222,570 | 37,921 | 7,432 | **778,855** |

### 2.3 · The repository's working figures, adjudicated

| Repository figure | Verdict | Evidence |
|---|---|---|
| **Exon 6 is 89 nt; `89 mod 3 = 2`; skipping is frameshifting** | ✅ **CONFIRMED** | c.517–c.605 inclusive = 89. Boundaries fixed by 39 acceptor records at `c.517−` and 21 donor records at `c.605+`. Scientist A's Battaglia-list arithmetic was right. |
| **`c.1057` is codon 353** | ✅ **CONFIRMED** | 3 × 352 = 1056, so c.1057 is base 1 of codon 353. |
| **Exon 9 encodes the last ~62 amino acids** | ✅ **CONFIRMED, exactly 62** | 189 coding nt = 63 codons, of which one is the stop; 414 − 352 = 62. |
| **WWOX has nine exons; exon 9 is the last** | ✅ **CONFIRMED** independently | Exactly 9 offset classes across 729 exonic variants; all 3′UTR variants (to c.\*385) share exon 9's offset. |
| **`c.1057-2A>G` = chr16:79,211,606** | ✅ **CONFIRMED** | Exon 9 begins at 79,211,608; −2 ⇒ 79,211,606. `DL-BIO-002`'s coordinate is right. |
| **`c.517-2A>G` (exon 6) and `c.1057-2A>G` (exon 9) sit in opposite NMD regimes** | ✅ **CONFIRMED** | Exon 6 is internal with two downstream junctions; exon 9 is terminal. Correction C-2 holds. |
| **Intron 8 is 778,856 bp** | ⚠️ **778,855 on GRCh38 by this derivation** — a 1-nt difference | The repository's figure comes from Schirmer 2016, plausibly GRCh37 or a different interval convention. **Biologically inconsequential**; recorded so the number is not silently inherited as exact. |
| **Q230P (`c.689A>C`) lies in exon 7** | ✅ **CONFIRMED** | c.689 ∈ c.606–c.791. |

### 2.4 🔴 The new arithmetic finding — exon 7 is the one internal exon that is in-frame

**Exon 7 is 186 nt. `186 mod 3 = 0`.** It opens at phase 2 (c.606 completes codon 202, since 3 × 201 = 603) and closes at phase 2 (c.791 is base 2 of codon 264, since 3 × 263 = 789). **A symmetric-phase exon: skipping it is a clean in-frame event.**

The skipped junction joins `c.605` to `c.792`, reconstituting codon 202 from c.604 + c.605 + c.792 and deleting **62 codons' worth of sequence**. Predicted product: a **352-residue internally deleted WWOX**, not a truncation. **No premature stop codon is created, so NMD is not invoked at all** — the transcript is predicted stable and translated.

🔴 **Why this matters more than a tidy number.** The acceptor of exon 7 is `c.606-1G>A` — the allele carried homozygously by the **five patients of PMID 26345274**, all of whom died before their third birthday. The repository currently reasons about WWOX splice alleles under a uniform "aberrant transcript → PTC → NMD *or* truncated protein" frame. **For this allele, if the outcome is exon skipping, neither branch applies.** The predicted product is an internally deleted protein carrying a 62-residue excision from inside the SDR domain — and the region excised **contains codon 230**, the repository's exemplar missense position. Whether such a protein is inert, unstable, or actively harmful is the same open safety question `DL-MECH-045` raises for the truncated product, and it is unmeasured.

⚠️ **Hedges, stated as hedges.** (a) Loss of a canonical acceptor does not compel exon skipping — intron retention, a cryptic acceptor, or use of an alternative terminal exon are all available, and for exon 7 intron 6 is 37,921 nt and intron 7 is 7,432 nt, so retention of either would be a long, likely non-productive species. (b) **Nobody has measured what `c.606-1G>A` does.** This is arithmetic plus a splicing rule, tagged `PREDICTED` throughout, and it is exactly the kind of statement that must not be voiced in the indicative.

### 2.5 · NMD expectation, per allele

The 50–55 nt rule: a PTC triggers NMD only when it lies upstream of the final exon–exon junction.

| Allele | If the exon is skipped | Frame | PTC position | NMD expected? |
|---|---|---|---|---|
| `c.107+1G>A` (5 pts) | exon 1 lost — no ATG | n/a | — | **Not applicable.** A lesion at the exon 1 donor is not an exon-skip problem; translation initiation itself is at issue. `PREDICTED`, and the least analysable of the set |
| `c.172+1G>C` (**measured**, M-1) | exon 2 lost, 65 nt | frameshift | far upstream of the exon 8/9 junction | **YES, predicted** — and the minigene that measured it spanned exons 1–3, so it was structurally blind to NMD |
| `c.173-1G>C/T` | exon 3 lost, 58 nt | frameshift | upstream | **YES, predicted** |
| `c.231-1G>C`, `c.409+1G>C/T` | exon 4 lost, 179 nt | frameshift | upstream | **YES, predicted** |
| `c.410-1G>A`, `c.410-2A>G`, `c.516+1G>A` (**measured**, M-2) | exon 5 lost, 107 nt | frameshift | upstream | **YES, predicted** |
| `c.517-1G>T`, `c.517-2A>G` (**measured**, M-3) | exon 6 lost, 89 nt | frameshift from codon 173 | upstream | **YES, predicted** — and M-3 nevertheless **sequenced the skipped product**, so NMD is demonstrably **not absolute** for this allele. Degraded fraction: unknown |
| 🔴 **`c.606-1G>A` (5 pts)** | exon 7 lost, 186 nt | **IN-FRAME** | **none created** | 🔴 **NO — NMD not expected at all.** Predicted stable, translated, internally deleted protein |
| `c.791+1G>A/C/T` | exon 7 lost | in-frame, same as above | none | **NO** |
| 🔴 **`c.1057-2A>G` (reference genotype)** | **exon 9 cannot be "skipped"** — § 2.6 | see § 2.6 | in the last exon or in intron 8 read-through | **NO — NMD-escape predicted.** `DL-MECH-045` is right for the right reason |

### 2.6 🔴 "Exon 9 skipping" is not a defined outcome, and the cryptic-site frame call is unresolved

**Two separate points about the reference genotype's own allele, both arithmetic, neither a measurement.**

**(a) There is no exon 10.** Exon 8's donor has nothing downstream to ligate to once the exon 9 acceptor is destroyed. `DL-MECH-045` lists *"skipping dell'ultimo esone"* among the plausible outcomes, and the repository elsewhere correctly notes that skipping exon 9 would lose the stop codon as well as the C-terminus. Sharpening it: **the outcome set for `c.1057-2A>G` is not {skip, retention, cryptic} but {cryptic acceptor, intron 8 read-through/retention, intronic polyadenylation or an alternative terminal exon}** — and Schirmer's documented *"transcripts terminating within intron 8"* means the last of those is not hypothetical in this gene. An assay that only asks "is exon 9 there or not" cannot tell these apart.

**(b) The `+8` cryptic acceptor: two conventions, opposite frames.** `DL-BIO-002` records SpliceAI `DS_AG 0.64` **at +8 nt**; `DL-MECH-045` then writes *"uso del sito criptico +8 (frameshift)"*. The offset is measured from the variant at chr16:79,211,606, and 79,211,606 + 8 = **79,211,614 = c.1063**.

| Reading | New exon starts at | Exonic nt deleted | `mod 3` | Consequence |
|---|---|---|---|---|
| **A** — SpliceAI's standard convention: `DP_AG` is relative to the variant, and the position marks the **first exonic base** of the gained acceptor | **c.1063** | `c.1057_1062` = **6 nt** | **0** | 🔴 **IN-FRAME deletion of codons 353–354.** No PTC. No NMD. A near-full-length WWOX missing two residues — **a hypomorph, not a null** |
| **B** — the offset read as "8 exonic nucleotides lost" | c.1065 | 8 nt | 2 | **Frameshift** from codon 353, PTC in the last exon ⇒ **NMD-escape ⇒ truncated protein**. This is the repository's current position |

**An independent consistency check favours Reading A, and I state its strength honestly.** A cryptic acceptor whose first exonic base is c.1063 requires an `AG` at c.1061/c.1062. Reconstructing exon 9's opening bases from ClinVar reference alleles gives `c.1062 = G` (recorded), with `c.1061` not covered by any ClinVar record. **The +8 offset lands exactly one base 3′ of a reference G** — a 1-in-4 coincidence if the convention were wrong. That is suggestive, not decisive.

🔴 **I do not adjudicate this, and the repository should not either until the raw SpliceAI output is re-read.** The stakes are the whole axis: under Reading A the allele is a hypomorph and `TX-001`'s headroom may be small; under Reading B it is a truncating null-equivalent and the headroom is large. **What settles it is not an argument — it is the `DP_AG` field of the original run, or one re-run.** Logged as the single cheapest open item in this document.

---

## § 3 · Leaky splicing — position, regime, and what has actually been measured

### 3.1 · The regime distinction, stated once

The 3′ splice site ends in an **invariant `AG` dinucleotide** at positions −2/−1, recognised by U2AF35. A change at **−1 or −2 destroys that dinucleotide**; a change at **−3 leaves it intact** and perturbs only the pyrimidine-tract/consensus context. These are different biological regimes, and the distinction is the whole of this section.

### 3.2 · Every WWOX acceptor allele at −1 to −3, from ClinVar

**All 14 are in the repository's own ClinVar file.**

| Position | Allele | Exon opened | Exon nt (`mod 3`) | ClinVar classification | Invariant AG | Residual canonical splicing **possible in principle**? |
|---|---|---|---|---|---|---|
| **−1** | `c.173-1G>C` | 3 | 58 (1) | Pathogenic | **destroyed** | **No** |
| **−1** | `c.173-1G>T` | 3 | 58 (1) | Pathogenic | **destroyed** | **No** |
| **−1** | `c.231-1G>C` | 4 | 179 (2) | Pathogenic | **destroyed** | **No** |
| **−1** | `c.410-1G>A` | 5 | 107 (2) | Pathogenic/Likely pathogenic | **destroyed** | **No** |
| **−1** | `c.517-1G>T` | 6 | 89 (2) | Pathogenic | **destroyed** | **No** |
| **−1** | 🔴 `c.606-1G>A` (**5 patients**) | **7** | **186 (0) — in-frame** | Pathogenic | **destroyed** | **No** |
| **−2** | `c.108-2A>T` | 2 | 65 (2) | Likely pathogenic | **destroyed** | **No** |
| **−2** | `c.410-2A>G` | 5 | 107 (2) | Likely pathogenic | **destroyed** | **No** |
| **−2** | `c.517-2A>G` (**M-3**) | 6 | 89 (2) | Pathogenic | **destroyed** | **No** |
| **−2** | 🔴 `c.1057-2A>G` (**reference genotype**) | **9 (last)** | 189 (0) | **Uncertain significance** | **destroyed** | **No** |
| **−3** | `c.108-3C>T` | 2 | 65 (2) | Uncertain significance | **intact** | **YES — partial/leaky use of the canonical site is mechanistically available** |
| **−3** | `c.231-3C>A` | 4 | 179 (2) | Uncertain significance | **intact** | **YES** |
| **−3** | `c.410-3T>C` | 5 | 107 (2) | Conflicting classifications | **intact** | **YES** |
| **−3** | 🔴 `c.1057-3C>T` | **9** | 189 (0) | Uncertain significance | **intact** | **YES** |

**Two things fall straight out of this table.**

🔴 **First, Correction C-2 of the feasibility file needs amending on one clause.** It states *"No `−3` neighbour variant exists in LEGEND for either."* **`c.1057-3C>T` is the −3 neighbour of the reference genotype's own acceptor allele**, and it is sitting in `disease-models/wwox/analysis/data/WWOX_clinvar_all_variants.csv`, inside the repository, classified **Uncertain significance**. So is `c.410-3T>C` at the exon 5 acceptor. The substantive half of C-2 — that `c.517-2A>G` and `c.1057-2A>G` are different acceptors in opposite NMD regimes — is correct and confirmed in § 2.3.

**Second, the classification pattern tracks the regime exactly, and it is a measurable gradient, not an impression.** Of the **10** WWOX acceptor alleles at −1/−2, **9 are Pathogenic or Likely pathogenic** and the tenth is the reference genotype's VUS. Of the **4** at −3, **none** is pathogenic-leaning: three VUS and one Conflicting. **10 vs 0.** ⚠️ This is a census of **classifications**, which are themselves largely annotation-driven — ACMG `PVS1` fires at ±1/±2 and does not at −3 — so the gradient partly measures the classification rule rather than the biology. It is consistent with the regime split; it is not independent evidence for it.

**Local sequence context, reconstructed from ClinVar reference alleles** (`.` = no ClinVar record at that position, so the base is unknown to me):

| Acceptor | −12 … −1 |
|---|---|
| exon 6 (`c.517`) | `C T C T C A T . G . A G` |
| exon 7 (`c.606`) | `. . . A . . . . . . . G` |
| exon 9 (`c.1057`) | `. . G G . T . . C C A .` |

For the reference genotype's allele this says something concrete and bounded: **positions −4 and −3 are `C` and `C`**, so `c.1057-2A>G` does **not** create or expose an `AG` immediately upstream, and the nearest known upstream dinucleotide (−10/−9 = `G,G`) is not one either. ⚠️ Positions −8 to −5 are unknown to me, so I cannot exclude an upstream `AG` there. This is consistent with SpliceAI nominating a **downstream, exonic** cryptic gain rather than an upstream shift — a consistency check on the prediction, not a substitute for it.

### 3.3 · And now the part that must never share a sentence with the above

**Has anyone ever MEASURED residual correctly-spliced transcript from any WWOX acceptor allele?**

> ## **No. Zero. Not once, for any allele, at any position, in any tissue.**

Stated separately and without hedging, because the brief is right that the distinction decides the axis:

- Of the 14 acceptor alleles in § 3.2, **exactly one has ever been put in front of an RNA method at all** — `c.517-2A>G`, by complementary-DNA sequencing (M-3), and that paper is unreadable here. What it reports is the **presence of a skipped species**. It reports **no fraction, no ratio, no residual normal band, and no statement that normal splicing was absent.**
- **None of the four −3 alleles — the ones where leaky splicing is mechanistically available — has ever been assayed.** All four are VUS or Conflicting *precisely because* nobody has looked. They are the cleanest available test of the leaky regime in this gene and they are untouched.
- **No aberrant:normal ratio exists for any WWOX allele of any class.** Confirmed today by three independent negative queries with a passing positive control (§ 5.2). `TX-001`'s efficacy endpoint still has no denominator.
- The single hard fact bearing on leakiness runs *against* totality: **M-3 sequenced the skipped product**, so whatever degradation occurs is incomplete. That tells us the aberrant species survives well enough to be read. It tells us nothing about how much correct product accompanies it.

⚠️ **One inference must not be smuggled in.** "Invariant AG destroyed ⇒ no residual canonical splicing" is a **mechanistic expectation**, and it is the reason the −1/−2 column above reads "No". It has never been tested in WWOX. In other genes, alleles at ±1/±2 occasionally retain a small residual normal fraction through mechanisms the simple rule does not cover. **For the reference genotype, the honest position is: residual correct splicing is expected to be near zero and has never been measured, and those are two different statements.**

---

## § 4 · What one cheap experiment would settle — and what it would not

The decision packet already specifies this experiment well. I add only what the arithmetic above forces to change, and the three defects it would otherwise have walked into.

### 4.1 · The design, with the three corrections the arithmetic forces

**Cells.** Donor-derived fibroblasts or LCL carrying the acceptor allele, plus two unrelated healthy lines. Unchanged, and B-2 now proves the matrix works: Davids measured WWOX junctions and isoform-resolved protein **in patient fibroblasts**.

**Primers — three reactions, not one.**

1. **Junction reaction.** Forward in **exon 8** (c.792–c.1056, 265 nt — ample room), reverse in **exon 9** (c.1057–c.1245 coding, plus ≥385 nt of 3′UTR). Designed so the amplicon spans `c.1056|c.1057`.
2. 🔴 **Cryptic-resolution requirement.** The candidate products differ by **6 or 8 nucleotides** (§ 2.6). **A 6-nt shift is invisible on an agarose gel and marginal on a 2 % gel.** Resolution must be **capillary electrophoresis or fragment analysis**, and **every product must be Sanger-sequenced regardless of whether it looks like one band.** A single band of apparently normal size is *not* evidence of correct splicing here — it is the expected appearance of a 6-nt in-frame cryptic product.
3. 🔴 **Intron 8 reaction, mandatory and separate.** Intron 8 is **778,855 nt**. Read-through, retention and intronic polyadenylation are the outcomes the junction reaction is structurally blind to, and Schirmer documented that transcripts terminating inside intron 8 exist in this gene. Forward in exon 8, reverse anchored **within the first ~200 nt of intron 8**. Without this reaction the assay cannot distinguish "no aberrant product" from "the aberrant product is a species this primer pair cannot amplify."
4. 🔴 **The normaliser must be re-chosen.** The decision packet proposes **exon 4–6 "core"**. B-2 shows why that is unsafe: WWOX has **three transcripts**, and the short isoform `NM_130791.3` **has its own exon 5–6 junction whose expression rose when the long isoform was lost**. An exon 4–6 amplicon therefore measures a **mixture whose composition moves with the lesion** — it is not an inert denominator. **Use an amplicon confined to a region unique to the long transcript** (an exon 7–8 junction assay, as Davids used, or exon 2–3), and **report the isoform composition rather than assuming it**.

**± cycloheximide.** Unchanged and still not optional — with one addition the literature now supplies: **the only NMD claim in the whole WWOX field (B-2) was made without a translation block**, from a qPCR ratio, and its own Results sentence says *"not expressed **or** degraded."* An endogenous NMD-sensitive positive control in the same cells (e.g. a `GAS5` or auto-regulated `SRSF` isoform) is what converts "no change on cycloheximide" from uninterpretable into informative.

**Why cycloheximide is needed even though NMD-escape is predicted.** `DL-MECH-045` predicts escape for `c.1057-2A>G`, and I confirm its premises. **A prediction of escape is a reason to run the arm, not to skip it** — the arm is what turns the prediction into a measurement, and it is the only way to tell an escaped stable transcript from a degraded one when both present as "less product."

**Quantification.** Fragment-analysis peak areas → **aberrant : normal ratio**, the primary endpoint; junction qPCR against a single-isoform normaliser as a continuous second measure; Sanger identity for every species. n ≥ 3 independent RNA extractions per line per condition, technical duplicates, quantification blinded to genotype and condition.

### 4.2 · Band pattern → outcome, pre-specified

| Observed | Interpretation | Frame | NMD |
|---|---|---|---|
| Single product, exon 8→9 junction, sequence = `…c.1056\|c.1057…` | correct splicing | — | — |
| Product **6 nt shorter**, junction `…c.1056\|c.1063…` | 🔴 **cryptic acceptor, Reading A** | **in-frame**, 2 codons lost | none — **hypomorph** |
| Product **8 nt shorter**, junction `…c.1056\|c.1065…` | cryptic acceptor, Reading B | frameshift from codon 353 | **escape** (last exon) → truncated protein |
| Product from the **intron 8 reaction** | read-through / retention / intronic polyA | PTC inside intron 8 | escape or not, depending on position |
| **Both** a normal-junction and an aberrant product in the same lane, quantified | 🔴 **LEAKY SPLICING — the number the axis is missing** | — | — |
| Junction product falls, intron 8 reaction negative, total transcript falls, and cycloheximide **restores** it | degradation | — | **NMD confirmed** — and it would be the first time in this gene |
| Junction product falls, intron 8 reaction negative, and cycloheximide changes **nothing** while the positive control responds | the transcript is not being made | — | not an NMD phenomenon |

### 4.3 · What it would NOT settle

- **Transcript is not protein.** No protein has ever been measured from a WWOX *splice* allele; the only isoform-resolved western in the field (B-2) was on a genomic deletion, and on the surface available to me its molecular weights were deleted by the extractor. A ratio says nothing about what is translated, nor whether an internally deleted or truncated product is inert, unstable or harmful.
- **Fibroblast is not neuron.** Splicing efficiency is tissue-dependent; the disease is neuronal; and `c.1057` sits in an exon adjacent to a 778 kb intron whose processing has every reason to be context-dependent.
- **A ratio is not a rescue**, and it does not choose between ASO and editing. `DL-MOL-011` remains parked and `TX-001` remains undemoted; this measurement is neutral between levers and is a prerequisite for all of them.
- **One donor is not an allele class**, and it says nothing about the missense allele *in trans*.
- **It does not transfer between alleles.** § 2 shows five distinct regimes inside one gene — frameshift+NMD (exons 2–6, 8), in-frame with no PTC (exon 7), and terminal-exon escape (exon 9). **An assay designed for one is mis-specified for another.**

---

## § 5 · Instruments, negatives, and what I could not verify

### 5.1 · Queries run today, verbatim, with counts

| # | Query | Count | Note |
|---|---|---|---|
| Q-A | `WWOX AND (splicing OR "splice site" OR "exon skipping")` | **19** | **Reproduces the prior census's Q1 exactly**, same PMIDs |
| Q-B | `WWOX minigene` | **2** | 39101447, 32669614. **Positive control — returns the known hit** |
| Q-C | `WWOX AND "exon skipping"` | **0** | WWOX term resolved correctly in the translation |
| Q-D | `WWOX AND "nonsense-mediated"` | **1** | **30362252 — the paper the census's queries could not see** |
| Q-E | `WWOX AND (antisense oligonucleotide OR "splice-switching")` | **0** | Term expanded to the full MeSH tree; **no ASO literature exists in this gene** |
| Q-F | `WWOX AND (cycloheximide OR emetine OR puromycin)` | **0** | ⚠️ title/abstract/MeSH only — PubMed does not index full text |
| Q-F′ | `CFTR AND cycloheximide` | **24** | **Positive control for Q-F — the field terms are indexed and findable** |
| Q-G | `WWOX AND (RT-PCR OR "cDNA sequencing") AND (splice OR splicing)` | **2** | 15870886, 11896615 — both oncology, already in the census |
| Q-H | `WWOX AND (nanopore OR "long-read" OR "long read")` | **0** | |
| Q-I | `WWOX AND (WOREE OR "DEE28" OR "EIEE28" OR SCAR12)` | **30** | |
| Q-J | Q-I `AND (RNA OR mRNA OR transcript OR cDNA OR splicing)` | **9** | All checked; no new measurement |
| Q-K | `WWOX AND (variant OR mutation) AND (transcript OR mRNA) AND (fibroblast OR blood OR lymphocyte)` | **18** | All checked; no new measurement |
| Q-L | `WWOX AND "c.517-2A>G"` | **1** | 30853297. **Positive control — HGVS phrase search works** |
| Q-M | `WWOX AND "c.516+1G>A"` | **1** | 38407561. Second positive control |
| Q-N | `WWOX AND "c.1057-2A>G"` | **0** | See 5.3 |
| Q-O | `WWOX AND "c.606-1G>A"` | **0** | 🔴 **FALSE ZERO — see 5.3** |
| Q-O′ | `WWOX AND "606-1G"` | **1** | **26345274.** The same string, reachable, proving Q-O's zero was an instrument failure |

### 5.2 · Retrievability tests actually performed

- `get_copyright_status` on `["30362252","26345274","30853297","38407561","42721537"]` — one batch, used as the pre-test. All five returned `is_open_access: false`; **four returned `pmc_id: null`**, so for those four no fetch target exists and **I did not attempt a transfer and do not claim to have tested them**.
- `get_full_text_article(pmc_ids=["PMC6296882"])` → **non-empty body, full article returned and read.** `is_open_access: false` was wrong about retrievability for the second time in this repository's record. **The flag still carries no information; only the fetch does.**
- No other fetch was attempted, because no other PMC handle existed.
- `files/fulltext/` **does not exist in this environment**, so the PMC6296882 body could not be persisted beside the repository's other artefacts. The passage-level excerpt I worked from is at `/tmp/claude-0/-home-user-legend-development/979a64a0-164e-56a4-849f-0d1692e54c42/scratchpad/PMID30362252_PMC_MCPtext.txt` (1,422 bytes). **No read receipt is claimed and the ledger was not touched.**

### 5.3 🔴 Two instrument defects, both demonstrated rather than asserted

**(a) The PubMed search tool produced a verifiable false zero.** `WWOX AND "c.606-1G>A"` returned **0 results, with `query_translation` echoing the raw string unprocessed** — the `WWOX` term was not even expanded, which it is in every other query in this table. Minutes earlier I had retrieved PMID 26345274's abstract, which contains `NM_016373.3:c.606-1G>A` in running text. Re-querying as `WWOX AND "606-1G"` returned that PMID immediately. **A zero accompanied by an unexpanded `query_translation` is a parser failure, not a result.** Rule for this repository: **read the `query_translation` field before believing any zero.**

**(b) The `c.1057-2A>G` zero is of a different and more trustworthy kind.** Its translation reads `("wwox"…) AND ("c 1057 2a"[All Fields] AND "g"[All Fields])` — PubMed **decomposed** the phrase, which is what it does when the exact phrase is not in its index, whereas it **preserved** `"c.517-2A>G"[All Fields]` and `"c.516+1G>A"[All Fields]` for the two alleles that are. **The decomposition is itself evidence that the string is absent from PubMed.** Combined with ClinVar holding the allele as a VUS with no supporting publication: **the reference genotype's own acceptor allele has never been published on.**

**(c) Scholar Gateway was not used.** Every HGVS string in this document came from PubMed metadata, from a PMC body, or from the repository's ClinVar file. **No variant string was attributed to any article by passage or cross-reference ID**, and no hyphen- or asterisk-stripped token entered the analysis.

### 5.4 · What I could not verify

1. **No sequence database.** `rest.ensembl.org`, `eutils.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov` and `www.ebi.ac.uk` all return **403 at CONNECT**. The exon map in § 2 is derived from **ClinVar's `NM_016373.4` annotation inside this repository**, not from the RefSeq exon table. Strong (729 + 191 concordant records, zero contradictions), but not the primary source.
2. **Four positions of the exon 9 acceptor (−8 to −5) are unknown to me**, so I cannot exclude an upstream cryptic `AG` there. Similarly `c.1061` is unknown, so Reading A's required `AG` is supported by only one of its two bases.
3. **The `+8` convention is unresolved** (§ 2.6) and I did not re-run SpliceAI. **This is the single cheapest open item in this document.**
4. **M-2 and M-3 remain abstract-depth**, as they were for the prior census. Nothing about tissue, quantification, NMD control or residual normal transcript can be claimed from either.
5. **No figure was inspected** in this environment, and per D-14 no negative asserted only by a figure is adjudicated.
6. **B-2's 46 kDa / 19 kDa isoform weights could not be re-verified** — the extractor deleted them (§ 1.2).
7. The **1-nt intron 8 discrepancy** (778,855 vs 778,856) is flagged, not resolved.
8. **Whether banked RNA exists** for the PMID 26345274 or PMID 42721537 cohorts is undocumented and not determinable from here.

---

## § 6 · Contradictions and amendments to what the repository currently asserts

| # | Standing text | Amendment | Basis |
|---|---|---|---|
| **E-1** 🔴 | `paper_registry_current` PAPER 044: *"qui l'NMD **avviene** perché la lesione è sull'esone 6"*, quoting the abstract *"the deletion led to nonsense-mediated decay"* | **The source's Results section does not say that.** It says *"suggesting that the two longer transcripts were not expressed **or were degraded**"* — an explicit disjunction — and **no NMD inhibitor was used**. The NMD attribution is an abstract-level inference. The registry's downstream reasoning (exon 6 vs exon 9 regimes) is right; its evidential warrant is one grade weaker than stated. | PMC6296882 body re-read today [DOI](https://doi.org/10.1002/humu.23675) |
| **E-2** 🔴 | `tx001_public_rna_data_feasibility` C-2: *"No `−3` neighbour variant exists in LEGEND for either."* | **`c.1057-3C>T` exists**, classified **Uncertain significance**, in `analysis/data/WWOX_clinvar_all_variants.csv` — the −3 neighbour of the reference genotype's own acceptor. So do `c.108-3C>T`, `c.231-3C>A`, `c.410-3T>C`. C-2's substantive half (different acceptors, opposite NMD regimes) is **confirmed**. | repository's own ClinVar file |
| **E-3** 🔴 | `DL-MECH-045`: *"uso del sito criptico +8 (**frameshift**)"* | **Unresolved, and the two conventions give opposite biology.** Under SpliceAI's standard convention the gained acceptor is at c.1063 ⇒ **6 nt lost ⇒ in-frame ⇒ hypomorph, no PTC, no NMD question at all.** Under the alternative ⇒ 8 nt ⇒ frameshift ⇒ the repository's current position. Neither is measured. **Re-read the raw `DP_AG` field before either is carried forward.** | § 2.6 arithmetic on `DL-BIO-002`'s own recorded coordinate |
| **E-4** 🔴 | Nothing in the repository records exon 7's length or frame; the splice alleles are reasoned about under a uniform PTC/NMD frame | **Exon 7 is 186 nt, `186 mod 3 = 0`, symmetric phase — the ONE internal exon whose skipping is in-frame.** Its acceptor is `c.606-1G>A`, the five-patient allele. If skipped, the predicted product is an internally deleted 352-aa protein with **no PTC and no NMD**, excising the region that contains codon 230. `PREDICTED`. | § 2.2, § 2.4 |
| **E-5** ⚠️ | `tx001_experiment_decision_packet` B.3: normaliser = **exon 4–6 "core"** | **That denominator is not inert.** B-2 measured that WWOX has three transcripts and that the **short isoform's exon 5–6 junction rose** when the long isoform was lost. An exon 4–6 amplicon measures a mixture whose composition moves with the lesion. Use a long-transcript-specific amplicon and report isoform composition. | § 1.2, § 4.1 |
| **E-6** ⚠️ | `wwox_splice_transcript_census_20260921` totals (20 records; 3 measured + 1 boundary + 2 annotated + 14 context) | **The totals are correct for the census's four queries and incomplete relative to the repository's own registry.** PMID 30362252 / PAPER 044 is a measured WWOX transcript study that no splice-word query can return, because its title and abstract contain no splice word. Boundary cases: **2, not 1.** The **3** splice-allele measurements are unchanged and independently verified. | Q-A, Q-D |
| **E-7** ℹ️ | `FT-110` carries `38902482` as a splice-census record awaiting a fetch attempt | **Not applicable.** PMID 38902482 is an esophageal-cancer Hippo/YAP cell-line study with no variant transcript work. The reading debt on it can be closed; the debt on `42721537` stands, as does FT-110's central argument. | metadata retrieved today [DOI](https://doi.org/10.1007/s10528-024-10856-9) |
| **E-8** ℹ️ | `tx001_experiment_decision_packet`: intron 8 = **778,856 bp** | **778,855 nt** on GRCh38 by this derivation. One nucleotide; assembly or interval convention. Inconsequential, recorded so it is not inherited as exact. | § 2.2 |
| **E-9** ✅ | `DL-MECH-045` premises: nine exons · exon 9 last · c.1057 = codon 353 · exon 9 = last ~62 aa · `DL-BIO-002` coordinate chr16:79,211,606 · exon 6 = 89 nt frameshifting | **All six CONFIRMED** against an independent derivation that does not use any of them. The prior sessions' arithmetic was right. | § 2.3 |

---

## § 7 · The answer to the question asked

**What is actually MEASURED about the transcript consequences of WWOX splice-site alleles?**

**Three sentences, in three papers, over twenty-five years of literature on this gene.** One donor allele in a two-exon minigene in embryonic kidney cells with a truncated intron, read in full. One donor allele in patient blood RNA, abstract only, unreachable. One acceptor allele by cDNA sequencing, abstract only, unreachable. **Every one of them reports an exon-skip and none of them reports a number.** No fraction, no ratio, no residual normal transcript, no NMD inhibitor, no protein, no correction arm, no long-read, in any of them, in any tissue, for any allele. Ten further patients across two canonical alleles have had their DNA read and their RNA never looked at. The reference genotype's own allele has **zero** publications.

**Does any of it constrain what the reference genotype's acceptor allele does?**

**Weakly, and less than it appears to.** The class precedent is real — canonical WWOX splice alleles that have been looked at produced exon skipping — but it comes from four other exons in four other frame and NMD regimes, and § 2 shows this gene contains at least three genuinely different regimes. The one measured acceptor allele, `c.517-2A>G`, opens **exon 6**, an internal 89-nt frameshifting exon whose PTC is an NMD substrate. The reference genotype's allele opens **exon 9**, the terminal exon, where **exon skipping is not even a defined outcome** and every plausible product escapes NMD. The two are not analogues; they are opposites that happen to share a position label. And whether the predicted cryptic product is a two-codon in-frame deletion or a frameshift — a hypomorph or a null — **turns on a coordinate convention that has never been written down.**

> ### 🔴 `PREMISE: NOBODY_LOOKED` — upheld.
> **3** splice-allele RNA measurements in the entire field, **1** on an acceptor, **0** readable here, **0** quantified, **0** with an NMD block, **0** with a protein readout, **0** with a correction arm, **0** on the reference genotype's allele, and **0** on any of the four −3 alleles where leaky splicing is mechanistically possible. **The gap is not difficulty. It is that nobody has done it.**

---

*Author: Scientist E. Date: 2026-09-22. READ-ONLY: no canonical file, registry, ledger, queue, receipt or state manifest was modified; no git operation was performed; no commit candidate was produced; this file is the only file written inside the repository. No contact was attempted with any research group and no personal contact details appear anywhere in this document. Nothing here is medical advice and nothing here is a treatment proposal — it is an assay specification and a census of absence. Article metadata and full texts were **retrieved from PubMed / PubMed Central**; exon coordinates were derived from the repository's own ClinVar export.*

**DOIs cited:**
[39101447](https://doi.org/10.1002/mgg3.2500) ·
[38407561](https://doi.org/10.1002/ajmg.a.63575) ·
[30853297](https://doi.org/10.1016/j.ejpn.2019.02.003) ·
[22071891](https://doi.org/10.1038/ejhg.2011.204) ·
[30362252](https://doi.org/10.1002/humu.23675) ·
[26345274](https://doi.org/10.1002/ajmg.a.37363) ·
[42721537](https://doi.org/10.1016/j.seizure.2026.08.027) ·
[38902482](https://doi.org/10.1007/s10528-024-10856-9) ·
[26857392](https://doi.org/10.1093/jnci/djv387) *(Schirmer 2016; DOI resolved with `convert_article_ids` this session, matching `paper_registry_current`. ⚠️ Self-correction recorded: I first wrote `djv407` from memory — the exact failure the brief names. Caught against the registry and then resolved with a tool.)*
