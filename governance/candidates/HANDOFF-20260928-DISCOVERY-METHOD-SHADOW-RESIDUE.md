# HANDOFF → HARNESS ENGINEERING (`plan`) — unshipped content in `LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md`

**From:** ACTOR_ID `scientist`, task `vps-residue-salvage`, 2026-09-28.
**Why a hand-off and not an implementation:** every target is `framework/instruction/` or
`.claude/skills/`, which is Harness Engineering's surface. Nothing below is applied.
**Status:** 🔴 **FINDINGS ONLY. Not a gate, not a precondition, nothing waits on it.**

---

## 0 · What was compared, and the census claim it tests

The residue census of 2026-09-28 flagged
`framework/instruction/LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md` — present on
`origin/claude/q230p-molecular-state-systemic-yruqvc`, absent from `main`, never merged — as
**"probably superseded"** by the shipped `legend-discovery-method` skill, and explicitly recorded
that judgement as needing *"a reader, not a count"* (census §5 limit 4).

**Read. Verdict: mostly superseded, and four things are not.** The shipped skill
(`.claude/skills/legend-discovery-method/SKILL.md`, 460 lines) covers the seven primitives, the
outcome-change observability vocabulary, KEEP / REFINE / DROP with per-primitive discard criteria,
the resolution of `adversarial_verify` into a pointer to `legend-locator-audit`, and the honest
statement that most primitives have never been observed to fail. **The shadow-mode file's §1, §3,
§6 and §7 are genuinely superseded and should not be resurrected** — a trace format with a required
line is closer to the form §26 forbids than anything the skill ships.

The file itself should **not** be landed. It is a 2026-09-22 instruction-layer draft for a method
that shipped as an optional skill, and landing it would put a second, non-normative address on a
subject that already has one. The four items below are what is worth extracting from it.

---

## 1 · 🔴 A live, verified one-line defect on `main` — the §26 misattribution

**Measured 2026-09-28, not taken from the shadow file:**

- `framework/instruction/LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md:29` reads
  *"`LEGEND_CORE` **§26** forbids answering a scientific mistake with a new gate, authority,
  auditor, registry or workflow."*
- `framework/instruction/LEGEND_CORE.md` **has no §26.** It ends at `## 22. FINAL MAXIMS`;
  `grep -cE '^## 2[3-9]\.'` returns **0**.
- The rule is the **operator's task directive** §26 — which is how every commit candidate in the
  repository cites it (*"per the operator's §26"*), and which
  `governance/candidates/CAND-20260819-ORCHSURF.md:444` had already disambiguated in writing
  (*"directive §26, not body §26"*).

**So a live instruction-layer file misattributes, to a section that does not exist, the one
constraint it calls *"the one design constraint that outranks everything below."*** The shadow file
caught this on 2026-09-22 and says it was *"corrected in the proposal in the same act as this
file"* — that correction never reached `main`, because the branch never merged. It is still wrong
today.

⚠️ **Nothing about the constraint changes; only its address does.** The proposal's lines 282 and 372
cite a bare *"§26"* and need no change.

**Cost:** one line. **Verdict proposed: ADOPT.**

---

## 2 · The two best-evidenced primitives in the repository are in neither the directive's list nor the skill

The shadow file's §2 reconciles the directive's seven candidates against the scorecard's eight and
finds they are **not the same list**. Re-checked against the shipped skill by string search —
**zero occurrences of all three of these names**:

| Absent from the skill | What the scorecard recorded for it |
|---|---|
| `verify_the_omitted_clause` | **6 instances — the strongest row on the scorecard** |
| `gate_is_not_quantity` | **5 instances across 4 domains** |
| `outcome_distribution_width` | 1 instance + **1 recorded failure** (the only primitive with a failure on record) |

Meanwhile two of the directive's seven — `compress_experiment` and `adversarial_verify` — entered
with **zero recorded instances**, and the skill ships both.

🔴 **So V0 shipped the primitives an author remembered proposing, and left out the two with the most
recorded outcome-changing instances.** The shadow file names this as *"a finding about how candidate
lists get written"*, and it is the substantive unshipped item here — not a missing feature but a
selection defect in how the shipped set was chosen.

**What to do with it is Harness Engineering's call, and the options are not equivalent:** adding
three primitives to a toolkit whose own success criterion is that it stays small has a cost the
scorecard does not measure. **Proposed verdict: TRIAL on `verify_the_omitted_clause` alone** (the
strongest row, and the one with a clean split — see item 3), **WATCH on the other two.**

---

