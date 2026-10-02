# Intake wave 2 — 2026-10-03 — Scientist C

`context_policy: SOURCE_FIRST`
ACTOR_ID `scientist` (Scientist C), branch `task/sci-C-20261003`, dispatched by the Orchestrator
under the operator's standing authorisation of 2026-09-28.
**Not medical advice.** Everything below is class-level: no patient, no individual record.

**Assigned question.** Which endpoint in each model / metabolic / ER-stress source could serve as
a **rescue readout** for a therapeutic test rather than only as a description of the defect, and
with what transfer limit to the WWOX-DEE genotype class — assessing model species and allele
(constitutive null vs conditional vs knockdown), tissue, the readout, its effect size and its
controls.

**List.** PMID 34268881 · 31543760 · 25649963 · 39952983 · 26302329 · 28749468.

---

## 1 · Context policy, declared

Each source was opened knowing only its identity, its acquisition state
(`fulltext_receipts.py status --pmid N`, exit status read directly), the question above, and the
integrity facts needed to read it (`EFetch` publication types and correction links). The six
first-pass readings were written down before any LEGEND record was opened. The transition is
written in each dossier as `FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR
COMPARISON`, and the comparison used targeted retrieval only —
`registry_records.py get --pmid <PMID>` — never a grep of a registry.

---

## 2 · Verdicts

| # | PMID | Verdict | What is new versus held |
|---|---|---|---|
| C1 | 34268881 | **INGEST** | Six text-versus-panel disagreements the corpus did not hold (`CC-20261003-C-STEINBERG-PANELS-01`); the delivery contrast between constitutive and post-hoc mosaic restoration, which is the transferable part of the rescue |
| C2 | 31543760 | **INGEST** | The knockdown depth is stated nowhere; the 3-D phenotype is unquantified and un-rescued; **twelve declared artefacts were missing from the corpus and were restored** |
| C3 | 25649963 | **INGEST** | The Ca²⁺ endpoint — the reason this paper was selected — is a picture, not a measurement; the morphometric rescue is the real readout, and `DL-MECH-021` already had it |
| C4 | 39952983 | **INGEST** | The human arm is suggestive **by the authors' own statement**, measures no WWOX expression at all, and co-moves with time in bed; the fly allele is a hypomorph; **four declared artefacts were missing and were restored** |
| C5 | 26302329 | **INGEST** | A true in-vivo gene-dosage result in the supplement; a labelling contradiction in the only panel supporting the paper's central claim; two integrity-flagged dependencies |
| C6 | 28749468 | **INGEST** | The direction of the rescue is wrong-signed for a DEE; the central IRE-1 claim rests on panels with no statistics; a non-significant panel reported as positive |

No source was DEFERRED, OFF-AXIS or ABSTRACT-SUFFICIENT. All six were acquired lawfully and free
from Europe PMC on the first attempt.

---

## 3 · The answer to the assigned question

**Three endpoints behave like a rescue readout**, and they are not the ones the selection
expected. Ranked, with effect size and controls:

1. **Single-neuron spontaneous firing rate** in patient-derived cerebral organoids
   (PMID 34268881 Fig 5C): 0.41 → **1.65** → 0.46 Hz, rescued-versus-parental `P = 0.7681`.
   Large, near-binary, measured in cells carrying the genotype, with the rescue arm drawn.
   Limits: n is neurons (24 / 41 / 40) from 3–4 organoids; one family; no blinding; no
   distributed P-value for any main figure of that paper.
2. **LFP oscillatory power, 0.25–1 Hz** (PMID 34268881 Figs 2C, 2G): ≈0.030 → ≈0.066 → ≈0.025,
   obtained by **lentivirus delivered to already-patterned week-5 organoids** producing sparse
   mosaic WWOX.
