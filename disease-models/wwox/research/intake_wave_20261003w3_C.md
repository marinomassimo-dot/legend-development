# Intake wave 3, 2026-10-03 — Scientist C

`context_policy: SOURCE_FIRST` for five of six papers; **`QUESTION_DRIVEN` and declared** for
PMID 41124647 (see below). ACTOR_ID `scientist`. Branch `task/sci-C-20261003w3`.
**Nothing here is medical advice.**

## Assignment

Group C of the wave-3 selection: themes 4 and 5 — the newest WWOX literature, and the DEE
gene-therapy / ASO literature that carries a transferable dose, window, vector or assay lesson.

**The question.** What does each source add to, or limit in, the claim that a WWOX-restoration
strategy is specifiable today — how much protein, in which cell types, by what route, inside what
developmental window, with what off-target organ risk, measured by what pharmacodynamic assay — and
which of those six parameters does each source actually *measure* rather than assume?

## Verdicts

| # | PMID | Verdict | New vs held |
|---|---|---|---|
| C1 | 41124647 | **INGEST** (re-read, resuming a declared-partial prior reading) | Two corrections to what the repository holds; the degradation mechanism itself is unchanged |
| C2 | 40349107 | **INGEST** (transferable method only) | New; no registry record existed |
| C3 | 39847501 | **INGEST** (transferable method only) | New; the selection's premise is corrected |
| C4 | 40263630 | **INGEST** (transferable architecture only) | New; the exposure record is internally inconsistent |
| C5 | 42181696 | **INGEST** (transferable method and a decisive negative) | New; the most consequential source in the group |
| C6 | 42521212 | **INGEST** (transferable method only) | New; the only portable pharmacodynamic asset in the set |

All six were acquired lawfully and free from Europe PMC REST `fullTextXML` into the root
`files/fulltext/`, hardlink-copied into the worktree. All six manifests validate with
`deepdive_manifest.py --verify-artifacts --require-current-schema` (VERDICT: PASS).
All six readings are declared **`partial_fulltext_read`**, because figure panels were inspected only
where named and reference lists were not read. That is said plainly rather than rounded up.

## The answer to the question, with its limits

**Of the six parameters, this literature measures three well, one poorly, and two not at all.**

- **Route** is the best-served parameter. ICV (bilateral neonatal, unilateral in NHP), ICV + IV when
  a peripheral organ is implicated, and intrathecal lumbar for an oligonucleotide in a preterm
  infant are all demonstrated with procedural detail. Route transfers better than anything else here
  because it is set by anatomy and capsid, not by the gene.
- **Cell-type reach** is measured, and the measurement is a warning: "pan-neuronal" promoters are not
  pan-neuronal, and the GABAergic compartment — the one WWOX work has repeatedly implicated — is the
  one that standard promoters miss. PMID 40349107 solves this by mining human regulatory genomics;
  PMID 39847501 reaches 36–46 % of PV⁺ interneurons from a Gad1 construct. **But WWOX's required
  cell set is unknown**, so there is nothing yet to aim at.
- **Off-target organ risk** is measured best of all, in PMID 40349107: blind-graded DRG and
  spinal-cord histopathology, nerve conduction, and serum neurofilament light as a toxicity
  biomarker with a stated separation (≥1,719 pg/mL in affected animals against ≤679 pg/mL with the
  detargeting element). DRG toxicity is an **AAV class effect**, so it transfers to any WWOX AAV
  programme unchanged.
- **Dose** is measured only as vector genomes, never as rescued protein per effect. And it is
  measured as something worse than a straight line: in two of the three animal studies the
  **highest dose was not the best dose**, and in PMID 42181696 the highest dose was actively harmful
  at both ages tested.
- **Window** is **not measured anywhere in this set.** This is the clearest correction this reading
  produces, and it reverses the premise under which the sources were selected (below).
- **Pharmacodynamic assay** is the parameter all the others quietly assume, and PMID 42521212 is the
  only paper that builds one. `WWOX AND HiBiT` returns **0** PubMed records (ESearch, 2026-10-03).

