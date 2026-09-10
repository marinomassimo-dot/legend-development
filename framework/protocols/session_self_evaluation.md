# Post-batch self-evaluation — the diagnosis a session runs on itself

> Applies to every disease model. Runs **after** the analytical work and **before**
> `legend-session-takeaways`, because takeaways written first will describe a session that
> went well.

## Why it exists

On **2026-07-26** a session did everything the existing checks ask for. It drew studies at
random, triaged them, ranked them, retrieved a full text, read it cover to cover including
every figure, caught an unsupported mechanistic claim in the source, caught a PDF
extraction fault that would have manufactured a false contradiction, persisted a
hash-chained reading receipt, and closed with a tidy summary reporting that the process had
run well.

Four things were nevertheless wrong, and **nothing in the system objected**:

1. The research group behind the paper was never assessed. Doing it afterwards took one
   query and materially changed the reading: 207 papers, 140 on diabetic retinopathy, **one**
   on WWOX. The mechanistic mislabel in the source was not sloppiness, it was predictable
   domain inexperience — which strengthens the unbiased observation and weakens the
   interpretation. Two different weights, invisible without the check.
2. Nothing was written to the **append-only ledgers**, although they are explicit carve-outs
   that a deep dive is allowed to append to. The leads sat in a staging file. The paper was
   findable only in a generated queue and the receipt ledger.
3. The receipt — immutable, hash-chained, tail-anchored — declared outputs
   (`DISC-2026-07-26-A/B/C`, `DISM-2026-07-26-A`) that **did not exist**, in an ID scheme this
   repository does not use. The one subsystem whose entire purpose is trustworthiness held a
   false record, and no tool could see it.
4. No multi-hop expansion was attempted, although the source cited three WWOX-direct papers
   inside its own discussion — including the one underpinning the alternative mechanism used
   to reject its central claim.

The lesson is not "try harder next time". It is that **self-assessment written by the same
agent that did the work is not evidence.** The session graded itself green while all four
held. Whatever can be executed must be executed; only what genuinely needs judgement stays
judgement, and it stays *written down* so its absence is visible.

## The principle that makes this enforceable

**An obligation that produces no artifact cannot be enforced.** Assessing a research group,
measuring field density, expanding multi-hop and cross-querying the corpus all share one
property: skipped, they write nothing. A reviewer — human or machine — inspects what exists,
so a silent omission is invisible by construction. Post-hoc checking cannot fix this. Only
two inversions can:

1. **Give every such obligation a required slot.** The deep-dive work manifest
   (`deepdive_manifest.py`) has one field per obligation. Each is either evidenced —
   integer counts, resolved identifiers, measured hits — or **waived with an argument long
   enough to disagree with**. Silence stops being an option; refusal becomes a position
   someone can challenge.
2. **Gate the strongest claim on the manifest, at the moment the claim is made.**
   `complete_fulltext_read` is the only depth that clears reading debt, so it is the only
   one worth over-claiming. `fulltext_receipts.py record` now refuses it unless the manifest
   validates. Checking afterwards is useless: by then the receipt is chained and immutable.
   This is the difference between reducing the gap and closing it — the claim becomes
   *unavailable*, not merely *auditable*.

**Stated residual.** A manifest can be filled with hollow but well-formed content. This
design does not make that impossible; it makes it reviewable instead of invisible, and makes
the honest path cheaper than the dishonest one. Numbers and resolved identifiers are harder
to fabricate than an unchecked box. Where the ceiling is judgement, Part 2 carries it — in
writing, so that its absence is itself visible.

## Part 1 — Executable. Run it; do not answer it.

```bash
python3 framework/scripts/session_self_eval.py --workspace . --disease wwox
python3 framework/scripts/deepdive_manifest.py --workspace . --disease wwox --pmid <PMID>
python3 framework/scripts/fulltext_receipts.py verify
python3 framework/scripts/legend_lint.py .
```

`session_self_eval.py` enforces five properties and returns `BLOCK_BATCH_COMMIT` on each:

