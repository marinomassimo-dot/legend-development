# Intake wave 2 — 2026-10-03 — Scientist B

`context_policy: SOURCE_FIRST`
Actor: scientist (Scientist B of intake wave 2). Branch `task/sci-B-20261003`.
Group B theme: the WWOX–tau/amyloid aggregation cascade and the neuronal kinase interface.

**Assigned question.** Of the proposed chain *WWOX loss → TRAPPC6AΔ/TIAF1 aggregation → caspase
activation → tau hyperphosphorylation and Aβ → neuronal death*, which link rests on a direct
measurement in neurons, and which on co-localisation, over-expression or one laboratory's reagent?

---

## 1 · The answer, link by link

| # | Link | Strongest evidence found, in the sources themselves | Neuronal? | System | Independent of the originating laboratory? |
|---|---|---|---|---|---|
| L1 | WWOX physically binds TPC6A/TPC6AΔ | Reciprocal endogenous co-IP (PMID 27551439 Fig 3c–d) in **HEK293**; everything else is FRET between over-expressed fusions | **No** | HEK293, COS7 | **No** — 0 of 9 `WWOX AND TIAF1` records lack Chang NS as author |
| L2 | WWOX loss → TPC6AΔ aggregation | siRNA knockdown in **COS7** (PMID 25650666 Fig 6, >80 % of cells); `Wwox−/−` **MEF** shuttling kinetics (27551439 Fig 2) | **No** | COS7, MEF (fibroblasts) | **No** |
| L3 | TPC6AΔ → TIAF1 aggregation, in this order | Inferred from knockdown asymmetry and shuttling kinetics; in vivo it is **co-localisation + antibody-FRET** in `Wwox−/−` cortex (27551439 Fig 7a–c) | in vivo brain, but co-localisation only | mouse cortex | **No** |
| L4 | Aggregation → caspase-3 activation | **Transient over-expression** of TPC6AΔ in SK-N-SH (25650666 Fig 4D–J) | **Yes, a neuroblastoma line** — over-expression | SK-N-SH | **No** |
| L5 | Caspase → APP degradation → Aβ | Aβ immunostaining ratio after TGF-β1 in over-expressing SK-N-SH (25650666 Fig 4A); the APP-Thr688 step is asserted in reviews, measured in none of these six | over-expression only | SK-N-SH | **No** |
| L6 | WWOX loss → tau hyperphosphorylation | pT181-tau **aggregate counts on brain sections**, n = 5, p = 0.0176 (25650666 Fig 5D) — not a phospho-western | in vivo, but a count | `Wwox−/−` mouse | **No** |
| L7 | WWOX binds tau via the SDR domain / restrains GSK-3β, ERK, JNK | **Not measured in any of these six papers.** It is a review sentence (PMID 34359949) resting on two same-laboratory primaries, refs 41 and 49 | — | — | **No** |
| L8 | → neuronal death | Over-expression toxicity in SK-N-SH, where wild-type TPC6A is **equally potent** as the Δ isoform (27551439 Fig 4a) | over-expression | SK-N-SH | **No** |

### Counted independence

Every count below is a PubMed `esearch` run on 2026-10-02 with `tool=LEGEND-research`.

| Query | Records | Without `Chang NS[au]` |
|---|---:|---:|
| `WWOX AND TIAF1` | 9 | **0** |
| `"TRAPPC6A" AND (aggregation OR plaque)` | 4 | **0** (all four are B1, B2, B3, B4) |
| `Zfra` | 17 | **1**, and that one is an unrelated zebrafish androgen-receptor paper matching the string by accident |
| `TIAF1` | 20 | 5, all incidental gene-list hits (Wilms tumour, Treg signature, Hirschsprung, oesophageal grade, exome burden) — **no functional work** |
| `WWOX AND "dorsal root ganglion"` | 1 | **0** |
| `WWOX AND tau` | 16 | 6 |
| `WWOX AND Alzheimer` | 32 | 16 |

Self-citation share of each paper's own bibliography (authorship resolved by PubMed `esummary`,
or from the citation strings where the deposit carries no PMID):
27551439 **54 %** · 25650666 **41 %** · 36498839 **48 %** · 29067327 **52 %** · 34359949 **47 %** ·
19918364 **21 %**.

