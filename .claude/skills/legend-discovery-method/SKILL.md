---
name: legend-discovery-method
description: LEGEND Scientific Discovery Method V0 — an OPTIONAL toolkit of seven reasoning primitives (enumerate_baseline, diverge, connect_domains, preregister, compress_experiment, recursive_reread, adversarial re-retrieval) for use when a scientific question needs more than a direct lookup. Use it when about to call something first/novel/absent/untested/unique; when one mechanism has been reached too quickly and rivals were never enumerated; when an adjacent literature may carry the assay or the precedent; when a prediction should be fixed before searching; when an experiment must be made to discriminate rather than merely to measure; or when a new question makes an already-read paper worth reopening. No step is mandatory, none gates anything, and invoking one primitive alone is the normal case. Do NOT use it to bypass epistemic_discipline classification, to promote a hypothesis into a claim, or as a template to fill before doing science.
---

# LEGEND Scientific Discovery Method — V0

**A toolkit, not a ritual.** Seven primitives. Use the one the task needs; skipping the other six
is the normal case, not a deviation. Nothing here blocks a `BATCH_COMMIT`, a deep dive, a
hand-back or anything else. Nothing here creates a registry, a role, an approval or a form.

`LEGEND_CORE` **§26** forbids answering a scientific mistake with a new gate, authority, auditor,
registry or workflow. **Every primitive below is a habit, never a check.** A primitive that
becomes a gate has failed, because a gate converts a thinking move into a compliance move, and a
compliance move is satisfied by the cheapest output that passes it.

The evidence for each primitive — the real session instances, the counter-instances, and the
honest admission of which ones are unproven — lives in
[`framework/instruction/LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md`](../../../framework/instruction/LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md).
Read it before arguing that a primitive should be kept or dropped. This file is how to *use* them;
that file is why they exist.

---

## 0 · The one distinction that must not collapse

```
DISCOVERY SPACE                      CANONICAL SPACE
speculation, analogy,                provenance, source depth,
weak connections, rival              epistemic classification,
mechanisms, counterfactuals,         verification, bounded language
predictions, untested experiments
```

`HYPOTHESIS ≠ CLAIM`. `DISCOVERY OUTPUT ≠ CANONICAL FACT`.

Everything this skill produces is **discovery-space output**. It reaches canonical space only
through the ordinary route — `INGEST → DEEP_DIVE → COMMIT` under
[`epistemic_discipline`](../../../framework/instruction/epistemic_discipline.md) — and this skill
grants no shortcut through it. Novelty is welcome on the left. It is not currency on the right.

---

## 1 · The cycle, and permission to skip most of it

```
BASELINE → DIVERGE → CONNECT → HYPOTHESIZE → PREDICT
         → COMPRESS EXPERIMENT → ADVERSARIAL VERIFY → REVISIT
```

**Not every task requires every step.** Concretely:

| Task | Reasonable entry point |
|---|---|
| A factual verification | skip DIVERGE entirely; BASELINE then verify |
| A new mechanism problem | the whole cycle is appropriate |
| A mature experimental design | begin at COMPRESS EXPERIMENT |
| Re-opening a read paper | begin at REVISIT |
| A novelty claim about to be written | BASELINE alone is often the whole job |

A Scientist may invoke only `DIVERGE`, or only `REVISIT`, or only `PREDICT + VERIFY`. That is
correct use, not partial use.

---

## 2 · The seven primitives

### 2.1 · `enumerate_baseline_before_scoring`

**When.** Before writing *first*, *novel*, *absent*, *untested*, *unique*, *never* — or before
grading a re-read's return as new.

**How — two steps, and the second is the one that gets skipped.**
1. **Enumerate** every repository artefact bearing the identifier, *by listing* (`ls`, `glob`,
   registry lookup) — never by guessing filenames.
2. **Read them.** Grep the target concepts across all of them.

> 🔴 **Enumeration without reading is not a baseline.** The primitive's defining failure was a
> re-read that enumerated four artefacts correctly and then measured only one, building a baseline
> that omitted four facts it went on to score as new.

**Bound the absence.** An absence claim states its scope, and the honest ones name at least:
`FILE TYPE` · `LANGUAGE` · `DOCUMENT CLASS` · `SOURCE/QUERY SCOPE`. "No WWOX study examined the
pellet" is not a finding until it says which corpus, which document class, and which query.

