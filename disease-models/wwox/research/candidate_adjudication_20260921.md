# Adjudication of the four parked commit candidates — 2026-09-21

> **READ-ONLY. Nothing here is propagated.** Each verdict is a recommendation to the Operator, in the
> fixed vocabulary `ACCEPT` / `ACCEPT WITH NARROWING` / `DEFER` / `REJECT`. Every factual anchor below
> was re-verified by the Orchestrator directly against `claim_registry_current.md`,
> `paper_registry_current.md` (via `registry_records.py`, never grepped) and the receipt ledger —
> not taken from the candidates' own prose.

## Summary table

| Candidate | Evidence strength | Canonical impact | Risk if accepted | Risk if rejected | Recommendation |
|---|---|---|---|---|---|
| **`CLAIM032-ENDPOINT-QUALIFIER`** | **Strong on the negative**: three sources enumerated, endpoints checked, and the quotation defect verified in the source. Weak on the counter-signal (one conditional-Cre slice result without a statistic, one single-lab aged finding). | **High and asymmetric.** `CLAIM 032` is `VERY HIGH` clinical relevance and its corollary sets the **dose threshold for every restoration lever**. | **Low.** No reversal, no status change. The residual risk is over-reading three subclinical instrument findings as a phenotype — mitigated by keeping them as `flag, not reversion`. | 🔴 **High.** The claim's title asserts *"haploinsufficiency **is not deleterious**"* and its summary opens *"La perdita di un solo allele di WWOX **non produce fenotipo**"* — while its own third leg is `nobody looked`. A dose argument keeps resting on an absolute the evidence does not carry. | **ACCEPT WITH NARROWING** |
| **`DETECTION-FLOOR`** | **Very strong.** A pure internal inconsistency, verified verbatim on both sides, requiring no new reading. | **Medium.** One word in one `in observation` claim, plus one `DEFAULTS THAT BIT US` row. | **Very low.** The change makes the claim *weaker in wording and stronger in fidelity*; `CLAIM 030`'s own thesis is unaffected and slightly reinforced. | **Medium.** *Absent* forecloses what *not detected* leaves open, and the foreclosed thing is the entire proteostasis lever. | **ACCEPT** |
| **`CLAIM039-CEREBELLAR`** | **Strong on the exclusion's fragility** (one hedged sentence, no quantitative motor test in 32 locators). **Weak on the counter-evidence** (one passing sentence, no number, n=3, unblinded, never captured as a locator). | **Medium-high** — it narrows a canonical **title**, the most-read line of a claim. | **Medium.** The real risk is the one the Operator named: letting *"delayed foliation"* at P1 become a demonstrated cerebellar contribution. The proposed text already refuses that, and the narrowing must not go further. | **Medium.** The title states a negative the source does not support, and a second propagation defect stays unrecorded. | **ACCEPT WITH NARROWING** |
| **`PAPER34140629-PROMOTION`** | **Strong on provenance, and it is the only thing at stake.** Receipt `FTR-20260920-34140629-01` exists; artefact present at **61,298 bytes** with `sha256 a2d6f1c1…` matching the candidate; `CORPUS-STUB-150` is live in the registry. | **Minimal.** A stub becomes a `PAPER` record. No claim, no link, no working-model edit. | **Very low.** | **Low but cumulative** — a read paper left as `not_processed` is how the same paper gets re-read, which happened twice this week for exactly this reason. | **ACCEPT** |

---

## 1 · `CLAIM032-ENDPOINT-QUALIFIER` — the transformation the Operator asked me to test for is present

**The test:** *does the current wording turn "no evidence under specific endpoints" into "no phenotype / not deleterious"?* **Yes, in two places, and one of them is the title.**

- **Title, verbatim:** *"WWOX haploinsufficiency **is not deleterious**: the therapeutic threshold is well below full restoration"*.
- **Summary, first sentence, verbatim:** *"La perdita di **un solo** allele di WWOX **non produce fenotipo**."*

