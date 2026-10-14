# Intake wave 11 (2026-10-04) — Scientist A reading note

`context_policy: SOURCE_FIRST` for all three sources: each was read, and its first-pass observations
written, before any LEGEND registry record, ledger lead or working-model statement about it or its
mechanism was opened. **Nothing here is medical advice. Public edition — no individual-level record.**

**Assigned question.** Does any of PMID 37248434, PMID 38719828 or PMID 40336300 measure WWOX
enzymatic or ligand-binding activity independently of the Bednarek / Aqeilan / Chang laboratories?

## 1 · The three readings in one table

| PMID | Verdict | WWOX content | What was measured | Receipt |
|---|---|---|---|---|
| 37248434 (Taouis 2023, *Cancer Gene Ther*) | **INGEST** | High — a measured WWOX protein interaction, domain-mapped | Binding (yeast two-hybrid, co-IP in HEK293, endogenous co-IP in MCF7); HR function (DR-GFP); clinical correlation of a partner | `FTR-20261004-37248434-01` |
| 38719828 (Martínez-Lumbreras 2024, *Nat Commun*) | **OFF-AXIS, read as a method donor** | Three mentions, one Discussion sentence, no experiment | Binding of a *different* protein's WW tandem: NMR structure, ITC affinities, SAXS, RDC/PRE, causal mutant, cellular IP-MS | `FTR-20261004-38719828-01` |
| 40336300 (Lawrence 2025, *Endocrinology*) | **OFF-AXIS, earned null for WWOX** | **Zero occurrences** | 17β-HSD enzymology: product formation in transfected cells, mouse genetics, LC-MS steroid panels, proteomics | `FTR-20261004-40336300-01` |

All three are first readings; none had a prior receipt, and dedup returned `NO RECORD MATCHED` for two
of the three (the third was the stub `CORPUS-STUB-041`).

## 2 · The answer to the assigned question

**Enzymatic activity: no. None of the three measures any WWOX enzymatic activity.** Zero substrate
assays, zero cofactor measurements, zero catalytic-site mutants, zero kinetic constants, across all
three sources. The SDR-substrate claim is **untouched** by this wave's Group A in the sense of
corroboration, and equally untouched in the sense of refutation.

**Ligand binding: partly, and in a specific sense that must not be inflated.** PMID 37248434 is an
orthogonal-laboratory measurement of a WWOX **protein–protein** interaction — Institut Curie / INSERM,
no author or affiliation shared with the Bednarek, Aqeilan or Chang/Aldaz laboratories — and its
domain mapping lands on the **SDR region**: a WW1-WW2 fragment does not bind MERIT40, a WW2-SDR
fragment does, and abolishing WW1's PPxY binding (Y33R) changes nothing. So an independent group
reports that the SDR region of WWOX carries a *binding* determinant. But:

- it is a co-IP and a two-hybrid, not an affinity measurement — **no Kd, no stoichiometry, no purified
  protein, no structure**;
- the mapping is at fragment resolution, and the authors themselves phrase the SDR placement as a
  suggestion;
- "directness" rests on the two-hybrid format plus a personal communication;
- the SDR appears only as a **fragment boundary**, never as a catalytic entity.

So the honest summary is: **the corpus now holds one independent measurement showing the SDR region
binds a protein partner, and still holds no independent measurement of WWOX catalysis at all.** A
binding surface and a catalytic surface are different claims and this wave separates them.

## 3 · What each adds, bounds or leaves untouched for the wave-10 finding

Wave 10's reading of PMID 21476439 concluded that the WWOX SDR-substrate claim rests on one
laboratory's crude-extract assay and on motifs cited to PMID 10786676 (paywalled, unread).

**PMID 37248434 — adds, in a different column.** It adds the first orthogonal WWOX measurement read
in this wave, and it is binding, not catalysis. It neither supports nor weakens the substrate claim.
It does, however, show that WWOX work of real quality exists outside the three laboratories, which
narrows the "single-chain" diagnosis from "all WWOX biology" to "all WWOX **enzymology**".

**PMID 38719828 — bounds, by supplying the missing assay format.** It demonstrates, on an adjacent
protein, exactly the battery that the WWOX SDR question has never had: ITC on purified protein with
stated conditions, a construct boundary justified by data rather than annotation, domain coupling
measured rather than assumed, a causal mutant, a cellular check against a mutant control, and two
orthogonal techniques required to agree. It also contributes two cautions. First, a published
tandem-WW structure in that very system **was wrong because its construct was truncated** — and the
WWOX two-hybrid bait in PMID 37248434 was itself "a truncated SDR domain", so construct truncation is
a live hazard in both papers this wave read. Second, the intra-tandem **chaperoning** story that the
WWOX literature treats as settled was tested for PRPF40A and failed.

