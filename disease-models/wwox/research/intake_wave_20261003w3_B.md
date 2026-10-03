# Intake wave 3 — 2026-10-03 — Scientist B (group B)

**context_policy:** `SOURCE_FIRST` — every source was opened knowing only its identity, its acquisition
state and the assigned question; each first pass was written before any registry statement about that paper
was read, and the comparison follows below.
**Author:** ACTOR_ID `scientist` (Scientist B), branch `task/sci-B-20261003w3`.
**Assigned question.** What does each source add to, or limit in, the claim that WWOX loss deranges a
*measurable* organelle endpoint — mitochondrial membrane potential and ROS, lysosomal/autophagic flux,
Bcl-2-family protein turnover, aggregate load — and in which direction, given that the literature contains
directly opposing statements about whether WWOX activates or suppresses autophagy?
**Instruction.** Characterise the contradiction; do not decide it.
**Not medical advice.**

---

## 1 · The six papers at a glance

| # | PMID | Verdict | Depth | What is new versus held |
|---|---|---|---|---|
| B1 | 21368882 | **INGEST** (debt closed, **earned null for WWOX**) | partial | No registry record of any kind existed. WWOX is not manipulated or measured in this paper |
| B2 | 41677633 | **INGEST** | partial | The direction nothing in LEGEND recorded: WWOX **loss is protective** under serum starvation, on three organelle endpoints |
| B3 | 24008736 | **INGEST** | partial | Panels and densitometry; the flux clamp is on the drug, not on WWOX; **the deposited supplement is another article's** |
| B4 | 21212468 | **INGEST** (ABSTRACT-SUFFICIENT in substance) | complete | A perspective with no experiment; every mitochondrial datum is secondary |
| B5 | 38542478 | **INGEST** | partial | "Overrides" is asserted twice at two strengths and measured nowhere; it carries two independent-laboratory references that matter |
| B6 | 30158849 | **INGEST** (re-read, `FT-057`) | partial | The phospho-code maps to compartment and cell fate and to **no measured organelle endpoint** |

Dossiers: `fulltext_dossiers/PMID<pmid>.md` for all six. Manifests: `deepdive_manifests/PMID<pmid>.json`,
all six `VERDICT: PASS` under `deepdive_manifest.py --verify-artifacts`.

---

## 2 · The answer to the assigned question

### 2.1 Which endpoints are actually measured, and on what manipulation

| Endpoint | Measured in | Manipulation | Clamp / control | Direction |
|---|---|---|---|---|
| Mitochondrial membrane potential (rhodamine 123) | PMID 41677633 Fig 4C | constitutive `Wwox−/−` MEF vs `Wwox+/+` | serum-fed control; n = 4 | **WWOX present → ΔΨm collapses** (~0.34 vs ~0.79 of control) |
| ROS (DCF-DA) | PMID 41677633 Fig 8A | same | baseline equality shown (n.s. at 0 h); NAC arm | **WWOX present → more ROS under stress**, equal at baseline |
| Viability / sub-G0/G1 | PMID 41677633 Fig 4A, 4B | same | serum-fed control | **WWOX present → more death** |
| Bcl-X<sub>L</sub> / Mcl-1 protein | PMID 41677633 Fig 5, 7, S2, S3 | null, Tet-On overexpression, shRNA | mRNA unchanged; MG132 / CQ / NH₄Cl / E64d+pepA | **WWOX present → both fall**, by a protease-inhibitor-sensitive route |
| Autophagy markers (Beclin-1, Atg12–Atg5, LC3-II), GFP-LC3 puncta, EM autophagosomes | PMID 24008736 Fig 3, 4, 6 | overexpression, siRNA, shRNA, Y33R dominant-negative | E64d+pepA clamp **on the drug only** | **WWOX present → all fall** |
| Aggregate load (TIAF1, Aβ) | PMID 21368882 | TIAF1 knockdown/overexpression — **no WWOX arm** | — | not a WWOX result |
| ΔΨm, cytochrome c, Bcl-2/Bcl-xL | PMID 21212468 | cited only | — | secondary report of one prior primary |
| anything organelle-level | PMID 38542478, PMID 30158849 | none — reviews | — | — |

**Three of the four endpoint families named in the question are measured on a WWOX manipulation, and all
three move the same way: WWOX presence is the costly state under stress, and WWOX loss is the protected
state.** Aggregate load is the exception — it is measured in this group only in a paper with no WWOX arm.

