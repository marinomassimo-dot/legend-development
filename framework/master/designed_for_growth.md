# 🌱 The system is alive and always growing — design for that, never for today

> **Superordinate design principle.** Companion to [`gold_is_in_the_details.md`](gold_is_in_the_details.md):
> that one governs *what you must read*, this one governs *what you may build*.
>
> **Provenance.** This file is the canonical home of a principle that lived in the root
> `CLAUDE.md` until 2026-08-16, when that file became a minimal router. The text is preserved,
> not restated. Where a consequence already has an executable enforcement site, this file names
> it rather than describing it twice.

---

> **LEGEND is never finished, and no artefact in it may assume it is.** The corpus grows every
> day. Batches follow batches, exports are periodic and in principle endless, and the model is
> corrected as it grows — correction is not an exception, it is the product.

**Calibrate before designing.** At the time this principle was written: ~15 complete reads, 39
canonical claims, 49 integrated papers, 356 corpus placeholders. One PubMed query on one gene
returns 706 records. The intended trajectory is **hundreds of thousands of full texts and
beyond** — the WOREE field leaders first, then all of WWOX, then everything that cascades: MYC,
WNT, genotypes, phenotypes, symptom-specific therapies, and whatever is needed for the inferences
and the inferences upon inferences. Growth is slow *now* because the infrastructure of tomorrow
is being built so nobody has to reopen it later. **Today's numbers are a starting point, never a
design target.**

Those figures are a narrative anchor and are deliberately not maintained by hand. The machine
counterpart that does get updated — and that fails loudly when it stops matching — is
[`framework/state/growth_anchors.jsonl`](../state/growth_anchors.jsonl), re-anchored by
[`growth_anchors.py`](../scripts/growth_anchors.py). If the two disagree, the anchors are right
and this paragraph is history.

🔴 **The question every check, constant, seal, baseline and ratchet must answer before it
ships: _will this still be informative at the thousandth batch?_** A control that is correct
today and noise at scale is not a control — it is a future alarm nobody hears, and the day it
means something no one will look.

## Five binding consequences, each learned by paying for it

**1 · Never pin a number a human must remember to update.** The change must be re-anchored by
the tool that causes it, as `fulltext_receipts.py record` re-anchors the ledger. The real
criterion is sharper than "automate it": **updating a constraint must cost at least as much as
complying with it.** When updating is cheaper than conforming, the guard is already lost —
someone will bump the number to make the suite green, which is precisely the gesture the check
existed to prevent. That has already happened here, diligent comment and all.
*Implemented and enforced:* [`growth_anchors.py`](../scripts/growth_anchors.py) module contract,
`test_growth_anchors.py`.

**2 · A freeze over living state reports drift; it does not assert violation.** Immutable inputs
are sealed whole. Living state — canonical registries, append-only ledgers — is verified by
*what was consumed*: prefix digests, extracted scope. And because exports are periodic and the
model keeps being corrected, each past seal would otherwise go red at its own moment, correctly
and uselessly. History informs; the gate bites at export time, where shipping a contribution
derived from superseded claims is the real risk.
*Implemented and enforced:* `FREEZE_SCOPE_GATE` in
[`learned_gates_registry.md`](../eval/learned_gates_registry.md), `scripts/test_freeze_scope.py`.

**3 · A fact about an external database is derived and cached, never hand-declared.** At five
hundred manifests "visible in review" means invisible: it presumes a reviewer who, at scale, does
not exist.

**4 · State scale assumptions out loud.** An artefact that silently assumes the current volume is
a defect waiting for a quiet birthday. If a design only works below some size, write the size
down.

**5 · Before building a guard, look for it — it is probably already here.** Three times in one
day the correct pattern existed in this repository, applied at one site and not carried to the
second: `append_only_prefix` in the ledger but not the registries; the corpus marker copied into
four guards; `tracked_paths()` unused by two checks in its own file. The failure mode of a system
that grows by accretion is not ignorance, it is **uneven application**. Grep the vocabulary —
`prefix`, `anchor`, `tracked`, `scope`, `ratchet` — before inventing a mechanism, and if you
diverge from what you find, say why.
*Implemented and enforced:* `PATTERN_ALREADY_SOLVED_GATE` in
[`learned_gates_registry.md`](../eval/learned_gates_registry.md), which carries the full incident
list and two variants beyond the three above.

## Why this principle exists

The receipt ledger was given `append_only_prefix` because someone thought about growth — for the
file that grows. The registries never got the equivalent, and a 2026-08-06 re-seal fixed *which
bytes* were pinned without fixing *what happens over time*. The principle was understood and
applied unevenly, twice. It is written here so the next design inherits it instead of
rediscovering it.

---

## Where this principle is applied elsewhere

| Site | Relation |
|---|---|
| [`mission.md`](../../disease-models/wwox/mission.md) | States the trajectory and the "starting point, never a design target" norm, and delegates the binding consequences here |
| [`learned_gates_registry.md`](../eval/learned_gates_registry.md) | Executable gates for consequences 2 and 5 |
| [`growth_anchors.py`](../scripts/growth_anchors.py) | Executable enforcement of consequence 1; obeys consequence 4 explicitly in its own docstring |
| [`governance/plan_defined_parameters.md`](../../governance/plan_defined_parameters.md) | Applies the thousandth-batch question and consequence 1 to the multi-agent governance parameters |

Consequences 3 and 4 have **no executable enforcement site**. They are carried by review alone,
which is exactly the condition consequence 1 warns about — and is recorded here rather than left
for someone to notice.