**Proportionality.** This is for claims that carry weight. Do not turn every grep into a forensic
project; a search that supports no novelty claim needs no enumeration.

**Do not let it become a gate.** No mandatory pre-search before every sentence.

---

### 2.2 · `diverge_hypotheses`

**When.** One mechanism arrived quickly and the rivals were never written down.

**How.** List **3–7 mechanistically distinct** explanations. *Distinct means they predict
different measurements, not different words.* For each, name the readout that separates it from
its neighbours.

> 🎯 **The discriminator column is the whole value.** A list without it is a brainstorm.

**Correct behaviour on a genuinely single-explanation case: return one, and say so.** Manufacturing
two more to reach a count is the failure this primitive is most likely to die of.

**Do not let it become a gate.** No minimum hypothesis count. Distinctness, not count, is the
property that matters, and distinctness cannot be checked mechanically.

---

### 2.3 · `connect_domains`

**When.** The WWOX corpus is small and self-referential; the constraint that decides a question is
often in a neighbouring literature sharing none of its vocabulary.

**How.** Find the nearest domain where the same *structural* question has been answered — for
mechanism, assay, experimental pattern, rescue strategy or disease analogy.

**Output — mandatory shape:**

```
WHAT TRANSFERS:     …
WHAT DOES NOT:      …   ← never the first without the second
```

> 🔴 **An analogy imported without its `DOES NOT` half becomes a premise.** Every imported datum
> carries its protein/system of origin, always.

**Correct behaviour when no good analogue exists: return none and say why.** Not the nearest weak
match.

**Do not let it become a gate.** No requirement that an analogy be found.

---

### 2.4 · `preregister_prediction`

**When.** Before targeted confirmatory searching on a high-value hypothesis. This is the only
primitive that makes an agent **scoreable**.

**How.** Write the predictions **with their falsifiers**, persist them with the result section
**empty**, in a medium carrying a timestamp the agent does not control. **A git commit is
sufficient and costs nothing.** Then search. Then grade:

`SUPPORTED` · `REFUTED` · `AMBIGUOUS` · `UNTESTED`

> Being wrong is scientifically acceptable. Rewriting the prediction after seeing the evidence is
> not.

**Do not optimise for hit rate.** A hit rate is exactly the wrong objective — the most valuable
predictions on record are the refuted ones. Rewarding accuracy selects for predicting the obvious.

**The way this primitive dies is vagueness, not error.** A prediction too vague to be scored has
already failed.

---

### 2.5 · `compress_experiment`

**When.** A design has been proposed and its components have not been justified individually.

**How.** Build a component-by-component table: for each component, **which hypothesis pair it
separates that nothing cheaper separates.** Components owning no pair are cut — **and each cut
states the blind spot it creates.**

> 🔴 **Compression is not minimisation.** The objective is *discrimination per unit cost*, and
> sometimes that means **adding**. An arm was once added to a design because the proposed readout's
> outcome distribution was narrow — both competing mechanisms predicted the same direction — and
> one extra condition turned a measurement into a discriminator.

**Pairs necessarily with outcome-distribution width:** *an experiment's value is the width of its
outcome distribution, not the importance of the quantity it measures.* A high-value-sounding
experiment whose outcomes do not separate live hypotheses is withdrawn, and withdrawal is a
success of the method, not a failure of it.

#### Executability check — embedded here, deliberately not its own primitive

Before a proposal is called **actionable**, ask five questions:

- required reagent exists?
- required sample exists?
- technique exists?
- readout measurable?
- appropriate comparator exists?

Classify: `EXECUTABLE NOW` · `EXECUTABLE WITH MINOR ADAPTATION` · `REQUIRES NEW REAGENT` ·
`REQUIRES NEW PROGRAM` · `UNKNOWN`.

> A scientifically elegant experiment can still be useless if its required reagent does not exist.
> Discovering that early is a **success** of the method even though the experiment dies.

🔴 **This is a check inside `compress_experiment`, not a gate and not a separate primitive.** Promote
it only if repeated evidence later justifies it.

**Do not let it become a gate.** No cost ceiling, and no rule that the smallest design wins — both
would have deleted the added arm above.