What the three sources measured: **survival, lifespan, growth, gross morphology, spontaneous neoplasia and overtly observed behaviour.** No cognition, no EEG, no network excitability. And the Aldaz quotation is, in its source, a **tumour sentence** — *"…appears not to be deleterious **or carcinogenic**"*, following *"no evidence of spontaneous neoplasia in any tissue examined"*. The registry's shortened form reads as a statement about organismal phenotype. **That is a `D-15` defect and it is ours.**

### The minimum narrowing — and it is genuinely minimal

**Do not** change the status, **do not** withdraw haploinsufficiency, **do not** promote the counter-signals. Change the two absolutes to name their endpoint class, and let the qualifier carry the rest:

> **Title:** *WWOX haploinsufficiency is not deleterious **for survival, growth and gross morphology**: the therapeutic threshold is well below full restoration* — **on those endpoints**.
>
> **Summary, first sentence:** *La perdita di un solo allele di WWOX **non produce fenotipo sugli endpoint misurati** (sopravvivenza, crescita, morfologia macroscopica, neoplasia spontanea, comportamento osservato). `PREMISE: NOBODY_LOOKED` su cognizione, EEG ed eccitabilità di rete.*

🔴 **The corollary is where the therapeutic weight actually sits, and it needs one clause, not a rewrite.** *"Correggere o compensare un solo allele basta"* must become *"basta **per gli endpoint su cui la soglia è nota**"*. The dose argument survives; it stops being unconditional.

**What I would refuse from this candidate:** its § 3 table presents the three subclinical findings as *"the pattern across the independent sources is the finding"*. That is one conditional-Cre slice result with **no statistic** for het vs WT (4/23 vs 0/11, Aqeilan a co-author), one single-lab latency measurement, and one single-lab aged-memory finding with **no n** in the relevant section. **Carry them as `REVIVAL_TRIGGER` material, not as "three laboratories".** The candidate's own text already does this; the framing above it does not.

---

## 2 · `DETECTION-FLOOR` — the distinction is real, verified, and consequential

Verified verbatim on both sides of the registry:

- **`CLAIM 019`** (`consolidated baseline`): *"qRT-PCR → livelli di trascritto WWOX normali; Western blot → **proteina WWOX non rilevata**"*.
- **`CLAIM 030`** (`in observation`, `VERY HIGH`): *"**Q230P** (SDR) ha **proteina assente** → **severo**."*

**`non rilevata` is an assay result bounded by a detection floor. `assente` is an absolute.** The consolidated-baseline record is the careful one, and the claim that departs from it is the one whose entire thesis is *"severity tracks residual protein **function**, not abundance"* — the one claim in the registry whose point is that an abundance measurement does not settle the question. It also gets it right two clauses later for a different allele: **G372R** is *"proteina **quasi non rilevabile** all'IF"*, correctly hedged.

**Why it matters and not merely tidies:** *absent* forecloses a residual pool; *not detected* leaves one open. The foreclosed object is exactly what a chaperone or proteostasis lever would act on — and `TX-003` is built on that possibility. The SDR-readout assessment reached the same place from the other direction, specifying **PRM/SRM absolute quantification to replace the western-blot floor**. One analysis says the floor must be replaced; the claim treats the floor as zero.

**`ACCEPT`, with one caution about scope:** change **one word in one row**, plus the `PREMISE: DETECTION_FLOOR` tag. **Do not** restate `CLAIM 030`'s thesis, **do not** touch `CLAIM 019`, **do not** extend the same edit to other alleles in the same table without checking each against its own source. The candidate's `D-17` row is a separate, larger proposal and should be judged on its own merits — see §6.

---

## 3 · `CLAIM039-CEREBELLAR` — accept the narrowing, refuse the upgrade

**The exclusion is thin and that is verified:** `CLAIM 039`'s title asserts *"it is not cerebellar"*; its source's entire basis is one hedged Discussion sentence — *"we did not detect any **marked** pathologic changes in the cerebella"* — on an unblinded light-microscopy look, with **no quantitative motor test anywhere in 32 enumerated locators**. `PMID 17803050` has no DOI and no PMCID and is **permanently unobtainable here**, so the histology's n, age, stain and section plane cannot be recovered.

