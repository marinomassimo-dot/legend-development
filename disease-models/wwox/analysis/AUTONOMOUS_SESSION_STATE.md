# Autonomous session — continuation state

**Updated:** 2026-09-21 · **Purpose:** recovery point. If this session is interrupted, a cold reader
resumes from here. **Not a handoff and not a stop.**

---

# ⏩ CHECKPOINT — 2026-09-21, SECOND autonomous continuation (Orchestrator)

**Everything below the horizontal rule after this block is the PREVIOUS continuation and is still
true unless contradicted here.** This block is newer. Read it first.

## 0 · The environment changed, and it decides what is possible

| Capability | Previous continuation | **Measured today** |
|---|---|---|
| `files/fulltext/` | 29 artefacts | 🔴 **EMPTY AT START.** Fresh container, `files/` is gitignored — **all 29 prior artefacts are gone and unrecoverable.** Re-populated today with 8 new ones. |
| PyMuPDF (`fitz`) | absent | 🟢 **`pip install pymupdf` WORKS** (1.28.2). Re-run per container; not persisted. |
| poppler (`pdftotext`/`pdftoppm`) | absent | 🔴 still absent |
| Shell/WebFetch egress to pubmed · pmc · europepmc · unpaywall · openalex · semanticscholar · crossref · core · **clinicaltrials.gov** | "denied" | 🔴 **ALL TESTED, ALL REFUSED** (`403 CONNECT tunnel failed` / `EGRESS_BLOCKED`) |
| **`WebSearch`** | not known to be available | 🟢 **WORKS.** Different channel from the egress proxy. **It is the only route to non-PubMed public information** and is what made the `TX-007` monitor runnable. |
| PubMed MCP | only route | 🟢 still the only route to literature, and it works |

