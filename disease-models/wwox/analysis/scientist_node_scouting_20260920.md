# Scientist-node scouting — which PI carries the next dedicated batch

**Date:** 2026-09-20 · **Mode:** READ-ONLY discovery/prioritisation. No gate, no protocol, no registry
change, no batch started. Non-canonical analysis file.

**Method.** Author census over `corpus_seed_pubmed_20260806.jsonl` (706 records, disambiguated
last-name+initials, affiliation-resolved), cross-joined against (a) identity-vs-mention PMID
occurrence in the seven registry surfaces via `registry_records.py`, and (b) receipt coverage from
`reading_state.md` (97 papers, 154 receipts). External completion via PubMed for the two named
hypotheses only. The corpus JSONL carries **no abstracts** — title/MeSH only — so a term absent from
a corpus title search is not absent from the field; every hypothesis below was re-checked against
PubMed directly.

---

## 1 · The coverage matrix that decides it

| PI (disambiguated) | corpus papers | senior-author | identity in registry | **read (receipt)** | neuro-titled |
|---|---|---|---|---|---|
| **Chang N-S** (NCKU / China Medical U, Tainan-Taichung) | **66** | 44 | 29 | **5** | 17 |
| Aqeilan R I (HUJI / Ohio State) | 65 | 44 | 62 | **53** | 9 |
| Aldaz C M (MD Anderson) | 38 | 21 | 33 | 8 | 7 |
| Bednarek A K (Lodz) | 37 | 27 | 29 | 3 | 5 |
| Huebner K (Ohio State) | 32 | 21 | 21 | 6 | 0 |
| **Hsu L-J** (NCKU) | **30** | 6 | 13 | **1** | 8 |
| **Sze C-I** (NCKU) | **23** | 4 | 14 | **2** | 13 |
| Richards R I / O'Keefe L V (Adelaide) | 9 / 7 | 7 / 2 | 8 / 6 | 1 / 1 | 0 |
| Suzuki H (TUAT, `lde` rat) | 5 | 2 | 5 | **3** | 4 |

**NCKU cluster as one lab** (Chang NS + Hsu LJ + Sze CI + Chiang MF + their trainees):
**72 distinct corpus papers · 5 with a receipt · 38 never entered a registry record at all.**

Aqeilan is saturated (53/65). Aldaz is mid-batch. **The largest unread coherent body in the entire
WWOX literature is the NCKU lab, and it is the body LEGEND has touched least.**

---

## 2 · Lithium — the field is three papers, and one is unread

`(WWOX) AND (lithium OR GSK3 OR glycogen synthase kinase)` returns **5 records in all of PubMed**
(PubMed, 2026-09-20). Two are off-axis (hepatocellular toosendanin/regorafenib, SARS-CoV-2 N protein).
The three on-axis:

