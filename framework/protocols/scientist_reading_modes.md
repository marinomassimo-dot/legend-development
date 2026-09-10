---
artifact: LEGEND protocol — SCIENTIST READING MODES · actor identity of Scientist A and B ·
  task ownership of a reading
protocol_id: SCIENTIST_READING_MODES
version: 1
governance_version: 3.1.1
normative: yes
status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC, after
  Mirror hostile review and HUMAN_APPROVAL. Until then it binds nobody.
applies_to: every actor under roles/scientist.md; the actor-identity section names scientist-a
  and scientist-b specifically
materialized_by: plan
materialized_on: 2026-08-18
authority: body §2, §8, §14, §22, §32, §36; Annex A, C, I.2, I.4; roles/scientist.md;
  HANDOFF-SCIENTIST-AB-SPEC (operator scope, transmitted L2-20260818-ORCH-051)
depends_on: framework/protocols/fulltext_read_receipt.md · framework/scripts/deepdive_manifest.py
  · framework/master/gold_is_in_the_details.md · framework/instruction/epistemic_discipline.md
---

# SCIENTIST READING MODES — and the identity of Scientist A and Scientist B

## 0 · What this protocol is, and the one tension it has to hold

Body §32 makes the three Scientists **equivalent**: *same mandate, same protocol, same scientific
authority, same obligations, same isolation, no static specializations.* The operator's scope
for the first controlled benchmark asks for two readers with different missions — a **primary
evidence reader** and an **independent critical reader**. Both are binding, and they are only
compatible if the difference is put in the right place.

**The difference is a property of the task, not of the actor.** This protocol defines two
**READING MODES** that a Task Contract (Annex A.1) assigns to a reading:

```
MODE A · PRIMARY_EVIDENCE_READ        — the reader of what the paper shows
MODE B · INDEPENDENT_CRITICAL_READ    — the reader of what the paper does not show
```

Scientist A and Scientist B remain equivalent under §32 in mandate, authority, obligations and
isolation. **In `BENCH-AB-001` the assignment is fixed — `scientist-a` reads in MODE A,
`scientist-b` reads in MODE B — and that fixing is scoped to that benchmark.** Whether the modes
rotate afterwards is Orchestrator's to decide per task, under Mirror's anti-fossilization guard
(§32: *"guardia anti-fossilizzazione di Mirror"*). A mode that stops rotating has become a static
specialization, and that is the failure Mirror should watch for.

The rest of this file does four things: fixes the identity of `scientist-a` and `scientist-b`
(§1); states when two readers on one paper is intended and when it is a defect (§2); states the
contract common to both modes and the two mode directives (§3–§5); and maps the reading's output
onto the data model this repository already has (§6).

---

## 1 · Actor identity — `scientist-a` and `scientist-b`

### 1.1 · The stable binding

| ACTOR_ID | Worktree | Branch | Contract | Actor class |
|---|---|---|---|---|
| `scientist-a` | `lettore` | `lettore` | `roles/scientist.md` | `PERSISTENT_LEGEND_ACTOR` |
| `scientist-b` | `lettore-b` | `lettore-b` | `roles/scientist.md` | `PERSISTENT_LEGEND_ACTOR` |

`ROLE_CONTRACT_HASH` is **derived, never stored here**: `sha256` of `roles/scientist.md` at the
canonical tip, the way `governance/scripts/governance_fingerprint.py compose --role scientist`
computes it. A value written into this table would be a copy that ages.

