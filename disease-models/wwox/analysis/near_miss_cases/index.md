# Near-miss cases — the 2026-09-09 Aqeilan sweep

**Analyst:** `analyst-nearmiss` · **Date:** 2026-09-09
**Primary source:** [`../orchestration_reviews/2026-09-09_actor_retrospective.md`](../orchestration_reviews/2026-09-09_actor_retrospective.md)
(commit `bc1b20a`), § 5.2 · corroborated per case against the manifests, receipts, task contracts,
session evaluations and commit bodies each file names.

These are the **six near-errors that were one step from landing** in an eleven-wave, 23-PMID sweep
across three actors. They are the sub-census that inverts the aggregate: of 57 censused incidents the
machines caught 24, but on these six the split was **self 3 · blind auditor 2 · peer 1 · machine
ZERO**.

> **These are records about work, not about actors.** Each case describes a defect that a competent
> reader nearly shipped, and in five of six the reader is also the person who wrote it down. They are
> written to be usable as training material and to be built against; nothing here is a performance
> assessment.

---

## The six

| # | One line | Actor | Caught by |
|---|---|---|---|
| [NM-01](2026-09-09_NM-01.md) | A false correction was drafted against a **correct** persisted figure locator, because Figure 6A of PMID 29724996 was read at the 667 px PMC rendering where its bars are unresolvable; at 400 dpi they stack by genotype and the existing 11/12-vs-4/18 locator is exactly right | `scientist-b` | **self** — a procedural rule applied *before* contradicting, not after |
| [NM-02](2026-09-09_NM-02.md) | The rule-5c suspect-surface screen was called with **inverted arguments**, silently screened the filename and returned CLEAN; the PMID 16223882 PDF text layer it was asked about carries 191 C0 controls and zero comparators, and twelve text locators were about to be anchored to it | `scientist-c` | **self** — refusing to believe a green result, on a separate character census |
| [NM-03](2026-09-09_NM-03.md) | A committed cross-panel bridge claimed Supporting Fig 6 of PMID 15070730 supplies the dose-to-expression step Fig 5 asserts; **it fails on cell line** (NIH 3T3 vs SAOS-2), a fact in a sentence the reader had captured as a locator two hours earlier | `scientist-a` | **blind auditor** — 7 of 13 triples corrected, then re-derived from the body by the reader |
| [NM-04](2026-09-09_NM-04.md) | Reference 1 of PMID 31428585 was given as `29581896`, taken from an external author search, **while the deposit's own `ext-link` markup carried 29310447** — a different paper; the wrong value reached an append-only receipt and the multi-hop debt | `scientist-a` | **both blind auditors**, independently |
| [NM-05](2026-09-09_NM-05.md) | A `REFUSED` verdict was nearly accepted without asking what it refused *for*: it fired on 8 front-matter separators and on suspicion-by-absence, while the signature set matched the actual genotype corruption (`Wwox+/−` → `Wwox?/-`) **with nothing** | `scientist-b` | **peer** — the coordinator's mid-task instruction to finish the determination |
| [NM-06](2026-09-09_NM-06.md) | A mid-wave regeneration of the four shared derived surfaces **baked in two peers' uncommitted manifests**; committing it would have published three actors' in-flight state under one actor's name | `scientist-c` | **self** — inspected the output, then reverted |

---

## They are three failure classes, not six

The brief asked whether the six collapse. They do, and further than expected. **Six cases, three
classes.**

### Class 1 · A verdict accepted without establishing what it could assert — NM-01, NM-02, NM-05

Three of the six. An instrument or a screen returned a result, and the reader acted on it without
asking what that result was capable of asserting.

- **NM-02** is the green form: the screen asserted nothing (it examined a filename) and was reported as
  though it had.
- **NM-05** is the red form: the screen asserted something true and irrelevant, and was accepted as
  though it had covered the load-bearing defect.
- **NM-01** is the same shape one level down, on a *measuring* instrument rather than a screening one:
  a 667 px raster returned a bar reading, and the reading was acted on without asking whether that
  rendering could resolve stacked segments at all.

The two actors' own formulations are the class definition, and neither is "be careful":
*"my check asserted nothing and I reported it as though it had"* and *"'the gate said no' is not a
finding; 'the gate said no because X' is."*

**NM-01 carries a second, orthogonal property that its class does not explain and that drives its
verification: it targeted persisted, correct work.** That is what made it near-catastrophic rather
than merely wrong, and it is why the retrospective's § 9.1 cuts NM-01 out as its own class. On a
four-class reading — *unexamined verdict* / *reversal of persisted work* / *unre-derived fact* /
*shared-surface write* — that cut is defensible. The three-class reading is the better teaching frame
because it groups by **what went wrong**; the four-class reading is the better building frame because
it groups by **what a check would have to watch**. Both are stated here rather than one being asserted.

### Class 2 · A fact asserted from expectation while the artefact that settles it was open — NM-03, NM-04

Two of the six, both `scientist-a` wave 3 and wave 4, and the actor supplied the class name itself:
**"an assumption asserted with the confidence of a measurement, in a place too small to look at
twice."**

In NM-03 the cell line was in the body text the reader had already quoted. In NM-04 the identifier was
in the markup of the file the validator itself had parsed. In both, the correct value was **inside the
declared artefact at the moment the wrong one was written**. This is the class that blind auditors are
good at and machines are not, because catching it requires reading the source, not the record.

### Class 3 · A write whose blast radius exceeded the writer's own work — NM-06

One of the six, and unlike the other five its failure mode is **attribution, not truth**. Every input
was a genuine, well-formed manifest; what was wrong was who was asserting it, and when. It is the only
case whose determining fact — *whose uncommitted file is this?* — no artefact records and `git` cannot
answer.

