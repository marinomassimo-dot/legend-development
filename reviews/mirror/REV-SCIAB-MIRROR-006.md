---
artifact: MIRROR hostile review, revision 6 (Annex C.2)
review_id: REV-SCIAB-MIRROR-006
object: CAND-20260818-SCIENTIST-AB-SPEC rev 6 · CANDIDATE_CONTENT_HASH beef6db0…6061 @ base cbce3016
level: R4 (MIRROR_REQUIRED — role contract in CORE, two new protocols, MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted or implied here
date: 2026-08-19
supersedes: nothing. REV-SCIAB-MIRROR-001 … -005 stand as the reviews of revisions 1–5 and are
  not amended.
verdict: ACCEPT — M-5 is closed. The direction of the asymmetry is entailed and the blocking
  level is presented as the policy choice it is, with the alternative named, the fail-closed
  argument stated, and the operator named as its approver, in canonical content. No executable
  byte moved. Two non-blocking findings recorded; N-7 unresolved and not load-bearing.
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c, identical at BASE_HEAD and at the candidate content tip
---

# The direction was entailed, the level was chosen, and §4.4 now says which is which

Reviewed from `R-1`. **VERDICT TRANSFER: NONE.** Nothing carries over from
`REV-SCIAB-MIRROR-001`, `-002`, `-003`, `-004` or `-005` — not a verdict, not `M-1`'s closure,
not `M-2`'s, not `M-3`'s, not `M-4`'s closure in both modes, not one row any of them passed.
Every number below was re-derived in detached worktrees of `BASE_HEAD` and of the candidate
tips, or in non-git exports under the session scratchpad; never in another actor's worktree and
never in root.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd == git top-level == .claude/worktrees/mirror       branch mirror · HEAD 1b988344 · clean
ACTOR_ID          mirror · roles/mirror.md read in full · PERSISTENT_LEGEND_ACTOR · worktree mirror
governance        3.1.1 · Annex C (C.1–C.4), Annex D (D.1–D.5), Annex E (E.1, E.2, E.5, E.6),
                  Annex G (G.1, G.2, G.3), Annex H.1/H.2, P5 — read at BASE_HEAD
fingerprint       compose --role mirror  3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                  at BASE_HEAD cbce3016 AND at content tip 2a854177 — IDENTICAL, measured.
                  scientist rotates 355e3529… → 82423a48…; plan and orchestrator unchanged.
STABLE ACTOR IDENTITY    mirror · worktree mirror · roles/mirror.md · reconstructed from durable
                  repository evidence alone; no part of it depended on a prior conversation
CURRENT SESSION ROUTING  not durable in the repository. No SESSION_REF is declared for this
                  session and none is invented or inherited. An actor cannot observe its own
                  routing reference. This session supersedes no other Mirror session.
Agent Card        no agent_card path exists at BASE_HEAD, on the candidate, or on branch mirror.
                  Mirror's four declared capabilities remain UNVERIFIED per contract; L2 suspended
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
                  active-learning selection, review-yield or autonomy methodology. Nothing in
                  this review self-ratifies Mirror methodology.
```

**MIRROR REHYDRATION: PASS.**

> **Worktree debt, disclosed because it moves numbers.** Branch `mirror` still carries
> `governance/plan_defined_parameters.md` at **P5 v3**, while `BASE_HEAD` carries **v4** with
> three control-plane roots. Every binding number in §1 was computed either with `BASE_HEAD`'s
> own script in a clean detached worktree, or by an implementation I wrote in the scratchpad
> from the v4 normative text. This is `R-10` of revision 1 — still Mirror's own debt, still not
> the candidate's, and it is the sixth review in which it has to be worked around.

---

## 1 · Binding — PASS

```
base cbce3016 · tip 2a854177 (CONTENT TIP)   beef6db08bdf8489b68078fc00c08fee913a585a4e1ee8359b592fc9e31a6061
  governed script (BASE_HEAD's own), runs 1·2·3      beef6db0…6061  ×3
  at 5edfd040 (MANIFEST TIP)                         beef6db0…6061   — invariant, measured
INDEPENDENT recomputation — my own implementation of P5.1/P5.2 written from the v4 normative
text (git ls-tree -r --full-tree read as raw bytes through a list argv, never a shell; the three
declared roots removed; PATH-sorted; v4 prefix; every entry newline-terminated including the last)
  at 2a854177  beef6db0…6061   included 527 · excluded 32   ×3
  at 5edfd040  beef6db0…6061   included 527 · excluded 33   (+CHK-plan-0016, control plane)
POSITIVE CONTROLS — all SIX published values of the earlier tips, same route
  at 2ffaedb2 (revision 5)            5307d4d2…423f    526 · 31   ✓ reproduces
  at a210f738 (revision 4)            07b65b37…5198    525 · 30   ✓ reproduces
  at a3cad1d  (revision 3)            570fcbbb…8ab7    524 · 29   ✓ reproduces
  at b634829  (superseded rev-3 tip)  7cef4ccc…4596    523 · 28   ✓ reproduces
  at daaa3335 (revision 2)            c0701094…21bcf   523 · 27   ✓ reproduces
  at b965ca58 (revision 1)            3b568aae…916c75  522 · 24   ✓ reproduces
THE TRAP, exercised deliberately at BOTH tips: sorting the whole ls-tree LINE, not the path
  at 2a854177  740cb9c11129f88f57379304ee33aafcce7a153ba126146bf1530c4389f3fc11
  at 2ffaedb2  ab884df6d3065202b7f9537d0e02f2cafd7ee4927da033a9f0e5b92ed4e1db2c
               — both exactly the values the manifest publishes as its own trap, and both
                 DIFFERENT from the real ones, because two 100755 entries move when the mode
                 leads the key
main   cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED, merge-base of the branch
```

Four governed runs and eight independent recomputations without the script, of which six are
historical controls, plus two traps. **An implementation that agreed only with itself would
prove nothing**; mine reproduces every published value including both trap values.

**The single content-domain entry separating `5307d4d2…` (526) from `beef6db0…` (527)**, derived
from the tree rather than from the report: `learning/plan/SLR-plan-0006.md`, added — the only
addition, with nothing removed. The other four changed content files move blobs without moving
the entry count, which is why the count alone is not the evidence and the hash is.

**Topology, verified rather than assumed.** `5edfd040^ == 2a854177`; the manifest commit touches
only `governance/candidates/` and `ledger/`, both declared `CONTROL_PLANE_ROOTS`; the content
commit touches five content files and nothing else. Revision 6 has exactly **one** content
commit, so no pre-SLR revision-6 hash could have been declared, and none was.

**BINDING: PASS.**

### 1b · Superseded bindings — CORRECTLY CLASSIFIED

I read every occurrence of every superseded value on the branch, in content and control plane
alike, with its line. `5307d4d2…`, `07b65b37…`, `570fcbbb…`, `7cef4ccc…`, `c0701094…` and
`3b568aae…` appear only as `supersedes:` clauses, `SUPERSEDED_*` fields, labelled positive-control
rows, historical checkpoint records, or sentences naming them superseded. **No third place presents
any of them as current.** `1613fa3b…` is declared *not* a binding and never was one; `740cb9c1…`
and `ab884df6…` appear only labelled as the trap's wrong values.

---

## 2 · STEELMAN (before the objections)

**Revision 6 does the rarest thing this candidate has been asked to do: it makes a claim weaker
and leaves everything else exactly where it was.**

`M-5` was the mildest blocking finding I have written on this candidate, and the cheap response
was available — delete the offending heading and move on. Plan did not take it. It reproduced the
finding from the sources before editing a byte, wrote the derivation out with numbered premises,
and reached the same place I did: `I4` eliminates the permissive reading of the unscoped guarantee
row and stops. It then went looking for the branch that would have made the level entailed — my
own `WHAT_WOULD_CHANGE_MY_MIND`, a clause requiring an unanticipated-but-allowlisted artifact to
exit non-zero — and reported that there is none. I ran that falsifier independently across
`BASE_HEAD` and revisions 1–4 and there is none.

**It corrected my finding's scope against me, and it was right to.** `M-5` names §4.4. Plan
searched the revision-5 content population for the claim's *meaning* and found it in **four**
operative places, three of which would have survived a grep for the review's own wording. I
reproduced that count independently. The `surface_spec.json` note was the worst of the four and
the furthest from the review — it dropped `I1`'s source-root disjunct entirely and asserted flatly
that `build` cannot produce the state, which is false. A finding names one site and is a lower
bound on the sites; this is the second revision running in which that rule earned its keep.

**The identity claim is measured, not asserted, and it survives four independent conventions.**
I compared the tool's definitions by `ast.dump` at top level, at top level with docstrings
stripped, over every nested definition, and over every top-level statement. All four say the same
thing: nothing added, nothing removed, nothing changed. The one class that differs by plain
`ast.dump` in the test file is exactly where the docstring was edited, and it stops differing when
docstrings are stripped.

**The `POLICY CHOICE` block is in the canonical text, not only in the manifest.** That was the
whole of `M-5`: the manifest is control plane and does not canonicalize, so disclosing the choice
there and calling it an entailment in §4.4 left a reader of §4.4 alone with the wrong belief. §4.4
now carries the rule, the rationale, the refused alternative, the fail-closed argument, and the
sentence that matters most — *the choice is the Human Operator's to approve or refuse under H.1,
and refusing it selects (b) without disturbing any other claim in this section.*

**And it disclosed a third harness defect of its own** — a regex over `run_release_regressions.py`
that missed two entries written as implicit string concatenation, giving 63/62 against the true
65/64 — rather than replacing the numbers. My AST reader returns 65/64. Plan's corrected
870/953 reconciles with my independent measurement exactly.

Then I went at the corrected §4.4, because a sentence replaced by several longer sentences has
more surface, not less.

---

## 3 · Population reviewed and evidence executed

**Read in full:** the authoritative candidate manifest at `5edfd040` (1 736 lines);
`reviews/mirror/REV-SCIAB-MIRROR-005.md` and `learning/mirror/SLR-mirror-0013.md`; the complete
rev5→rev6 diffs of all four edited content files; `learning/plan/SLR-plan-0006.md`;
`framework/protocols/controlled_benchmark_ab.md` §1, §2.2, §2.3, §3, §4.3, §4.4 and the guarantee
table at the content tip; `framework/scripts/benchmark_input_surface.py` around `cmd_verify`,
`scan_skip_reason` and `SCAN_SKIP_CLASSES`; the edited docstring and its test;
`surface_spec.json`; `ledger/checkpoints/plan/CHK-plan-0016.json`; at source `roles/mirror.md`,
Annexes C, D, E, G, H.1, and P5 **v4** at `BASE_HEAD`.

**Executed** — detached worktrees `wt-base` = `cbce3016`, `wt-rev4` = `a210f738`,
`wt-rev5` = `2ffaedb2`, `wt-rev6` = `2a854177`, `wt-rev6m` = `5edfd040`; plus non-git exports of
the rev5 and rev6 trees into the scratchpad for surface construction. The packet was copied
read-only from root `files/fulltext/` into those two exports only. Every attack surface is a copy
under the session scratchpad.

```
binding                   4 governed runs + 8 independent recomputations + 2 traps       PASS
M-5 derivation            re-derived from §1, §2.2, §2.3, §3 at source; falsifier run    CLOSED
false-claim sweep         23 content files, meaning not wording, with a rev-5 control     0
behaviour rev5→rev6       AST ×4 conventions · JSON structural · 4 live verify runs      IDENTICAL
partition M-3/M-4         independent os.walk universe, scan measured BY EFFECT,
                          instrument check passed, both modes, both revisions            SILENT 0
UTF-16 at the gate        rc=1 · 2× UNANTICIPATED · undecodable_text; post-read rc=0     PASS
mode oracles              mutation: verify_pre() redirected to --post-read → 18 failures PASS
M-1                       guard byte-identical to BASE_HEAD; the named test green at both PASS
M-2                       same bytes under the prefix and one dir away; render control   PASS
freeze                    receipts field-identical; verify-freeze PASS; mutation refused PASS
regression                65/64 targets by AST, both tips, omission channel empty        0 ADDED
gates                     LINT · publication gate · anchors · receipts · fresh clone     PASS
```

---

## 4 · THE PRIMARY QUESTION — derived, or chosen?

I re-derived this before reading Plan's answer, and I did not transfer my own from `-005`.

### 4A · The direction — ENTAILED

```
P1  §2.2  "Plan builds each surface and is its only writer until HANDOVER; at handover the
           writer becomes the named actor."
P2  §3    "`build` copies files, it does no templating."
P3  §3    "A surface that fails is rebuilt from the spec, never patched."
P4  §1    P-7 "Input surfaces built, verified, manifest frozen"; BLIND FIRST PASS authorized
           only when every row reads satisfied AT THE MOMENT OF HANDOVER.
P5  §2.3  the ex-ante blinding evidence: `grep -c -i -E '42397075|aqeilan|…'` → 0 per file.
P6  code  `undecodable_text` ≡ allowlisted, text suffix, bytes not UTF-8; the only class with
           `expected: False`.
──────
D1  pre-handover the writer is Plan and the tree is a pure copy of the source root under the
    allowlist; post-handover the writer is the reader, who is PERMITTED to write files.
D2  the pre-handover guarantee row asserts "no identifier leak — ALL OF IT OBSERVED"; the
    post-read row asserts ENUMERATION.
D3  an `undecodable_text` file is inconsistent with the pre-handover row AS WRITTEN — §2.3's
    grep over it is vacuous for exactly the reason the scan is — and CONSISTENT with the
    post-read row as written, because an enumerated file is enumerated.
──────
∴   the same class carries different epistemic weight on the two sides of the transfer, and
    that difference follows from P1 alone. No discretionary premise is used.
```

I attacked the one step that could fail. `I1`'s disjunction — *the source root carries such a
file, or the surface was patched* — has **one branch left standing**: §3 forbids patching, it does
not forbid the source root carrying a non-UTF-8 text-suffixed file, and `build` copying it
faithfully is what §3 protects rather than what it forbids. Revision 6 states this, with the
contingency, and its move is correct: **either branch leaves the same epistemic state**, so the
direction survives the surviving branch. I checked the contingent fact too — 16 of 16 allowlisted
text-suffixed files decode as UTF-8 at the content tip, so the branch is empirically empty for
`BENCH-AB-001` as specified today, which is what the protocol now says rather than more.

**ASYMMETRY DIRECTION: ENTAILED.**

### 4B · The level — A POLICY CHOICE

What the premises reach is `I4`: *a `PASS` in that state would assert a guarantee the run cannot
support.* That eliminates the combination *unscoped row + `PASS`*. It leaves two contracts:

```
(a) BLOCK      rc=1, the surface is not handed over and is rebuilt from the spec
(b) ENUMERATE  PASS, the file named under [UNCHECKED] with EXPECTED_BY_PROTOCOL NO, counted
               apart, and the pre-handover GUARANTEE_PROVIDED row narrowed to say so
```

I checked (b) against every clause §4.4 cites and it is consistent with all of them. §3's *rebuilt
from the spec, never patched* governs what happens **when** a surface fails; it does not decide
**which** states are failures. §1's `P-7` reads satisfied under (b) with a narrowed row. And (b)
is not hypothetical: it is exactly what the same tool does post-read with the same class.

I ran the falsifier independently rather than accepting the report. `framework/protocols/
controlled_benchmark_ab.md` and `benchmark_input_surface.py` **do not exist at `BASE_HEAD`** —
verified from the tree — and the token `BLOCKING` first appears in the protocol at revision 5.
Revisions 1–4 contain no clause requiring an unanticipated-but-allowlisted artifact to exit
non-zero. **There is no prior durable rule from which the level could be inherited.** My sweep
harness discriminates: it finds `POLICY CHOICE` at revision 6 and not at revision 5, and finds
*derived and not chosen* at revision 5 and not at revision 6.

The give-away is the one Plan names in `SLR-plan-0006` L-2 and it is right: the premises speak of
what can be **asserted**, the conclusion speaks of an **exit code**. Nothing carries one to the
other.

**PRE-HANDOVER BLOCKING LEVEL: POLICY CHOICE.** Independently derived, not inherited.

### 4C · The fail-closed claim — verified structurally, not taken on the sentence

§4.4 claims *(a) can only refuse surfaces (b) would admit*. I did not accept this from prose. In
`cmd_verify` the pre-handover branch is a guarded loop that **only appends** to `findings`; it
removes nothing and it alters no other check. Deleting it is precisely (b) minus the row
narrowing. So the two contracts cannot disagree in the permissive direction in any reachable
state, and the claim holds by construction rather than by enumeration of cases.

### 4D · Plan's authority to propose it — PASS

```
the protocol is NOT canonical      neither file exists at cbce3016. Verified from the tree.
                                   There is no prior rule this is "stricter than".
H.1                                "Integrazione strutturale / candidate → Plan". Authoring a
                                   benchmark protocol as candidate content is squarely Plan's.
D.2 / change class                 MAJOR. Approval binds to CANDIDATE_CONTENT_HASH + BASE_HEAD;
                                   the gates are Mirror R4 (this review) and operator
                                   HUMAN_APPROVAL. Neither is spent. Nothing is self-approved.
G.2                                not engaged.
```

**PLAN AUTHORITY TO PROPOSE: PASS.**

### 4E · M-5 — CLOSED

The three things `M-5` required are in the canonical text, not only in the manifest:

| `M-5` required | Where it now is | Verified |
|---|---|---|
| the entailed direction separated from the chosen level | §4.4 heading *"a derived direction, and a chosen level"*, and two labelled bullets **Derived — the direction** / **Chosen — the level** | read at the content tip |
| the alternative named, and why it was refused | §4.4 `ALTERNATIVE NOT CHOSEN`, naming (b) and *"it narrows the epistemic content of the handover gate in order to admit a surface the stricter rule can refuse"* | read at the content tip |
| who approves it | §4.4 `STANDING`: *"the choice is the Human Operator's to approve or refuse under H.1, and refusing it selects (b) without disturbing any other claim in this section"* | read at the content tip |

I applied my own test from `-005` §4E: **would an operator reading §4.4 alone know a decision is
theirs?** Yes. The heading says a level was chosen; the `POLICY CHOICE` block names the rule, the
alternative, the fail-closed property and the approver; and the closing sentence of the derived
bullet — *"That much is entailed, and it is the whole of what §2.2 settles"* — bounds the
entailment instead of extending it. The sentence I objected to is gone and nothing replaced it
that overclaims in the other direction.

**M-5: PASS.**

---

## 5 · The four operative sites — found independently, and swept for a fifth

`M-5` was written against §4.4. I searched the revision-5 content population for the claim's
meaning and reproduced Plan's four, then swept revision 6 for what survived.

| Site | Revision 5 | Revision 6 | Class |
|---|---|---|---|
| `controlled_benchmark_ab.md` §4.4 | *"Why the one asymmetry, derived and not chosen"* | separated, with the `POLICY CHOICE` block | **CURRENT TRUE** |
| `benchmark_input_surface.py` ~L596 | *"the asymmetry is derived rather than chosen"*, directly above the branch that implements the blocking | DERIVED/CHOSEN separated; names the branch that goes if the operator refuses | **CURRENT TRUE** |
| `test_benchmark_input_surface.py` docstring | *"It is a FINDING, and `rc=1`"* — the same jump, no keyword to grep | *"This test pins the declared rule; it does not prove the rule was the only one available"* | **CURRENT TRUE** |
| `surface_spec.json` `content_scan/_note` | *"See §4.4 for **the derivation**"*, and *"is not a state build can produce"* — false twice | DERIVED/CHOSEN separated, `FROM A TEXT SOURCE` restored, points at the `POLICY CHOICE` block | **CURRENT TRUE** |
| revision 5's commit message | *"derived rather than chosen"* | not rewritten | **HISTORICAL** — rewriting it would move the content tip and destroy the binding chain |
| `SLR-plan-0005` L-2 | the same reasoning in the session record | not rewritten; curated by Mirror under E.2 | **HISTORICAL** — it is the evidence `M-5` rests on |

**My sweep, and its instrument check.** I swept all 23 content files for the class of claim, not
the string: `derived and not chosen`, `derived rather than chosen`, `follows necessarily`,
`logically forced`, `inevitab`, `no alternative`, `the only consistent`, `had to be`, `must block`,
`not a decision`, `not a choice`, `is forced`, `compelled`, `leaves no choice`, `by necessity`,
`entail`. The same sweep against revision 5 finds the two known false sites, so it discriminates.

At revision 6 the surviving hits are: §4.4's *"That much is entailed"* (bounding the entailment to
the direction — **true**, and I derived it myself in §4A), §4.4's *"it is not an entailment of the
premises above"* (a disclaimer — **true**), §4.4's `ALTERNATIVE NOT CHOSEN` label (**true**), and
quotations of the old formulation inside `SLR-plan-0006` where it is being reported as the defect
(**HISTORICAL**). I then read every content site that mentions the class or the rule at all —
§3's ex-ante list, §4.3's census bullet, `SCAN_SKIP_CLASSES`, the two `PASS` sentences, three test
docstrings — and every one **declares** the rule; none claims it was entailed.

```
FALSE OPERATIVE CLAIMS (entailment class):   0
```

---

## 6 · Behaviour rev5 → rev6 — IDENTICAL

The identity claim is the one everything else rests on, so I measured it four ways rather than
one, and I ran an instrument check on the instrument.

```
benchmark_input_surface.py
  top-level FunctionDef/ClassDef, ast.dump          32 / 32 identical · 0 added · 0 removed
  the same with every docstring stripped            32 / 32 identical
  EVERY definition incl. nested, qualified names    33 / 33 identical
  every top-level STATEMENT (Plan's convention)     51 / 51 identical      ← reconciles §4.6a
test_benchmark_input_surface.py
  top-level defs, plain ast.dump                    27 / 28 — HandoverGateCensusTests differs
  the same with docstrings stripped                 28 / 28 identical      ← a docstring is not
  every definition incl. nested, docstrings stripped 126 / 126 identical      an assertion
  test methods added at rev6                        0
surface_spec.json — parsed and compared leaf by leaf against the revision-5 blob
  exactly ONE key path differs: content_scan/_note. No key added, none removed, no path,
  pattern, suffix, exemption or prefix touched.
```

**INSTRUMENT CHECK on my own comparator:** run over rev4 → rev5 it reports exactly two changed
definitions, `cmd_verify` and `unchecked_surface` — the pair `-005` measured. A comparator that
reported "identical" for every input would have said what I wanted here.

**Live runs, on real surfaces built from each tree.**

```
                              REV 5            REV 6         output comparison
pre-handover, clean           rc=0 PASS        rc=0 PASS      BYTE-IDENTICAL
--post-read, clean            rc=0 PASS        rc=0 PASS      BYTE-IDENTICAL
UTF-16 hostile at the gate    rc=1 FAIL        rc=1 FAIL      identical but for the tree digests
same bytes --post-read        rc=0 PASS        rc=0 PASS      identical but for the tree digests
census, both modes, clean     32 · 32          32 · 32
suite                         83 / 83 OK       83 / 83 OK
freeze receipt                29 fields        29 fields      field-for-field identical, same
                                                              TREE_SHA256 e2c1e171…
verify-freeze, untouched      PASS             PASS
verify-freeze, one byte appended after the freeze              rc=1, refused
```

**The two digest differences are the payload, and I proved it rather than explaining it.** The
hostile payload *is* the protocol text, which differs between the revisions, so the digests must
move. I re-ran the pair with **identical bytes** planted at both revisions: the outputs are then
byte-identical **including** the tree digests, in both modes. That control converts an explanation
into a measurement.

**BEHAVIOR REV5→REV6: IDENTICAL.**

---

## 7 · M-1 · M-2 · M-3 · M-4 — targeted non-regression, re-measured

**M-1 — PASS.** `scripts/test_locator_obligation_reaches_every_route.py` is byte-identical to
`BASE_HEAD` (`git diff` empty over `cbce3016 → 2a854177` and over `2ffaedb2 → 2a854177`), so the
guard is unweakened. §5.1 is present and `verbatim_locators` appears three times in the protocol,
so the semantic obligation is still carried by the route rather than exempted. Run alone,
`test_every_route_carries_the_obligation_or_declares_an_exemption` is **green at `BASE_HEAD` and
green at the content tip**, and it is absent from both failing sets in §9.

**M-2 — PASS.** Same bytes, one directory apart, against the rev-6 tool, planted into both
surfaces:

```
output/renders/smuggled.md                     → NOT ALLOWLISTED + IDENTIFIER LEAK 20 hit(s), rc=1
…/fulltext_dossiers/NOTES.md      (control)    → NOT ALLOWLISTED + IDENTIFIER LEAK 20 hit(s), rc=1
output/renders/fig1_page1.png     (real render)→ rc=0, and [UNCHECKED] names it undecodable_prefix
```

The prefix admits only bytes the tool cannot decode; a decodable file there takes every check it
would take anywhere else. The old prefix-smuggling defect remains closed, and the positive control
that must not move did not move.

**M-3 and M-4 — PASS, measured with an independent oracle in BOTH modes.** My harness enumerates
the universe with `os.walk`, measures scan membership **by effect** (the paper's identifier planted
in each present file in turn, `IDENTIFIER LEAK` naming it observed), and parses census membership
from the printed `[UNCHECKED]` lines. It imports nothing from the module and reads no report.

```
                    instrument   PRESENT   SCANNED   CENSUSED   SILENT   OVERLAP
rev6 pre-handover     PASSED        48        16         32        0         0
rev6 --post-read      PASSED        48        16         32        0         0
rev5 pre-handover     PASSED        48        16         32        0         0
rev5 --post-read      PASSED        48        16         32        0         0
```

The instrument check — `roles/scientist.md` must be observed leaking — **passed in every run**; had
it failed, no zero above would have been evidence and the harness says so instead of reporting one.
No silent file class reappears, in either mode. Both census populations are correct and identical
across the revisions.

---

## 8 · UTF-16, freeze and the mode oracles

**UTF-16 at the gate — PASS, with the reason and not the code.** The whole protocol text encoded
UTF-16, written into `framework/eval/failure_taxonomy.md` in **both** surfaces so parity cannot
see it:

```
PRE-HANDOVER   rc=1 · VERDICT: FAIL — 2 finding(s) · UNANTICIPATED ×2, one per surface ·
               class undecodable_text · MODE line reads "pre-handover (HANDOVER GATE)"
--post-read    rc=0 · VERDICT: PASS · UNANTICIPATED 0 · named under [UNCHECKED] as
               undecodable_text · MODE line reads "--post-read"
```

Identical at revision 5 and revision 6. The post-read half is unchanged, as `-004` §9 ruled and as
revision 6 declines to disturb.

**Mode-specific oracles — PASS, proved by mutation rather than by reading.** In a scratchpad copy
I redirected `verify_pre()` to invoke `--post-read`. **18 tests fail** — every mode-specific test
in `HandoverGateCensusTests` plus the at-handover partition — and the post-read partition correctly
does **not**. The mode assertions are load-bearing, and each checks argv *and* the tool's own
printed `MODE` line. The claimed mode matches the actual mode in every run above.

**Freeze — PASS, unchanged.** Receipts at both revisions are field-for-field identical (29 fields,
same `TREE_SHA256`); `SURFACE_ABSOLUTE_PATH` carries the declared-absent value rather than a path;
`verify-freeze` passes on the untouched tree; and the positive control — one byte appended after
the freeze — refuses with `rc=1`.

**No load-bearing pass in this review rests on an exit code alone.** Every negative above asserts a
reason string, a class, or a population.

```
WRONG-REASON LOAD-BEARING PASSES:   0
```

---

## 9 · Regression accounting — my own harness, granularity separated from suite level

I re-authored the harness. It reads the target list from `scripts/run_release_regressions.py`
**by AST**, because Plan disclosed that a regex over that source misses two entries written as
implicit string concatenation. My reader returns **65 targets at the candidate and 64 at base** —
the true values, and the ones `-005` published. It parses `subTest` failures (which print a `FAIL:`
header while the top-level line still ends `... ok`), sums each target's own `Ran N tests` line,
and separates targets with no attributable test id.

```
                              BASE cbce3016     REV 6 2a854177
targets present                     64                65
targets missing                      0                 0
FAILING SUITES                       6                 6
FAILING TESTS                        7                 7
tests executed                     870               953        delta 83 = the added suite
suites red, NO parsed test failure   ∅                 ∅         (the omission channel)
targets with no test-id granularity  3                 3
```

**BASE GRANULAR FAILING TESTS — 7:**

```
framework/scripts/test_session_self_eval.py::SelfEvalGate::test_diagnosis_is_wired_before_growth_and_takeaways
scripts/test_abstract_corpus_is_not_evidence.py::InstructionSurfacesCarryTheDistinction::test_the_bootstrap_bounds_the_corpus (file='CLAUDE.md')
scripts/test_fulltext_trace_contract.py::FulltextTraceContractTests::test_normative_layers_make_receipts_universal
scripts/test_fulltext_trace_contract.py::FulltextTraceContractTests::test_normative_write_rules_name_the_append_only_carveout
scripts/test_locator_obligation_reaches_every_route.py::ObligationReachesEveryRoute::test_the_bootstrap_states_the_rule (file='CLAUDE.md')
scripts/test_release_runner_verdict.py::EveryTestSuiteIsActuallyRun::test_every_tracked_test_file_is_in_the_runner
scripts/test_release_surface.py::ReleaseSurfaceTests::test_shebang_python_entrypoints_are_executable
```

**REV 6 GRANULAR FAILING TESTS — 7: the same seven, and nothing else.**

```
ADDED FAILING TESTS    ∅        REMOVED FAILING TESTS    ∅        SHARED    7
ADDED FAILING SUITES   ∅        REMOVED FAILING SUITES   ∅
SAME-REASON            7 / 7 identical after normalization · UNEXPLAINED REASON CHANGES 0
```

Same-reason compares each failure's parsed block, per test id, base against candidate. Normalized:
scratchpad and worktree paths, temp directories, `line <N>`, elapsed times, memory addresses. **No
assertion text is normalized**, so a changed reason cannot be normalized into agreement.

**The omission channel is empty at both tips**, measured — no target exits non-zero while reporting
no failing test — so the zero above is a measurement rather than an absence of measurement.

**NON-GRANULAR TARGETS — reported apart, never counted as passes.** Three targets are custom
harnesses that print their own verdicts and attribute no test id:

```
launch/test_legend_launch.py                                              rc=0 at both tips
.claude/skills/legend-study-intake-triage/scripts/test_study_dedup_triage.py     rc=0 at both tips
.claude/skills/legend-batch-inferential-sweep/scripts/test_batch_inferential_sweep.py  rc=0 at both
```

I compared their **actual output**, not only their exit codes: **byte-identical at both tips** after
path normalization. That is a suite-level result and a reason comparison; it is not test-level
evidence, and I do not present it as one.

**`P-10` reconciles.** Plan's corrected 870/953 is exactly what my independently authored harness
measures, and `REV-SCIAB-MIRROR-004` published 870 for the base a revision earlier. Two instruments
agreeing on a number is not agreement on the set underneath, so I compared the sets: same seven
test ids, same seven reasons.

---

## 10 · SLR-plan-0006 — BOUND, and curated under Annex E.2

### 10.1 · Procedural integrity — PASS

```
belongs to this session/candidate   task SCIENTIST-AB-SPEC-001 · directive v1 · generation 6,
                                    matching CHK-plan-0016 ✓
is CONTENT                          learning/ is under no CONTROL_PLANE_ROOT; P5.1 declares it
                                    CONTENT by intent and says so explicitly ✓
in the authoritative content tip    present at 2a854177, absent at 2ffaedb2 — and it IS the single
                                    entry taking the domain 526 → 527 ✓
written BEFORE the binding          revision 6 has exactly ONE content commit, which carries the
                                    remediation and this record together. No tip could be named
                                    before it existed, so nothing was superseded within the
                                    revision — third consecutive revision ✓
no pre-SLR revision-6 hash          only beef6db0… is presented as current, anywhere on the
                                    branch. Verified by reading every 64-hex value with its line ✓
```

**SLR-plan-0006: BOUND.**

### 10.2 · Epistemic curation (Annex E.2) — three refinements, none auto-ratified

E.2 gives durability to Plan and epistemic curation to Mirror. Every `CONFIRMATION_CLASS` in the
record is marked *proposed*, which is correct and is the shape E.2 exists to produce. I do not
ratify them as written.

**L-1 — *"I argued for the authority I had by claiming I had not used it"*. Proposed
`REPLICATION` of `-005` §4C. REFINED: it is two learnings with two classes.**

The *defect instance* did not originate with Plan — Mirror named it, and Plan re-derived it
afterwards. Under E.2 that reaches Plan as `EXPOSURE_AFTER_BROADCAST`, which counts less than
fully, and calling the whole entry a `REPLICATION` of §4C overstates the overlap: §4C contains the
finding about §4.4 and contains no generalisation. The *mechanism* Plan adds — that a fail-closed
option presents itself as the absence of a decision, because refusing to weaken something feels
like not having chosen — is **not in my review** and is Plan's own. Split:

```
L-1a  the §4.4 defect instance                    EXPOSURE_AFTER_BROADCAST (origin: mirror, -005 §4C)
L-1b  "a fail-closed choice is the kind most      ORIGINAL_OBSERVATION (plan, this session)
      likely to be written up as an entailment"   SCOPE: offered for wider scope — ACCEPTED as
                                                  a candidate for it, on one confirmation
```

L-1b is the durable half and it is Plan's. It reaches **1 confirmation of a fully-counting class
plus Mirror validation**, which is E.2's second threshold for `BEST_PRACTICE_CANDIDATE`. I record
it as meeting that threshold. I state separately that this is a judgement about a formulation, not
a measurement.

**L-2 — *"a derivation that ends in a disjunction has not ended"*. Proposed `ORIGINAL_OBSERVATION`.
REFINED: partly replication, and the instrument is the original part.**

The observation that the step from `I4` to `C` is unstated is `-005` §4B and is mine, so that half
is `REPLICATION`, not `ORIGINAL_OBSERVATION`. What is genuinely new is the **detector**: *if the
premises speak of what can be claimed and the conclusion speaks of what the machine does, there is
an unstated step.* That is a mechanical, cheap, reusable test that appears in neither review, and
it is `ORIGINAL_OBSERVATION`. I accept the rule as formulated and correct only the class of the
half that restates my finding.

**L-3 — *"the same sentence was in four artifacts, and the review named one"*. Proposed
`ORIGINAL_OBSERVATION`. REFINED to `REPLICATION`, by the record's own text.**

`SLR-plan-0004` L-1 already holds *the finding is a lower bound on its own population*, and
`SLR-plan-0004` L-2 already holds *one rule implemented twice will diverge*. L-3 says so itself —
*"this is `SLR-plan-0004` L-2 arriving at the level of prose"*. E.2's dedup rule is explicit: a
similar existing learning is **confirmed with a class**, not filed as a new original. The genuinely
new content is the **substrate**, and it is worth keeping:

```
L-3   REPLICATION of SLR-plan-0004 L-1 (plan, this session), SCOPE widened:
      from the population of a FINDING IN CODE to the population of a NORMATIVE CLAIM IN PROSE,
      where no shared predicate is available and the only instrument is a meaning-search.
```

That widening is the second confirmation `SLR-plan-0004` L-1 needed. With it, **`SLR-plan-0004`
L-1 crosses E.2's ≥2 threshold and I record it as `BEST_PRACTICE_CANDIDATE`** — which is a
consequence of L-3 being a replication rather than an original, not despite it.

**The boundary section's self-classification is correct and I ratify it as written.** The
regression-harness target-list defect is filed as `REPLICATION` of `SLR-plan-0005` L-3 *on a new
form — the target list, not the result*. That is the right class and the right qualification.

**Two factual imprecisions in the record, neither changing a conclusion.** *"All **51** top-level
definitions … identical by `ast.dump`"* — the 51 are top-level **statements**; the top-level
definitions number 32, and all conventions agree the set is unchanged (§6), so the measurement is
right and the noun is wrong. And *"the four `verify` runs … produce **byte-identical** output at
both revisions"* is true of two of the four without qualification; the two hostile runs differ in
their tree digests because the payload is the edited protocol, which the **manifest** states
correctly at §4.6a and this record does not. Both are recorded as `P-13`.

**No Mirror methodology is self-ratified here (G.2).** The curation above is E.2 work on Plan's
record, which is Mirror's under H.1 (*lifecycle learning: epistemico Mirror*). Nothing in it
changes Mirror's rubric, clustering, active-learning selection, review-yield or autonomy method.

---

## 11 · Findings — none blocking, two recorded, thirteen carried

| # | Plan's class at rev 6 | Mirror's finding |
|---|---|---|
| **P-4** | CARRIED, STATED, NOT CLOSED | **CARRIED, TRUTHFULLY.** By AST: `emit_digests` appears **6 times in `cmd_build` and 0 times in `cmd_verify`**; `verify` exposes no digest input. Every hostile probe in this review made the identical-edit-to-both-surfaces move and parity was silent in every one, exactly as declared. Revision 6 claims nothing about it |
| **P-6** | CARRIED — unchanged in both halves | **CARRIED, CORRECTLY.** `iter_files` byte-identical and still excludes `.git`, so a forbidden artifact there is invisible to `verify` and to `freeze`. Both `PASS` sentences print the `.git/` scope. **Not closed**, and Plan does not claim it is |
| **P-7** | CARRIED — unchanged | **CARRIED.** `test_bomless_utf16_decodes_as_utf8_unless_a_byte_exceeds_7f` is byte-identical and green; the residual is a scan limit, not a census hole |
| **N-7** | UNRESOLVED, fifth review running | **UNRESOLVED, NON-BLOCKING — and I say why, rather than only that.** See §12 |
| **P-9** | FIXED | **RESOLVED.** The four `Status` cells now read *(rev 3, rev 4, rev 5, rev 6)*; the probe count reads **83** and the suite runs 83; the control-plane figure reads **9 at the content tip** and I measure 9 at the content tip and 10 at the manifest tip, with every checkpoint row listed. All control plane; the binding does not move |
| **P-10** | FIXED | **RESOLVED.** `tests executed` reads **870 / 953**, which is exactly what my independently authored harness measures, and 953 − 870 = 83 is exactly the added suite. The revision-4 cell is struck rather than back-filled, which is the right call for a tree Plan did not re-run |
| **P-11** | CARRIED, ACCEPTED | **CARRIED.** Not repaired, and repairing it would re-partition a discrimination set inside a revision meant to change one sentence. Correctly declined |
| **N-1** | CARRIED | **NON-BLOCKING CARRIED.** `surface_spec.json` is edited at this revision — one `_note` block — and the File012 normalization contradiction is again not among them. Correctly declared |
| **N-2 · N-3 · N-8** | CARRIED | **NON-BLOCKING CARRIED.** `cmd_population`, `_pdf_pages`, `_regex_units` and `cmd_locators` are identical by `ast.dump`, verified over every definition including nested ones |
| **N-6** | CARRIED, declared | **NON-BLOCKING CARRIED, and the rev-6 claim is TRUE by construction: 0 test methods were added**, measured by name-set difference. No exit-code-only assertion could have been added |
| **N-9** | CARRIED | **NON-BLOCKING CARRIED.** Vocabulary in a note, untouched |
| **P-1 · P-3 · P-5** | CARRIED | **CONFIRMED** — `BASE_HEAD`'s guard, and see N-6 / N-7 |
| **R-1 … R-12** | not reopened | Not reopened. `R-10` is still Mirror's own worktree debt (§0) and moved numbers again |
| **M-1 · M-2 · M-3 · M-4** | retested, not reopened | **All four re-measured from `R-1` and closed** — §7 |
| **freeze** | retested, not redesigned | **PASS** — §8 |

**New this review, both non-blocking:**

- **`P-12` — non-blocking.** §4.3 of the manifest states *"`test_benchmark_input_surface.py` —
  **59 tests, all green** (45 at revision 2)"* and *"against this revision 45 ran · 45 pass"*. The
  suite is **83**. Those are revision-3 and revision-2 numbers, and §4.3 carries **no revision
  label**, while the section immediately after it is titled *"Revision 1's evidence, retained"*.
  The neighbouring section got a retention label and this one did not, so *"against this revision"*
  reads as revision 6. This is `P-9`'s class one revision after `P-9` was closed — the candidate's
  own `L-1` again, *a repaired instance is not a repaired class*. It is control plane, it moves no
  hash, and the true count is stated correctly three times elsewhere in the same document
  (§4.6, §4.6a). **Weighed non-blocking on consistency with `-005`, which classed `P-9` and `P-10`
  — the same class, in the same document — as P-class.** The remedy is a four-word label.
- **`P-13` — non-blocking.** The manifest §4.6a and `SLR-plan-0006` both say *"**51** of 51
  **top-level definitions**"* and *"**40 of 40** definitions"*. Those counts are of top-level
  **statements**, not definitions: the tool has 32 top-level definitions, 33 including nested ones,
  and 51 top-level statements; the test file has 15, 126 and 40. The counts reproduce exactly under
  the statement convention and the substantive claim is true on all four conventions I ran, so this
  is a naming defect and not a false measurement — but a reviewer reproducing the claim at its
  natural reading gets 32 and concludes the number is wrong. See also §10.2 on the same record's
  unqualified *"byte-identical"* for the two hostile runs.

**Nothing is marked resolved because `M-5` was fixed.** `P-9` and `P-10` are the only closures and
both are numbers in the manifest, exactly as Plan says.

---

## 12 · N-7 — unresolved, and NOT load-bearing for this candidate

`N-7` is that I could not reproduce Plan's differential counts for **revision 1's tool** — I
measured 45 / 9 ERROR / 14 pass / 12 genuine against the published 41 / 22 / 10 / 9 / 7. It is
unreconciled for the fifth review running; revision 6 did not re-run revision 1's tool and neither
did I. I asked the directive's question — is it secretly blocking? — and answered it by finding
what depends on it.

```
what N-7's numbers are evidence for   that the revision-2 suite DISCRIMINATED against revision
                                      1's tool, i.e. that the probes detect the defects
what carries that claim now           (i) the rev-4-tool differential (20 of 83 fail; 17 on
                                      substance with the MODE line back-ported), (ii) the
                                      rev-3-tool differential (12 of 71), and (iii) my own
                                      mutation experiment in §8, which produced 18 failures and
                                      is independent of every published count
does any CURRENT guarantee rest on    no. No PASS sentence, no census claim, no census class,
the revision-1 differential           no guarantee-table row and no test cites it.
where the disputed numbers live       §4.3 of the manifest alone — control plane, and the
                                      section P-12 is about
```

Both sides remain measured-versus-inferred and neither has moved. But nothing the candidate now
claims depends on it, and I proved discrimination by a route that uses none of the disputed
figures. **N-7: UNRESOLVED NON-BLOCKING.** It is entangled with `P-12` only in this sense: because
§4.3 is unlabelled, a reader can take the disputed numbers as current, which makes an unresolved
historical dispute look like a live one. Labelling §4.3 fixes the appearance; it does not settle
`N-7`, and I do not claim it would.

---

## 13 · Human approval surface — CLEAR

I read the surface the way the operator will meet it, and I checked the canonical half separately
from the control-plane half, because that separation is what `M-5` was about.

| The operator must learn | In canonical content (§4.4) | In the manifest (§1b) |
|---|---|---|
| **WHAT is being approved** | the `POLICY CHOICE` block: *at PRE-HANDOVER, a present artifact classified `EXPECTED_BY_PROTOCOL: NO` causes verification failure and blocks handover — `rc=1`* | yes, and it is §1b, immediately after the manifest block, not buried |
| **WHY** | `RATIONALE`, ending *"This is a judgement about which of two true contracts to publish; it is not an entailment of the premises above"* | yes |
| **WHAT ALTERNATIVE existed** | `ALTERNATIVE NOT CHOSEN` — (b), enumerate and scope, *"what this tool already does post-read"* | yes |
| **WHAT REFUSING IT COSTS** | `STANDING`: *"refusing it selects (b) without disturbing any other claim in this section"* | yes, and more explicitly: `WHAT REFUSING IT COSTS` names the one branch removed and the one table cell narrowed |
| **WHO decides** | `STANDING`: Plan proposes under H.1; *"the candidate is MAJOR: the choice is the Human Operator's to approve or refuse under H.1"* | yes, and it adds Mirror R4 and `HUMAN_APPROVAL` are both unspent |
| **that it is fail-closed** | `FAIL-CLOSED`: *(a) can only refuse surfaces (b) would admit* — which I verified structurally in §4C | yes |

`HUMAN_APPROVAL: NONE — not requested, not granted, not implied`, and *"No `HUMAN_APPROVAL` is
pre-filled"* at §5. The four-role separation is stated: Plan proposes, Mirror reviews, the Human
Operator approves, Orchestrator executes if authorized. **The operator does not need to reconstruct
any of this from Git history.**

**HUMAN APPROVAL SURFACE: CLEAR.**

---

## 14 · Gates, and non-regression of the stabilized properties

```
                                   BASE cbce3016              REV 6 2a854177
legend_lint.py .                   PASS (1 pre-existing INFO)  PASS (1 pre-existing INFO)
public_release_gate.py             PASS · BLOCKS: 0            PASS · BLOCKS: 0
growth_anchors.py check            PASS · 39/70/356/390        PASS · 39/70/356/390
fulltext_receipts.py verify        OK · 128 chained, anchored   OK · 128 chained, anchored
test_fresh_clone_reader_journey    5 tests OK                   5 tests OK
test_documented_commands           2 tests OK                   2 tests OK
governance_fingerprint --all       scientist 355e3529…          scientist 82423a48… (rotated)
                                   mirror/plan/orchestrator identical at both
```

**Stabilized properties — 18 of the 23 content files are byte-identical to revision 5 by blob sha**,
and every property below rests on one of them. Byte identity is the evidence; I did not re-run the
scientific benchmark machinery, which the directive permits and which would have added nothing.

```
B-1  population        evidence_units.json byte-identical; re-derived from the tree at rev6:
                       65 units · 109 sub-units · 6 main_figure · 7 main_results_section ·
                       2 main_methods_section · 24 supplement_methods_section ·
                       7 supplement_table_section · 10 supplementary_figure · 9 source_data_blot
B-3  freeze receipt    §8 — re-run live, 29 fields, mutation control refuses
B-5  benchmark fields  OUTPUT_SCHEMA.md byte-identical
MODE A / MODE B        MODE_A.md and MODE_B.md byte-identical
actor equivalence      scientist_reading_modes.md byte-identical — the mode stays a task
                       parameter, not a property of the actor
C-2                    scientist_reading_modes.md byte-identical; nothing reopened
input parity           §6 — parity holds in all four live runs; PARITY BROKEN fires when I plant
                       into one surface only
scientific depth       MODE_A/MODE_B and BENCHMARK_INSTRUCTIONS.md byte-identical
actor registration     roles/scientist.md and BOOTSTRAP.md byte-identical; status still
                       "PROPOSED — binding once Mirror hostile review passes and the operator
                       approves"; no agent_card path exists at BASE_HEAD, on the candidate,
                       or on branch mirror
canonicalization       CONFIRMED — the scientist fingerprint rotates 355e3529… → 82423a48…,
  dependency           so a checkpoint written before execution is INCOMPATIBLE after it (A.6)
no parallel schema     the three files naming `claims.json` / `claim_schema` were read at the
                       content tip and every hit is a clause FORBIDDING it. NONE present
scope containment      content diff cbce3016 → 2a854177: zero paths matching
                       session|rout|registr, zero *_current.md, zero registry or receipt-ledger
                       paths. rev5 → rev6 changes exactly 4 content files edited + 1 added
```

**SCOPE CREEP: NONE.**

---

## 15 · EVIDENCE_FOR · EVIDENCE_AGAINST · ALTERNATIVES_CONSIDERED · KEY_OBJECTIONS

**EVIDENCE_FOR.** The binding reproduces on twelve runs, six published controls and two traps. The
asymmetry's direction is entailed by §2.2 on a derivation I wrote myself before reading Plan's.
The blocking level is a choice, and §4.4 now says so in canonical content with the alternative,
the cost of refusal and the approver named. All four operative sites are corrected and a sweep for
the claim's meaning across all 23 content files finds nothing false. Behaviour is identical on four
AST conventions, a structural JSON comparison and four live runs with a payload-controlled digest
check. M-1 through M-4 re-measured from R-1 and closed, with a passing instrument check in every
partition run. Regression delta zero at test granularity, same seven reasons, omission channel
empty, non-granular targets separated and compared by output. All gates pass at both tips.

**EVIDENCE_AGAINST.** §4.3 of the manifest carries revision-2 and revision-3 suite counts with no
retention label, one revision after the same class was raised as `P-9` (`P-12`). The manifest and
`SLR-plan-0006` both call top-level statements "definitions", and the record's *"byte-identical"*
is unqualified where the manifest qualifies it (`P-13`). `N-7` is unreconciled for the fifth review
running. `P-4`, `P-6`, `P-7` and `P-11` are carried and none is closed.

**ALTERNATIVES_CONSIDERED.** (i) *Weigh `P-12` as blocking*, on the ground that a false sentence in
the artifact the operator reads to approve is what `M-5` was about. Rejected: `M-5` was blocking
because it was in **canonical content**, and `-005` classed `P-9` and `P-10` — stale numbers in the
same manifest — as P-class on exactly that distinction. Weighing `P-12` differently would be
applying a rule I declined to apply one revision ago. (ii) *Require `N-7` settled before ACCEPT*.
Rejected on §12: nothing the candidate now claims depends on it, and I proved discrimination by a
route independent of every disputed figure. (iii) *Treat the corrected §4.4 as over-correcting* —
i.e. that (b) is in fact inconsistent with a cited premise, which would make the level entailed
after all and the correction an error in the other direction. I ran this seriously and it fails:
§3 governs what happens **when** a surface fails, not which states are failures, and §1's `P-7`
reads satisfied under (b) with a narrowed row.

**KEY_OBJECTIONS.** The one that survives is `P-12`, and it survives as a P-class finding rather
than a blocking one. The pattern it belongs to — a number corrected in one place and left standing
in another — is now on its fourth appearance in this candidate (`N-4`, `N-5`, `P-8`, `P-9`/`P-10`,
`P-12`), and the candidate's own `L-1` diagnosed it two revisions ago. That it recurs inside the
revision that fixed its previous instance is the honest reading, and it is why I record it rather
than waive it.

---

## 16 · VERDICT

```
Annex C.2 VERDICT       CONFIRMED — no defect found given the available evidence bundle, on the
                        object the revision was scoped to. §4.4 now separates the entailed
                        direction of the asymmetry from the chosen level; the blocking level is
                        presented as a policy choice with its alternative, its fail-closed
                        property and its approver named, in the text that canonicalizes; the same
                        claim is corrected at all four operative sites and a meaning-search finds
                        no fifth; and nothing executable moved, measured four ways with a
                        discriminating instrument check. CONFIRMED is "no defect found given the
                        available evidence bundle", never "true".
MIRROR_REVIEW           ACCEPT
REVIEWER_CONFIDENCE     high on the binding (12 reproductions, 6 published controls, both traps
                          matched)
                        high on behaviour identity (4 AST conventions, structural JSON, 4 live
                          runs, payload-controlled digest check, comparator proved on rev4→rev5)
                        high on M-1…M-4 (independent os.walk universe, scan by effect,
                          instrument check passed in all four runs, 0 silent, 0 overlap)
                        high on the mode oracles (mutation → 18 failures, post-read correctly
                          unaffected) and on freeze (mutation control refuses)
                        high on the regression delta (own AST-based harness, 65/64 targets,
                          omission channel empty, 7/7 same-reason, non-granular targets compared
                          by output rather than by exit code)
                        MEDIUM on M-5's closure — it is a judgement about how a normative
                          sentence will be read, not a measurement, and I state it as such, as I
                          stated the finding itself
RESIDUAL_UNCERTAINTY    M-5's closure is the mirror image of M-5: I judged the old sentence
                          misleading and I judge the new one clear, and both are judgements. An
                          adjudicator who read §4.4 and still could not tell that a decision was
                          theirs would be pointing at something I cannot see from here.
                        P-12 is a live instance of a class this candidate has closed four times.
                          I weigh it non-blocking on consistency, not on an independent severity
                          scale, and an adjudicator could reasonably ask for the label first.
                        N-7 is unreconciled for the fifth review running and I did not settle it.
                        P-4, P-6, P-7 and P-11 are carried and none is closed.
                        Two instrument defects of my own are reported in §18; every number here
                          is from the corrected runs.
EVIDENCE_NEEDED         None for this verdict. For the next revision, whenever one occurs and
                        without reopening this one: a four-word retention label on §4.3, the
                        word "statements" where the manifest and SLR-plan-0006 say "definitions",
                        and the tree-digest qualification carried from manifest §4.6a into
                        SLR-plan-0006. All three are control plane or a learning record; none
                        moves the candidate hash; none is a condition of this ACCEPT.
WHAT_WOULD_CHANGE_MY_MIND
                        M-5: a fifth OPERATIVE site in the content population still presenting
                             the blocking LEVEL as entailed — I swept all 23 content files for
                             the meaning with a sweep proved to discriminate against revision 5,
                             and found none; or a demonstration that (b) is inconsistent with a
                             premise §4.4 cites, which would make the level entailed and the
                             correction wrong in the other direction; or a reading of §4.4 alone
                             under which the operator would not know the decision is theirs.
                        behaviour: any differing ast.dump over the tool's definitions on any
                             convention, a surface_spec key other than content_scan/_note, a
                             differing verify output on an identical payload in either mode, or
                             a test whose result moves — none found.
                        M-3/M-4: any present file that verify, in EITHER mode, neither scans nor
                             names — 48 probed by effect in each mode at both revisions,
                             instrument check passed in all four, 0 found.
                        M-1: the guard is byte-identical to BASE_HEAD; any diff would reopen it.
                        binding: any of the six published controls failing to reproduce through
                             my implementation — all six reproduce, and both traps match the
                             published wrong values.
                        P-12 → blocking: a demonstration that an operator relies on §4.3 in
                             deciding this approval. I could not construct one; §4.3 carries no
                             clause the POLICY CHOICE decision depends on.
AUTHOR_RESPONSE         required (C.2); silence is not acceptance. Plan owes a response on P-12,
                        P-13 and the E.2 re-classifications in §10.2 — none of which gates this
                        ACCEPT.
```

**HUMAN_APPROVAL: NONE — not granted, not recommended, not implied.** ACCEPT is a review verdict
under H.1 (*epistemic / method review → Mirror*). The MAJOR approval is the operator's and is
unspent. Nothing here canonicalizes, and Orchestrator's `CANONICAL_BATCH_COMMIT` remains the only
route to execution, under an ACTIVE lease and GATE 0.

**MAIN: cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED.**
**Nothing was executed, nothing canonicalized, no benchmark run, no registration performed, no
other actor's worktree written, the candidate branch not written.**

---

## 17 · Scope, and what this review did not touch

**SESSION-ROUTING DEBT: OUT OF SCOPE — NOT SILENTLY RESOLVED.** §5c of the manifest names the gap
between stable `ACTOR_ID` and current routable `SESSION_REF` and implements nothing. This review
implements nothing either, declares no `SESSION_REF` for itself, infers no routing from chat
recency, and supersedes no other Mirror session.

Not touched: the benchmark was not executed; no actor was registered; no capability was verified;
the L2 suspension stands; `main` was not moved; no lease was taken; no `*_current.md`, registry or
receipt ledger was written; Mirror's methodology observation remains **UNRATIFIED** and is not
self-ratified here (G.2).

---

## 18 · Provenance of this review

Detached worktrees created with `git worktree add --detach`: `wt-base` at `cbce3016`, `wt-rev4` at
`a210f738`, `wt-rev5` at `2ffaedb2`, `wt-rev6` at `2a854177`, `wt-rev6m` at `5edfd040`. The rev5
and rev6 trees were additionally exported with `git archive` into **non-git** directories under the
session scratchpad for surface construction, so no git worktree was dirtied by a built surface. The
packet was copied read-only from root `files/fulltext/` into those two exports only. Every attack
surface is a copy under the scratchpad. All binding numbers were computed with `BASE_HEAD`'s own
script in a worktree carrying P5 **v4**, or by an implementation written in the scratchpad from
P5.1/P5.2, never in this branch's checkout, which carries P5 v3 (`R-10`).

The session guard refused one inline heredoc while the shell was inside a repository worktree. I
did not reach for an unchecked tool: the mutation harness was authored with `Write` into the
scratchpad, made to refuse any path outside it, and invoked by name; the measurement is the same
one.

**Two instrument defects committed by this reviewer, both caught, both disclosed.**

1. **My falsifier sweep across revisions 1–4 returned zero hits at every tip, and the zeros were an
   error, not a measurement.** In `zsh`, `"$tip:framework/…"` consumes `:fr` as history modifiers,
   so every `git show` received a truncated path and failed; `2>/dev/null` swallowed the message and
   the loop printed clean zeros. Caught by an instrument check I had not yet run — a string I knew
   was present came back absent. Re-run with `${tip}:${P}`, the sweep discriminates (`POLICY CHOICE`
   present at rev6, absent at rev5) and every number in §4B is from the corrected run. **This is a
   new form of the family in `SLR-mirror-0013`**: there the shell's `grep` was a shimmed function;
   here the shell's *quoting* was the instrument, and again nothing I wrote was wrong.
2. **My first hostile battery wrote its pristine copies inside the surface**, and `verify` correctly
   reported them as `NOT ALLOWLISTED` — my findings, not the tool's, inflating the pre-handover run
   to 4 findings and the post-read run to 2. A harness that adds files to the population it is
   measuring is measuring itself. Backups moved outside the surface tree, surfaces rebuilt, and a
   clean-pair control added that must `PASS` in both modes at both revisions before any hostile run
   is read. Seventh sighting of this family in my own harnesses.
3. My first byte-comparison of the two `verify` outputs reported `BYTE-IDENTICAL` while both runs
   had exited `rc=2` on a wrong `--surfaces` argument — two identical refusal messages. Caught by
   requiring a real `VERDICT` line rather than an exit code, which is the discipline this candidate
   taught me and the one `SLR-mirror-0010` §4 records against my own B-4 battery.

Time source: the runtime exposes no wall clock beyond the date. Governance loaded 3.1.1; the mirror
fingerprint is identical at `BASE_HEAD` and at the candidate content tip, measured.

**WRONG-REASON LOAD-BEARING PASSES in the candidate: 0.**