---

### 2.6 · `recursive_reread`

**When.** The scientific state changed and an already-read paper was read against a *different*
question.

```
READ(Q1) → new knowledge → READ(Q2) → new observation → new hypothesis
```

> **A paper being `READ` is not a terminal scientific state.** `complete_fulltext_read` is not a
> property of a paper; it is a property of a paper **and a question**.

**Before reopening, persist:** `OLD QUESTION` · `NEW QUESTION` · `WHY THE QUESTION CHANGED` ·
`PREDICTIONS`. (This is `preregister_prediction` composed with this one.)

**Run `enumerate_baseline_before_scoring` in full as the first act** — both steps. Without it the
grade below is unreliable, and the recorded failures of this pair are all baseline failures.

**After, grade the return:**
`NONE` · `REDISCOVERY` · `NEW DETAIL` · `NEW CONNECTION` · `NEW HYPOTHESIS` · `EXPERIMENT-CHANGING`

> 🔴 **List the zeros.** A re-read that does not report what it looked for and did not find is not
> scoreable. In the two recorded deliberate re-reads, three of five and four of five returns were
> already held.

**Correct behaviour on a question the first read already answered: `NO NEW INFORMATION`, reported
as a success.**

**Receipt obligation — this primitive re-opens an already-read paper, so it must not be
memoryless.** It reuses rather than replaces: locate the **`prior_receipt`** for that paper first,
and emit a new `FULLTEXT_READ_RECEIPT` carrying a `reread_reason` and a reference to that
`prior_receipt`. A re-read that appends no receipt is indistinguishable from no re-read at the next
session, and a re-read that omits its `prior_receipt` reports itself as a first read — which is how
a re-read's rediscoveries get scored as discoveries.

**Persist it.** An emitted receipt is not a durable one:

```bash
python3 framework/scripts/fulltext_receipts.py record --receipt <file>
```

Hand-editing the ledger breaks its hash chain and halts LEGEND. **This primitive needs no new store
at all** — the machinery already exists, which is a point in its favour.

**Do not let it become a gate.** No re-read quota, and no rule that a paper must be re-read before
a claim moves.

---

### 2.7 · Adversarial verification — **a habit, and a pointer to an existing tool**

🟠 **This is deliberately NOT implemented as a new primitive.** LEGEND already has
[`legend-locator-audit`](../legend-locator-audit/SKILL.md), a blind adversarial audit where the
auditor receives only (proposition, quote, anchor) triples and never the reader's conclusions.
**That is a stronger instrument** than verification performed while knowing the conclusion.
Adding a parallel primitive would be precisely the §26 duplication this method exists to avoid.

**What V0 contributes is one habit:** *re-retrieve the source of a load-bearing claim rather than
trusting its quotation.* A delegate's report is a compression of its work, written by the party
with an interest in the conclusion; and the same habit catches the orchestrator's own errors as
often as a delegate's, which is the argument for its being a habit rather than a role.

**Verify what is load-bearing.** Verifying every claim is unaffordable and would displace the
science.

**Sequencing matters:** do not apply the critic so early that DIVERGE never happens. Expand first,
then break.

---

## 3 · Observability — measure value, not compliance

For each primitive actually used, record **one line**: did it change anything?

`PREVENTED FALSE NOVELTY` · `CHANGED HYPOTHESIS` · `CHANGED EXPERIMENT` · `FOUND NEW CONNECTION` ·
`KILLED BAD EXPERIMENT` · `CREATED FOLLOW-UP` · `NO EFFECT`

**A primitive that merely ran does not count. Only outcome changes count.** A primitive repeatedly
producing `NO EFFECT` should be simplified, made rarer, or removed.

There is no store for this and none should be built — the session self-evaluation
([`legend-session-self-eval`](../legend-session-self-eval/SKILL.md)) and the git history already
hold it.

---

## 4 · KEEP / REFINE / DROP — the standard, and where each primitive currently stands

**No primitive is protected because it is part of V0.**

- **KEEP** if repeated use has changed an experiment, prevented false novelty, generated a useful
  hypothesis, enabled a valuable re-read, or exposed an important hidden assumption.
- **REFINE** if useful but noisy.
- **DROP** if it mainly creates ceremony.

