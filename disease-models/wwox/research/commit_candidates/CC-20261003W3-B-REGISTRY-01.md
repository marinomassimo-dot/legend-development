# COMMIT CANDIDATE — CC-20261003W3-B-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 3 2026-10-03, branch `task/sci-B-20261003w3`.
**context_policy:** `SOURCE_FIRST` — every source was read and its first pass written before any registry
statement about it was opened; the comparison is in `research/intake_wave_20261003w3_B.md`.
**Not medical advice.** Class-level statements about published models only.

## Target
- `paper_registry_current.md`: **create** `PAPER 142`–`PAPER 147` for the six PMIDs of intake wave 3
  group B, and close the `Next action` line of the four corpus placeholders they promote.
- `literature_tracking_log_current.md`: **create** `LIT-0440` and `LIT-0441` for the two PMIDs that had no
  record of any kind; mark `LIT-0165`, `LIT-0158`, `LIT-0037`, `LIT-0033` processed and promoted; resolve the
  duplicate identity on PMID 41677633 by superseding `LIT-EX-005` in favour of `LIT-0165`.

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needed creation? |
|---|---|---|---|
| 21368882 | `PAPER 142` (new) | `LIT-0440` (new) | **yes — no record of any kind existed** |
| 21212468 | `PAPER 143` (new) | `LIT-0441` (new) | **yes — no record of any kind existed** |
| 41677633 | `PAPER 144` (new, promotes `CORPUS-STUB-147`) | `LIT-0165` (existing) · `LIT-EX-005` superseded | PAPER yes; LIT exists, duplicated |
| 24008736 | `PAPER 145` (new, promotes `CORPUS-STUB-139`) | `LIT-0158` (existing) | PAPER yes |
| 38542478 | `PAPER 146` (new, promotes `CORPUS-STUB-010`) | `LIT-0037` (existing) | PAPER yes |
| 30158849 | `PAPER 147` (new, promotes `CORPUS-STUB-006`) | `LIT-0033` (existing) | PAPER yes |