## 3 · `verify_the_omitted_clause` must be counted as two mechanisms, and its real count is 2, not 6

The shadow file's §4.2, unshipped and not reproduced anywhere on `main`:

| | mechanism | what it would justify |
|---|---|---|
| **A** | **SOURCE OMISSION** — a limiting clause exists in the source and was not propagated | a native scientific-reading primitive |
| **B** | **HAND-BACK COMPRESSION** — the delegate found it and omitted it from the summary | agent communication / harness design, **not** a reading primitive |

Of the six recorded instances: **two are cleanly source-side**, three are corrections to delegate
reports, and one is a third class the file records as source-side-equivalent (the omitted clause was
in *our own* evidence chain — a page adjudication that restored `±`, `<`, `⁺`, `⁻` on a table row and
never named the row's **unit**, while the needle used to find the row was made of the character in
doubt).

⚠️ **The headline count of 6 is therefore not the number that supports adoption; the number is 2 or
3.** Counting A and B together measures how much a hand-back compresses and calls it a property of
the literature.

🟢 **Independent corroboration, found today and not available in 2026-09-22.** That third-class
instance is not hypothetical and it is not closed: this same task verified first-hand that
`page_adjudications/PMID17803050/adjudications.json` resolves the two Table 2 rows with the needles
`"BUN (mg/ml)"` and `"GLU (mg/ml)"` — **strings drawn from a layer this repository classifies
`SUSPECT` and matched against that same layer** — and that the render's *"the page prints"* column
names **no unit on either row**. The consequence propagated into canon as an assertion that the
source's unit header is *"sbagliata alla fonte"*, and is retracted by
`research/commit_candidates/CC-20260922-CLAIM038-UNIT-CLASS-02.md`, landed today. **So mechanism A
has a live, canon-reaching instance with a dated repair — which is a stronger evidence base than the
scorecard's row.**

**Proposed verdict: ADOPT the A/B split as a counting rule if the primitive is trialled at all.**
Cost: it is a definition, not code.

---

## 4 · Two smaller items, both partially shipped

**(a) `outcome_distribution_width`'s repair.** The shadow file's §4.1 revises the rule to
`score = OUTCOME WIDTH × HYPOTHESIS DISCRIMINATION`, adding *"check that any arm you add perturbs
ONLY the variable in question"* — the clause whose absence caused the original failure (a withdrawn
26–30 °C arm that moved synthesis, degradation and the chaperone complement at once). The skill
ships the **instance** (fixture E, line 423: *"an arm withdrawn because outcome width did not
guarantee hypothesis discrimination"*) but **not the formula and not the one-variable clause**. The
shadow file's own caveat should travel with it: *"repairs of broken rules are exactly the kind that
look right and are not."* **Proposed verdict: WATCH.**

**(b) The missing negative control.** The shadow file's §5 closes with an instrument that does not
exist: *"Every row's failure column would fill fastest by running a primitive **deliberately on a
case where it should not help** and recording that it did not. No such run has been made."* The
skill ships the **diagnosis** (§4: *"Most of these have never been observed to fail. That is not
evidence they are sound — it is evidence that too few cases have been built that could break
them."*) but not the proposal. 🔴 **Until such a run exists, a `KEEP` verdict on any primitive is a
statement about a sample with no negative controls in it.** `legend-research-loop` already exists and
is the natural instrument. **Proposed verdict: TRIAL — one deliberate negative-control run, one
primitive, recorded wherever it lands.**

**Also unshipped, and noted without a verdict:** the shadow file's KEEP / DROP thresholds are
numeric and firable (`KEEP` = ≥3 outcome-changing instances from ≥2 actors on ≥2 days **and** ≥1
recorded correct-null; `DROP` = ≥2 costly instances with no compensating success, **or** shown to
duplicate a shipped tool). The skill's equivalent is prose. Whether a toolkit that gates nothing
needs firable thresholds is exactly the §26 question, and it is Harness Engineering's to answer.

---

## 5 · What this hand-off does not do

- ❌ **Nothing is implemented.** No file under `framework/`, `.claude/` or `governance/` is edited by
  this hand-off other than its own creation.
- ❌ **`LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md` is not landed**, and is not recommended for
  landing. It remains readable at
  `git show origin/claude/q230p-molecular-state-systemic-yruqvc:framework/instruction/LEGEND_DISCOVERY_METHOD_V0_SHADOW_MODE.md`.
- ❌ **No primitive is proposed as mandatory, and none may gate anything.** The directive §26
  constraint governs this hand-off as much as its subject.
- ❌ **No scientific claim, no current file, no registry is touched.**
