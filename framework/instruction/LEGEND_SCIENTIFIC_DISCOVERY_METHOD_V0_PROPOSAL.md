# LEGEND SCIENTIFIC DISCOVERY METHOD — V0 PROPOSAL

**Status:** 🔴 **PROPOSAL. READ-ONLY. NOT IMPLEMENTED, NOT NORMATIVE, NOT A GATE.**
No code, no governance, no registry and no workflow is created by this file. It has no authority
over any actor and nothing in LEGEND reads it. It exists to be argued with.

**Date:** 2026-09-22 · **Author:** Orchestrator · **Evidence base:** one long autonomous session —
roughly a dozen delegate waves, two deliberate recursive re-reads, and the defects the session
committed against itself and recorded.

---

## §0 · The one design constraint that outranks everything below

The operator's standing directive **§26** forbids answering a scientific mistake with a new gate, authority, auditor,
registry or workflow. **Every primitive here is therefore proposed as a habit, never as a check.**
A primitive that becomes a gate has failed, because a gate converts a thinking move into a
compliance move, and a compliance move is satisfied by the cheapest output that passes it.

Second constraint, from the evidence rather than the law: **a primitive earns its place only from
an instance where it changed an outcome** — a conclusion, a grade, a next experiment, or a caught
error. A primitive that merely ran does not count. The counts below are counts of **outcome
changes**, not of executions.

Third: 🔴 **six of the seven have never been observed to fail.** That is not evidence they are
sound. It is evidence that this session never built a case that could break them. Every
KEEP/DISCARD criterion below is therefore written so that it can actually fire.

---

## §1 · `diverge_hypotheses`

**WHY IT EXISTS.** The first mechanistic explanation an agent produces is the one most available
from its training, not the one best supported by the corpus. Divergence is a cheap forcing function
against that.

**REAL SESSION EXAMPLE.** `DISCOVERY_TRACE` cycle 1 required 3–7 mechanistically distinct
explanations before choosing. My chosen `D1` turned out to be a **rediscovery** — Abu-Remaileh &
Aqeilan 2014 already state that *Wwox*-KO mice *"succumb to hypoglycemia"*. `D3` (multi-system
metabolic derangement) survived **only because divergence was mandatory**, and it produced the
session's surviving question: how does a neuron-restricted `hSynI` vector rescue a death with
peripheral components — acidosis, haematopoietic failure, hypocalcaemia, bone mineralisation — that
count **zero** in the TX-007 analyses?

**WHAT FAILURE IT PREVENTED.** Committing a rediscovery as a discovery, and stopping at the first
plausible mechanism.

**MINIMAL INPUT.** One observation and the instruction *"list 3–7 mechanistically distinct
explanations; distinct means they predict different measurements, not different words."*

**MINIMAL OUTPUT.** A numbered list plus, for each, the readout that would separate it from its
neighbours. **The discriminator column is the whole value**; a list without it is a brainstorm.

**INTERACTION WITH EXISTING LEGEND.** Feeds `legend-hypothesis-forge` and the discovery ledger.
Does not touch the four canonical current files.

**🔴 WHAT MUST NOT BECOME A GATE.** A minimum hypothesis count. The moment "at least three" is
enforced, the third and fourth become padding. **Distinctness, not count, is the property that
matters, and distinctness cannot be checked mechanically.**

**FIXTURE / TEST.** A case with a genuinely single explanation. The primitive is behaving correctly
if it returns **one** and says so, rather than manufacturing two more.

**KEEP / DISCARD.** DISCARD if, over the next ten uses, the chosen hypothesis is the first-listed
one in ≥8 of them — that would mean divergence is decorating a decision already made.
**Evidence count: 2.**

---

## §2 · `connect_domains`

**WHY IT EXISTS.** The WWOX corpus is small and self-referential. The constraint that decides a
question is often in a neighbouring literature that shares no vocabulary with it.

**REAL SESSION EXAMPLE — and the pair matters more than either instance.**
(a) **Lou 2018** (`PMID 29141528`), a protein-engineering paper on an unrelated SDR: across the
whole engineered panel, **stabilisation and activity were anti-correlated** — all seven more-stable
mutants lost activity, the best retaining 28.7 %. (b) **Atanasov 2007** (`PMID 17314322`): a
*pathogenic human SDR missense* (11β-HSD2 `Y338H`) functionally rescued by osmolyte and permissive
temperature.

