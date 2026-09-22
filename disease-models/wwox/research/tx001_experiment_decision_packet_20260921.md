# TX-001 — experiment decision packet: the missing biological denominator

> **What this is.** `TX-001` proposes correcting a canonical splice-acceptor allele and names its
> efficacy endpoint as the fraction of correctly spliced transcript. A bounded census
> (`wwox_splice_transcript_census_20260921.md`, reading `FTR-20260921-39101447-01`) established that
> **no aberrant:normal ratio exists for any WWOX allele, in any tissue, anywhere in the literature.**
> The strategy has an endpoint with no baseline to measure against. That is a scientific gap, not a
> harness gap, and this packet specifies the smallest experiment that closes it.
>
> **READ-ONLY toward every canonical file. Nothing here is medical advice, and nothing here is a
> treatment proposal.** It is an assay design.

---

## A · EXPERIMENTAL QUESTION

**In donor-derived cells carrying a canonical WWOX splice-acceptor allele, what fraction of WWOX transcript is correctly spliced across the affected junction, what is the aberrant species, and how much of the aberrant transcript is being hidden by nonsense-mediated decay?**

---

## B · MINIMAL DESIGN

### B.1 Sample and matrix
- **Donor-derived dermal fibroblasts** (or LCL) carrying the acceptor-site allele. Skin biopsy is a standard diagnostic procedure, and the matrix is already named in `DL-BIO-001`/`DL-BIO-002`.
- ⚠️ **Availability is NOT assumed.** This repository documents *feasibility*, not possession. See § E.

### B.2 Controls — four, and each does distinct work
| Control | What it rules out |
|---|---|
| **Healthy donor fibroblasts**, sex- and passage-matched | The baseline aberrant fraction of the **wild-type** junction. Non-zero baselines are normal, and without this the patient number has no scale. |
| **A second unrelated healthy line** | Inter-individual variation in that baseline. One control cannot distinguish a genotype effect from a donor effect. |
| **Vehicle-only arm** for every cycloheximide condition | Solvent effects on transcript abundance. |
| **A transcript unrelated to WWOX and known to be NMD-sensitive** (e.g. an endogenous NMD reporter such as `SRSF` auto-regulated isoforms or `GAS5`) | That the cycloheximide block **worked**. Without a positive NMD control, "no change after cycloheximide" is uninterpretable. |

### B.3 The junction and the amplicons
- **The affected junction** is the intron 8 / exon 9 acceptor. The public worked-example allele of this class is `c.1057-2A>G`.
- **Junction amplicon:** forward primer in **exon 8**, reverse primer in **exon 9**, positioned so the amplicon **spans the exon 8→9 junction**. 🔴 **CORRECTED 2026-09-22 — read this, not what it replaced.** **WWOX has NINE exons: there is no exon 10, so "exon 9 skipping" is not a definable outcome.** Real outcome set: **cryptic acceptor at `c.1063`** — the only available `AG` — giving a product **6 nt SHORTER** than normal; **intron-8 read-through/retention** (778,856 nt, cannot be a mature mRNA, and **carries no exon 9, so the exon-9 reverse primer has no site and this species is simply ABSENT from the trace — its absence must NOT be read as support for the cryptic-acceptor outcome**); **intronic polyadenylation or an alternative terminal exon** (documented in this gene by Schirmer).
- **Normaliser amplicon:** **exons 4–6** ("core"), which lie upstream of the affected junction and report total WWOX transcript.
- 🔴 **A published assay of exactly this shape already exists and should be redesigned from, not reinvented:** Schirmer MA *et al.* 2016, *J Natl Cancer Inst* (`PMID 26857392`, PMC4859408) quantifies **exon 8→9 junction transcripts against core exon 4–6 transcripts**, reporting a ratio of **~67 %** with intra-line correlation **r = 0.68** (r = 0.80 under gemcitabine), in **89 lymphoblastoid lines**. It also documents alternative transcripts **terminating within intron 8**. `DL-BIO-003` already names it as the template.
- ⚠️ **No primer sequences are given in this packet, deliberately.** They are not derivable with certainty from the records held here, the exon 8/9 boundary is the object under test, and a wrong primer placement would silently answer a different question. **Design them from the canonical transcript (`NM_016373.4`) and the Schirmer assay, and validate on the healthy control first.**

