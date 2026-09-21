# COMMIT CANDIDATE — CC-20260920-DETECTION-FLOOR-01

**Source:** not a reading. An internal inconsistency between two canonical claims, found by the
blunt-instrument claim audit (`disease-models/wwox/analysis/blunt_instrument_claim_audit_20260920.md`,
39 claims screened) and **re-verified by the orchestrator directly against
`claim_registry_current.md`**.
**Ledger:** `fulltext_receipts.py verify` → **OK: 168 chained receipt(s), tail anchored**.
**Change class:** **MINOR** — one word in one claim, plus one `DEFAULTS THAT BIT US` row.
**Target:** no working-model bump proposed.
**Status:** ✅ `PROPAGATED — BATCH_20260921_001` (2026-09-21), on the Operator's decision of 2026-09-21. ACCEPT. One row of `CLAIM 030` changed: *proteina assente* → *proteina non rilevata al Western blot*, with `PREMISE: DETECTION_FLOOR` and a pointer to `CLAIM 019` (`consolidated baseline`), which records the same datum carefully. Assay, detection context, the rest of the claim and its status are preserved. 🔴 **`D-17` was DEFERRED by the operator and is NOT part of this batch** — it is separable and was not needed to repair the detection floor.
**Status (superseded, kept append-only):** `PROPOSED — NOT PROPAGATED`.
**Review floor:** R2. No claim is reversed, narrowed or removed; `CLAIM 030`'s thesis is **unchanged
and slightly strengthened**, so `legend-locator-audit` (R4) does not apply.

---

## 1 · The inconsistency, quoted from both sides

| Record | Status | What it says about Q230P protein |
|---|---|---|
| **`CLAIM 019`** | **`consolidated baseline`** | `Type:` *"DATO (endpoint funzionale: mRNA normale + **proteina non rilevata**)"* · body: *"qRT-PCR → livelli di trascritto WWOX normali; Western blot → **proteina WWOX non rilevata**"* |
| **`CLAIM 030`** | `in observation` · **VERY HIGH** | *"**Q230P** (SDR) ha **proteina assente** → **severo**"* |

**`non rilevata`** is an assay result bounded by a detection floor. **`assente`** is an absolute.
The registry asserts both about the same protein in the same genotype, and the consolidated-baseline
record is the careful one.

🔴 **Where it bites.** `CLAIM 030`'s own thesis is *"In WWOX the severity tracks residual protein
FUNCTION, not protein abundance."* It is the one claim in the registry whose entire point is that an
abundance measurement does not tell you the answer — and it is the one that converts an abundance
measurement into an absolute. `CLAIM 030` gets this right two clauses later for a different allele:
**G372R** is described as *"proteina **quasi non rilevabile** all'IF"*, correctly hedged. The defect
is one word in one row, inconsistent with the claim's own practice in the adjacent row.

**Why it is not cosmetic.** *Absent* forecloses what *not detected* leaves open. If Q230P protein is
absent, no chaperone, stabiliser or proteostasis strategy can act on it and the prognostic limb is
`funzionalmente null/null`. If it is below a western-blot floor, a residual pool may exist — which is
precisely what a proteostasis lever would try to raise. **The same conclusion arrived independently
from the other direction tonight:** the SDR-readout assessment
(`sdr_missense_readout_assessment_20260920.md`) ends by specifying **PRM/SRM absolute quantification
to replace the western-blot detection floor** as a thing the field does not have. One analysis says
the floor must be replaced; this claim treats the floor as zero.

## 2 · What is proposed, and what is refused

**Proposed, two items.**

**(a)** In `CLAIM 030`, align the wording to the source and to `CLAIM 019`:

> `Q230P` (SDR) ha **proteina non rilevata al Western blot** (→ `PREMISE: DETECTION_FLOOR` — *non
> rilevata* non è *assente*; la soglia dell'immunoblot non è misurata, e `CLAIM 035` registra già
> che in questo sistema un readout scelto male produce un falso negativo) → **severo**.

**(b)** Add one row to `dismissal_ledger_current.md` → `🩸 DEFAULTS THAT BIT US`:

