# FAQ — you just cloned this repository, now what?

Seven questions a new reader asks first, answered honestly. Where a claim has a
maturity status, it is stated: a capability is not "shipped" because a file
describing it exists. The vocabulary — **BUNDLED**, **IMPLEMENTED**,
**SPECIFIED**, **EXTERNAL** — is defined in [SKILLS.md](SKILLS.md).

> This is an orientation document, not canonical scientific state, and nothing
> here is medical advice.

---

## 1. What can you actually do?

LEGEND is not a chatbot with a bibliography attached. It is **22 composable
skills** and **5 subagents** operating over a set of versioned Markdown state
files, with gates between the stages. Five families:

| Family | What it does | Representative skills |
|---|---|---|
| **Acquire** | Triage a study list of 1 or 5 000 records, deduplicate it against every registry, retrieve full texts through a tiered lawful-access cascade, quarantine each new source before it can touch the canonical state | `legend-study-intake-triage` (BUNDLED) · `find-fulltext` (SPECIFIED, needs network) · `legend-ingest` |
| **Analyze** | Read a full text section by section with a coverage map, tag every assertion epistemically, sweep a whole batch for signals that keyword filtering would drop, run cited RAG over the local corpus | `legend-deepdive` · `legend-discovery` · `legend-batch-inferential-sweep` (BUNDLED) · `legend-paperqa` (EXTERNAL) |
| **Generate** | Forge scored therapeutic hypotheses through a generate → critique → rank → evolve loop, triage splice-correcting antisense rationale, rank papers by concrete mechanistic utility | `legend-hypothesis-forge` (IMPLEMENTED) · `legend-aso-designer` · `legend-proband-priority-matrix` (BUNDLED) |
| **Safeguard** | In-silico ADMET / blood–brain-barrier druggability triage, structural integrity LINT, all-or-nothing batch commits with snapshot and restore | `legend-safety-triage` (EXTERNAL) · `legend-commit` (BUNDLED) · `legend-lint-repair-plan` |
| **Grow** | End every session with at least one capability micro-upgrade, and validate any procedural change against a baseline before adopting it | `legend-capability-scout` · `legend-research-loop` · `legend-session-takeaways` |

The full catalogue, each row with its maturity status, its inputs and its
outputs, is in [SKILLS.md](SKILLS.md). The census of the underlying patterns is
in [CAPABILITIES.md](CAPABILITIES.md).