3. **Eye diameter at 48 hpf** in zebrafish (PMID 25649963 Fig 2E): ≈265 → ≈205 → ≈270 µm,
   `P < 0.01`, n = 30 across three experiments, with two independent knockdown reagents and a
   rescue construct consisting of the **SDR/ADH domain alone**.

**The most useful single fact is not an endpoint but a contrast.** PMID 34268881 contains two
different restorations. The constitutive AAVS1 knock-in, expressed ubiquitously from pluripotency,
gives a partial rescue that **overshoots** wild type on cortical-layer markers and fails to rescue
the *GAD1* transcript at all. The lentiviral arm, delivered at day 35 to tissue that had already
formed, mosaic and sparse, **normalises the network readout completely**. Those two facts say that
the electrophysiological phenotype is not locked in once cortical patterning has begun and does
not require every cell to be corrected — a statement about **timing and coverage** that a
constitutive knock-in cannot make.

**Two endpoints are large but unusable as published:** 3-D network formation of human neural
progenitors in ECM (PMID 31543760) — near-binary, human, reproduced three times, and
**unquantified, un-n'd, untested, un-rescued**, in a line whose knockdown depth is never stated;
and *Drosophila* daytime sleep (PMID 39952983) — ≈500 → ≈300 min, `****`, n = 32, automated and
non-terminal, with **no rescue arm**.