🎯 **They disagree, and that is the point.** Engineered stabilisation cost activity; natural
destabilisation was recoverable by restabilisation. Together they say the stability and activity
axes in an SDR are **decoupled, with a sign that depends on where the lesion sits** — which is
exactly the unmeasured quantity for `Q230P`.

**WHAT FAILURE IT PREVENTED.** Reasoning about a chaperone strategy with no case of a pathogenic
human missense ever being restored to **measured function** — and, once one was found, treating it
as a green light without reading the clause that bounds it.

**MINIMAL INPUT.** The question, plus the instruction to find the nearest domain where the same
*structural* question has been answered.

**MINIMAL OUTPUT.** 🔴 **A `WHAT TRANSFERS` / `WHAT DOES NOT` pair. Never the first without the
second.** For Atanasov: the existence proof transfers; the dexamethasone arm does not, because the
lesion classes differ (`Y338` is a C-terminal stability element with catalysis intact; `Q230` is
buried, `SASA 0.00 Å²`, and a proline).

**INTERACTION.** Feeds the discovery ledger as `CROSS-DOMAIN-DERIVED`. Every imported datum carries
its protein of origin, always.

**🔴 WHAT MUST NOT BECOME A GATE.** A requirement to find an analogy. An analogy imported without
its `DOES NOT` half **becomes a premise**, and this session has a near-miss of exactly that class:
the uncited *"WWOX omodimerizza via SDR"* clause, which I amplified into a therapeutic fork.

**FIXTURE / TEST.** A question with no good analogue. Correct behaviour is to return **none** and
say why — not the nearest weak match.

**KEEP / DISCARD.** DISCARD if an imported analogy is ever found load-bearing in a canonical file
**without** its `DOES NOT` half attached. **Evidence count: 2.**

---

## §3 · `preregister_prediction`

**WHY IT EXISTS.** An agent that searches first and states its expectation afterwards will always
appear to have expected what it found. This is the only primitive here that makes an agent
**scoreable**.

**REAL SESSION EXAMPLE.** `DISCOVERY_TRACE` §7 was committed **empty** at `fd5bebd`, then the search
ran — and `H1` was graded `REDISCOVERY` rather than retrofitted. Recursive re-read #1 fixed five
predictions at `e2d2c7c` with §§5–6 empty; `P1` and `P2` were **refuted**, and the refutation *was*
the finding. Re-read #2 fixed five more at `ee85697`; `P1` refuted, `P5` partially refuted.

**WHAT FAILURE IT PREVENTED.** Post-hoc narrative. Concretely: without pre-registration, re-read #1
would have reported *"the founding paper is silent on cerebellum"*, which is **false** — it
measured cerebellum, in two figures, through a gate that cannot see Purkinje cells.

**MINIMAL INPUT.** The question, and a commit before the search.

**MINIMAL OUTPUT.** Predictions with **falsifiers**, persisted with the result section empty, in a
medium with a timestamp that the agent does not control. A git commit is sufficient and costs
nothing.

**INTERACTION.** Pairs with `session_self_evaluation`. Needs no new store — the existing commit
history is the instrument.

**🔴 WHAT MUST NOT BECOME A GATE.** A required prediction count or a required hit rate. **A hit
rate is exactly the wrong objective** — this session's most valuable predictions were the refuted
ones. Rewarding accuracy would select for predicting the obvious.

**FIXTURE / TEST.** A case where a pre-registered prediction is so specific that it blinds the
reader to an unpredicted finding. **Not yet observed; it is the failure mode I most expect.**

**KEEP / DISCARD.** DISCARD if predictions start being written so vaguely that they cannot be
scored — vagueness is how this primitive dies, not error. **Evidence count: 3.**

---

## §4 · `compress_experiment`

**WHY IT EXISTS.** Delegates propose experiments that are complete rather than decisive. A design
with six readouts where four discriminate nothing costs a real laboratory real money and produces
the same answer.

**REAL SESSION EXAMPLE.** Scientist I **cut two of six readouts** — degradation kinetics and
localisation — on the explicit ground that *each owns zero cells in the mechanism matrix*, with the
reason *"you cannot chase a band you cannot see"*, and **stated the blind spot each cut created**.
Scientist J compressed to a single three-channel stain. Scientist M reduced its ask to a protocol
amendment on tissue already being discarded.