Each primitive's own discard criterion, written so that it can actually fire:

| Primitive | DISCARD if |
|---|---|
| `enumerate_baseline` | it is run in full and still misses a held fact that a listing would have surfaced |
| `diverge_hypotheses` | over ten uses, the chosen hypothesis is the first-listed in ≥8 — divergence decorating a decision already made |
| `connect_domains` | an imported analogy is ever load-bearing in a canonical file **without** its `DOES NOT` half |
| `preregister_prediction` | predictions start being written too vaguely to score |
| `compress_experiment` | it cuts a component a later result shows was discriminating (log cuts precisely so this can be checked) |
| `recursive_reread` | three consecutive deliberate re-reads return `NONE` or `NEW DETAIL` only |

🔴 **Honest state at V0.** Most of these have never been observed to fail. That is not evidence
they are sound — it is evidence that too few cases have been built that could break them.
`enumerate_baseline_before_scoring` is the opposite case: its entire evidence base is **negative**
(three failures, no clean success), which makes it the least proven and the most honest entry here.

---

## 5 · Fixtures — the real cases these were derived from

Each is a compact, real instance. They are the regression tests: a change to this method that makes
any of these come out differently needs a reason.

| # | Case | Primitive | Outcome |
|---|---|---|---|
| **A** | **Glucose.** The preferred mechanism turned out to be a **rediscovery** — already stated in the 2014 literature. A rival preserved only because divergence was required produced the session's surviving question. | `diverge_hypotheses` | `PREVENTED FALSE NOVELTY` + `CHANGED EXPERIMENT` |
| **B** | **SDR cross-domain.** An engineered-SDR panel where stabilisation and activity were **anti-correlated**, paired with a pathogenic human SDR missense functionally rescued. They disagree — and the disagreement says the stability and activity axes are decoupled with a lesion-dependent sign. | `connect_domains` | `CHANGED HYPOTHESIS` — interpretation moved from *protein rescue* to *protein rescue + independent functional rescue* |
| **C** | **Repudi 2021 re-read.** Fully read six weeks earlier for dose and myelination; reopened under a cerebellar cell-type question. The value sat in a figure-legend region list the first reader's question had made irrelevant. | `recursive_reread` | `NEW CONNECTION` — the blind spot is the programme's, not one study's |
| **D** | **Puro-PLA.** Elegant discriminator designed; reagent enumeration then showed the required antibody class is **empty** across the censused panel. | `compress_experiment` (executability) | `KILLED BAD EXPERIMENT` — a **success**, despite the experiment dying |
| **E** | **Withdrawn temperature arm.** A high-value-sounding arm withdrawn because outcome width did not guarantee hypothesis discrimination. | `compress_experiment` | `CHANGED EXPERIMENT` — `GENERATE → TEST → WITHDRAW` is a supported path, not a failure |

> Fixtures D and E together carry the method's least intuitive lesson: **an experiment that dies
> under the method is evidence the method worked.**

---

## 6 · What this skill deliberately does not do

- ❌ No gate. Not one primitive may block a `BATCH_COMMIT`, a deep dive or a hand-back. (§26)
- ❌ No new registry, ledger, state file or second scientific registry. Every artefact these
  primitives need already exists: git commits for pre-registration, the discovery ledger for
  hypotheses, `FULLTEXT_READ_RECEIPT` for re-reads.
- ❌ No new authority, role, reviewer, approval mechanism or compliance field. A primitive with a
  checkbox becomes a checkbox.
- ❌ No mandatory template to fill before doing science.
- ❌ No scoring of agents on hit rate.
- ❌ No mandatory counts — of hypotheses, re-reads, analogies or verifications.
- ❌ No workflow engine, and no monolithic "Discovery Framework".

**Reversibility.** This method is two files: this skill and its evidence record. Deleting this
directory removes it completely; nothing else in LEGEND depends on it.

---

## 7 · The success criterion

The criterion is **not** *"the agents followed the process."*

It is:

> **the process caused LEGEND to ask a better question, avoid a false discovery, make a useful new
> connection, or select a better experiment.**

And the sentence the method has to keep earning:

> *Do not judge discovery by how many hypotheses it creates; judge it by whether it changes the
> next experiment.*
