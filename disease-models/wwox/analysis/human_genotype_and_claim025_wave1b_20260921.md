# Human genotype architecture, a homozygous missense allele, and an independent test of `CLAIM 025`

**Wave 1b — W-3 / W-4 / W-5 · Scientist B · 2026-09-21**

**Mode:** READ-AND-REPORT, **READ-ONLY toward every canonical file.** No registry, ledger, claim,
`*_current.md` or working-model file was edited. No `BATCH_COMMIT`, no commit candidate, no receipt
written. The only files this reading creates are this analysis file and the six retrieved-text
artefacts fingerprinted in § 1.

**Sources.** According to PubMed. Full texts retrieved through the PubMed MCP server (PMC
open-access subset).
W-3: Dong X-S, …, Li Z-M, *BMC Med Genomics* 2023;16(1):291, PMID 37974179 / PMC10652538 —
[DOI](https://doi.org/10.1186/s12920-023-01731-4).
W-4: Sukkar G, …, Al Lohaibi RS, *Cureus* 2022;14(5):e25003, PMID 35712340 / PMC9193507 —
[DOI](https://doi.org/10.7759/cureus.25003).
W-5: Hammouz RY, Maciejek K, Bednarek AK, *Int J Mol Sci* 2026;27(15), PMID 42589397 / PMC13467099 —
[DOI](https://doi.org/10.3390/ijms27156740).

> **Not medical advice.** Public edition: this file reasons about a WWOX-DEE genotype class and
> about published, already-public case reports. It introduces no individual-level linkage.

---

## 0 · Ledger check, performed BEFORE reading

Run with `registry_records.py` — **the two large registries were never grepped.**

| PMID | Expected by the brief | **Measured today** | Verdict |
|---|---|---|---|
| `37974179` | `CORPUS-STUB-096` / `LIT-0118`, `not_processed` | `paper_registry_current.md:1650` → `CORPUS-STUB-096`, `Status: not_processed`, `Claim links: none`; `literature_tracking_log_current.md:3599` → `LIT-0118`, `Status: discovered`, `clinical relevance: HIGH` | ✅ **confirmed**, with one refinement: the LIT record's status string is `discovered`, not the word `not_processed` (that string belongs to the paper-registry stub). Both mean unread. |
| `35712340` | `CORPUS-STUB-141` / `LIT-0160`, `not_processed` | `paper_registry_current.md:2077` → `CORPUS-STUB-141`, `Status: not_processed`; `literature_tracking_log_current.md:4741` → `LIT-0160`, `Status: discovered`, `clinical relevance: LOW` | ✅ **confirmed**, same refinement. |
| `42589397` | **no record** | No identity record in any of the seven searched surfaces. One **mention** only, at `full_text_queue_current.md:5127` (`FT-113`), which is the queue entry that dispatched this very reading. | ✅ **confirmed** — held in no registry, no tracking log, no claim. |

`reading_state.py`: **none of the three PMIDs appears anywhere in the 123-paper / 186-receipt union.
No receipt exists for any of them.** ✅ as expected.

⚠️ **Tool-reported state, recorded not hidden:** every `registry_records.py` call in this session
printed `🔴 read at commit …, WORKING TREE DIRTY: disease-models/wwox/research/full_text_queue_current.md`.
The `FT-113` text quoted above therefore reproduces an uncommitted edit.

**Prior art read before retrieval** (so it is not re-derived):
[`next_node_scout_20260921_orchestrator.md`](next_node_scout_20260921_orchestrator.md),
[`lodz_node_discriminator_20260921.md`](lodz_node_discriminator_20260921.md) (sibling actor, today),
[`AUTONOMOUS_SESSION_STATE.md`](AUTONOMOUS_SESSION_STATE.md), and `CLAIM 025` fetched by
`registry_records.py get --id "CLAIM 025"` **before** W-5 was opened.

### 🔴 CORRECTION, against myself, before the reading is reported

A sibling actor appended a correction to
[`next_node_scout_20260921_orchestrator.md`](next_node_scout_20260921_orchestrator.md) while this
reading was in progress, earning the method rule **`NO RECORD MATCHED` ≠ `NOT HELD`**:
`registry_records.py` reads a fixed surface list that **excludes `disease-models/wwox/analysis/`
and `therapeutic_hypotheses_ledger_current.md`**, reads **committed** state only, and returns
`NO RECORD MATCHED` for an identifier sitting inside the *body* of a record on a surface it does
read. I applied that rule with a plain sweep — `grep -rn "<id>" --include=*.md disease-models/`,
**excluding the two large registries, which `registry_records.py` had already covered** — and it
overturned two statements I had already written.

**Correction 1 — `DL-MECH-020` exists, and I had written that it did not.**
`registry_records.py get --id "DL-MECH-020"` returns `NO RECORD MATCHED` because the record's
heading is not the bare ID but `### DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via
HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica`. It is at
`discovery_ledger_current.md:457`, and it states the corroboration weight in its own words:

> *"⚠️ **E non sono due voci che si corroborano:** sono **un primario di un laboratorio più la review dello stesso laboratorio su quel primario**, appoggiati ai topi di Aqeilan e a una linea MCF7. **Peso di corroborazione: uno.**"*

**§ 7's corroboration answer now rests on the record itself, not on a substitute.**

**Correction 2 — 🔴 W-3 is NOT unread. It is already deep-read and already `promoted-to-CC`.**
This is the more consequential of the two, and it changes what this reading is worth.
`discovery_ledger_current.md:1340` carries:

> ### `DL-MECH-053` — *Una chiamata exon-level corretta puo' nascondere un'architettura WWOX allelica diversa*
> - **Status:** `promoted-to-CC` · **Tag:** DATO (PMID 37974179) + INFERENZA multi-paper (con PMID 35573960)
> - **Fonte:** Dong et al. 2023, PMID 37974179 / PMCID PMC10652538; main text, figure e due supplementari letti integralmente. Dossier: `staging/deepdive_PMID37974179_Dong2023.md`.

🔴 **The headline finding I was dispatched to establish is already held, in a lead whose title says
it in one line.** `DL-MECH-053` already records the WES/qPCR-vs-WGS inversion, already records
*"nessun RNA, proteina o funzione"*, already records that residual function of the `del ex6-8`
allele is *"soltanto predetta"*, and — remarkably — **already records the very size-swap defect I
found independently at L05**: *"le dimensioni delle due delezioni paterne sono scambiate in una
frase narrativa"*. Its framing is also better than mine and I adopt it: *"La diagnosi WWOX
biallelica non era falsa, ma la rappresentazione era incompleta."*

**So the paper-registry stub is stale, not the laboratory's knowledge.** `CORPUS-STUB-096` says
`not_processed` and `LIT-0118` says `discovered` while a `promoted-to-CC` lead cites the paper's
main text, figures **and two supplementaries** as read in full. The registry surfaces and the
discovery ledger disagree, and **the surfaces `registry_records.py` reads are the ones that are
wrong.** Recorded for the operator; not repaired here, because this actor is read-only.

**What this reading therefore still contributes on W-3, stated at its true and reduced weight:**

1. 🔴 **There is no receipt and no retrievable dossier.** `fulltext_receipts.py verify` reports
   `OK: 188 chained receipt(s)` and **none is for `37974179`**; `reading_state.py` does not list the
   PMID; and the dossier `DL-MECH-053` cites — `staging/deepdive_PMID37974179_Dong2023.md` — **does
   not exist in this checkout** (`disease-models/wwox/research/staging/` is absent entirely; the
   string `deepdive_PMID37974179` occurs in exactly one file, the ledger entry that cites it).
   Either that dossier lives on an unmerged branch or in the private edition, or it is lost. **Per
   `reading_state.py`'s own header warning, a count over unmerged state is not evidence of absence —
   so I report this as unverifiable here, not as missing.** Either way: a `promoted-to-CC` lead
   currently rests, *in this tree*, on a reading nothing in this tree can check.
2. ✅ **This reading supplies exactly what was missing: a fingerprinted artefact** (§ 1) against
   which `DL-MECH-053`'s statements can be verified, plus **19 verbatim locators re-matched against
   it**. Every load-bearing sentence of `DL-MECH-053` that concerns the main text is confirmed
   character-for-character below. **It is an independent second reading that agrees**, which under
   the parallel-reading rule is a sibling, not a correction.
3. 🔴 **One discrepancy between `DL-MECH-053` and the source, flagged rather than resolved.** The
   lead's DATO line reads *"WGS 30x + gap-PCR/Sanger hanno rivelato **un allele di sito accettore**
   `del ex6-8` **e un allele missense** con due delezioni discontinue (`intron 5` + `exon 6`)"*.
   **The paper describes neither a splice-acceptor allele nor a missense allele in this proband** —
   it describes an in-frame genomic deletion of exons 6–8 (`c.517_1056del`, `His173_Met352del`, L09)
   and two discontinuous genomic deletions on the other allele (L05, L06). ⚠️ **I do not call this a
   scientific error**, because *"allele di sito accettore"* and *"allele missense"* are precisely the
   two class names the public edition uses for the reference genotype, so this is at least as likely
   to be a **de-identification substitution artefact** introduced when the private record was
   rewritten for the public edition. **Operator decision, not mine.** It matters either way, because
   as it stands the lead assigns this proband to two genotype classes the source does not support.

**Correction 3 — the same sweep, applied to W-4 and W-5.** `35712340` appears only in
`full_text_queue_current.md` (FT-113), `batch_queue.md` (`screened`) and the scout file; `42589397`
appears only in FT-113 and the scout file. **Neither has a deep-dive, a dossier, a discovery lead or
a receipt.** ✅ For these two the brief's expectation holds under the stronger test as well.

---

## 1 · ARTEFACT MANIFEST

Every retrieved body was written to disk **before** analysis. The bodies were first hand-persisted
from the tool return, then **re-derived programmatically from the tool's own persisted JSON and
overwritten**, so that what is on disk is byte-identical to what the extractor returned (the
hand-persisted copies differed only by a trailing newline, and for W-5 not at all). Abstracts are
kept as separate sidecars so that abstract-anchored locators are re-matchable too.

| Paper | Path | Bytes | Chars | sha256 |
|---|---|---|---|---|
| W-3 · PMID 37974179 · body | `files/fulltext/PMID37974179_PMC_MCPtext.txt` | 17,775 | 17,590 | `50a6174ff75ee6aded57a5f4715a1a4d5ca43dfeea7c8ec5c945612d2ef979fb` |
| W-3 · abstract | `files/fulltext/PMID37974179_PMC_MCPabstract.txt` | 1,782 | 1,774 | `8b3ebd1bd0ab6bc862321aefc30b70ff75ff5b7e2485f08cc4615243dc610df8` |
| W-4 · PMID 35712340 · body | `files/fulltext/PMID35712340_PMC_MCPtext.txt` | 15,396 | 15,270 | `777ca3f956db0e0bf7a28893b159793a9eaf9e641c2d9c58a02db921d616355e` |
| W-4 · abstract | `files/fulltext/PMID35712340_PMC_MCPabstract.txt` | 1,351 | 1,349 | `6d44274ea60766ee72542461facd68dfe8dfbc290c1db1276cfc3d76baf9c3f7` |
| W-5 · PMID 42589397 · body | `files/fulltext/PMID42589397_PMC_MCPtext.txt` | 55,875 | 55,725 | `572a7e6b14b8d10ec993c901dd367b2163437077f5b6fb429e874a5fc43e6e16` |
| W-5 · abstract | `files/fulltext/PMID42589397_PMC_MCPabstract.txt` | 1,919 | 1,913 | `3a5bed8ffe3c0cdd518fb7f30eeb8962c132c25214b6744fee613e3fe42b3411` |

No body came back empty. Byte counts exceed character counts because the extractor emits multi-byte
characters (en dashes, primes, thin spaces, non-breaking spaces, `−` U+2212).

### 🔴 Instrument limits measured on these six artefacts

1. **Italic gene tokens are elided.** `thegene`, `theratio`, `Theratio`, `heterozygousexons`,
   `ofas` are all extractor damage, not source text. **No zero string-count for any gene symbol in
   these artefacts is a biological negative.** Every negative asserted in § 5 rests on a positive
   statement by the authors or on the absence of an entire Methods section, never on a token count.
2. **Superscripts are elided — and in W-5 this destroys p-values.** The Results read
   `= 5.7 × 10`, `= 4.8 × 10`, `= 5.9 × 10`: **the exponents are gone and are not recoverable from
   this route.** I report those p-values as `5.7 × 10^(exponent elided)` and never as "p = 5.7".
   The same elision removes the `L` subscript in "L penalty" (LASSO L1) and the `2^(-ΔΔCt)` in W-3's
   `The fold-change was calculated using the 2method`.
3. **Citation numbers are elided**; markers render as `[]`, `[,]`, `[-]`, `[,–]`. **No statement in
   this file is attributed to a numbered reference.** Where I name another study (Mignot, Abdel-Salam,
   Suzuki, Ehaideb, Mallaret, Ben-Salem, Hussaine), the name is printed in the body text itself; I
   attribute by that printed surname only, never by resolving a bracket.
4. **Reference lists are ABSENT in all three bodies** — `grep -ic "References"` returns 0 for W-3 and
   W-4. This matches the corpus-wide measurement recorded in `AUTONOMOUS_SESSION_STATE.md`
   (29/29 artefacts). Now 32/32.
5. **No figure image is inspectable.** W-3's molecular findings are figure-anchored (`Fig.a`,
   `Fig.b`, `Fig.c, d` — the panel letters survive, the figure numbers do not). Figure *legends* did
   not survive into the body text either, so for W-3 and W-5 there is **nothing quotable from any
   figure**. Every numeric result below comes from Results prose.
6. **Tables are flattened to one cell per line.** W-4's Tables 1–3 survive as unlabelled value
   sequences. Column alignment in Table 3 is therefore **not reliable** — the `Nature of mutation`
   row emits seven `Homozygous` cells for six patient columns and the `Variant` row emits three
   entries for five studies. I take from Table 3 only the single cell that is unambiguous by
   adjacency (`P.lle136Val`, immediately under `Amino acid change` and in the `Current case` column)
   and I flag the rest as not safely readable.

---

## 2 · VERDICT

**W-3 (37974179).** A documented case in which **the exome call was wrong about the allele
structure in every respect that matters** — one homozygous exon-6 deletion became three deletions
of 13.3 / 53.9 / 177.2 kb across two alleles, resolved only by WGS plus gap PCR and Sanger, and the
correction changes the predicted genotype class from *frameshift-null on both alleles* to
*frameshift-null / in-frame SDR-removing deletion with a theoretical residual product*; **no RNA
and no protein were measured, so "residual function" is predicted and never observed.**

**W-4 (35712340).** A single consanguineous case with a homozygous `c.406A>G` (`p.Ile136Val` per the
paper's own table), **no transcript accession, no stated ACMG class, no evidence codes, no domain
assignment for the residue, and no functional or protein work of any kind** — a genotype–phenotype
datum only, and an unusual one, because this child has **no seizures and a normal MRI**, which the
authors themselves reduce to "partially supportive of DEE28".

**W-5 (42589397).** A larger, newer TCGA analysis of the WWOX/HIF1A ratio that is **from the same
laboratory and the same senior author as LEGEND's existing supporting papers, run on the same
datasets as that group's own earlier overall-survival paper**, whose own abstract calls the ratio
"not … a uniform or strongly predictive prognostic marker" and its survival trends "non-significant
and exploratory", and whose bootstrap-corrected discrimination for the breast multivariable model
is **centred close to zero**.

**Overall.** The batch's one consequential result is W-3's method-level correction, which is a
constraint on how LEGEND may assign genotype classes from exome-derived reports; W-4 adds one
missense/missense data point with a large phenotypic caveat and no mechanism; W-5 **qualifies**
`CLAIM 025` by showing the ratio's prognostic *sign is not invariant across contexts*, and — being
same-group, same-dataset, tumour-only and perturbation-free — **cannot raise its corroboration
weight and provides nothing that would license transfer to a non-tumoral CNS claim**.

---

## 3 · Per paper

### 3a · W-3 · PMID 37974179 — genotype architecture

**Design.** Single-proband case report with family segregation (proband III1; father II1; mother
II2; maternal grandfather I3), unrelated Chinese family. **n = 1 affected individual.** Four
molecular methods, all DNA-level: WES (KAPA HyperExome, MGIseq-2000, PE100, GRCh38, BWA + GATK +
SnpEff; CNVs by ExomeDepth); a **gene-dosage qPCR on genomic DNA** for exon 6 (the paper calls it
"qRT-PCR", but the template is DNA diluted to 50 ng/µl from family members and a healthy control —
it is a dosage assay, not a transcript assay); 30× WGS (DNBSEQ-T7, PE100, BWA-MEM + GATK, CNVnator
for CNVs, BreakDancer for SVs); and gap PCR with Sanger sequencing for breakpoints, with
RepeatMasker and R-loopDB screens of the junction flanks. **Endpoint:** molecular diagnosis and
breakpoint resolution. **Statistics:** none — there is no statistical test anywhere in this paper.

**What each method called.**

| Method | Call |
|---|---|
| **WES** | *"a homozygous deletion involving exon 6"* (L01) — one event, exon-6-limited, homozygous. |
| **qPCR gene dosage** | I3, II1 and II2 each heterozygous for an exon-6 deletion; *"No amplification was seen in the proband as if he harbors a biallelic deletion of exon 6"* (L02). **This did not correct the WES call — it corroborated it.** |
| **WGS** | *"three larger deletions … not two deletions"* (L03): **177,200 bp** removing exons 6–8 (chr16:78,331,193–78,508,394); **13,261 bp** in intron 5 (78,337,740–78,351,002); **53,904 bp** removing exon 6 (78,368,802–78,422,707), all hg38 (L04). |
| **Gap PCR + Sanger** | Junctions confirmed at base resolution: 177,204 bp in I3/II2/III1; 13,260 bp at 78,337,741–78,351,002 in II1/III1; 53,904 bp at 78,368,802–78,422,707 in II1/III1 **with an `ATACACACACAC` insertion at the junction** (L06). Phase: exons 6–8 maternal; intron 5 + exon 6 paternal and discontinuous (L05). |

#### 🔴 Did the exome call misrepresent the true allele structure? — **YES.**

Plainly, and in four separate respects: the **number** of events (one vs three), their **size**
(exon-6-limited vs 13.3–177.2 kb), their **phase** (homozygous vs compound heterozygous with two
deletions in *cis* on the paternal allele), and the **extent** of the lesion on the maternal allele
(exon 6 vs exons 6–8). The sentences are:

> *"The WES analysis revealed a homozygous deletion involving exon 6 of thegene in the proband."* (L01)

> *"Interestingly, the WGS analysis revealed also the presence of three larger deletions in thegene in the proband, not two deletions (Fig.)."* (L03)

and the authors' own conclusion:

> *"While WES may encounter some pitfalls in detecting copy number variations in the WWOX gene, WGS accurately addresses intricate variant configurations and investigates potential mechanisms underlying their formation."* (L07)

**Why this is consequential for LEGEND, stated precisely.** The genotype *class* changes with the
correction. Under the WES call both alleles carry the exon-6 deletion, which the paper itself
predicts is *"a common deletion predicted to cause a frameshift mutation resulting in a truncated
protein with loss of function"* (L08) — i.e. **null/null**. Under the WGS-corrected structure one
allele is that frameshift-null and the other is an **in-frame internal deletion**, which the paper
predicts *"theoretically produces a protein with normal WW domains, but due to the disruption of the
SDR domain, it may retain poor residual function"* (L09). 🔴 **"Theoretically" and "may retain" are
the paper's words and must survive**: nothing was measured. This is therefore a documented instance
where an exome-derived report would have placed a proband in **null/null** when the true structure
is **null / possible-residual-protein**, and both of those are classes LEGEND reasons about
separately. It also means the **`large deletion / CNV` class cannot be treated as a single class**:
a CNV call of "exon 6 deletion" and a CNV call of "exons 6–8 deletion" imply different predicted
protein consequences, and an exome-based CNV caller conflated them here.

**Two further constraints, both from this paper alone.**
- The **qPCR dosage assay did not catch the error** (L02). A confirmatory orthogonal assay that is
  itself exon-targeted reproduces the exon-targeted blind spot. So "CNV confirmed by qPCR" is not
  evidence of allele structure.
- The error was detectable only because the two paternal deletions lie **inside the span of the
  maternal deletion**. *(My arithmetic on the paper's own hg38 coordinates, labelled as mine and not
  the paper's: 78,337,740–78,351,002 and 78,368,802–78,422,707 both fall within
  78,331,193–78,508,394; the stated spans compute to 177,201 / 13,262 / 53,905 bp against the paper's
  177,200 / 13,261 / 53,904, and gap PCR reports 177,204 / 13,260 / 53,904 — off-by-small
  discrepancies I record rather than smooth over.)* Because exon 6 is absent from **both** alleles,
  exome read-depth sees zero coverage and reads "homozygous deletion". **That failure mode is
  generic to WWOX**, which the paper notes spans FRA16D from introns 5 to 8.

🔴 **A discrepancy internal to the paper, recorded rather than repaired.** L05 states the paternal
alleles as *"intron 5(53,904 bp) and exon 6(13,260 bp)"* — the two sizes are **swapped** relative
to L04 and to the abstract, both of which assign 13,261 bp to intron 5 and 53,904 bp to exon 6.
The abstract (L19) is internally consistent with L04. I take L04/L19 as the intended assignment and
flag L05 as a transcription error in the source. **Anyone reusing this paper's numbers must not
quote L05's parenthetical sizes.**

**Was any RNA or protein measured? — NO.** Confirmed positively, not by token count: the Materials
and methods section contains exactly four assays (WES, DNA-dosage qPCR, WGS, gap PCR/Sanger) and no
RNA extraction, no RT step on RNA, no cDNA, no Western blot, no antibody, no cell culture and no
tissue. Every string match for "RNA" in the artefact falls inside *maternal*, *internal* or
*International*. 🔴 **"Not measured" is not "absent":** this paper does not show that the exons 6–8
allele fails to make protein, nor that it makes any. It shows nothing at all about protein.

**Phenotype.** Term birth, NSVD, 3.39 kg (50th centile), no perinatal hypoxia. **Onset day 15** —
*"infantile seizures characterized by clenched teeth, cyanosis around the lips and tetanic twitch of
the limbs"* (L10), 10–15/day. **Sodium valproate and topiramate ineffective** (L11). Growth
retardation and developmental delay; unable to follow objects, roll over, sit alone or speak.
**EEG:** *"slow weakened of background activity observed in both hemispheres and and polyspikes
low-wave discharge in bilateral temporal lobes"* (L12, `sic` — the doubled "and" is in the source).
**MRI:** *"white matter hyperintensity and delayed myelination in the brain"* (L13) — note
**no** corpus callosum finding, **no** cerebral atrophy and **no** optic atrophy are reported for
this proband, although the Introduction lists all three as typical. **Death at 2.5 years, cause
given as persistent seizures**; at death 69 cm (−6 SD) and 8 kg (−4 SD) (L14).
🔴 **No head circumference is reported anywhere.** The Discussion names *"progressive microcephaly"*
as a WOREE feature in general; **it is not documented in this child and must not be imported into a
per-case record.**
🔴 Results call the events *"tetanic twitch of the limbs"*; the Discussion calls them *"multidaily
tonic seizures"*. Results-first: the semiology of record is L10.
🔴 The Discussion's *"Our proband had the earliest onset of epilepsy, presenting on the 15th day of
life"* (L16) is a **priority claim whose supporting comparison sits in a Supplementary Table that is
not in this artefact.** It is not verified here and should not be carried as a fact.

**Not tested / not done.** No RNA, no protein, no functional assay, no cell or animal work, no
statistics, no longitudinal EEG series, no head circumference, no autopsy, no second affected
individual. The grandfather/lung-cancer connection is explicitly *hypothesised* (L17), never
measured. Clean in-paper negative: *"No R-loop forming sequences were found"* at the three junctions
(L15) — a real negative about the **mechanism of deletion formation**, with no bearing on WOREE
biology.

---

### 3b · W-4 · PMID 35712340 — a homozygous missense allele

**Design.** Single-patient case report with literature comparison. **n = 1.** Trio-supported WES
(Bioscientia Labor Ingelheim; Roche KAPA HyperExome; Illumina; mean coverage 116.4×; ~99.9 % of
target ≥ 15× and ≥ 20×). **Endpoint:** molecular diagnosis. **Statistics:** none.

**The variant.**
- **Nucleotide change:** `c.406A>G`, homozygous, `WWOX (OMIM:605131)` (L20).
- 🔴 **Transcript reference: the paper does not give one.** No `NM_`, no `ENST`, no RefSeq
  accession, no transcript version appears anywhere in the body or the abstract (`grep -c "NM_"` =
  0, `"ENST"` = 0, `"RefSeq"` = 0 — and none of these is an italic token, so the extractor is not
  the explanation). **A `c.` designation without a transcript is not a complete variant
  description.** Genome coordinate given in Table 3 for the current case: `Chr16:78149048`, **with no
  stated assembly**; the comparator column that does name one says `GRCh37`.
- **Predicted protein change:** `P.lle136Val` (L32) — Table 3, `Amino acid change` row, `Current
  case` column. Read as `p.Ile136Val` (the extractor renders capital I as lowercase l). This is
  **the paper's** assignment, not mine.
- 🔴 **Domain: the paper does not say.** Its only domain statement is the generic architecture
  sentence — *"two interacting WW domains at the N-terminal … and a short-chain
  dehydrogenase/reductase domain at the C-terminus"* (L31). **Residue 136 is never assigned to WW1,
  WW2 or SDR-ADH anywhere in this paper.** I have not computed an assignment and I do not supply
  one; the honest record is *domain assignment absent from source*.
- **ACMG:** 🔴 **no classification and no evidence codes are reported.** The paper states only the
  framework — *"Classifications of variants were conducted based on ACMG Guidelines (Richards et al.)
  considering database entries (inc. HGMD), Bioinformatics predictions tools, and literature status"*
  (L23). The words "pathogenic", "likely pathogenic" and "VUS" never appear as a verdict on
  `c.406A>G`; `grep` for `PM2`, `PP3`, `PS3`, `PVS1` returns zero. **The variant is never formally
  classified in this paper.**
- **Evidence actually offered instead:** an in-silico tally — *"Out of 21 bioinformatic in silico
  experiments, 15 showed a pathogenic effect"* (L21) — and a frequency statement: 0.0042 % of the
  general population, five heterozygotes, **0 homozygotes in gnomAD v2.1.1 controls** (L24).
- 🔴 **A predicted splice effect that was never tested.** *"The in silico predicted that the position
  of the identified variant might lead to significant alterations in mRNA splicing owing to an
  altered splice site"* (L22). **"Might lead" is the paper's mood and it stays.** No RNA was
  extracted, no RT-PCR, no minigene, no transcript analysis of any kind was performed. **So it is
  not established that this allele behaves as a missense allele at all** — it may be a splice
  allele, and the paper cannot say which. *(As my own labelled observation, not the paper's: the
  comparator variant `c.409+1G>T` in Table 3 sits three bases downstream of `c.406`, which is
  consistent with `c.406` lying near an exon–intron boundary; the paper does not make this argument
  and no RNA evidence exists either way.)*

**The prenatal WES arm.** *"A parallel analysis of prenatal WES data revealed that both parents were
heterozygous carriers of thevariant, confirming its homozygosity"* (L25); the abstract says the same
(L64). 🔴 **What it showed is parental carrier status — a segregation/trio confirmation.** No fetus,
no gestational age, no indication, no prenatal phenotype, no prenatal imaging and no outcome of any
pregnancy is reported. **It is not a prenatal phenotype observation and must not be logged as one**
in a node whose research question is about the prenatal brain.

**Consanguinity and family.** *"his parents were consanguineous; of his first-degree relative with
four siblings, three were healthy and one was known to have seizures"* (L26); a cousin with a
history of cerebral palsy. **Neither relative was genotyped** — no segregation beyond the parents is
reported.

**Phenotype.** 21-month-old boy; term, caesarean, no NICU. Motor delay dominant: at 1 year could not
roll, sit or stand unsupported; by 15 months crawling, pulling to stand, sitting unsupported; at 21
months *"he can say 10 words but not complete sentences, climb stairs with assistance, walk, and run
with recurrent falling"* (L35). Power 4/5 in all limbs with good reflexes and tone; leg bowing; flat
feet; a café-au-lait spot on the right thigh; good eye contact; an abnormal gaze noted three times.
Mild hepatosplenomegaly. **Alive at report.**

🔴 **Two prominent negatives that make this case atypical for DEE28/WOREE:**
> *"our patient presented with a global developmental delay and no early seizure disorder despite a family history of seizures and cerebral palsy in his brother and cousin, respectively."* (L27)

> *"Additionally, the MRI was normal, with no progressive microcephaly or bilateral optic atrophy."* (L28)

and the authors' own hedge: *"From the available information, the patient phenotype appears
partially supportive of DEE28."* (L29). **No seizures, normal MRI, normal head growth, alive at 21
months** — in a disease defined by refractory neonatal/infantile seizures and abnormal MRI in
essentially all reported patients. Either the allele is hypomorphic, or the phenotype is not
WWOX-driven; **this paper cannot distinguish those, and it does not claim to.**

**Biochemistry reported.** Elevated alpha-aminobutyric acid (28; ref 3–26) and markedly low cystine
(5; ref 16–84); high CK; high AST, albumin, total and direct bilirubin; low globulin; low
triglyceride; high B12 and 25-OH vitamin D. 🔴 **Text–table contradiction:** the text says *"Liver
profiles, including ALT and GTT, were normal"* (L36) while Table 1 lists **ALT = Low** and **GGT =
Low**; the text and conclusion call the picture *cholestasis*, which low GGT and low ALT do not
support. **Do not carry "cholestasis" as a measured WWOX-associated finding.** The name "GTT" in the
text and "Creatinine Kinase" in Table 1 are also mis-namings of GGT and creatine kinase.

**Is there ANY functional or protein-level work? — NO.** Confirmed positively: the paper contains no
Methods section beyond the WES protocol; `grep -ic` for `Western`, `blot`, `immunoblot` returns 0
for each, no cell line, no construct, no antibody, no expression measurement, no enzymatic assay.
**This is a genotype–phenotype datum only.** It supports no mechanistic proposition, and it cannot
be used to say anything about WWOX protein abundance, stability, localisation or activity.

**Journal-level quality caveat (recorded, and *not* used to dismiss the genotype).** *Cureus* is a
low-editorial-bar venue and the artefact shows it: the Discussion asserts *"The present case report
study reported the first case of a WWOX-related phenotype"* (L33), which is plainly false — the same
Discussion then compares four previously reported families, and the title itself says "With
Literature Review". Table 3 is headed *"Current case, 2021"* in a 2022 paper, and its row alignment
is internally inconsistent (seven `Homozygous` cells across six patient columns). The abstract
asserts the WOREE seizure phenotype as background while the body reports a seizure-free child.
🔴 **None of this is a reason to discard the observation that a homozygous `c.406A>G` was found in a
consanguineous family with a described phenotype** — that observation stands at its own weight. It
*is* a reason to require independent confirmation before the allele or the phenotype is used
load-bearingly, and to record the variant as **unclassified** rather than pathogenic.

---

### 3c · W-5 · PMID 42589397 — an independent-*sounding* test of `CLAIM 025`

**Design.** Retrospective bioinformatic analysis of **public TCGA data only** (L59): RNA-seq
(RNASeqV2, RSEM-normalised) and clinical profiles from Firehose Broad GDAC, accessed 12 January
2024. Cohorts: **TCGA-BRCA n = 390** and **TCGA-OV n = 228** (total 618), after exclusion of male
BRCA patients and any patient missing clinical data, neoplasm cancer status or follow-up. BRCA
intrinsic subtypes taken from published PAM50 calls, not re-estimated. Five analysis groups:
Basal-like, Luminal A, Luminal B, HER2-enriched, OV (L37). **No perturbation of any kind** —
no knockdown, no overexpression, no drug, no animal.

**The endpoint, and the proxy — scrutinised.** The paper's own word is **proxy**, in the abstract
(L62) and in Results (L38). Its construction:

> *"a proxy for disease-free survival (DFS) was derived using the TCGA “Person Neoplasm Cancer Status” field (treating “With Tumour” as the event and “Tumour Free” as censoring) paired with “Days to Last Follow-up” and “Days to Death.”"* (L43)

🔴 **The justification offered for the proxy is procedural, not validated.** Nowhere does the paper
show that this field tracks recurrence, nor cite a validation of it as a DFS surrogate, nor discuss
its known weaknesses: "Person Neoplasm Cancer Status" is a **status at last contact**, not a dated
recurrence event, so pairing it with "Days to Last Follow-up" assigns the event time to the
follow-up date rather than to the recurrence date — an **immortal-time / event-time misassignment**
that is not acknowledged. The event yield is the tell: **BRCA 22 events in 390 patients (5.6 %),
368 censored; OV 161 events in 228 (70.6 %), 67 censored** (L42). A 5.6 % event rate for
"disease-free survival" in a 390-patient breast cohort is implausibly low for true recurrence and
is much more consistent with a cross-sectional status field. The paper names the low event count as
a power problem (L53) but never as a **validity** problem for the endpoint itself. **The proxy is
the weakest link in the paper and it is not defended.**

**What the ratio actually predicted.**

*Kaplan–Meier, subtype-stratified, data-derived cutpoints.* Direction is **subtype-dependent and it
reverses**: *"Patients with Basal-like and HER2-enriched BRCA **tended** to show more favourable DFS
in the high-ratio group, whereas those with Luminal A, Luminal B, and OV tumours showed more
favourable DFS in the low-ratio group"*. 🔴 **"Tended" is the source's word and it stays.** 🔴 **No
log-rank statistic, no p-value and no confidence interval is reported for any KM comparison in the
body** (`grep -ic "log-rank"` = 0) — they live in a figure that is not inspectable. The paper
immediately declares them **exploratory**:

> *"Given the modest number of DFS events per subtype and the exploratory nature of the subgroup cutpoints, these effects are descriptive and hypothesis-generating rather than formally validated prognostic groupings."* (L39)

and the abstract goes further: *"The observed subtype-specific survival trends … are
**non-significant and exploratory**"* (L61). **Preserved exactly: exploratory, and non-significant.**

*Cox, continuous ratio.* This is the only place the ratio is tested with reported effect sizes:

| Cohort / model | HR | 95 % CI | p | Concordance |
|---|---|---|---|---|
| BRCA, ratio alone | **0.25** | 0.15–0.44 | `5.7 × 10^(exponent elided by extractor)` | 0.66 |
| BRCA, ratio + WWOX + HIF1A | **0.31** | 0.14–0.70 | `4.8 × 10^(exponent elided)` | — |
| OV, ratio alone | **1.11** | 0.92–1.35 | **0.27 (ns)** | 0.49 |
| OV, ratio + WWOX + HIF1A | **1.44** | 0.99–2.09 | **0.055 (borderline)** | 0.55 |

(L40, L41.) 🔴 **The direction flips between cohorts**: HR < 1 in BRCA (higher ratio → lower hazard)
and HR > 1 in OV (higher ratio → higher hazard, not significant). In the combined models *"the
individual genes lost significance"* (L40) — the ratio absorbs them, which is the paper's argument
for using a ratio at all. **OV concordance 0.49 is indistinguishable from chance.**

*Multivariable LASSO-Cox.* BRCA (n = 390, 22 events): λ ≈ 0.0138 by 10-fold CV, nine predictors
retained. **The only robustly significant predictor is clinical stage** — HR ≈ 2.78 (1.24–6.23),
p = 0.013 (L54); gene-level predictors *"showed weaker or borderline associations"*, age not
independent. Apparent C-index 0.79 (SE 0.055), likelihood-ratio p = 0.001, Wald p = 0.01, *"but
these statistics are expected to be optimistic in view of the low event count"* (L55). And then the
result that matters most:

> *"Bootstrap internal validation confirmed that the multivariable breast model has negligible validated discriminative performance: the optimism-corrected C-indices were centred close to 0 with a wide interval (approximately −0.50 to 0.46)."* (L46)

> *"these results indicate that the full-cohort LASSO-Cox model does not provide reliable prognostic discrimination for DFS in this setting and should be interpreted purely as hypothesis-generating."* (L47)

OV (n = 228, 161 events) fares better but modestly: apparent C 0.55, optimism-corrected ≈ 0.53,
interval ≈ 0.47–0.56 (L56).

**Were cutpoints subtype-specific and data-derived? — YES, and the optimism problem is only
partially addressed.**

> *"Kaplan–Meier survival curves were generated by stratifying patients into High and Low ratio groups using subtype-specific optimal cutpoints determined by maximally selected rank statistics (maxstat)."* (L44)

🔴 **Naming the problem explicitly, as the brief requires.** `maxstat` searches every candidate
threshold and keeps the one that maximises the test statistic. The resulting split is therefore
selected *on the outcome*, and its nominal p-value is anti-conservative: the reported significance
is inflated unless corrected, either by the standard maximally-selected-rank-statistic distribution
(Lausen–Schumacher), by permutation, or by an optimism-corrected resampling scheme. On top of that,
the cutpoint search was run **five times, once per subtype**, which multiplies the selection.
**Did they correct?** `grep` for `log-rank`, `multiple compar`, `multiplicity` returns **zero**;
`permutation` appears once and refers to the 10,000 permutations inside `fgsea`, not to the cutpoint
search. **So: no correction of the cutpoint selection, and no multiple-comparison adjustment across
the five subtype survival tests.** Benjamini–Hochberg FDR *is* applied — but to the differential
expression (FDR ≤ 0.05), the KEGG ORA (FDR < 0.05, displayed to 0.25) and the immune deconvolution
(FDR < 0.05), **not** to the survival analysis. Their stated mitigation is different in kind:

> *"To evaluate hazard ratios (HRs) without threshold-selection bias, univariable and multivariable Cox proportional hazards regression models were fitted using the standardized continuous ratio (Z-score, per SD change) as well as the cutpoint-stratified categorical ratio."* (L45)

That is the right instinct and it is why the continuous Cox table above is the only survival result
worth carrying. **It does not rescue the KM figures**, and the authors do not claim it does — they
label them exploratory instead (L39, L61). ✅ **Credit where due: the paper does not present the
cutpoint-derived KM result as a validated finding.** This is the *opposite* of the citation-fidelity
defect the sibling Lodz audit documented; here the hedge is preserved in the paper's own abstract.

**Does the Cox model treat the ratio as continuous and standardised? — YES**, per L45: standardised
Z-score, per SD change, in univariable and multivariable models, alongside the categorical version.
**The adjusted effect** — the ratio inside the multivariable LASSO-selected model — is *not reported
as a standalone HR with CI* in the body; what is reported is that stage dominates (L54), that
gene-level predictors are weak or borderline, and that the whole model's validated discrimination is
≈ 0 (L46). **The honest summary is: the adjusted effect of the ratio in BRCA is not separately
quantified in the retrievable text, and the model containing it does not discriminate.**

**Everything else the paper reports** — Notch-gene differential expression, KEGG ORA, Hallmark GSEA,
MCP-counter immune deconvolution, hormone-receptor target overlap — is descriptive transcriptomics
stratified by the same data-derived cutpoints, and the paper states that most pathway results *"did
not yield many pathways that survive strict FDR < 0.05 correction"* and are shown *"up to FDR < 0.25
as exploratory trends"* (L48). One self-aware detail worth crediting: HIF1A's own differential
expression between ratio groups is declared *"an internal consistency check rather than an
independent finding"* (L50), because HIF1A is in the ratio's denominator.

**What was NOT tested.** No perturbation of WWOX or HIF1A — the authors say so: *"Prospective in
vitro and in vivo functional studies—including targeted perturbations … are required to establish
direct mechanistic causality"* (L63), and *"The identified relationships … are computational and
correlated rather than causal"* (L49). No protein — the entire analysis is bulk mRNA; **no WWOX or
HIF1α protein, no HIF1α stabilisation, no hypoxia measurement, no metabolic flux, no lactate**. No
external validation cohort (METABRIC/GEO named as needed, not done). No single-cell or spatial
resolution. **No neural tissue, no neuron, no brain, no seizure, no developmental endpoint
anywhere.** And no germline WWOX genotype: the analysis measures *expression*, never allele status.

🔴 **Abstract-vs-Results check, performed as required.** There is no inversion here, but there *is*
a tension worth stating precisely. Results 2.1 says the ratio *"was strongly associated with DFS"* in
BRCA (L40); the abstract says the ratio *"does not act as a uniform or strongly predictive prognostic
marker … modest, context-dependent and statistically fragile"* (L60). These are reconcilable —
"strongly associated" is about the p-value of a single continuous covariate, "not strongly
predictive" is about discrimination (C 0.66 apparent; ≈ 0 after bootstrap correction, L46) — but a
citing author who carries only the Results sentence will overstate the paper. **The abstract is the
more conservative of the two, which is the reverse of this literature's usual failure mode, and the
correct sentence to carry is the abstract's.**

---

## 4 · VERBATIM LOCATORS

Every quote below was **programmatically re-matched against the saved artefact files** after this
table was written. Quotes are reproduced character-for-character, including the extractor's damage
(`thegene`, `theratio`, `[]`, doubled "and", elided exponents) and including its thin spaces and
non-breaking spaces. Anchors name the section as the artefact presents it; **page and line anchors
do not exist on this route.**

| # | Paper | Proposition | Exact quote (character-for-character) | Section anchor |
|---|---|---|---|---|
| `L01` | `37974179` | WES called a single homozygous exon-6 deletion | *"The WES analysis revealed a homozygous deletion involving exon 6 of thegene in the proband."* | W-3 Results → Molecular findings |
| `L02` | `37974179` | The qPCR dosage assay was consistent with the (wrong) homozygous reading | *"No amplification was seen in the proband as if he harbors a biallelic deletion of exon 6."* | W-3 Results → Molecular findings |
| `L03` | `37974179` | WGS overturned the WES call: three deletions, not one, and not two | *"Interestingly, the WGS analysis revealed also the presence of three larger deletions in thegene in the proband, not two deletions (Fig.)."* | W-3 Results → Molecular findings |
| `L04` | `37974179` | Sizes and hg38 coordinates of the three deletions as called by WGS | *"A large deletion about 177,200 bp in length involved exons 6–8 at chr16: 78331193–78,508,394 (hg38). Another deletion about 13,261 bp in length involved intron 5 at chr16: 78337740–78,351,002 (hg38). The last deletion about 53,904 bp in length involved exon 6 at chr16: 78368802–78,422,707 (hg38)."* | W-3 Results → Molecular findings |
| `L05` | `PMID 37974179` | Phase **as published in PMID 37974179 (Dong 2023)**: maternal exons 6–8; paternal intron 5 + exon 6 (note the paper's own size swap here) | *"The exons 6–8 deletion (177,204 bp) was inherited from the mother (II2), while the discontinuous deletion of intron 5(53,904 bp) and exon 6(13,260 bp) were inherited from the father (II1)."* | W-3 Results → Molecular findings |
| `L06` | `37974179` | Breakpoint junction of the exon-6 deletion carries an insertion | *"a 53,904 bp deletion (exons 6 deletion) was detected with breakpoints at 78368802 and 78,422,707, along with an ATACACACACAC insertion at the deletion junction."* | W-3 Results → Molecular findings |
| `L07` | `37974179` | The authors' own statement that WES has pitfalls for WWOX CNVs | *"While WES may encounter some pitfalls in detecting copy number variations in the WWOX gene, WGS accurately addresses intricate variant configurations and investigates potential mechanisms underlying their formation."* | W-3 Conclusion (final paragraph of Discussion) |
| `L08` | `37974179` | Consequence predicted for the exon-6 deletion allele: frameshift, truncated, loss of function | *"The exon 6 deletion (: c.517_605del, His173AlafsTer67) is a common deletion predicted to cause a frameshift mutation resulting in a truncated protein with loss of function."* | W-3 Discussion |
| `L09` | `37974179` | Consequence predicted for the exons 6–8 allele: WW domains intact, SDR disrupted, possible poor residual function — 'theoretically', 'may' | *"The exon 6–8 deletion (:c.517_1056del, His173_Met352del) theoretically produces a protein with normal WW domains, but due to the disruption of the SDR domain, it may retain poor residual function []."* | W-3 Discussion |
| `L10` | `37974179` | Age at seizure onset and semiology as recorded in Results | *"At 15 days after birth, he presented infantile seizures characterized by clenched teeth, cyanosis around the lips and tetanic twitch of the limbs"* | W-3 Results → Clinical features |
| `L11` | `37974179` | Anti-seizure medication was ineffective | *"The administration of antiepileptic drugs (sodium valproate and topiramate tablet) was not effective."* | W-3 Results → Clinical features |
| `L12` | `37974179` | EEG findings | *"Electroencephalograms (EEGs) shows slow weakened of background activity observed in both hemispheres and and polyspikes low-wave discharge in bilateral temporal lobes."* | W-3 Results → Clinical features |
| `L13` | `37974179` | MRI findings | *"Magnetic resonance imaging (MRI) showed white matter hyperintensity and delayed myelination in the brain."* | W-3 Results → Clinical features |
| `L14` | `37974179` | Age and stated cause of death; growth at death | *"He died at the age of two and a half years because of persistent seizures. At the time of death, the affected individual was 69 cm (−6SD) in height and 8 kg (−4SD) in weight."* | W-3 Results → Clinical features |
| `L15` | `37974179` | Clean in-paper negative: no R-loop forming sequences at the junctions | *"No R-loop forming sequences were found using R-loopDB to screen the sequences flanking the breakpoint junctions of the three deletions."* | W-3 Discussion |
| `L16` | `37974179` | Priority claim about onset made in Discussion | *"Our proband had the earliest onset of epilepsy, presenting on the 15th day of life."* | W-3 Discussion |
| `L17` | `37974179` | The grandfather/lung-cancer link is declared a hypothesis, not a measurement | *"we hypothesized that the heterozygousexons 6–8 deletion observed in maternal grandfather (I-3, lung cancer affected individual) caused an abnormal WWOX expression and the consequent clinical phenotype."* | W-3 Discussion |
| `L18` | `37974179` | Abstract's statement of the WES call | *"Whole exome sequencing revealed homozygous exon 6 deletion in thegene in the proband."* | W-3 Abstract → Result |
| `L19` | `37974179` | Abstract's statement of the WGS correction | *"However, using whole-genome sequencing, we identified three larger deletions (maternal allele with exon 6–8 deletion and paternal allele with two deletions in proximity one in intron 5 and the other in exon 6) involving thegene in the proband, with deletion sizes of 13,261 bp, 53,904 bp, and 177,200 bp."* | W-3 Abstract → Result |
| `L20` | `35712340` | The variant, as reported: c.406A>G, homozygous; no transcript accession given anywhere | *"WES identified the homozygous variant c.406A>G in WWOX (OMIM:605131) resulting in amino acid change (Table)."* | W-4 Case presentation |
| `L21` | `35712340` | In-silico prediction tally (15 of 21) | *"Out of 21 bioinformatic in silico experiments, 15 showed a pathogenic effect of this variant."* | W-4 Case presentation |
| `L22` | `35712340` | A splice effect was PREDICTED, never measured — mood preserved ('might lead') | *"The in silico predicted that the position of the identified variant might lead to significant alterations in mRNA splicing owing to an altered splice site."* | W-4 Case presentation |
| `L23` | `35712340` | ACMG is named as the framework; no class and no evidence codes are reported | *"Classifications of variants were conducted based on ACMG Guidelines (Richards et al.) considering database entries (inc. HGMD), Bioinformatics predictions tools, and literature status."* | W-4 Introduction |
| `L24` | `35712340` | Population frequency; never seen homozygous in gnomAD | *"The variant has been detected in 0.0042% of the general population (five heterozygous, 0 homozygous; gnomAD v2,1,1 controis) and this is the first time we detected it in our internal database in a homozygous state."* | W-4 Introduction |
| `L25` | `35712340` | The 'prenatal WES' arm is a parental-carrier/segregation confirmation | *"A parallel analysis of prenatal WES data revealed that both parents were heterozygous carriers of thevariant, confirming its homozygosity."* | W-4 Case presentation |
| `L26` | `35712340` | Consanguinity and family history | *"Upon investigating the family history, his parents were consanguineous; of his first-degree relative with four siblings, three were healthy and one was known to have seizures."* | W-4 Case presentation |
| `L27` | `35712340` | 🔴 No early seizure disorder in this patient | *"our patient presented with a global developmental delay and no early seizure disorder despite a family history of seizures and cerebral palsy in his brother and cousin, respectively."* | W-4 Discussion |
| `L28` | `35712340` | 🔴 MRI normal, no progressive microcephaly, no optic atrophy | *"Additionally, the MRI was normal, with no progressive microcephaly or bilateral optic atrophy."* | W-4 Discussion |
| `L29` | `35712340` | The authors' own hedge on the phenotype's fit to DEE28 | *"From the available information, the patient phenotype appears partially supportive of DEE28."* | W-4 Discussion |
| `L30` | `35712340` | MRI normal, stated in the case presentation | *"Brain MRI results were normal."* | W-4 Case presentation |
| `L31` | `35712340` | The only domain statement in the paper — generic architecture, no residue assignment | *"It encodes for 414 amino acid protein, with two interacting WW domains at the N-terminal with conserved proline and tryptophan residues and a short-chain dehydrogenase/reductase domain at the C-terminus [-]."* | W-4 Introduction |
| `L32` | `35712340` | The protein change, given only in the comparison table | *"P.lle136Val"* | W-4 Table 3 (flattened by the extractor) |
| `L33` | `35712340` | 🔴 Editorial defect: 'the first case of a WWOX-related phenotype' | *"The present case report study reported the first case of a WWOX-related phenotype."* | W-4 Discussion |
| `L34` | `35712340` | The paper's own limitation on genotype–phenotype inference | *"WWOX genotypes appeared to correlate with the severity and onset of seizures and spasticity in the studied cases. However, studies on more patients are needed to establish accurate genotype-phenotype correlations."* | W-4 Discussion |
| `L35` | `35712340` | Developmental status at 21 months | *"Currently, at the age of 21 months, he can say 10 words but not complete sentences, climb stairs with assistance, walk, and run with recurrent falling."* | W-4 Case presentation |
| `L36` | `35712340` | Liver panel as stated in text (contradicted by its own Table 1 for ALT/GGT) | *"Liver profiles, including ALT and GTT, were normal, whereas AST, albumin, total bilirubin, and direct bilirubin levels were high, and globulin level was low."* | W-4 Case presentation |
| `L37` | `42589397` | Design: 618 patients, five groups, subtype-specific optimal cutpoints | *"A total of 618 patients were included and categorized into distinct molecular groups (Basal-like, Luminal A, Luminal B, HER2-enriched, and OV), then stratified into high and lowratio groups using subtype-specific optimal cutpoints ()."* | W-5 Results 2.1 |
| `L38` | `42589397` | The endpoint is a proxy, and the paper says so in Results | *"Survival analysis using neoplasm cancer status as a proxy for disease-free survival (DFS) revealed context-dependent associations betweenratio status and clinical outcomes."* | W-5 Results 2.1 |
| `L39` | `42589397` | The KM subgroup effects are declared descriptive and hypothesis-generating | *"Given the modest number of DFS events per subtype and the exploratory nature of the subgroup cutpoints, these effects are descriptive and hypothesis-generating rather than formally validated prognostic groupings."* | W-5 Results 2.1 |
| `L40` | `42589397` | BRCA continuous-ratio Cox: effect size, CI, concordance (p-value exponent elided by the extractor) | *"In BRCA, the ratio was strongly associated with DFS (HR 0.25, 95% CI 0.15–0.44,= 5.7 × 10; concordance 0.66) and remained significant in the combined model withand(HR 0.31, 95% CI 0.14–0.70,= 4.8 × 10), whereas the individual genes lost significance."* | W-5 Results 2.1 |
| `L41` | `42589397` | OV continuous-ratio Cox: not significant; combined model borderline | *"In OV, the ratio was not significantly associated with DFS in the single-predictor model (HR 1.11, 95% CI 0.92–1.35,= 0.27; concordance 0.49) and showed only a borderline association in the combined model (HR 1.44, 95% CI 0.99–2.09,= 0.055; concordance 0.55), indicating weaker prognostic value in that cohort ()."* | W-5 Results 2.1 |
| `L42` | `42589397` | Event counts — 22 events in 390 BRCA; 161 in 228 OV | *"resulting in final DFS-proxy cohorts of 390 BRCA patients (22 events, 368 censored) and 228 OV patients (161 events, 67 censored), detailed in."* | W-5 Methods 5.1 |
| `L43` | `42589397` | Exact construction of the DFS proxy | *"a proxy for disease-free survival (DFS) was derived using the TCGA “Person Neoplasm Cancer Status” field (treating “With Tumour” as the event and “Tumour Free” as censoring) paired with “Days to Last Follow-up” and “Days to Death.”"* | W-5 Methods 5.1 |
| `L44` | `42589397` | Cutpoints are data-derived by maximally selected rank statistics | *"Kaplan–Meier survival curves were generated by stratifying patients into High and Low ratio groups using subtype-specific optimal cutpoints determined by maximally selected rank statistics (maxstat)."* | W-5 Methods 5.5 |
| `L45` | `42589397` | Their stated mitigation for threshold-selection bias: a standardised continuous ratio | *"To evaluate hazard ratios (HRs) without threshold-selection bias, univariable and multivariable Cox proportional hazards regression models were fitted using the standardized continuous ratio (Z-score, per SD change) as well as the cutpoint-stratified categorical ratio."* | W-5 Methods 5.5 |
| `L46` | `42589397` | 🔴 Bootstrap optimism correction destroys the BRCA multivariable model's discrimination | *"Bootstrap internal validation confirmed that the multivariable breast model has negligible validated discriminative performance: the optimism-corrected C-indices were centred close to 0 with a wide interval (approximately −0.50 to 0.46)."* | W-5 Results 2.6.1 |
| `L47` | `42589397` | The authors' own verdict on that model | *"these results indicate that the full-cohort LASSO-Cox model does not provide reliable prognostic discrimination for DFS in this setting and should be interpreted purely as hypothesis-generating."* | W-5 Results 2.6.1 |
| `L48` | `42589397` | Pathway results largely fail FDR<0.05; displayed to FDR<0.25 as exploratory trends | *"Across subtypes, the KEGG and Hallmark analyses did not yield many pathways that survive strict FDR < 0.05 correction; instead, we highlight the most strongly enriched pathways up to FDR < 0.25 as exploratory trends"* | W-5 Discussion |
| `L49` | `42589397` | The relationships are correlational, not causal — the authors' words | *"The identified relationships among metabolic programmes, immune microenvironments, and Notch signalling are computational and correlated rather than causal."* | W-5 Study Limitations |
| `L50` | `42589397` | HIF1A's own differential expression is an internal consistency check, not a finding | *"contributes directly to the ratio definition, its differential expression is expected and serves as an internal consistency check rather than an independent finding."* | W-5 Results 2.2 |
| `L51` | `42589397` | Relationship to their own prior OS paper | *"while our previous work established the baseline prognostic association of theratio with overall survival (OS) [], across TCGA breast and ovarian macro-cohorts, the present study represents a distinct extension."* | W-5 Introduction |
| `L52` | `42589397` | 🔴 Same datasets as their prior analysis, re-endpointed — not an independent cohort | *"As in our OS-focused analysis, we use the same TCGA BRCA and OV carcinoma datasets, but here we reanalyse them with neoplasm cancer status as a DFS-proxy endpoint and incorporate new layers of Notch, immune and hormone-related profiling."* | W-5 Introduction |
| `L53` | `42589397` | Subtype analyses are power-limited and exploratory | *"Subtype-specific analyses were strictly constrained by very low DFS event counts (for example, Luminal A: n = 181)."* | W-5 Results 2.6.2 |
| `L54` | `42589397` | The only robust multivariable predictor is clinical stage, not the ratio | *"Advanced stage remained significantly associated with increased hazard (HR ≈ 2.78; 95% CI 1.24–6.23;= 0.013)"* | W-5 Results 2.6.1 |
| `L55` | `42589397` | Apparent C-index 0.79 is declared optimistic by the authors | *"The apparent C-index of this model was 0.79 (SE 0.055), and global tests reached significance (likelihood ratio= 0.001; Wald= 0.01) (), but these statistics are expected to be optimistic in view of the low event count."* | W-5 Results 2.6.1 |
| `L56` | `42589397` | OV bootstrap validation: moderate, not strong | *"Bootstrap internal validation yielded an apparent C-index of 0.55 and an optimism-corrected C-index of approximately 0.53, with a bootstrap interval of about 0.47–0.56, indicating moderate but not strong discriminative performance."* | W-5 Results 2.6.3 |
| `L57` | `42589397` | Immune finding in basal-like BRCA | *"In basal-like BRCA, monocyte-lineage populations were significantly enriched in tumours with lowerratios."* | W-5 Results 2.4.1 |
| `L58` | `42589397` | Clean negative: no immune/stromal differences in OV, HER2-enriched, Luminal B | *"In ovarian carcinoma, as well as HER2-enriched and Luminal B BRCA subtypes, no significant differences were observed across the evaluated immune and stromal cell populations (all FDR > 0.05)."* | W-5 Results 2.4.3 |
| `L59` | `42589397` | Single-source data: TCGA only | *"all transcriptomic and clinical survival analyses derive exclusively from the public Cancer Genome Atlas (TCGA) repository [] using uniformly processed Firehose data."* | W-5 Study Limitations |
| `L60` | `42589397` | 🔴 The abstract's own verdict: not a uniform or strongly predictive marker; statistically fragile | *"Theratio does not act as a uniform or strongly predictive prognostic marker but instead delineates distinct biological states whose association with DFS is modest, context-dependent and statistically fragile in TCGA."* | W-5 Abstract |
| `L61` | `42589397` | 🔴 The abstract declares the subtype survival trends non-significant and exploratory | *"The observed subtype-specific survival trends (high-ratio favourability in basal/HER2, low-ratio favourability in luminal A,B and OV) are non-significant and exploratory, and all ratio-based survival patterns require confirmation in independent cohorts and functional studies."* | W-5 Abstract |
| `L62` | `42589397` | 'proxy' is the abstract's own word | *"using neoplasm cancer status as a proxy for disease-free survival (DFS)"* | W-5 Abstract |
| `L63` | `42589397` | Perturbation experiments are named as still required | *"Prospective in vitro and in vivo functional studies—including targeted perturbations ofand, manipulation of key Notch pathway components, and functional metabolic and immune assays- are required to establish direct mechanistic causality."* | W-5 Study Limitations |
| `L64` | `35712340` | Abstract's statement of the prenatal-WES arm | *"This variant of WWOX was also observed in the prenatal WES data, indicating that both parents were heterozygous carriers and the detected variant was homozygous."* | W-4 Abstract |

**RE-MATCH RESULT: 64/64 exact, zero mismatches.** Verification method: each quote was
first tested as a literal substring of the artefact; quotes that failed were re-matched with a
whitespace-class pattern (` `, U+00A0, U+2009, U+202F, U+200A interchangeable) against the artefact
and **replaced in this table by the exact string the artefact contains**, then re-tested as literal
substrings. 16 of the 64 needed that repair — all 16 were whitespace-encoding differences introduced
by transcription, none was a wording error. Final pass: 64/64 literal substring matches.

---

## 5 · NEGATIVE RESULTS — explicit and prominent

### From W-3 (37974179)
- 🔴 **No RNA was measured.** No transcript assay of any kind exists in this paper. The predicted
  consequences of both alleles (L08, L09) are **predictions**.
- 🔴 **No protein was measured.** No Western blot, no antibody, no abundance, no localisation, no
  activity. **The exons 6–8 allele's "poor residual function" is theoretical and unobserved.**
- 🔴 **No head circumference reported** — microcephaly is neither established nor excluded in this
  child.
- **No corpus callosum abnormality, no cerebral atrophy and no optic atrophy reported** on this
  proband's MRI, though all three are named as typical in the Introduction. **Not reported ≠ absent**
  — a single MRI description in a case report is not a systematic assessment.
- ✅ **A real in-paper negative:** *"No R-loop forming sequences were found using R-loopDB to screen
  the sequences flanking the breakpoint junctions of the three deletions."* (L15) — about deletion
  **mechanism**, not about WOREE.
- **Anti-seizure medication failed**: valproate + topiramate *"was not effective"* (L11). A negative
  therapeutic datum at n = 1.
- **The confirmatory qPCR dosage assay failed to detect the error** (L02) — a negative about method,
  and the most transferable one in the paper.

### From W-4 (35712340)
- 🔴 **No functional work whatsoever.** No protein, no RNA, no cells, no constructs, no assay.
- 🔴 **The predicted splice effect was never tested** (L22) — so it is unknown whether `c.406A>G`
  behaves as a missense or a splice allele.
- 🔴 **No ACMG classification and no evidence codes** are reported for this variant (L23). It is
  **unclassified** in this source.
- 🔴 **No transcript accession** — the `c.` numbering cannot be anchored.
- 🔴 **No domain assignment for residue 136** anywhere in the paper (L31 is the only domain sentence).
- **No seizures** (L27); **normal MRI** (L28, L30); **no progressive microcephaly**; **no optic
  atrophy**; patient **alive**. These are reported observations at 21 months, not lifetime
  exclusions — a seizure-free 21-month-old may still develop seizures.
- **Affected relatives were not genotyped**; segregation stops at the parents.
- **No prenatal phenotype, imaging or outcome** is reported despite the "prenatal WES" wording (L25).

### From W-5 (42589397)
- 🔴 **No perturbation, therefore no causal claim** — the authors say so twice (L49, L63).
- 🔴 **No protein measured** — WWOX and HIF1α are mRNA throughout. HIF1α is a protein regulated
  post-translationally by oxygen-dependent degradation; **`HIF1A` transcript is a poor proxy for
  HIF1α activity**, and the paper measures no hypoxia marker, no HIF1α stabilisation and no
  metabolic flux.
- 🔴 **No neural, developmental or seizure endpoint of any kind.**
- 🔴 **The ratio is NOT prognostic in ovarian carcinoma**: HR 1.11 (0.92–1.35), p = 0.27, concordance
  0.49 (L41). This is a clean negative in the larger-event cohort (161 events vs 22).
- 🔴 **The breast multivariable model has no validated discrimination**: optimism-corrected C-index
  centred close to 0, interval ≈ −0.50 to 0.46 (L46, L47).
- **No immune or stromal differences** in OV, HER2-enriched or Luminal B (all FDR > 0.05) (L58);
  neutrophils not different in basal-like or Luminal A either.
- **Most pathway results do not survive FDR < 0.05** (L48).
- **No external validation cohort** was run (L59; METABRIC/GEO named as future work).
- **Subtype KM comparisons report no test statistic at all** in the retrievable text.

---

## 6 · Genotype transferability

| Class | W-3 (37974179) | W-4 (35712340) | W-5 (42589397) |
|---|---|---|---|
| **null / null** | **Touches it only as the error state.** The WES call implied frameshift-null on both alleles (L01, L08); WGS showed that was wrong (L03). So this paper is evidence about **how a proband can be misassigned into this class**, not evidence about the class. | ✗ | ✗ |
| **splice / null** | ✗ — no splice allele. | ✗ — but see below: the paper cannot exclude that its "missense" allele is a splice allele (L22), so it cannot cleanly populate *any* class. | ✗ |
| **splice / missense** | ✗ | ✗ | ✗ |
| **missense / missense** | ✗ | **Touches it — weakly.** One homozygous `c.406A>G` / `p.Ile136Val` in a consanguineous family (L20, L32), **unclassified (L23)**, **no transcript reference**, **no domain assignment**, **splice behaviour untested (L22)**, **no functional data**, and a phenotype the authors call only *"partially supportive"* (L29). **It is a genotype–phenotype data point and nothing more.** | ✗ |
| **residual-protein** | **Touches it as a prediction only.** The exons 6–8 allele *"theoretically produces a protein with normal WW domains … may retain poor residual function"* (L09). **No protein was measured, so this paper adds no empirical residual-protein evidence** — it adds a hypothesis with a stated allele. | ✗ — nothing measured. | ✗ |
| **large deletion / CNV** | **Touches it centrally, and constrains it.** Three deletions, base-resolution breakpoints, phase established by gap PCR (L04, L05, L06), plus the method-level finding that **exome CNV calling misrepresented all of it** (L01→L03, L07). 🔴 **It also shows the class is not homogeneous**: "exon 6 deletion" (frameshift, L08) and "exons 6–8 deletion" (in-frame, SDR-removing, L09) have different predicted consequences and were conflated by the exome caller. | ✗ | ✗ |

🔴 **W-5 touches no WOREE genotype class at all.** It measures **expression** in tumour tissue and
never germline allele status; a low WWOX/HIF1A ratio in a breast tumour is not a WWOX genotype and
carries no information about biallelic germline loss.

---

## 7 · `CLAIM 025` verdict

### One word: **QUALIFY**

**One sentence.** This paper supports `CLAIM 025`'s *architectural* proposition — that the
WWOX/HIF1A ratio behaves as a composite index of biological state rather than a single-gene readout
— while **undercutting its implicit directionality and its strength**, because the ratio's
association with outcome **reverses sign between tumour lineages**, is **not significant at all in
the larger-event ovarian cohort**, and survives bootstrap optimism correction with **negligible
discrimination**.

**Justification, itemised.**

1. **What genuinely supports the claim.** The ratio outperformed its two components: in the combined
   BRCA model *"the individual genes lost significance"* while the ratio did not (L40). That is a
   direct, independent-of-context argument for using a **ratio** rather than either transcript
   alone, and it is the part of `CLAIM 025` that is strengthened. The paper's own framing — a
   *"context-dependent molecular index"* integrating hypoxia, immune and hormone-related states — is
   close in spirit to `CLAIM 025`'s "systems-level marker of maladaptive biological state".
2. **What qualifies it — the sign is not invariant.** `CLAIM 025` derives from GDM leukocytes where
   **low ratio = maladaptive**. Here, low ratio is associated with **worse** DFS in basal-like and
   HER2-enriched BRCA but **better** DFS in Luminal A, Luminal B and OV. A "marker of maladaptive
   state" whose direction flips by context is a *state descriptor*, not a *severity index*. 🔴 This
   directly constrains any LEGEND use of the ratio in which "lower is worse" is assumed.
   It also happens to be consistent with the boundary `CLAIM 025` already carries from PMID 29724996
   (*"the gene set that reports it is not fixed"*) — now extended from the **reporter gene set** to
   the **sign of the association itself**.
3. **What undercuts it — statistical fragility, in the paper's own words.** *"non-significant and
   exploratory"* (L61); *"does not act as a uniform or strongly predictive prognostic marker …
   statistically fragile"* (L60); optimism-corrected C-index *"centred close to 0"* (L46);
   OV concordance 0.49 (L41); cutpoints data-derived with **no correction** for the selection or for
   five parallel subtype tests. 🔴 **The endpoint itself is a proxy the paper never validates** (§ 3c).
4. **Net.** Not SUPPORT, because the only thing corroborated is the ratio's superiority over its own
   components, and it is corroborated in a context `CLAIM 025` does not target. Not UNDERCUT, because
   nothing here contradicts the GDM observation — a different tissue with a different sign is not a
   refutation. **QUALIFY**, with the qualifier being *directionality is context-dependent and the
   effect is fragile.* `Status: in observation` is the right status and this reading does not change
   it. **No claim edit is proposed; this file is read-only.**

### 🔴 Transferability must be argued, not assumed

**What would have to be true for a tumour result to bear on a non-tumoral CNS claim:**

| Requirement | Does W-5 provide it? |
|---|---|
| **(a)** The quantity must be measurable and meaningfully variable in **non-tumoral** tissue. | **No.** TCGA only (L59); every sample is a tumour. |
| **(b)** The **direction** of the WWOX→HIF1A relation must be conserved across tissues with different baseline oxygen, metabolic and proliferative set-points. | **No — it refutes conservation.** The sign flips across five lineages *within one study* (L40 vs L41, and the KM directions). If it is not conserved across tumour lineages, conservation into brain cannot be assumed. |
| **(c)** The measured layer must be the one the CNS claim is about (protein/activity, not transcript). | **No.** Bulk mRNA only; no HIF1α protein, no stabilisation, no hypoxia marker, no flux. |
| **(d)** A **neural or developmental endpoint** must exist. | **No.** None anywhere in the paper. |
| **(e)** **Causality** must be established, or the claim must be explicitly restricted to association. | **No** — and the authors state this themselves (L49, L63). |
| **(f)** A tumour-specific confound must be excluded: **WWOX spans FRA16D** and is somatically deleted or silenced in a large fraction of breast and ovarian tumours, so tumour WWOX mRNA partly reads **genomic instability at a fragile site**, not a regulated physiological state. | **No.** The confound is never raised; no copy-number covariate is included. 🔴 **This is the single strongest reason a tumour WWOX/HIF1A ratio cannot be equated with a physiological one.** |

**Conclusion on transferability: none of the six conditions is met.** The paper provides **zero**
licence to move this result toward a CNS claim. Its value to LEGEND is entirely negative and
directional: it tells the model **not** to assume the ratio's sign is universal.

### Corroboration weight — the affiliation check, performed verbatim

Affiliations retrieved from PubMed metadata, quoted exactly:

| Paper | Authors | Affiliation (verbatim) |
|---|---|---|
| **42589397** (W-5) | Hammouz RY; Maciejek K; **Bednarek AK** | *"Department of Molecular Carcinogenesis, Medical University of Lodz, Żeligowskiego 7/9, 90-752 Lodz, Poland."* (all three authors) |
| **35328751** | Baryła I; Styczeń-Binkowska E; Płuciennik E; Kośla K; **Bednarek AK** | *"Department of Molecular Carcinogenesis, Medical University of Lodz, 90-752 Lodz, Poland."* (all five authors) |
| **33520443** | Baryla I; Pluciennik E; Kośla K; Wojcik M; Zieleniak A; Zurawska-Klis M; Cypryk K; Wozniak LA; **Bednarek AK** | *"Department of Molecular Carcinogenesis, Medical University of Lodz, Lodz, Poland."* (first, second, third and last authors; the others are Structural Biology / Internal Diseases and Diabetology at the same university) |

> ### 🔴 **YES — it is the same group. Same department, same institution, same senior author (Bednarek AK) on all three. Therefore this paper CANNOT raise the corroboration weight of the HIF1A branch, and `DL-MECH-020`'s weight of *one* stands unchanged.**

**And it is worse than merely same-group, in a way that matters.** The paper states that it reuses
its own prior cohorts:

> *"As in our OS-focused analysis, we use the same TCGA BRCA and OV carcinoma datasets, but here we reanalyse them with neoplasm cancer status as a DFS-proxy endpoint and incorporate new layers of Notch, immune and hormone-related profiling."* (L52)

> *"while our previous work established the baseline prognostic association of theratio with overall survival (OS) [], across TCGA breast and ovarian macro-cohorts, the present study represents a distinct extension."* (L51)

🔴 **So this is not an independent replication even of the same group's own earlier result: it is the
same data, re-endpointed.** Same lab, same patients, same expression matrix, a different outcome
field. Under any reasonable accounting that is **zero added independent observations** — it adds a
*new analysis*, not a *new test*. **Corroboration weight after this reading: still one.**
(Recorded here as a finding; no ledger edit is made. `DL-MECH-020`'s own sentence — *"Peso di
corroborazione: uno."* — is quoted verbatim in § 0, from `discovery_ledger_current.md:457`.)

---

## 8 · Therapeutic classification of anything intervention-like

| Item | Paper | Classification | Why |
|---|---|---|---|
| Sodium valproate + topiramate | W-3 | **GENERAL SYMPTOMATIC** | Standard anti-seizure medication; *"was not effective"* (L11) at n = 1. A negative therapeutic observation, not a mechanism. |
| WGS + gap PCR breakpoint resolution | W-3 | **not an intervention — diagnostic method** | Classified here only because it is the paper's actionable output. It changes **how a genotype is assigned**, not what is done to a patient. |
| WES as an early diagnostic test in consanguineous populations | W-4 | **not an intervention — diagnostic recommendation** | The paper's only actionable recommendation. 🔴 Note the irony against W-3: W-4 recommends exome-first, W-3 documents exome failure for this gene. |
| *"strategies targeting hypoxia pathways, metabolic dependencies, or macrophage-driven immune evasion"* | W-5 | **NOT TRANSFERABLE TO WOREE** | Hypothetical, un-named, tumour-context, derived from correlational data with no perturbation (L49, L63), in tissue whose WWOX loss is somatic and fragile-site-driven. It is at best **MECHANISTIC PROBE ONLY** in oncology, and **nothing** in a WWOX-deficient developing brain. |
| The WWOX/HIF1A ratio as a biomarker | W-5 | **MECHANISTIC PROBE ONLY** (in tumour); **NOT TRANSFERABLE TO WOREE** as stated | The paper itself calls it exploratory (L39, L60, L61) with negligible validated discrimination (L46). |

🔴 **No compound, dose, route, schedule or target is proposed by this reading.** Nothing here is
medical advice.

---

## 9 · INFORMATION GAIN

| Item | Y/N | One line |
|---|---|---|
| **Mechanistic graph** | **NO** | Nothing mechanistic was measured in any of the three papers — W-3 and W-4 are DNA-only case reports, W-5 is correlational bulk mRNA with no perturbation (L49, L63); the only graph-adjacent result is a *constraint* on an existing non-CNS node (the ratio's sign is not invariant), which is logged under Uncertainty rather than as a new edge. |
| **Therapeutic hypothesis** | **NO** | No candidate, no target, no lever. The only intervention reported is a failed standard anti-seizure regimen (L11), and W-5's therapeutic sentence is hypothetical and tumour-bound. |
| **Experimental roadmap** | **YES** | **(i)** The guardrail W-3 implies is already written into `DL-MECH-053`'s *Esperimento/procedura proposta*, so it is **re-confirmed, not new**. **(ii)** Genuinely new: the untested question W-4 leaves open — does `c.406A>G` alter splicing, as predicted (L22)? — is answerable by RT-PCR or a minigene and would decide whether this allele belongs in **missense/missense** or in a **splice** class at all; no such assay exists for this variant anywhere. **(iii)** Housekeeping, not science, but blocking: `CORPUS-STUB-096` / `LIT-0118` say unread while `DL-MECH-053` says read-in-full, and the dossier it cites is not in this tree — that needs an operator decision (§ 0). |
| **Genotype stratification** | **YES, but weaker than it looked** | 🔴 **W-3's stratification lesson was already held** as `DL-MECH-053` (`promoted-to-CC`), title and all — so this is **corroboration by independent re-reading, not new information** (§ 0). What is new: a verifiable artefact and 19 re-matched locators for a lead that had neither in this checkout, plus a flagged discrepancy between the lead's allele descriptors (*"allele di sito accettore"*, *"allele missense"*) and the source. W-4 adds one genuinely new but thin, unclassified missense/missense point with a seizure-free, normal-MRI phenotype (L27, L28) — and it cannot even be assigned to that class with confidence, because the predicted splice effect was never tested (L22). |
| **Intervention ranking** | **NO** | Nothing ranks, reranks or removes any therapeutic candidate. |
| **Uncertainty** | **YES** | Three distinct updates: **(a)** exome-derived WWOX genotype classes carry a documented, non-hypothetical misassignment risk, and orthogonal exon-targeted confirmation does not remove it — *already held, now verifiable*; **(b)** `c.406A>G` is unclassified, un-anchored to a transcript, undomained and possibly a splice allele — its genotype class is genuinely unknown, not merely unrecorded; **(c)** the WWOX/HIF1A ratio's association with outcome **changes sign by context** and is statistically fragile in its largest test to date, so any LEGEND use presuming "lower is worse" must now carry that caveat. |

🔴 **An honest accounting, revised downward after the § 0 correction: four of the six mission axes
gain nothing, and the fifth gains less than it first appeared.** The batch's real yield is
**(1)** one thin, genuinely new genotype datum (W-4) that cannot be confidently classed;
**(2)** one directional caveat on a live claim (W-5) — the ratio's sign is not invariant — together
with the finding that W-5 **adds zero independent observations** to the HIF1A branch;
**(3)** independent verification, with a fingerprinted artefact and re-matched locators, of a
`promoted-to-CC` lead that had neither in this checkout; and **(4)** one flagged inconsistency
between that lead's allele descriptors and its source. **The single most useful thing this session
produced was the correction against its own § 0**, which only happened because a sibling actor's
rule — `NO RECORD MATCHED` ≠ `NOT HELD` — arrived mid-reading and was applied instead of ignored.
**No claim was manufactured to show productivity.**

---

## 10 · DEFAULTS_TAKEN

1. **Persistence route.** Bodies were first written by hand from the tool return, then **re-derived
   from the tool's own persisted JSON and overwritten**, so the artefacts are byte-identical to the
   extractor output. The hand copies differed only by a trailing newline (W-3, W-4) and not at all
   (W-5); this is reported rather than quietly fixed.
2. **Abstract sidecars.** The brief said "persist every retrieved body". I also persisted the three
   **abstracts** as separate files, because six of the sixty-four locators are abstract sentences
   and a locator that cannot be re-matched against a saved artefact cannot be receipted. Abstracts
   are kept **separate from** the bodies so no body fingerprint is contaminated.
3. **Whitespace repair of quotes.** Sixteen quotes initially failed literal re-match because the
   extractor emits U+00A0 and U+2009 where I transcribed U+0020. I re-matched them with a
   whitespace-class pattern and **replaced my text with the artefact's exact string**. No wording
   was changed; the repaired quotes were then re-tested as literal substrings and all passed.
4. **Elided p-value exponents are written as `10^(exponent elided)`**, never resolved, never guessed,
   never dropped.
5. **`p.Ile136Val` is reported as `P.lle136Val`'s intended reading**, on the grounds that the
   extractor renders capital I as lowercase l; the raw string is quoted in the locator table so the
   reader can judge.
6. **Domain assignment for W-4's residue 136 was NOT computed.** The brief permitted saying "the
   paper does not say"; the paper does not say, so that is what is recorded.
7. **Table 3 of W-4 is used for exactly one cell** (`Amino acid change` / `Current case`), because
   the flattened rendering makes column alignment unreliable; this is stated in § 1.
8. **I ran a plain `grep` sweep over `disease-models/` that the brief did not ask for**, after a
   sibling actor's correction established `NO RECORD MATCHED` ≠ `NOT HELD`. **The two large
   registries were excluded from that sweep**, so CLAUDE.md's prohibition is intact — they were
   covered by `registry_records.py`, as required. The sweep overturned two statements I had already
   written (§ 0), including the premise that W-3 was unread. **Both corrections are left visible with
   the reasoning, not silently edited out.**
8b. **I did not repair the stale `CORPUS-STUB-096` / `LIT-0118` statuses, nor the `DL-MECH-053`
   allele-descriptor discrepancy, nor the missing dossier reference.** All three are canonical or
   research-layer surfaces and this actor is read-only; they are raised for the operator instead.
8c. **I did not decide whether the `DL-MECH-053` descriptor discrepancy is a scientific error or a
   de-identification artefact.** Both readings are stated and the choice is left to the operator,
   because the public edition demonstrably substitutes reference-genotype class names elsewhere.
9. **Arithmetic I performed myself** (deletion-span sums, the nesting of the two published deletions
   inside the larger published span in **PMID 37974179**, the `c.409+1` adjacency in W-4) is
   labelled as mine at each occurrence and is never attributed to the papers. Every inheritance
   statement in this file describes the published pedigree of **PMID 37974179** and nothing else.
10. **"Not measured" was never converted to "absent"**, and hedged verbs (*theoretically*, *may
    retain*, *tended*, *might lead*, *exploratory*, *proxy*, *partially supportive*) are reproduced
    with their mood intact throughout.
11. **No canonical file was touched.** No receipt was written; a receipt for these three readings is
    now *possible* because § 1 gives the fingerprints it would be taken against, but writing one is
    outside this actor's mandate.

---

## 11 · Receipt status and the `DL-MECH-053` evidence base

**Appended 2026-09-21 by Scientist B acting as RECEIPT VERIFIER, not as the reader.** The three
readings reported above were performed earlier today under a read-only brief that omitted **step 7
of the paper-processing pipeline — "create receipt"** (the omission is recorded at
[`full_text_queue_current.md`](../research/full_text_queue_current.md) entry **`FT-114`**). § 10
item 11 above states the gap in the reader's own words. This section closes it and records what the
closing did and did not establish. **Nothing in this section edits any registry, ledger or claim.**

### 11.1 The receipts now on the ledger

Written one JSON at a time and appended **only** through the validated writer
`framework/scripts/fulltext_receipts.py record`; `verify` was run before the first append and after
every single one. **Ledger 188 → 193 chained receipts, `OK` at every step.** The writer computed
each `ledger_prev_hash` and re-anchored `framework/state/state_manifest_current.md`
(`fulltext_ledger_events: 188 → 193`) by itself — **the anchor was not hand-edited, and neither was
the ledger.**

| Paper | `event_id` | Depth | Artefact sha256 | Locators re-matched by the verifier |
|---|---|---|---|---|
| W-3 · `37974179` | `FTR-20260921-37974179-01` | `partial_fulltext_read` | `50a6174f…2ef979fb` | **19/19 exact** (L01–L19; 17 body + L18/L19 abstract sidecar) |
| W-4 · `35712340` | `FTR-20260921-35712340-01` | `partial_fulltext_read` | `777ca3f9…d616355e` | **18/18 exact** (L20–L36, L64; 17 body + L64 sidecar) |
| W-5 · `42589397` | `FTR-20260921-42589397-01` | `partial_fulltext_read` | `572a7e6b…c43e6e16` | **27/27 exact** (L37–L63) |

**Zero unmatched. Zero whitespace-only near-misses** — every failed literal was re-tested with a
U+0020/U+00A0/U+2009/U+202F/U+200A-interchangeable pattern and that pattern fired on nothing,
confirming § 4's declared repair of 16 quotes had already been written back into the table as the
exact artefact strings. 64/64 for this file, independently reproduced.

🔴 **Why `partial_fulltext_read` and not `complete`, for all three.** Three independent reasons,
each sufficient: no deep-dive work manifest exists at
`disease-models/wwox/research/deepdive_manifests/PMID<pmid>.json` for any of the three, so
`require_work_manifest` makes `complete_fulltext_read` **mechanically unavailable**, not merely
unclaimed; the **reference list is absent** from every artefact (§ 1.4), so no multi-hop expansion
was possible; and **no figure image was inspectable and no supplementary content was retrieved**
(§ 1.5). Under-claiming is the safe direction and it is the one taken. Coverage was derived from
§ 4's locator table and this file's prose, cross-checked against each artefact's own heading
structure; no section was upgraded to `read` on a general assertion of full reading.

### 11.2 The `staging/` dossier cited by `DL-MECH-053`

`DL-MECH-053` (`discovery_ledger_current.md:1340`, status `promoted-to-CC`) cites
`staging/deepdive_PMID37974179_Dong2023.md`. **`disease-models/wwox/research/staging/` does not
exist in this tree**, and the string `deepdive_PMID37974179` occurs in exactly one file — the ledger
entry that cites it.

🔴 **This is reported as ABSENT FROM THIS TREE, which is not the same as lost.** Per
`reading_state.py`'s own header warning, a count taken over unmerged state is not evidence of
absence: that dossier may sit on an **unmerged branch** or in the **private edition**, both of which
are ordinary and expected. **No conclusion is drawn about whether it exists.** What *is* now true
and was not true this morning: `37974179` has a receipt and a fingerprinted artefact in this tree,
so `DL-MECH-053`'s main-text statements are checkable here regardless of where that dossier lives.

### 11.3 🔴 The allele-descriptor discrepancy — stated, not resolved

`DL-MECH-053`'s DATO line describes the proband as carrying
*"un allele di sito accettore `del ex6-8` e un allele missense"*.

**PMID 37974179 describes neither.** It describes an **in-frame genomic deletion of exons 6–8**
(`c.517_1056del`, `His173_Met352del` — `L09`) on the maternal allele, and **two discontinuous
genomic deletions** (intron 5 and exon 6 — `L05`, `L06`) on the paternal allele. There is no
splice-acceptor variant and no missense variant anywhere in the paper. All 19 locators re-match the
fingerprinted artefact exactly, so this is not a transcription question about the source.

**Two readings are open and both are plausible:**

| Reading | What it would mean | What supports it |
|---|---|---|
| **(a) Scientific error** | The lead assigns this proband to two genotype classes the source does not support, and the assignment should be corrected at the ledger. | The descriptors are flatly contradicted by the paper's own text, and the lead is `promoted-to-CC` — i.e. already load-bearing. |
| **(b) De-identification substitution artefact** | *"allele di sito accettore"* and *"allele missense"* are precisely the two class names the **public edition** uses for the reference genotype; the substitution would have been introduced when the private record was rewritten for this edition, leaving the private text correct. | The public edition demonstrably substitutes reference-genotype class names elsewhere, and the rest of `DL-MECH-053` — the WES/qPCR-vs-WGS inversion, *"nessun RNA, proteina o funzione"*, residual function *"soltanto predetta"*, even the published size-swap defect — is **confirmed character-for-character** by this reading. A lead that accurate elsewhere is unlikely to have simply invented two allele classes. |

🔴 **I do not choose between them, and no ledger was edited.** The two readings imply opposite
repairs — (a) corrects the ledger, (b) corrects the de-identification mapping and leaves the science
alone — and only the Operator can see both editions. **OPERATOR DECISION.** Recorded here so the
question is visible on a surface a reader of this reading will reach.

---

*Non-canonical analysis file. Read-only toward every canonical registry, ledger, claim and current
file. No commit candidate. Not medical advice.*
