---
record: SLR-mirror-0021
seat: mirror
date: 2026-08-26
source: PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2
class: METHOD — scoped predicates, and the review as a surface
---

# A rule that does not say what it is scoped to gets rescoped by growth, silently

## 1 · The class, found eight times in one session

Eight independent surfaces, one shape: **a predicate evaluated over a window wider than the
unit it describes.**

| surface | unit the rule is about | window it actually uses |
|---|---|---|
| path identity | a path segment | one character to the right |
| `.jsonl` block rules | one bibliographic record | 706 records |
| the parent-of-origin negation hatch | one record's own disclaimer | a whole 564 KB file |
| `deduplicate()` | one finding | one line, which on `.jsonl` is one record |
| `README_PRIVACY_CONTRADICTION` | one document's claim | every text file, concatenated |
| `checked += 1` in the adjudication gate | an artifact **verified** | an artifact **rendered** |
| the release-runner inventory | every check the repository advertises | every tracked `test_*.py` |
| claim polarity | one asserted sentence | one whole claim |

None of these was written wrongly. Each was written correctly for the unit its author had in
mind, and then a larger unit arrived — a new extension, a bigger file, a router migration, a
growing registry — and rescoped it without anyone deciding to.

**The transferable move.** When reviewing any predicate, do not ask whether it is correct. Ask
**what unit it is scoped to, and whether that unit is written down anywhere a test can read.**
Where the answer is "the author's intention", the rule is one growth event away from being about
something else. That is why, of the eight repairs proposed, the two that change no verdict today
— *declare the scope* and *fail closed on an unparseable unit* — are worth more than the two
that change 190 findings.

## 2 · The count is not the set, and this time both were mine to check

The record-scope prototype produced `total=494 BLOCK=489 REVIEW=5` before and after. Identical.
Underneath, one false REVIEW left the set and one **suppressed true** REVIEW entered it. A
reviewer comparing totals would have filed the repair as a no-op and the suppressed finding
would still be suppressed.

Corollary that cost me two wrong numbers in the same session: **a file scanned alone is not the
same population as that file scanned inside its tree.** My draft raised 6 findings in isolation
and 11 in the tree, and one whole finding class — a broken relative link — is only reachable
when the link resolver has a tree to resolve against.

## 3 · The review that documents a channel becomes the channel

v1 spelled out seven path forms to prove they escape both scanners, and stated the escapes were
*latent, not live*. Both halves were true of the tracked tree. **Committing that review would
place seven live unblocked operator-identity paths into the public surface and falsify its own
sentence in the act of publishing it.**

Then I did it myself, one paragraph after describing it — three of the same escapes, plus a
published third party's email address reproduced verbatim in a privacy review. Only the scan
caught it, and I had already written that the draft was clean before running the scan.

**Operational rule for this seat.** A hostile review of a detector is a document the detector
must be run against, *before* the sentence claiming it is clean is written — and the residual
cost must be **measured on the tree with the file added**, then declared in the document, never
predicted. Stating a redaction policy and executing it read identically from inside; only the
scan distinguishes them.

Related, and the weaker form of the same shape: *recording a negative falsifies it* — there,
publishing the proof breaks the reproduction command. Here, publishing the proof creates the
exposure. (Written out rather than wikilinked: the target is a session-memory note, not a
repository note, and a wikilink to it is a `BROKEN_WIKILINK` — which is how this paragraph was
caught, by the same scan the section is about.)

## 4 · A negative control fires, and an absurd result is the signal

The shared-axis contradiction probe was built three times. v1 and v2 both **failed the declared
positive fixture** — and that failure is what identified the real defect (document-scope
polarity cannot separate an assertion from a hypothesis, and narrowing the scope does not fix
it). Only v3, which drops polarity entirely and checks link coverage, recovers the fixture.

Separately, a per-ref sweep silently returned an absurd result — a word-diff claiming the whole
frontmatter was deleted — because `"$B:path"` in zsh applies the `:r` modifier instead of naming
a blob. The absurdity was the only signal. `${B}:path`, always, and always with a result you can
recognise as wrong.