**🔴 AND THE COUNTER-EXAMPLE, which is why this primitive needs a partner.** I **added** an arm to
Scientist K's design — a 26–30 °C incubation — because the proposed blot's outcome distribution was
**narrow**: both competing mechanisms predicted less soluble protein. One extra plate, no new
reagent, and the same blot separates foldable-but-unstable from fold-incompetent. **Compression is
not minimisation.** The objective is *discrimination per unit cost*, and sometimes that means
adding.

**WHAT FAILURE IT PREVENTED.** Two classes: an expensive design that answers the same question, and
a cheap design that answers none.

**MINIMAL INPUT.** A proposed design and its hypothesis set.

**MINIMAL OUTPUT.** A component-by-component table: for each component, **which hypothesis pair it
separates that nothing cheaper separates**. Components owning no pair are cut, **with the blind spot
each cut creates stated.**

**INTERACTION.** Feeds the therapeutic tracker and decision packets. Pairs necessarily with
`outcome_distribution_width` — *an experiment's value is the width of its outcome distribution, not
the importance of the quantity it measures.*

**🔴 WHAT MUST NOT BECOME A GATE.** A cost ceiling, or a rule that the smallest design wins. Both
would have deleted the 26 °C arm.

**FIXTURE / TEST.** A design where the cheapest variant is genuinely uninformative. Correct
behaviour: **grow** it and say why.

**KEEP / DISCARD.** DISCARD if it ever cuts a component that a later result shows was
discriminating — and log the cut components precisely so that this can be checked.
**Evidence count: 3, plus 1 counter-instance.**

---

## §5 · `recursive_reread`

**WHY IT EXISTS.** A completed read is a read **against one question**. The corpus is small and
mostly already read; new questions arrive faster than new papers.

**REAL SESSION EXAMPLE — two deliberate tests, both pre-registered.**
**#1, Repudi 2021** (`PMID 34747138`), read six weeks earlier for dose and myelination, re-read
under *"can this paper see the cell type its own ataxia rescue implicates?"*. Result: the founding
study reports a **cerebellar** `NeuN⁺WWOX⁺` percentage, and every recording in it is neocortical by
stated coordinates. The blind spot is the **programme's**, not TX-007's. Graded `NEW CONNECTION`.
**#2, Wang 2011** (`PMID 22193544`), read in July for engagement-partner mapping, re-read under
*"what does this paper's handling of its own constructs say about WWOX solubility?"*. Result: a
buffer **named RIPA** containing neither SDS nor deoxycholate — which forced a re-grading of a
census written six hours earlier. Graded `NEW CONNECTION`.

🎯 **Both re-reads found their value in the same place: the part of the paper the first reader's
question made irrelevant.** #1's yield was a figure-legend region list; #2's was a buffer recipe.

**WHAT FAILURE IT PREVENTED.** Treating `complete_fulltext_read` as *finished*. It is not a property
of a paper; it is a property of a paper **and a question**.

**MINIMAL INPUT.** A completely-read paper, a **new** question written before re-opening it, and a
baseline.

**MINIMAL OUTPUT.** `NO NEW INFORMATION` / `NEW DETAIL` / `NEW CONNECTION` / `EXPERIMENT-CHANGING
INSIGHT`, with the zero-scoring returns listed explicitly. **In re-read #1, three of five returns
were already held; in #2, four of five.** A re-read that does not list its zeros is not scoreable.

**INTERACTION.** Requires `FULLTEXT_READ_RECEIPT` with a `reread_reason`, which already exists. This
primitive needs **no new machinery at all** — that is a point in its favour.

**🔴 WHAT MUST NOT BECOME A GATE.** A re-read quota, or a rule that a paper must be re-read before
a claim moves. Cost is one full-text fetch plus a proper baseline; yield so far is one connection
per re-read. **Mandating it would invert that ratio immediately.**

**FIXTURE / TEST.** Re-read a paper under a question the first read **already** answered. Correct
behaviour: `NO NEW INFORMATION`, reported as a success.