| Check | Property | Catches |
|---|---|---|
| `ORPHAN_COMPLETE_READ` | A paper recorded as completely read appears in a structured ledger/queue/registry section carrying both its PMID/DOI and a real record ID — **not** in a generated view or incidental process note | reading that leaves no scientific trace |
| `UNRESOLVED_OUTPUT_FILE` | Every file a receipt names exists | a receipt promising a dossier nobody wrote |
| `UNRESOLVED_OUTPUT_ID` | Every record ID a receipt names is present in the file it names | the 2026-07-26 defect exactly |
| `OUTPUT_STUDY_MISMATCH` | Every named output file contains the receipt's PMID, DOI or receipt ID | two concurrent studies reusing one candidate filename |
| `WORK_MANIFEST` | Every complete read carries a valid manifest: group assessed **and typed by the evidence it can produce**, primary-for-the-**disease** answered separately from primary-for-the-**gene**, field density measured, **reference list enumerated as an integer**, multi-hop resolved or queued, corpus cross-queried, retraction checked, skills declined with reasons | **the omissions nothing else can see** |
| `UNREAD_PREMISE` | No *new* citation in the reasoning layer — metas, therapeutic strategies, analysis — may lean on a paper with no complete-read receipt, no registry full-text declaration and no queue entry. A **ratchet** against `unread_premise_baseline` in the state manifest: the count may fall, never rise | a conclusion resting on a paper nobody opened — the defect that let PMID 22193544 be load-bearing in five files while unread, with every other check passing |

Two of these came from the **2026-07-26 self-evaluation of the PMID 22193544 run**, and both
describe damage that had already happened rather than damage imagined:

- **`captions_only`** (in the receipt vocabulary, enforced by `fulltext_receipts.py`): that run's
  most valuable finding was a supplementary figure whose panels contradict its own caption. Text
  and caption agreed with each other and both were wrong; only the image showed it. A coverage
  value of `read` that can also mean "read the captions" cannot distinguish a reading that would
  have caught it. `complete_fulltext_read` now refuses `captions_only`.
- **`references_enumerated`**: the same run declared a complete read while its 28-item reference
  list had never been *listed*. Debt had been **declared and not paid** — and the list contained a
  paper (PMID 20067585, the neuron-specific GSK3β isoform) that qualified the reading's own
  inferences and named a therapeutic risk absent from the scoring. An integer is cheap to state
  and hard to fake, which is exactly what a required slot is for.

**On `UNREAD_PREMISE` being a ratchet and not a wall.** First measurement: **17 of the 18** PMIDs
cited in the WWOX reasoning layer had no receipt, no registry full-text declaration and no queue
entry. Blocking on the whole legacy backlog would only teach sessions to route around the check.
Capping it makes every new unread premise a visible regression, and lowering the baseline the only
way to make progress. Three things clear a citation, and only three: a persisted complete-read
receipt, a registry record declaring the full text reviewed, or an explicit full-text-queue entry.
The third is what keeps this honest rather than punitive — **declared reading debt is legitimate
work in progress; silence is not.**

Declared gaps are printed on every run as `[DECLARED GAP]`. They do not block — a queued
multi-hop debt is honest work in progress — but they cannot be hidden, and they accumulate
visibly until closed.

## Part 2 — Judgement. Answer in writing, with evidence, in the takeaways.

Each question is followed by *what a bad answer looks like*, because the failure mode is
answering yes to all of them.

**Sources and depth**
1. Did I read the full text section by section, including figures **as images** and tables,
   or did I read the text layer and the legends? — *Bad: "read the full text" with no
   coverage map, and a `figures: read` that means "read the captions".*
2. Did I read against the grain of the disease label — oncology, adult neurology, animal,
   plant, metabolism — or did proximity to the phenotype decide my attention? — *Bad:
   the deep-dived paper is always the one whose title matches.*
3. What did I find that a keyword search for the gene would **not** have returned? Name it.
   — *Bad: nothing; every finding sits in a sentence containing the gene name.*

**The group behind the paper**
4. What does this group actually do, and how many of their papers concern this gene? Is it
   a primary group for this disease, an adjacent lab, or a first encounter? — *Bad: skipped
   because the journal is reputable.*
5. Descriptive series, or a lab with experiments? Does the evidence type match the strength
   of the claim being made? — *Bad: treating a cohort description and a mechanistic
   experiment as the same kind of support.*
6. **Did group inexperience predict a specific error?** An unbiased hit from a lab with no
   stake in the gene is a *stronger* observation and a *weaker* interpretation. Weigh them
   separately. — *Bad: one global "credibility" score applied to both.*

