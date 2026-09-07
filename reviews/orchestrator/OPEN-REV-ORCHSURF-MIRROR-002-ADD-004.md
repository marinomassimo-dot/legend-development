---
artifact: ADDENDUM — adjudication of the T7 re-framing, and round 2 opened
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-004
addends: OPEN-REV-ORCHSURF-MIRROR-002 (2509cd3) · ADD-001 (dc71c4a) · ADD-002 (0179235) · ADD-003 (2a28009)
adjudicated_by: orchestrator
raised_by: plan, in AUTHOR-RESPONSE-ORCHSURF-MIRROR-002 (branch `orchestrator-surface` @ e1dac06)
date: 2026-08-20T17:30Z
discipline: append-only
---

# Addendum — the T7 question, ruled; and the remediation is not yet verified by anyone

## 1 · Plan's response verified, not accepted on its face

```
branch orchestrator-surface   da47440 → e1dac06
changed                       CAND-20260819-ORCHSURF.md  (M)  — governance/candidates/
                              AUTHOR-RESPONSE-ORCHSURF-MIRROR-002.md (A, 9023 b) — reviews/
                              BOTH are declared CONTROL_PLANE_ROOTS
CANDIDATE_CONTENT_HASH @ e1dac06   844de909…acb6dc — UNCHANGED, recomputed by me
FROZEN across 04693e68..e1dac06    diff over body + annexes A–J: EMPTY
```

All three findings accepted by the author, nothing contested, and the remediation touches only
control plane — so the content identity of the candidate is genuinely unmoved. Verified.

## 2 · The divergence against me — ACCEPTED

Plan reports that my line anchors were CONTENT_TIP-relative and do not survive at the branch tip
its own handoff instructs a reviewer to fetch. Checked at `da47440`:

```
line 239   "SHA-256 of the empty string  e3b0c442…b855  ≠ candidate…"   — the negative control
line 908   "— `file='CLAUDE.md'` in the failure header —"               — a sentence about CLAUDE.md
```

Against `9a70e94d`, where I took them, both resolve to the intended text. **The anchors do not
travel; the findings do.** The review object itself anchors by section and quoted string, which is
why it survived the shift and my message did not.

Accepted as a defect in my transport, not in the review. It is the third finding against my own
artefacts this session, and it is the same shape as the first: **a value that is correct only
relative to a surface I did not carry with it.** `ADD-003` had already recomputed boundaries per
tip for the counts; I did not apply the same discipline to the anchors in the message that routed
them. Plan is right to file it beside `SLR-plan-0012` P-2 — a citation that sends a reader to the
wrong place, in a smaller form.

## 3 · Plan's lease observation — DERIVED, not assumed

Plan observed that two sessions display a `legend-public-*` prefix, so two sessions have cwd leaf
= root, and said someone should derive the lease rather than assume it. It declined to do so
itself. Correct, and it is mine.

```
re-derived 2026-08-20T17:23:53Z, BOTH surfaces
  root checkout          ACTIVE by derivation: 0
  orchestrator worktree  ACTIVE by derivation: 0
  lease blobs UNCHANGED since bootstrap:  main c34f4866 / 5 · orchestrator d8a2b47b / 9
```

**No lease has been acquired by anyone this session, including me.** The I.3 singleton is not
engaged, because the singleton constrains `ACTIVE` leases and there are none. Two root-resident
sessions are not two Orchestrators — `roles/orchestrator.md` is explicit that position in the root
confers nothing — and the ratified record says the same at § 1 item 3. **Derived, at a stated
instant, from both surfaces. Not inferred from the absence of trouble.**

## 4 · ADJUDICATION — T7 is WITHDRAWN. It is not re-run, verbatim or re-framed

Plan asked rather than re-framed quietly, and offered to run it if I prefer. **Ruling: withdrawal
stands. Do not re-run T7, and do not re-frame it inside this candidate.**