### The answer in one paragraph

**No link of the chain is supported by a direct measurement in a neuron with a WWOX genotype.**
The two links that touch neurons at all (L4, L8) do so by transient over-expression in one
neuroblastoma line, and in that assay the wild-type isoform is as toxic as the Δ isoform, which
removes the Δ isoform's special status from the assay that is supposed to establish it. The two
links with in-vivo WWOX genotype (L3, L6) are immunostaining — co-localisation and aggregate
counts — in a constitutive null that dies at about a month. L1 and L2 are fibroblast and kidney-line
results. L7, the link that matters most for an SDR-destabilising allele, is **not measured
anywhere in this group**: it appears as a review's sentence, and in that review the direct-binding
phrasing occurs only in the abstract. Outside the originating laboratory the entire TRAPPC6AΔ/TIAF1
node has **zero** records.

### Where a statement is only a review's sentence

1. *WWOX binds tau via the C-terminal SDR domain* — 34359949 **abstract only**; the body states the GSK-3β version and cites two same-laboratory primaries.
2. *Aggregation takes "less than 15 days after birth"* — 34359949 §7.2; a ceiling imposed by the null mouse's lifespan, not a measured latency, and juvenile rather than embryonic.
3. *`Wwox+/−` mice decline faster than 3×Tg* — 34359949 §7.2 and 36498839 §2.5, both citing 29067327, whose only supporting panel is self-inconsistent (below).
4. *"The stronger the binding, the better the suppression"* — 34359949 §10.3; an analogy transferred from cancer, used to motivate a therapeutic programme.
5. *Caspase-mediated APP Thr688 dephosphorylation* — stated in 29067327's introduction and 34359949 §7.2; measured in none of the six.

---

## 2 · What the figure inspection changed (the two debts)

**PMID 25650666 (prior `partial_fulltext_read`, `figures: unavailable`).** The PMC figure rasters
are 550 px wide and unreadable at panel level; panels were taken instead from images embedded in
the article PDF at 1500–1750 px. Three findings were invisible before:
- Figure 3A: the human filter-retardation null carries **p = 0.942** (TPC6A) and **p = 0.850**
  (TIAF1) while p-WWOX (0.036), NFT (0.014) and Aβ (0.003) separate on the same blot — so the null
  is not an assay failure, and the abstract's "preceding Aβ generation" is a reading of a flat
  cross-section.
- Figure 5D: the pT181-tau claim is `+/+` ≈ 11, `−/+` ≈ **6**, `−/−` ≈ 26 aggregates, n = 5,
  p = 0.0176 — **the heterozygote is below wild type**, so the panel carries no gene dosage.
- The supplementary PDF contradicts the Methods on antibody numbering (84–100/Tyr112 vs
  70–86/Tyr116 for the identical peptide).

**PMID 29067327 (`FT-104`).** Supplementary Figure 1, extracted from `mmc1.docx` and rendered, is
the paper's only WWOX-genotype datum — and **its numbers do not reproduce its own legend**. The
legend claims a >55 % memory drop in `Wwox+/−` at ages 10–12; the figure's axes read 3, >10, 8, 10
months, carry **no genotype label at all**, have no age 12, no n per bar and no test, and under
either assignment of bar pairs to genotypes the drops are ≈ 43 %/13 % and ≈ 52 %/33 %. This is the
sole support for a claim that B3 and B6 both carry forward.

## 3 · The 3×Tg paper, as asked

It is **not a WWOX model**: `Psen1` M146V + APPswe + tau P301L, wild-type `Wwox`.
Dose 2 mM Zfra4–10 in 100 µL PBS (the melanoma arm uses 1 mM in water), tail vein, four weekly
injections from 10 months, PBS sham as the only comparator — no vehicle+scrambled arm, no
dose–response, no pharmacokinetics. **Blinding and randomisation are not mentioned**: the strings
`blind` and `randomi` occur **zero times in all six artefacts of this group**. Group sizes are
mutually inconsistent four ways (Methods 5/5; Fig 1A 6/5; Fig 1B 12/10; Fig 2 3/5) and the
histology statistics are computed over fields (n = 10) and cells (n = 40), not animals —
pseudoreplication in a cohort of at most ten mice.