| PMID | Paper | LEGEND state |
|---|---|---|
| 22193544 | Wang/Lu 2012 — WWOX ⊣ GSK3β via SDR 388–407 / L404 | `PAPER 056`, complete read, 5 receipts → `CLAIM 035` |
| 32000863 | Cheng/**Hsu LJ** 2020 — Wwox-null → GSK3β-mediated PTZ seizures, LiCl suppression | `PAPER 019`, complete read → `CLAIM 016` |
| 15126504 | **Sze/Chang** 2004 — WWOX down-regulation induces Tau phosphorylation | **`FT-024`, HIGH, UNREAD** |

There is no lithium PI. There is a **three-paper arc, two-thirds already read, whose third paper is a
Chang-lab paper sitting unread in the full-text queue.** `CLAIM 016` already records the decisive
negative: the `PMID32000863` image locator shows LiCl suppressed PTZ seizures in **all three
genotypes, wild-type included** — an anticonvulsant that works in a model that seizes, not a
WWOX-specific rescue. `DIS-009` already rejected the "WWOX-mimetic is safer than lithium" safety
argument (Suppl. Fig. C: WWOX inhibits GSK3β phosphorylation of GS-1 at ~82 % — generic docking-site
block, not substrate selectivity). `FT-022` (Castaño 2010, GSK-3β2 isoform) is the live
`REVIVAL_TRIGGER` and is **paywalled with the acquisition cascade exhausted**.

**Verdict: NOT YET as a scientist batch.** The remaining lithium work is `FT-024` + `FT-022` — two
items, already queued, already prioritised HIGH. It rides inside the NCKU batch; it does not justify
one.

---

## 3 · Zfra — one lab, one independent replication, and a sign problem

The Zfra literature is **~13 papers**, of which **11 are Chang N-S senior-author**. The only
independent node is Carvalho / **Moreira P I** (Coimbra), PMID 35984507.

The direction of effect is the finding:

- Moreira 2022 uses Zfra1-31 as **"the specific inhibitor of WWOX"** — it blocks WWOX pY33 activation.
- Chang's own 2024 review (PMID 38542478): *"Zfra binds WWOX to both N- and C-termini, which leads to
  **accelerated WWOX degradation**"*, while in the same abstract *"**WWOX limits the progression of
  neurodegeneration** … by binding tau and tau-hyperphosphorylating enzymes."*

**Zfra's proposed mechanism is the accelerated destruction of WWOX.** In a WWOX loss-of-function
genotype there is nothing to inhibit; against a destabilising SDR missense allele the direction is
actively wrong. The in-vivo evidence (tail-vein Zfra4-10, 3xTg-AD memory rescue, spleen Hyal-2⁺ Z
cells) is an oncology-immunology programme with an Alzheimer arm, not a LoF-rescue programme.

**Verdict: MECHANISTIC AUDIT, not a batch.** But the audit is worth doing, because the same lab
asserts the opposite sign elsewhere — `WWOX **deficiency**` drives the TRAPPC6AΔ → TIAF1 → tau → Aβ
aggregation cascade (PMID 26355344, 27551439). Whether that cascade is downstream of WWOX *loss* or
of WWOX *hyperactivation* is a single unresolved question inside one lab's corpus, and its answer
decides whether any Zfra-class intervention can touch WOREE at all.

---

## 4 · Recommendation

**Next scientist-specific batch: Nan-Shan Chang and the NCKU cluster (Hsu L-J, Sze C-I, Chiang M-F).**

**Batch name:** `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION`

**Research question.** *Does the NCKU lab's WWOX-deficiency neuro-proteostasis arc — phospho-switch
(pY33/pS14) → TRAPPC6AΔ/TIAF1/tau/Aβ aggregation → mitochondrial failure → GSK3β de-repression →
lysosomal degradation — survive LEGEND's locator discipline, and does any of its two peptide
intervention classes act downstream of WWOX rather than through it?*

**Scope.** 43-paper neuro/intervention pool identified; **24–28 to process**, excluding the
bubbling-cell-death / Z-cell / TIAF1-oncology mass. 40 of the 43 are unread.

**First five, in order:**
1. `PMID 27551439` — WWOX **dysfunction** induces sequential aggregation of TRAPPC6AΔ, TIAF1, tau, Aβ
2. `PMID 26355344` — the aggregation cascade bombards mitochondria under WWOX deficiency *(flagged `News` in PubMed article types — verify genre before weighting)*
3. `PMID 15126504` — `FT-024`, the third GSK3β source, closes or kills `CLAIM 016`
4. `PMID 41677633` — WWOX induction → Bcl-XL/Mcl-1 degradation **via lysosome** (2026, Hsu LJ senior)
5. `PMID 31752354` — WWOX N-terminal **cell-surface-exposed** epitopes WWOX7-21 / WWOX7-11

**What it can move.** `TX-003` (proteostasis — the lab has WWOX lysosomal biology and LEGEND's
missense route is CMA/lysosome: `D-02`, `D-03`, `DIS-001`); `TX-005` (closed or killed by `FT-024`);
a functional pY33/pS14 readout for missense alleles alongside `CLAIM 035`'s SDR assay; and — if the
surface-epitope work holds — an extracellular WWOX signalling claim that touches both the
non-cell-autonomous axis and protein-replacement as a delivery route.

**Principal risk.** The frame is contested: `PAPER 053` records Aldaz attributing the Chang lab's
pro-apoptotic/localisation claims to adenoviral-vector artefact, and the dispute lands on the SDR.
The corpus is overexpression-heavy, review-heavy and self-citing, and `D-14` was caught in a paper
this lab co-authored. The batch must be run with figure-image adjudication on by default.

**Runner-up.** Richards R I / O'Keefe L V (Adelaide) — Drosophila WWOX, aerobic metabolism and
mitochondrial respiratory complex, 8 of 9 unread; a screening platform rather than a therapy line →
`SMALL TARGETED BATCH`.

---

**STOP — awaiting operator approval before starting the batch.**