**What runs without any agent runtime at all:** the structural LINT, the batch
commit machinery, the coverage and queue reports, the semantic-graph generator,
the release gate and every regression suite — plain Python, standard library.
See [Quick start after cloning](README.md#quick-start-after-cloning).

---

## 2. What makes it different — in analysis, and in how it grows?

**In analysis**, four things a summarizer does not do:

- **Full text or nothing.** Every analysis route emits a coverage map and a
  hash-chained `FULLTEXT_READ_RECEIPT`. Retrieval, indexing and RAG queries do
  not count as reading. Contract:
  [`fulltext_read_receipt.md`](framework/protocols/fulltext_read_receipt.md).
- **`grep` is forbidden as a method of analysis.** It may find a file,
  deduplicate a list or audit after the fact. It may never decide what a paper
  says.
- **Context is never dropped.** A result carries its variant, species, tissue,
  cell type, developmental stage and assay; transferring it elsewhere is an
  explicit, tagged act.
- **Nothing dies in silence.** Every rejection is written to the dismissal
  ledger with the premise it rests on (`PREMISE_TAG`) and with a
  `REVIVAL_TRIGGER` naming the evidence that would reopen it. A false positive
  gets tested and dies; a false negative is silent, permanent and compounds.

**In growth**, the part that is a pattern and not a slogan. Three concrete
mechanisms, each with a file behind it:

1. **Every session leaves a capability micro-upgrade.** Not "the system learns"
   — an actual named artifact: a new gate, a new regression fixture, a fixed
   heuristic, an imported tool. `legend-capability-scout` runs at the end of
   every session and its output is proportional to what was learned.
2. **Every real error becomes a named guardrail.** The library in
   [`learned_gates_registry.md`](framework/eval/learned_gates_registry.md) —
   `DEGRADATION_DIRECTION_GATE`, `MECHANISM_DIRECTNESS_GATE`,
   `KG_EDGE_HAS_NO_SIGN`, `PROTEIN_STATE_IDENTITY_GATE` and the rest — was not
   designed up front. Each entry is a mistake that actually happened, converted
   into permanent immunity for its whole class. Those same gates seed the
   failure benchmark in [`framework/eval/`](framework/eval/).
3. **New evidence re-audits old conclusions.** When a new mechanistic `DATO`
   arrives, the dismissal ledger is re-scanned for rejections whose premise it
   touches. This temporal loop is the difference between self-*correction*
   (fixing an answer) and self-*improvement* (fixing the process that produced
   it).

And a change to the machinery is not adopted because it sounds better:
`legend-research-loop` requires a baseline, one changed variable, a pre-declared
success criterion and a `KEEP` / `DISCARD` / `INCONCLUSIVE` / `CRASH` verdict.

---

## 3. How do I start it?

Open the cloned repository in an agent runtime that reads instruction files —
the skills are authored for [Claude Code](https://claude.com/claude-code), which
discovers them from `.claude/skills/` automatically — and say what you want:

```text
"start a LEGEND session"           → selects context for the task, runs LINT, declares READY or BLOCK
"work this list of PMIDs"          → the autopilot: intake → sweep → ranking → retrieval → deep dive → commit gate
"deep dive this paper"             → coverage map → dossier → COMMIT CANDIDATE
"squeeze this paper for leads"     → grows the discovery ledger (biomarker / molecule / repurposing)
"generate therapeutic hypotheses"  → the co-scientist loop over what is already known
"what's new on WWOX"               → a recency-first literature sweep
```

Practical first move: **paste a list.** PMIDs, DOIs, titles, a PubMed Clipboard
export, a mixed and messy citation list — triage normalizes and deduplicates it
before anything expensive happens. You can also start with no list at all and
ask the system to look for what is new; see the next question.

Before any of that, copy
[`.claude/settings.json.example`](.claude/settings.json.example) to
`.claude/settings.local.json` and read its security note. Permissions are yours
to set, deliberately.

If you only want to verify the repository is sound, no agent required:

```bash
python3 framework/scripts/legend_lint.py .
python3 scripts/test_link_targets.py
```

---

## 4. Do you find the studies yourself, or must I paste them?

**Both — and the blend is the intended mode of operation.**

| Route | Who drives | What happens |
|---|---|---|
| **You paste** | You | A PubMed Clipboard export, PMIDs, DOIs or raw titles. [`pubmed_clipboard_to_seed.py`](framework/scripts/pubmed_clipboard_to_seed.py) turns a snapshot into a batch seed; triage deduplicates it against the paper registry, the tracking log, the queue and the commit queue, so you never pay twice for the same paper. |
| **The system searches** | The system | The `wwox-scout` agent runs recency-first sweeps across PubMed and grey literature; `find-fulltext` chases a specific paper through ten retrieval tiers; the discovery skill autonomously generates and pursues the follow-up searches a lead implies. |
| **The system expands your list** | Both | From what you pasted it pulls related and cited work, chases the partner protein or assay a paper exposed, and queries the local full-text corpus for confirmations and contradictions across papers. |

Why the blend rather than full automation: a human list carries intent — you
know why those papers landed on your desk — while autonomous search catches what
intent misses, which for WWOX is most of the useful material, because the
mechanistic biology tends to live in oncology and adult-neurology papers whose
titles promise nothing about a neurodevelopmental disorder.

**Honest about requirements:** autonomous search reaches public services over
the network. The PubMed retrieval used by the scout and dossier agents comes
from an MCP server you configure in your own runtime; it is not bundled here,
and no API key ships with this repository. Offline, the dedup, ranking, LINT,
commit and report tooling still runs on your own registries.

---

## 5. Why is this better than asking a normal chat?

A chat answers. This accumulates. Concretely:

| A normal chat | LEGEND |
|---|---|
| State lives in the conversation and dies with it | State lives in versioned files; **rebuilding canonical files from chat memory is forbidden** |
| An assertion is fluent text | Every assertion is tagged `DATO` / `INFERENZA` / `IPOTESI` / `ESPANSIONE`, with its source and its context |
| Reads an abstract, sounds confident | Reads the full text, emits a coverage map, and records reading debt for whatever it did not read |
| Silently overwrites yesterday's conclusion | Changes pass a LINT gate and an all-or-nothing batch commit with snapshot and restore; history is never erased |
| Discards a lead invisibly | Records the rejection, its premise, and what would reopen it |
| Repeats the same class of error indefinitely | Turns each observed error into a named gate and a regression fixture |
| Starts each session equally capable | Starts each session more capable than the last — that is the whole bet |

The counterpart of the honesty: it is slower, it says "I have not read this" more
often than you would like, and it will refuse to promote a plausible hypothesis
to a conclusion. That is the intended trade.

---

## 6. What is the mission, and where does it go from here?

The full statement is
[`mission.md`](disease-models/wwox/mission.md). In short: build a cumulative,
auditable, continuously improving mechanistic intelligence system for WWOX —
connecting the whole cross-domain literature to mechanisms, biomarkers,
therapeutic hypotheses and the decisive experiments that would discriminate
among them. Two inseparable products: a growing body of knowledge, and a growing
system capable of handling it. Either one alone degrades — knowledge without
capability becomes unmanageable, capability without evidence becomes
speculation.

The rails along which it develops:

- **Depth of corpus** — from a triaged bibliography toward complete, receipt-backed full-text coverage, with reading debt reported rather than hidden. Current state: [`coverage_report.md`](disease-models/wwox/registries/coverage_report.md).
- **Mechanism resolution** — turning associated pathways into a *signed* causal map: does WWOX loss raise or lower this node, in which cell type, in which developmental window.
- **Biomarkers** — Tier 1/2 proximal readouts of WWOX-linked biology, kept strictly separate from Tier 3 distal clinical endpoints, with a defined validation path each.
- **Drug repurposing** — a declared objective and a staged track. It opens as the other rails mature: gene and protein function, signed pathway direction, a proximal readout, and CNS/paediatric safety. Until then, candidates stay hypotheses in the discovery and hypothesis ledgers, never described as treatments. See [Track C](disease-models/wwox/mission.md#drug-repurposing--a-declared-objective-deliberately-staged).
- **Interoperability** — alignment with the [Monarch Initiative](https://monarchinitiative.org/) ontologies and a [DisMech](https://dismech.monarchinitiative.org/)-compatible contribution, so the model is consumable outside this repository.
- **Measured reasoning failure** — a public failure benchmark and a reproducible evaluation comparing base model, structured schema and schema-plus-guardrails, including a temporal T0→T1 test of whether new evidence reopens the right earlier conclusion. Spec: [`framework/eval/`](framework/eval/).
- **Portability** — the engine is disease-agnostic; WWOX is the first implementation, not the boundary. [`framework/ADOPTING.md`](framework/ADOPTING.md).

What is available now versus in development is stated at the top of
[README.md](README.md), and the outstanding items are tracked by name in
[`release/losslessness_manifest.json`](release/losslessness_manifest.json).

---

## 7. Why invest in this one?

Addressed to anyone deciding where to put compute, funding or attention —
including [Anthropic's AI for Science](https://www.anthropic.com/) rare-disease
track, for which this work is being proposed.

**It scales past its own disease.** Roughly 7 000 rare diseases exist, most with
a scattered literature, no model organism consensus and no approved therapy. The
expensive part of LEGEND is not the WWOX content — it is the engine: epistemic
discipline, provenance model, reading-debt controls, the semantic-link contract,
falsification procedures, the failure-aware evaluation and the capability-growth
loop. All of that is disease-agnostic and documented for reuse in
[`framework/ADOPTING.md`](framework/ADOPTING.md). A second disease reuses the
method and rebuilds the evidence from its own literature; it does not inherit
WWOX conclusions.

**It unites the people a rare disease usually keeps apart.** Researchers hold
the mechanisms, clinicians hold the phenotype and the feasibility constraints,
foundations hold the funding and the continuity, and family communities hold the
longitudinal observations and the urgency. They rarely share one artifact,
because each needs a different view of the same evidence. A provenance-tracked,
navigable model with explicit epistemic status is a substrate all four can read
without any of them having to trust an unsourced summary — which is exactly why
the honesty layer is load-bearing rather than decorative. This edition is
developed in partnership with, and sponsored by, the
[WWOX Foundation](https://www.wwox.org/) ([statement](SPONSORSHIP.md)).

**It measures where AI reasoning fails, on real scientific work.** The failure
taxonomy here was not imagined: it was harvested from actual errors made during
long-running literature synthesis — a mechanism promoted without direct
evidence, a causal direction inverted, a textbook default applied without
checking its preconditions, a result transferred from the wrong variant. Each
became a named guardrail and a candidate benchmark family. That artifact is
useful well beyond WWOX: it is evidence about how AI-assisted science degrades
over months, and what stops it.

**It is inspectable.** The engine ships, the scripts run, the regression suites
are public, the maturity of each claim is stated, and the outstanding gaps are
listed by name. You are not asked to take the compounding claim on faith —
[CAPABILITIES.md](CAPABILITIES.md) tells you where to check it, and where it is
not yet certified.

**What it is not.** Not a clinical decision system, not a treatment pipeline,
not a completeness claim. It does not perform patient-level analysis: this is
the public, disease-level edition, and the individual N-of-1 overlay is excluded
by design. Nothing here is medical advice.

---

**Next:** [README.md](README.md) · [SKILLS.md](SKILLS.md) ·
[CAPABILITIES.md](CAPABILITIES.md) · [ARCHITECTURE.md](ARCHITECTURE.md) ·
[mission.md](disease-models/wwox/mission.md) ·
[operator manual](framework/manuals/operator_manual.md)
