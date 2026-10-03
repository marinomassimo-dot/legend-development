# COMMIT CANDIDATE — CC-20260928-GRAPH-HYGIENE-01 (STUB)

**Candidate ID:** CC-20260928-GRAPH-HYGIENE-01
**Status:** `STUB — SCOPED, NOT PROPOSED` (it carries no `old`/`new` op yet; see § 5 for what turns it into a proposal)
**Base head:** `cf40b73` (`main` at writing; written on `task/mirror002b-repairs`)
**Author:** ACTOR_ID `scientist`, package `mirror002b`, 2026-09-28
**Owner:** ACTOR_ID `scientist` — named, not implied. The claim→claim graph is scientific annotation in the claim registry, so it is a Scientist surface; Harness Engineering owns the *measuring* tool (`pathograph` export, `growth_anchors`), not the edges.
**Trigger (either one, whichever comes first):**
1. **Event trigger** — the next `BATCH_COMMIT` whose scope already opens any of the **eleven** claim records § 3 lists as needing an edit. That batch closes the edges that fall inside its own scope, on this candidate's op list, and records the rest here. Closing an edge inside a record the batch is already editing costs one `replace-within`; the point of the trigger is that nobody opens `CLAIM 028` to add a wikilink and nobody opens it twice.
2. **Date trigger** — **2026-10-05**. On that date the owner either proposes this candidate in full or records, in one line in § 6, why the set decision is deliberately abandoned. 🔴 **A third deferral without one of those two outcomes is a finding against the owner**, because that is precisely what three rounds of deferral already produced.
**Review date:** **2026-10-05** (see § 6, which is the dated line the review writes).
**Declared change class if proposed:** `MINOR` — annotation only. No claim `Status`, `Type`, `Transferability`, `clinical relevance`, BLOCCO 1 field or therapeutic `SCORE`/`SAFETY` value moves; no datum changes; no claim is added or removed. **Adding a back-reference does not narrow or reverse any claim's meaning**, so no locator triples are owed; if the set decision ends up *removing* an edge instead of closing it, that item narrows a claim's cross-reference structure and gets its own triples at proposal time.
**`context_policy`: `QUESTION_DRIVEN`** — declared. Held before any source was opened: `disease-models/wwox/analysis/data/pathograph_export.jsonl` (718 records, read as JSON, never grepped); `disease-models/wwox/registries/claim_registry_current.md` re-partitioned by `## CLAIM nnn` heading and read **by record**, never `cat`-ed wholesale; `disease-models/wwox/analysis/data/dismech_phase2_baseline.json` `inputs.*.scope_blocks`; the Mirror ex-post reviews of `BATCH_20260928_001` (FINDING 11) and `BATCH_20260928_002` (FINDING 8). Question fixed before the measurement: *which claim→claim edges are declared in one direction only, which record must be edited to close each, and what does closing it cost.*

---

## 1 · Why this file exists

**Three consecutive rounds deferred the same decision, each time to "a dedicated candidate", and no
such candidate existed on disk.** The Mirror ex-post review of `BATCH_20260928_002`, FINDING 8 (MINOR),
named that as the defect: *"A deferral whose exit condition is a document nobody has been asked to
write is, by the third round, a way of not deciding."* It also supplied the reason for the deferral
that nobody had written down — § 4 below.

This stub exists so that the deferral now has **a document, an owner, a trigger and a dated review**.
It deliberately does **not** carry the fifteen `old`/`new` ops: writing them is the work the trigger
authorises, and pre-writing them would fix `old` strings against a registry that three other packages
are editing this week. What the stub fixes is the **scope, the cost and the exit condition**, which is
what three rounds of deferral never produced.

**Mirror's own falsifier, checked before FINDING 8 was accepted.** The falsifier was: the finding
dissolves if a graph-hygiene candidate, or a dated owned hand-off for the fifteen edges, already exists
somewhere the reviewer did not look. Re-checked here across the whole of
`disease-models/wwox/research/commit_candidates/` (154 files at `cf40b73`, listed, none named for the graph except
`CC-20260825-GRAPH-MATERIALIZATION-01` — which *materialised* the graph and does not close an edge —
and the three `CROSS-CLAIM-CENSUS` files of 2026-08-26, which count links rather than own them) and
across the `growth_anchors check` backlog (14 items at `cf40b73`, none of them a graph candidate). The
falsifier **holds**; FINDING 8 stands, and this file is its second limb satisfied.

---

## 2 · The measurement, and the two counting rules named

🔴 **State which rule you used.** The two rules give different numbers, and every previous round quoted
a number without naming its rule, which is how *15* and *11* came to look like a disagreement about
facts when they were a disagreement about counting. Both were re-derived here **from the claim registry
itself**, by re-partitioning it on `## CLAIM nnn` and matching the wikilink form `claim_registry_current#CLAIM <n>` (written with double brackets in the registry),
independently of the `pathograph` export — and the any-field figure then reproduced the export's own
`findings.asymmetric_links` list edge for edge.