**These two ACTOR_IDs are fixed on canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC`.**
`PID-12` held them *proposed — confirmed at registration*; the operator's HUMAN_APPROVAL of that
candidate is the deliberate moment `BOOTSTRAP.md` asks for, and it is taken **before** any
session incarnates either actor, for a reason specific to the benchmark: the input surfaces,
the task contracts and the frozen receipts of `BENCH-AB-001` are prepared and named **per
ACTOR_ID before the sessions open**. An identity that only becomes permanent when a session
shows up would leave every one of those records pointing at a proposal. **`scientist-c` is not
touched by this protocol**: it stays exactly as the operator's step-6 directive left it —
proposed until its own registration completes.

### 1.2 · ACTOR_ID is not SESSION_REF

```
ACTOR_ID      permanent · identity, provenance, learning attribution · survives every chat
SESSION_REF   ephemeral · routing of one runtime incarnation · new after every crash or restart
```

Annex I.4 and body §8, verbatim in substance: *the `from` is routing; the ACTOR_ID is identity.*
Consequences that this protocol makes explicit because they were violated once already:

- **No actor observes its own SESSION_REF.** `ListAgents` shows peers only. A session that needs
  its own reference either derives it by set complement across peer lists (recorded as
  `DERIVED_BY_COMPLEMENT — pending L1 confirmation`) or reads it back from the `from` field of its
  own L1 ping. **It never invents one, and this protocol never asks it to.**
- **A registration record carries both, in separate fields, and only the ACTOR_ID is durable
  identity.** A registry row whose SESSION_REF is stale is a stale row (body §43); the actor it
  names is not thereby unregistered.
- **Nothing in a first-pass output, a task claim, a checkpoint or a frozen receipt is keyed by
  SESSION_REF.** They are keyed by ACTOR_ID + TASK_ID + GENERATION.

### 1.3 · Registration — the canonical path, made concrete for A and B

The path is Annex I.2 step 7 (`BOOTSTRAP.md` step 6): *the actor reads its contract, rehydrates,
and REGISTERS — ACTOR_ID + SESSION_REF + declared capabilities — and the registrar records the
card (I.4).* This protocol adds no second path. It says what the declaration must contain for
these two actors, what the registrar checks, and where the record lives so that it outlives the
chat.

**The actor's declaration** (message type per Annex B, `STATE_CHANGE: yes`, ACK required):

```yaml
REGISTRATION:
  ACTOR_ID:               scientist-a | scientist-b          # fixed value; any other is refused
  ROLE:                   scientist
  ROLE_CONTRACT:          roles/scientist.md
  ROLE_CONTRACT_HASH:     <sha256 recomputed in the actor's own worktree>
  GOVERNANCE_VERSION:     3.1.1
  APPLICABLE_GOVERNANCE_FINGERPRINT: <governance_fingerprint.py compose --role scientist,
                                      run inside the actor's worktree>
  WORKTREE:               lettore | lettore-b
  BRANCH:                 lettore | lettore-b
  WORKTREE_HEAD:          <sha> · <n> behind main · <m> ahead · CLEAN | DIRTY(<paths>)
  SESSION_REF:            <observed via L1 `from`, or DERIVED_BY_COMPLEMENT — never invented>
  SESSION_ID:             <declared>
  CAPABILITIES:           the six of roles/scientist.md, each status: UNVERIFIED
  C2_STATE_ACK:           # both actors — see §1.4
  C2_ORIGIN_STATEMENT:    # scientist-b only — see §1.4
```

**What the registrar verifies** — the same checks the 2026-08-17 registrations passed, none
skipped: bootstrap core present in the worktree; governance 3.1.1 loaded; ROLE_CONTRACT_HASH
equal to canonical; fingerprint recomputed *in situ* equal to canonical; committed history
intact; working tree state as declared. A declaration whose ROLE_CONTRACT_HASH does not match
canonical is a stale worktree, not a different actor: the registrar answers *sync, then
re-declare*.

**Where the record lives — two seats, two writers, one identity:**

| Seat | Writer | What it is |
|---|---|---|
| Agent Card registry (Annex I.4; today `runtime/agent_card_registry.md` on branch `orchestrator`) | the registrar; maintained by Plan (body §43) | the laboratory's roster row for the actor |
| `ledger/registrations/<ACTOR_ID>/REG-<ACTOR_ID>-<nnnn>.json`, on the actor's **own** branch | the actor | the actor's own durable declaration — the record that survives the chat |

The second seat is what makes *"identity survives the end of a chat"* true from the actor's
side and not only from the registrar's: after a crash the new session finds its own last
declaration in its own worktree, with the ACTOR_ID it must re-declare and the SESSION_REF it
must **not** reuse. `ledger/` is a declared control-plane root (P5.1), so this record moves no
candidate hash and no fingerprint. Where the Agent Card registry ultimately lives is the open
C-9 §7.2 question and is **not decided here**.

**What registration does not do.** It verifies no capability (that is L2), assigns no task, and
confers no authority. A registered `scientist-a` with six `UNVERIFIED` capabilities can be
addressed and cannot yet be assigned (body §8: assignment on VERIFIED capabilities).

### 1.4 · The C-2 preconditions are due at registration — and are answered by declaration, not by action

`HANDOFF-C-2-PMID42422765` (branch `orchestrator`, `runtime/handoff/C-2/`) recorded, and Plan
re-verified on 2026-08-18: both worktrees hold one modified file,
`disease-models/wwox/research/deepdive_manifests/PMID42422765.json`, byte-identical
(`sha256 6c3fe60f…`, blob `86bba8bb`, protected by tag `handoff/C-2/PMID42422765-working-blob`),
whose two-line delta is already canonical and superseded in `main`. **Content: CLOSED. Nothing
is to be reset, checked out, deleted or committed by anyone else.** What C-2 deferred *to
registration* is answered there, as two declaration fields:

```
C2_STATE_ACK          both actors     "I observed the modified file; I verified against main
                                       that the -05 receipt is present and superseded by -06;
                                       I will not WORK_COMMIT it; I will sync to main before
                                       any new work."   — or a statement of what contradicts this