### B.4 The ± cycloheximide arm
- **Cycloheximide**, standard NMD-inhibition conditions for fibroblasts, applied to **both patient and control** lines, each **with a vehicle-only twin**.
- **Why it is not optional:** without an NMD block, *"the aberrant transcript is absent"* and *"the aberrant transcript is being degraded as fast as it is made"* are **indistinguishable** — and they imply opposite things for a correction strategy. The census measured that **no WWOX splice allele has ever been assayed with an NMD inhibitor**: `cycloheximide`, `emetine`, `actinomycin` and `nonsense-mediated` occur **zero** times across the reachable literature.
- **Read out the ratio in both arms.** The *change* in aberrant fraction on NMD block is the NMD contribution, and it is a number nobody has.

### B.5 Quantification
1. **Capillary electrophoresis or densitometry** of the RT-PCR products, giving the **aberrant:normal ratio** — the primary endpoint.
2. **Junction-spanning qPCR** (junction amplicon / core amplicon), as in Schirmer, giving a continuous measure independent of gel saturation.
3. **Sanger sequencing of every band**, because a band size is not an identity — this is how exon skipping, a cryptic acceptor and a heteroduplex are told apart.
4. 🔴 **If multiple species appear, escalate once to long-read (nanopore/PacBio) cDNA sequencing.** Short-read junction assays cannot phase two events on the same molecule, and a compound-heterozygous background makes that a live possibility.

### B.6 Replicates
- **Minimum n = 3 independent RNA extractions** per line per condition (biological), each with technical duplicates for qPCR.
- **Two patient lines if obtainable**; with one, the design measures an allele in a donor, not an allele.
- **Blind the quantification** to genotype and condition. It costs nothing and this disease model has recorded four separate instances of an unblinded readout carrying a claim.

### B.7 Expected products
| Event | Junction amplicon | Detectable here? |
|---|---|---|
| Correct splicing | full-length exon 8→9 | ✅ primary readout |
| ~~**Exon 9 skipping**~~ 🔴 **NOT A DEFINABLE OUTCOME — there is no exon 10** | ~~shorter, exon 8→10~~ **withdrawn 2026-09-22** | ⛔ |
| **Cryptic acceptor at `c.1063`** (SpliceAI `DS_AG 0.64`; `+8` is a **genomic offset from the variant**, **not** an amplicon size change) | 🔴 **CORRECTED 2026-09-22: 6 nt SHORTER, not `+8 nt`.** The old entry was wrong in **sign and magnitude** — a downstream cryptic acceptor loses `c.1057–1062`. **A lab sizing against the old row would look 8 nt ABOVE normal while the real species sits 6 nt BELOW, and would score the assay negative while the predicted event was occurring.** | ✅ — but **not on a gel and not on native PAGE**: 6 nt is 2.2% of a ~271 nt amplicon, and a 6-nt heteroduplex migrates anomalously. **Capillary electrophoresis / GeneScan (denaturing, ±1 nt), with a known 6-nt indel sizing standard on the same run**, and **Sanger every band including the apparently-normal one** |
| **Intron 8 retention** | — | ❌ **requires a separate intron-anchored reaction**; intron 8 is 778,856 bp |
| Transcript terminating within intron 8 | — | ❌ separate 3′-anchored reaction; Schirmer documents these exist |

---

## C · WHAT IT WOULD RESOLVE

| LEGEND node | Today | After this assay |
|---|---|---|
| **`TX-001` baseline** | An efficacy endpoint with **no denominator in any WWOX allele in any tissue** | A measured aberrant:normal ratio in the relevant cell type — the number every rescue is compared against |
| **NMD contribution** | **Never measured for any WWOX splice allele** | Quantified as the ratio's shift on cycloheximide |
| **Residual correctly spliced transcript** | Predicted in silico only (SpliceAI/Pangolin) | Measured — and if it is non-trivial, the genotype's position between WOREE and SCAR12 acquires a number |
| **Denominator for ASO rescue** | Absent | Present, in the matrix an ASO would be tested in |
| **Whether splice correction has realistic headroom** | Unknown | 🔴 **Decided.** If correct splicing is already near-normal, `TX-001` has little to recover and the portfolio should shift to the missense allele. If it is near-zero and NMD-hidden, the headroom is large. |
| **`DL-BIO-002`** | `in-silico done (wet open)` | Converts from prediction to measurement |
| **`DL-BIO-003`** | A published assay named as transferable | Transferred, or shown not to transfer |