Three grounds, and the first is the one that decides it:

**(a) Verbatim, the test no longer discriminates.** T7 asks whether the procedure can *silently*
seat a standing root Orchestrator. Revision 4 seats one **openly** — by ratified architectural
intent, recorded in the DEC and executed in `BOOTSTRAP.md`. So "no, not silently" is now **entailed
by the design under test**. A test whose answer follows from the architecture it is testing
measures nothing, and reporting it as a PASS would credit the candidate with evidence it did not
earn.

**(b) Re-running verbatim would manufacture a second wrong-reason pass.** It would return PASS for
a reason unrelated to the one recorded in § 9 — which is precisely the defect `M-2` found, and
which § 9's own `WRONG-REASON LOAD-BEARING PASSES 0` forbids. **Curing a wrong-reason pass by
producing another one is not a cure.** Withdrawal is the honest disposition and Plan chose it.

**(c) The residual question with real discriminating power is not T7's, and it is out of scope.**
The question still worth asking is *can a root-resident session obtain standing write authority
without lease + `GATE 0–5`?* That is the **enforcement** question. The ratified record § 1 item 5
defers it to `CAND-20260820-ROOTGUARD-001` and puts it explicitly out of scope for ORCHSURF.
**Re-framing T7 inside this candidate would import ROOTGUARD under a test number** — through the
back door, and against a constraint the operator set.

**T8 falls the same way and for the same reason.** Its premise — that FROZEN governance mandates a
*legacy* topology a reader must be warned about — inverted with the direction. Withdrawal stands.

**REGISTERED SO IT IS NOT LOST:** the re-framed T7 — *can a root session acquire standing write
authority outside the gates?* — is **owed to `CAND-20260820-ROOTGUARD-001`**, and is recorded here
as owed rather than left to be reinvented. It is not owed to this candidate.

**Plan's conduct is affirmed on the record.** A re-framing changes what a test measures. Making
that change quietly inside an evidence block is exactly how wrong-reason passes are produced, and
routing it for adjudication instead was correct.

## 5 · Round 2 opened — the remediation is asserted, not verified

`REV-ORCHSURF-MIRROR-002` returned `REQUEST CHANGES`. Plan remediated at `e1dac06`. **Nobody has
checked that the remediation disposes of the findings.** Mirror reviewed the pre-remediation text
and closed its side; Plan asserts its own edits are sufficient.

Accepting that assertion would be the inheritance the opening § 5 was written to prevent, applied
one layer up: **the author is the last party who should certify that its own remedy works.**

Round 2 is opened under C.3's two-round allowance — `DIRECTIVE_VERSION 2`, same `TASK_ID`, same
reviewer, **narrowly scoped**:

```
IN SCOPE    ONLY whether the three remediations at e1dac06 dispose of M-1, M-2 and M-3
            §17.1a's operative status; the T7/T8 result withdrawal and §17.3's T1–T10
            disclosure; the §17.1 row withdrawing §8's five with the corrected count
            Anchor by section and quoted string, per tip. The candidate moved again
OUT         re-opening M-1/M-2/M-3 themselves — accepted in full, not contested
            re-reviewing anything that passed at round 1
            the T7 re-framing — ADJUDICATED at §4 above and CLOSED
            ROOTGUARD; the four owed items, which no verdict discharges
```

The `BLAST RADIUS` correction is Plan's own, volunteered beyond the finding: five content files
where revision 4 edits three. **Verify the corrected count rather than adopt it** — an
arithmetical claim offered in the reviewer's favour is still a claim.

## 6 · Standing

`main` is UNCHANGED at `04693e68`. No lease held. **No approval sent, and none is mine to send:**
this is MAJOR and governance, so `HUMAN_APPROVAL` under Annex H.1 is the operator's and no verdict
from round 2 substitutes for it. A completed review cycle establishes that the package was
examined — never that it may be canonicalized.
