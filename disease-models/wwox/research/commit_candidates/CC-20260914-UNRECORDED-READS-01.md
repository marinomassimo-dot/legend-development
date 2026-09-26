# COMMIT CANDIDATE — CC-20260914-UNRECORDED-READS-01

**Actor:** `orchestrator` · **Date:** 2026-09-14 · **Mandate:** `SCIENCE-EXEC-20260914` step I1
**Class:** MINOR — three `PAPER` records created for readings already attested · **§21d consultation:** owed before propagation
Public, disease-level, de-identified. **Nothing here is medical advice.**

## 1 · The defect, and how the population was cut down

Joining the receipt ledger (`evidence_depth: complete_fulltext_read`, key `study_id.pmid`) against the
registry `Identifier` gave **six** completed readings with no registry record at all. Four of the six
turned out not to need a new `PAPER` record, and finding that out **before** writing them is the point:

| PMID | What it actually is | Disposition |
|---|---|---|
| 28373548 | *Editorial Expression of Concern* on PMID 16223882 | already recorded: `PAPER 082` carries `PUBLICATION_INTEGRITY_HOLD` naming it. **No record owed** |
| 30470736 | *Author Correction* on PMID 29724996 | already recorded: `PAPER 091` carries it as an attached ordinary Author Correction. **No record owed** |
| 42397075 | the refereed version of `PAPER 001`'s preprint | **already proposed** in `CC-20260826-PROVENANCE-01` §C as a successor record; propagate that, do not duplicate it here |
| 21212533, 33058734, 42082822 | three research papers read in full, in no registry | **this candidate** |

Writing six records would have invented two studies out of two editorial notices and duplicated
another actor's worked proposal.

## 2 · The three records, with every field sourced

Identity fields come from Europe PMC, queried 2026-09-14 (`EXT_ID:<pmid> AND SRC:MED`, `resultType=core`),
not from memory. Locator counts and receipts come from the manifests and the ledger.

### 2.1 · PMID 21212533 — Saeki 2011

`Biol Pharm Bull` 2011;34(1):146–149 · DOI `10.1248/bpb.34.146` · no PMCID
*Glycogen synthase kinase-3β2 has lower phosphorylation activity to tau than glycogen synthase kinase-3β1*
Saeki K, Machida M, Kinoshita Y, Takasawa R, Tanuma S.
Receipt `FTR-20260726-21212533-01`, `complete_fulltext_read`; manifest `PMID21212533.json`, **14 locators**.
**Canonical use today:** `DL-MECH-066` and `DL-MECH-068` in the discovery ledger, and **seven** occurrences in the
full-text queue, all under the single entry `FT-026` (measured 2026-09-15 at `a5bc548`). 🔴 The
consultation said "five times (`FT-026`–`FT-028`)"; five is the count of matching *lines* and the
other two entries contain none. Corrected against my own measurement, not copied; **no claim
cites it**.
Proposed `Role`: *isoform-discrimination anchor for the GSK3β node — the source of "tau is a disfavoured
substrate for β2", not "β2 is a weak kinase": on the synthetic peptide pGS-2 the two isoforms are
equally active.* `Claim links: none`. `Transferability`: T3 (HEK293T co-expression and in vitro).
**Boundary to travel with the record:** the Figure 3 titration series are **not matched** between
isoforms, so no fold figure may be taken from it.

### 2.2 · PMID 33058734 — Zeng 2021

`Am J Respir Cell Mol Biol` 2021;64(1):89–99 · DOI `10.1165/rcmb.2020-0145OC` · PMC7780991
*Cigarette Smoke and Nicotine-Containing Electronic-Cigarette Vapor Downregulate Lung WWOX Expression,
Which Is Associated with Increased Severity of Murine Acute Respiratory Distress Syndrome*
Zeng Z, Chen W, Moshensky A, Shakir Z, Khan R, Crotty Alexander LE, Ware LB, Aldaz CM, Jacobson JR,
Dudek SM, Natarajan V, Machado RF, Singla S. (byline from the Europe PMC core record, 2026-09-14)
Receipt `FTR-20260913-33058734-01`, `complete_fulltext_read`; manifest **32 locators**, schema v2 strict
PASS; dossier present; artefacts 46/46 present and digest-matching.
**Canonical use today:** `DL-MECH-012` (as its fourth, peer-reviewed leg) and `DL-REPO-002`; one mention
in the working model; **no claim cites it**.
🔴 **`Role` rewritten on `SCI-CONSULT-20260914-C` findings C5, C6 and C7.** My first draft called
this paper *"the peer-reviewed null on the inflammatory-cytokine endpoints"* and credited it with a
withdrawal it did not cause. Both are false, and the second would have reinstated in canon a framing
the discovery ledger corrected hours earlier. The text to apply, verbatim from the consultation:

