# ADV-286 design note: a prospective hold of engine against simple baselines (IT28, 2026-11-26; draft before any freeze)

Hypothesis level; reference genotype class only; nothing here is medical advice. No prediction is made in this note
and nothing is frozen by it. Recipient of decisions: ADV. Dates in the assignment: start by 2026-12-01, freeze by
2026-12-04, AES poster 1.019 on 2026-12-05, Table EV1 or E-MTAB-14792 re-check not before 2026-12-06.

## 1. Candidate events (step 1, first pass)

A candidate needs three things together: a source that can be retrieved by a plain request, independent biological
units, and a real choice the prediction would inform.

| Id | Event | What would be revealed | Independent units | Choice informed | Duplicate | Standing on 2026-11-26 |
|---|---|---|---|---|---|---|
| C1 | AES poster 1.019, 2026-12-05 (RP-042) | population, intervention, model and age, per-animal EEG measure, comparators, none of them guaranteed | unknown; possibly animals | whether INV-15 reopens at level 1, 2 or 3 | none with P-SCI-1 or ADV-175 | retrievability UNKNOWN: a poster, unlike an abstract, is usually not public by plain request |
| C2 | Table EV1 or E-MTAB-14792 (RP-043) | per-line organoid values | two lines per genotype; effective n of 1 for a genotype claim | whether the WOREE-over-SCAR12 week-16 contrast stays an input | the event-rate ordering duplicates P-SCI-1 | no release date exists, only a re-check date: not a dated external release |
| C3 | a private repository record with a printed release date, named in a held source | expression or other deposited data | depends on the record | depends on the record | none | none found: the twelve highest-numbered GEO series accessions named in held texts all read "Public" (plain requests, 2026-11-26: GSE328363, 328222, 328221, 328220, 327486, 327470, 317932, 314177, 313678, 300694, 293769, 292221). ArrayExpress and BioStudies: E-MTAB-14792 returns "Study not accessible" on the BioStudies API (plain request, 2026-11-26), no release date printed; it is the same item as C2. Recipe (dated 2026-11-26, to be repeated on 2026-11-30): for each GEO series or E-MTAB accession named in a held full text, request the public status page or API with a plain request, record status and any printed release date; a candidate needs a status other than "Public" AND a date; the held-text list was built by a content search of the held full texts for accession patterns. Result so far: no such candidate besides C2 |

First-pass reading: C1 is the only candidate with a date, and it may never be retrievable; C2 is not dated and its main
quantity is already frozen. Unless a further candidate appears before 2026-12-01, RP-005 is likely to stay parked, with
the failing condition stated per candidate. A freeze for C1 is still cheap and is worth doing: if the poster is never
retrieved the item closes as UNRESOLVED, which is not a score.

### Decision date (ADV, 2026-11-26)
If C1 and C2 are both unretrievable or undated, IT says so on **2026-11-30 at the latest** (not on 12-01) and the fallback is the **retrospective-hold design**: answers are frozen by hash for questions whose answer already exists in a held source that no arm has been given, so the hold is a date-blinded one rather than a time-forward one; freeze by 2026-12-04; scoring as in section 4; the weaker status is stated in the entry ("retrospective hold, not a prospective test"). Scoring is descriptive in both designs.

## 2. Arms

Every arm receives the same input packet (held sources and the portfolio rows named in it), hashed before use, and
answers the same frozen questions in the same format: for each question one of {increase, decrease, no change, present,
absent, a rank order, ABSTAIN with the missing datum named}.

| Arm | Rule |
|---|---|
| ENGINE | an agent with the repository materials, free to reason |
| B0 textbook pairing | the class-level expectation for the lever and phenotype, written from general knowledge, without the repository |
| B1 always abstain | ABSTAIN everywhere |
| B2 first option | the first option listed in the question |
| B3 direction only | the sign implied by the stated direction of the nearest held measurement, ignoring system and age |
| B4 evidence only | only what a held row measures in the same system and endpoint; otherwise ABSTAIN |

ENGINE and B0 each need their own context. Running them as delegates is beyond nothing already allowed for one delegate
at a time, but ADV is told before any dispatch, as the assignment asks.

## 3. Hold and freeze

* Freeze: no later than 2026-12-04T23:59Z for C1. Files: input packet, question list, every arm's answers, scoring rule.
  One sha256 per file, a commit landed on `development/main`, and a prediction-ledger entry with weight zero in the
  ranking, falsification only.
* Nobody who writes an arm's answers has seen the outcome. Whoever opens the poster scores; they do not edit answers.
* Nothing frozen under RP-045 is touched, and the sealed ADV-174/175 material is not opened.

## 4. Scoring

Per question: MATCH, MISS, ABSTAINED (counted apart, never a hit), UNRESOLVABLE (the release does not answer it;
dropped for every arm). A question where B2 or B3 matches is marked SATURATED: it cannot rank an engine above a null
(the ADV-197 lesson). With one event and very few units the result is descriptive: no percentage of skill, no
probability, no claim that the engine predicts.

## 5. Comparator-completeness metric

Applies to the engine's written reasoning, independently of the release, so it can be scored even if C1 never resolves.

1. **Mechanical share.** Every fold, ratio, range, "higher", "lower", "only" or "largest" statement that refers to a held
   source table is listed. A statement is complete if it uses every row of that table for that measure (all arms,
   groups, ages, units). The share of complete statements is reported with numerator and denominator. The one-line
   baseline "print all rows before any fold" scores 100 percent by construction, so this share is a conformance floor:
   below 100 percent the engine is worse than one line of instruction.
2. **Blind-check share.** The same statements go to a blind reader with the whole source table, graded MUST CHANGE, ADD or
   STANDS. The reference bar is ADV's figure of 25 to 45 percent of agent-written consumer sentences needing a change,
   from five samples. Pass: the MUST CHANGE share of the engine's statements is below 25 percent, on at least 30
   statements; with fewer than 30 the count is reported and no pass or fail is declared.
**Which band applies (ADV, 2026-11-26).** Two reference bands exist and they are not interchangeable. (a) First-draft consumer sentences, before any wording rule or correction round: 25 to 45 percent need a change (five earlier samples; IT28 first round 10 of 24 = 42 percent, and 4 of 4 blocks in the ADV-285/288 consumers needed a wording change). (b) Cards after a wording rule and a correction round: 8 to 14 percent (SCI's ADV-287 extension: 4 of 49 assessable verified, 7 of 50 with flagged items). The engine arm is compared with the baseline arm **at the same first-draft stage, never against a corrected card**; the pass line of item 2 below applies to band (a).

3. **Matched control (preferred).** The five samples measured different sentence kinds, so they are a reference and not a
   matched control. If budget allows, a plain agent with the same sources and no repository answers the same questions
   and its statements are graded in the same blind packet, unlabelled.

## 6. Open points for ADV

* Accept that C1 may close as UNRESOLVED, or ask for a further candidate search (conference or preprint records with a
  printed release date) before 2026-12-01.
* Whether the metric of section 5 is worth running alone if no candidate resolves: it needs one blind reader.
