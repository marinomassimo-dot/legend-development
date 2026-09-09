# SLR-scientist-b-0003 — wave 2 of `AQEILAN-FT-B-001`, PMID 18674750

**Written before the capability scout and before the closing report**, per
`session_self_evaluation.md`: takeaways written first describe a session that went well.

## Part 1 — the executable gate, run before any of this was written

| Check | Result |
|---|---|
| `session_self_eval.py --disease wwox` | **PASS** — 138 receipts · 70 complete events · 59 active complete reads · unread premises **4/4, this batch added none** |
| `deepdive_manifest.py --pmid 18674750 --verify-artifacts --require-current-schema` | **PASS, 0 gaps**, 41 locators / 12 artifacts (the prior manifest passed with 1 gap) |
| `fulltext_receipts.py verify` | **OK**, 138 chained, tail anchored |
| `legend_lint.py .` | `BLOCK_BATCH_COMMIT` — **peer-caused** (`FTR-20260909-33916893-01` declares a commit candidate not yet written); my own four `WARN_BUT_PROCEED` queue warnings were mine and are fixed |
| `test_deepdive_manifest.py` | 90 green before the upgrade → **92 green** after |

None of the `[DECLARED GAP]` lines belongs to this reading.

## Part 2 — the judgement, and where it is bad

### The three things that went right, stated first so the rest is not read as false modesty

1. **The digest discipline held under a real test.** All 13 pre-existing body locators were
   re-verified character-for-character against the new deposit (13 exact, 0 miss) and all three
   main figures re-opened **before** any digest changed. This is wave 1's lesson applied, not
   rediscovered.
2. **The Figure 2 correction was made to the right standard.** I contradicted my own prior locator
   only after measuring marker centroids at native resolution *and* corroborating the calibration
   against an author-published number — Table 2's effect sizes, which the four measured separations
   reproduce to two decimals. An external number is a stronger check than my eye, and it is the one
   that was applied.
3. **A guess was retired rather than inherited.** Ref 47 was resolved from its own DOI to
   PMID 17360458, **not** the PMID 18487609 the prior reading had guessed.

### 🔴 The three process failures, with attribution to whoever actually caught them

**F1 · I asserted a structural fact from indirect evidence, and only checking saved it.**
Reading per-page text lengths, I concluded and wrote that *"the supplementary figures are not in
this PDF — only legends"*. `pdfimages -list` then showed **16 image XObjects on pages 4–7**. The
figures were there all along, sliced into strips by Word→PDF. **Caught by: me, one step later, and
only because I ran the check instead of proceeding.** Had I not, the coverage map would have
recorded `captions_only` for the supplement and the entire debt this wave exists to pay would have
been declared unpayable. Distance from a false negative: one command.

**F2 · The validator caught my locator modelling, and I had read the rule this same session.**
Five coupled locators carried `panel_qualifies_text` / `text_contradicted_by_panel` on the **text**
side. `fulltext_read_receipt.md` open item 4 — which I read in full, today, before starting — says
in terms that *"the marker belongs to the PANEL locator — the evidence that makes the assertion."*
I read it, agreed with it, and then did the opposite on first draft. **Caught by:
`deepdive_manifest.py`, not by me.** The correction produced genuinely better structure: the Table S2
defect is now three locators (extracted row · Results sentence · pixel adjudication) exactly as that
open item prescribes. **Reading a rule is not the same as having applied it, and this is the second
consecutive wave in which a check, not the reader, enforced a rule the reader had just read.**

**F3 · A manifest passed STRICT while naming four queue IDs that belong to other entries.**
I minted `FT-072`–`FT-075` for new multihop hops. All four are **live entries about unrelated
papers**; `FT-071` is in fact this paper's own existing entry. I caught it only because I
independently grepped the queue before writing the queue file — **after** the manifest had already
validated PASS with the wrong IDs. **Nothing in `deepdive_manifest.py` checks that a
`multihop.queued[].queue` identifier exists or names the same PMID**, so a manifest can point at
another paper's debt and every gate stays green. Corrected to `FT-079`–`FT-082`.

### What I did NOT do, said plainly

- **The second paper of this wave, PMID 38499540, was not started.** See the closing report; this is
  a context judgement, not an omission I am hiding.
- **`legend-locator-audit` was not run.** The threshold was evaluated and did not fire, and the
  check is recorded in the manifest's `skills_considered` so the non-trigger is auditable. I note
  against myself that F2 is an argument for running it anyway when a wave contradicts its own prior
  locators — the audit would not have caught F2, but the reflex to seek external review would have.
- **One red is left standing deliberately.** `test_batch_queue`'s
  `test_coverage_is_not_overstated_against_the_registry` reports 68 against 67, because six studies
  now carry a complete receipt with **no** `paper_registry` record (`18674750`, `21212533`,
  `30470736`, `38355659`, `42082822`, `42397075`) — two of them mine. Only a `BATCH_COMMIT` can
  clear it and that is reserved. Named in its commit message rather than left as an anonymous red.

## Part 3 — the micro-upgrade, shipped

**Shipped, with regressions:** the printable-substitution screen in `deepdive_manifest.py` now knows
the Elsevier/LiveCycle table — `¼` for `=` and the digit `3` for `×`. The gap was **measured, both
branches executed**: as extracted the surface is refused by the C0 check; with the controls stripped,
exactly as a repair does, it was **accepted** while 65 `¼`-for-`=` and 12 digit-3-for-`×` survived,
and suspicion-by-absence could not catch it because the text still held 5 `<` and 9 `>` from
`p < 0.05`. Two patterns, two tests — one asserting refusal, one asserting the patterns do **not**
fire on ordinary prose, because a pattern that refuses good surfaces is a defect and not a stricter
guard. 90 → 92 green; all 15 local text surfaces still accepted.

**Registered and deliberately not built: the F3 check.** A `multihop.queued[].queue` cross-check
against `full_text_queue_current.md` would close it, and it is small. I did not build it, and the
reason is not that it is hard: I had already shipped one upgrade with its regressions, and a second
validator change written at the end of a long wave is exactly the kind of change that gets its tests
written to match whatever it does. **One upgrade with real regression evidence is worth more than
two rushed ones.** The measurement is preserved above so the next actor inherits the evidence and not
a recollection of it.

## Grade

**Content: strong.** A declared debt paid, its own description corrected, two self-corrections made
by measurement, a published data defect adjudicated on the page, an undisclosed experimental arm
found, and a guess retired.

**Process: adequate, not good.** Two of the three failures above were caught by a machine or by a
check I nearly skipped, and only one by judgement. The gap between *having read a rule today* and
*having applied it* is the finding I most want the next wave to carry.
