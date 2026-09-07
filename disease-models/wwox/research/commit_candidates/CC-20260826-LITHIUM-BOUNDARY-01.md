# COMMIT CANDIDATE — lithium: propagate the existing genotype boundary, and retire "disease modifier"

**Candidate ID:** CC-20260826-LITHIUM-BOUNDARY-01
**Status:** proposed — not integrated, not committed
**Base head:** `b80ae8b`
**Receipts:** `FTR-20260804-32000863-01` (`complete_fulltext_read`, PMID 32000863)
**Author:** scientist-b

---

**CURRENT_TARGET**

`CLAIM 016` **already carries** the genotype boundary (propagated 2026-08-10, `BATCH_20260810_005`).
Three downstream records do not:

1. `therapeutic_strategies_current.md#TX-005` — *"lithium **abolishes** PTZ-induced seizures in
   Wwox-/-"*, scored `EVID 2`.
2. `therapy_levers.md` **A2** — *"Lithium (GSK3β inhibition) — **the strongest repurposing
   signal**… GSK3β is elevated in cortex, hippocampus and cerebellum; lithium inhibits GSK3β and
   abolishes seizures"*.
3. 🔴 `therapy_levers.md` **Practical priority 2** — *"lithium as a preclinically-grounded **disease
   modifier** (GSK3β)"*, in a section headed *"for clinical discussion"*.

**PROPOSED_DELTA**

- Propagate `CLAIM 016`'s existing boundary verbatim into `TX-005` and `therapy_levers.md` A2.
- Retire *"the strongest repurposing signal"*.
- 🔴 **Retire *"disease modifier"* from Practical priority 2.** Proposed replacement: *"lithium — a
  general anticonvulsant with a WWOX-adjacent mechanistic rationale that has not been demonstrated;
  no developmental endpoint has ever been measured under lithium in any WWOX system"*.
- Add one sentence to all three: *the effect is a **general anticonvulsant effect**, not a
  WWOX-specific rescue, and it is a **negative result in an assay of demonstrated sensitivity**.*
- Re-score `TX-005` on the failed specificity test rather than on the mechanistic rationale.

**CHANGE_CLASS:** MINOR — `CLAIM 016` is `in observation` and already carries the boundary; this is
propagation into a tracker and an analysis file.

**CANONICAL_TARGETS:** none of the four scientific current files.
`therapeutic_strategies_current.md` and `therapy_levers.md` are **not** batch-gated — verified: neither
appears in `prompt_batch_commit.md` nor in the state manifest's controlled-file lists. Routing is
Plan integration, not `BATCH_COMMIT`.

**DIRECT_EVIDENCE**

- **Figure 7d** — three stacked genotype panels, **each carrying its own `****` bracket** for PTZ vs
  PTZ+LiCl: `+/+` N = 12 vs 8 · `+/−` N = 12 vs 12 · `−/−` N = 6 vs 7. **Lithium suppresses in wild
  type at the same declared significance level as in the null.**
- **Figure 7b** — the comparator that settles it. Ethosuximide is marked **`n.s.` in `+/+` and
  `+/−`** and significant in `−/−`, and the text declares it: *"ethosuximide pretreatment had no
  effects on the behavior changes in Wwox+/+ and Wwox+/− mice"*. **For lithium the paper declares no
  converse.** ⇒ the assay **can** detect genotype specificity; it did, for the other drug, in the
  same figure and cohort. This is *"we looked and it wasn't there"*, not *"we don't know"*.
- **Six of seven disaggregated components are empty:** no GSK3β readout under lithium, no Tau
  phosphorylation, no target engagement in treated animals, no survival (`Kaplan` and `lifespan`
  return 0 hits in the PMC XML), no behaviour, no myelin, no gliosis, no ECoG.
- The authors state the developmental component themselves: *"Whether lithium treatment can rescue
  the deficits in neuronal migration and differentiation during development in Wwox−/− mice
  **remains to be studied**."*
- ⚠️ **Floor effect, recorded so the argument is not overstated.** In the `+/+` panel the PTZ trace
  peaks near stage 1.3 and sits at 0.3–0.5 for most of the hour, so the wild-type suppression is
  significant against a near-floor baseline. **The magnitude differs between genotypes even though
  the significance does not — and the paper reports no interaction term, so the difference in
  magnitude is not evaluable.** Per-genotype significance stars are not an interaction test.

**LOCATORS**

Caption: *"**d** Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure
activity in Wwox−/− mice."* · Results: *"…significantly suppressed PTZ-induced epileptic seizure in
Wwox−/− mice **(Fig. 7 d)**."* · Methods: *"LiCl (i.p., 60 mg/kg) were pretreated three times within
1 h before PTZ injection."*
Panels re-read at 2× from `files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png`,
sha256 `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542`, native 1946 × 1627 —
digest and dimensions verified equal to the manifest's `source_artifacts` entry.
Manifest: `deepdive_manifests/PMID32000863.json`, entries 0 and 1.

**TRANSFER_BOUNDARY**

Lithium's paediatric use and its general anticonvulsant literature are **T4/T5** and are **not WWOX
evidence**. The paper's own Discussion supplies three non-WWOX mechanisms that would produce the
same result: lithium attenuates PTZ seizures in ordinary mice; it rescues Wnt-dependent cerebellar
midline defects; it induces β-catenin-mediated myelin gene expression in Schwann cells.
⚠️ **Not transferred and not claimed:** the isoform risk. An ATP-competitive or global GSK-3
inhibitor cannot spare **GSK3β2** — enriched in growth cones, maximal in the developing brain,
required for axon growth. `TX-005`'s `SAFETY` score still does not carry it.

**THERAPEUTIC_EFFECT**

Verdict **unchanged — `DEPRIORITIZE`** — reasons strengthened, scope narrowed. Lithium remains a real
anticonvulsant with real paediatric use. 🔴 **The one substantive movement is the removal of
*"disease modifier"***: lithium was tested on **one endpoint, once, acutely, as a pre-treatment**,
in all three genotypes, with **zero** developmental endpoints and the authors' own statement that
the developmental question is unstudied. Calling it a disease modifier in a section headed *"for
clinical discussion"* is the exact inference `N-15` and `CLAIM 031` forbid.

⚠️ **Boundary against over-correction.** The primary's abstract says lithium *"significantly
**abolishes** the onset of PTZ-induced seizure in Wwox−/− mice"*. **The verb *"abolishes"* is the
source's own word and is not a defect.** The defects are the missing genotype boundary, the
abundance clause (see `CC-20260826-GSK3B-S9-AXIS-01`), and *"disease modifier"*.

**REVIEW_REQUIRED:** Plan. Mirror **not** required.

**HUMAN_GATE:** ⚠️ **Yes, advisory.** Practical priority 2 sits under *"for clinical discussion"* and
names a drug in paediatric use. The wording change removes a therapeutic implication rather than
adding one, so it cannot create clinical risk — but the operator should see any edit to that section.
**No clinical recommendation is made or withdrawn here; nothing in this candidate is medical advice.**

---

**REVIVAL_TRIGGER**

*Reopen if a seizure-susceptibility experiment reports a **tested, pre-specified genotype ×
treatment interaction** for lithium in `Wwox−/−` versus `Wwox+/+` — the comparison ethosuximide
already has — **or** if any WWOX system shows a lithium-attributable change in a **WWOX-dependent
molecular readout** (Tau pS396/S404, nuclear β-catenin, or GSK3β kinase output by a **non-pS9**
assay) with a wild-type arm run in parallel.*

**Target WM:** none.
**Batch gate:** not a `BATCH_COMMIT` object.
