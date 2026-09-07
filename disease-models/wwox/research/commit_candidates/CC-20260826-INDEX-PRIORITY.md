# INDEX — the 2026-08-26 repair set, ranked by canonical impact

**Index ID:** CC-20260826-INDEX-PRIORITY
**Date:** 2026-08-26
**Status:** index only; **no canonical file modified** by any member of this set
**Ranked by:** (1) false canonical statement · (2) therapeutic reasoning · (3) disease-mechanism
structure · (4) provenance integrity · (5) future experiment selection.
**Not** ranked by ease of editing — the cheapest edit in the set (item 6, five metadata fields)
sits fifth, and the most expensive (item 1, a MAJOR authorization) sits first.

---

| # | Artifact | What it repairs | 1 false stmt | 2 therapy | 3 mechanism | 4 provenance | 5 experiment | Gate |
|---|---|---|---|---|---|---|---|---|
| **1** | [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md) | `CLAIM 037` headline is **false**; `CLAIM 005` carries a **prohibition against a true statement** | 🔴🔴🔴 | ○ | ●●● | ●● | ●●● | 🔴 **authorization** |
| **2** | [`CC-20260826-CLAIM032-01`](CC-20260826-CLAIM032-01.md) | global quantifier on haploinsufficiency; reconciliation with `CLAIM 011`; dose axes separated | 🔴🔴 | ●●● | ●●● | ○ | ●●● | review |
| **3** | [`CC-20260826-CLAIM002-01`](CC-20260826-CLAIM002-01.md) | depolarizing-GABA presented as a signature; the two candidate mechanisms compete and only one is measured | 🔴 | ●● | ●●● | ● | ●●● | review (BLOCK-1 wording) |
| **4** | [`CC-20260826-CLAIM003-01`](CC-20260826-CLAIM003-01.md) | `CLAIM 003` names as missing an experiment its own source performed | 🔴 | ● | ●● | ● | ●●● | review |
| **5** | [`CC-20260826-PROVENANCE-01`](CC-20260826-PROVENANCE-01.md) | four source records that do not identify their source | ○ | ● | ● | 🔴🔴🔴 | ● | 🔴 **authorization (item A only)** |
| **6** | [`PROPOSAL-20260826-…-PROPAGATION`](PROPOSAL-20260826-LOCATOR-TO-CLAIM-PROPAGATION.md) | measures the gap that produced items 1–5; three gates proposed, one refused | ○ | ○ | ○ | ●●● | ● | proposal |
| — | [`CC-20260825-ADVERSARIAL-FALSIFICATION-01`](CC-20260825-ADVERSARIAL-FALSIFICATION-01.md) | the pass these repairs come from; **carries an append-only correction of its own false statement** | — | — | — | — | — | superseded in part by #1 |

---

## Why this order and not another

**Item 1 first, despite being the most expensive.** It is the only member of the set where a
canonical file states something **false** rather than over-broad, and where a canonical *rule* —
*"No canonical statement may describe a Wwox-null mouse as showing epileptogenesis"* — actively
forbids writing down a true, `p < 0.0001`, rescue-confirmed result. A prohibition is worse than a
wrong claim: a wrong claim can be contradicted by the next reading, while a prohibition instructs
the next reader not to.

**Item 2 second on therapy.** `CLAIM 032` is `clinical relevance: VERY HIGH` and sets the dose
target for the whole restoration portfolio. Its repair does not merely qualify the claim — it
shows that the claim and `CLAIM 011` have been answering each other's questions across
non-commensurable axes (uniform gene dose vs mosaic vector dose vs per-line expression level).

**Item 3 third, above item 4, because of what it protects.** The demotion removes an unmeasured
premise from under a clinically consequential caution. Left alone, the caution is fragile in the
dangerous direction: the day someone measures E_GABA and finds it normal, a caution resting on
depolarizing GABA would look refuted while the human VABAM signal it actually rests on is
untouched.

**Item 4 fourth on experiment selection.** It converts a decisive experiment from "build a mouse"
into "run histology and EM on a line that already exists and breeds" — the largest change in
expected cost per unit of information in the set.

**Item 5 fifth despite being the easiest.** Metadata repairs move nothing scientific on their
own. They are ranked here, rather than lower, only because item A suspends two
`consolidated baseline` claims whose source names no paper.

**Item 6 last, and it is the one that compounds.** Items 1–5 are corrections. Item 6 is the
measurement of the process that produced them: six real propagation failures, five legitimately
pending cases, three gates recommended and one refused with its reason.

---

## The single sentence a reviewer should read first

Two canonical claims in the same registry state opposite things about the same animal —
`CLAIM 011` records ECoG spike-wave discharges in `Wwox`-null mice as a domain its gene therapy
rescues, and `CLAIM 037` states that seizures are *"explicitly absent in Wwox-null mice"* — and
neither cites the other.
