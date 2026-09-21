# Fresh scientist/node scout — 2026-09-21, autonomous continuation (Orchestrator)

**Mode:** READ-ONLY census. No canonical file edited, no claim created, no therapy proposed.
**Method:** PubMed (the only literature route open in this checkout — see § 0), cross-checked against
LEGEND by `registry_records.py get --pmid` for **every** candidate before it was called new.
**Source of all bibliographic records:** PubMed. DOI links given per record.

> **§ 0 is not a footnote.** It re-orders the candidate list, exactly as the environment constraint
> did in [`next_scientist_scout_20260921.md`](next_scientist_scout_20260921.md) — but the constraint
> has **changed** since that file was written, in one direction and not the other.

---

## § 0 · The environment, re-measured rather than inherited

| Capability | 2026-09-21 earlier scout | **This checkout, measured today** |
|---|---|---|
| `fitz` / PyMuPDF | absent | 🟢 **INSTALLABLE and INSTALLED** (`pip install pymupdf` → 1.28.2) |
| `pdftotext` / `pdftoppm` / `pdfimages` | absent | 🔴 still absent (no poppler) |
| `files/fulltext/` local artefact corpus | 29 artefacts | 🔴 **EMPTY — the container is fresh and `files/` is gitignored.** Every one of the 29 extracted artefacts is gone. Any re-read requires a re-fetch. |
| Shell egress to NCBI / EBI / Unpaywall / OpenAlex / Semantic Scholar / Crossref / CORE | denied | 🔴 **denied — all eight tested, all `CONNECT tunnel failed, 403` (organization egress policy)** |
| `WebFetch` to europepmc.org / pmc.ncbi.nlm.nih.gov | not tested | 🔴 **`EGRESS_BLOCKED`, both** |
| PubMed MCP server (PMC open-access subset) | the only route | 🟢 **still the only route, and it works** |

🔴 **Consequence, stated once.** PyMuPDF now exists but there is **no way to put a PDF on disk**:
every download route is policy-blocked and `WebFetch` returns text, not bytes. So the new capability
is real but **conditional on an operator-supplied PDF** — which is exactly how `A9` was read. It
does **not** reopen any of the packet items by itself. What it *does* do is remove the second half
of the old blocker: a supplied PDF is now readable, and `figure_ppi_preflight`, `surface_census`
and `regenerate_adjudications` become runnable, so a supplied PDF can now carry a figure-anchored
locator under rule 5d. **`D-14` is no longer an unconditional bar; it is a bar conditional on
acquisition.** Recorded so the next session does not re-measure it. (`pip install` is not persisted
by the repository; it must be re-run per container.)

---

## § 1 · The publication-integrity sweep — a clean NEGATIVE, and it is the first result

Query: `WWOX AND (Retracted Publication[pt] OR Retraction of Publication[pt] OR Expression of
Concern[pt] OR Published Erratum[pt])` → **12 records in all of PubMed.** Four of them are papers
LEGEND holds. **All four were already correctly classified and reconciled.** Verified record by
record with `registry_records.py`:

| PMID | What it is | LEGEND's state | Verdict |
|---|---|---|---|
| `38355659` | *Correction:* WWOX promotes osteosarcoma development via upregulation of Myc | **`PAPER 092`**, declared `**published erratum**`, `Claim links: none — the source supports no biological proposition`, read in its own right with `FTR-20260909-38355659-01` and a strict-PASS manifest | ✅ correct |
| `30470736` | *Author Correction:* WWOX controls hepatic HIF1α… (Fig 3A/3D H&E duplication) | **`PAPER 091`** carries a `Publication integrity` field naming it, **and the erratum was read as its own source** (`FTR-20260909-30470736-01`); the erratum's declared scope was checked against all 38 locators and **none sits on Fig 3A or 3D** | ✅ correct, and checked rather than trusted |
| `28373548` | *Editorial Expression of Concern* on the PNAS WWOX gene-restoration paper | **`FT-088`**, titled `🔴 PMID 16223882 porta una EXPRESSION OF CONCERN permanente` | ✅ already flagged |
| `23446842` | *p73 participates in WWOX-mediated apoptosis in leukemia cells* — **Retracted** | **`CORPUS-STUB-179`**, `🔴 PUBLICATION_INTEGRITY_HOLD — retracted`, `No canonical claim rests on this record`, legacy receipt quarantined append-only by `FTR-20260806-23446842-02` | ✅ correct |