| counting rule | directed claim→claim references | asymmetric edges |
|---|---|---|
| **ANY DECLARED FIELD** — a reference counts wherever it appears in the record (`Wikilinks`, `Summary`, `Clinical meaning`, `Evidence boundary`, a dated note, …) | **65** | **15** |
| **`Wikilinks` FIELD ONLY** — a reference counts only in the record's `**Wikilinks:**` line | **56** | **10** |

**The rule used for this candidate is ANY DECLARED FIELD, and the working figure is 15.** Reason: the
graph the repository actually publishes is the `pathograph` export, whose `claim_edge` records carry a
`declaring_fields` list and accept any field — six of the fifteen are declared in `Wikilinks`, the
other nine in `Evidence boundary`, `Clinical meaning`, `Summary` and one dated counter-directional
note. A hygiene pass that closed only the `Wikilinks`-declared edges would leave the published graph
asymmetric and would have to be run again.

⚠️ **The earlier pass's `11` is not reproducible under either rule as the registry stands at
`cf40b73`.** Measured today: the `Wikilinks`-only rule gives **10**, not 11. The likely cause is that
the registry has changed since — `CLAIM 030 <-> CLAIM 033` is asymmetric under the `Wikilinks`-only
rule and **symmetric** under any-field, because `CLAIM 030`'s prose now cites `CLAIM 033` while its
`Wikilinks` line does not, and that prose citation was added by the 2026-09-27/28 repair series. The
figure is therefore stamped: **15 (any field) / 10 (`Wikilinks` only), measured at `cf40b73`**, per the
locator-audit rule that a figure travels with its mode.

---

## 3 · The fifteen edges, and which record must be edited to close each

Verbatim from `pathograph_export.jsonl` → the `findings` record → `asymmetric_links`, re-derived
independently from the registry. The record to edit is always the **source of the missing direction**.

| # | edge | declared direction | missing direction | record to edit | declaring field |
|---|---|---|---|---|---|
| 1 | `CLAIM 004 <-> CLAIM 040` | `040 -> 004` | `004 -> 040` | `CLAIM 004` | `Wikilinks` |
| 2 | `CLAIM 005 <-> CLAIM 036` | `036 -> 005` | `005 -> 036` | `CLAIM 005` ⚠️ | `Evidence boundary` |
| 3 | `CLAIM 007 <-> CLAIM 041` | `041 -> 007` | `007 -> 041` | `CLAIM 007` | `Wikilinks` |
| 4 | `CLAIM 009 <-> CLAIM 025` | `025 -> 009` | `009 -> 025` | `CLAIM 009` | `Clinical meaning` |
| 5 | `CLAIM 009 <-> CLAIM 028` | `009 -> 028` | `028 -> 009` | `CLAIM 028` | ⚠️ counter-directional note (`BATCH_20260726_001`) |
| 6 | `CLAIM 011 <-> CLAIM 031` | `011 -> 031` | `031 -> 011` | `CLAIM 031` | `Summary` |
| 7 | `CLAIM 016 <-> CLAIM 033` | `033 -> 016` | `016 -> 033` | **`CLAIM 016` 🔒 SEALED** | `Nota di direzione` |
| 8 | `CLAIM 016 <-> CLAIM 039` | `039 -> 016` | `016 -> 039` | **`CLAIM 016` 🔒 SEALED** | `Evidence boundary` |
| 9 | `CLAIM 017 <-> CLAIM 020` | `017 -> 020` | `020 -> 017` | `CLAIM 020` | `Clinical meaning` |
| 10 | `CLAIM 019 <-> CLAIM 033` | `033 -> 019` | `019 -> 033` | `CLAIM 019` | `Wikilinks` |
| 11 | `CLAIM 028 <-> CLAIM 034` | `034 -> 028` | `028 -> 034` | `CLAIM 028` | `Clinical meaning` |
| 12 | `CLAIM 028 <-> CLAIM 035` | `035 -> 028` | `028 -> 035` | `CLAIM 028` | `Wikilinks` |
| 13 | `CLAIM 030 <-> CLAIM 032` | `030 -> 032` | `032 -> 030` | `CLAIM 032` | `Wikilinks` |
| 14 | `CLAIM 030 <-> CLAIM 035` | `035 -> 030` | `030 -> 035` | `CLAIM 030` | `Clinical meaning` |
| 15 | `CLAIM 031 <-> CLAIM 032` | `032 -> 031` | `031 -> 032` | `CLAIM 031` | `Wikilinks` |

**Eleven distinct records** would be opened: `CLAIM 004 · 005 · 007 · 009 · 016 · 019 · 020 · 028 ·
030 · 031 · 032`. `CLAIM 028` carries **four** of the fifteen and `CLAIM 016` two; the other nine
records carry one each — which is the second argument for one set decision over fifteen incidental
ones.