🔴 **PyMuPDF is real but conditional:** there is no way to *get* a PDF onto disk, so it only helps
for an **operator-supplied** PDF — as `A9` was. What it does change: `D-14` ("no figure panel is
inspectable") is **no longer unconditional**; it is conditional on acquisition.

## 1 · What this continuation did

**Four landings, each gate-PASS on the exact SHA and verified by `ls-remote`:** `e096984` ·
`0ee3cf9` · `d8573b4` · `36860a2` on `claude/legend-autonomous-woree-tv6gz8`.

**Nodes settled ON EVIDENCE, not on absence — both NO:**
- **Adelaide (Richards/O'Keefe)** — [`adelaide_node_discriminator_20260921.md`](adelaide_node_discriminator_20260921.md).
  Dies on its own review: the fly *"displays no phenotypic consequences"*, so every readout is a
  modifier assay in a sensitised background, and **the sign runs backwards for WOREE**. Survives as
  a **construct constraint for `TX-007`**: raising WWOX suppresses the mitochondrial phenotype only
  with an intact SDR catalytic site (fly Y288F abolishes; Y288 ≡ human Y293) — **necessity, not the
  domain sufficiency `DL-MECH-021` wants. `DL-MECH-021` stays at `basso`.**
- **Lodz (Bednarek/Kośla)** — [`lodz_node_discriminator_20260921.md`](lodz_node_discriminator_20260921.md).
  Dies on a count: in a review titled *"The WWOX gene in brain development and pathology"*,
  `embryonic day`, `gestation`, `fetal`, `trimester`, `cortical plate`, `radial glia` all occur
  **zero** times. **Not one developmental timepoint.** Two citation-fidelity defects found.

**The node selected and run:** `NODE_WWOX_HUMAN_PRENATAL_AND_INFANT_PHENOTYPE`
([`next_node_scout_20260921_orchestrator.md`](next_node_scout_20260921_orchestrator.md) — **read its
correction banner**). Wave 1 (`28763065`, `41378749`): **INFORMATION GAIN NO on all six axes.**
Wave 1b (`37974179`, `35712340`, `42589397`): YES on experimental roadmap and uncertainty, NO on four.

🔴 **The single most useful result of this continuation** —
[`mave_portability_to_wwox_20260921.md`](mave_portability_to_wwox_20260921.md) +
[`missense_rescue_methodology_census_20260921.md`](missense_rescue_methodology_census_20260921.md):

> **The measurement the proteostasis matrix says nobody has ever made — function at matched
> abundance — is a published, scaled platform (MAVE / VAMP-seq), already run on an oxidoreductase
> (CYP2C9, CYP2C19) and on a neurodevelopmental epilepsy gene (TSC2). LEGEND had never heard of it:
> `VAMP-seq`, `deep mutational scan*`, `multiplexed assay*` appeared NOWHERE in the repository.**
>
> **And it is not portable to WWOX today.** The function half needs five things and WWOX supplies
> one. TSC2's trick was that its readout is **an epitope, not an activity** — an antibody stain of
> fixed cells (pS6) with genomic DNA recovered from the sorted cells themselves. So the missing
> piece **need not be catalytic turnover**, which *reduces* the obstacle without removing it.
> 🔴 **The gate is the prior invention of a single-cell, fluorescence-readable WWOX activity
> sensor** — and the matrix's own chosen readout, **co-IP, is intrinsically per-sample: the
> pulldown destroys the cell-to-genotype link pooling depends on.**
>
> 🔴 **The `P282A` brake now has a number from a real gene: 31/80 = 38.75 %** of known-pathogenic
> TSC2 missense alleles carry **normal abundance**. An abundance-only WWOX MAVE would be expected
> to miss about **two in five** of exactly the alleles that matter.
>
> **The CMA question is CLOSED as ORTHOGONAL.** The one systematic degron map in existence is a
> **ubiquitin-proteasome** screen by construction and conclusion (bortezomib and E1i stabilised;
> *"no substantial change was observed with chloroquine"*) — the **mirror image** of the WWOX
> observation, where MG-132 did nothing and CQ/NH₄Cl restored the band. Its 30-residue tiles could
> never resolve `LRSVQ` 187–191 anyway.

**`TX-007` monitor M1–M5 run** (it declares *"review every LEGEND session"*) —
[`tx007_monitor_update_20260921.md`](../therapeutics/tx007_monitor_update_20260921.md).
No peer-reviewed case report · no WWOX trial registered · no expanded access · the June-2026
*"FDA filing within two months"* is **past date, unconfirmed**. 🔴 **But the sponsor's sibling
programme answers the age question the discovery ledger asked for, and weakens it:** `MZ-1866`
(AAV9-TCF4, Pitt Hopkins, `NCT07135050`, ICV route — **the same route as the WWOX n=1**) is dosing
and enrolling **ages 2–25**, not infants; FDA **Rare Pediatric Disease Designation** August 2026.
The WWOX asset is designated **`MZ-9138`**. ⚠️ **All press-release/registry level, none peer-reviewed,
and `clinicaltrials.gov` is egress-blocked so even the registry was read via search summaries —
`SEGNALE TRASLAZIONALE`, never evidence. Re-verify before acting.**

**Publication-integrity sweep — a clean NEGATIVE.** All 12 retraction/erratum/EoC records in the
WWOX literature; four concern papers LEGEND holds; **all four already correctly classified. Zero new
defects.** Do not re-run without new dated literature.

## 2 · Method rules earned TODAY — apply, do not rediscover

- 🔴 **A PAPER'S STATE IS A JOIN OF THREE SOURCES, AND EACH ONE MISLED ONCE TODAY.** Registry
  status, the **receipt ledger**, and the **manifest directory**. Checking any one alone is how
  every provenance error of this session was made — four times, by four different readers.
  - **`NO RECORD MATCHED` ≠ `NOT HELD`** (registry silent, laboratory knows).
    `registry_records.py get --pmid` answers *"is there a RECORD KEYED to this PMID"*. Its surface
    list **excludes `disease-models/wwox/analysis/` and `therapeutic_hypotheses_ledger_current.md`**,
    it reads **committed** state only, and it returns no match for a PMID sitting inside the *body*
    of a record on a surface it does read. **It prints its own warning and this session converted
    that warning into a negative — twice.** Pair it with
    `grep -rn "<PMID>" --include=*.md disease-models/`.
  - 🔴 **`not_processed` ≠ `NOT READ`** (registry stale, receipt and manifest exist). `PMID 30356099`
    carried `CORPUS-STUB-059` / `not_processed` while holding a **six-week-old receipt and a
    deep-dive manifest**. A whole re-read was spent before the ledger refused the duplicate receipt
    and exposed it.
  - **"No receipt" ≠ "unprocessed"** (receipt ledger silent, registry knows). `PAPER 003` is
    `integrated`, `clinical relevance HIGH`, a BLOCK-1 **safety anchor** — and carries no full-text
    receipt because it was processed from its abstract. It looked like a discovery twice.
  - **The cheap check that would have caught all three:** `grep -rn "<PMID>" --include=*.md
    disease-models/` **plus** a grep of `fulltext_read_receipts.jsonl` **plus** `ls
    research/deepdive_manifests/PMID<PMID>.json`. Three commands.
  - (The CLAUDE.md prohibition is on grepping the **two large registries** for records;
    `registry_records.py` covers those.)
- 🔴 **A brief that assigns a paper MUST order artefact persistence as step 1**, before analysis:
  body verbatim to `files/fulltext/PMID<PMID>_PMC_MCPtext.txt`, with bytes/chars/sha256. Four papers
  were read today and **could not be receipted** because their text lived only in an agent's
  context — see `FT-114`. Discovered *after* the contexts closed, i.e. at the cost of a re-read.
- 🔴 **`is_open_access:false` with `checked_sources:["pubmed"]` means PMC WAS NEVER CONSULTED.**
  **Three false negatives in this repository now**, the latest a paper that then delivered
  **46,589 characters**. Retrievability is established by **attempting the fetch and measuring the
  body length** — never by reading the flag.
- 🔴 **The publication gate's inheritance guard is conservative in one direction, and a DISCLAIMER
  trips it harder than the thing it disclaims.** Adding a clause that *denied* any link to the
  persistent disease-model genotype took the gate from **2 blocks to 6** — the guard tests for that
  genotype's *presence in the window*, and a denial puts it there. To attribute such material,
  **name the PMID and say nothing else about genotype class.** `STUDY_IDENTIFIER` requires a literal
  `PMID <digits>`, `PMC<digits>` or a DOI — **a bare number in a table cell does not match**, which
  is what blocked the first attempt. ⚠️ **The guard also cannot tell a rule ABOUT the topic from
  data OF the topic:** two drafts of *this very bullet* were themselves blocked. Write guidance
  about this guard using neither the two inheritance-side words nor the genotype phrase.
  **Read `scripts/public_release_gate.py` around `PARENT_OF_ORIGIN_PAIRING` before drafting; it is
  faster than three gate runs.**
- **The `UNREAD_PREMISE` ratchet is WWOX-corpus-scoped.** It fired on single corpus PMIDs twice
  today and stayed at `0/0` with six unheld non-corpus PMIDs in the tree. It protects against
  leaning on an unread **WWOX** paper, not an unread **anything**. Documented, **no gate proposed**;
  the six are queued as `FT-115` so they carry an anchor regardless.
- **The extractor also strips citation numbers**, not only italics and superscripts — markers render
  as `[]`. "Quote with its citation number" is **not satisfiable** from the MCP route. Attribute by
  content-match against the cited paper's abstract, and say that is what you did.

## 3 · Open flags left for the Operator — NOT resolved autonomously

1. **`DL-MECH-053` is `promoted-to-CC` and its cited dossier `staging/deepdive_PMID37974179_Dong2023.md`
   does not exist in this tree** (`research/staging/` is absent entirely). Per `reading_state.py`'s
   own header this may mean **unmerged or private, not lost** — recorded as *unverifiable here*.
2. **`DL-MECH-053` describes the proband as carrying *"un allele di sito accettore `del ex6-8` e un
   allele missense"*. `PMID 37974179` describes NEITHER** — it describes an in-frame exons 6–8
   genomic deletion plus two discontinuous genomic deletions. Those two phrases are exactly the
   public edition's reference-genotype class names, so this is **at least as likely a
   de-identification substitution artefact as a scientific error.** Both readings stated; neither chosen.
3. **Opening a WWOX MAVE would be a materially new research programme** — recorded as existing and
   costed in `FT-115`; **explicitly not proposed.**

## 3b · The two results that came after the first checkpoint write

### 🔴 The first therapeutic-class denominator this repository has ever had
[`woree_therapeutic_class_census_20260921.md`](woree_therapeutic_class_census_20260921.md).
`variant_triage_rescuability.md` set out the mechanism→lever logic with **two worked examples** and
said the full-set version was *"planned, resources permitting"*. This is it, at the depth the
evidence supports.

| Class | Alleles | % of 88 | Patients served alone | % of 44 |
|---|---:|---:|---:|---:|
| GENE-REPLACEMENT | **63** | **71.6 %** | **25** | **56.8 %** |
| PROTEIN-RESCUE *(conditional)* | 25 | 28.4 % | 6 | 13.6 % |
| **RNA-RESCUE** | ⊆ the 63, not separable | — | 🔴 **0 demonstrated** | **0 %** |
| READ-THROUGH | ⊆ the 63, not separable | — | 0 | 0 % |

🔴 **The finding is the asymmetry, not the percentage.** Gene addition is **allele-agnostic**, so by
mechanism its addressable share is 100 %. What 56.8 % measures is the **complement** — the share of
reported patients for whom **no allele-specific lever is conceivable on either allele**. The two
allele-specific levers are each bounded by a minority; the allele-agnostic one is bounded by none.

- **The denominator is 44, not 50.** The cohort abstract gives only percentages; 56.8/29.5/13.6 has
  a **unique exact integer solution over n ∈ [3,50]**: 25/13/6. Six individuals are carried as
  UNASSIGNABLE, not dropped.
- **`Q230P` is the most recurrent single WWOX allele of any class** — 8 patients, 6 families.
- **Zero WWOX alleles have a demonstrated productive splice outcome.** Every measured outcome is
  exon skipping toward frameshift. *"Splice-site"* licenses *"ASO-rescuable"* on **no row.**
- 🔴 **`PMID 30356099` (Piard 2019) — the "never read" finding was WRONG, and the correction is
  the more useful result.** The census concluded from `CORPUS-STUB-059` / `not_processed` that the
  largest WOREE series had never been read. **It was read on 2026-08-11** —
  `FTR-20260811-30356099-01`, with a **deep-dive manifest** and queue entry `FT-002` — off a Europe
  PMC XML surface of **45,559 characters**. That six-week-old receipt **already records verbatim**
  both sentences today's work presented as new, **and** that Q230P is the cohort's most recurrent
  missense allele at four families. Today's read was a **duplicate on a poorer surface** (33,357
  chars, `References` 0, no captions), now recorded as `FTR-20260921-30356099-02` with its parent
  declared. 🔴 **It was caught by the LEDGER, not by a reader:** `fulltext_receipts.py` refused the
  receipt — *"prior_receipt is null and this study already has 1 receipt(s)"* — and that refusal is
  what surfaced six weeks of stale registry state. **The real defect is that
  `paper_registry_current.md` still calls a twice-receipted, manifest-backed paper `not_processed`;
  fixing it needs a commit candidate.**
- 🔴 **And that paper threatens PROTEIN-RESCUE**, with a claim LEGEND did not hold: *"Up to 10 % of
  known disease-associated missense variants … alter pre-mRNA splicing"*, and that it is *"likely
  that a fraction of predicted missense variants … results in loss of expression due to abnormal
  splicing."* **An unknown fraction of the 25 missense alleles may not be missense alleles at all.**
  Under investigation as of this write.
- ⚠️ **Ascertainment:** severe-pole, consanguinity-enriched, parent-reported registry with
  documented survival bias. **56.8 % is plausibly a floor, not a ceiling.**

### The sensor question, and an assessment overturned by a sibling reader
[`wwox_activity_sensor_census_20260921.md`](wwox_activity_sensor_census_20260921.md).
**No single-cell fluorescence/FACS-readable WWOX activity reporter exists** — 24 queries, written
out. The **nearest thing** is a cell-surface lectin stain: WWOX knockdown → N-/O-glycosylation
defects → **increased plasma-membrane binding of HPA and GNL**, i.e. a WWOX-dependent epitope on the
**outside of an intact, unfixed, sortable cell** — a *better* starting point than TSC2's fixed-cell
pS6. ⚠️ `PMID 42523332` is a **preprint**, n = 30 cells, siRNA, RPE1, **zero replication**, and it is
a side observation in a Golgi-tethering paper.

🔴 **`F4` re-scored ⚠️ ADVERSE → 🟢 FAVOURABLE**, against a sibling Scientist's own file. The
original premise conflated WWOX's **binding** role (positive, scaffolding) with its **regulatory**
role (suppressive). Three independent axes are **gain-on-loss**: surface lectin binding ↑ on KD;
Wnt/β-catenin output ↑ on KD (**bidirectionally validated** — *"enforced WWOX expression inhibited,
and inhibition of endogenous WWOX expression stimulated"*); HIF1α glycolytic output ↑ in silenced
fibroblasts. **The § 6.C gate conclusion still stands**; what is retired is the stronger claim that
nothing in the literature points at what such a sensor might read.

🔴 **The substrate question has more texture than the inherited one-liner.** A **2011 enzymology
paper exists** (`PMID 21476439`, Bednarek group) reporting *"a course of enzymatic reactions for
**selected steroid substrates**, and … related Km values"*. **LEGEND holds it as `CORPUS P306`,
Tier C, `Claim links: none` — never read, never connected.** So *"no substrate has ever been
demonstrated"* is **FALSE**; *"no **physiological** substrate has been identified"* is **TRUE**, and
`TX-003`'s existing wording is already correct. It reduces the `F1` gap by **nothing**: a
spectrophotometric cuvette assay on bacterial crude extract is the opposite of a consequence
readable inside one intact cell.

⚠️ **A WebSearch fabrication was caught, and only because the paper was read.** WebSearch asserted a
2025 review says *"the true substrate(s) … remain to be identified"*. The body was fetched and
counted: `substrate` = **0**. **The sentence is not in that paper.** Treat WebSearch output as a
lead, never as a quotation.

### Integrity, measured not assumed
- **`trace_claim_foundation.py --all-drift`: 39 claims scanned, 1 finding — and it is already
  adjudicated inside `CLAIM 005`'s own `Evidence boundary`**, where the rat paper is cited **to
  refuse a transfer**, not to make one. Classified `CONTEXTUAL_DISSOCIATION`.
  [`claim_foundation_spot_check_20260921.md`](claim_foundation_spot_check_20260921.md).
- 🔴 **`CLAIM 001`'s safety anchor has never been read and cannot be read here.** `PAPER 003` /
  `PMID 41442931` — vigabatrin-associated brain MRI abnormalities in two WWOX children — has **no
  PMCID**, and `CLAIM 001` is 1/5 manifest-backed. The authors ask whether children with epilepsy
  *"related to the **GABAergic pathway or delayed myelination**"* are more susceptible — **WOREE has
  both.** ⚠️ That sentence is a **question**, not a finding, and must never be re-voiced as one.
  **This is now the sharpest acquisition item in the model.**
- `cross_claim_contradiction_census.py`: **46 candidate pairs, 38 not cross-linked.** Run and
  **deliberately not pursued** — adjudicating them *is* the fenced-off broad reconciliation.

### Release battery — read this before trusting a green
**The battery went 1 red → 6 red, and 5 of the 6 were ours.** Appending receipts drifts every
surface derived from the receipt ledger. `coverage_report`, `batch_queue`, `reading_state`,
`session_self_eval` and `paper_packet` all assert the committed derived surface still matches the
registries. **Regenerating them restored all five.** The order is forced and the tooling enforces
it: `derived_inputs.py` **refuses** to derive while the ledger is uncommitted, so **receipts land
first, surfaces rebuild against the committed tree** — Phase 4.7, arriving by another route.
**The sixth, `test_surface_census.py`, is not ours and was red before**: its two failures assert
`files/fulltext/` holds a structured deposit and the `PMID 17803050` Suzuki HTML, and `files/` is
gitignored.

🔴 **One self-inflicted process defect, recorded.** The publication gate returned
`BLOCK_PUBLICATION` and a commit happened anyway, because the gate was chained to the commit with
`&&` through a `grep` that **exits 0 whatever the verdict says**. That is the exact defect
`safe_push.py` was built to prevent — its docstring names the 2026-09-09 chained-gate incident.
**The control worked: nothing was pushed**, because `safe_push` runs the gate itself against the
exact SHA. **A gate's verdict must decide by exit status, never by a printed line someone greps.**

🔴 **And the gate is a floor, not a ceiling.** It caught one `REIDENTIFYING_VARIANT_COMBINATION` in
the class census and **passed a worse one** — a row pairing the same two variants more explicitly
*and* adding four population descriptors. Both were removed by hand. **A cohort has a provenance;
an individual's allele pair does not get one.**

---

## 3c · The therapeutic result that matters most, and three live files corrected

### 🔴 `TX-007`'s window caveat is half a finding and half an inference — and the authors say which half
[`tx007_window_and_ceiling_20260921.md`](tx007_window_and_ceiling_20260921.md). This matters because
the class census put **56.8 % of classifiable individuals in null/null**, whose only lever is
allele-agnostic gene addition. For that majority, the ceiling of `TX-007` is the whole question.

- ✅ **Measured half:** a neuron-restricted vector leaves radial glia transcriptionally and
  cell-cycle-wise untouched — **once**, in human organoids (`PMID 42397075`).
- 🔴 **Unmeasured half:** *"the older the patient, the smaller the reversible fraction"* has **no
  measurement behind it in any species.**
- 🔴 **No WWOX gene-therapy experiment in any living animal treats later than mouse P5.** One
  experiment varies age at all and spans **four days** (P1/P2/P3/P5; no P0, no P4; P300 survival for
  two arms; histology for one).
- 🔴 **And the authors state the reason themselves** — later dosing *"was not explored, as Wwox-null
  mice rapidly deteriorate"*, and the inability to assess later intervention *"likely reflects …
  model-specific biological constraints and technical limitations, **rather than a definitive
  boundary for therapeutic responsiveness**."* **The window is a property of a mouse that dies at
  3–4 weeks, not a demonstrated ceiling on the therapy.**
- **Where the ceiling IS measured it is high:** near-WT survival to 300 days (`p = 0.78`), SWD rate
  back to WT-indistinguishable, growth/glycaemia/fertility restored.
- **Closure is never measured, for any endpoint.** Onsets differ — prenatal migration vs postnatal
  and long myelination — and that is load-bearing. **But onset is not a deadline**, and the endpoint
  with *no* structural deadline (excitability) is exactly the one nobody tested late.
- **Never tested ≠ shown negative:** no treated animal was ever birth-dated or layer-stained.
  *"Prenatal defect"* does not imply *"unhelpable"* without a separate irreversibility argument
  nobody has made.
- ⚠️ All 40 locators re-matched 40/40, but **every one is second-order** (dossier- or
  manifest-derived) — `files/` holds none of the gene-therapy artefacts in this container.

### Three live files carried something false, all corrected
1. 🔴 **The myelin census's *"no g-ratio and no electron microscopy exist anywhere in this
   literature"*.** § 1 measured that correctly **in the paper it read**; an orchestrator note widened
   it to the field. **`PMID 34747138` holds both, first-hand.** And the truth is better than the
   zero: **g-ratio normalises under gene therapy while unmyelinated-axon counts stay significantly
   worse** — *thickness recovers, how many axons get myelinated at all does not* — with the caveat
   that the brackets run WT-vs-KO and KO-vs-rescued, **never WT-vs-rescued, so the residual gap is
   untested, not absent.**
2. 🔴 **`mechanism_intervention_map.md` R-01 described a construct that is not the clinical one** —
   it listed a **WPRE element**, which the 2026 clinical-track vector **removed deliberately**
   (*"a proactive risk-mitigation step to improve the predictability and control of neuronal WWOX
   expression"*). Not cosmetic: efficacy was recovered by **~6-fold more dose** without it, so dose
   expectations read off that row were out by that factor.
3. **`FT-116`'s *"mai guardati"*** was false for two of eight — see § 3d.

### `FT-116` triage — **MARGINALLY**, and one item is the session's most concrete opening
[`ft116_cohort_triage_20260921.md`](ft116_cohort_triage_20260921.md). Seven of eight are gene-list
mentions or pointers. The eighth (`37583270`, 4 WWOX children, India) carries a complete per-patient
variant table: **five new alleles, all null-like — not one new missense**, so the 19-allele missense
enumeration is numerically unchanged and the null-majority finding is reinforced.
- 🔴 **`c.517-3C>A`** — one nucleotide further into intron 5 than **`c.517-2A>G`** (`CLAIM 018`,
  consolidated baseline, the allele with existing patient-derived iPSC lines). Under investigation.
- **`c.790C>T` p.(Arg264Ter)** → **2–3 patients** (overlap with the 2025 registry cannot be
  excluded); would be the only nonsense allele reaching 3, and a **READ-THROUGH candidate** — the
  lever class with zero demonstrated members.
- **`35715422` correctly EXCLUDED**: likely-pathogenic + VUS alongside a pathogenic *ATP7A*
  frameshift with a Menkes phenotype. Not a WOREE patient.

## 3d · 🔴 The provenance join needs a FOURTH surface, and a fifth error mode appeared

[`staging_dossier_audit_20260921.md`](staging_dossier_audit_20260921.md). **Nine discovery-ledger
entries declare readings *"letti integralmente"* and cite dossiers under `research/staging/` — a
directory that does not exist here. Six of the nine have no receipt and no manifest either**, and two
of those six are **`promoted-to-CC`**.

⚠️ **This is NOT a claim the readings did not happen.** `reading_state.py`'s own header says a count
is true of one checkout; `staging/` is the shape of an uncommitted working directory, and the public
edition excludes a private overlay by design. **The audit demotes nothing and proposes no re-reading
campaign** — the one such reading independently redone today (`37974179`) **confirmed** its
declaration, 19/19 locators. It asks the Operator one cheap question instead: *does `research/staging/`
exist in the private or unmerged edition?*

**The join, with the fourth surface added:**

| Surface | What it cannot tell you |
|---|---|
| `registry_records.py` | `NO RECORD MATCHED` ≠ **not held** |
| Registry `Status` | `not_processed` ≠ **not read** |
| Receipt ledger | "no receipt" ≠ **unprocessed** |
| 🔴 **Discovery ledger** | **the other three are blind to it** — six readings are declared only here |

**And a fifth, different error mode:** `37095367` is filed in the ledger as *"del corrigendum"*. It
is **not** a corrigendum — it is the primary WGS article. Its `batch_queue` row carries **`✎ corrected`**,
meaning *has a correction*; it was read as *is a correction*. `32214227` and `31618474` carry the same
marker. 🔴 **A paper filed as an administrative corrigendum is a paper nobody will read** — and this
one reports a novel WWOX variant from a population LEGEND has zero representation from.

## 4 · Queue state at this checkpoint

| Entry | What it holds |
|---|---|
| `FT-112` | The retraction notice for `23446842` — **status entry, not a reading debt**. The HOLD it would justify is already on `CORPUS-STUB-179`. |
| `FT-113` | The prenatal/infant wave, five papers. **Closed**: W-1/W-2 gained nothing on all six axes; W-3/W-4/W-5 gained roadmap, stratification and uncertainty. |
| `FT-114` | 🔴 **Four papers read end to end that can never be receipted** — their text lived only in a closed agent context and `files/` started empty. The rule earned: **a brief must order artefact persistence as step 1.** |
| `FT-115` | The MAVE methodology, six papers. Two now read and receipted; **retrievability still UNTESTED on the other four** (`checked_sources:["pubmed"]` alone means untested, not blocked). |
| `FT-116` | 🔴 **39 neuro-relevant corpus records never triaged at all** — no registry record of any kind, ~14 with PMCIDs. **Eight actionable rows.** The useful residue is *multi-gene epilepsy cohorts reporting WWOX patients*, not redundant case reports. |
| `FT-117` | `42523332` read, receipted at **partial** depth, **debt declared**: `abstract`/`introduction`/`methods`/`limitations` `not_read`. Closes the ratchet honestly rather than by claiming a complete read nobody performed. |

**Receipts: 188 → 195** across this continuation. 🔴 **One receipt still owed**: `PMID 30356099`
(Piard 2019) was read and fingerprinted today and has **no receipt**, and its registry record is
still `CORPUS-STUB-059` `not_processed`. The stub→PAPER upgrade needs a **commit candidate**; the
receipt does not, and should be written next.

### The measure that matters, and the one that misleads
🔴 **"No receipt" is NOT "unprocessed."** A paper can be fully triaged, registered and `integrated`
from its abstract with no full-text receipt — `PAPER 003` is exactly that, and it looked like a
discovery twice today before the registry said otherwise. **Measure unprocessed work by registry
`Status`; measure reading depth by receipt.** They answer different questions.

---
---

## Current state — 2026-09-21, end of the PREVIOUS autonomous continuation

- `main` == `origin/main` · working tree clean · LINT **PASS** · publication gate **PASS, 0 blocks**
  · receipts **186 chained, tail anchored** · growth anchors **PASS** · `session_self_eval.py`
  **PASS** · release regressions exit 0 (every non-pass a declared environment absence).
- 🔴 **`UNREAD_PREMISE` ratchet: 2 → 0.** For the first time this repository leans on **no** paper
  that nobody has opened. Manifest baseline lowered to match; `growth_anchors` reports
  `RATCHET_IMPROVED`.
- 🔴 **The accessible reading queue is EMPTY, and that is measured rather than assumed.** Every
  copyright-verified open paper carrying no receipt has been read. What remains is **human
  acquisition**: packet items `A1`–`A9`, each with its route tried and recorded.
- **Read and receipted in this continuation (13 events over 11 papers):** `21766012` (+ correction)
  · `25650666` (adversarial re-read) · `27845895` · `25238782` · `24008736` · `41124647` ·
  `35573960` · `39101447` · `33134515` · `35328751` · `36271927` · `27869163`.
- **Tools shipped, both routed and regression-backed:** `scoped_record_edit.py` (16 tests) ·
  `extraction_damage_report.py` (11 tests).
- **Self-evaluation:** Parts 1–3 complete —
  `research/session_evaluations/2026-09-21_orchestrator_autonomous_continuation.md`.
  **Capability scout:** appended to `research/capability_scout_log.md` with the host-keyed preflight.

### The corpus-wide measurement, so nobody re-derives it

`extraction_damage_report.py` over all **29** local artefacts:
**29/29 italic-class counts INADMISSIBLE · 29/29 reference list ABSENT.**
So **no italic-class zero from any local artefact has ever been admissible as evidence**, and **no
citation attribution has ever been traceable from one**. Run the tool before offering any count.

## ✅ BATCH_20260921_001 — the four parked candidates are LANDED (2026-09-21)

**Operator-approved, propagated, `WM_v4.4 → WM_v4.5` (MINOR).** No claim reversed, no status
changed, no other pending candidate dragged in. **`D-17` deferred by the Operator and excluded.**

| Candidate | Canonical effect |
|---|---|
| `CLAIM032-ENDPOINT-QUALIFIER` | Title, Summary and dose corollary now name the endpoint class actually measured; `PREMISE: NOBODY_LOOKED` on cognition, EEG, network excitability. **State: «evidence insufficient for a general conclusion of no phenotype»** — and it still does not demonstrate disease in carriers. *"three independent laboratories"* **not propagated**. |
| `DETECTION-FLOOR` | `CLAIM 030`: *proteina assente* → *proteina non rilevata al Western blot*, `PREMISE: DETECTION_FLOOR`, aligned to `CLAIM 019`. |
| `CLAIM039-CEREBELLAR` | Title narrowed to the light-microscopy endpoint; boundary records that **neither stream establishes nor excludes** a cerebellar contribution. **Stays a rat-model claim**; human MRI not imported. |
| `PAPER34140629-PROMOTION` | `CORPUS-STUB-150` → **`PAPER 096`**, `T3`/`LOW`, generating no claim. |

**BLOCK 2 mirror rows 032 and 039 moved with their claims** — the defect the working model's own
previous last-update note recorded. Growth delta declared (`papers +1`). `batch_queue.md`
regenerated against the committed registries.

⚠️ **Remote housekeeping is BLOCKED BY TOOLING**, not by policy: deleting
`origin/claude/wwox-next-scientist-batch-n74f0z` (0 commits not on `main`) fails with
`send-pack: unexpected disconnect` on every attempt through this proxy. A second fully-merged
branch, `origin/claude/legend-architecture-evaluation-zovohw`, is also present and **was not
touched** — no authorisation was given for it.

---

## 🔴 The three results a cold reader should know before anything else

1. **Every therapeutic candidate this literature has produced acts by ANTAGONISING WWOX**, and an
   independent laboratory now says so in neurons. `PMID 35984507` (Coimbra, outside NCKU):
   *"**WWOX inhibition** by Zfra1-31 **restores** mitochondrial homeostasis and viability of
   neuronal cells exposed to high glucose."* With the pTyr33 peptide (`18371080`: *"activated WOX1
   plays an essential role in the MPP+-induced neuronal death"*) and the C1q axis (`19484134`:
   *"C1q activates WOX1 in neurons, which ultimately leads to cell death"*), that is three lines.
   **A WWOX antagonist has nothing to antagonise in a WWOX-deficient brain. This is a category
   objection, not a dosing one.**
   🔴 ~~Packet item `A9`; rests on an abstract, so it must be *read*.~~ **`A9` HAS NOW BEEN READ —
   2026-09-21, operator-supplied PDF + supplementary**
   ([`A9_fulltext_read_20260921.md`](A9_fulltext_read_20260921.md); `FTR-20260921-35984507-01`,
   `-02`), **and the reading narrows this bullet.** There is **no genetic WWOX arm**, **no
   inactive-peptide control**, and **total WWOX was never reported** although `ABN413` is in the
   methods and the blots are normalised to β-actin. So `35984507` shows that **Zfra1-31 is
   protective in neurons and lowers pY33-WWOX** — *not* that inhibiting WWOX is. And line 1 of the
   three appears *inside* `35984507` only as a citation to its ref [18], so under `D-15` it is not
   a second observation. **The category objection is unchanged and firmer** — inhibition and
   substrate-consumption point the same way in a genotype short of functional WWOX — but the
   sentence that carries it must now be the narrow one.
2. **The first node of the Chang cascade disclaims its own load-bearing step.** `25650666`'s
   Discussion asserts TGF-β1 dissociates WWOX from TPC6AΔ and, two paragraphs later, says
   *"Whether TGF-β1 regulates the binding of WWOX with TPC6AΔ **is unknown**"*. There is **no
   binding assay in the paper**. And `TRAPPC6AΔ` and `TIAF1` are **one measurement, not two**.
3. **All four levers the model cared about were finally tried in a WOREE null, and all four
   failed** (`35573960`): vigabatrin, ACTH, CBD oil, ketogenic diet. `n = 1`, null/null,
   day-one onset — **not a refutation for a genotype with residual protein**, and the ledger
   says so.

## Completed programme so far
1. **`SCIENTIST_CHANG_NS_…` waves 1–5** — closed, formally saturated.
2. **Fallback queue P1–P5** — closed.
3. **Open-ended continuation** (current) — dynamic queue, regenerated at each boundary.

## Standing commit candidates — `PARKED_PENDING_OPERATOR`, do not re-litigate
| Candidate | Class | One line |
|---|---|---|
| `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01` | MINOR | `CLAIM 032`'s cognition leg is *nobody looked*; headline quote is a tumour sentence |
| `CC-20260920-DETECTION-FLOOR-01` | MINOR | `CLAIM 030` says *proteina assente* where `CLAIM 019` says *non rilevata*; proposes `D-17` |
| `CC-20260920-CLAIM039-CEREBELLAR-01` | ORDINARY | *not cerebellar* rests on one hedged sentence; a P1 contradiction was read and never landed |
| `CC-20260920-PAPER34140629-PROMOTION-01` | MINOR | `CORPUS-STUB-150` → `PAPER 096` |

**None is a session blocker.** Revisit only if new evidence materially changes one.

## Live findings a cold reader must not re-derive
- **Six abstract-versus-results inversions** across six papers: `32764489` (brain engagement),
  `29067327` (Zfra pY33), `25650666` (null rendered temporal), `31543760` (p=0.0626 conjoined),
  `42092735` (neurotransmitter studies "normal" when never obtained), `25649963` (breast-cancer
  similarity unsupported). **In this literature the abstract does not index the results.**
- **Normal by blunt instrument, abnormal by sharp one** — four instances. Proposed as `D-17`.
- **The heterozygote phenotype is inside the control groups**, not missing from the literature.
- **Two "read but never landed" locators** (`CLAIM 016` lithium, `CLAIM 039` cerebellar) plus three
  more found in the narrow audit (spontaneous het tumours ×2, het bone deficit).
- **Zfra / all WWOX peptides: DISMISSED for WOREE.** No brain engagement; never dosed in a
  WWOX-deficient animal by anyone.
- **Lithium: DOWN.** One record in all of PubMed; no GSK3β inhibitor ever used in any WWOX context.
- **SDR missense readout: NO.** Nine of nine candidates fail on "would the protein even be there?"
- **`DL-MECH-021` lowered** medio → basso; domain-sufficiency arc demoted to author assertion; the
  seizure bridge withdrawn as a category transfer. **The platform survives.**

## Method rules earned here — apply, do not rediscover
- **Never grep `paper_registry_current.md` or `literature_tracking_log_current.md`** — use
  `registry_records.py`.
- **The MCP extractor elides gene lists into empty commas.** An abstract read through it is not a
  reliable index of a paper's content. *(This bit us on `PMID 41153369`, against our own registry.)*
- **No figure panel is inspectable in this environment.** No JATS, no PDF tooling, egress denied to
  NCBI/EBI/publishers. Per `D-14`, no figure-asserted negative may be adjudicated here.
- **A paper can be in PMC and outside the OA subset** — that is a permanent licence wall. Check
  `get_copyright_status` before re-queuing.
- **The broad `landing`-field audit is a definitional artefact** (74/81) and expands into the
  fenced-off mass reconciliation. Run that screen only against a specific claim under question.
- 🔴 **An identifier or a byline enters a durable record only by copy, in the same act, from a
  verified source — never from recall and never from a delegate's prose.** This failed **twice in
  two days**, both times mine, both times against a repository that already held the correct value:
  `FT-108` was written with `CORPUS P331` and "Hsu L-J … Chang N-S" (correct: `CORPUS P330`,
  first author **Hong Q**), and `FTR-20260921-21766012-01` was written with "Houlihan LM, Harris SE,
  Luciano M" (correct: **Hamilton G**, Harris SE, Davies G, Liewald DC, Tenesa A, Starr JM,
  Porteous D, Deary IJ — the queue entry and the analysis file both had it right). Corrected by
  append in `FTR-20260921-21766012-02`.
- 🔴 **Never re-fetch an article to a path an existing receipt already fingerprints, and check the
  ledger for the PMID before dispatching a read.** `PMID 25650666` was re-fetched to
  `files/fulltext/PMID25650666_PMC_MCPtext.txt` on 2026-09-21; the bytes changed
  (`9635516b…` → `c6e336a9…`) and the original is **unrecoverable**, because `files/` is in
  `.gitignore` and the artefact was never under version control. The earlier reading stands — its
  quotations are all present in the current artefact and were re-verified — but its fingerprint no
  longer binds to a file. Declared in `FTR-20260921-25650666-02` rather than quietly re-anchored.
- 🔴 **A DELEGATE'S CENSUS DESCRIBES THE FIELD, NEVER THIS REPOSITORY — and this cost three
  corrections in one day.** A census that says *"nobody has done X"* or *"paper Y is unread"* has
  measured PubMed, not LEGEND. **Before acting on any such statement, check the receipt ledger AND
  the discovery and therapeutic ledgers.** Today: `FT-102` was re-read a day after it had been read
  (stale queue entry); the two AAV9-SynI-WWOX papers were reported unread while carrying **four and
  seven** ledger events; and the oligodendrocyte-autonomy question was reported open while
  `DL-MECH-031` had settled it and `HYP-20260709-07` had been **parked** on it in July. **When a
  delegate chooses which paper to read, the ledger check must be written into the brief** — the
  Orchestrator cannot pre-check a paper it has not yet named.
- 🔴 **`is_open_access: false` is often a NOT-CHECKED reading, not a paywall.** Look at
  `checked_sources`: if it is `["pubmed"]` alone, PMC was never consulted and the flag means
  nothing. **A PMCID existing is not evidence of retrievability either** (`PMC4935222` and
  `PMC6965410` both resolve and both return a zero-length body). **Retrievability is established
  only by attempting the fetch and measuring the body length.** Both halves of this rule cost this
  session real work before it was written down.
- 🔴 **INTERROGATIVE-TO-DECLARATIVE RE-VOICING — a citation-fidelity failure mode that string
  comparison cannot catch.** A source's *question* is quoted accurately and re-attributed as its
  *finding*. Every content word matches, so quote-matching and grep find nothing; only reading the
  sentence's **grammatical mood** catches it. Found on `PMID 25238782`, whose abstract asks
  *"a question that emerges is whether fragility in these regions is only a structural 'passive'
  incident…"* and which was cited as having *concluded* that it is *"unlikely only a structural
  'passive' incident"*. **When auditing a citation, check the mood of the sourced sentence, not
  just its words.** Distinct from the seven abstract-versus-results inversions recorded here, which
  are contradictions *inside* one paper.
- **A stale queue entry will dispatch duplicate work.** `FT-102` still read *"non acquisito"* a day
  after the paper had been read. Close a queue entry in the same cycle as the read, not later.
- **A zero string count for a gene symbol in MCP body text is an instrument reading, not a
  negative.** Demonstrated conclusively on `PMID 21766012`: `TRAPPC6A` occurs **zero** times in the
  body — as do `APOE`, `APP`, `BIN1`, `CLU`, `PICALM`, which the paper is entirely about — while the
  symbol **survives intact in the PubMed metadata abstract**. The extractor deletes italicised
  tokens. Under `D-15`, never let such a count carry a negative; rest the conclusion on study
  design stated in Methods, or on prose you can quote.

## Next queue, ranked (as of this write)
0. **Landed this cycle:** `FT-102` / `PMID 25650666` (adversarial re-read — internal contradiction
   on the load-bearing binding step; human arm is an age-confounded null; TPC6AΔ and TIAF1 collapse
   to **one** node) and `FT-073` / `PMID 27845895` (the DisMech quote is real but is the strongest
   of four statements, and the axis **attenuates** death when WWOX is scarce). `DL-BIO-004` and
   `DL-MOL-008` updated; `PMID 18371080` added to the acquisition packet as **A6**.
1. ~~**FT-090** / `PMID 25416187`~~ — **CLOSED, `EVIDENCE_BLOCKED` (licence).** `PMC4935222` is a
   metadata-only stub (`full_text:""`, `is_open_access: false`, `found_in_pmc: 0`). **But the
   question that mattered is answered from metadata: `27551470` cites a REVIEW as evidence**
   (`article_types` includes `Review`; *"The aim of this review is to summarize…"*). The chain does
   not bottom out there — it passes through. Acquisition debt `A7`; **ask for the reference list,
   not the body.**
2. ~~**FT-018** / `PMID 28123895`~~ — **NOT ACCESSIBLE.** The surface census already records it as
   `idIsNotOpenAccess` / `pdf_only`. Do not re-dispatch; it is acquisition work.
3. ~~**FT-098 / FT-099** — the other two independent `TRAPPC6A` cohorts.~~ **CLOSED.** `FT-099`
   read (fails its own permutation); `FT-098` licence-walled. With `FT-097` already null, **all
   three legs of the `TRAPPC6A` node-independence claim are down and the claim is retracted in
   full** — see the retraction appended to `chang_ncku_wave2_node_independence_20260920.md`.
4. ~~**FT-092** / `PMID 25238782`~~ — **CLOSED, read.** The 2016 framing is the faithful one: the
   chapter **proposes**, it does not conclude, and the phrase attributed to it is its **question**.
   Named the re-voicing failure mode above.
5. ~~**FT-074** — four mTOR/autophagy stubs two reasoning files already lean on.~~ **PARTLY
   CLOSED, and the standing negative is FALSIFIED as stated.** `24008736` read: it **fixes** the
   sign (WWOX ⊣ autophagy), four times, including a **germline `Wwox`-knockout MEF arm** that is
   loss-of-function, drug-free and non-cancer. The narrowed form that survives: the direction **is**
   fixed on **steady-state autophagy-protein abundance**; it is **not** established on **flux**
   (no clamp was ever applied to a WWOX manipulation, and the paper's own MG132 result shows LC3 is
   being degraded proteasomally in that system), **not** established in neural tissue, and the
   **mTOR-mediated route is asserted, never tested**. The two-directions standoff now reduces to
   **one** discordant paper, `36621327`, whose acquisition priority rises above the other two.
6. **`PMID 27869163`** (Wwox–Brca1, CC BY-NC-ND) — copyright-verified open, never dispatched.

## Permanently evidence-blocked — do not retry automated routes
`15126504` (`FT-024`, no PMCID) · `27569545` (`FT-105`, **licence wall**, verified) · `15026124`
(no PMC) · `33914858` (no PMCID) · `24369382` (empty PMC body) · `17803050` (no DOI/PMCID).
Packaged for a human in `acquisition_packet_20260920.md`.

**Added 2026-09-21, each verified with `get_copyright_status` and/or `convert_article_ids` — do not
re-test:**

| PMID | Why it is blocked | Where it now lives |
|---|---|---|
| `18371080` | **no PMCID** (record returns the PMID alone); Wiley paywall | `FT-109` · packet **`A6`** |
| `25416187` | PMCID **`PMC4935222` exists but is a metadata-only stub** — `full_text:""`, `is_open_access:false`, `found_in_pmc:0` | `FT-090` · packet **`A7`** |
| `26345274` | **no PMCID** | `FT-032` · packet **`A8`** |
| `33134515` | licence wall | `FT-098` |
| `33300063` | ⚠️ **weaker than first written — see the correction below** | `FT-074` |
| `31966718`, `36621327` | verified unobtainable earlier in this session | `FT-074` |
| `30094525` | ⚠️ **weaker than first written — see the correction below** | `FT-032` |
| `11719429` | ⚠️ **weaker than first written — see the correction below** | `FT-032` |
| `17360458` | `PMC1820689` exists, PNAS 2007, **not OA-licensed**; a local PDF exists but **this checkout has no PDF tooling** | `FT-032` |
| `28123895` | `PMC5214935`, `idIsNotOpenAccess` / `pdf_only` per the surface census | `FT-018` |

🔴 **CORRECTION TO THE THREE ROWS MARKED ABOVE, made the same hour, against myself.**
`is_open_access: false` is **not** a statement that a paper is paywalled. For `33300063`,
`30094525` and `11719429` the tool returned `source: "not_available"` with
`checked_sources: ["pubmed"]` — **PMC was never consulted**, so the flag records *what was not
checked*, not *what is not there*. Demonstrated within this session: `41124647` returned
`is_open_access: false` with `checked_sources: ["pubmed"]`, and its body then came back **in full at
68,491 characters**. Those three rows are therefore **not verified blocked**; they are *untested*.
The authority on whether a PMCID exists is **`convert_article_ids`**, and the only authority on
retrievability is **attempting the fetch and measuring the body length**. The rows that ARE verified
are the ones where `checked_sources` includes `pmc`, or where a fetch was attempted and returned an
empty body.

⚠️ **The stub trap, stated once so it is not rediscovered:** a **PMCID existing does not mean a body
exists**. `PMC4935222` resolves, round-trips through `convert_article_ids`, and returns HTTP success
with `"full_text":""`. **Check `get_copyright_status` for `found_in_pmc` and `is_open_access` before
dispatching a read**, and treat an empty body as a licence wall, not a transient failure.

**Copyright-verified OPEN and still unread:** `27869163` (Wwox–Brca1, CC BY-NC-ND 4.0, PMC5398941) ·
`35573960` (Front Pediatr 2022, `PMC9100683` — the tool reports `is_open_access:false` with a null
licence field, but Frontiers deposits full text, **so this one is worth exactly one fetch
attempt**).