**PMID 40336300 — bounds, and answers the brief's sub-question.** *Is WWOX involved at all?* **No.**
WWOX occurs zero times; it is not mentioned, not tested, and not even present in the paper's own
proteomic census of testicular hydroxysteroid dehydrogenases. What it bounds is the **inference
method** behind the WWOX regiochemistry: a 17β-HSD family assignment does not deliver a substrate
(one residue at position 234 flips C19-steroid acceptance between orthologues), a substrate negative
in this family is condition-dependent (two published negatives for mouse HSD17B7 overturned by
raising substrate and lengthening incubation), and an activity assay in cells or crude extract has a
**measured non-zero endogenous floor**. That last point is the sharpest: it is independent evidence
that the crude-extract format behind the WWOX substrate claim cannot, without a catalytically dead
control, distinguish WWOX activity from background.

## 4 · What would change the model if true, and what would falsify it

- **Would change it:** a purified-WWOX ITC or NMR titration against MERIT40's 43–206 region giving a
  Kd and a stoichiometry would convert the SDR region from "binds something in a pull-down" to a
  characterised binding surface, and would make a structure-guided reading of SDR missense alleles
  possible for the first time.
- **Would falsify the binding reading:** a purified-protein experiment showing no WWOX-SDR/MERIT40
  interaction, or evidence that the co-IP is bridged by a third protein, would retire it.
- **Would falsify the enzymology reading in either direction:** a WWOX oxidoreductase assay run with a
  catalytically dead control (YxxxK motif), a substrate titration and a stated cofactor. Until that
  exists, both "WWOX has this substrate" and "WWOX has no measurable activity" are unproven.

## 5 · Where the brief's premises were tested against the source

| Brief statement | Verdict against the source |
|---|---|
| A1 "the only free, unread text that **measures a WWOX interaction**" | **Correct**, and the measurement is domain-mapped. The brief's uncertainty — "whether any Kd, stoichiometry or domain mapping is reported is unknown until read" — resolves as: **domain mapping yes, Kd and stoichiometry no.** |
| A1 "122 871 B, 179 WWOX hits" | Byte count correct. The WWOX occurrence count on the persisted artefact is **171**, not 179; a small count discrepancy, recorded because an uncorrected count propagates. |
| A2 "3 WWOX hits … transfer is to assay design only" | **Correct on both counts.** The three hits are one Discussion sentence and its reference. |
| A3 "0 WWOX hits … an earned-null risk, and a genuine possibility that it adds only the negative" | **Correct.** It adds the negative *and* three transferable bounds on the inference method, which is more than only the negative, but nothing about WWOX itself. |
| A3 "This tests that relative's enzymology with knockout + substrate work" | **Correct**, with one qualification the brief does not state: the enzymology is product formation in transfected HEK-293T cells at a single substrate concentration, not purified-enzyme kinetics. |

## 6 · Reading debts named by these readings

- PMID 37248434's manifest queues six gene-direct references with reasons; the load-bearing one for a
  future wave is **PMID 34998176** (Park 2022, Wwox-Brca1 resection), which bears on the contested
  direction of WWOX's effect on homologous recombination.
- PMID 38719828's only gene-direct reference, **PMID 22634283**, is already held with a
  `complete_fulltext_read` receipt — and that receipt records that **Aqeilan is a co-author** of it.
  So the one existing purified-protein affinity measurement for WWOX's WW domains is **not**
  independent of the originating chain either. That is a finding of this wave and it sharpens the
  original question: outside the three laboratories, the corpus now holds **one** WWOX binding
  measurement (PMID 37248434, no affinity) and **no** WWOX affinity or enzymatic measurement at all.
- The paywalled motif provenance (PMID 10786676 and the five other closed items named in the wave
  selection) is untouched by these three readings; none of them cites it.

## 7 · Artefacts produced

| Kind | Path |
|---|---|
| Dossiers | `fulltext_dossiers/PMID37248434.md`, `PMID38719828.md`, `PMID40336300.md` |
| Manifests | `deepdive_manifests/PMID37248434.json` (11 locators), `PMID38719828.json` (9), `PMID40336300.json` (7) — all strict PASS, 0 gaps |
| Candidates | `CC-20261004W11-A-ORTHOGONAL-01.md`, `CC-20261004W11-A-ASSAYSPEC-01.md`, `CC-20261004W11-A-SDRCLUSTER-01.md`, `CC-20261004W11-A-REGISTRY-01.md` |
| Receipts (prepared, not recorded) | `receipts_pending_w11/sciA_37248434_1.json`, `sciA_38719828_1.json`, `sciA_40336300_1.json` |

## 8 · What was not read, and why

A model safety classifier halted the response in which the rendered Figure 1 of PMID 37248434 was
being inspected. Per the wave brief the read was not retried in other words. Consequence: **figure
panels were not inspected for any of the three papers**, all three receipts declare
`figures: captions_only` and `evidence_depth: partial_fulltext_read`, and no number that lives only
in a panel is carried into any dossier, manifest or candidate. The six figure images of PMID 37248434
were nonetheless persisted and fingerprinted so that a later reader can close the debt without
re-acquiring. Supplementary material: `not_read` for PMID 37248434 (a single .ppt container) and for
PMID 38719828 (three PDFs and one xlsx, including the full ITC table); `not_present` for
PMID 40336300, whose deposit declares none.