C2_ORIGIN_STATEMENT   scientist-b     one sentence on how the identical two-line edit came to
                                       exist in lettore-b: double assignment, copied tree, a
                                       tool that rewrote the field, or "unknown"
```

`"unknown"` is an admissible answer. A missing field is not. The forward-ownership half of C-2
is a task-ownership rule and is answered in §2.4.

---

## 2 · Two readers on one paper — intended, or a defect

### 2.1 · The two cases

```
PARALLEL_INDEPENDENT_READING   intentional. Two or more Task Contracts on the same source, each
                               with its own OWNER, each carrying the SAME PARALLEL_READ_GROUP
                               naming the protocol that declares the parallelism and lists the
                               members. Outputs are kept separate and later compared.
DUPLICATED_ASSIGNMENT          accidental. Two Task Contracts (or one contract and one existing
                               reading) on the same source with no shared PARALLEL_READ_GROUP.
                               Nobody intended two readings; the second is waste at best and a
                               silent merge conflict at worst — C-2 was the small case of this.
```

### 2.2 · The rule

1. **Every reading Task Contract names exactly one `OWNER` (ACTOR_ID) and the source(s) it
   covers** (PMID/DOI). Ownership is explicit; it is never inferred from a worktree, a branch,
   or a file someone happens to have open.
2. **Two contracts on one source are legal only under a declared group:** both carry
   `PARALLEL_READ_GROUP: <PROTOCOL_ID or BENCHMARK_ID>`, and the named protocol lists the
   members and the reason. `BENCH-AB-001` is such a group; its members are exactly `scientist-a`
   and `scientist-b`.

   🔴 **`PARALLEL_READ_GROUP` is an EXTENSION FIELD on the Annex A.1 Task Contract schema,
   introduced here by protocol.** Annex A is not amended and this candidate amends no governance
   text; A.1 declares its minimum fields *extendible, never removable*, which is the clause this
   extension stands on. It is named as an extension so that a reader of A.1 who does not find it
   there knows where it came from and that it was a deliberate act, not drift (Mirror R-4). Any
   promotion of it into Annex A itself is a separate governed change.
3. **The actor checks before it claims** (Annex A.3): before `TASK_CLAIM`, query the receipt
   ledger for the source and the task ledger for open contracts on it. An existing reading or an
   open contract without a shared group → **do not claim**; raise `BLOCKER` to Orchestrator
   with the two records named. This costs one query and prevents the case C-2 recorded.
4. **Plan detects at reconciliation** (A.3 `CLAIM_CONFLICT` shape): over `ledger/tasks/*/`, any
   two open contracts on one source without a shared group → `DUPLICATED_ASSIGNMENT`, recorded,
   routed to Orchestrator. Orchestrator adjudicates: `TASK_CANCEL`, or generation+1, or a
   declared group made after the fact **with the reason written down**. Duplicates are censused,
   never lost in silence.

### 2.3 · Why "detectable" is the honest word

There is no lock (J.0). The rule guarantees uniqueness **by construction of the records**: one
assigner, one owner per contract, a group name that must be present in both records to make two
readings legal. What it guarantees is that a duplication **cannot exist without leaving two
records that contradict each other**, and that both the actor and Plan look at those records at
defined moments. It does not guarantee that nobody ever opens the same PDF twice.

### 2.4 · C-2, forward ownership — resolved as a rule

C-2 escalated *"who owns PMID42422765.json, and by extension PMID 42422765, once the Scientists
are registered?"* and correctly refused to answer without a lease. **This protocol answers the
rule and leaves the assignment where H.1 puts it:**

- Ownership of a source going forward **is the `OWNER` of the Task Contract that names it**.
  Before such a contract exists, no Scientist owns PMID 42422765; the two stale working copies
  are each actor's own to clear (§14, one writer per directory), and the content is held by the
  canon.
- The first contract naming PMID 42422765 **must cite `HANDOFF-C-2-PMID42422765`** and state
  whether it is a single-owner reading or a `PARALLEL_READ_GROUP` member. A contract that omits
  the citation is refusable by the actor under §2.2 rule 3.
- **Who that OWNER is remains Orchestrator's, under an ACTIVE lease** — an assignment, not a
  rule, and not made here.

The duplicated-assignment *root cause* is asked of `scientist-b` at registration (§1.4).

---

## 3 · The contract common to both modes

Everything in this section binds MODE A and MODE B identically. A mode directive (§4, §5) adds
to it and never subtracts from it.

### 3.1 · Inputs

The reader receives **a source packet** — article binary, article text surface, supplements as
listed by the Task Contract or, in a benchmark, by the input manifest — and nothing else about
the paper. Under `BENCH-AB-001` the packet is the allowlisted surface of
`framework/protocols/controlled_benchmark_ab.md` §2 and the reader works **in that surface, not
in its LEGEND worktree**, for the reason that protocol states.

### 3.2 · Reading discipline — nothing here is new, and all of it binds

The scientific method of this repository is not replaced by a mode and is not negotiable by
one (`roles/scientist.md`, *Working discipline*). Named so a reviewer can point at the rule:

- **Parity of sources; what counts as having read something** —
  `framework/master/gold_is_in_the_details.md` rules 1–8, 5b–5e. Grep is not a method of
  analysis. Full text over abstract wherever full text exists. Figures inspected at original
  resolution; a caption is not a panel.
- **Verbatim locators captured while the document is open** — proposition · snippet ·
  surface (`body | figure | table | supplement | abstract`) · artifact · anchor ·
  `panel_text_relation`, exactly the entry the manifest validator accepts
  (`framework/scripts/deepdive_manifest.py`, `verbatim_locators.entries[]`). A `figure` surface
  is an attestation, not a quote, and says so.
- **The receipt contract** — coverage map over Abstract · Introduction · Methods · Results ·
  Figures · Tables · Discussion · Limitations · Supplementary, each `read | captions_only |
  not_present | unavailable | not_read`; a complete read carries no `not_read`
  (`framework/protocols/fulltext_read_receipt.md`).
- **Epistemic typing** — every statement carried out of the reading is `DATO | INFERENZA |
  IPOTESI | ESPANSIONE` (`framework/instruction/epistemic_discipline.md` §1); every rejection or
  non-trivial conclusion names its premise and tags it `PREMISE: DATO | INFERENZA |
  DEFAULT_FROM_TEXTBOOK`; every negative carries a `REVIVAL_TRIGGER`.
- 🔴 **Contradicting a locator that is already persisted is its own act, with its own order of
  operations.** Re-inspect the surface at original resolution **before** drafting the
  contradiction, not after it; then run the blind audit on the contradicted triples
  (`.claude/skills/legend-locator-audit/SKILL.md`, fourth mandatory trigger; Annex C.1). The rule
  is stated in this order because the order is the whole control: on 2026-09-09 a reader working
  from a 667 px rendering **began drafting a correction to a locator that was exactly right**, and
  what stopped it was re-opening the figure at 400 dpi *before* writing rather than after. An edit
  to an existing locator is the highest-confidence act a reader performs — the reader believes
  they are fixing an error — and it is therefore the act least likely to be re-checked.
- 🔴 **An identifier, a count or a residue identity comes from the artefact or from a command run
  in this session** — never from recall, never from the first hit of a search. Where it genuinely
  comes from outside, it carries `external_provenance` naming the command or index and the date.
  The rule is `scientist-a`'s own, adopted verbatim after a wave in which a PMID was taken from a
  search *while the correct identifier sat in the open artefact's `ext-link` markup*, two
  field-density counts were written from expectation, and a false sentence was built on one of
  them: *"an assumption asserted with the confidence of a measurement, in a place too small to
  look at twice."*

### 3.3 · Forbidden — in both modes

| Forbidden | Why it is a rule and not advice |
|---|---|
| Turning a hypothesis into an observation — an author's *"suggests"* into the reader's *"shows"* | it is the exact seam §6.2 exists to keep visible |
| Using general knowledge without declaring it | undeclared background is `DEFAULT_FROM_TEXTBOOK` and *"the most dangerous premises are the ones too obvious to write down"* |
| Inferring from the abstract when the full text is available | `abstract` is a legal surface and a weak one; the validator flags abstract anchoring for a reason |
| Compressing depth or coverage for token, time or cost | a reading shortened for budget produces a receipt that overstates itself; the cost stop condition is J.4's and is declared, not silently absorbed into the reading |
| Modifying the canonical disease model or any `*_current.md` | readings propose; `BATCH_COMMIT` disposes |
| Reading the other reader's output, or any prior LEGEND output on the paper, during a first pass declared blind | blindness is a property of the surface (benchmark protocol §4), and stepping outside the surface is the one act that defeats it |
| Contacting the other reader during the first pass, or asking Orchestrator to relay content | the same, by another channel |
| Correcting a persisted locator without re-inspecting the surface at original resolution first, or without the blind audit on the contradicted triples | the sweep of 2026-09-09 produced three such contradictions and audited one; the unaudited near-miss would have been *"confident, well-argued, and would have passed every gate this repository owns"* |
| Reporting a screen's verdict without stating what it screened | a screen that returns CLEAN on an unscreened input is worse than no screen, and this repository has now shipped one: `_refuse_suspect_surface` called with inverted arguments screened a *filename* and returned green over a surface carrying 191 C0 controls |

### 3.4 · Permitted inference, and where it stops

The reader may state `INFERENZA` and `IPOTESI` — that is what *claim candidates* and *mechanistic
implications* are — and must type them as such. It may not: present an `INFERENZA` as `DATO`;
present an `ESPANSIONE` as `INFERENZA`; convert an author interpretation into a LEGEND
observation; or leave a load-bearing premise untagged. **Unresolved ambiguity is a legitimate
output** and is recorded as such, not resolved by choosing the more interesting reading.

### 3.5 · Outputs — the three surfaces, and nothing parallel to them (see §6)

```
READING PROVENANCE   a work manifest, schema_version 2, valid under deepdive_manifest.py
LOCATOR FIDELITY     a dossier in the fulltext_dossiers/*.md form — artifact table with digests,
                     verbatim locators, section by section
CLAIM ASSERTION      claim candidates in the claim_registry_current.md section form
                     (## CLAIM <id> + the twelve canonical fields), plus the seven
                     BENCHMARK / INTERMEDIATE fields of §6.2 and the Locators
                     cross-reference — NOT written to the registry
```

MODE B produces, in addition, a **critical-reading record** (§5.3) whose entries point back at
claim candidates or locators; it is a fourth *file*, not a fourth *data model*.

### 3.6 · Completion criteria

A reading is complete when, and only when: the coverage map contains no `not_read`; every claim
candidate has at least one locator that resolves against the packet by digest; the manifest
validates (`--verify-artifacts --require-current-schema`); every carried statement is typed;
every negative or rejection carries premise tag and revival trigger; unresolved ambiguities are
listed rather than absent; and — MODE B — every mandatory critical axis of §5.2 has either
findings or an explicit *"searched, none found"* with what was searched.

### 3.7 · Handoff schema

`TASK_COMPLETE` (Annex B) with `DURABLE_POINTER` to the output tree, its tree digest, the
manifest validator's verdict line, and the coverage map. Under a benchmark, completion is
declared to Plan for **freezing** before anyone else reads it (benchmark protocol §7).

### 3.8 · Acceptance test — what a reviewer runs, in this order

```
1. deepdive_manifest.py --workspace <output root> --pmid <PMID> --verify-artifacts \
     --require-current-schema                                → PASS
2. every locator's `artifact` is inside the declared packet and its digest matches
3. coverage map: no not_read
4. per claim candidate: the twelve canonical fields present; the SEVEN benchmark fields of
   §6.2 present, plus `Locators:` — eight labels, the same eight the output schema requires,
   so the acceptance test and the schema cannot disagree about what a complete claim is;
   Type ∈ {DATO, INFERENZA, IPOTESI, ESPANSIONE} (compound allowed, as the registry does)
5. blind locator audit (`.claude/skills/legend-locator-audit`) over the (proposition, snippet,
   anchor) triples — auditor receives triples + packet, never the dossier or the reader's name
```

Steps 1–4 are mechanical. Step 5 is the one that catches a careful reading that says more than
its source.

---

## 4 · MODE A — `PRIMARY_EVIDENCE_READ`

**Mission: the primary evidence reader.** Produce the primary scientific reading of the paper —
what it did, what it found, in what system, with what strength — so that a claim candidate can
be built on it and a second reader can attack it.

The reading must reach, for every experimental finding it carries: full-text basis; the
experimental finding itself; the methods that produced it; population / model / context;
genotype; cell type; developmental stage; intervention; endpoint; **directionality**;
**negative and null findings**, with the same care as positive ones; the figures and tables that
bear on it, inspected; caveats stated by the authors; locator; provenance (which artifact, which
digest); epistemic typing; uncertainty; limitations; the claim candidate(s) it supports;
mechanistic implications, typed as `INFERENZA` or `IPOTESI`; and every unresolved ambiguity.

MODE A is not "read charitably." It is "read completely, and say what is there, at the level at
which it is there." An author interpretation reported by MODE A is reported *as* an author
interpretation (§6.2 `AUTHOR_INTERPRETATION`), which is exactly what lets MODE B do its job.

---

## 5 · MODE B — `INDEPENDENT_CRITICAL_READ`

### 5.1 · Mission

**The independent critical scientific reader.** MODE B shares MODE A's core in full — the same
completeness, the same outputs, the same discipline — and **in addition searches explicitly**, on
the axes below, for what the paper does not establish. It is a reader, not a reviewer of A: it
never sees A's output during a blind first pass, it does not adjudicate A, and it is not asked
to agree with A.

### 5.2 · The mandatory critical axes

Each axis is searched and reported — with findings, or with *"searched; none found"* plus what
was searched. Silence on an axis is incompleteness, not a null result.

| Axis | What MODE B looks for |
|---|---|
| `CONTRADICTORY_EVIDENCE` | results inside the paper that pull against its own conclusions; panels that qualify or contradict the running text (`panel_qualifies_text`, `text_contradicted_by_panel` — the manifest already has the vocabulary) |
| `NEGATIVE_EVIDENCE` | null results, absent comparisons, "not significant" left unquantified, controls that did not behave |
| `OVERCLAIM` | conclusion strength exceeding the evidence — sample size, effect size, one system generalized |
| `UNSUPPORTED_INFERENCE` | a mechanistic step asserted and never measured (`MECHANISM_DIRECTNESS_GATE`, `framework/eval/failure_taxonomy.md`) |
| `MODEL_DEPENDENCE` | conclusions that hold in the model used and are stated as if general; species, cell type, stage, dosage |
| `RESULT_VS_INTERPRETATION` | where the text moves from *observed* to *concluded* without saying so — the seam of §6.2 |
| `METHODS_STATISTICS` | test choice, multiplicity, n per group vs n reported, blinding, replicates, unmarked panels |
| `ALTERNATIVE_EXPLANATION` | an account of the same data the authors did not exclude |
| `CONTEXT_COLLAPSE` | a finding in one context (genotype, tissue, stage, intervention) carried into another |
| `OMISSION` | what a primary reading is likely to carry silently — the thing MODE B would expect to see and does not |
| `UNSUPPORTED_MECHANISTIC_LEAP` | pathway language attached to a phenotype without the intermediate (`TARGET_ATTRIBUTION_GATE`, `DEGRADATION_DIRECTION_GATE`) |

### 5.3 · The critical-reading record

One entry per finding: `axis · target (claim candidate id or locator index) · statement ·
locator(s) · what would resolve it`. Entries are typed like everything else — a critical finding
can itself be an `INFERENZA` — and each is anchored, so that it can be audited by the same blind
locator audit as a positive claim.

### 5.4 · 🔴 MODE B is not Mirror

| | MODE B | Mirror |
|---|---|---|
| Object | the **paper** — its evidence and its inferences | the **process** — how the laboratory reasoned, reviewed and recorded |
| Authority | a Scientist's: *what the evidence supports*, subject to review, never to order (§2) | epistemic / method review; MAJOR classification when in doubt (H.1) |
| Sees A? | **no**, during a blind first pass | yes, both, after freezing — as adjudicator of the process |
| Output | a reading with a critical record | a review under Annex C.2; an adjudication of the benchmark's *method* |
| Replaces? | nothing — a second reader is a second reader | nothing — Mirror is not made redundant by a critical reader |

Mirror remains reviewer and adjudicator **of the process** of any benchmark this protocol is
used in. A second reader does not review the first; a peer review, if one is opened, is opened
by Orchestrator under Annex C.3 and is a separate act.

---

## 6 · One data model, three surfaces, seven benchmark fields — no parallel schema

### 6.1 · Verified, not assumed — 2026-08-18

| Surface | Artifact family | Verified shape |
|---|---|---|
| READING PROVENANCE | `disease-models/wwox/research/deepdive_manifests/*.json` | `schema_version 2`; top level `pmid · doi · receipt · landing · skills_considered · group_assessment · field_density · multihop · corpus_crossquery · retraction_check · source_artifacts[] · verbatim_locators{entries[]}`; entries carry `proposition · snippet · surface · artifact · anchor · panel_text_relation · found_or_sought` (+ `contradicts`/`qualifies` pointers) — **no per-claim array** |
| LOCATOR FIDELITY | `disease-models/wwox/research/fulltext_dossiers/*.md` | artifact table with SHA-256; verbatim quotes with surface and anchor; section by section |
| CLAIM ASSERTION | `disease-models/wwox/registries/claim_registry_current.md` | `## CLAIM NNN` sections (39 counted; 43 `## ` total; 0 `### CLAIM`) with **Title · Status · Type · Pathway · Genotype/model relevance · Transferability · clinical relevance · Summary · Clinical meaning · Source · Wikilinks · Impact on Working Model** |

`AUTHOR_INTERPRETATION`, `LEGEND_INTERPRETATION`, `OBSERVATION`, `DIRECTION` as **field names**:
`0` occurrences in tracked state (`git grep`). As **practice**: present in prose — `CLAIM 001`'s
`Clinical meaning` carries a *Nota epistemica* separating observation from conclusion;
`Type: DATO (osservazione clinica) + INFERENZA (degli autori)` puts the seam inside the `Type`
value; `CLAIM 009` and `CLAIM 034` carry *"counter-directional evidence"* as labelled prose.
**Absent from the schema, present in the practice** — which is what makes promoting them safe.

### 6.2 · The operator's sixteen, mapped — canonical home first, extension only where none exists

| Operator name | Canonical home | Kind |
|---|---|---|
| `CLAIM_ID` | the `## CLAIM <id>` heading | structural field |
| `SOURCE_ID` | `Source` + `Wikilinks` (→ `paper_registry_current#PAPER nnn`) | structural field |
| `SOURCE_TYPE` | `paper_registry_current.md` → `Source type` | structural field (paper registry) |
| `EXACT_CONTEXT`, `MODEL/POPULATION` | `Genotype/model relevance` (+ `Transferability` T1–T3) | structural field |
| `EPISTEMIC_TYPE` | `Type` ∈ DATO · INFERENZA · IPOTESI · ESPANSIONE, compound allowed | structural field |
| `LOCATOR` | dossier quotes + manifest `verbatim_locators.entries[]` | the other two surfaces |
| `PROVENANCE` | manifest `receipt` · `source_artifacts[]` (path + sha256 + kind) · `Wikilinks` | the other two surfaces |
| `MECHANISTIC_RELEVANCE` | `Pathway` + `Impact on Working Model` | structural field |
| **`UNCERTAINTY`** | **none as a label** — `Status` carries a lifecycle value, not this | **BENCHMARK / INTERMEDIATE field** |
| **`LIMITATIONS`** | **none as a label** — prose inside `Summary` / `Clinical meaning`, unlabelled | **BENCHMARK / INTERMEDIATE field** |
| **`CONTRADICTORY_EVIDENCE`** | **none as a label** — one claim carries *⚠️ Counter-directional evidence*; `Status: conflicting evidence` is cross-paper lifecycle, not intra-paper contradiction | **BENCHMARK / INTERMEDIATE field** |
| **`OBSERVATION`** | **none** | **BENCHMARK / INTERMEDIATE field** |
| **`AUTHOR_INTERPRETATION`** | **none** | **BENCHMARK / INTERMEDIATE field** |
| **`LEGEND_INTERPRETATION`** | **none** — today blended into `Summary` | **BENCHMARK / INTERMEDIATE field** |
| **`DIRECTION`** | **none** — prose only (*up-regolata*, *counter-directional*) | **BENCHMARK / INTERMEDIATE field** |

### 6.3 · Why the last three moved — revision 2, Mirror finding B-5

Revision 1 refused to promote `UNCERTAINTY`, `LIMITATIONS` and `CONTRADICTORY_EVIDENCE` on the
stated ground that *"the registry already carries them as labelled prose under stable labels"*.
**That premise fails measurement.** Counted over the 39 `## CLAIM` sections of
`claim_registry_current.md` at `BASE_HEAD cbce3016`, and re-counted independently after the
finding was raised:

```
the twelve canonical bold labels          39/39   (Wikilinks 38/39)
**Uncertainty:**   as a label              0/39
**Limitations:**   as a label              0/39
**Contradictory evidence:** as a label     0/39
**Evidence boundary:**                     5/39  + 3 suffixed variants  = 8 claims
**⚠️ Counter-directional evidence …:**      1/39
Status: conflicting evidence                     cross-paper lifecycle value, not this concept
```

There is no stable label to defer to. An evaluator could not locate any of the three across
claims without reading prose, which is precisely the comparison the benchmark has to make. So
the refusal rested on something that is not the case, and the classification is corrected:
**seven benchmark fields, not four.**

Two things this does *not* change, and they are the load-bearing half. The refusal of a
**parallel claim schema** stands and was right. And nothing here is added to
`claim_registry_current.md`: the three move from *"already canonical, do not duplicate"* to
*"benchmark-only, like the other four"* — a move **within** the benchmark field set, not a step
toward the canonical registry. Whether any of the seven is later promoted remains a separate
governed decision after the benchmark outcome exists.

**The seven benchmark fields are written by both modes, per claim candidate, in a fixed block
after the twelve canonical fields:**

```
**Observation:**            what was measured, in what, with what result — no verb of conclusion
**Author interpretation:**  what the authors conclude from it, in their terms, marked as theirs
**LEGEND interpretation:**  what the reader concludes, typed (INFERENZA / IPOTESI), or "none"
**Direction:**              increase | decrease | no change | not tested | mixed  — of the endpoint
                            under the intervention/genotype named in the observation
**Uncertainty:**            what is not settled, and by what
**Limitations:**            authors' limitations and the reader's, distinguished
**Contradictory evidence:** inside this paper, or "none found — searched: <what>"
```

A block of eight labels appears in the output schema: these seven, plus **`Locators:`**, which
is a cross-reference to manifest entry indices rather than a claim concept. It is counted
separately for that reason, and it is required exactly as the seven are.

The first four exist because *the one thing a second reader must be able to attack is the seam
between what was observed and what was concluded, and today that seam is inside a paragraph.*
The last three exist because the labels they were deferred to do not exist. All seven are
**benchmark fields**: written in benchmark outputs, evaluated in the comparison, and **not added
to `claim_registry_current.md`** by this protocol.

### 6.3 · What is explicitly not created

No `claims.json`, no `claim_schema.yaml`, no `benchmark_claim_registry.md`, no parallel enum for
`Type`, no second locator format. A reader who finds one of these in a benchmark output has
found a protocol violation.

---

## 7 · What this protocol does not do

It does not register anyone — actors register (I.2 step 7). It does not verify a capability
(L2). It does not assign a task (H.1, Orchestrator under lease). It does not fix `scientist-c`'s
ACTOR_ID. It does not open a peer review, promote a claim, touch a `*_current.md`, or decide the
home of the Agent Card registry (C-9 §7.2). It does not modify body §32 — it interprets it: the
modes are per task, and the anti-fossilization guard is Mirror's.