---

## D · DECISION VALUE — why this beats more paper scouting on the same point

**The literature has been measured, and it is empty on exactly this question.** Of 20 splice-relevant records: **three measured a transcript** from a WWOX splice allele, **two merely annotated one**, and **one of the three is reachable here**. That one is a **minigene in HEK293T with an artificially shortened intron**, not patient RNA, with **no NMD block, no quantification, no protein, and no correction arm**. Its own conclusion — *"a minigene assay … revealed that the variation resulted in protein truncation"* — is an in-silico translation voiced as an assay result.

So further scouting can only return the same shape of answer: **nobody has measured it.** That is already established to the standard this repository requires, by fetch-and-measure rather than by inference.

**Three further reasons this specific experiment dominates:**

1. 🔴 **It is the gate `TX-001` already imposes on itself.** The strategy's mandatory gate reads: *no ASO-versus-editing choice before junction-specific RT-PCR + amplicon sequencing + allele-specific quantification.* That gate was written as prudence; the census shows **it is the only available first step**, because the measurement it demands does not exist for any allele.
2. **It can falsify the strategy cheaply.** A near-normal correctly spliced fraction would retire `TX-001` before any ASO design cost is incurred — and **no ASO or splice-correction arm exists anywhere in the WWOX literature**, so `TX-001` has zero in-gene precedent to borrow confidence from.
3. **It is a standard assay, not a new method.** RT-PCR, cycloheximide and Sanger are routine; the design work is primer placement, and a published template exists.

**Ten patients across two canonical alleles have never had their RNA examined** — `PMID 42721537` (`c.107+1G>A`, five patients, `FT-110`) and `PMID 26345274` (`c.606-1G>A`, five patients, packet `A8`). The same assay run on banked RNA from either cohort would answer the class-level question even without the reference allele.

---

## E · PRACTICALITY — only what the repository documents

| Item | Documented status | Source |
|---|---|---|
| Donor-derived fibroblasts for the reference genotype | **Feasible, not documented as available.** `DL-BIO-001` records only that *"la biopsia cutanea è una procedura diagnostica standard"*. | `DL-BIO-001` |
| A group that **holds WOREE patient fibroblasts and runs WWOX RT-PCR** | ✅ **Documented.** `PMID 35573960` (Genoa), read in full this session: *"The RT-PCR derived from fibroblast extracts of patient and unaffected parents and age-matched neurotypical control"* | `FTR-20260921-35573960-01` |
| A published junction-vs-core WWOX assay to redesign from | ✅ **Documented**, with its ratio, correlation and cohort size | `DL-BIO-003`, `PMID 26857392` |
| Banked RNA from either five-patient cohort | ❌ **Not documented.** Both papers are acquisition-blocked here; whether RNA exists is unknown. | `FT-110`, packet `A8` |
| Local capacity to run any of this | ❌ **None.** This is a wet-lab assay; this deployment has no bench. | — |

🔴 **The honest summary: LEGEND can specify this experiment completely and cannot run any part of it.** The single highest-value action is therefore a **contact**, not a computation — and the Genoa group is the one collaborator the repository can document as already holding both the cells and the assay.

## F · What remains unknown even after a clean result

- **Transcript is not protein.** No protein has ever been observed from a WWOX splice allele. A measured ratio does not say what, if anything, is translated.
- **Fibroblast is not neuron.** Splicing efficiency is tissue-dependent, and the disease is neuronal.
- **A ratio is not a rescue.** It establishes the denominator; whether an ASO can shift it is a separate experiment with its own controls.
- **One donor is not an allele class**, and the reference genotype is compound heterozygous — the missense allele's contribution to total WWOX is a different measurement (see the proteostasis line).

---

*Orchestrator, 2026-09-21. READ-ONLY; no canonical file modified; no commit candidate created. No primer sequence is asserted. Nothing here is medical advice, and no clinical action is proposed.*
