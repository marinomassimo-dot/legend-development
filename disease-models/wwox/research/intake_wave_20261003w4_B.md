# Intake wave 4 — 2026-10-03 — Scientist B (group B)

**Author:** ACTOR_ID `scientist` (Scientist B), branch `task/sci-B-20261003w4`.
**context_policy:** `SOURCE_FIRST` for four of six sources — identity, acquisition state and the assigned
question only, with the first pass written before any registry statement was opened. 🔴 **For PMID
33914858 and PMID 35328751 the policy is declared `QUESTION_DRIVEN` instead, and the reason is
structural**: the mandatory acquisition-state check (`fulltext_receipts.py status --pmid`, which the
brief requires *before* opening a source) returns the standing receipt, and these two receipts carry
`evidence_basis` fields that are several paragraphs of substantive findings about the paper. On a
re-read of a paper the laboratory has already read, `SOURCE_FIRST` is not achievable through the
prescribed route. That is a finding about the protocol, not an excuse, and it is listed in § 6.
**Assigned question.** What does each source add to, or limit in, the claim that WWOX dose is
*continuously* read out by the white matter — full loss → hypomyelination, partial loss → a measurable
sub-clinical phenotype, re-supply → a restored endpoint — and is the myelin or carrier phenotype
measured **cell-autonomously** or inferred from mixed tissue and a population association?
**Not medical advice.** Everything below is class-level: allele class × zygosity × phenotype band.

---

## 1 · The six records at a glance

| # | Record | Verdict | Depth | What is new versus held |
|---|---|---|---|---|
| B1 | PMID 33914858 (Repudi 2021, *Brain*) | **INGEST** (targeted re-read) | partial, 5 printed pages of 48 | The myelin quantities the registry deferred to an unobtainable PDF; **a heterozygote arm no LEGEND record mentions**; and the declared **absence** of the artefact behind the standing receipt |
| B2 | bioRxiv **PPR1124524** 🔴 *not peer reviewed* | **INGEST — research layer only** | partial | The Olig2-Cre deletion `CLAIM 003` names as its missing experiment — in a source that cannot discharge it; and a **near-null baseline** that reframes what it shows |
| B3 | bioRxiv **PPR1015434** 🔴 *not peer reviewed* | **INGEST — research layer only** | partial | WWOX moved **both ways in one model**; endogenous ~2× up-regulation rescues; a direct **negative on the HIF1α route** |
| B4 | PMID 35460704 (Dong 2022, *J Lipid Res*) | **INGEST — as a bounded negative** | partial | The "four WWOX carriers" resolve to three missense alleles, one ClinVar-**Benign**, no significance, **no comparator cohort** |
| B5 | PMID 35328751 (Baryła 2022, *IJMS*) | **INGEST** (re-read, prior coverage inadequate) | partial | The **overexpression arm**, absent from every LEGEND record — and it does **not** mirror the loss arm |
| B6 | PMID 33612478 (Liu 2021, *Aging*) | **OFF-AXIS**, stub upgraded | partial | Its own authors **withdraw** the WWOX–HDL-C association |

Dossiers: `fulltext_dossiers/PMID33914858.md`, `PPR1124524.md`, `PPR1015434.md`, `PMID35460704.md`,
`PMID35328751.md`, `PMID33612478.md`. Manifests for the four PMIDs:
`deepdive_manifests/PMID{33914858,35460704,35328751,33612478}.json`, all `VERDICT: PASS` under
`deepdive_manifest.py --verify-artifacts`.

**Why the two preprints have no manifest.** `deepdive_manifest.py` keys manifests by PMID
(`PMID<pmid>.json`), and `test_manifest_receipt_provenance` resolves each manifest to a receipt through
`study_id.pmid`. A `PMIDPPR1124524.json` would be a manifest no receipt can be matched to, which turns a
green suite red to record a reading honestly. The locators therefore live in the dossiers and in the
commit candidates, and this is recorded as a harness gap in § 6.

---

## 2 · The answer to the assigned question

### 2.1 The dose claim has three links. Only one of them holds as stated.

| Link | Evidence in this group | Verdict |
|---|---|---|
| Full loss → hypomyelination | B1: at P17 the **neuronal** conditional has 55 ± 35 vs 180 ± 40 myelinated axons per field in corpus callosum, a 2-fold drop in mature oligodendrocytes, more OPCs, higher g-ratio, no oligodendrocyte death | **Holds** — for the neuronal deletion, in development, n = 3 per genotype |
| Partial loss → measurable sub-clinical phenotype | B1's own heterozygote arm: bursting in 17 % of slices vs 0 % in controls and 86 % in the homozygote — **but no statistical test of the heterozygote, and no myelin, imaging or behavioural endpoint for it**. B4: in humans, three heterozygous missense alleles, one ClinVar-Benign, no significance, **no comparator cohort**. B2: heterozygous mice exist in the colony and are used for nothing | **Weakly supported and badly measured.** One allele is not silent; nobody has measured what it does |
| Re-supply → restored endpoint | B3: ~2× endogenous up-regulation rescues lifespan, locomotion and amyloid load in flies — **without restoring lactate**, through a different (methionine) route. B5: ~850× overexpression in fibroblasts **raises** lactate in two of four conditions instead of lowering it | **Does not hold as "restoration".** Re-supply changes outcomes without reversing the mechanism that loss engaged |