---

## Attributions verified, and one correction to the brief

Each attribution was checked against the artefact rather than inherited.

- **The 667 px near-error is confirmed as the brief states it**: `scientist-b`, wave 1, PMID 29724996
  Figure 6A, caught by the reader's own rule and by no machine. The primary record is
  `learning/scientist-b/SLR-scientist-b-0002.md`, which sits outside `session_evaluations/`; the
  corrected arithmetic is now visible in `PMID29724996.json` `entries[21]` itself.
- **NM-06's attribution is split, and the brief's single-actor framing needs one adjustment.** The
  near-error and the revert are `scientist-c`'s. The **standing policy** that followed — regenerate
  derived surfaces only at wave close on a clean tree, because the generators read the working tree
  rather than the index — is `scientist-b`'s, established in its wave 4/5 and honoured unbroken by the
  other two; by wave 4 it was a dispatch constraint in all three task contracts. Both credits belong in
  the record and they are not the same credit.
- **NM-06's sole primary record is the orchestrator's commit body at `a8a6a1d`.** No self-evaluation
  and no task contract records the original regeneration or the revert — `scientist-c` wave 2 was
  terminated by a rate limit and produced no evaluation. The case file says so; a reader should know
  this one rests on one artefact where the other five rest on several.
- **NM-04's correction was made lawfully and the mechanism is worth citing on its own**: the wrong PMID
  was in an append-only ledger and was fixed by a linked `receipt_correction`
  (`FTR-20260909-31428585-02`), never by editing the JSONL.
- **NM-03 is the only one of the six that actually landed** before being withdrawn, and its withdrawal
  is preserved in place in the manifest rather than deleted.

---

## Which verifications are worth building

Ranked by value per unit of work, and stated as a judgement rather than a list of possibilities. Where
the honest answer is "a human rule, not a machine", the case file says so.

| Rank | Check | Covers | Why |
|---|---|---|---|
| **1** | **A uniform verdict contract for every screen**: a verdict is a record carrying `screened: {digest, bytes}` and, on a refusal, **which signature fired**; a verdict over empty or non-artefact input is an error, never a pass | **NM-02, NM-05** | The only proposal covering two of the six. No document-content heuristic, so effectively no false-positive surface. Baseline measured: **0 of 7** screens report what they screened, **1 of 7** refuses an uninformative pass. One seventh is already shipped and mutation-tested (`test_suspect_surface_call_shape.py`, 9/9) |
| **2** | **Wire `locator_identifier_provenance.py` in as a WARN with a required declaration** — an identifier asserted in a proposition must occur in a declared artefact or carry an explicit `external_provenance` naming the command and date | **NM-04** | Already built, by the actor whose defect motivated it. Asserts the weak checkable property (*could the reading have got this value from what it declares it read?*), never correctness. Baseline measured: 80 manifests, 15 undeclared external — a review queue, **not** 15 errors, which is why it must not block |
| **3** | **A dirty-tree guard on the derived-surface generators** — refuse to run when `git status --porcelain` reports paths outside the invoking actor's declared scope, and name them | **NM-06** | Tens of lines. Near-exact fit to the defect. The scope argument the commit wrapper already takes removes the one real false positive. Converts eleven waves of standing attention into one `git` call |
| **4** | **Declare the fidelity a figure reading was taken at** — a figure locator asserting a count or ratio declares the pixel dimensions it was read at; the validator compares them against the artefact | **NM-01** | Cheap, and it makes the 667-px fact *exist in the record*, where today 667 px and 400 dpi are indistinguishable once the digest matches. It asserts the declaration is not fiction, never that the resolution was sufficient — no machine can know that |
| **5** | **Flag a locator that reverses a persisted one** — as a **git-diff** on committed manifests, extending `manifest_flag_drift.py`, plus a blind audit **scoped to the changed triples** | NM-01 (severity limb) | Buildable in its declaration limb. **Do not build it as a prose grep**: `PMID15070730.json` alone carries several entries that correctly narrate audit corrections in exactly that vocabulary, and `manifest_flag_drift.py` already records that two note-detecting designs both passed the case they existed to catch |
| **—** | **Not worth building: a cell-line / model-system comparability checker** | NM-03 | Large NL machinery, per-paper calibration, and wrong in the direction that matters — a confident verdict about experimental comparability. The blind audit caught this in one pass. The proportional response is to **widen the R4 trigger** so a reading that contradicts a persisted locator is audited blind whatever the claim status, and to keep blind audits expensive |

**The human rules the six leave standing, none of which should be dressed as a check:**

- Inspect a figure at original resolution **before** contradicting an existing locator. No check can
  enforce the ordering of two acts inside one session; the checks above can only make the ordering
  visible afterwards.
- Before a locator carries an identifier, a count or a residue identity, the value must come from the
  artefact or from a command run in this session — never from recall, never from the first hit of a
  search. (Only the identifier limb has a machine form.)
- Treat unfamiliar in-flight state as read-only until proven otherwise, and write a `not_mine`
  inventory into the task contract.
- "The gate said no" is not a finding; "the gate said no because X" is. NM-05 shows a reader carrying
  this rule in its own words from one wave earlier and still needing a second party to make it operate
  — which is the strongest single argument in the record for keeping blind audits and mid-task
  coordination expensive rather than replacing them with gates.

**The number to watch**, and it is already measurable: **high-severity incidents self-caught / total.
This sweep: 3 of 6.** A rising ratio means reader practice is improving; a falling one means the gates
are carrying more of the load than the readers are.

---

*Disease-level, derived from public literature. Nothing here is medical advice. This is the public
edition and contains no individual-level record: where a private edition would reason about one
person, this reasons about the reference genotype, a WWOX-DEE genotype class.*