**KEEP / DISCARD.** DISCARD if three consecutive deliberate re-reads return `NO NEW INFORMATION` or
`NEW DETAIL` only. 🔴 **Honest state: two instances is not enough to call this reliable. What it has
shown twice is that it returns *something* — not that the something is worth the fetch.**
**Evidence count: 2.**

---

## §6 · `adversarial_verify`

**WHY IT EXISTS.** A delegate's report is a compression of its work, written by the party with an
interest in the conclusion. Verifying the load-bearing claim **at source** is the only way to know
which half survived the compression.

**REAL SESSION EXAMPLE.** Every delegate wave this session received an `ORCHESTRATOR VERIFICATION`
section appended by me, built from an **independent** retrieval. It caught, among others: a
census verified against a tree containing that census (twice); two DOIs written from memory, both
wrong; `Asp223` mislabelled a "salt-bridge partner" when a Gln amide is neutral; a ThermoMPNN CSV
read 1-based when it is 0-based; and a claim that the WWOX SDR *"has never been expressed or
purified by anyone"*, which was too strong — `PMID 21476439` reports two bacterial expression
systems.

**WHAT FAILURE IT PREVENTED.** Propagating a delegate's compression as a measurement. 🔴 **And it
caught my own errors as often as theirs**, which is the argument for its being a habit rather than
a role.

**MINIMAL INPUT.** The load-bearing claim and its identifier.

**MINIMAL OUTPUT.** A verdict per claim — verified verbatim / verified with a bound / refuted —
**plus the bound**, which is usually the informative part.

**🔴 INTERACTION — AND THE MOST IMPORTANT LINE IN THIS FILE.** LEGEND **already has**
`legend-locator-audit`, a blind adversarial audit where the auditor receives only
(proposition, quote, anchor) triples and never the conclusions. **That is a stronger instrument
than what I practised**, because I verified *knowing* the delegate's conclusion. **This primitive
should therefore probably NOT be added to V0 at all** — the honest proposal is to **use the
existing skill more**, and V0's contribution is a habit of re-retrieving sources rather than a new
capability. **Proposing a primitive that duplicates a better existing tool is exactly the §26
failure this file is supposed to avoid.**

**WHAT MUST NOT BECOME A GATE.** Mandatory verification of every claim — unaffordable, and it would
displace the science. Verify what is **load-bearing**.

**FIXTURE / TEST.** A delegate report that is entirely correct. Correct behaviour: a verification
section that says so, briefly, and adds nothing.

**KEEP / DISCARD.** 🟠 **DISCARD AS A NEW PRIMITIVE** — fold into `legend-locator-audit`. Keep only
the habit: *re-retrieve the source of a load-bearing claim rather than trusting its quotation.*
**Evidence count: high, but not attributable to a new primitive.**

---

## §7 · `verify_the_omitted_clause` — HELD AS CANDIDATE, with the A/B measurement the Operator asked for

**The claim.** When checking a headline, read what sits **beside** the quoted sentence: the
transmitted clause was chosen for the claim, and the adjacent one was chosen for nothing.

🔴 **The Operator required that two causes be measured separately before promotion.**
**A** — source-side omission: the *paper* buries the decisive clause next to the quotable one.
**B** — delegate hand-back compression: the *report* drops it in summarising.

### The eight instances, classified

| # | Instance | Cause |
|---|---|---|
| 1 | Atanasov 2007's *"rather than … loss of catalytic activity"* — the clause deciding whether the precedent transfers | **B** (delegate quoted the rescue sentence, not the mechanism sentence) |
| 2 | Hamdan 2006's `BRET_50`-vs-`BRET_max` paragraph — a second free discriminator, two paragraphs past the quoted one | **A** |
| 3 | TX-007's Methods: an **empty parenthesis** beside a populated one ⇒ a deleted catalogue number, not an absent one | **A** (extraction-surface, source-side) |
| 4 | Johannsen's abstract: *"fibroblasts of **one** patient"* — the `n` one clause from the load-bearing result | **B** |
| 5 | Chen 2024: the housekeeping collapse is **UV *plus* cold shock**, in COS7, at 4–22 °C, with **30 °C not studied** | **B** |
| 6 | Breton 2021: *"placed **caudal-side down**"* — the clause explaining *why* the cerebellum is removed | **A** |
| 7 | Wang 2011: a buffer **named** RIPA containing neither SDS nor deoxycholate | **A** |
| 8 | Wang 2011: a GST pull-down with **no lysis step written down at all** | **A** |