**So the white matter does not read WWOX dose continuously — and the model should stop expecting it to.**
What the group actually supports is a **threshold-and-challenge** picture: homozygous loss produces a
developmental deficit; one allele produces, at most, a sub-threshold electrophysiological signal nobody
has powered; and the oligodendroglial requirement is invisible at baseline and appears only under
ageing or toxic demyelination (B2: 117.6 ± 12.5 vs 125.1 ± 9 myelinated axons per field at baseline,
P = 0.22).

### 2.2 Cell autonomy, measured rather than asserted

| Source | Species | Allele | Autonomy as designed | Readout |
|---|---|---|---|---|
| B1 | mouse | Syn1-Cre **neuronal** conditional; plus Nestin-Cre, null, and **Syn1-Cre heterozygote** | **Non-cell-autonomous by construction** — the oligodendrocyte never loses the gene | EM axon counts, g-ratio, CC1/PDGFRα, LFP, conductivity |
| B2 | mouse + human snRNA-seq | **Olig2-Cre lineage** conditional; in vitro from **constitutive null** pups | Cell-autonomous **for the lineage**, and by culture isolation — *not* for an adult OPC: Olig2-Cre is neither inducible nor OPC-timed, and the in vitro arm uses the null, not the conditional | TEM, MBP, CC1/PDGFRα, SOX10, snRNA-seq, pull-down, CHX chase |
| B3 | fly | RNAi and CRISPRa, cell-type drivers | Cell-type-resolved: neuronal knockdown matters for amyloid toxicity, glial knockdown does not | lifespan, climbing, sleep, Aβ42, transcriptome, metabolome |
| B4 | human | heterozygous missense, unperturbed | Not applicable — association absent | HDL-C at cohort level |
| B5 | human fibroblast line | knockdown (called KO) and overexpression | Autonomous but in one non-neural cell line | uptake, lactate, enzyme activity, HRE reporter |
| B6 | human population | common SNPs, unperturbed | Not applicable | serum lipids |

**The two myelin sources are not two witnesses.** B1 and B2 share a senior author and a co-author. The
oligodendrocyte-intrinsic requirement rests today on **one laboratory and one unreviewed manuscript**.

### 2.3 The sharpest single result in the group

B1 and B2 produce the **same cellular signature — fewer CC1⁺ oligodendrocytes, more PDGFRα⁺ OPCs — from
opposite sides of the cell membrane.** Deleting WWOX in neurons gives it; deleting it in the
oligodendroglial lineage and then challenging gives it. A differentiation-block signature therefore does
**not** identify where WWOX is required, and any future readout built on CC1/PDGFRα ratios inherits that
ambiguity.

---

## 3 · What would change the model, and what would falsify it

| If true | Consequence |
|---|---|
| A peer-reviewed, **independent** oligodendroglial conditional reproduces the cuprizone repair deficit | `CLAIM 003` acquires a second, cell-autonomous component; "non-cell-autonomous" becomes "both, differently timed" |
| An **inducible, OPC-timed** deletion (PDGFRα-CreER) reproduces it | Cell autonomy is established for the adult OPC, which is what a repair therapy would target |
| A heterozygote shows a myelin or imaging endpoint with a real comparison | The dose claim's middle link becomes measurable rather than asserted |
| Endogenous ~2× WWOX up-regulation improves a **mammalian** myelin endpoint | The lever class of B3 becomes relevant to this disease rather than analogous to it |
| **Falsifier:** an Olig2 or CNP-specific *rescue* in a neuronal-deletion animal fails to improve myelin | The oligodendrocyte-intrinsic route is not the residual that `CLAIM 003`'s boundary hypothesises |
| **Falsifier:** a powered heterozygote cohort shows no electrophysiological or imaging difference | The 17 % bursting proportion was noise, and the carrier arm closes |

---

## 4 · Comparison with what LEGEND already held

- `CLAIM 003` (*consolidated baseline*) says neuronal WWOX deletion induces **non-cell-autonomous**
  hypomyelination, and its evidence boundary names the missing experiment: *"Non promuovibile senza una
  delezione o un rescue Olig2/CNP-specifici."* **That experiment now exists and is a preprint.** Handled
  in `CC-20261003W4-B-MYELIN-CELLAUT-01`; the claim's status does not move.
- `PAPER 004` says the quantitative enrichment was deferred to a PDF that was never obtained. **Supplied
  here from the printed page**, with the artefact-absence debt declared
  (`CC-20261003W4-B-REGISTRY-01`).