**Numbers are provisional.** Measured 2026-10-03 with `registry_records.py catalog` on `main`
`0e6fd4e9b886`: highest `PAPER 132`, highest `LIT-0431`. the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`–`141` and `LIT-0432`–`LIT-0439`, so this candidate starts at `PAPER 142` and `LIT-0440`. Wave-3 peers A and
C may claim the same numbers; the integrator renumbers in event order and updates the `insert-after` anchors
and the `LIT link` wikilinks.

## What this fixes beyond the landing
1. **Two PMIDs were invisible to the registries.** `registry_records.py get` exits 1 for 21368882 and
   21212468 — no `PAPER`, no `LIT`, no stub. One of them (21368882) is a reading debt named by an earlier
   wave; a debt with no record is a debt nothing can measure.
2. **One PMID has two literature records.** `registry_records.py` itself flags PMID 41677633 `AMBIGUOUS`
   (`LIT-0165` and `LIT-EX-005`). This candidate keeps `LIT-0165` live and marks `LIT-EX-005` superseded,
   rather than deleting it.
3. **`LIT-EX-005`'s filter reason was true about the cell systems and wrong about what the paper contains.**
   It reads *«non-CNS, non-pediatric, mechanistically distant»* and *«not translatable»*; the paper's
   mitochondrial-membrane-potential and ROS endpoints are measured on a constitutive `Wwox` null against
   wild type, and in that comparison WWOX loss is protective. The correction states the measured direction
   and leaves the transfer limit standing.

## Change class
**MINOR** — record creation and placeholder closure (§ 7). No claim status changes, no working-model block.

## Ordering
The receipts named below must be appended to the ledger before this candidate is propagated, so that no
record cites a receipt the ledger does not hold. They are prepared, not recorded:
`scratchpad/receipts_pending_w3/sciB_<pmid>_1.json`, event ids `FTR-20261003-<pmid>-01` or `-02`.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 on `main` 0e6fd4e9b886 with `record_scoped_edit.py apply`: exit 0, 10 op(s), keys ['PAPER 132', 'PAPER 142', 'PAPER 143', 'PAPER 144', 'PAPER 145', 'PAPER 146', 'CORPUS-STUB-147', 'CORPUS-STUB-139', 'CORPUS-STUB-010', 'CORPUS-STUB-006'])

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 132",
  "text": "\n## PAPER 142\n**Short title:** Lee 2010 Cell Death Dis - TGF-beta1 drives TIAF1 self-aggregation independently of the type II receptor, and aggregated TIAF1 precedes amyloid in vitro\n**Full title:** TGF-β induces TIAF1 self-aggregation via type II receptor-independent signaling that leads to generation of amyloid β plaques in Alzheimer's disease\n**Authors:** Lee MH, Lin SR, Chang JY, et al.; Sze CI, Chang NS\n**Year:** 2010\n**Source type:** primary research - cell biology and postmortem human tissue\n**Journal/source:** *Cell Death Dis* 2010;1:e110\n**Identifier:** PMID 21368882 / PMCID PMC3032296 / DOI 10.1038/cddis.2010.83\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.\n**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-21368882-01`; manifest `deepdive_manifests/PMID21368882.json`; dossier `research/fulltext_dossiers/PMID21368882.md` (figure panels read as legends only)\n**Primary pathway:** protein aggregation / TIAF1-APP cascade\n**Model/species:** cell lines (COS7, L929, Mv1Lu, HCT116, NCI-H1299, SK-N-SH, SH-SY5Y and others), postmortem human hippocampus, APP/PS1 and APP transgenic mouse\n**Genotype/model:** no WWOX genotype - WWOX is not manipulated or measured in this paper\n**Transferability:** T4 for WWOX: this is the upstream link of the TIAF1 cascade, not a WWOX experiment\n**clinical relevance:** LOW for WWOX directly; MODERATE as the primary behind the TIAF1 arm of the aggregation cascade\n**Claim links:** none\n**Role:** 🔴 **Earned null for the gene.** WWOX/WOX1 occurs three times in the whole article - a yeast-two-hybrid positive control, a cited background sentence on the TGF-beta1/Hyal-2/WOX1/Smad4 route, and one Discussion sentence on C1q - with no WWOX manipulation, readout or figure. What it does fix: TIAF1 aggregation is TbetaRII-independent and Smad4 prevents it; human hippocampal filter retardation gives TIAF1 aggregates in 59.0% of nondemented (n=41, age 59.0±17.0) and 54% of Alzheimer samples (n=97, age 80.0±8.8), with Aβ in 15% and 48%. ⚠️ The 'aggregation precedes amyloid' inference is cross-sectional across two groups that differ by ~21 years of mean age, and TIAF1 aggregation itself is not higher in the demented group. ⚠️ The abstract says aggregation causes Thr668 DEphosphorylation; the Results say TIAF1 overexpression INCREASED Thr668 phosphorylation and TGF-beta1 suppressed it - carry the two-step form.\n**LIT link:** [[literature_tracking_log_current#LIT-0440]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 142",
  "text": "\n## PAPER 143\n**Short title:** Dudekula 2010 Aging - Zfra at the mitochondrion: Bcl-2/Bcl-xL down, no cytochrome c release, membrane potential dissipated, WOX1 antagonised (perspective, no experiment)\n**Full title:** Zfra is a small wizard in the mitochondrial apoptosis\n**Authors:** Dudekula S, Lee MH, Hsu LJ, Chen SJ, Chang NS\n**Year:** 2010\n**Source type:** narrative perspective - no Methods, no Results, one schematic\n**Journal/source:** *Aging (Albany NY)* 2010;2:1023-1029\n**Identifier:** PMID 21212468 / PMCID PMC3034171 / DOI 10.18632/aging.100263\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.\n**Evidence depth:** `complete_fulltext_read` - receipt `FTR-20261003-21212468-01`; manifest `deepdive_manifests/PMID21212468.json`; dossier `research/fulltext_dossiers/PMID21212468.md`\n**Primary pathway:** mitochondrial apoptosis / Zfra-WWOX antagonism\n**Model/species:** none - secondary account of cell-line experiments published elsewhere\n**Genotype/model:** no genotype; every statement is about ectopically overexpressed Zfra or WOX1\n**Transferability:** T4 - overexpression in cancer lines, no neuron, no human allele\n**clinical relevance:** LOW - useful as an endpoint map (Bcl-2-family level, cytochrome c release and ΔΨm are separable), not as evidence\n**Claim links:** none\n**Role:** 🔴 **Secondary source on its own central result.** The Bcl-2/Bcl-xL suppression without cytochrome c release, the ΔΨm dissipation and the blockade of WOX1-induced cytochrome c release are all attributed to one earlier primary of the same laboratory; nothing is measured here. The Zfra-versus-WWOX relation is an inhibition of a GAIN-of-function effect, and the article states the endogenous question as open in its own words. Subject near-exclusive to one laboratory: `Zfra NOT Chang NS[au]` returns 1 PubMed record, an unrelated zebrafish paper matching the string by accident (measured 2026-10-03).\n**LIT link:** [[literature_tracking_log_current#LIT-0441]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 143",
  "text": "\n## PAPER 144\n**Short title:** Su 2026 Cells - stress-induced WWOX degrades Bcl-XL/Mcl-1 through a lysosomal route, and WWOX-null cells SURVIVE serum starvation better than wild type\n**Full title:** WWOX Induction Promotes Bcl-X<sub>L</sub> and Mcl-1 Degradation Through a Lysosomal Pathway upon Stress Responses\n**Authors:** Su YH, Chiang W, Wang YY, Kung YH, Cheng PS, Chang TH, Chang NS, Lai FJ, Hsu LJ\n**Year:** 2026\n**Source type:** primary research - cell biology\n**Journal/source:** *Cells* 2026;15:270\n**Identifier:** PMID 41677633 / PMCID PMC12897155 / DOI 10.3390/cells15030270\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.\n**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41677633-02` (earlier: `FTR-20260920-41677633-01`, partial, over a text extraction); manifest `deepdive_manifests/PMID41677633.json`; dossier `research/fulltext_dossiers/PMID41677633.md`\n**Primary pathway:** organelle biology / proteostasis / redox\n**Model/species:** primary mouse embryonic fibroblasts (`Wwox+/+` and `Wwox-/-`), HeLa Tet-On, human SCC-15\n**Genotype/model:** constitutive mouse null versus wild type; inducible ectopic WWOX; shRNA knockdown. No heterozygote arm, no human missense or splice allele\n**Transferability:** T3 for the direction of effect; T4 for mechanism in neurons - nothing in this paper is neural\n**clinical relevance:** MODERATE - three measurable organelle endpoints (ΔΨm, ROS, anti-apoptotic Bcl-2-family protein level) with a pharmacological handle (NAC)\n**Claim links:** none\n**Role:** 🔴 **Direction, measured at panel level: under serum starvation the WWOX-NULL cell is the surviving cell.** Viability ~35%→~21% at 72 h in `Wwox+/+` against ~40% flat to 96 h in `Wwox-/-` (Fig 4A); sub-G0/G1 ~21% vs ~11% (Fig 4B); ΔΨm falls to ~0.34 of control in `Wwox+/+` and stays ~0.79 in `Wwox-/-` (Fig 4C); ROS rises more in `Wwox+/+` at 6-48 h and is EQUAL at baseline (Fig 8A). Bcl-XL and Mcl-1 fall post-transcriptionally in `Wwox+/+` only; MG132 does not rescue, chloroquine, E64d and pepstatin A do. ⚠️ No autophagic-flux assay anywhere; the lysosomal route is inhibitor pharmacology on static westerns, and the authors ask for the genetic test themselves. ⚠️ Neither Bcl-XL nor Mcl-1 co-immunoprecipitates with WWOX. ⚠️ Text-versus-panel: the Results name chloroquine as the rescuing lysosome inhibitor and Figure S3B shows NH₄Cl, in the same experiment, failing to rescue.\n**LIT link:** [[literature_tracking_log_current#LIT-0165]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 144",
  "text": "\n## PAPER 145\n**Short title:** Tsai 2013 Cell Death Dis - WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated squamous carcinoma; the flux clamp is on the drug, never on WWOX\n**Full title:** WWOX suppresses autophagy for inducing apoptosis in methotrexate-treated human squamous cell carcinoma\n**Authors:** Tsai CW, Lai FJ, Sheu HM, et al.; Chang NS, Hsu LJ\n**Year:** 2013\n**Source type:** primary research - cell biology with tumour biopsies\n**Journal/source:** *Cell Death Dis* 2013;4:e792\n**Identifier:** PMID 24008736 / PMCID PMC3789168 / DOI 10.1038/cddis.2013.308\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.\n**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-24008736-02` (earlier: `FTR-20260921-24008736-01`, partial, no figures); manifest `deepdive_manifests/PMID24008736.json`; dossier `research/fulltext_dossiers/PMID24008736.md`. Partial for one reason only: the supplement deposited under this identifier is a different article's supplement (see `CC-20261003W3-B-SUPPDEPOSIT-01`)\n**Primary pathway:** autophagy / mTOR / chemosensitivity\n**Model/species:** human SCC-4, SCC-9, SCC-15; tumour biopsies; one sentence of `Wwox` knockout MEF data\n**Genotype/model:** ectopic WWOX overexpression, siRNA and shRNA knockdown, Y33R dominant-negative; `Wwox+/-` and `Wwox-/-` MEFs in the unreachable Supplementary Figure 7\n**Transferability:** T3 for the sign in epithelial cancer under antimetabolite stress; T4 for neurons and for any constitutive human genotype\n**clinical relevance:** MODERATE - the readable half of the autophagy-direction disagreement\n**Claim links:** none\n**Role:** Direction: WWOX reduces Beclin-1, Atg12-Atg5, LC3-II, GFP-LC3 puncta and EM autophagosomes, and co-immunoprecipitates with mTOR while raising p-mTOR and p-p70S6K. 🔴 **The lysosomal clamp (E64d + pepstatin A) is applied to METHOTREXATE, never to a WWOX manipulation** (Fig 3c: LC3-II 1.6→1.0 under the clamp at 12 h), so the WWOX→autophagy step is never measured as flux. ⚠️ The mTOR causal order is stated as a possibility by the authors. ⚠️ LC3 loss is routed to the PROTEASOME here (MG132 blocks it), which is a different route from the lysosomal one the same laboratory later assigns to Bcl-XL/Mcl-1 in the same SCC-15 background - different cargo, not one mechanism stated twice. ⚠️ The paper's own scope sentence binds the direction to a drug, a tumour and an apoptotic endpoint. Integrity: no notice on this paper; its reference 15 (PNAS 2005) carries a 2017 expression of concern (`dependency_integrity.py screen`, 2026-10-03).\n**LIT link:** [[literature_tracking_log_current#LIT-0158]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 145",
  "text": "\n## PAPER 146\n**Short title:** Chen 2024 Int J Mol Sci - 'Zfra overrides WWOX' is asserted by a perspective review with no head-to-head experiment\n**Full title:** Zfra Overrides WWOX in Suppressing the Progression of Neurodegeneration\n**Authors:** Chen YA, Liu TY, Wen KY, Hsu CY, Sze CI, Chang NS\n**Year:** 2024\n**Source type:** perspective review\n**Journal/source:** *Int J Mol Sci* 2024;25:3507\n**Identifier:** PMID 38542478 / PMCID PMC10970703 / DOI 10.3390/ijms25063507\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.\n**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-38542478-01`; manifest `deepdive_manifests/PMID38542478.json`; dossier `research/fulltext_dossiers/PMID38542478.md` (figure panels read as legends only)\n**Primary pathway:** therapeutic strategy / Zfra peptide / WWOX phospho-code\n**Model/species:** none of its own\n**Genotype/model:** none of its own; cites a heterozygous `Wwox` mouse cortex finding (pT12-WWOX aggregates) and 3xTg-AD mice\n**Transferability:** T4 - no measurement in this article\n**clinical relevance:** MODERATE - it is the only source stating a RANK ORDER between a Zfra strategy and a WWOX strategy, which decides whether the two are additive or antagonistic\n**Claim links:** none\n**Role:** 🔴 **The hierarchy is asserted, not measured.** Section 11 says *'We determined that Zfra overrides WWOX...'*; section 11.2 says *'Zfra may override WWOX deficiency...'*. No experiment in this article - it performs none - and none it cites compares a WWOX-restoration arm with a Zfra arm in one model. The one head-to-head datum is the opposite kind: Zfra4-10 and WWOX7-21 given TOGETHER lose the antitumour effect each has alone. ⚠️ Useful import: it carries two independent-laboratory references on this group's question - PMID 33300063 (WWOX inhibits autophagy, ovarian carcinoma) and PMID 35984507 (blocking WWOX restores mitochondrial homeostasis in neuronal cells under high glucose).\n**LIT link:** [[literature_tracking_log_current#LIT-0037]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 146",
  "text": "\n## PAPER 147\n**Short title:** Liu 2018 Front Neurosci - the WWOX phospho-code maps to compartment and cell fate, and to NO measured organelle endpoint\n**Full title:** WWOX Phosphorylation, Signaling, and Role in Neurodegeneration\n**Authors:** Liu CC, Ho PC, Lee IT, et al.; Sze CI, Chiang MF, Chang NS\n**Year:** 2018\n**Source type:** review with one original database analysis\n**Journal/source:** *Front Neurosci* 2018;12:563\n**Identifier:** PMID 30158849 / PMCID PMC6104168 / DOI 10.3389/fnins.2018.00563\n**Status:** processed\n**Record provenance:** created by `CC-20261003W3-B-REGISTRY-01` (intake wave 3 2026-10-03, Scientist B). Provisional number, measured with `registry_records.py catalog` on `main` 0e6fd4e9b886 (highest `PAPER 132`); the three wave-2 registry candidates (A, B, C) already claim `PAPER 133`-`141` and `LIT-0432`-`LIT-0439`, so this candidate starts at `PAPER 142` / `LIT-0440`. The integrator renumbers in event order and updates the anchors.\n**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-30158849-02` (earlier: `FTR-20260811-30158849-01`, partial, over an artefact absent from this checkout); manifest `deepdive_manifests/PMID30158849.json`; dossier `research/fulltext_dossiers/PMID30158849.md`\n**Primary pathway:** WWOX phospho-code / neurodegeneration\n**Model/species:** none of its own except a public brain-expression database analysis\n**Genotype/model:** none of its own\n**Transferability:** T4 as evidence; T1 as a map of what the phospho-code is claimed to do\n**clinical relevance:** MODERATE - it is LEGEND's named source for the phospho-code, and the open debt `FT-057`\n**Claim links:** none\n**Role:** 🔴 **Measured answer to the question it was read for: the residue-to-organelle-endpoint mapping does not exist in this source.** pY33 is mapped to mitochondrial/nuclear relocation and apoptosis, pS14 to differentiation and disease progression, pY287 to proteasomal turnover; pT12 is ABSENT from this 2018 review and appears only in the group's 2024 one. No residue is tied to a measured ΔΨm, ROS, lysosomal or autophagic readout. The lysosome appears once, in an uncited list of compartments. ⚠️ One transferable direction is stated for the constitutive null: *'If cells are devoid of WWOX (e.g., Wwox-/- MEF), cell death is retarded'*. The ROS/SDR link is carried from two laboratories that are not the authoring group.\n**LIT link:** [[literature_tracking_log_current#LIT-0033]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-147",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none - upgraded (41677633 → `PAPER 144`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-139",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none - upgraded (24008736 → `PAPER 145`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-010",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none - upgraded (38542478 → `PAPER 146`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-006",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none - upgraded (30158849 → `PAPER 147`) by `CC-20261003W3-B-REGISTRY-01`; this placeholder is kept as history"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; dry run 2026-10-03 on `main` 0e6fd4e9b886: exit 0, 8 op(s), keys ['LIT-0431', 'LIT-0440', 'LIT-0165', 'LIT-0158', 'LIT-0037', 'LIT-0033', 'LIT-EX-005', 'LIT-EX-005'])

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0431",
  "text": "\n## LIT-0440\n**Short title:** Lee 2010 TIAF1 aggregation and amyloid\n**Authors:** Lee MH, et al.; Chang NS\n**Year:** 2010\n**Source type:** primary research - cell biology and postmortem human tissue\n**Journal/source:** *Cell Death Dis* 2010;1:e110\n**Identifier type:** PMID / DOI\n**Identifier value:** PMID 21368882 / DOI 10.1038/cddis.2010.83\n**Date discovered:** 2026-10-03\n**Date processed:** 2026-10-03\n**Discovery window:** intake wave 3 2026-10-03 (Scientist B, group B)\n**Discovery source:** Orchestrator wave-3 selection record\n**Discovery query:** WWOX organelle endpoints - mitochondria, lysosome/autophagy, ROS, aggregation\n**Status:** processed\n**Primary pathway:** protein aggregation / TIAF1-APP cascade\n**Genotype/model tag:** no WWOX genotype\n**Transferability:** T4\n**clinical relevance:** LOW for WWOX directly\n**Claim links:** none\n**Working Model impact:** none\n**Report mentions:** `research/intake_wave_20261003w3_B.md`\n**Next action:** none\n**Flags:** created by `CC-20261003W3-B-REGISTRY-01`; provisional number\n**Note:** Paired with [[paper_registry_current#PAPER 142]]. Read in full 2026-10-03; WWOX is not manipulated or measured in it - an earned null for the gene.\n\n---\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0440",
  "text": "\n## LIT-0441\n**Short title:** Dudekula 2010 Zfra mitochondrial apoptosis\n**Authors:** Dudekula S, Lee MH, Hsu LJ, Chen SJ, Chang NS\n**Year:** 2010\n**Source type:** narrative perspective\n**Journal/source:** *Aging (Albany NY)* 2010;2:1023-1029\n**Identifier type:** PMID / DOI\n**Identifier value:** PMID 21212468 / DOI 10.18632/aging.100263\n**Date discovered:** 2026-10-03\n**Date processed:** 2026-10-03\n**Discovery window:** intake wave 3 2026-10-03 (Scientist B, group B)\n**Discovery source:** Orchestrator wave-3 selection record\n**Discovery query:** WWOX organelle endpoints - mitochondria, lysosome/autophagy, ROS, aggregation\n**Status:** processed\n**Primary pathway:** mitochondrial apoptosis / Zfra-WWOX antagonism\n**Genotype/model tag:** no WWOX genotype\n**Transferability:** T4\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none\n**Report mentions:** `research/intake_wave_20261003w3_B.md`\n**Next action:** none\n**Flags:** created by `CC-20261003W3-B-REGISTRY-01`; provisional number\n**Note:** Paired with [[paper_registry_current#PAPER 143]]. Secondary throughout: every mitochondrial datum traces to one earlier primary of the same laboratory.\n\n---\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0165",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none - screened and read in full on 2026-10-03 (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 144]] by `CC-20261003W3-B-REGISTRY-01`"
 },
 {
  "op": "replace-within",
  "id": "LIT-0158",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none - screened and read in full on 2026-10-03 (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 145]] by `CC-20261003W3-B-REGISTRY-01`"
 },
 {
  "op": "replace-within",
  "id": "LIT-0037",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none - screened and read in full on 2026-10-03 (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 146]] by `CC-20261003W3-B-REGISTRY-01`"
 },
 {
  "op": "replace-within",
  "id": "LIT-0033",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none - screened and read in full on 2026-10-03 (intake wave 3, Scientist B); promoted to [[paper_registry_current#PAPER 147]] by `CC-20261003W3-B-REGISTRY-01`"
 },
 {
  "op": "replace-within",
  "id": "LIT-EX-005",
  "old": "**Filter reason:** WWOX in Bcl-XL/Mcl-1 degradation via lysosome in cancer cells — non-CNS, non-pediatric, mechanistically distant",
  "new": "**Filter reason:** 🔴 **Duplicate identity and an outdated rationale, corrected 2026-10-03 (`CC-20261003W3-B-REGISTRY-01`).** The same PMID is also carried by [[literature_tracking_log_current#LIT-0165]], which is the record promoted to [[paper_registry_current#PAPER 144]]; this one is kept as history and is no longer the live record. On the substance: the cell systems are indeed non-CNS (MEF, HeLa, SCC-15), but the paper is NOT only a cancer-apoptosis result - two of its endpoints (mitochondrial membrane potential, ROS) are measured on a constitutive `Wwox` null versus wild type, and in that comparison WWOX loss is PROTECTIVE under serum starvation. Read in full on 2026-10-03: receipt `FTR-20261003-41677633-02`, dossier `research/fulltext_dossiers/PMID41677633.md`"
 },
 {
  "op": "replace-within",
  "id": "LIT-EX-005",
  "old": "**Status:** filtered_out",
  "new": "**Status:** superseded - see [[literature_tracking_log_current#LIT-0165]] (same PMID, promoted)"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the paper reports higher viability in the Wwox-null fibroblast than in the wild type under serum starvation | Wwox+/+ MEFs showed a significantly enhanced reduction in cell viability as compared with Wwox−/− MEFs after serum starvation for 72 h | PMID 41677633, Results 3.3; files/fulltext/PMID41677633_Su2026_PMC.xml)
(the mitochondrial membrane potential falls in the WWOX-expressing cell and not in the null | we detected a significant reduction in MMP in Wwox+/+ MEFs after serum starvation in a time-dependent manner | PMID 41677633, Results 3.3; files/fulltext/PMID41677633_Su2026_PMC.xml)
(the two cargo proteins do not bind WWOX | Co-immunoprecipitation experiments revealed that neither Bcl-XL nor Mcl-1 physically interacted with WWOX. | PMID 41677633, Results 3.5; files/fulltext/PMID41677633_Su2026_PMC.xml)
(the paper binds its own autophagy direction to a drug, a tumour and an apoptotic endpoint | Thus, WWOX suppresses autophagy for inducing apoptosis in MTX-treated human SCC. | PMID 24008736, Discussion first paragraph; files/fulltext/PMID24008736_Tsai2013_PMC.xml)
(the hierarchy between the two levers is asserted in a review's summary | We determined that Zfra overrides WWOX in suppressing cancer growth and the progression of neurodegeneration. | PMID 38542478, section 11; files/fulltext/PMID38542478_Chen2024_PMC.xml)
(the same review states the same relation conditionally | Zfra may override WWOX deficiency in restoring normal physiological functions. | PMID 38542478, section 11.2; files/fulltext/PMID38542478_Chen2024_PMC.xml)
(the 2018 review names the lysosome once, in a list of compartments | WWOX localizes in many subcellular compartments, including cell membrane, mitochondrion, lysosome, nucleus, and others. | PMID 30158849, Hyal-2/WWOX TBI section; files/fulltext/PMID30158849_Liu2018_PMC.xml)
(the mitochondrial statements of the Zfra perspective are attributed, not measured | At the mitochondrial level, Zfra downregulates the expression of apoptosis inhibitor Bcl-2 and Bcl-xL | PMID 21212468, 'Zfra executes mitochondrial apoptosis on its own manner'; files/fulltext/PMID21212468_Dudekula2010_PMC.xml)
(WWOX appears in the TIAF1 paper only as cited background for another route | TGF-β1 binds membrane hyaluronidase type 2 (Hyal-2) for recruiting tumor suppressor WW domain-containing oxidoreductase (WOX1) (also named WWOX or FOR) and Smad4 to relocate to the nuclei | PMID 21368882, Results, TβRII-independent section; files/fulltext/PMID21368882_Lee2010_PMC.xml)


---

## BATCH DISPOSITION — `BATCH_20261003_002` (2026-10-03, ACTOR_ID `scientist`, Scientist G), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED (MINOR), with one op reconciled rather than applied

**PMID 21212468 was not given a second record.** `PAPER 142` / `LIT-0440` already existed as the identity landing `BATCH_20261003_001` wrote; this candidate's scientific assessment was written INTO those records (provenance line updated, the candidate's own field values carried) and its `PAPER 143` / `LIT-0441` creation ops were dropped. **Renumbered:** 21368882 → `PAPER 146` / `LIT-0443`; 41677633 → `PAPER 147`; 24008736 → `PAPER 148`; 38542478 → `PAPER 149`; 30158849 → `PAPER 150`; every anchor and wikilink rewritten. **Integrator amendments:** (1) four `LIT` lines and `LIT-EX-005` said *read in full* where every receipt is `partial_fulltext_read` — now say so; (2) `PAPER 147`'s panel magnitudes carry the fact that no panel locator was persisted and the receipt declares `figures: captions_only`; (3) `LIT-EX-005`'s `Status` took the bare vocabulary value after Phase 5 returned `INVALID_LIT_STATUS`, the pointer moved to its own line.

**Not medical advice.**