> the peer-reviewed leg that **splits**: vascular leak and histologic injury are significantly
> greater under both LPS and MRSA, and endothelial cells isolated from the same animals secrete more
> IL-6, KC and MCP-1 under MRSA; what does **not** reproduce is the cytokine leg **in BALF, in vivo**,
> measured twice (LPS and MRSA) with no significant difference on twelve bars per figure. The model
> is an endothelial conditional deletion with about 85% residual knockdown, which is **not** the
> intratracheal siRNA model of `PAPER 094 (VPS numbering, PMID 28283473)`. 🔴 The "multi-tissue
> convergence" argument was withdrawn from `DL-MECH-012` in `BATCH_20260913_003 (VPS batch, never on main)` on other grounds —
> one laboratory's tissues, one unreviewed preprint — and **not** on this paper's reading.

`Claim links: none`.

### 2.3 · PMID 42082822 — Denkboy Ongen 2026

`Reprod Sci` 2026;33(5):1020–1025 · DOI `10.1007/s43032-026-02112-9` · PMC13230315
*The Role of WWOX Gene Variant in Hypospadias and 46,XY Disorders of Sexual Development*
Denkboy Ongen Y, Tezcan-Unlu H, Unal U, Efendi-Erdem E, Cecener G, Eren E.
Receipt `FTR-20260811-42082822-01`, `complete_fulltext_read`; manifest **9 locators**.
**Canonical use today: none at all** — the paper is cited nowhere in the registries, the working model or
the discovery ledger.
Proposed `Role`: *a human association this corpus does not support: the reading records that the father
carries the identical homozygous genotype and is reported unaffected, that his phenotype is inferred
from a treatment record rather than an examination, that the panel shows the two homozygotes are not
alike where the text says they are, and that a 100-control cohort is about twenty-five times too small
for the inference drawn from it.* `Status`: `filtered_out` on evidential grounds, record kept so the
exclusion is auditable. `Claim links: none`.

### 2.4 · The `Evidence depth` line, required on all three (finding C8)

Without it the three records classify `abstract`, `abstract` and `filtered`, the guard's registry
side stays at 63, and **42082822's complete reading sits under a status ranking below
`catalogued`** — so item 2 as first drafted reopened the gap `CC-20260914-EVIDENCE-DEPTH-01` closes,
three records wider. Each new record therefore carries, in the `PAPER 094`–`096` form:

| Record | Line to write |
|---|---|
| 21212533 | `**Evidence depth:** complete_fulltext_read — receipt FTR-20260726-21212533-01; manifest `deepdive_manifests/PMID21212533.json`, 14 locators` |
| 33058734 | `**Evidence depth:** complete_fulltext_read — receipt FTR-20260913-33058734-01; manifest `deepdive_manifests/PMID33058734.json`, 32 locators, 46/46 artefacts present` |
| 42082822 | `**Evidence depth:** complete_fulltext_read — receipt FTR-20260811-42082822-01; manifest `deepdive_manifests/PMID42082822.json`, 9 locators` |

**Citation completed (minor finding):** 42082822 is *Reprod Sci* 2026;**33(5):1020–1025**.

**Provenance ceiling, declared:** 0 of 12 artefacts are present on this disk for 21212533 and 0 of 2
for 42082822, so those two identity blocks rest on their manifests and an external bibliographic
lookup. Re-acquisition is owed before either record is cited outside this corpus.

## 3 · What this candidate does not do

- It creates **no claim**, moves no claim status, and writes no pathway, transferability or clinical
  relevance beyond what the three readings state at their locators.
- It does not touch `PAPER 001`, `PAPER 082` or `PAPER 091`.
- It does not promote any placeholder (step I3). It **does** carry an `Evidence depth` line on each
  new record (§2.4, finding C8); the six replacements and additions on existing records remain step
  E1's act, not this one's.

## 4 · Questions for the consultation

1. Is `filtered_out` the honest status for 42082822, or does a completely read paper with a recorded
   segregation failure belong at `background_only` with the failure in the `Role`?
2. Should 21212533 carry `Claim links: none` when `DL-MECH-066`/`-068` lean on it, or does the
   discovery-ledger use oblige a claim link that does not exist yet?
3. Is any of the three roles above an assertion the reading does not carry?

---

## BATCH DISPOSITION — appended by the integrator, append-only

**Status:** **RE-QUEUED** — recovered 2026-09-26 from the VPS backup (`06ee25a`). The VPS batch that disposed of this candidate never reached `main`: re-queued for `BATCH_20260926_ALDAZ`. Identifiers written on the VPS are annotated in place as `(VPS numbering)` / `(VPS batch, never on main)`; full-text queue ids were renumbered (see `disease-models/wwox/research/vps_recovery_20260925/README.md`).
