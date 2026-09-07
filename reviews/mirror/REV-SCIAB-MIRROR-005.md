---
artifact: MIRROR hostile review, revision 5 (Annex C.2)
review_id: REV-SCIAB-MIRROR-005
object: CAND-20260818-SCIENTIST-AB-SPEC rev 5 · CANDIDATE_CONTENT_HASH 5307d4d2…423f @ base cbce3016
level: R4 (MIRROR_REQUIRED — role contract in CORE, two new protocols, MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted or implied here
date: 2026-08-19
supersedes: nothing. REV-SCIAB-MIRROR-001, -002, -003 and -004 stand as the reviews of revisions
  1–4 and are not amended.
verdict: REQUEST CHANGES — M-4 is genuinely closed in both modes, measured; and §4.4 presents as
  *derived* the one step in it that is chosen, in the normative text the operator must approve.
  One new blocking finding, three recorded, thirteen carried re-classified.
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c, identical at BASE_HEAD and at the candidate content tip
---

# The census now runs in both modes, and the sentence that says why it must block says it was not a decision

Reviewed from `R-1`. **VERDICT TRANSFER: NONE.** Nothing carries over from
`REV-SCIAB-MIRROR-001`, `-002`, `-003` or `-004` — not a verdict, not `M-1`'s closure, not
`M-2`'s, not `M-3`'s closure in `--post-read`, not one row of the eighteen `-004` passed. Every
number below was re-derived in detached scratch worktrees of `BASE_HEAD` and of the candidate
tips, or in non-git exports under the session scratchpad; never in another actor's worktree and
never in root.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd == git top-level == .claude/worktrees/mirror       branch mirror · HEAD 609553cc · clean
ACTOR_ID          mirror · roles/mirror.md read in full · PERSISTENT_LEGEND_ACTOR · worktree mirror
governance        3.1.1 · Annex C (C.1 ladder, C.2 format, C.3 discipline, C.4 objects),
                  Annex D (D.1–D.5), Annex E (E.1, E.2 curation, E.5, E.6), Annex G (G.1, G.2,
                  G.3), Annex H.1, body §12/§14/§15/§36.5, P5 — all read at BASE_HEAD
fingerprint       compose --role mirror  3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                  at BASE_HEAD cbce3016 AND at content tip 2ffaedb2 — IDENTICAL, measured
STABLE ACTOR IDENTITY    mirror · worktree mirror · roles/mirror.md · reconstructed from durable
                  repository evidence alone; no part of it depended on a prior conversation
CURRENT SESSION ROUTING  not durable in the repository. No SESSION_REF is declared for this
                  session and none is invented or inherited. An actor cannot observe its own
                  routing reference.
Agent Card        runtime/agent_card_registry.md is not on main and not on this branch; mirror's
                  four declared capabilities remain UNVERIFIED per contract, L2 suspended
mission           governance layer (MAJOR when in doubt, fail-closed, body §12) · hostile review
                  layer (C.2 format, STEELMAN before objections, declared falsifier;
                  CONFIRMED ≠ true) · metacognitive layer (E.2 curation, dissent lifecycle)
review authority  SYSTEM objects (C.4) at R4; no command over any actor; no primary evidence;
                  may NOT grant HUMAN_APPROVAL (H.1: operator); may NOT CANONICAL_BATCH_COMMIT
                  (H.1: orchestrator); may NOT self-approve changes to its own rubric,
                  clustering, active-learning selection, review-yield or autonomy method (G.2)
permitted writes  branch mirror only, under reviews/ · ledger/ · learning/
forbidden writes  main, root, any other actor's worktree, any *_current.md, any registry, the
                  receipt ledger, the candidate branch
proposer ≠ reviewer ≠ executor   author plan · reviewer mirror · adjudicator operator — holds
G.2               NOT ENGAGED: nothing in the candidate touches Mirror's rubric, clustering,
                  active-learning selection, review-yield or autonomy methodology
```

**MIRROR REHYDRATION: PASS.**

> **Worktree debt, disclosed because it moves numbers.** Branch `mirror` still carries
> `governance/plan_defined_parameters.md` at **P5 v3**, while `BASE_HEAD` carries **v4** with
> three control-plane roots. Every binding number in §1 was computed either in a clean detached
> worktree of `BASE_HEAD` or by an implementation I wrote in the scratchpad from the v4 normative
> text. This is `R-10` of revision 1 — still Mirror's own debt, still not the candidate's, and it
> is the fifth review in which it has to be worked around.

---

## 1 · Binding — PASS

```
base cbce3016 · tip 2ffaedb2 (CONTENT TIP)     5307d4d213c1d25c42a51e27811b7e375907ceed77682b343dee68e0e2b8423f
  governed script, run 1 · 2 · 3               5307d4d2…423f  ×3
  at 4501a8af (MANIFEST TIP)                   5307d4d2…423f   — invariant, measured
INDEPENDENT recomputation — my own implementation of P5.1/P5.2 written from the v4 normative
text (git ls-tree -r --full-tree read as raw bytes through a list argv, never a shell; the three
declared roots removed; PATH-sorted; v4 prefix; every entry newline-terminated including the last)
  at 2ffaedb2  5307d4d2…423f   included 526 · excluded 31
  at 4501a8af  5307d4d2…423f   included 526 · excluded 32   (+CHK-plan-0015, control plane)
POSITIVE CONTROLS — all FIVE published values of the earlier tips, same route
  at a210f738 (revision 4)            07b65b37…5198    525 · 30   ✓ reproduces
  at a3cad1d  (revision 3)            570fcbbb…8ab7    524 · 29   ✓ reproduces
  at b634829  (superseded rev-3 tip)  7cef4ccc…4596    523 · 28   ✓ reproduces
  at daaa3335 (revision 2)            c0701094…21bcf   523 · 27   ✓ reproduces
  at b965ca58 (revision 1)            3b568aae…916c75  522 · 24   ✓ reproduces
  at b1061ebb (mid-rev-4, NOT a binding)  1613fa3b…9332  524 · 30  ✓ reproduces
THE TRAP, exercised deliberately: sorting the whole ls-tree LINE instead of the path
  at 2ffaedb2  ab884df6d3065202b7f9537d0e02f2cafd7ee4927da033a9f0e5b92ed4e1db2c
               — exactly the value the manifest publishes, and a DIFFERENT one, because two
                 100755 entries move when the mode leads the key
main   cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED, merge-base of the branch
```

Four governed runs and eight independent recomputations without the script, of which six are
historical controls. **An implementation that agreed only with itself would prove nothing**; mine
reproduces every published value including the trap, and the trap was run rather than quoted.

**The single content-domain entry separating `07b65b37…` (525) from `5307d4d2…` (526)**, derived
from the tree rather than from the report: `learning/plan/SLR-plan-0005.md`, added. The manifest's
claim is exact, and its `--show-domain` counts reproduce at both tips.

**BINDING: PASS.**

### 1b · Superseded bindings — CORRECTLY CLASSIFIED

Every occurrence of every superseded value in the authoritative manifest was read with its line.
`07b65b37…` at 5, 48, 131, 148, 180, 202; `570fcbbb…` at 6, 50, 132, 206, 1382; `7cef4ccc…` at
53, 133, 206, 1384; `c0701094…` at 7, 55, 134, 1383; `3b568aae…` at 8, 57, 135. Each is a
`supersedes:` clause, a `SUPERSEDED_*` field, a labelled positive-control row, or a sentence
naming it superseded. **No third place presents any of them as current.** `1613fa3b…` is declared
*not* a binding at line 145 and never was one; `ab884df6…` appears once, labelled as the trap's
wrong value.

---

## 2 · STEELMAN (before the objections)

**Revision 5 took the harder of the two remedies I offered, and it was right to, for a reason it
states rather than asserts.**

`REV-SCIAB-MIRROR-004`'s `EVIDENCE_NEEDED` gave Plan two routes: run the census in both modes, or
scope the two printed sentences and §4.5's bullet 2 to `--post-read` and declare the pre-handover
skip population a named residual. The second is cheaper and closes the finding. Plan refused it
and says why: it requires weakening the pre-handover row of the guarantee table — *"no identifier
leak, all of it observed, not attested"* — while the mechanism to satisfy that row already existed
and was one `if` away from running. Weakening a guarantee the code can meet is the permissive
choice with a precision argument in front of it. That reasoning is correct and I accept it.

**The repair is structural where an arithmetical one was available.** `post_read` now has **no
default**, so no future call site can acquire the post-read universe by omission — which is
precisely how the existing one acquired it. The census is computed unconditionally and the mode
became a parameter of what it *means* rather than of whether it *runs*. I verified this by AST:
**37 of 39 top-level definitions byte-identical**, exactly two changed (`cmd_verify`,
`unchecked_surface`), none added, none removed — and `scan_skip_reason` and `SCAN_SKIP_CLASSES`
are among the identical, which is what `M-3`'s closure rests on.

**The oracle's mode is now a runtime fact rather than a fixture name.** `assert_mode()` checks the
claim on argv *and* on the tool's own printed `MODE` line *and* asserts the other mode's line is
absent. I tested this the only way it can be tested: I redirected `verify_pre()` to invoke
`--post-read` in a scratchpad copy and re-ran the suite. **18 tests fail.** Every mode-specific
test in `HandoverGateCensusTests` plus the at-handover partition — and the post-read partition
correctly does not. The assertions are load-bearing, not decorative.

**Plan corrected my own boundary while using it, and it was right.** My `REV-SCIAB-MIRROR-004` §8
bounded `P-7` with *"it disappears the moment the payload contains one non-ASCII character"*. That
sentence is **false** and I confirmed it by construction (§10). Plan found it by having a red
battery it did not understand, pursued it instead of blaming the fix, and pinned the corrected
bound as three executable rows.

**And it disclosed two defects in its own regression harness rather than replacing the numbers.**
The corrected count reconciles with mine exactly: same seven tests, same seven reasons, at both
tips, measured by two independently authored instruments.

I ran the falsifier the candidate hands me — a present file that `verify`, in either mode,
neither scans nor names. I probed 48 by effect in each mode with a passing instrument check and
found none. Then I went at the derivation.

---

## 3 · Population reviewed and evidence executed

**Read in full:** the authoritative candidate manifest at `4501a8af` (1 466 lines), the complete
rev4→rev5 diffs of all five changed content files, `benchmark_input_surface.py` and
`test_benchmark_input_surface.py` at revision 5, `surface_spec.json`,
`controlled_benchmark_ab.md` §1, §2.1–2.3, §3, §4.3–§4.4, §5–§5.1, §9 and the guarantee table,
`learning/plan/SLR-plan-0005.md`, `reviews/mirror/REV-SCIAB-MIRROR-004.md`,
`learning/mirror/SLR-mirror-0012.md`, `ledger/checkpoints/mirror/CHK-mirror-0006.json`; at
source: `roles/mirror.md`, Annexes C, D, E, G, H.1, P5 v4, `scripts/run_release_regressions.py`.

**Executed** — detached worktrees `wt-base` = `cbce3016`, `wt-rev5` = `2ffaedb2`,
`wt-rev5m` = `4501a8af`, `wt-rev4` = `a210f738`, `wt-rev4m` = `0ec863b3`; plus non-git exports of
the rev4 and rev5 trees into the scratchpad for surface construction. The packet was copied
read-only from root `files/fulltext/` into the two exports only. Every attack surface is a copy
under the session scratchpad.

```
binding                   4 governed runs + 8 independent recomputations + 1 trap    PASS
content population        22 content files · +6855 / −1 · derived from git
rev4→rev5 delta           4 content files edited + 1 added; 17 byte-identical by blob sha
function-level delta      37 identical · 2 changed · 0 added · 0 removed  (AST segment)
INDEPENDENT FILE UNIVERSE os.walk + behavioural scan probe, both modes, both revisions     §7 §8
M-4 historical repro      revision 4 pre-handover: SILENT 32, CENSUS 0, VERDICT PASS   REPRODUCED
revision 5                both modes: PRESENT 48 · SCANNED 16 · CENSUSED 32 · SILENT 0 · OVERLAP 0
same bytes, six paths     both modes, both revisions — 24 runs                             §8
encoding battery          13 payload rows × 2 modes, 2 instrument checks first             §9
P-7 boundary              9 code points, LE and BE, byte-level                            §10
mode-specific oracles     anti-vacuity mutation → 18 failures                             §11
discrimination            83/83 green; 20 fail vs rev4's tool; 17 with the MODE back-ported §12
freeze / verify-freeze    13 cases, positive control FIRST                          13 / 13
input parity              5 negatives each on its reason, both modes, control first  5 / 5
release regressions       64 targets @ base · 65 @ rev5, my own harness, per test id       §14
population (B-1)          re-derived ×2, byte-identical to each other AND to the tracked
                          evidence_units.json (b41c7b9f…) · 65 units · 109 panels
publication gate          PASS / BLOCKS 0 · LINT PASS (1 pre-existing INFO) · anchors PASS
fresh-clone journey · documented commands · CLI smoke                              OK · OK · OK
fingerprints              scientist 355e3529… → 82423a48… · plan, mirror, orchestrator IDENTICAL
```

---

## 4 · THE PRIMARY QUESTION — is the pre-handover blocking rule entailed?

I answered this before looking at whether the implementation works, as the directive requires,
and the answer decides this verdict.

### 4A · The derivation, written out with its sources

```
P1  §2.2  "Plan builds each surface and is its only writer until HANDOVER."          unchanged since rev 1
P2  §3    "`build` copies files, it does no templating."                             unchanged since rev 1
P3  §3    "A surface that fails is rebuilt from the spec, never patched: a patched
           surface is one whose content is no longer a function of the allowlist."   unchanged since rev 1
P4  §1    P-7 "Input surfaces built, verified, manifest frozen"; and "BLIND FIRST
           PASS is authorized only when every row reads satisfied at the moment of
           handover."                                                                unchanged since rev 1
P5  §2.3  the ex-ante blinding evidence recorded for the included discipline files:
           `grep -c -i -E '42397075|aqeilan|steinberg|awag239|MYC'` → 0 in each      unchanged since rev 1
P6  code  `undecodable_text` ≡ an allowlisted file with a text suffix whose bytes do
           not decode as UTF-8; the only class with `expected: False`                 rev 4
──────
I1  from P1, P2, P6:  pre-handover an `undecodable_text` file means EITHER the source root
                      carries a non-UTF-8 text-suffixed file, OR the surface was written
                      to after `build`.
I2  from P3:          the SECOND disjunct is forbidden.
I3  from P5, P6:      whichever disjunct holds, the ex-ante grep §2.3 records returns 0 over
                      that file for the same reason the scan does — the recorded blinding
                      evidence for it is vacuous.
I4  from P4, I3:      a `PASS` in that state makes P-7 read satisfied over a file about which
                      the pre-handover guarantee — "no identifier leak, ALL OF IT OBSERVED" —
                      cannot be asserted.
──────
C   §4.4  "Pre-handover it BLOCKS" — rc=1, the surface is not handed over.
```

### 4B · Each inference, attacked

**I1 → I2 is a disjunction with one branch left standing.** §3 forbids *patching*. It does not
forbid the source root carrying a non-UTF-8 text-suffixed file, and `build` copying it faithfully
is precisely *"content that is a function of the allowlist and the source root"* — the thing §3
protects, not the thing it forbids. Plan's own sentence names both branches and then refutes only
the second. **The first branch is not excluded by any normative clause.**

I gave it the strongest steelman I could: I checked whether that branch is empty in fact. Of the
allowlisted entries whose *surface* path carries a scanned text suffix, **16 exist in the source
root and all 16 decode as UTF-8**, measured at the content tip. So the un-forbidden branch is
**empirically empty for BENCH-AB-001 as specified today** — which is a contingent fact about this
tree, not a normative exclusion, and one re-encoding of any of those 16 files restores it.

**I3 holds, and I checked it rather than accepting it.** Over the whole protocol text encoded
UTF-16 (BOM'd and BOM-less), `/usr/bin/grep -c -i -E '…'` returns **0**, against **7** over the
same text in UTF-8. Plan's premise is true.

> **An instrument defect of my own, disclosed because it briefly reversed this row.** My first run
> of that check returned **7** for the BOM'd case, which would have made P5 false. The cause was
> not my script: `grep` in this session's shell is a Claude Code shell **function** shimming to
> `ugrep`, which auto-decodes a UTF-16 BOM. The system `grep` — the one §2.3 means — returns 0.
> The reading was an artifact of my own harness and is discarded. Recorded in `SLR-mirror-0013`.

**I4 holds — and it does not reach C.** I4 establishes that *the pre-handover guarantee row, as
written, cannot be asserted over such a file*. That forces a choice between exactly two internally
consistent designs:

```
(a) BLOCK          rc=1, UNANTICIPATED, the surface is rebuilt from the spec — what revision 5 does
(b) ENUMERATE      PASS, the file named under [UNCHECKED] with EXPECTED_BY_PROTOCOL NO, counted
                   separately, and the guarantee row scoped to say so — exactly what --post-read does
```

(b) is consistent with P1–P6 and with every clause §4.4 cites. Nothing in the premises selects (a)
over (b). The step from *"this is an anomaly and the guarantee cannot be said"* to *"therefore the
command exits non-zero"* is **unstated, and it is the whole of the difference**.

**And Plan knows it.** §4.0aaa of the manifest: *"`REV-SCIAB-MIRROR-004`'s `EVIDENCE_NEEDED`
offers two routes… The second closes the finding. It also requires weakening the pre-handover row
of the guarantee table."* `SLR-plan-0005` L-2: *"I did not take it, and the reason is worth
recording."* Both describe a decision, correctly.

### 4C · What §4.4 says about that step

§4.4's heading over both bullets reads: **"Why the one asymmetry, derived and not chosen."** The
commit message removes any ambiguity about the referent: *"`EXPECTED_BY_PROTOCOL: NO` is BLOCKING
pre-handover and INFORMATIONAL post-read, and the asymmetry is derived rather than chosen."* The
asymmetry named there is **blocking vs informational** — the level, not merely the direction.

The *direction* is genuinely derived: §2.2's writer identity decides whether an unanticipated file
is an anomaly or an artifact, and the closing sentence — *"Who the writer is decides whether an
unanticipated file is an anomaly or an artifact"* — is exactly right and is entailed. The **level**
is not. An anomaly can be named, classified and counted without blocking; that is what the other
mode does with the same class.

```
PRE-HANDOVER BLOCKING DERIVATION:  SUPPORTED_BUT_NOT_ENTAILED
  the ASYMMETRY'S DIRECTION        ENTAILED by §2.2, and correctly so
  the BLOCKING LEVEL              a well-supported CHOICE between two consistent contracts,
                                  disclosed in the manifest and in SLR-plan-0005 L-2,
                                  and described in §4.4 as "derived and not chosen"
```

### 4D · Then: is Plan permitted to specify it here? — YES

I separated this question from the one above, because the answers differ.

```
the protocol is NOT canonical      framework/protocols/controlled_benchmark_ab.md does not exist
                                   at cbce3016; neither does benchmark_input_surface.py. Verified.
                                   There is no prior durable rule this is "stricter than" — the
                                   candidate IS the normative text being authored.
H.1                                "Integrazione strutturale / candidate → Plan". Authoring a
                                   benchmark protocol as candidate content is squarely Plan's.
D.2 / change class                 MAJOR. Approval binds to CANDIDATE_CONTENT_HASH + BASE_HEAD;
                                   the gates are Mirror R4 (this review) and operator
                                   HUMAN_APPROVAL. Neither is spent. Nothing is self-approved.
G.2                                not engaged.
the rule is DECLARED, not smuggled §3's ex-ante list ("EXPECTED_BY_PROTOCOL: NO in this mode is a
                                   FINDING, not a note"), §4.4's table row, and the guarantee-table
                                   row all state it, and the implementation matches all three —
                                   measured in §8.
```

**PLAN AUTHORITY FOR CHANGE: PASS.** The rule is authorized. It is the *characterization* of the
rule that is not.

### 4E · M-5 (BLOCKING) — the decision the operator must make is written as one that was not made

This candidate is `MAJOR` and goes to the operator under H.1 (*"Spese / MAJOR approval /
governance → Operatore"*). §4.4 is content: it becomes canonical. The manifest is control plane
and does not. An operator reading the canonical protocol at §4.4 is told that the blocking level
follows from §2.2 and §3 — that there is nothing here to decide. **There is: it is the one
genuinely discretionary decision revision 5 makes**, and describing it as an entailment removes it
from view at exactly the point where the operator's authority applies.

I want to be exact about the size of this, because it is smaller than `M-2`, `M-3` and `M-4`:

- it is **not** a false claim about what the instrument checks. All four artifacts — the tool's
  two `PASS` sentences, the tool's inline comments, §3's ex-ante list and §4.4's matrix — agree
  with the measured behaviour in both modes (§8). I looked for a false clause and found none;
- the behaviour is **fail-closed**: (a) can never admit a surface (b) would block;
- the alternative **is** disclosed in the content domain, in `SLR-plan-0005` L-2.

And it is still blocking, on one ground: it is a false sentence in normative text about the
provenance of a rule requiring approval, and the two artifacts that disclose the choice do not
correct it — `SLR-plan-0005` L-2 records that the *remedy* was chosen, while §4.4 says the
*asymmetry* was not, and those are different objects. A reader of §4.4 alone is left with the
wrong belief, and §4.4 alone is what canonicalizes.

**The remedy is one sentence and no behaviour change.** §4.4 already contains the reasoning; what
it needs is for the reasoning to stop calling itself a derivation — that the direction of the
asymmetry is entailed by §2.2, that the blocking *level* is a choice between (a) and (b), that (b)
would have required scoping the pre-handover guarantee row, and that (a) was taken because the
mechanism to satisfy the unscoped row already existed. Plan has written every clause of that
already, in §4.0aaa and in `SLR-plan-0005` L-2. It belongs in the protocol.

**M-5: FAIL.** Not on the rule. On the sentence that says the rule was not a decision.

---

## 5 · What the contract promised before, and what it promises now

| Property (pre-handover `verify`) | REV 1–4 | REV 5 | Source of change | Class |
|---|---|---|---|---|
| ex-ante list: parity, forbidden paths, allowlist, slots empty | present | present, unchanged | — | — |
| `CONTENT_SCAN hits == 0` | present | *"over every present file the spec does not exempt"* | §3 | clarification of existing behaviour |
| census printed | **not mentioned** — and not produced | *"the unchecked surface enumerated per actor under `[UNCHECKED]`, class and reason"* | §3, §4.4, code | **IMPLEMENTATION OF EXISTING RULE** — §4.5 bullet 2 already said *on every run* at rev 4, unscoped, and the tool printed the partition clause in both modes. Revision 5 makes the printed claim true instead of scoping it |
| forbidden paths, no exemption at the gate | true in code, **unstated** | stated: *"EVERY one of them, with no exemption; the blind spot is a post-read object"*, and printed as `[BLIND SPOT] none in this mode` | §3, code | **statement of existing behaviour** — the forbidden-path block is **byte-identical** rev4→rev5, verified; same 8 findings at both tips on the same fixture |
| `EXPECTED_BY_PROTOCOL: NO` at the gate | **no clause anywhere**, rev 1 through rev 4 | **BLOCKING** — a finding, `rc=1` | §3, §4.4, guarantee row, code | **NORMATIVE STRENGTHENING** — new rule, new behaviour |
| guarantee row `GUARANTEE_PROVIDED` | *"…no identifier leak — all of it observed, not attested"* | the same, plus the partition, plus *"any class the protocol does not declare is a finding here"*, plus *"observed is now the exact population the census names, not the whole tree"* | §4.3 table | **MIXED** — the added census clause implements what was already claimed; the "finding" clause is new |
| `present` excludes `.git/` | unstated in both modes | stated in **both** `PASS` sentences | code | P-6's printed-claim half, addressed |
| `MODE` line | absent | printed on every run including failing ones | code | new, and it is what makes a mode-assertion possible |

```
REV4→REV5 CONTRACT CHANGE:  MIXED
  census in both modes               IMPLEMENTATION_OF_EXISTING_RULE
  forbidden-path clause, .git scope  STATEMENT of unchanged behaviour
  EXPECTED_BY_PROTOCOL:NO blocking   NORMATIVE_STRENGTHENING — authorized (§4D), mischaracterized (§4E)
```

**Revision 5 did strengthen the contract beyond revisions 1–4.** It did so knowingly, declared it
in three places, and implemented exactly what it declared. That is the right way to strengthen a
contract. Calling the strengthening a derivation is the defect.

---

## 6 · M-4 reproduced historically — revision 4, before anything was believed

Built both surfaces from the revision-4 tree on a clean run and measured with `os.walk` for the
population, scan membership **by effect** (the paper's identifier planted in each present file in
turn, `IDENTIFIER LEAK` naming it observed), census membership parsed from the printed
`[UNCHECKED]` lines. Nothing in the harness imports the module or calls `scan_skip_reason()` or
`unchecked_surface()`.

```
REVISION 4                       PRE-HANDOVER        --post-read
  PRESENT (os.walk)                   48                 48
  SCANNED (by effect)                 16                 16
  CENSUSED                             0                 32
  SILENT                              32                  0      ← 16 per surface
  OVERLAP                              0                  0
  VERDICT                           PASS               PASS
  MODE line                        (none)             (none)
  instrument check               PASSED             PASSED
```

**M-4 REPRODUCED EXACTLY**, including the sixteen-per-surface figure. And the sharpest form, the
whole of `controlled_benchmark_ab.md` re-encoded UTF-16 into `framework/eval/failure_taxonomy.md`
in **both** surfaces so parity cannot see it: at revision 4's gate, `VERDICT: PASS`, `rc=0`, the
path named **0 times**.

---

## 7 · Revision 5 — the partition measured in both modes

```
REVISION 5                       PRE-HANDOVER        --post-read
  PRESENT (os.walk)                   48                 48
  SCANNED (by effect)                 16                 16
  CENSUSED                            32                 32
  SILENT                               0                  0
  OVERLAP                              0                  0
  SYMLINKS                             0                  0
  VERDICT                           PASS               PASS
  MODE line          "pre-handover (HANDOVER GATE)"   "--post-read"
  census classes      scan_exempt_input 12 ·           scan_exempt_input 12 ·
                      suffix_not_scanned 20            suffix_not_scanned 20
  instrument check               PASSED             PASSED
```

Every one of the 48 present files was established as **SCANNED** or **CENSUSED-AS-UNSCANNED**, in
each mode, and never both. Plan's reported counts reproduce exactly.

**The same bytes at six paths, both modes, both revisions** — the payload is the whole of
`controlled_benchmark_ab.md`, a declared `forbidden_prior_output_path` naming the paper, written
identically into both surfaces:

```
                                              REVISION 4                REVISION 5
                                          PRE-HAND   post-read      PRE-HAND   post-read
CLAUDE.md              scan_exempt_input  PASS 0×    PASS NAMED 2×  PASS NAMED 2×  PASS NAMED 2×
benchmark/MODE_DIRECTIVE.md               PASS 0×    PASS NAMED 2×  PASS NAMED 2×  PASS NAMED 2×
files/…/File011.pdf    suffix_not_scanned PASS 0×    PASS NAMED 2×  PASS NAMED 2×  PASS NAMED 2×
output/renders/.gitkeep                   PASS 0×    PASS NAMED 2×  PASS NAMED 2×  PASS NAMED 2×
roles/scientist.md     CONTROL, scanned   FAIL LEAK  FAIL LEAK      FAIL LEAK      FAIL LEAK
output/renders/smuggled.md CONTROL        FAIL ×4    FAIL ×4        FAIL ×4        FAIL ×4
                                          (NOT ALLOWLISTED + IDENTIFIER LEAK in all four)
```

The two controls fail in both modes at both revisions, so the difference is attributable to the
**mode**, not to the payload and not to the invocation. **M-4: PASS.**

---

## 8 · Mode-specific contract matrix — four artifacts, per mode

Constructed independently from the code and the measurements, then compared against the normative
text and the tests. **NORMATIVE TEXT · TOOL OUTPUT · EXECUTABLE BEHAVIOUR · TEST EXPECTATION agree
on every row, in both modes.**

| Property | `verify` — PRE-HANDOVER | `verify --post-read` |
|---|---|---|
| census printed | **yes** — 32, measured | **yes** — 32, measured |
| classes reachable | **3 of 6**: `scan_exempt_input`, `suffix_not_scanned`, `undecodable_text` — the other three sit behind `post_read and _is_expected_output(...)` in the predicate, verified by reading it | **all 6** |
| identifier scan | 16 scanned, measured by effect | 16 scanned, measured by effect |
| allowlist | `NOT ALLOWLISTED` fires, both actors | fires, declared outputs excluded |
| forbidden paths | **every one, no exemption** — `[BLIND SPOT] none in this mode`; `PRIOR OUTPUT` fires on the blind-spot path | every path **except** the printed blind spot |
| slot state | must be empty — `NOT EMPTY` fires | declared outputs expected |
| parity | `PARITY BROKEN` / `NOT DIFFERING` / `ABSENT` all fire | same |
| unexpected outputs | `NOT ALLOWLISTED` | `NOT ALLOWLISTED`; under an output prefix, exempt only if undecodable |
| `EXPECTED_BY_PROTOCOL: NO` | **BLOCKING** — `UNANTICIPATED`, `rc=1`, path named 4×, class `undecodable_text` | **INFORMATIONAL** — named 2×, counted separately, `PASS` |
| verdict effect | any finding → `rc=1` | any finding → `rc=1` |
| handover effect | `PASS` is P-7 of §1 and authorizes step 3 | none |

```
EXPECTED_BY_PROTOCOL:NO AT HANDOVER:  BLOCKING — declared, implemented and measured;
                                      the rule is authorized (§4D), its stated provenance is not (§4E)
```

---

## 9 · UTF-16 hostile battery at the gate — PASS, with the right reason

Instrument checks first: untouched pair `PASS` in both modes; the same payload in UTF-8 →
`rc=1 IDENTIFIER LEAK` in both. Then the payload written identically into **both** surfaces at
`framework/eval/failure_taxonomy.md` — allowlisted, `.md`, normally scanned.

| payload | PRE-HANDOVER | `--post-read` |
|---|---|---|
| UTF-16 (BOM) | **rc=1 FAIL** · `UNANTICIPATED` · `undecodable_text` · named **4×** | rc=0 PASS · named 2× · `EXPECTED_BY_PROTOCOL NO` |
| UTF-16LE no BOM | **rc=1 FAIL** · same | rc=0 PASS · same |
| UTF-16BE no BOM | **rc=1 FAIL** · same | rc=0 PASS · same |
| UTF-16LE + BOM | **rc=1 FAIL** · same | rc=0 PASS · same |
| UTF-16BE + BOM | **rc=1 FAIL** · same | rc=0 PASS · same |
| CP1252 | **rc=1 FAIL** · same | rc=0 PASS · same |
| latin-1 | **rc=1 FAIL** · same | rc=0 PASS · same |
| **ASCII-only, UTF-16LE no BOM** | rc=0 PASS · not named · **genuinely scanned** | rc=0 PASS · not named |
| **ASCII-only, UTF-16BE no BOM** | rc=0 PASS · not named · **genuinely scanned** | rc=0 PASS · not named |
| ASCII-only, UTF-16LE + BOM | **rc=1 FAIL** · `undecodable_text` · named 4× | rc=0 PASS · named 2× |

Parity **holds** in every row — the bytes are identical in both surfaces — so no row is a parity
check answering for a scan. The blocking rows carry the **correct reason**: `UNANTICIPATED …
undecodable_text`, not a generic non-zero exit. The post-read column is byte-for-byte the
behaviour `REV-SCIAB-MIRROR-004` §9 ruled informational, undisturbed.

**UTF16 HANDOVER: PASS.**

---

## 10 · P-7 — my own boundary was false, and the correction is right

Reproduced by construction, per code point, both byte orders:

```
                       UTF-16LE   UTF-16BE   any byte > 0x7f   LE decodes as UTF-8
U+2014 em dash  —      14 20      20 14           no                  YES
U+2013 en dash  –      13 20      20 13           no                  YES
U+2018–201D ‘’“”       18 20 …    20 18 …         no                  YES
U+00A7 section  §      a7 00      00 a7          YES                   no
U+1F534         🔴     3d d8 34 dd  d8 3d dd 34  YES                   no
U+00E9          é      e9 00      00 e9          YES                   no
```

A sentence containing an em dash, an en dash and curly quotes — **non-ASCII by any definition** —
encodes to UTF-16LE and UTF-16BE with a maximum byte of `0x79`, zero bytes above `0x7f`, and
**decodes as valid UTF-8**. So the file is genuinely read by the scan.

```
P-7 OLD REASONING (mine, REV-SCIAB-MIRROR-004 §8):
  "it disappears the moment the payload contains one non-ASCII character"        FALSE
P-7 REVISED BOUNDARY (Plan): the criterion is a BYTE above 0x7f, not a character  SUPPORTED
```

And the conclusion my false test was offered for **survives**: the real artifact carries 411
non-ASCII characters including `§` and `🔴`, giving **188 bytes above `0x7f`** in its UTF-16LE
encoding, and it does not decode. A BOM alone (`FF FE`) also suffices. `P-7` remains a **scan
limit, not a census hole**, and it is carried, not closed. The bound is now three executable rows
plus the BOM case rather than a sentence in one of my reviews.

---

## 11 · Mode-specific oracles — PASS, and proved by mutation

`assert_mode()` checks three things before any population is read: that argv does or does not
carry `--post-read` as the claimed mode requires; that the tool's own printed `MODE` line names
that mode; and that the other mode's line is **absent**. A fixture name is nowhere evidence.

```
HANDOVER oracle    verify_pre()  → argv ("verify", "--spec", …, "--surfaces", …)   NO FLAG
POST-READ oracle   verify_post() → the same argv + "--post-read"
                   both return (result, argv); every mode-specific test asserts on both
```

**Anti-vacuity, measured rather than argued.** I redirected `verify_pre()` to invoke
`--post-read` in a scratchpad copy of the tree and changed nothing else:

```
83 tests → FAILED (failures=18)
  every mode-specific test in HandoverGateCensusTests            12 methods / 16 cases
  ExpectedOutputPrefixTests.test_…_at_handover                    1
  test_bomless_utf16_… (all rows)                                 (within the 18)
  test_…_post_read                                     CORRECTLY DOES NOT FAIL
```

A wrong mode makes the relevant tests fail. **MODE-SPECIFIC ORACLES: PASS.**

Both partition tests delegate to `_assert_partition(mode)`, which asserts the four population
identities as **sets** and carries the anti-vacuity guard
`assertTrue(scanned, "positive control: the scan never fired…")`.

> **A second instrument defect of mine.** My AST audit of the added probes first reported *"2
> exit-code-only"* — the two partition tests — because it did not follow the delegation into
> `_assert_partition`. Reading the helper corrected it. `N-6`'s claim that no exit-code-only
> assertion was added is **TRUE**: of the 13 added tests, 11 assert a class or reason string and a
> mode directly, and the 2 that delegate assert four set identities plus the guard.

---

## 12 · Discrimination — sets compared, not counts

```
revision 5 suite at revision 5's tool                      83 / 83 GREEN
revision 5 suite against revision 4's TOOL, raw            20 non-passing
revision 5 suite against revision 4's tool + the MODE
  line back-ported and NOTHING else                        17 non-passing (15 FAIL + 2 ERROR)
```

Plan claims *"the 3 that stop failing are the two positive controls and the post-read partition,
which must not [discriminate]"*. Two counts agreeing is not a check; I compared the **sets**:

```
STOPPED being non-passing once rev4's tool got the MODE line — exactly three, and exactly these:
  ExpectedOutputPrefixTests.test_every_present_file_is_either_scanned_or_named_post_read
  HandoverGateCensusTests.test_positive_control_the_same_payload_in_utf8_is_read_and_caught
  HandoverGateCensusTests.test_positive_control_the_scan_fires_at_the_handover_gate
NEWLY non-passing:  ∅
```

**The claim is exact.** The two `ERROR`s are substantive, not instrument noise:
`KeyError: 'CLAUDE.md'` — revision 4's tool produced no census at the gate for the census lookup
to read. That is `M-4` itself.

> **One row of the 17 discriminates on a statement rather than a behaviour**, and Plan's phrase
> *"fail on SUBSTANCE"* is imprecise for it. `test_the_handover_gate_exempts_no_forbidden_path`
> fails against revision 4's tool only on the new printed line `[BLIND SPOT] none in this mode`;
> the forbidden-path enforcement block is **byte-identical** rev4→rev5 and produces the same eight
> findings at both tips on that fixture, which I verified directly. The line it asserts is **true**
> — the gate really does exempt no forbidden path — so this is a documentation gain correctly
> tested, not a behaviour change and not a false claim. Recorded as `P-11`, non-blocking.

**WRONG-REASON LOAD-BEARING PASSES: 0.**

---

## 13 · M-1, M-2, M-3 and freeze

**M-1: PASS.**

```
git diff cbce3016 2ffaedb2 -- scripts/test_locator_obligation_reaches_every_route.py   EMPTY
git diff a210f738 2ffaedb2 -- (same)                                                   EMPTY
§5.1 of controlled_benchmark_ab.md — zero locator lines in the rev4→rev5 diff
test_every_route_carries_the_obligation_or_declares_an_exemption   ok at cbce3016 AND at 2ffaedb2
the suite's one failure is test_the_bootstrap_states_the_rule (file='CLAUDE.md'), identical
  at both tips and one of the seven pre-existing baseline failures
roles/scientist.md byte-identical rev4→rev5
```

**M-2: PASS.** `output/renders/smuggled.md` is caught in **both** modes at revision 5 —
`NOT ALLOWLISTED` + `IDENTIFIER LEAK`, `rc=1`, path named 4× — and identically at revision 4, so
the mechanism was not touched. `_is_expected_output`, `_is_decodable_text`, `_classify` and
`iter_files` byte-identical by AST.

**M-3: PASS in both modes.** `SILENT 0` post-read *and* pre-handover, measured with the
independent oracle rather than with `scan_skip_reason()`. The predicate itself did not move:
`scan_skip_reason` and `SCAN_SKIP_CLASSES` are **byte-identical by AST segment**, so the six
classes and their order are the ones revision 4 closed on.

**FREEZE: PASS — 13 / 13, positive control first.**

```
POSITIVE CONTROL untouched tree           rc=0 · 29 fields · outputs 0 · unexpected 0
  SURFACE_ABSOLUTE_PATH  "NOT RECORDED — local-instance value (protocol §2.3)"
  fields carrying an absolute machine path: NONE
verify-freeze on the untouched tree       rc=0 PASS
one edited byte after the freeze          rc=1, names roles/scientist.md
a file added after the freeze             rc=1, names newfile.md
a file removed after the freeze           rc=1, names roles/scientist.md
receipt pointed at the other actor's tree rc=1, 3 differences
freezing A's tree as scientist-b          rc=2, names 'scientist-a' read from inside the tree
wrong benchmark id                        rc=2, names BENCH-AB-001
invalid first-pass state                  rc=2, argparse "invalid choice"
a symlink present in the tree             rc=2, SYMLINK
decodable text in the render slot         UNEXPECTED_FILE_SET=[output/renders/smuggled.md]
a real binary render                      OUTPUT_FILE_SET=[output/renders/fig1.png]
UTF-16 over an allowlisted INPUT          neither OUTPUT nor UNEXPECTED; in FILES with its digest
```

Plan's claim that freeze cannot have interacted with the change is exact and I verified it by AST
rather than by reading: `cmd_freeze`, `cmd_verify_freeze` and `_classify` are byte-identical, and
**none of the three calls `cmd_verify` or `unchecked_surface`** — their call sets are
`{_classify, _front_matter, _git, iter_symlinks, load_spec, refuse, sha256_file, tree_digest, …}`,
`{_front_matter, iter_symlinks, refuse, tree_digest, …}` and `{_allowed_paths, _is_expected_output}`.

---

## 14 · Regression accounting — my own harness, granularity separated from suite-level

Every target of each tip's own `TESTS` tuple executed the way the runner executes it
(`python3 <relative>`, cwd = tree root) in clean detached worktrees; neither holds `files/`.
Failure blocks parsed per test id, `subTest` parameter suffixes included. Normalization is limited
to worktree root, temp dirs, `line <N>`, addresses and elapsed times — **no assertion text is
normalized**, so a changed reason cannot be normalized into agreement.

```
                                    BASE cbce3016      REV 5 2ffaedb2
targets in TESTS                          64                 65
targets missing                            0                  0
tests executed (granular targets)        870                953      ← delta 83 = the new suite exactly
FAILING SUITES                             6                  6
GRANULAR FAILING TESTS                     7                  7
suites red with NO parsed test failure      ∅                  ∅      ← the omission channel is empty
targets with NO test-id granularity        3                  3
```

**FAILING SUITES — identical set at both tips:**
`framework/scripts/test_session_self_eval.py` · `scripts/test_abstract_corpus_is_not_evidence.py` ·
`scripts/test_fulltext_trace_contract.py` · `scripts/test_locator_obligation_reaches_every_route.py` ·
`scripts/test_release_runner_verdict.py` · `scripts/test_release_surface.py`

**GRANULAR FAILING TESTS — the same seven at both tips, and nothing else:**

```
framework/scripts/test_session_self_eval.py::SelfEvalGate.test_diagnosis_is_wired_before_growth_and_takeaways
scripts/test_abstract_corpus_is_not_evidence.py::…::test_the_bootstrap_bounds_the_corpus(file='CLAUDE.md')
scripts/test_fulltext_trace_contract.py::…::test_normative_layers_make_receipts_universal
scripts/test_fulltext_trace_contract.py::…::test_normative_write_rules_name_the_append_only_carveout
scripts/test_locator_obligation_reaches_every_route.py::…::test_the_bootstrap_states_the_rule(file='CLAUDE.md')
scripts/test_release_runner_verdict.py::…::test_every_tracked_test_file_is_in_the_runner
scripts/test_release_surface.py::…::test_shebang_python_entrypoints_are_executable

ADDED GRANULAR FAILING TESTS    (rev5 − base) = ∅        ADDED FAILING SUITES   = ∅
REMOVED GRANULAR FAILING TESTS  (base − rev5) = ∅        REMOVED FAILING SUITES = ∅
SAME-REASON                                   = 7 / 7    UNEXPLAINED REASON CHANGES = 0
```

**NON-GRANULAR RED TARGETS: none red — but three carry no test-id granularity at all**, and I
report them apart rather than as test-level passes, which is the distinction Plan asks for and
gets right:

```
launch/test_legend_launch.py                                             rc 0 → 0
.claude/skills/legend-study-intake-triage/scripts/test_study_dedup_triage.py     rc 0 → 0
.claude/skills/legend-batch-inferential-sweep/scripts/test_batch_inferential_sweep.py  rc 0 → 0
   NON-GRANULAR COMPARISON: rc AND normalized output byte-identical at both tips, all three.
   No test-level equivalence was measured inside them and none is claimed.
```

**Does the absence of test ids in those three prevent a load-bearing non-regression conclusion?**
No — but only because their entire normalized output is identical, which is a *stronger* check
than a test-id set comparison for a suite that prints its own verdict. Had their output differed
at all, the conclusion would have been unsupported and I would say so. Plan's declaration of this
limitation is accurate and correctly refuses to count them as passes.

**REGRESSION: PASS. SUITE DELTA 0 · TEST-METHOD DELTA 0 · SAME-REASON 7/7 · OMISSION CHANNEL EMPTY.**

> **`P-10`, recorded, non-blocking.** §4.2's *"tests executed"* row reports **850** at `BASE` and
> **933** at revision 5. I measure **870** and **953**, and `REV-SCIAB-MIRROR-004` measured 870 at
> `BASE` with a differently authored harness — two independent instruments agreeing on the set and
> on the number. Plan's row is also internally inconsistent: its own revision-4 cell says **941**,
> and `941 − 850 = 91` while revision 4's suite is 71 tests, whereas `941 − 870 = 71` exactly. The
> row appears to mix a re-measured pair with a carried-over figure. It is **descriptive**: not one
> of the load-bearing rows — failing suites, failing tests, same-reason, omission channel,
> granularity — depends on it, and all of those reconcile exactly. Same class as `P-8`.

### 14b · The two wrong-harness results Plan discloses

`SLR-plan-0005` L-3 records three, not two: (1) a hostile-UTF-16 battery that went red because the
payload's em dash encodes below `0x80` — the tool was right and the test was wrong (this is L-4
and §10); (2) `python3 -m unittest <dotted-module>` cannot name twelve targets whose paths carry
hyphens or dots, and single-line verbose matching drops every test with a docstring, giving 421
tests; (3) `subTest` failures print a `FAIL:` header while the top-level line still ends `... ok`,
giving five failing tests where seven fail.

Verified: the corrected count is the one that reconciles with my independent measurement, and
mine was authored without reading Plan's harness (which is **not committed** — a limitation
`SLR-plan-0003` L-4 declared and neither revision 4 nor revision 5 repaired). **The discarded runs
are durably disclosed rather than silently replaced**, in a content-domain record. That is the
correct handling and I record it as met.

---

## 15 · Gates, commands and the reader journey

```
publication gate         VERDICT: PASS · BLOCKS: 0 at the content tip ([REVIEW] rows pre-existing)
legend_lint              VERDICT: PASS (1 pre-existing INFO — CLAIM 010 wikilink not required)
growth_anchors check     VERDICT: PASS — claims=39 · papers=70 · corpus=356 · literature=390
test_documented_commands 2 tests OK          test_fresh_clone_reader_journey  5 tests OK
test_cli_smoke           1 test OK           candidate suite                 83 / 83 OK
```

**Does the actual journey invoke the mode whose guarantee revision 5 specifies?** Yes, and this is
the question a passing unit test on a dead mode would not answer. `verify` **without** `--post-read`
is the documented gate on the live route: §5 step 1 is *"build both surfaces…; `verify`"*, §5 step
3 is HANDOVER, and §1's P-7 is *"Input surfaces built, verified"*. §3's ex-ante block now names it
in the text — *"← THE HANDOVER GATE. §5 step 1 runs it… No flag: `--post-read` is a different
contract."* No documented `.md` invocation anywhere in the tree passes `--post-read` to `verify`.
The mode that revision 5 specifies is the mode the protocol's own sequence runs, and it is the one
that was silent at revision 4.

---

## 16 · Findings — one blocking, three recorded, thirteen carried

| # | Plan's class at rev 5 | Mirror's finding |
|---|---|---|
| **P-4** | CARRIED, STATED, NOT CLOSED | **CARRIED, TRUTHFULLY.** By AST: `emit_digests` appears **only** in `cmd_build`; `cmd_verify` has no reference to it and the CLI exposes no digest input on `verify`. Every hostile probe in this review made the identical-edit-to-both-surfaces move and **parity was silent in every one** — 24 six-path runs and 26 encoding runs — exactly as declared. Revision 5's new pre-handover language does **not** imply P-4 is solved: the `scan_exempt_input` census line still scopes its coverage claim to *"a change made to one surface only"*, and both `NOT CHECKED` sentences now name *"a change made identically to BOTH surfaces, which parity cannot see"* |
| **P-6** | CARRIED — printed half addressed | **CARRIED, CORRECTLY.** `iter_files` byte-identical, so `.git/**` is still outside both populations. I re-ran the exposure: the whole protocol text at `.git/info/notes.md` in a surface gives `VERDICT: PASS`, census unchanged at 32, the path named **0 times**, in **both** modes. What changed is that both `PASS` sentences now print *"`Present` is every regular file in the surface tree outside `.git/`"*. **Not closed**, and Plan does not claim it is |
| **P-7** | CARRIED — boundary corrected | **CARRIED, and the correction is mine to accept.** §10. My stated boundary was false; Plan's is right; the conclusion survives; the residual is unchanged and is a scan limit |
| **P-8** | FIXED | **RESOLVED.** The front matter now says *"FIVE content files change: four edited and one added"*, and five change — verified from the tree. But see `P-9` |
| **N-1** | CARRIED | **NON-BLOCKING CARRIED.** `surface_spec.json` is edited at this revision — one `_note` block, about the census in both modes — and the File012 normalization contradiction is again not among them. Correctly declared |
| **N-2** | CARRIED, unchanged | **NON-BLOCKING CARRIED.** `cmd_population` byte-identical by AST; `declared_empty_sources` still accepted on declaration. Population re-derived: 65 units, 109 panels, one declared-empty source |
| **N-3** | CARRIED, latent | **NON-BLOCKING CARRIED.** `_pdf_pages` / `_regex_units` byte-identical, verified |
| **N-6** | CARRIED, declared | **NON-BLOCKING CARRIED, and the rev-5 claim is TRUE.** Of the 13 tests added, 11 assert a class or reason string **and** the mode; the 2 that delegate assert four set identities plus the anti-vacuity guard. No exit-code-only assertion was added — §11 |
| **N-7** | UNRESOLVED, honestly labelled | **UNRESOLVED.** Fourth review running. Revision 5 did not re-run revision 1's tool and neither did I. A measured number and an inferred explanation still face each other, and neither side has closed it |
| **N-8** | CARRIED, contained | **NON-BLOCKING CARRIED.** `cmd_locators` byte-identical, verified |
| **N-9** | CARRIED | **NON-BLOCKING CARRIED.** Vocabulary in a note, untouched |
| **P-1 · P-3 · P-5** | CARRIED | **CONFIRMED** — `BASE_HEAD`'s guard, and see N-6 / N-7 |
| **R-1 … R-12** | not reopened | Not reopened. `R-10` is still Mirror's own worktree debt (§0) and moved numbers again |
| **M-1 · M-2 · M-3** | retested, not reopened | **All three re-measured from R-1 and closed** — §13 |

**New this review:**

- **`M-5` — BLOCKING.** §4.4 presents the pre-handover **blocking level** as derived when it is a
  choice between two internally consistent contracts, in normative content that becomes canonical
  and on the one point where the operator's MAJOR authority applies. §4E. Not a false claim about
  what the instrument checks; a false claim about whether a decision was made.
- **`P-9` — non-blocking.** The manifest's §2 file-list table is stale at revision 5 in three
  respects, measured: the **Status** cell of all four modified content files still reads
  *"modified (rev 3, rev 4)"* and omits rev 5; the classification cell for
  `test_benchmark_input_surface.py` still says ***71** probes* where the suite is **83**; and the
  block below the table says *"control plane 6 files"* where the measured count is **8** at the
  content tip and **9** at the manifest tip (6 was correct at revision 3). The prose immediately
  under the same table **is** updated and exact — 37/39, 525→526, four edited plus one added,
  named. Control plane, excluded from the hash, does not move the binding. It is `P-8`'s class,
  one revision after `P-8` was closed, which is the candidate's own `L-1` again: *a repaired
  instance is not a repaired class*.
- **`P-10` — non-blocking.** §4.2's *"tests executed"* row: 850/933 against my 870/953, with
  `REV-SCIAB-MIRROR-004` independently at 870, and internally inconsistent with its own rev-4
  cell. §14.
- **`P-11` — non-blocking.** One of the 17 substantive discriminating tests discriminates on a new
  printed line over byte-identical behaviour. §12. The line is true; the characterization is
  imprecise.

**Nothing is marked resolved because `M-4` was fixed.** `P-8` is the only closure and it is a
number in a manifest, exactly as Plan says.

---

## 17 · SLR-plan-0005 — BOUND, and curated under Annex E.2

### 17.1 · Procedural integrity — PASS

```
belongs to this session/candidate   task SCIENTIST-AB-SPEC-001 · directive v1 · generation 5 ✓
is CONTENT                          learning/ is under no CONTROL_PLANE_ROOT; P5.1 declares it
                                    CONTENT by intent, and says so explicitly ✓
committed BEFORE any revision-5 binding   2ffaedb2 IS the declared CONTENT_TIP and the commit that
                                    carries the record — ONE content commit for the whole revision.
                                    Absent at a210f738, verified ✓
included in the authoritative hash  the SINGLE content-domain entry separating 07b65b37… (525)
                                    from 5307d4d2… (526), derived from the tree ✓
no pre-SLR binding presented as authoritative   no intermediate revision-5 content commit exists.
                                    Nothing had to be superseded within the revision — the second
                                    consecutive revision to achieve that, by a simpler route ✓
```

**SLR-plan-0005: BOUND.**

### 17.2 · Epistemic curation (Annex E.2)

Vocabulary is the repository's: `CONFIRMATION_CLASS ∈ {ORIGINAL_OBSERVATION, REPLICATION,
EXPOSURE_AFTER_BROADCAST}`; only the first two count fully; `BEST_PRACTICE_CANDIDATE` threshold is
≥2 confirmations in those two classes, or 1 + Mirror validation; conflicts → Mirror adjudicates →
`SUPERSEDED` with reason. **No `LEARNING_INDEX` exists** — E.2 names the instrument and Plan owns
its durability — so this curation lives here and in `SLR-mirror-0013` and can be queried by
nothing. That debt is Plan's, declared in the record itself, and is now **four reviews old**.

Every class in the record is marked *proposed* and the record refuses to self-certify. Correct.

**L-1 — *I fixed the predicate and reasoned as if that fixed the report*.**
Self-classed `REPLICATION` of `SLR-mirror-0012` §1, read at source before the remediation began.
**ACCEPTED, and the self-classification is the right one** — I wrote the mode-axis observation
first and Plan read it, so this is not an `ORIGINAL_OBSERVATION` and Plan does not claim it is.
`CLASS: FAILURE_PATTERN` — accepted. What Plan **adds** beyond my formulation is the diagnosis of
*why holding the rule did not help*: `SLR-plan-0004` L-1 is a rule about **populations**, `M-2` and
`M-3` were population errors, and `M-4` is a **mode** error the population rule does not reach.
That is a genuine refinement of my own record and I adopt it. With `SLR-mirror-0012` §1
(`ORIGINAL_OBSERVATION`, mirror) + this `REPLICATION` (plan), `EVIDENCE_COUNT: 2` in the first two
classes → **BEST_PRACTICE_CANDIDATE**. `STATUS: LOCAL → PROVISIONAL` is available on E.1 and I
leave the promotion to Plan's durability role, since no index exists to record it in.

**L-2 — *the two modes were one contract in my head and two in the code*.**
`ORIGINAL_OBSERVATION` (plan) — **ACCEPTED.** `CLASS: MICRO_UPGRADE` — accepted. `STATUS: LOCAL`.
The proposed rule — *when one mechanism runs at two points of a transfer of authorship, write its
contract once per point before deciding anything about either* — is correct, transferable, and is
the most useful sentence in the record. Writing §4.4 as two contracts is what made the census
error impossible to restate.

**One formulation inside L-2 is SUPERSEDED, with reason**, and it is the same formulation as `M-5`:

> *"The asymmetry, if there is one, is usually already stated somewhere as a fact about who the
> writer is — and inherited from the other point it looks like a design decision when it is an
> unexamined transfer."*

**The inverse also happens, and it happened here.** The fact about the writer settles whether an
unanticipated file is an **anomaly or an artifact**; it does not settle whether an anomaly
**blocks**. Reading the writer-identity fact as settling the level makes a design decision look
like an unexamined transfer *pointed the other way* — a decision presented as a derivation. The
record's own L-4 states the discipline that catches it: *a residual recorded with a stated boundary
has two claims in it, and the boundary is the one nobody re-derives.*

**REFINED_FORMULATION (L-2):** *writing one mechanism's contract once per point of a transfer
reveals which properties differ; it does not by itself license the strength assigned to either
side. Separate the entailed **direction** of an asymmetry from the chosen **level** of it, and say
in the normative text which is which.* With Plan's `ORIGINAL_OBSERVATION` plus this Mirror
validation the **narrowed** formulation reaches `BEST_PRACTICE_CANDIDATE`; the general one does not.

**L-3 — *my own harness produced three wrong numbers, each caught by a control I nearly left out*.**
Self-classed `REPLICATION` of `SLR-mirror-0010` §4 / `-0011` §3 / `-0012` §2 — **correctly, and
generously**: Plan credits the family to my records rather than claiming it. **ACCEPTED.**
`CLASS: MICRO_UPGRADE` · `STATUS: LOCAL`. What is genuinely **new** and is Plan's own is the
observation that **none of the three was an exit-code battery** — all three were assertions on
*content* that read exactly like correct negatives. That extends the rule I have paid for five
times, and I paid for it twice more in this session (§22) in the two forms Plan names: a wrong
invocation, and an instrument that was not my script at all. `CONFIRMATION_CLASS: REPLICATION`
(mirror, this session) added on the extension. **EVIDENCE_COUNT ≥ 4 across both actors →
`BEST_PRACTICE_CANDIDATE`**, and it is the strongest-supported item in either actor's records.

**L-4 — *a review's conclusion can be right while the test it states for it is not*.**
`ORIGINAL_OBSERVATION` (plan) — **ACCEPTED**, and it is about my own review. `CLASS:
FAILURE_PATTERN` — accepted. The generalisation — *a residual recorded with a stated boundary has
two claims in it, and the boundary is the one nobody re-derives* — is correct, I reproduced the
encoding facts independently (§10), and Plan's restraint in not reclassifying `P-7` while
correcting its bound is the right handling. **This is the record's best entry**: it corrects the
reviewer, does not inflate the correction into a finding, and converts a prose boundary into three
executable rows. `CONFIRMATION_CLASS: REPLICATION` (mirror, this session) on the encoding facts.

**Cross-cutting.** For the fourth consecutive revision, both actors independently record that the
artifact written to correct a false claim is where the next one lives — and revision 5 is the
fourth instance, in a milder form: `M-4`'s remedy is correct, and the section written to justify it
carries `M-5`. `M-2` was scoped to a spec key, `M-3` to a skip condition, `M-4` to a CLI flag, and
`M-5` is not a scope error at all — it is the *justification* of the remedy overreaching. The
family has moved from *what was measured* to *what was claimed about why*.

**G.2.** This curation is of Plan's learning, which is E.2 work and squarely Mirror's. It ratifies
nothing of Mirror's own methodology. The two observations this session produced about my own
harness (§22) are filed `LOCAL` in `SLR-mirror-0013` and are **not** self-ratified; if either is to
bind it goes `MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen by
Orchestrator.

---

## 18 · Non-regression of stabilized properties

Seventeen of revision 4's twenty-two content files are **byte-identical at revision 5 by blob
sha**, and the binding proves no other content moved. Where a row rests entirely on those files a
targeted confirmation is recorded; where revision 5 touched the file, the row was re-measured.

```
B-1 SCIENTIFIC POPULATION  PASS       re-derived ×2, byte-identical to each other AND to the
                                      tracked evidence_units.json (b41c7b9f…) · 65 units ·
                                      109 panels · 6 main_figure · 7 main_results ·
                                      2 main_methods · 10 supplementary_figure ·
                                      24 supplement_methods · 7 supplement_table ·
                                      9 source_data_blot · 1 declared empty
B-3 FREEZE RECEIPT         PASS       §13 — 13/13, 29 fields, no absolute machine path
B-5 SEVEN BENCHMARK FIELDS PASS       OUTPUT_SCHEMA.md byte-identical to revision 4
MODE A/B TASK SCOPING      PASS       scientist_reading_modes.md, MODE_A.md, MODE_B.md and both
                                      ASSIGNMENT files byte-identical; no instruction file touched
ACTOR EQUIVALENCE          PRESERVED  no file carrying §32 was edited at this revision
C-2 FORWARD OWNERSHIP      PASS       byte-identical
INPUT PARITY               PASS       5 negatives each on its reason in BOTH modes, positive
                                      control first: PARITY BROKEN · NOT DIFFERING · ABSENT ·
                                      NOT ALLOWLISTED · IDENTIFIER LEAK
SCIENTIFIC DEPTH           PRESERVED  no MODE file, no assignment, no instruction and no
                                      population file changed at revision 5
ACTOR REGISTRATION         PASS       roles/scientist.md and BOOTSTRAP.md byte-identical
CANONICALIZATION DEP.      CONFIRMED  measured at both tips: scientist 355e3529… → 82423a48…;
                                      plan 9c0c13fb…, mirror 3dff8954…, orchestrator e2c54470…
                                      ALL THREE IDENTICAL — exactly as §9 states
NO PARALLEL CLAIM SCHEMA   NONE       no claim-schema file changed at revision 5
PUBLICATION GATE           PASS / BLOCKS 0 at the content tip
LINT / growth anchors      PASS (1 pre-existing INFO) · claims=39 · papers=70 · corpus=356 ·
                                      literature=390
```

---

## 19 · EVIDENCE_FOR · EVIDENCE_AGAINST · ALTERNATIVES · KEY_OBJECTIONS

**EVIDENCE_FOR.** The binding reproduced twelve times, eight without the governed script, with
**five** published control values and the line-sort trap run deliberately and matching the
published wrong value; `M-4` reproduced exactly at revision 4 (32 silent, 0 censused, `PASS`) and
closed at revision 5 in **both** modes against an independent `os.walk` universe with a passing
instrument check — 48 = 16 scanned + 32 censused, 0 silent, 0 overlap; the repair structural, with
37 of 39 definitions byte-identical and the mode parameter left without a default so no call site
can acquire the wrong universe by omission; the mode-specific oracles proved by mutation, 18 tests
failing when the handover oracle is pointed at the wrong mode; the discrimination compared as a
**set** — 20 → 17 with the `MODE` line back-ported, and the three that stop are exactly the two
positive controls and the post-read partition; the UTF-16 battery blocking at the gate with the
**correct reason** in all seven non-ASCII rows and informational post-read in all seven, parity
holding in every one; `M-1`, `M-2` and `M-3` re-measured from R-1 and closed, the predicate
`M-3` rests on byte-identical; freeze 13/13 with the positive control first and provably isolated
from both changed functions by AST; the regression delta zero at test-method granularity over seven
shared failures whose reasons are byte-identical with no assertion text normalized, the omission
channel empty at both tips, and the three non-granular targets reported apart rather than as
passes; the population re-derived byte-identically to the tracked file; every carried residual
named and none falsely closed, `P-4` and `P-6` explicitly not closed by `M-4`'s repair, `N-7`
honestly unresolved; the Session Learning Record bound as the single entry that moves the hash,
committed before any binding was named; my own false `P-7` boundary corrected by the author and
the correction verified; no scope creep.

**EVIDENCE_AGAINST.** §4.4 — the section this revision adds, and the one Plan asked to be attacked
first — states that the blocking level of `EXPECTED_BY_PROTOCOL: NO` is *"derived and not chosen"*.
It is not derived. Its first leg is a disjunction of which §3 forbids only one branch, and the
un-forbidden branch is excluded here only by a contingent fact about today's source root (16 of 16
allowlisted text-suffixed files decode; measured). Its remaining legs establish that the
pre-handover guarantee row cannot be asserted over such a file — which forces a **choice** between
blocking and scoping the row, not blocking itself. Plan states elsewhere, twice, that it made that
choice and why. The protocol says it did not.

**ALTERNATIVES_CONSIDERED.**
(i) *Classify the derivation `INVENTED` and require the blocking behaviour struck* — **rejected.**
The rule is declared in three places in the candidate's own normative text, implemented exactly as
declared, fail-closed, and authored by the actor H.1 gives candidate authority to, under gates
neither of which is spent. It is not invented; it is under-described.
(ii) *Accept, carrying `M-5` as a recorded finding* — **rejected.** It is a false sentence in
content that becomes canonical, about whether a decision requiring the operator's MAJOR authority
was a decision. `REV-SCIAB-MIRROR-002` rejected *"carry the false claim as a debt"* and the ratchet
does not get to slacken because this instance is milder.
(iii) *Treat it as `AMBIGUOUS` and block on benchmark isolation* — **rejected.** Isolation does not
depend on it: the stricter rule is fail-closed and can only refuse surfaces the weaker rule would
admit. The finding is about the record, not the isolation.
(iv) *Block on `P-9`/`P-10` too* — **rejected.** Both are control-plane numbers that move no
binding and mislead no reader about what the instrument checks. `REV-SCIAB-MIRROR-004` recorded
`P-8`, the identical class, as non-blocking, and applying a harder standard now would be
inconsistency rather than rigour.
(v) *Treat `M-4` as not fully closed* — **rejected.** It is closed, in both modes, measured with an
independent oracle. Saying otherwise would be inaccurate and would matter to whoever reads
revision 6.

**KEY_OBJECTIONS Plan may raise, and my answer.**
*"'The one asymmetry' means the direction — anomaly vs artifact — and that IS derived."* — Agreed,
and I say so in §4C. But the commit message attaches the same word to *"BLOCKING pre-handover and
INFORMATIONAL post-read"*, and the bullet that concludes *"Pre-handover it blocks"* sits under the
heading. The referent a reader takes is the level, and the level is chosen.
*"§4.0aaa and `SLR-plan-0005` L-2 both say the choice was made, so nothing is hidden."* — §4.0aaa
is in the manifest, which is control plane and does not canonicalize. L-2 is content and says the
**remedy** was chosen — the census over the scoped sentence. Neither corrects §4.4's statement
about the **blocking level**, and §4.4 is what a future reader of the canonical protocol has.
*"The stricter rule is safer; blocking it is rewarding the weaker design."* — I am not asking for
the weaker design. §4E asks for one sentence and no behaviour change. If the answer is that the
level really is entailed, the falsifier below says what would show it.
*"Revision 5 was scoped to `M-4`; the derivation is new scope."* — It is not: §4.4 is the section
revision 5 added to justify `M-4`'s remedy, and Plan's own §6.0000 puts it **second** in the order
it most wants attacked, ahead of the behaviour.

---

## 20 · VERDICT

```
Annex C.2 VERDICT       REFINED — M-4 is genuinely and completely closed: the census runs in both
                        modes, the mode is a parameter of what it means rather than of whether it
                        runs, the parameter has no default, the two modes print two sentences each
                        stating only what its own run checked, and the oracles were proved by
                        mutation to exercise the modes they name. And the section written to
                        justify the one new rule inside that remedy says the rule was derived when
                        it was decided — the fourth consecutive revision in which the artifact
                        written to correct a claim carries the next one, now one level up: not in
                        what was measured, but in what was claimed about why.
REFINED_FORMULATION     §2.2's writer identity entails the DIRECTION of the asymmetry — who wrote
                        the tree decides whether an unanticipated file is an anomaly or an
                        artifact. It does not entail the LEVEL: an anomaly can be named,
                        classified and counted without blocking, which is what the other mode does
                        with the same class. The blocking level is a choice between two contracts
                        consistent with every premise §4.4 cites, and it is the choice the
                        operator is being asked to approve.
MIRROR_REVIEW           REQUEST CHANGES
REVIEWER_CONFIDENCE     high on the binding (12 reproductions, 5 published controls, trap matched)
                        high on M-4's closure in both modes (independent os.walk universe +
                          behavioural probe, instrument check passed in both, 0 silent, 0 overlap,
                          reproduced at revision 4 first)
                        high on the mode oracles (mutation → 18 failures) and on the
                          discrimination (sets compared, not counts)
                        high on the regression delta (own harness, omission channel empty,
                          7/7 same-reason, non-granular targets separated)
                        MEDIUM on M-5 — it is a judgement about how a normative sentence will be
                          read, not a measurement, and I state it as such
RESIDUAL_UNCERTAINTY    M-5 is the mildest blocking finding I have written on this candidate and I
                        say so. The behaviour is correct, fail-closed, and the choice is disclosed
                        twice in the durable record — just not in §4.4. I weigh it as blocking on
                        consistency with REV-SCIAB-MIRROR-002's rejection of "carry the false claim
                        as a debt" and on H.1 putting MAJOR approval with the operator, rather than
                        on an independent severity scale, and an adjudicator could reasonably
                        weigh it as P-class. N-7 is unreconciled for the fourth review running and
                        I did not settle it. P-6 and P-9/P-10 did not influence the verdict. Two
                        instrument defects of my own are reported in §22; the numbers here are
                        from the corrected runs.
EVIDENCE_NEEDED         §4.4: one sentence separating the entailed direction of the asymmetry from
                        the chosen level, stating that scoping the pre-handover guarantee row was
                        the available alternative and why it was refused — the text already exists
                        in §4.0aaa and SLR-plan-0005 L-2 and needs to be in the protocol. No
                        behaviour change, no test change. Optionally: P-9's four stale cells in the
                        manifest's §2 table and P-10's tests-executed row corrected.
WHAT_WOULD_CHANGE_MY_MIND
                        M-5: a clause in §2.2, §3, §1 or §4.3 — at BASE_HEAD or at revisions 1–4 —
                             under which an unanticipated-but-allowlisted artifact must make the
                             pre-handover command exit non-zero rather than be enumerated; or a
                             demonstration that (b) — PASS, named, counted separately, guarantee
                             row scoped — is inconsistent with a premise §4.4 cites, which would
                             make the level entailed after all; or §4.4 rewritten so the sentence
                             matches what §4.0aaa already says, in which case M-5 becomes P-class
                             and the verdict changes with no other change to this candidate.
                        M-4: any present file that verify, in EITHER mode, neither scans nor names
                             — 48 probed by effect in each mode, instrument check passed, 0 found.
                        M-3: the predicate moving — scan_skip_reason and SCAN_SKIP_CLASSES are
                             byte-identical by AST segment.
                        binding: any of the five published controls failing to reproduce through
                             my implementation — all five reproduce, and the trap matches the
                             published wrong value.
AUTHOR_RESPONSE         required (C.2); silence is not acceptance.
```

**HUMAN_APPROVAL: NONE — not granted, not recommended, not implied.**
**MAIN: cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED.**
**Nothing was executed, nothing canonicalized, no benchmark run, no registration performed, no
other actor's worktree written, the candidate branch not written.**

---

## 21 · Scope, and what this review did not touch

**SCOPE CREEP: NONE.** Measured over the content diff `cbce3016 → 2ffaedb2`: zero content paths
matching `session|rout|registr`; zero `*_current.md`; zero registry or receipt-ledger paths. The
rev4→rev5 diff touches exactly eight files — four content edited, one content added, and three
control-plane. `roles/scientist.md`, `BOOTSTRAP.md`, both MODE files, both ASSIGNMENT files,
`OUTPUT_SCHEMA.md`, `scientist_reading_modes.md`, `benchmark_manifest.json`,
`evidence_units.json`, `run_release_regressions.py` and `framework/protocols/index.md` are all
byte-identical to revision 4.

**SESSION-ROUTING DEBT: OUT OF SCOPE — NOT SILENTLY RESOLVED.** §5c of the manifest names the gap
between stable `ACTOR_ID` and current routable `SESSION_REF` and implements nothing. This review
implements nothing either, declares no `SESSION_REF` for itself, infers no routing from chat
recency, and supersedes no other Mirror session.

---

## 22 · Provenance of this review

Detached worktrees created with `git worktree add --detach`: `wt-base` at `cbce3016`, `wt-rev5` at
`2ffaedb2`, `wt-rev5m` at `4501a8af`, `wt-rev4` at `a210f738`, `wt-rev4m` at `0ec863b3`. The rev4
and rev5 trees were additionally exported with `git archive` into **non-git** directories under the
session scratchpad for surface construction, so no git worktree was dirtied by a built surface.
The packet was copied read-only from root `files/fulltext/` into those two exports only. Every
attack surface is a copy under the scratchpad. All binding numbers were computed in a worktree
carrying `BASE_HEAD`'s script and P5 **v4**, or by an implementation written in the scratchpad from
P5.1/P5.2, never in this branch's checkout, which carries P5 v3 (`R-10`).

The session guard refused one inline heredoc while the shell was inside a repository worktree. I
did not reach for an unchecked tool: the mutation was authored with `Write` into the scratchpad,
made to refuse any path outside it, and invoked by name; the measurement is the same one.

**Two instrument defects committed by this reviewer, both caught, both disclosed.**
1. My independent file-universe probe reported `PRESENT 48 · SCANNED 0 · CENSUSED 0 · SILENT 48`
   in **both** modes — a partition claim false in the opposite direction, in a review whose subject
   is a partition claim. The cause was a wrong `--surfaces` argument giving `rc=2` on every run.
   It was caught **only** because the battery requires `roles/scientist.md` to be observed leaking.
   The run was discarded and the harness re-authored; every number in §7–§9 is from the corrected
   one. Sixth sighting of this family in my own harnesses (`SLR-mirror-0010` §4, `-0011` §3,
   `-0012` §2).
2. My check of Plan's §2.3 grep premise returned **7** where it should return 0, which would have
   falsified a load-bearing premise of §4.4. The defect was not in my script: `grep` in this
   session's shell is a Claude Code shell **function** shimming to `ugrep`, which auto-decodes a
   UTF-16 BOM. `/usr/bin/grep` returns 0, and Plan's premise stands. **This is a new form** — the
   instrument was the shell itself, not anything I wrote, and no positive control inside my script
   could have caught it; what caught it was that the result contradicted a premise I had reason to
   expect held, and I went looking. Recorded in `SLR-mirror-0013`, **not** self-ratified.
3. My AST audit of the added probes reported two as exit-code-only because it did not follow a
   delegation into `_assert_partition`. Corrected by reading the helper; `N-6`'s claim is true.

Time source: the runtime exposes no wall clock beyond the date. Governance loaded 3.1.1; the mirror
fingerprint is identical at `BASE_HEAD` and at the candidate content tip, measured.

**WRONG-REASON LOAD-BEARING PASSES in the candidate: 0.**