> **D-17** · *"a normal result on a coarse endpoint is a normal phenotype"* · **Why it is FALSE
> here:** this disease has produced the inversion at least four times. `Wwox+/−` mice are normal on
> rotarod, gait and clasping and abnormal on EEG (spontaneous network bursting) and on motor-evoked-
> potential latency (2.13±0.22 ms vs 1.39±0.13, p<0.05). `Wwox`-null cortex is normal on **layer-resolved
> NeuN counts** — *"no significant difference … in neuron number in each cortical layer at PND21"*,
> with the layers themselves delimited *"based on specific morphology of NeuN-positive cells"*, which
> is near-circular — and is mislaminated when read with Satb2/Tbr1 markers and E16.5 BrdU
> birth-dating; neuron **number** is normal, laminar **placement** is not. 🔴 **This is a NARROWING,
> not a self-reversal, and the distinction is the entry's whole point:** the two sets of measurements
> are mutually compatible, taken at non-overlapping ages (PND5–21 vs E16.5→P1), and only the
> *migration* limb of the earlier conclusion falls — its *proliferation* limb was never re-tested.
> What was wrong was not the data but the **unqualified conclusion drawn from an endpoint that could
> not see lamination.** `CLAIM 032` rests on
> neoplasia, lifespan, band intensity and observed behaviour, and its cognition leg is *nobody
> looked*, not *looked and found nothing*. And a western-blot non-detection is recorded elsewhere in
> this registry as protein **absence**. · **Cost:** a negative was, or nearly was, promoted to a
> phenotype in four separate places. · **Rule: a negative result is a statement about an
> INSTRUMENT, not about an organism. Record the endpoint with the negative, or the negative is not
> interpretable. Before accepting "no phenotype", ask what the measurement could have detected had
> the phenotype been present — and if the claim does not name its endpoint, that is the finding.**
> **Corollary, and it is the cheapest thing in this entry:** the heterozygote phenotype is not
> missing from this literature — **it is inside the control groups.** Tochigi pools `+/+` with
> `+/lde` as "normal"; Breton pools het into `S-CTL`; `PAPER 058` reports `0/14 controls`
> undifferentiated; the Aqeilan colony is bred het × het and has published only fertility rate and
> litter size from it.

**Refused, explicitly:** `CLAIM 030`'s thesis is **not** changed · no claim is reversed or
re-statused · `CLAIM 032` is **not** touched here (it has its own candidate) · no therapeutic entry
· no working-model edit · no new field, vocabulary or gate.

## 3 · Why this strengthens rather than weakens

`CLAIM 030` argues that abundance does not predict severity. Replacing *assente* with *non rilevata*
**removes the one abundance absolute in a claim built to distrust abundance**, and makes the Q230P
row consistent with the G372R row beside it and with `CLAIM 019` above it. The claim says the same
thing afterwards, with one fewer thing that a careful reader could use against it.

## 4 · Declared limits

- This candidate rests on **registry text, not on a new reading**. `CLAIM 019`'s underlying source
  was not re-opened tonight; the endpoint quoted is the one `CLAIM 019` itself declares.
- `D-17` cites the `Wwox+/−` electrophysiology from readings at **abstract/metadata depth** (Breton
  2021) and from `partial_fulltext_read` receipts with `figures: unavailable` (Cheng 2020 via
  `PAPER 019`). **No figure panel was inspected anywhere in this batch**, so the entry is written as
  a methodological rule and not as a quantitative finding.
- 🔴 **The `D-17` NeuN row above was itself corrected before landing.** As first drafted it said
  *"bulk NeuN counts"* and *"self-reversal"*, copying the audit. A source-verification task then
  established that Tochigi's counts were **layer-resolved**, and that Iacomino **narrows** rather than
  reverses. Committing the first draft would have put a false contradiction into the ledger — inside
  an entry about not over-reading evidence.
- The audit's other three ranked items (`CLAIM 039`'s *not cerebellar* limb, `CLAIM 013`'s MRI null,
  `CLAIM 014`'s evidence boundary) are **deliberately not included**: they are under source
  verification in a separate task, and a candidate written before that returns would be exactly the
  error this one exists to correct.