**Eight candidate readouts are rejected and written down as rejected**, with the reason, in
`CC-20261003-C-RESCUE-READOUT-01`. All fail
[`LEGEND_CORE.md` § 13](../../../framework/instruction/LEGEND_CORE.md#13-biomarker-scope-hard-rule):
Ca²⁺ by FRET, resazurin reduction, pro-MMP2/9, cleaved caspase-3, GRP78 / phospho-IRE-1 / PERK,
γH2AX / 53BP1, self-reported sleep duration, and *WWOX* mRNA as a chemotherapy-response predictor.
None measures the functional state of *WWOX*, and none can be sampled in a living patient's
neurons. They are Tier 3 or not biomarkers at all; that is a different thing from being useless,
and several are perfectly good **model** readouts.

**Transfer limit, stated once for all of them.** Every ranked readout comes from a **null** — a
CRISPR exon-1 frameshift, a homozygous splice-acceptor allele, or a morpholino/siRNA knockdown.
A constitutive null models neither P47T nor Q230P nor G372R nor A141T nor P252A, and PMID
34268881's own SCAR12 arm (homozygous G372R) shows weaker organoid phenotypes than its WOREE arm —
so transfer to a milder missense class is untested in exactly the direction that matters.

---

## 4 · One cross-source finding the batch produced

Three organisms, three systems, one direction (`CC-20261003-C-APOPTOSIS-DIRECTION-01`):

* Human WWOX-null cerebral organoids — ventricular-zone cleaved caspase-3 falls from ≈24 % to
  ≈9 % on loss and returns to ≈16 % on restoration (n.s. versus wild type).
* *Drosophila* epithelium under ectopic TNFα — loss **protects** (two RNAi lines, `****`; a single
  heterozygous allele already shifts it), gain worsens.
* Human *WWOX*-null ovarian carcinoma — restoration roughly halves survival under paclitaxel and
  tunicamycin; removal roughly doubles it.

**WWOX loss lowers the stress-induced apoptotic response; WWOX restoration raises apoptotic
sensitivity under stress.** For a gene-replacement strategy aimed at neurons already carrying a
measured DNA-damage load (γH2AX 0.78 → 1.5 foci per nucleus in the same organoids), that is a
dose-and-context question worth carrying. It is **not** an argument against replacement: in the
organoid the restored value is not significantly different from wild type, and in the fly ectopic
WWOX alone produces no phenotype at all.

---

## 5 · What would change the model if true, and what would falsify it

**If true and currently unproven** — that WWOX restoration after cortical patterning has begun
still normalises network activity. PMID 34268881's lentiviral arm is the only evidence, it is one
endpoint in one model, and it would widen the therapeutic window from "prenatal" to "postnatal
and still useful". **Falsifier:** the same lentiviral delivery at progressively later time points
with the 0.25–1 Hz AUC read at each; if normalisation disappears beyond some week, the window
closes and the number is the answer.

**If true** — that the apoptotic direction above holds in a stressed human neuron. **Falsifier:**
a titrated WWOX restoration in patient-derived neurons under a declared stressor, with apoptosis
as a declared endpoint and a wild-type comparator at every dose. Monotonic increase past wild
type makes it a dose constraint; saturation at wild type makes it a non-issue.

**What would falsify the ranking itself:** if firing rate and 0.25–1 Hz power do not move together
across a titrated rescue series, then "the electrophysiological phenotype" is not one endpoint and
the ranking collapses into two independent readouts that happen to agree once.

---

## 6 · What in the assignment was wrong

The selector's "what is uncertain" lines were treated as hypotheses and tested. Four were wrong or
answerable:

1. **C3, "Morpholino knockdown with no rescue control stated".** Wrong. The paper carries two
   independent knockdown reagents (MO 56 %, siRNA 62 % penetrance) and a **quantified rescue** on
   two morphometric endpoints. `DL-MECH-021` already recorded it, including that the rescue
   succeeds with the SDR/ADH domain alone.
2. **C4, "Whether the two SNVs survive genome-wide correction needs the body".** Answered, and the
   answer is in the authors' own limitations: *"the WWOX gene did not reach the conventional
   genome-wide significance level"*. The supplement's Bonferroni values imply correction over
   ≈1.8 × 10⁵ tests, not 6.42 million; the Manhattan threshold is drawn at 1 × 10⁻⁵.
3. **C5, "Gene-dosage directionality in flies vs. mammals is untested here".** It is tested, and
   in the supplement: a **single heterozygous loss-of-function allele** measurably shifts the eye
   phenotype (`*`, `****` for two independent alleles). What is *not* measured here is ROS — the
   proposed link is carried entirely from an earlier paper.
4. **C1, "`FT-059` records 69 figure panels never read".** Stale. The 2026-08 addendum to
   `fulltext_dossiers/PMID34268881.md` already reports reading all of them. Reconciling the queue
   entry with that history is the Orchestrator's, not a Scientist's, and this note does not do it.

One further premise in the brief's framing deserves recording: the selector described
PMID 28749468 as carrying "named ER-stress branches, with GRP78 as the modifier". The branches are
named, but **the panels that establish WWOX-dependence carry no statistics at all**, and the
absolute KIRA6 effect is identical in both genotypes.

---

## 7 · Harness repair performed in this session

Two deep-dive manifests were **`BLOCK`** at the start of this reading because every artefact they
declared had vanished from the gitignored corpus:

* `PMID31543760.json` — one JATS XML and eleven figure JPEGs, all absent.
* `PMID39952983.json` — one JATS XML, two figure JPEGs and one supplementary DOCX, all absent.

Re-acquisition from Europe PMC on 2026-10-02 returned files whose sha256 **matches every declared
digest exactly** (16 of 16). They were restored under their declared paths, and both manifests now
report `VERDICT: PASS … complete (0 gap(s))` with `--verify-artifacts`. This is the
"absent artefact is often misplaced" failure mode: the manifests were not wrong, the corpus had
lost the files, and the repair was a re-fetch plus a digest comparison — not a re-reading and not
a ceiling change.

**Not checked, and worth a sweep by whoever owns the corpus:** how many other manifests in
`deepdive_manifests/` declare artefacts that are no longer on disk. This session checked only its
own six.

---

## 8 · Receipts, manifests, dossiers and candidates produced

| PMID | Receipt file (prepared, **not** recorded) | event_id | depth | manifest |
|---|---|---|---|---|
| 34268881 | `scratchpad/receipts_pending_w2/sciC_34268881_1.json` | `FTR-20261003-34268881-06` | `partial_fulltext_read` | 31 locators, PASS |
| 31543760 | `…/sciC_31543760_1.json` | `FTR-20261003-31543760-03` | `partial_fulltext_read` | 14 locators, PASS |
| 25649963 | `…/sciC_25649963_1.json` | `FTR-20261003-25649963-02` | `partial_fulltext_read` | 7 locators, PASS |
| 39952983 | `…/sciC_39952983_1.json` | `FTR-20261003-39952983-02` | `partial_fulltext_read` | 14 locators, PASS |
| 26302329 | `…/sciC_26302329_1.json` | `FTR-20261003-26302329-01` | `partial_fulltext_read` | 8 locators, PASS |
| 28749468 | `…/sciC_28749468_1.json` | `FTR-20261003-28749468-01` | `partial_fulltext_read` | 9 locators, PASS |

**All six are `partial_fulltext_read`, and every one says why.** Five fall short on supplementary
material that was read as captions but not panel by panel; one (PMID 34268881) falls short because
the Appendix Figures S1–S6 the Results cite throughout are **not distributed by PMC at all**.
Every reference list was enumerated and screened mechanically (`dependency_integrity.py screen`)
but not read item by item, which is recorded as `references: not_read` in all six.

Dossiers: `fulltext_dossiers/PMID{25649963,26302329,28749468,31543760,39952983}.md` (new) and a
dated addendum appended to `fulltext_dossiers/PMID34268881.md` (the existing dossier was **not**
replaced).

Candidates, all with executable op lists dry-run against `f5f946837924` at exit 0:

| Candidate | Class | Ops |
|---|---|---|
| `CC-20261003-C-RESCUE-READOUT-01` | MINOR | 1 append to the discovery ledger |
| `CC-20261003-C-APOPTOSIS-DIRECTION-01` | MINOR | 1 append + 1 `replace-within` on `DL-MECH-023` |
| `CC-20261003-C-STEINBERG-PANELS-01` | MINOR | 1 append |
| `CC-20261003-C-SLEEP-SUGGESTIVE-01` | MINOR | 1 `replace-within` on `DL-MECH-013` |
| `CC-20261003-C-REGISTRY-01` | MINOR | 2 ops on the tracking log + 2 on the paper registry |

Registry landings: five of six PMIDs already have one. Only **PMID 39952983** had no record in
either canonical surface — `LIT-0421` and `PAPER 119` are proposed for it — and PMID 28749468's
two records were unscreened stubs, which are enriched rather than promoted.

---

## 9 · Integrity

PubMed EFetch over all six PMIDs in one call, 2026-10-02: publication types `Journal Article`
(plus `Research Support, Non-U.S. Gov't` where applicable), and **no** `CommentsCorrections`
element of any `RefType` — so no retraction, erratum, expression of concern, comment or update
link on any of the six.

Dependency screen (`dependency_integrity.py screen --manifest-block`, Retraction Watch snapshot
2026-09-10, 72,476 rows): five of six `SCREENED_CLEAN`. **PMID 26302329 returns
`FLAGGED_RETRACTION`** on two citation-only dependencies:

* `10.1073/pnas.0505485102` — Fabbri 2005, *WWOX gene restoration prevents lung cancer growth in
  vitro and in vivo* — **expression of concern**, 2017-04-03, reasons including image duplication
  and data unavailability. Cited as reference 17, Introduction, background only.
* `10.1074/jbc.M709062200` — Trapasso 2008, FHIT–ferredoxin reductase — **retracted** 2017-08-03.
  Cited as reference 63, Discussion, background only.

Neither carries a measurement into PMID 26302329. The first is recorded beyond its citing paper
because it is a load-bearing citation for the general premise that *WWOX restoration suppresses
tumour growth in vivo*, and any future record leaning on that premise should know its source's
status.