**The single most consequential datum is a negative.** PMID 42181696 obtained a blinded, randomised,
multi-endpoint rescue — survival 50 → 84.2 %, febrile seizures 11/15 → 2/13, spontaneous seizures
1.12 → 0.03 per mouse per day — and under that rescue the protein the therapy exists to raise did not
measurably rise (NaV1.1 ≈ 0.45 → 0.49 of wild type, not significant), while mRNA moved about 8 % of
the wild-type level. Either the assay cannot see the increment, or full normalisation is not needed.
Both readings lead to the same operational conclusion: **a restoration dose cannot be specified by a
programme whose assay cannot see the increment it is trying to produce.** The assay comes first.

**Limits of this answer.** Six papers, five of them about a different gene, none about WWOX. Every
transfer limit is written out in the dossiers and repeated in the candidates. The group assessments
show one industrial sponsor on its own product, one academic group reporting on a drug whose sponsor
co-authors the paper, and one method paper whose senior author declares consulting income from the
company whose proprietary ASO validates the assay. None of that invalidates the measurements; all of
it belongs in the record.

## Four places where the assignment's premises were wrong

Following wave 1's lesson, every sentence of the selection was treated as a hypothesis.

1. **PMID 39847501 is not a window lesson.** The selection called it "the transferable window
   lesson". The paper attributes its P10 failure to transgene level and distribution, not to
   development, and supports that with its own immunohistochemistry showing substantially restricted
   expression after P10 dosing and with the 7–14 days single-stranded AAV needs to reach therapeutic
   levels. It also says in terms that whether the phenomenon occurs in human infants remains to be
   established. The question the selection wanted settled **is** settled — and the answer is delivery,
   not biology.
2. **PMID 40349107's NHP group sizes are stated, not "unstated".** The selection flagged "'Well
   tolerated' is over a short NHP study with unstated n". The paper gives n = 3 per arm (n = 4 for
   one), a 50-day study, juvenile cynomolgus macaques of 16–20 months, no immunosuppression. The
   shortness is real; the missing n is not.
3. **PMID 41124647's two alleles are not both SDR missense substitutions.** The selection and the
   repository both treat P252A and P282A as a pair in the SDR domain. The paper's own Figure 1D
   places the SDR at residues 125–262 and puts P282A outside it.
4. **"Measured complete loss of function — the evidence class the registry's missense alleles lack"
   overstates what PMID 41124647 shows.** Supplementary Table 4 reports gnomAD allele frequencies of
   0.0063 and 0.0733 for the two alleles, and calls P282A "Tolerated" by SIFT and a "Polymorphism" by
   MutationTaster. An allele carried by 7 % of chromosomes is not a demonstrated organismal null,
   whatever an engineered overexpression assay in a thyroid-cancer line shows.

A fifth, smaller one: PMID 40263630's exposure is reported three different ways in the same article
(19 administrations over 20 months; seven doses of 30.5 mg plus ten of 8 mg; "a total of 94 mg").
The interval — 4 to 6 weeks, from measured CSF concentrations — is the part that can be carried.

## Receipts prepared (not recorded)

| PMID | File | event_id | reread_reason | depth |
|---|---|---|---|---|
| 41124647 | `scratchpad/receipts_pending_w3/sciC_41124647_1.json` | `FTR-20261003-41124647-02` | `inadequate_prior_coverage`, prior `FTR-20260921-41124647-01` | `partial_fulltext_read` |
| 40349107 | `scratchpad/receipts_pending_w3/sciC_40349107_1.json` | `FTR-20261003-40349107-01` | `first_read` | `partial_fulltext_read` |
| 39847501 | `scratchpad/receipts_pending_w3/sciC_39847501_1.json` | `FTR-20261003-39847501-01` | `first_read` | `partial_fulltext_read` |
| 40263630 | `scratchpad/receipts_pending_w3/sciC_40263630_1.json` | `FTR-20261003-40263630-01` | `first_read` | `partial_fulltext_read` |
| 42181696 | `scratchpad/receipts_pending_w3/sciC_42181696_1.json` | `FTR-20261003-42181696-01` | `first_read` | `partial_fulltext_read` |
| 42521212 | `scratchpad/receipts_pending_w3/sciC_42521212_1.json` | `FTR-20261003-42521212-01` | `first_read` | `partial_fulltext_read` |