## 4 · What would change the model if true, and what would falsify it

**Would change it.** If TPC6AΔ aggregation were shown, by any other laboratory, in WWOX-deficient
*neurons* — iPSC-derived or primary — with an antibody validated against a genetic null, the
cascade would become a usable mechanism rather than a one-laboratory narrative, and the
heterozygote plaque result (36498839 Fig 5C) would become a carrier biomarker candidate.

**Would falsify it.** (a) An isoform-resolved human measurement showing no TPC6AΔ excess in
WWOX-deficient brain. (b) Demonstration that the pS35-TPC6AΔ antiserum detects a different
epitope — the antibody is validated by peptide blocking only, in every paper of the group. (c) A
`Wwox−/−` brain at P15–P21 with no tau or Aβ excess measured biochemically rather than by section
counts. (d) For L7 specifically: a WWOX–tau co-IP or structural measurement from outside this
laboratory that fails.

**The cheapest discriminating experiment** is not more mouse brain: it is to run the existing
pS35-TPC6AΔ and TPC6AΔ antisera against `TRAPPC6A`-knockout lysate. Every claim in the group
depends on those two reagents, and no genetic-null validation of either exists anywhere.

## 5 · The directional problem the model should carry

PMID 19918364 is the one record whose direction is **pro-death for activated WWOX**: in rat DRG,
injury raises `Wwox` mRNA within 30 min, nuclear pY33-WWOX accumulates over two months, and
over-expressed WOX1 suppresses CREB-, CRE- and AP-1-driven reporters while enhancing NF-κB. Three
bounds found in the source: the promoter assays are **HEK-293 fibroblasts with Gal4 fusions**, not
neurons; the chronic accumulation is **equal on the uninjured side** (≈ 72 % contralateral vs
≈ 71 % ipsilateral at month 2, Supplementary Fig S3), with sham animals already at 31–37 %, so
axotomy is not its sufficient cause; and the "co-activation" percentages in the abstract are
**bin labels from a categorical heat map** (Fig 4) with no n, no error and no test. The paper's
own neuronal death at the endpoint is "less than 5 %".

Also confirmed against the source: the paper defines small/medium/large **only** by diameter
(<20, 20–30, >30 µm). `nocicept`, `unmyelin`, `IB4`, `CGRP`, `substance P` occur **0 times**. The
earlier LEGEND audit was right — the size→modality labelling is imported convention.

## 6 · Anything in the assignment that was wrong

- The selection describes 25650666 as putting "tau pathology in a *young* WWOX-null brain". True as
  far as it goes, but the panel shows **no heterozygote intermediacy** — the `−/+` mean is below
  wild type — so it is not evidence of a dose-dependent `Wwox` effect on tau.
- The selection calls 36498839's heterozygote result "pT12-WWOX aggregation". The pT12-WWOX
  **immunointensity** panel reports **p > 0.05**; only the plaque count is significant, at n = 3
  with one of three animals near zero.
- The wave-1 observation that reached me as context ("26 of 56 references in one such paper were
  the same laboratory") is of the right order: measured here, 41–54 % across five of the six, and
  21 % for the 2009 paper.
- One premise of the brief holds exactly: `WWOX AND TIAF1 NOT Chang NS[au]` returns **0**, re-run
  2026-10-02.

## 7 · Receipts, manifests, candidates

Receipts prepared (not recorded): `scratchpad/receipts_pending_w2/sciB_<pmid>_1.json` for
27551439, 25650666, 36498839, 29067327, 19918364, 34359949.
Manifests: `deepdive_manifests/PMID<pmid>.json`, six, each `VERDICT: PASS` with 0 gaps and 0
ratchets under `deepdive_manifest.py --verify-artifacts`.
Candidates: `CC-20261003-B-CASCADE-INDEPENDENCE-01`, `CC-20261003-B-ZFRA-TRANSFER-01`,
`CC-20261003-B-WWOX-DIRECTION-01`, `CC-20261003-B-REGISTRY-01`.

> Nothing here is medical advice. All patient-level material is described at class level only.
