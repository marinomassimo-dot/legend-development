# 🛠️ Harness development principles — how LEGEND's machine is allowed to change

> **Superordinate design principle**, companion to
> [`gold_is_in_the_details.md`](gold_is_in_the_details.md) (*what you must read*) and
> [`designed_for_growth.md`](designed_for_growth.md) (*what you may build*). This one governs
> **how the harness evolves**. Dictated by the operator on 2026-09-29 (verbatim at the foot) and
> completed by Harness Engineering (`plan`) from principles already binding elsewhere in the
> repository. Where a principle already has a canonical home, this file **names it and does not
> restate it**; if the two ever disagree, the canonical home wins.

**The harness exists to make the science faster and bolder, not safer on paper.** Every principle
below is a consequence of that one sentence.

---

## A · Speed and shape of change

1. **Agility, T0.** A decided change is made now, in the same session, in hours. "Next session",
   "declared debt" and "carried forward" are not places to put an implementable change.
   → [`LEGEND_CORE.md` §21e](../instruction/LEGEND_CORE.md#21e-agile-operating-mode)
2. **No gates on the harness.** No approval queue, no review precondition and no classification
   ceremony stand between a harness change and `main`. Mirror reviews **after** the fact; a finding
   is a new task, never a hold. → §21e GATES
3. **A test is not a gate.** Automatic checks that run in seconds and report a regression are
   welcome; what is forbidden is anything that waits on a person, a round or a token of
   approval. A check earns its place only if it will still be informative at the thousandth
   batch. → [`designed_for_growth.md`](designed_for_growth.md)
4. **Answer a mistake with a habit or a tool, never with a new gate, authority, auditor, registry
   or workflow.** A primitive that becomes a gate has failed: a gate turns a thinking move into a
   compliance move, satisfied by the cheapest output that passes.
   → [`legend-discovery-method`](../../.claude/skills/legend-discovery-method/SKILL.md) (task directive §26)
5. **Simple to modify.** One canonical home per rule; everything else routes to it. A reader
   changes a rule in one place. → [`CLAUDE.md`](../../CLAUDE.md) (router), [`framework/scripts/README.md`](../scripts/README.md)
6. **Stop only when you must.** An actor stops only for an act reserved to the operator or a
   condition with no safe default; everything else takes the default and records it.
   → [`LEGEND_CORE.md` §21c](../instruction/LEGEND_CORE.md#21c-stop-policy)
7. **Decide, act, record.** Every non-reserved decision is taken by the actor and written under
   DECISIONS_TAKEN with how to revert it. A wrong decision is a finding and a revert, never a
   reason to have waited. → [`LEGEND_CORE.md` §21d](../instruction/LEGEND_CORE.md#21d-decision-authority)
8. **The only hard boundaries are the reserved ones:** publication to the public release
   repository, history rewrite, irreversible deletion of unique material, external spend above the
   default (zero), exposure of private or patient data, and changes to §21c–§21e. Everything else
   is harness, and harness is T0. → §21d RESERVED

## B · Where improvements come from

9. **Need-driven.** A harness change answers a concrete need observed in the work of the
   Scientists or of Harness Engineering (a failure, a slowdown, a missed lead), not an idea that
   merely sounds good. The session self-evaluation turns each weak answer into a proportional
   micro-upgrade. → [`legend-session-self-eval`](../../.claude/skills/legend-session-self-eval/SKILL.md)
10. **Continuous micro-upgrades, systematically.** Many small, reversible improvements beat a
    redesign. `CHANGE = NONE` is a valid outcome; a fix is opportunity-driven, never a quota.
    → [`legend-capability-scout`](../../.claude/skills/legend-capability-scout/SKILL.md)
11. **Correction is the product, and it is logged.** Every stop, default, decision and defect that
    taught something is written where the next actor will find it: STOP_LOG / DEFAULTS_TAKEN /
    DECISIONS_TAKEN (§21c–§21d), [`learned_gates_registry.md`](../eval/learned_gates_registry.md),
    the `DEFAULTS THAT BIT US` table in the dismissal ledger. A lesson that lives only in a
    transcript is lost.
12. **Continuous scouting and mining.** Tier-1 repositories and papers are mined every week for
    best practice and fed into a pipeline with a verdict (ADOPT / TRIAL / WATCH / REJECT) and a
    cost in hours. → [`legend-harness-scout`](../../.claude/skills/legend-harness-scout/SKILL.md),
    `governance/candidates/HARNESS-SCOUT-*.md`
13. **Importing a best practice is cheap by design.** Take the pattern, not the runtime: a rule,
    a field, a small script. Check the license before copying code; re-implement when there is
    none. A candidate that needs paid services is a pattern at most.
    → [`_external_repos/MANIFEST.md`](../../_external_repos/MANIFEST.md) inclusion contract
14. **Look before building: the pattern is probably already here.** The characteristic failure
    of a system that grows by accretion is uneven application, not ignorance.
    → [`designed_for_growth.md`](designed_for_growth.md) consequence 5
15. **Measure value, not compliance.** An upgrade is kept for what it changed (a prevented false
    novelty, a changed experiment, a new connection, a revived lead), never because it ran. What
    keeps producing no effect is simplified or dropped. Performance decisions rest on measured,
    back-to-back figures that name their command. → [`legend-research-loop`](../../.claude/skills/legend-research-loop/SKILL.md),
    [`harness_cost_20260928.md`](../../governance/design_records/harness_cost_20260928.md)

## C · Cost

16. **Reduce the cost and tokens of the registries.** Load only what a task needs: selective
    registry access, read by record, never grep the two large registries. A MINIMAL session was
    cut by 82 % this way; the next reductions come from separating current state from history.
    → [`registry_records.py`](../scripts/registry_records.py), [`framework/scripts/README.md`](../scripts/README.md)
17. **Capabilities before actors.** Statistics, parsing, citation resolution, ontology lookup and
    scheduling are software, not agents; models get the jobs that need scientific judgment.
    *(Design record, non-binding: [`sviluppo_lettori.md`](../../governance/design_records/sviluppo_lettori.md) § 129.)*
18. **Zero external spend by default.** Paid APIs, datasets and compute are reserved (§21d).

## D · The science the harness serves

19. **Data → inference → hypothesis → expansion → experiment.** Every output is typed `DATO`,
    `INFERENZA`, `IPOTESI` or `ESPANSIONE`, and a finding is worth what it moves: its lever, its
    next decisive experiment, what changes if it is true.
    → [`epistemic_discipline.md`](../instruction/epistemic_discipline.md), [`CAPABILITIES.md`](../../CAPABILITIES.md) (actionability contract)
20. **Stimulate research; look for gold, not for faults.** The goal is leads for therapies,
    experiments and biomarkers, not dismantling the literature. Speculation, analogy, weak
    connections and rival mechanisms are welcome, and uncertainty is a reason to write the
    hypothesis down, not to drop it.
21. **Boldness and rigor live in two different spaces, and that is what makes both possible.**
    In *discovery space* the rule is freedom; at the boundary of *canonical space* (the four
    current files, through `BATCH_COMMIT`) the rule is provenance. Rigor is not the enemy of
    boldness; it is the price only of what gets promoted. `HYPOTHESIS ≠ CLAIM`.
    → [`legend-discovery-method`](../../.claude/skills/legend-discovery-method/SKILL.md) § 0
22. **No conclusion is sealed.** Conclusions are weakened or strengthened as new studies are
    read; history informs, and a freeze over living state reports drift instead of asserting a
    violation. → [`designed_for_growth.md`](designed_for_growth.md) consequence 2
23. **Nothing dies in silence.** A rejection names its load-bearing premise and what evidence
    would reopen it; every new mechanistic datum re-scans the dismissals. A false negative is a
    compounding loss, a false positive only a cost.
    → [`epistemic_discipline.md`](../instruction/epistemic_discipline.md) § 2
24. **Read as many times as the question needs: read1, read2, read3…** A new question makes an
    already-read paper worth reopening. Each reading leaves its own receipt, so a re-read adds to
    the record instead of replacing it.
    → [`fulltext_read_receipt.md`](../protocols/fulltext_read_receipt.md), `recursive_reread` in discovery-method
25. **Parity of sources.** No tier, score or disease context authorizes *not* reading; the gold
    is in the details, and often in the oncology paper nobody filed as relevant.
    → [`gold_is_in_the_details.md`](gold_is_in_the_details.md)
26. **Accumulate, never lose.** Supersede instead of overwriting; better redundancy than deletion;
    what is not read today becomes explicit reading debt.
    → [`LEGEND_CORE.md` §22](../instruction/LEGEND_CORE.md#22-final-maxims)
27. **Privacy is the layering.** Generic engine, public disease model, and a private overlay that
    is never in this repository and never leaves its perimeter. No query to an external tool
    carries individual-level data. → [`CLAUDE.md`](../../CLAUDE.md) § 0

---

## Tensions, and how they are resolved

| Apparent conflict | Resolution |
|---|---|
| "Not too rigorous" (20) against receipts, LINT and `BATCH_COMMIT` | Principle 21: freedom in discovery space, provenance only at promotion. Receipts are method, not ceremony (§21e GATES). |
| "No gates" (2) against learned gates and regression suites | Principle 3: an automatic check that reports is a test; a gate is waiting on someone. |
| "Continuous upgrades" (10) against a harness that must stay simple (5) | Principles 14 and 15: look before building, and drop what shows no effect. A small toolkit that is used beats a large one that is complied with. |

---

## Operator's dictation, 2026-09-29 (verbatim)

> agilità, flessibilità, no rigidità e gate, governance e harness semplice da modificare,
> semplicità di implementazione di nuovi pattern considerati best practice ed estrapolati da
> altre repo tier 1, riduzione costo e token dei registri,e conclusioni scientifiche non vengono
> sigilate ma possono essere indebolite e potenziate dopo aver letto altri studi, gli studi
> possono essere letti più volte read1, read2, read3... in base alle necessità degli Scientist,
> paradigma dato-inferenza-ipotesi-espansione-esperimento, focus su creare stimolo alla ricerca
> e cercare spunti terapeutici anche a costo di non essere eccessivamente rigorosi: lo scopo non
> è essere troppo rigorosi e smontare tutta la ricerca ma cercare gold nei dettagli e cercare
> spunti per terapie, esperimenti, miglioramento continuo di harness e legend, micro upgrade
> continui, correction log e mmigro upgrade sistematici, migliorie implementate sulla base delle
> esigenze concrete di Legend e attività degli Scientist e di Harness Engeneer, scouting e mining
> continuo e ricerca di best practice per creare pipeline di sviluppo

Principles 1–2, 5, 9–13, 16, 19–22 and 24 come from this dictation. Principles 3–4, 6–8, 14–15,
17–18, 23 and 25–27 were added by Harness Engineering from the canonical homes named beside each.