**MEASUREMENT: A = 5 · B = 3.**

🟢 **The source-side count is now the majority and stands on its own.** Five instances, five
different papers, four journals, and none of them mediated by a delegate — including the two that
changed the most (#7 forced a re-grading of a census; #6 changed an experiment's cost class). So
the primitive is **not** merely measuring hand-back compression.

🔴 **But it is not promotable to V0 yet, for a reason the counts do not show.** Instances 6, 7 and 8
all come from **two papers read on the same day by the same reader (me) under the same kind of
question — a Methods question**. The source-side value may be a property of **Methods sections**
specifically, not of sources generally. That is a narrower and more useful claim, and it is
testable: run it on Results and Discussion prose and see whether the yield survives.

**STATUS: HELD AS CANDIDATE, per the Operator's instruction. Not proposed for V0.**
**Next measurement required:** source-side instances from **non-Methods** prose.

---

## §8 · The seventh candidate, which arrived by failing

**`enumerate_baseline_before_scoring`** — before judging anything "new", enumerate every repository
file bearing the identifier **by listing**, then **grep the target concepts across all of them**.

🔴 **Observed three times in one day, all three as failures, and never once executed correctly
end-to-end.**
1. Re-read #1's baseline was built from **guessed filenames** and missed a second dossier for the
   same PMID; two rediscoveries were within one step of being graded as discoveries.
2. Two delegates independently proposed as a **first** measurement an experiment published in 2018
   (Johannsen), whose record sits in the discovery ledger under a heading naming the allele.
3. Re-read #2 **enumerated correctly and then measured only one of the enumerated files** — the
   manifest — and so built a baseline that omitted the registry note and the queue entry, which
   together held four facts I would otherwise have scored as new.

🎯 **Failure #3 is the one that defines the primitive: enumeration without reading is not a
baseline.** It has two steps and I have never executed both.

**KEEP / DISCARD.** Cannot be judged — it has no successful instance. **KEEP AS CANDIDATE**, and the
next re-read must run it in full as its first act. It is also the only candidate here whose evidence
is entirely *negative*, which makes it the most honest entry on the page and the least proven.

---

## §9 · What V0 would actually be, if it were built — and what must not be built

**Proposed for V0 (four):** `diverge_hypotheses` · `connect_domains` · `preregister_prediction` ·
`compress_experiment`.
**Held as candidates (three):** `recursive_reread` (2 instances, unproven cost-benefit) ·
`verify_the_omitted_clause` (A/B measured, Methods-confound open) ·
`enumerate_baseline_before_scoring` (three failures, no success).
**Proposed for DISCARD as a primitive (one):** `adversarial_verify` — fold into the existing
`legend-locator-audit`.

**🔴 WHAT MUST NOT BE BUILT, and this is the part I would defend hardest:**
- **No gate.** Not one of these may block a `BATCH_COMMIT`, a deep dive or a hand-back. §26.
- **No new registry, ledger or state file.** Every artefact these primitives need already exists:
  git commits for pre-registration, the discovery ledger for hypotheses, receipts for re-reads.
- **No auditor role and no compliance field.** A primitive with a checkbox becomes a checkbox.
- **No scoring of agents on hit rate.** The refuted predictions carried this session.
- **No mandatory counts** — of hypotheses, re-reads, analogies or verifications.
- **No code in this run**, per the Operator's instruction, and none should be written until at
  least one of the four has a **recorded failure**. Six of seven have none, and a primitive that has
  never been observed to fail has not yet been tested — only used.

**The single sentence V0 would have to earn.** *Do not judge discovery by how many hypotheses it
creates; judge it by whether it changes the next experiment.* Of everything in this session, the
items that met that bar were: the cerebellar `NeuN` gate (changed which stain to run), the 26 °C arm
(changed a blot into a discriminator), the `caudal-side down` clause (changed an experiment's cost
class), and the buffer-name finding (changed how a census must be read). **Three of those four came
from `recursive_reread` or `verify_the_omitted_clause` — the two primitives I am NOT proposing for
V0.** That tension is real, it is not resolved, and it is the reason V0 should not be implemented on
this evidence.
