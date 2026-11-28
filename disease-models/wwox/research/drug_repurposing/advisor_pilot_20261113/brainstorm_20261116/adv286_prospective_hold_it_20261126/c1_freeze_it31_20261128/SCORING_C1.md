# ADV-286 C1: arms, scoring and abstention rule (frozen with the questions)

Hypothesis level; reference genotype class only; nothing here is medical advice. Prospective only if the retrieved
document prints a date after the freeze; otherwise the entry is UNRESOLVED. One event, six questions: descriptive.

## Arms
| Arm | Input | Rule |
|---|---|---|
| ENGINE | `QUESTIONS_C1.md`, `INPUT_PACKET_C1.md`, the repository | free to reason; one reason per answer |
| B0 textbook pairing | `QUESTIONS_C1.md` only | general knowledge; no repository read, no search, no tool call |
| B1 abstain | none | ABSTAIN on all |
| B2 first option | none | option (a) on all |
| B3 and B4 | none | no question asks a direction and no held row measures any of the six in the same system: the same ABSTAIN-all as B1, reported as one arm with B1 |

The design note (section 2) gives every arm the same packet; B0's own rule excludes the repository, so B0 gets the
question file alone: a stated deviation. A delegate may still carry project instructions and a memory index at start,
so B0 is "no repository read in this task", not memory-free. ENGINE holds the whole repository, Kv7 material included.

## Scoring
* Per question and arm: MATCH, MISS, ABSTAINED (counted apart, never a hit) or UNRESOLVABLE (dropped for all arms).
* A question on which B2 or B3 matches is SATURATED: it cannot rank ENGINE above a null. For Q4 to Q6 option (a) is
  the default of the scorer, so saturation is expected there.
* Q5 and Q6 are UNRESOLVABLE whenever Q1 is.
* Report counts with denominators per arm. No percentage of skill, no probability, no claim that the engine predicts.
* Whoever opens the poster scores and does not edit any answer. A poster with an ambiguous reading: record both
  readings, UNRESOLVABLE if they differ.
