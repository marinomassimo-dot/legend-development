# Two bounded foundation checks — 2026-09-21

**Actor:** Orchestrator · **Mode:** READ-ONLY, two tool runs and two record reads. No canonical file
written, no claim created, no receipt, no commit candidate.

> **Scope, declared up front.** This is **not** the broad registry↔ledger reconciliation, which is
> fenced off. It is two targeted questions: *what does the safety claim rest on*, and *does the
> species-drift screen have anything in it*. Both were prompted by today's reading, not by a sweep.

---

## 1 · 🔴 `CLAIM 001`'s safety anchor has never been read, and cannot be read here

`trace_claim_foundation.py --claim "CLAIM 001"`:

```
status: conflicting evidence · type: DATO · declared model: human
Rests on: PAPER 003 (41442931) · PAPER 014 (40875931) · PAPER 016 (39101447)
          PAPER 017 (36537114) · PAPER 045 (30361190)
Coverage — 1/5 supporting papers are manifest-backed (20%)
```

Four of the five carry full-text receipts. **`PAPER 003` does not.** And `PAPER 003` is the one the
registry itself calls the **`safety anchor paper`**, with `clinical relevance: HIGH` and
`Working Model impact: BLOCCO 1 safety`.

**What `PAPER 003` is:** `PMID 41442931` — Choi HW *et al.*, *Pediatric Neurology* 2025;175:230–233,
*"Vigabatrin-Associated Brain Magnetic Resonance Imaging Abnormalities in Two Children With WWOX-Related
Epileptic Encephalopathy Syndrome"* ([DOI](https://doi.org/10.1016/j.pediatrneurol.2025.12.001)).
🔴 **No PMCID — verified today with `convert_article_ids`.** Elsevier. **Unobtainable by any route
available in this checkout.**

### Why this is the sharpest acquisition item in the model right now
Vigabatrin is **in active use in this population** — it is one of the four levers tried and failed in
the WOREE null case (`PMID 35573960`). The paper reports, at abstract level:

> *"Brain magnetic resonance imaging during vigabatrin treatment revealed new symmetrical signal
> changes in the globus pallidi and thalami consistent with VABAM."*

and closes by asking a question that lands directly on WWOX biology:

> *"Further research is warranted to investigate whether children with genetic epilepsy related to the
> **GABAergic pathway or delayed myelination** are more susceptible to VABAM."*

🔴 **WOREE has both.** LEGEND holds the GABAergic axis (`CLAIM 005`, `PMID 30290271`) and the
hypomyelination/oligodendrocyte axis (`CLAIM 002`, `CLAIM 003`, `DL-MECH-027`). **So the authors'
own proposed susceptibility mechanism is the disease model's own two best-established features.**

⚠️ **Mood preserved, and it matters.** That sentence is a **question** — *"Further research is
warranted to investigate whether…"*. It is **not** a finding that WWOX children are more
susceptible, and it must never be re-voiced as one. `n = 2`, case reports, association, *"consistent
with"*. `CLAIM 001`'s own status is already `conflicting evidence`.

**What a full text would settle that the abstract cannot:** the two children's genotypes and
WWOX variant classes; vigabatrin dose, duration and co-medication; whether MRI change was
symptomatic or incidental; whether it reversed on withdrawal; what the baseline imaging showed
(the abstract already notes *pre-existing* periventricular white matter volume loss and corpus
callosum atrophy — **which is itself a confounder for reading new signal change**); and whether the
authors report any WWOX-specific comparison at all or only the two cases.

> **ACQUISITION ASK — promote this.** It is a two-page clinical report in a mainstream journal, it
> bears on a drug a treating team may be using today, and it is the unread anchor of the only
> BLOCK-1 safety claim. **It should sit at the top of the human-acquisition packet, above the
> mechanistic items.** Nothing here is medical advice, and no dosing or treatment inference is drawn.

---

## 2 · 🟢 The species-drift screen: 1 finding in 39 claims, and it is already adjudicated

`trace_claim_foundation.py --all-drift` → `scanned 39 claims · 1 species-drift findings`:

> `CLAIM 005: model 'mouse' rests on PAPER 058 (PMID 19500159) — 'rat'`

**This is the screen working, and the finding is already closed inside the claim's own text.**
`CLAIM 005` is `consolidated baseline`, 3/3 manifest-backed, and its `Evidence boundary` field
explains the rat edge at length — the rat paper is cited **to establish the opposite of a transfer**:

> *"🔴 **And that terminus asserts the opposite for the mouse:** PMID 19500159 states in three
> places, and in a Table 2 whose `Epilepsy` row is **empty for both mouse models**, that Wwox-null
> mice show no epilepsy … **No canonical statement may describe a Wwox-null mouse as showing
> epileptogenesis.**"*

So the rat study is present as a **boundary and a negative**, not as a phenotype crossing a species
line. Classified **`CONTEXTUAL_DISSOCIATION` — already reconciled**, not `TRUE_CONTRADICTION`.

🔴 **Recorded so it is not re-opened.** The detector cannot distinguish "rests on a rat paper for a
transferred phenotype" from "rests on a rat paper to refuse a transfer", and it should not be
expected to — **that judgement is in the claim text, which is where it belongs.** A future session
seeing this one drift line should read `CLAIM 005`'s `Evidence boundary` and stop.

**The honest reading of the clean result:** 39 claims, one flag, already handled. But the coverage
caveat the tool prints itself applies — where a claim's support is registry-declared rather than
quote-verified, **absence of a drift finding is bounded by that**, not proof of absence. `CLAIM 001`
above is exactly such a case at 20 % coverage.

---

## 3 · What was deliberately NOT done

- **The broad registry↔ledger reconciliation was not opened.** It remains fenced.
- **`cross_claim_contradiction_census.py` was run and its output was NOT pursued**: 46 candidate
  pairs, **38 not cross-linked**. That is a screen, not a verdict, and adjudicating 38 pairs *is*
  the broad reconciliation. Recorded here only so the number is on file. The tool's own instruction
  stands — adjudicate against the primaries, and do not grow the count with ambiguous cases.
- **No claim was edited, no status changed, no commit candidate produced.**

*Non-canonical analysis file. Not medical advice.*