**Field density**
7. How large is the intersection between this mechanism and this gene in the whole
   literature? A near-empty intersection in a rare disease is a signal, not an absence. —
   *Bad: never measured; two papers and two thousand feel the same.*

**Epistemics**
8. For every conclusion that **closes a door**, did I name the load-bearing premise and tag
   it, and did I record a `REVIVAL_TRIGGER`? — *Bad: rejections stated as verdicts.*
9. Did I separate what the source **shows** from what it **claims**? Did I check whether its
   own figures contradict its own wording? — *Bad: extracting the abstract's conclusions.*
10. Did I distinguish an extraction fault from an author error before asserting a
    contradiction? — *Bad: publishing "the paper contradicts itself" on a text-layer artefact.*

**Compounding — the part that makes the system grow rather than accumulate**
11. Did the reading reach an **append-only ledger**, or only a staging file? — *Bad:
    "proposed entries".*
12. Did I run the **multi-hop**: resolve the sources cited inside, dedup them against the
    registry, queue them? — *Bad: naming a reference number and moving on.*
13. Did I **query the existing corpus** for what I just learned — confirmations, conflicts,
    prior occurrences of this mechanism? — *Bad: the new paper never meets the old ones.*
14. Which **existing claim** does this touch, support, or put under tension? Did I say so
    where that claim lives? — *Bad: a new claim with no edges.*
15. Was the **reading debt written into the queue**, or only mentioned in prose? — *Bad:
    "carried forward" in a summary nobody re-reads.*

**Capability**
16. Which capability grew, and is the growth **disease-agnostic**? — *Bad: a fix that only
    helps this gene.*
17. Did anything break during the run, and did I fix it, register it, or merely narrate it?
    — *Bad: a defect described in the takeaways and left in the code.*
18. If a check caught me, did I **strengthen the check** or just satisfy it? — *Bad:
    renumbering an ID without asking why the collision was possible.*
19. Where the ranking and my judgement diverged, did I record the divergence? A ranking that
    is never contradicted is not being used. — *Bad: silent agreement with every tier.*

**Batch scorecard — mandatory synthesis (no yes/no-only answers)**
20. What are the study's **main message, original contribution and hidden gold**, each with
    a section/figure/table anchor? — *Bad: three paraphrases of the abstract.*
21. Did I apply source parity on two independent axes: **study type** (review as synthesis,
    primary paper as new data) and **recency** (recent frontier work can change a rare-disease
    model)? — *Bad: “review = more important” or “recent = stronger” used as a shortcut.*
22. Did I classify the team as `primary disease group`, `adjacent method expert`,
    `descriptive/clinical`, or `experimental lab`, and weight observation separately from
    interpretation? — *Bad: one reputation score for the whole paper.*
23. Which useful skill, learned gate or inference pattern was used, and which plausible one
    was declined with a reason? — *Bad: invoking everything, or silently using nothing.*
24. Where did each output land: durable ledger/registry, queue, dossier, commit candidate,
    and wikilinks to touched claims? — *Bad: “catalogued” without IDs and paths.*
25. Can the next run answer, mechanically, **full text or abstract only; when; from which
    source fingerprint; with what coverage and supplement status**? — *Bad: a prose note
    disconnected from the receipt ledger.*
26. What friction occurred — wrong path, schema rejection, failed retrieval, extraction
    mismatch, retry, concurrent writer — and did the system catch it before overclaim? —
    *Bad: “everything went smoothly” because the final command passed.*
27. What capability delta will still help on a different gene or rare disease, and what
    regression or gate makes it persist? — *Bad: a one-off wording fix called evolution.*

Write the answers using
[`batch_self_evaluation_template.md`](batch_self_evaluation_template.md). Store the completed
diagnosis in a durable disease-level research path, never only in `staging/`. If the
workspace-wide executable verdict is blocked by a concurrent run, report both the local
paper verdict and the global blocking condition; do not collapse one into the other.

## Part 3 — The attribution census. Required, fixed, parseable.