- `PAPER 023` describes B5 as "mixed mechanistic / non-CNS direct" with a "WWOX downregulation
  framework". **Both are vaguer than the design, and the overexpression arm is missing entirely**
  (`CC-20261003W4-B-HIF1A-SCOPE-01`).
- `CORPUS-STUB-109` (B6) is `not_processed`; B4 has **no record at all**. Both land in
  `CC-20261003W4-B-REGISTRY-01`, together with a merge for the duplicate identity `CORPUS-STUB-087`,
  open since 2026-07-05.
- **No registry statement about any of these six papers was found to be false.** Two were found to be
  under-specified, which is a different defect and is repaired rather than reversed.

---

## 5 · What was wrong in the assignment

The brief said to treat every sentence of the selection as a hypothesis. Four were tested; three did not
survive intact.

1. **"Group B's carrier arm is built from human heterozygote data instead [because the murine
   heterozygote literature is receipt-complete]."** False in a consequential way: **B1 itself contains a
   murine heterozygote arm** with a quantified electrophysiological phenotype, unrecorded anywhere in
   LEGEND. The carrier arm did not have to be built from human data at all.
2. **"B2 … is chosen because it is in tension with B1."** Not a tension. B2 states explicitly that it
   does not contradict the neuronal-deletion result and keeps a non-cell-autonomous contribution open.
   The two are complementary requirements at different times, and reading them as rivals would have
   produced a false contradiction.
3. **"four heterozygous WWOX carriers with a measured biochemical abnormality"** (B4). The four
   occurrences are **three distinct missense alleles**; the one carried by two people is **Benign in
   ClinVar** and common; **no lipid value is reported for any WWOX carrier**; and the cohort has **no
   normal-HDL-C comparator**. The abnormality was the selection criterion, not a measurement attributable
   to WWOX.
4. **Confirmed:** B1's acquisition is the risk, not the content — and worse than stated. The artefact
   behind the standing receipt is **gone from the checkout**, and no free route returns a new one.
5. **A detail the selection could not have known:** B6's two "WWOX SNPs" are ~500 kb apart in weak LD,
   and the positions the paper prints put rs2222896 **outside** the WWOX gene body as that body is given
   by B4's own supplement in the same build.

---

## 6 · Harness and protocol findings

1. 🔴 **`SOURCE_FIRST` is unachievable on a re-read, through the protocol's own prescribed route.** The
   acquisition-state check returns receipts whose `evidence_basis` is substantive scientific content. A
   `--state-only` mode for `fulltext_receipts.py status` (identity, depth, coverage keys, chain state —
   no `evidence_basis`, no `workflow`) would make the policy honourable. Until it exists, a re-reader
   must declare `QUESTION_DRIVEN`, as this note does.
2. 🔴 **Preprints have no home in the manifest layer.** Manifests are keyed by PMID and the provenance
   module resolves them by `study_id.pmid`; a DOI-only record cannot carry a manifest without turning a
   green suite red. Two of six readings in this group are therefore locator-rich and manifest-less.
3. **`evidence_presence.py --search` is scoped to manifests**, so it cannot look for an artefact that an
   old receipt declares and no manifest does — which is exactly the B1 case. The search here was done by
   hand (filename sweep plus a SHA-256 sweep over 504 candidate files).
4. **Europe PMC's `supplementaryFiles` archive can arrive truncated** with no end-of-central-directory
   record and still return HTTP 200; two of three archives did on first fetch and succeeded on retry.
   Worth a retry-and-verify in whatever acquires supplements.
5. **Model-safety halt, reported as the brief requires.** A reading of the figure-layout pages of B2's
   PDF was stopped by a safety classifier. The content was not reworded or retried; the pages were left
   unread, and no number in any output depends on them.

---

## 7 · Receipts prepared, not recorded

| File | Event id | Depth |
|---|---|---|
| `scratchpad/receipts_pending_w4/sciB_33914858_1.json` | `FTR-20261003-33914858-02` | partial (re-read) |
| `scratchpad/receipts_pending_w4/sciB_PPR1124524_1.json` | `FTR-20261003-PPR1124524-01` | partial |
| `scratchpad/receipts_pending_w4/sciB_PPR1015434_1.json` | `FTR-20261003-PPR1015434-01` | partial |
| `scratchpad/receipts_pending_w4/sciB_35460704_1.json` | `FTR-20261003-35460704-01` | partial |
| `scratchpad/receipts_pending_w4/sciB_35328751_1.json` | `FTR-20261003-35328751-02` | partial (re-read) |
| `scratchpad/receipts_pending_w4/sciB_33612478_1.json` | `FTR-20261003-33612478-01` | partial |

All six were dry-checked by appending them, in that order, to a **throwaway copy** of the ledger with a
throwaway copy of the state manifest: six exit-0 appends, and
`fulltext_receipts.py --ledger <copy> --manifest <copy> verify` returns
`OK: 326 chained receipt(s)`. The real ledger and the real manifest were not touched.