### 2.2 The autophagy contradiction, characterised

| | "WWOX suppresses autophagy" | "WWOX activates autophagy" |
|---|---|---|
| Sources | PMID 24008736 (read here) · PMID 33300063 (abstract only; `CORPUS-STUB-056`) | PMID 36621327 (`CORPUS-STUB-043`; no PMCID, not readable) |
| Laboratories | two, **independent of each other** (Taiwan; a separate Chinese group) | one, independent of both |
| Cell type | human tongue SCC-15 / SCC-9 (epithelial carcinoma) · human ovarian carcinoma | mouse lung epithelium and human H292 |
| Stress | antimetabolite (methotrexate) · taxane (paclitaxel) | inflammatory injury (LPS) |
| Manipulation | overexpression **and** knockdown **and** dominant-negative **and** (one sentence) constitutive null | overexpression |
| Readout | static markers (Beclin-1, Atg12–Atg5, LC3-II), GFP-LC3 puncta, EM | LC3B-II, cited as marker |
| Flux clamp | **present, but applied to the drug, never to a WWOX manipulation** | not stated in the abstract; the body is unavailable |
| mTOR arm | physical interaction + phospho-correlation; causal order explicitly "a possibility" | "regulates mTOR and ULK-1 signalling" |
| Direction of the mTOR step | methotrexate **raises** p-mTOR in the WWOX-high line; WWOX knockdown suppresses that rise | WWOX overexpression **activates** autophagy via mTOR–ULK1 |

**What the contradiction is not.** It is not one laboratory contradicting itself, and it is not a single
paper against a single paper: the census (PubMed `esearch`, 2026-10-03, `tool=LEGEND-research`)
gives `WWOX AND autophagy` = 10 records, of which 8 are from neither Chang NS nor Hsu LJ.

**What it is.** Two poles that differ simultaneously in laboratory, tissue, stress class and direction of
the mTOR step — and in which **neither pole has measured the WWOX→autophagy step under a flux clamp**. The
readable pole has a clamp and spends it on the drug; the other pole's body cannot be read at all. A
disagreement between two static markers is not the same object as a disagreement between two flux
measurements, and until one side clamps a WWOX manipulation the sign is under-determined by construction.

**A third relation that is neither pole, and the one this wave adds.** PMID 41677633 does not say the
lysosome is WWOX's *target*; it says the lysosome is WWOX's *effector* — WWOX-dependent degradation of
Bcl-X<sub>L</sub> and Mcl-1 is blocked by chloroquine, E64d and pepstatin A. In the same SCC-15 background
the 2013 paper routes LC3 loss to the **proteasome** (MG132 blocks it). Same laboratory, same cell line,
opposite relation to the same organelle, different cargo. These two papers are therefore **not** a
contradiction, and reading them as one would be the easy error.

### 2.3 What would change the model if true, and what would falsify it

- **If true:** under cellular stress, WWOX function is a pro-death, pro-oxidant input at the mitochondrion,
  and removing it protects. For a genotype class defined by WWOX loss, that predicts a *stress-resistant*
  cell phenotype on these endpoints — the opposite of the intuition that a loss-of-function disease cell is
  fragile everywhere — and it makes any **WWOX-restoration** strategy a two-edged move whose cost appears
  specifically under stress. ΔΨm and DCF-DA ROS become candidate *pharmacodynamic* readouts (not endpoints
  in the §13 sense) for such a strategy, with NAC as an existing pharmacological handle on the loop.
- **What would falsify it for this model:** the same two readouts, measured in a neuronal system carrying
  the reference genotype class, with and without functional WWOX under a defined stress. If WWOX loss does
  **not** protect there, the direction is specific to fibroblast/epithelial systems and does not transfer.
  One independent datum already points the same way in neurons (PMID 35984507: blocking WWOX with Zfra1-31
  restores mitochondrial homeostasis and viability in neuronal cells under high glucose) — not read here,
  named as the control this wave did not run.
- **The transfer limit that must travel with every one of these numbers:** every loss-of-function arm in
  this group is a **constitutive mouse null**. A null models neither a destabilising SDR missense allele nor
  a splice-acceptor allele; a heterozygote arm exists nowhere in this group except as a cited aggregation
  phenotype in a review; and nothing here is a neuron.