Added **2026-09-10**, after the 2026-09-09 sweep had to have this reconstructed by hand from
nine prose diagnoses written in inconsistent vocabularies — a reconstruction its own analyst
called *"contestable at the margins"*, over the number that is the most decision-relevant thing
in the record. **It is what tells the operator whether to invest in gates, in auditors, or in
reader practice**, and it was the one thing nine careful diagnoses did not make readable.

Every diagnosis ends with exactly this block:

```
ATTRIBUTION_CENSUS
incidents: <n>
machine: <n>   blind_auditor: <n>   peer: <n>   self: <n>
severity_high: <n>   of which self: <n>
undetected_known: <n>
```

**The counting rule**, so the number is reproducible and not a mood. An **incident** is one
defect or near-error. Repeated instances of one rejection class inside one wave — *"the
validator rejected my locator design four times"* — count as **one**, with the instance count in
the prose. A **catcher** is: `machine` (a validator, writer, linter, screen, test suite, HTTP
status or shell error) · `blind_auditor` (`legend-locator-audit`, run blind on triples) · `peer`
(another actor or the coordinator) · `self` (your own re-reading, cross-measurement, control run,
or refusal to believe a result you had not earned). `severity_high` counts the incidents that
would have **reached the record** — a wrong locator, a wrong coverage claim, a wrong identifier —
as opposed to a schema rejection that could never have got past the writer.

🔴 **The last two lines carry the information the aggregate hides, and they are the reason the
block exists.**

- `severity_high · of which self` is the number to watch. **2026-09-09: 3 of 6.** A rising ratio
  means reader practice is improving; a falling one means the gates are carrying more of the load
  than the readers are — the condition an actor named in wave 1 of that sweep: *"Every one of the
  six was caught by a machine or another agent. Not one was caught by my own re-reading, which is
  the single most useful line in this diagnosis."*
- `undetected_known` — defects found **later** and attributed to this wave — is the only line that
  pushes back on the census's structural blind spot: **a diagnosis is written by the actor, so an
  error nobody caught appears in no list.** The aggregate measures how caught errors were caught;
  it cannot measure the undetected rate. Leaving this line at `0` forever is itself a finding.

Why the aggregate alone misleads, measured on the sweep that produced this section: across 57
incidents the split was machine 24 · self 23 · blind auditor 5 · peer 5, which reads as a
repository whose machines are doing the work. **On the six near-errors that were one step from
landing, the split was self 3 · blind auditor 2 · peer 1 · machine 0.** The validators are
excellent at refusing malformed *declarations* and blind to wrong *content* — that is their
design, and it is why the two controls that actually worked are the ones to invest in.

```bash
python3 framework/scripts/attribution_census.py            # ratios across the diagnoses
python3 framework/scripts/attribution_census.py --queue    # which surfaces are missing the block
```

The parser reports ratios and **never blocks**. A census is a measurement, and a measurement that
can fail a build gets written to pass the build.

## Part 4 — What §21c produced, in a surface that survives the session

§21c's safe-default mechanism is what allows a sweep to run unattended at all: an actor takes the
default, continues, and records it. On 2026-09-09 that machinery ran for ten hours across eleven
waves, and **a repository-wide grep afterwards found `DEFAULTS_TAKEN` in two files** — the brief
that mandates it and one commit candidate. Everything else lived in final messages to the
coordinator, which are transcripts. The evidence of every decision taken without the operator was
gone by morning.

So both go where the actor already writes per-wave state and where it already survives a session
death: **the task contract JSON**, as required keys of each `WAVE_n_RESULT` (Annex A.1). The
shape is in [`../../governance/annex_a_task_contract.md`](../../governance/annex_a_task_contract.md).

**This changes nothing in §21c**, which is reserved to the operator and is not touched: the stop
policy already requires both. What changes is that they land in durable state instead of a
transcript, so a later session can answer *"what did this actor decide without the operator, and
why was it safe?"* from committed artefacts alone. A secondary effect is worth having: the count
of defaults taken per wave becomes a measurable, and **an actor reporting zero defaults across a
ten-hour unattended wave becomes visible as the anomaly it probably is.**

## The rule

A session is not closed by having produced output. It is closed when Part 1 returns `PASS`,
Part 2 is answered in writing, Part 3 carries the census and Part 4's two keys are in the task
contract. **Where an answer is weak, the session owes a proportional micro-upgrade** — and the
upgrade is the answer, not the promise of one.