> **Result: `0` new integrity defects. The WWOX publication-integrity surface is fully reconciled as
> of 2026-09-21.** The retraction *notice* for `23446842` (`PMID 42464650`, IJMM 2026, CC BY) is
> itself not held as a record; that is a bibliographic gap of no consequence, since the HOLD it
> would justify is already on the stub. **This negative is the finding — do not re-run this sweep
> without new dated literature.**

---

## § 2 · Candidates A–E, scored

Scoring notes: "readable" = PMC open-access, **tested today** with `convert_article_ids` +
`get_copyright_status`. "held" = tested today with `registry_records.py get --pmid`.

### A · Richards / O'Keefe (Adelaide) — 🔴 **SETTLED ON EVIDENCE: NO**

Two readable items (`26302329` PMC4547717, 37,561 chars; `34210081` PMC8305172, 26,370 chars) were
dispatched to Scientist A **as a discriminator, not as a batch**. Both were read end-to-end,
Results-first; **15/15 verbatim locators re-matched against the retrieved text, zero mismatches**.
Full report: [`adelaide_node_discriminator_20260921.md`](adelaide_node_discriminator_20260921.md).

> **Verdict: the node gives WOREE neither a therapeutic lever nor a practical screening platform.**
> The deciding fact is the review's own statement that the fly carries **no baseline phenotype to
> rescue** — *"deficiency in[] displays no phenotypic consequences [] and, therefore, might be
> considered a poor model for those species (including humans) for which[] is necessary."* Every
> Adelaide readout is therefore a **modifier assay in a sensitised oncogenic or mitochondrial
> background**, and in both readable assays **the sign runs backwards for WOREE**: WWOX *promotes*
> cell death and losing it is *protective* — *"Decreased WWOX activity together with ectopic
> expression of Egr/TNFα … resulted in a decrease in the relative area of Caspase 3 staining …
> Conversely, increased WWOX expression increased the relative area of Caspase 3 staining."*

**The node is not null, and the non-null part is a constraint rather than a lever.** Raising WWOX
suppresses a mitochondrial-deficiency phenotype **only with an intact SDR catalytic site** (fly
Y288F abolishes it; fly Y288 ≡ human Y293). That bears on **`TX-007`** (must an AAV construct be
catalytically competent?) and **`TX-003`**. 🔴 It is held **second-hand through the review, with no
receipt**, and it is **necessity, not the domain *sufficiency*** that `DL-MECH-021` wants — the
review's own G372R-vs-P47T passage (two different domains, one clinical outcome) argues *against*
single-domain sufficiency. **`DL-MECH-021` stays at `basso`; it gains nothing either way.**

**Three further results worth not re-deriving:**
- **The platform is disqualified on throughput and on a genotype-correlated exclusion**, not merely
  on relevance: 10 hand-traced eyes / ≥20 hand-dissected discs per genotype, plus *"Significant
  disruption to eye disc morphology was observed in 13/52 pairs of the[] clones and 31/50 pairs;[]
  clones and these were not included in these analyses"* — **25 % vs 62 %, the worst discs removed,
  differentially by genotype.**
- **Every therapeutic proposal in this node is blocked upstream by the same sentence:** *"Despite
  more than twenty years of research on the[] protein, the substrate and product of the enzyme
  reaction that it catalyses are yet to be discovered."*
- **Genotype transferability is where the node dies.** Its only expression-raising manoeuvre is
  useless in **null/null** and **large deletion/CNV** (nothing to upregulate), **potentially adverse**
  in the **splice** classes (more transcript from a splice-defective allele → more truncated
  unstable product, cf. `DL-MECH-045`), and coherent only for **residual-protein** — the class that
  least needs it.

**A fourth independent line for the standing category objection.** Here too the phenotype-improving
move is *removing* WWOX. Recorded as corroboration of the objection already in
`AUTONOMOUS_SESSION_STATE.md`; **not proposed as a claim and not for commit.**

**One clean in-paper negative preserved:** altered WWOX had **no** effect on p53- or Hid-driven eye
phenotypes in either direction — which narrows the mammalian WWOX–p53 literature.

⚠️ **Instrument reading recorded by the reader, against himself:** the extractor stripped italic
gene/species tokens **and every citation number** (markers render as `[]`). The brief's request to
quote "with their citation numbers" **could not be satisfied from this route**; attribution of the
two key passages to `26390919` / `23765596` was made by content-match against their PubMed
abstracts, and both matched exactly. Stated rather than hidden. No negative rests on an italic count.