⚠️ **`CLAIM 005` (row 2) is the epileptogenesis prohibition**, which the repair series has kept
untouched by standing convention. Adding a back-reference to its `Evidence boundary` does not touch the
prohibition, but it does open the record, so that op is proposed **separately and named**, never folded
into a batch's incidental scope.

---

## 4 · The cost nobody had written down (Mirror `BATCH_20260928_002` FINDING 8, measured)

🔴 **Rows 7 and 8 require editing `CLAIM 016`, and `CLAIM 016` is a DisMech-sealed block.** The
DisMech Phase-2 baseline's `inputs.*.scope_blocks` seal `CLAIM 016 / 024 / 035` in the claim registry
and `PAPER 019 / 055 / 056` in the paper registry, under `verification_policy: sealed_scope`. Closing
`016 → 033` and `016 → 039` therefore:

1. **drifts a sealed digest** — the edit is *inside* the sealed scope, which the baseline's own
   `verification_scope` distinguishes explicitly from an edit outside it (*"Editing a registry outside
   that scope is not a violation of this freeze; editing inside it is"*);
2. **obliges `reseal_dismech_baseline.py --absorb`**, not the `--check` a batch normally runs; and
3. **consumes a fresh revision ordinal**, on a `revision` field whose label history three conventions
   already make unreadable (the open `M10` / Mirror `7` item).

That is a real, named cost, and it is the argument for **one** set decision rather than fifteen
incidental ones: thirteen of the fifteen edges are free, two cost an absorb and an ordinal, and paying
that price once for two edges is defensible where paying it twice on two separate incidental batches is
not. It is also why the event trigger in the header says a batch closes only the edges **already inside
its own scope**: a batch that happens to open `CLAIM 016` for other reasons is the cheapest moment
these two will ever have.

---

## 5 · What turns this stub into a proposal

1. **A decision on the counting rule**, recorded — ANY DECLARED FIELD is this stub's working choice
   (§ 2) and the set decision may overrule it, but not silently.
2. **A decision per edge: close, or record as deliberately one-directional.** 🔴 **Not every
   asymmetry is a defect.** Row 5's declared direction lives in a **counter-directional evidence**
   note, and a note that says "this claim's evidence cuts against that one" is not obviously owed a
   symmetric partner; row 7's is a `Nota di direzione` that already declares itself as cutting both
   ways. An honest pass may well close twelve and record three, with the reason inside the record.
3. **Fifteen `old`/`new` op lists**, each `old` measured **unique inside its record** at the base the
   proposal declares, per `prompt_batch_commit.md` § 4.0.
4. **The `CLAIM 016` decision** — absorb and spend an ordinal now, or record those two edges as
   deferred *to the next batch that opens `CLAIM 016` anyway*, which is a deferral with a real exit
   rather than a repetition of the last three.
5. **A re-measurement at the proposal's own base**, because the counts in § 2 and § 3 are stamped at
   `cf40b73` and three packages are editing the claim registry this week.

---

## 6 · Review line — written on the review date, append-only

*(Empty by design. On **2026-10-05** the owner appends one dated line here: either "proposed as
`CC-…-GRAPH-HYGIENE-02`, N edges closed, M recorded one-directional" or "abandoned, because …". An
empty § 6 after 2026-10-05 is the finding.)*

---

## 7 · What this stub does NOT do

- It does **not** touch any of the four scientific current files, `disease_model.md`, any tool, any
  generated surface or any sealed block. It is a research-layer candidate file and nothing else.
- It does **not** close an edge, add a wikilink or re-seal anything.
- It does **not** re-open `BATCH_20260928_002`, its classification or any claim status.
- It does **not** assert that fifteen edges are fifteen defects. § 5 item 2 is the part a reader should
  not skip.

**Not medical advice.**

---

## BATCH DISPOSITION — written 2026-10-03 by `BATCH_20261003_001` (ACTOR_ID `scientist`, Scientist F), append-only

**Verdict:** DEFERRED

🔴 **Not propagated, and still owed.** `batch_20260928_005_scope` names this candidate inside the words *«NOT IN SCOPE and still queued»*, and a mention closes a candidate whatever the sentence around the id says — so the backlog counter read one short while the work was never done. It is a stub with no ops and a dated review trigger. This block exists so the candidate's own record states what that scope's prose meant: **queued, not propagated**, and it is counted as pending again. `BATCH_20261003_001` did not touch its content.


---

## BATCH DISPOSITION — `BATCH_20261003_002` (2026-10-03, ACTOR_ID `scientist`, Scientist G), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** DEFERRED

Still a stub with no op list (its § 5 names what turns it into a proposal) and its own review date is 2026-10-05. Content untouched.

**Not medical advice.**