---

## 3 · Comparison with what LEGEND already held (after the first pass, as the policy requires)

| What LEGEND held | What the source says | Disposition |
|---|---|---|
| `DL-MECH-016`: *«già integrato; full text riletto nel batch»* for PMID 41677633 | the ledger's own receipt is `partial_fulltext_read` over a text extraction, no figures, no supplement | corrected in `CC-20261003W3-B-AXIS-01` |
| `DL-MECH-016` records the mechanism and no direction of effect | the direction is the transferable part, and it is the inverse of the protective reading | added |
| `LIT-EX-005`: *«non-CNS … mechanically distant … not translatable»*, `filtered_out` | true about the cell systems; the paper also carries null-versus-wild-type organelle endpoints | corrected, and the duplicate identity with `LIT-0165` resolved (`CC-20261003W3-B-REGISTRY-01`) |
| `FT-074`: *«nessuno dei quattro letto»* | the record's own 2026-09-21 block says one was read | corrected (`CC-20261003W3-B-SUPPDEPOSIT-01`) |
| `FT-074` counts PMID 24008736's `Wwox`-null MEF arm among the four | that arm lives in a supplementary figure the deposit does not carry | declared, with the two routes measured |
| `FT-074`: the autophagy stalemate reduces to "one paper" | the axis has 10 records, 8 of them from other laboratories; a second independent lab is on the readable side | stated with the census |
| LEGEND's phospho-code source is PMID 30158849 | that review maps residues to compartment and cell fate, never to a measured organelle endpoint, and contains no pT12 | stated in `PAPER 147`'s record text |

### Where the wave-3 selection record was wrong
- **B2.** It states *«`Wwox`-null MEFs show higher ROS and death on serum deprivation»*. Both the running
  text and Figure 8A say the opposite: ROS and death are higher in **wild-type** MEFs; the nulls are the
  resistant ones, and ROS is equal at baseline. The inversion is the single most consequential error found
  in this wave's brief, because the whole therapeutic reading turns on it.
- **B1.** It calls the paper *«the upstream origin of the cascade»* with human data; accurate, but the WWOX
  content is nil, and the 17 % / 48 % figures are conditional prevalences inside TIAF1-positive samples in
  two groups whose mean ages differ by ~21 years. The abstract's *n* is in the body (41 and 97).
- **B3.** It says *«no bafilomycin clamp stated in the abstract»* and asks whether the LC3-II change is flux
  or steady state. A clamp exists (E64d + pepstatin A) and is quantified in a panel — but it is spent on the
  drug, never on a WWOX manipulation, so the question survives in a sharper form.
- **B4.** It calls the article *«a commentary-weight piece … by the originating group»*. Correct, and
  stronger than stated: the JATS deposit types it `research-article` and PubMed types it "Journal Article",
  yet it has no Methods, no Results and one schematic. Nothing in it is a measurement.
- **B6.** It expects the review to map the phospho-code onto the organelle outcomes B2 and B4 measure. It
  does not: no residue in it is tied to a measured organelle readout, and pT12 is not in it at all.

---

## 4 · Receipts, candidates, gates

**Receipts prepared, not recorded** (`scratchpad/receipts_pending_w3/`):
`sciB_21368882_1.json` · `sciB_41677633_1.json` · `sciB_24008736_1.json` · `sciB_21212468_1.json` ·
`sciB_38542478_1.json` · `sciB_30158849_1.json`.
Dry-checked by appending all six, in this order, to a throwaway copy of the ledger with a throwaway copy of
the state manifest: 290 → 296 events, `validate` returns `OK: 296 valid receipt(s)`. The live ledger and the
live manifest were not touched.

**Commit candidates:** `CC-20261003W3-B-REGISTRY-01` (MINOR) · `CC-20261003W3-B-AXIS-01` (MINOR) ·
`CC-20261003W3-B-SUPPDEPOSIT-01` (MINOR). Every op list was dry-run with `record_scoped_edit.py apply` on
`main` `0e6fd4e9b886`, exit 0.

**What this wave did not do:** no claim was created, qualified or reversed, and no working-model block was
touched. The direction found in §2 is the kind of datum that would eventually bear on a claim about WWOX
restoration, and it rests on one paper, one stress and a constitutive null — so it is recorded as a
research-layer lead with an explicit falsifier, not promoted.