### B · Bednarek / Kośla (Lodz) — *delegated to Scientist B, verdict pending*
Standing assessment: ~40 papers, predominantly oncology; developmental output is **one primary**
(`31543760`, read and audited) **plus one review** (`32389029`, dispatched). Two independent
confirmations found today that the node is oncology-dominant: `34204789` (Kałuzińska/Bednarek,
*Cancers* 2021, WWOX-dependent glioblastoma biomarker triad) and **`42589397`** (Hammouz/Bednarek,
*IJMS* 2026, WWOX/HIF1A ratio across TCGA BRCA and OV).

🔴 **But `42589397` is more than a confirmation, and it is why Lodz does not simply lose.** It is
**2026, open access (PMC13467099, [DOI](https://doi.org/10.3390/ijms27156740)), NOT HELD by LEGEND**,
and it tests, in TCGA, the very quantity `CLAIM 025` is about — *"The WWOX/HIF1A ratio may function
as a systems-level marker of maladaptive biological state"*. A live LEGEND claim now has a newer,
larger, independent test of its central quantity that LEGEND has not read. **That is a reading
obligation regardless of which node wins**, and it is queued below as W-5.

### C · A developmental / embryonic node outside these labs — **THE WINNER**

The prior scout closed this candidate on the ground that its two decisive primaries (`15026124`,
`33914858`) are unobtainable. **That was true of those two papers and false of the node.** A census
run today on `WWOX AND (embryonic OR prenatal OR fetal OR cortical development OR neuronal
migration OR neural progenitor OR corticogenesis OR neurogenesis OR interneuron OR radial glia)`
returns **47 records in all of PubMed** — a genuinely small field — and inside it are **three
papers carrying human developmental WWOX signal that LEGEND has never held at all**, plus two
retrievable stubs it holds and has never read.

**What makes this node win is not volume. It is life stage.** The Chang batch's structural lesson
was that a large neurodegenerative/proteostatic literature *begins too late relative to WOREE
onset*. Every item below is measured **prenatally, in infants, or on a congenital endpoint**.

### D · Protein-rescue / proteostasis — **ALREADY WORKED TO EXHAUSTION AT THE LITERATURE LEVEL**

This candidate was scouted and **found closed, not open**, which is itself the answer to the brief's
question. LEGEND already holds
[`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md) (127 lines),
[`wwox_missense_cma_degradation_audit_20260921.md`](wwox_missense_cma_degradation_audit_20260921.md)
(329 lines), [`sdr_missense_readout_assessment_20260920.md`](sdr_missense_readout_assessment_20260920.md)
(348 lines), [`proteostasis_rationale.md`](proteostasis_rationale.md) and
[`variant_triage_rescuability.md`](variant_triage_rescuability.md).

A fresh PubMed census confirms there is no unread WWOX proteostasis literature to add:
`WWOX AND (protein stability OR proteasome OR degradation OR chaperone OR ubiquitin OR folding OR
misfolding OR lysosomal)` returns 412 records whose WWOX-proteostasis core is **one primary**
(`41124647`, read) plus reviews and off-axis oncology/GWAS. The decisive statement already stands in
the matrix and is reproduced here so it is not re-derived:

> 🔴 **"No functional measurement has ever been made on a WWOX missense protein whose abundance was
> restored."** Not weak evidence — none. And the same paper supplies the counter-case: **P282A** is
> an SDR-span substitution that is indistinguishable from empty vector in every functional assay
> **with no stability defect at all**.

**Therefore the residual Candidate-D question is not "which lab has WWOX proteostasis papers" — it
is "which lab has the *method*."** That is a transferable-methodology question, not a WWOX-literature
question, and it is queued below as **W-6** rather than treated as a scientist node. Reading more
WWOX papers cannot answer it.

### E · Any superior node
None found. The genuinely superior *unit of work* is C, and it is a **question node**, not a person —
consistent with the prior scout's structural finding that no single WWOX lab has an unread corpus
that can carry a batch.

---

## § 3 · Selection

> ### **CLEAR WINNER: `NODE_WWOX_HUMAN_PRENATAL_AND_INFANT_PHENOTYPE`**
> ### Research question: **what is measurably different about the human brain, before birth and in infancy, when WWOX is lost — and does any of it discriminate genotype classes?**

It is a clear winner and not a close call, on four of the ten stated criteria at once:

1. **Life-stage fit — decisive, and unique.** Every item is prenatal, neonatal or infant. This is
   the only readable material in the corpus that sits *before* the window the Chang batch overshot.
2. **Incremental information — three of five items are held by LEGEND in no form whatsoever**, which
   is the strongest "not already known" signal available and was verified per-PMID, not assumed.
3. **Species — human throughout.** Candidates A and B are fly, cancer line and TCGA.
4. **Retrievability — 4 of 5 verified open access today**, against Adelaide's 2-of-8.

It does **not** win on therapeutic leverage, and that is stated rather than hidden: an association
study changes no intervention by itself. It wins because it can change **genotype stratification**
and the **developmental-window** premise, which are two of the six things the mission names.

---

## § 4 · WAVE 1 — five papers, acquisition verified today

| # | PMID | Paper | Held by LEGEND? | Acquisition | What it would settle |
|---|---|---|---|---|---|
| **W-1** | **28763065** | Xia K, …, Knickmeyer RC, *Transl Psychiatry* 2017;7(8):e1188 — *"Genome-wide association analysis identifies common variants influencing infant brain volumes"*, **n = 561 infants** | 🔴 **NOT HELD — no record in any surface** | ✅ PMC5611727 · [DOI](https://doi.org/10.1038/tp.2017.159) | The abstract reports an intronic WWOX SNP (`rs10514437`) that **"neared genome-wide significance for white matter volume."** 🔴 *Neared* is the source's word and must survive the read. If it holds up in Results, it is **the only human infant white-matter signal at the WWOX locus in the literature** — and white matter / myelin is exactly where `DL-MECH-027`, `CLAIM 002` and `CLAIM 003` live. If it does not, that is a clean negative on a tempting lead. |
| **W-2** | **41378749** | Mondragon-Estrada E, …, Morton SU, *Birth Defects Res* 2025;117(12):e70007 — folate × genetic risk for **neural tube defects**, Bangladesh | 🔴 **NOT HELD** | ✅ PMC12697008 · [DOI](https://doi.org/10.1002/bdr2.70007) | A **coding-region** WWOX variant (`rs7184417`, OR 6.20, p = 2.22E-06) **nominally** associated with spina bifida. 🔴 *Nominal*, n = 91 vs 97, and the authors themselves say it "should be assessed in additional cohorts". The value is the **endpoint class**: neural-tube closure is the earliest neurodevelopmental phenotype there is. Read to establish whether this is a real prior for prenatal WWOX function or a small-n artefact — **a dismissal is a perfectly good outcome.** |
| **W-3** | **37974179** | Dong X-S, …, Li Z-M, *BMC Med Genomics* 2023;16(1):291 — compound heterozygous **deletions** in WOREE, breakpoints mapped by WGS + gap PCR | `CORPUS-STUB-096` / `LIT-0118`, `not_processed` | ✅ PMC10652538 · [DOI](https://doi.org/10.1186/s12920-023-01731-4) | **Genotype transferability, directly.** WES called a homozygous exon-6 deletion; **WGS showed it was three different larger deletions** (13,261 / 53,904 / 177,200 bp) on two alleles. That is a concrete, documented case of **an exome call misrepresenting the true allele structure** in this gene — which bears on every genotype-class statement LEGEND makes from exome-derived variant reports, and on the `large deletion / CNV` class specifically. |
| **W-4** | **35712340** | Sukkar G, …, Al Lohaibi RS, *Cureus* 2022;14(5):e25003 — homozygous **`c.406A>G`** WWOX, WES incl. **prenatal** WES data | `CORPUS-STUB-141` / `LIT-0160`, `not_processed` | ✅ PMC9193507 · [DOI](https://doi.org/10.7759/cureus.25003) | A **homozygous missense** allele with a described phenotype — the missense/missense genotype class, where LEGEND's evidence is thinnest. Low-tier journal, case report, no functional work expected: read it **to place the allele and the phenotype**, not for mechanism, and say so. |
| **W-5** | **42589397** | Hammouz RY, …, Bednarek AK, *IJMS* 2026 — WWOX/HIF1A ratio across TCGA BRCA (n=390) and OV (n=228) | 🔴 **NOT HELD** | ✅ PMC13467099 · [DOI](https://doi.org/10.3390/ijms27156740) | **A live LEGEND claim has a newer, larger, independent test it has not read.** `CLAIM 025` (`in observation`) asserts the WWOX/HIF1A ratio may be a systems-level state marker. Read to see whether the 2026 analysis **supports, qualifies or undercuts** it — and note the ratio is here tested in **tumour** tissue, so transferability to a non-tumoral CNS claim must be argued, not assumed. |

**Optional W-6 — the Candidate-D residual, and it is not a paper-reading task.**
*"Does a laboratory or transferable methodology exist that can measure whether a destabilised
missense protein, once re-stabilised, is functional — at matched abundance?"* This is a
**methods** question aimed outside the WWOX literature (pharmacological chaperones, folding
correctors, abundance-clamped function assays, SDR/Rossmann-fold stabilisation). Queue it as a
bounded methods census **after** Wave 1, and hold it to the same rule: **a method that only
restores abundance answers nothing**, because `P282A` already proves abundance and function
dissociate in this exact domain.

---

## § 5 · Acquisition debt this scout adds or sharpens

| PMID | Why it matters | State |
|---|---|---|
| **`25716914`** | Valduga M, …, Jonveaux P, *J Hum Genet* 2015;60(5):267–71 — *"WWOX and severe autosomal recessive epileptic encephalopathy: **first case in the prenatal period**"*. 0.6 Mb homozygous 16q23.1 deletion removing WWOX exons 1–6; **the only report of prenatal ultrasound findings in a WWOX-null fetus** in the entire literature, with an affected sibling who died at 22 months. This is the single most on-target paper for the question *"what goes wrong before birth?"* | 🔴 **NO PMCID — verified today** with `convert_article_ids`. Springer/Nature, paywalled. Already queued as `FT-030` / `FT-057`; **raise its acquisition priority — it now heads the prenatal question, not merely a queue.** |
| **`26390919`** | Choo 2015, *Genes Chromosomes Cancer* 54(12):745–61, [DOI](https://doi.org/10.1002/gcc.22286) | 🔴 no PMCID, **re-confirmed today**. **Do not re-queue for automated retrieval.** Scientist A's read converted this from a vague packet entry into **two answerable questions**: (1) *Was the SDR domain tested **alone** (sufficiency), or only full-length protein bearing Y288F (necessity)?* — plus **a Western showing Y288F protein is present at wild-type levels**, without which "abolished function" is indistinguishable from "protein absent"; (2) *Does any WWOX-loss phenotype exist **without** the mitochondrial co-insult?* — the direct test of the no-baseline-phenotype sentence. |
| **`23765596`** | Dayan 2013, *Genes Chromosomes Cancer* 52(9):823–31, [DOI](https://doi.org/10.1002/gcc.22078) | 🔴 no PMCID, **re-confirmed today**. Two questions: *Was WWOX **protein** measured, or only mRNA?* — with fold-change, n and statistic for the galactose/OXPHOS arm — and *is the raised transcript the full-length correctly spliced isoform?* |
| — | 🟢 **The node need not be reopened if these papers arrive. Only these four questions do.** | — |
| `33914858` | Repudi 2021 *Brain*, primary under `CLAIM 003` (`consolidated baseline`), never read | 🔴 no PMCID, **re-confirmed today**. Packet `A4`. 🟢 **But note § 0: with PyMuPDF now installable, an operator-supplied PDF of this paper IS now readable in this checkout, figures included.** That changes the ask from "we cannot use it" to "send the PDF". |

---

## § 6 · Why the other framings lose — stated so they are not re-proposed

- **"Pick a famous WWOX PI."** No WWOX laboratory has an unread corpus that can carry a batch. That
  was established by the prior census and nothing today contradicts it.
- **"Human WOREE natural history."** Largely read. Today's check confirms the two newest cohort
  papers are **not** openings: `42721537` (Argentina, n=7) is **already held as `FT-110`** and is
  already load-bearing in the TX-001 packet — 🔴 *this scout nearly reported it as a new find, and
  the LEGEND-first check caught it; the failure mode the state file names as "a delegate's census
  describes the field, never this repository" is live and it caught me* — and `42190144`
  (*Neurology* 2026, burst-suppression EIDEE, n=110) is **MRI-negative by cohort design**, whereas
  WOREE is MRI-abnormal in essentially all reported patients, so WWOX is excluded by selection
  before it is counted. Paywalled in any case.
- **"Proteostasis."** See § 2 D. Closed at the literature level; open only as a methods question.
- **"Re-run publication integrity."** See § 1. Zero defects; do not re-run without new literature.

---

*Non-canonical analysis file. No canonical registry, ledger, claim or current file was written. No
commit candidate produced. No receipt claimed — **nothing in this file is a read**; every § 2–§ 5
statement about a paper's content rests on its PubMed abstract or on a LEGEND record, and is
labelled as such. **An abstract is not a read.** Not medical advice.*