**The counter-evidence is real but small:** the same strain, same colony, `PMID 32581702` at **P1**: *"the development of cerebellum was delayed … as shown by reduced number of foliation"* — **one passing sentence, no number, n=3, unblinded, and never captured as a locator**. That last part is the finding worth recording: a **second instance** of the propagation defect already on `CLAIM 016`.

### Preserving the epistemic mood — the Operator's specific instruction

The two are **compatible as measurements**: the ages are disjoint (P1 vs ~28 days), and a developmental delay at P1 need not leave *marked* pathology at 28 days. **That compatibility is the whole point** — it is why the 28-day silence was never evidence of cerebellar normality, and equally why the P1 sentence is not evidence of a cerebellar contribution to the ataxia.

**Accept:** the title narrowing to what the source supports, the evidence boundary with `PREMISE: LIGHT_MICROSCOPY_FLOOR`, and the `BLOCK 2` endpoint column.
**Narrow further than the candidate proposes, in one respect:** the evidence boundary should say in its own words that **neither record establishes a cerebellar contribution to the ataxic gait**, so that a later reader cannot take the juxtaposition as an argument. The `REVIVAL_TRIGGER` (Purkinje counts, foliation index, molecular-layer thickness, or a motor battery) is correct as written.

⚠️ **And the human material from this session must not enter here.** `PMID 26345274`'s *"a characteristic pattern of neurodegeneration in which the cerebellum is spared"* is (a) an **abstract**, (b) written as *"We **suggest**"*, and (c) **contested** — `PMID 35573960`, read in full, reports vermian hypoplasia from day 7 and states that cerebellar vermis hypoplasia *"have been described in most cases"*. **A human MRI volume statement and a rat light-microscopy statement are not the same proposition and must not be scored against each other.** `CLAIM 039` should remain a **rat** claim.

---

## 4 · `PAPER34140629-PROMOTION` — provenance checks out; accept

Verified independently, not taken from the candidate:

| Requirement | Verified |
|---|---|
| Full-text receipt | `FTR-20260920-34140629-01`, **1 event for this PMID** ✅ |
| Evidence depth | `partial_fulltext_read`, `coverage.figures: unavailable` ✅ — and the proposed record **says so** |
| Provenance | artefact present, **61,298 bytes**, `sha256 a2d6f1c11595b65e…` matching the candidate ✅ |
| Registry state | `CORPUS-STUB-150` live at `paper_registry_current.md:2157` ✅ |
| Scientific relevance | **Honestly low, and the record says so**: `T3`, `clinical relevance: LOW`, no WWOX-DEE allele, all endpoints oncological, **and it deliberately generates no claim** ✅ |

**This is the cleanest of the four.** A read paper carrying `not_processed` is how a paper gets re-read — which happened twice this week for that exact reason. The promotion costs nothing and closes that door. **`ACCEPT` as written.**

---

## 5 · What I would not do with any of them

- **No `BATCH_COMMIT` is proposed here**, and none of these is propagated. This document is an adjudication, not a commit.
- **No working-model version bump** is warranted by any of the four.
- **No new claim, no new therapeutic entry, no new field or vocabulary** is created by accepting all four as recommended.

## 6 · One item inside `DETECTION-FLOOR` that should be judged separately

The candidate bundles **`D-17`** — a new `DEFAULTS THAT BIT US` row generalising *"a normal result on a coarse endpoint is a normal phenotype"*. That is a **framework-level addition**, not a claim repair, and it arrives in the same session where the Operator asked that new structure not be added reflexively. It is also **substantively true and well-evidenced** (four instances). **Recommendation: `DEFER` the `D-17` row and `ACCEPT` the one-word claim repair now.** They are separable and the repair should not wait on the generalisation.

---

*Orchestrator, 2026-09-21. READ-ONLY; no canonical file modified; no candidate propagated. Every quotation re-verified against the registry at commit `4e053ba`. Not medical advice.*
