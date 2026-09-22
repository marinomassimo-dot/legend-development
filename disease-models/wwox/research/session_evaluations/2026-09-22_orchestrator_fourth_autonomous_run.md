# Session self-evaluation — Orchestrator, fourth autonomous run (2026-09-22)

**Scope:** from `f226955` to this commit. Four Scientist waves (N, O lost/returned; P, Q; R, S
running). Four landings. **The upgrade is the answer, not the promise of one** — this run ships
`framework/scripts/census_verify.py`, caused directly by the defect in §2.1.

---

## 1 · What the run actually established

| | |
|---|---|
| 🟢 **A therapeutic axis reopened** | Non-allele-specific WWOX upregulation was closed by an **unsourced, untagged** premise that collapsed a hedged disjunction. Withdrawn. The axis is live for the first time since 2026-07-09 |
| 🟢 **The empirical floor is `NEVER TESTED`** | No WWOX allele, any class, any species, has ever met an NMD reagent. Every count re-measured against the committed tree |
| 🟢 **A fifth way a query-zero lies** | A **reagent named only in Methods is invisible to `[All Fields]`** even with a flawless expansion. Miss rate in this gene: **100%** |
| 🟢 **The deletion is a packing lesion, not an active-site lesion** | >20 Å from the SDR tetrad; backbone admits local accommodation; six polar contacts lost |
| 🟢 **A valid discriminator for short in-frame deletions** | Span feasibility + register exposure + lost-contact inventory. ΔΔG and deleted-residue relSASA are **invalid**. Closes the gap `D-30`'s corollary opened |
| 🟡 **The unit ambiguity is bounded, not fatal** | `u` cancels; the ratio is degenerate; the defect is confined to the absolute axis at exactly 2× |

## 2 · ATTRIBUTION_CENSUS

```
ATTRIBUTION_CENSUS
incidents: 8
machine: 1   blind_auditor: 0   peer: 1   self: 6
severity_high: 2   of which self: 2
undetected_known: 2
```

**Counting, so the numbers can be argued with.**

`machine: 1` — the publication gate refusing `nascimento_supplement_retrieval:337` on a broken
markdown link.

`peer: 1` — Scientist O's arithmetic establishing that `u` cancels from the dose ratio, against my
own written framing that the ambiguity *was* the effect.

`self: 6` —
1. 🔴 **§2.1 below** — verifying a census on a contaminated tree, twice.
2. 🔴 **The metric ambiguity** — reporting "every count is exact" without saying that `78` and `22`
   are **line** counts; as occurrence counts they are `91` and `27`.
3. The *"unit ambiguity is the size of the effect"* category error (`D-33`, withdrawn).
4. The journal-name sweep that reported itself complete after grepping **abbreviations only**,
   leaving every long-form spelling alive — **in the three highest-authority files**. Third wrong
   count on one defect.
5. Sketching a register-shift catastrophe for `p.Gln353_Gln354del` before measuring the span test
   that refutes it. Caught by my own next command, but I had already written the wrong mechanism.
6. `claim_registry`'s `Last update` line, unbumped since 2026-07-25 across three batches **including
   my own seizure propagation this morning** — found only because this batch touched the same line.

`severity_high: 2`, both self — (1) and (2). Either could have caused a correct delegate census to
be discarded, or an incorrect one to be landed.

`undetected_known: 2` — the metric ambiguity was invisible until the new tool printed both columns;
the `Last update` convention defect is **recorded and deliberately unrepaired** (§4).

### 2.1 The defect that earned the tool

A delegate census asserted eleven reagent terms absent from the repository. I verified by grepping
the working tree — **which by then held the delegate's own 474-line census, naming all eleven.** The
re-count came back non-zero and the census looked wrong. **It was not wrong.** I then reached for
`grep --exclude`, which **this deployment's grep silently ignores**, and reproduced the same false
mismatch. Only counting at the committed tree resolved it: **11/11 exact.**

Two failure modes, one root cause — **the surface I verified on was not the surface the claim was
made about.** The same shape as the base64 false-positive trap found earlier this session: the
search surface silently included something that was not evidence.

🔴 **And the near-miss is the real lesson.** My standing rule is *never trust a delegate census
without a repository check*. That rule, executed literally, was about to convict a correct delegate.
**The check needs a defined surface, or it is worse than no check** — it converts a good delegate
into a discarded one with the full confidence of having verified.

## 3 · The upgrade shipped

`framework/scripts/census_verify.py` — measures claimed counts **at a git ref**, prints the
working-tree count beside it, and **names the files responsible** for any difference.

- **12 tests** (`test_census_verify.py`), including `test_the_real_2026_09_22_contamination_is_caught`
  reproducing the incident verbatim, each contamination case **paired with the clean case it must
  not flag**, and the `ASE` substring trap (8,842 → 0 under `-w`).
- **Mutation-tested three ways:** contamination detection disabled → **2 failures**; `lines` metric
  made identical to `occurrences` → **1**; `parse_claim` splitting on the first `=` → **1**.
- Routed in `framework/scripts/README.md` § 4; `scripts/test_tool_routing.py` **7/7 OK**.
- 🟢 **It found a second defect the moment it ran on the real case** — that "count" is ambiguous
  between lines and occurrences, and that my verification had silently compared the wrong quantity.
  That is `self: 2` above, and it is the argument for building the instrument rather than writing
  the lesson down.

**§26 compliance:** this is a **measurement instrument**, not a gate, authority, auditor, registry or
workflow. It authorises nothing and blocks nothing; a non-zero exit is a finding for a human to read.

## 4 · What I deliberately did NOT do

- **No broad repair campaign.** `claim_registry`'s stale `Last update` convention spans at least
  three batches and every registry. **Recorded in the batch note, not fixed** — repairing it is a
  campaign, and the Operator's bound is *repair only what current scientific work directly depends on*.
- **No canonical propagation of the reopened axis.** `CC-20260922-NMD-PREMISE-WITHDRAWAL-01` and
  `CC-20260922-CLAIM011-DOSE-ENDPOINTS-01` are both **gated**: non-zero scientific deltas on canonical
  surfaces, outside the current authorization's scope.
- **No MD run.** No engine in this deployment — recorded blocked, **not retried** (§27).
- **No re-litigation of `DL-MECH-045`'s verdict.** Its verdict is **upheld**; only its mechanism is
  withdrawn. Being right for the wrong reason is not an error to reverse.

## 5 · The rule this run adds

> **A verification needs a defined surface before it needs rigour.** Name the ref, name the metric,
> and name what is in the tree that was not in the claim — otherwise a correct result and a
> contaminated one are indistinguishable, and the check's confidence is borrowed from nothing.

Corollary, learned twice today: **a sweep is not finished when it returns. It is finished when the
term has been enumerated in every spelling it has** — abbreviation *and* long form, line *and*
occurrence.
