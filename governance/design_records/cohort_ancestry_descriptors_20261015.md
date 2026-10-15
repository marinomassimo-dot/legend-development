---
artifact: LEGEND governance — design record
record: published-cohort ancestry and geography descriptors in the public edition
normative: NO — provenance for an existing rule, not a new one
binding_on_actors: none (the rule it explains binds; this record only shows how it decides the case)
decided_on: 2026-10-15
decided_by: Harness Engineering (ACTOR_ID plan), under the operator's written delegation of the same day
raised_by: BATCH_20261004_007 report, 2026-10-04 — "decide once, in writing, whether published-cohort ancestry descriptors stay in this edition"
---

# Published-cohort ancestry descriptors stay. The existing rule already decides it.

## The question as the batch left it

`BATCH_20261004_007` repaired one paired parent-of-origin descriptor in `CLAIM 032` and, by the same
lexicon scan, **measured** nine nationality/geography tokens elsewhere in the record. It did not
rewrite them, because doing so is a scope decision with scientific content, and it asked that the
decision be taken once, in writing, and then applied in one pass rather than one word at a time.
Until this record the question was open.

## What the tokens are — measured 2026-10-15 on `main` at 86b91b70

`registry_records.py get --id "CLAIM 032"`, scanned for nationality and geography tokens:

| Where in the record | Tokens | What they describe |
|---|---|---|
| allele-class census sentence | Moroccan, Iranian, French, Yemenite | the national cohorts of four **published** homozygous / compound-heterozygous patient series, carried with their counts |
| Tabarki-overlap paragraph | Saudi centre | the recruiting centre of a **published** neurodevelopmental cohort, named to settle whether two reports describe the same patients |
| 16q-deletion paragraph | Tunisian (×3) | a **published** diagnostic cohort, named for the same reason — cohort identity, not a person |

Every token is **cohort-level**, **attributed to a published paper**, and **already public in that
paper's own title or abstract**. None is paired with an age, a sex, a family structure, a date of
diagnosis, a genotype at individual resolution, or any feature of the reference genotype. Two of the
three groups exist precisely to disambiguate overlapping cohorts — which patients a count refers to
— and that is scientific content, not colour.

## The rule that decides it

The public edition carries **no individual-level record** and **no individual linkage**
(`CLAUDE.md` § 0; the registries' own preambles: *"All individual-linking data removed — names,
geography, report/sample IDs, dates, parent-of-origin, cell-line ownership"*). The word *geography*
in that list is scoped by the list it sits in: it names the geography **of an individual**, and the
release gate enforces exactly that reading — `scripts/public_release_gate.py` flags geography only
when it is linked to a person/proband context, and flags paired parent-of-origin text as REVIEW.

A published cohort's nationality is not an individual's geography. It is a property of a dataset
that another group published, at the aggregation its authors chose, and it is a reading-relevant
covariate (consanguinity rate, founder alleles, which cohort a number counts). Removing it would
delete unique scientific content from this edition and would not remove it from the world.

**Decision:** published-cohort ancestry and geography descriptors **stay**, under three conditions
that are already the rule and are restated here only so nobody re-derives them:

1. **cohort-level only** — a nationality may describe a series, a centre or a cohort, never one
   patient of it;
2. **attributed** — the sentence that carries it names, or sits in a record that names, the
   published source it comes from;
3. **never combined with the reference genotype** — no sentence may place a cohort descriptor
   and a feature of the reference genotype (age, sex, variant at individual resolution, parent of
   origin, timing) in the same individual-level frame. That combination is what the gate's
   person/proband context rule catches, and it stays the only enforced check.

## What this changes

Nothing in any current file, and no new gate. The nine tokens in `CLAIM 032` meet all three
conditions and are left as they are. No rewrite pass is owed. A future batch that finds a cohort
descriptor failing condition 1 or 3 repairs it as `BATCH_20261004_007` repaired the parent-of-origin
descriptor — one exact `replace-within`, measured by script — and cites this record instead of
reopening the question.

The lexicon scan the batch used lived in its scratch directory and is not in the repository; a
batch that wants to repeat the measurement runs `registry_records.py get` on the record and greps
the output for nationality tokens, as this record did. Promoting that scan to a shipped tool was
considered and declined: the gate already carries the one rule that is enforced, and a second
scanner for a category the rule deliberately does not flag would be a control with no verdict.

## Authority

The batch report named this for *"Mirror or for the next batch"*. The operator, on 2026-10-15,
delegated the decision to Harness Engineering in writing (*"decidi tu, ti autorizzo"*). The
decision is reversible by a one-line amendment to this record and a single batch; it reverses
nothing the gate enforces.