Dry-checked by appending all six, in that order, to a throwaway copy of the ledger with a throwaway
copy of the state manifest: six `record` calls at exit 0, then `validate` → `OK: 296 valid
receipt(s)`. The real ledger and the real state manifest were not touched.

## Commit candidates

| id | class | what it proposes |
|---|---|---|
| `CC-20261003W3-C-ALLELE-CLASS-01` | MINOR | Correct `DL-MECH-047` (both residues in the SDR → only P252A) and `DL-BIO-001` (domain placement is the paper's, in Figure 1D, not the reader's arithmetic); add the gnomAD frequencies; fix the 2026 → 2025 year in `CORPUS P348` and `LIT-0348` |
| `CC-20261003W3-C-RESTORATION-SPEC-01` | MINOR | One research line (the six parameters and which are measured), one dismissal-ledger negative (no therapeutic window is bounded by this literature), one research candidate (acquire a WWOX pharmacodynamic readout before specifying a dose) |
| `CC-20261003W3-C-REGISTRY-01` | MINOR | A structured registry landing for the five PMIDs with no record, so `ORPHAN_COMPLETE_READ` does not block `BATCH_COMMIT` once the receipts land |

## Artefacts persisted into the corpus

| path | sha256 |
|---|---|
| `files/fulltext/PMID41124647_Zhang2025_PMC.xml` | `4d48045e3a67f0dd0b86f6fbff12819b66a88c7d6ac6f60b545b1881a9a5b6cb` |
| `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-g003.jpg` | `076059c2a61e0a6a27b49e21818af06b68c74dbaceb967b8585f830b37683313` |
| `files/fulltext/PMID41124647_Zhang2025_supplement/ADVS-13-e07602-s001.docx` | `6e402eff70ea9bc41fbd1d2516c12628e46b8847c5ffb97f9e0d9d9600b16b95` |
| `files/fulltext/PMID40349107_Aeran2025_PMC.xml` | `cce8fcc05fdc2ff133d9b76b800010f3344edffd52c0d7ec8a601d5ca444d98a` |
| `files/fulltext/PMID39847501_Chen2025_PMC.xml` | `61ab73c4264ebec5b1c1638187f4464007f89379899186eee573a6b8477a7986` |
| `files/fulltext/PMID39847501_Chen2025_supplement/jci-135-182584-g230.jpg` | `94186d85a1a52283ae7a3c75aac87b75338b770dec7c9b8ac619e87431540e19` |
| `files/fulltext/PMID40263630_Wagner2025_PMC.xml` | `6765e777d3ba6285200bf7d143c42c6959808d7805664a0599a1b2feb0fc9f77` |
| `files/fulltext/PMID42181696_Diaz2026_PMC.xml` | `6d8e80e74a5e4d06398e3e057daae09b5361f820acd29684d6f05b6b4fe2c82c` |
| `files/fulltext/PMID42521212_Saravanan2026_PMC.xml` | `7b745dec658a5556f4f57dcc60643898888b0008f02e3d4fdcbcad979450af56` |

The Europe PMC `supplementaryFiles` bundles themselves are **not** persisted: two fetches of the same
bundle minutes apart returned different SHA-256 digests, so the archive has no stable fingerprint and
only the extracted members are declared.

## Honest shortfalls

- No reference list was read for any of the six, and no multi-hop expansion was performed. The
  machine dependency screen (`dependency_integrity.py screen --manifest-block`) returned
  `SCREENED_CLEAN` for all six against the 2026-09-10 Retraction Watch snapshot, but a machine screen
  is not a reading, and the `references` coverage key says `not_read` in every receipt.
- Figure panels were inspected only where a number my question needed lived in a panel: Figure 1D of
  PMID 41124647, Table 1 of PMID 39847501, Figure 4 of PMID 40349107 and Figure 4 of PMID 42181696.
  Everything else is `captions_only`, which is why no reading is `complete_fulltext_read`.
- Supplementary PDFs for PMID 40349107, PMID 39847501, PMID 40263630 and PMID 42181696 were acquired
  but not opened. For PMID 42181696 that includes Table S1, the dose table — the doses quoted here
  come from the body text and the Methods, not from that table.
- One model-safety halt occurred early in the session and is reported in the handback. It stopped a
  single file-reading command; it did not touch any of the six readings, and nothing was reworded to
  get around it.
