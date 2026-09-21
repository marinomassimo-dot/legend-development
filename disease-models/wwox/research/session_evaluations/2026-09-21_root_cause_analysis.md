# Root-cause analysis of the eight `severity_high` incidents — 2026-09-21

> **READ-ONLY analysis. No gate, no workflow and no authority layer is created here.** The
> Operator's instruction was explicit: *analyse, do not govern.* The mitigation column below is
> ordered by the stated preference — **reuse existing control > targeted test > optional audit >
> mandatory gate** — and in five of eight cases the honest answer is that a control that already
> exists was simply not used.

Source: `2026-09-21_orchestrator_autonomous_continuation.md`, `ATTRIBUTION_CENSUS`:
`incidents: 17 · machine: 8 · blind_auditor: 0 · peer: 4 · self: 5 · severity_high: 8 (of which self: 3)`.

## The eight, classified

| # | Incident | Failure class | Catcher | Minimal intervention that would have prevented it |
|---|---|---|---|---|
| 1 | Author byline written into a receipt from memory, against a queue entry and an analysis file that both had it right | **identity/mention confusion** | self | **Existing control, not used.** `get_article_metadata` had already been called for that PMID in the same session. *Copy, never recall* — a habit, not a check. |
| 2 | Gene-symbol zero counts offered as evidence of a paper's silence | **extraction damage** | peer | **Targeted tool — now shipped.** `extraction_damage_report.py` turns the nine repeated prose warnings into one command with an admissibility verdict. This is the one incident that justified new code. |
| 4 | Artefact re-fetched to a path an existing receipt fingerprinted; prior bytes unrecoverable | **propagation omission** (of the ledger's own state into the dispatch decision) | self | **Existing control, not used.** One `grep -c '"pmid": "X"'` against the ledger before dispatching. Zero cost. |
| 5 | Three papers recorded as verified-blocked on a copyright flag whose `checked_sources` omitted `pmc` | **detection-floor overstatement** (a not-checked reading read as a negative) | peer | **Existing control, not used.** The flag's own `checked_sources` field said PMC had not been consulted. The rule *"retrievability is established by fetching and measuring"* is now written down; it needed no tooling. |
| 6 | `33134515` recorded as *"licence-walled"* in a retraction and in the queue; it returns a full body | **detection-floor overstatement** (same root cause as #5, different record) | peer | Same as #5. **Counting these as one class is the point** — one habit fixes both. |
| 10 | Parent-of-origin language written into an append-only receipt → `BLOCK_PUBLICATION`, unfixable without Operator authorisation | **other** — a privacy-surface collision with an append-only medium | machine | **Existing control worked, too late.** The gate caught it correctly; the cost was that the medium is append-only. The mitigation is a **one-line drafting habit** now recorded: keep inheritance-side attribution out of receipts entirely. **No new gate.** |
| 15 | *"Two species, two modalities, the same negative about the cerebellum"* written into the packet and queue; contradicted hours later | **endpoint too blunt** — two different propositions (MRI midline volume vs light-microscopy histology) treated as one | peer | **Better use of an existing discipline.** The repository already distinguishes endpoint from claim; I collapsed two endpoints into one sentence. A **checklist line** — *name the endpoint before asserting a convergence* — is proportionate. |
| 17 | Oligodendrocyte autonomy reported open and **pushed**; `DL-MECH-031` had settled it and `HYP-20260709-07` was parked on it in July | **source not read** (the repository's own record) | self | **Existing control, not used.** `registry_records.py` and a targeted read of the discovery/therapeutic ledgers. Same root cause as #4 at one level up. |

## What the classification actually says

**Three classes account for six of the eight.**

- 🔴 **"I did not read our own record" — incidents 4, 17, and the dispatch half of 1: three of eight.** Not a literature failure, not an extraction failure. The most expensive errors of the session came from acting on a **delegate's census**, which measures PubMed, as though it measured **LEGEND**. No tool is missing for this; the tools were in hand and unused.
- **Detection-floor overstatement — incidents 5 and 6: two of eight, one root cause.** A `false` that meant *not checked* was read as *checked and negative*. This is the same epistemic error the repository already names in `D-17`'s draft and in the `CLAIM 030` detection-floor candidate, arriving in a tooling context rather than a scientific one.
- **Extraction damage — incident 2: one of eight**, and the only one where nine prose warnings had demonstrably failed and code was the proportionate answer.

**`of which self: 3 of 8` against 3 of 6 on 2026-09-09 is a worse ratio**, and the classification shows why: the errors that machines catch (schema, links, addresses, gates) were caught, while the errors that **only reading our own record would catch** were caught by delegates, or by me one cycle late. That is a reader-practice signal, not a gate signal.

**`blind_auditor: 0`** — and the classification does not make a mandatory blind audit look like the fix. **None of the eight is a locator-support failure**, which is what `legend-locator-audit` measures. It would have caught none of them.

## The counting caveat that constrains all of the above

`undetected_known: 0`. Three of the seventeen were errors published earlier in this same session and found later in it; a session ending six hours sooner would have reported `0` and looked cleaner. **This analysis describes how caught errors were caught. It cannot measure the undetected rate**, and nothing here should be read as if it could.

---

*Orchestrator, 2026-09-21. READ-ONLY. No gate, workflow, registry or authority layer created. Not medical advice.*

---

# Governance / harness recommendation — the two proposals this session generated

> The Operator asked that neither be implemented automatically, and that each be judged on error
> reduction, false-positive friction, duplication of existing controls, whether a lighter rule
> substitutes, and whether it adds a permanent gate. Both are judged below. **Neither is implemented.**

## Proposal 1 — wire `extraction_damage_report.py` into `session_self_eval.py`

| Test | Assessment |
|---|---|
| **Real errors reduced** | **One class, and it is a real one** (incident 2). But the tool already exists and is one command; wiring it into the gate does not make the measurement better, only **compulsory**. |
| **False positives / friction** | **Low but not zero, and structurally awkward.** The tool's verdict is *"italic-class counts are inadmissible"* — true of **29 of 29** local artefacts. A check that fires on 100 % of inputs carries no information and becomes noise a reader learns to scroll past. |
| **Duplicates an existing control?** | **Partly.** The receipt schema already requires an `evidence_basis`, and this session wrote the admissibility verdict into nine receipts **voluntarily, without a gate**. |
| **Lighter substitute?** | **Yes, and it is better.** A **receipt-writing habit**: when a receipt offers any string count, it names the token class. That is already what the nine receipts do. |
| **Adds a permanent gate?** | **Yes** — and on a check that would pass-with-warning on every input. |

### ⇒ **KEEP OPTIONAL**
Keep the tool, keep it routed in `framework/scripts/README.md`, keep using it before offering a
count. **Do not wire it into the gate.** Revisit only if a *future* session offers an italic-class
zero as evidence **despite** the tool existing — that would be evidence the habit is insufficient,
which today's evidence is not, since the habit did not yet exist.

## Proposal 2 — mandate `legend-locator-audit` for retractions of analysis-layer claims

| Test | Assessment |
|---|---|
| **Real errors reduced** | 🔴 **Zero, on the measured record.** None of the eight `severity_high` incidents is a locator-support failure. The audit answers *"does this quote support this proposition?"* — and today's failures were **unread own-records, unchecked flags, and conflated endpoints**. It would have caught none of them. |
| **False positives / friction** | **High.** A blind audit is a full delegated read. Mandating it on every analysis-layer retraction would have fired **at least four times today**, at roughly one Scientist each, for a failure class the record shows is not occurring. |
| **Duplicates an existing control?** | **Yes.** The audit already fires on `consolidated baseline` claims and on a `MAJOR` change class — the two places where locator support is load-bearing. Analysis-layer files are, by design, **below** that line. |
| **Lighter substitute?** | **Yes.** Personal verification of every load-bearing quotation against the artefact — which **was done for all nine readings today**, and is why the quotations survived. |
| **Adds a permanent gate?** | **Yes**, and a costly one. |

### ⇒ **DO NOT ADD**
The `blind_auditor: 0` line is worth keeping visible as a **standing observation**, not converting
into a rule. 🔴 **The honest reading of that zero is not "we need a mandatory auditor": it is that
the session retracted a three-legged claim with every quotation verified by the actor who wanted the
retraction.** The proportionate response is to **use the existing skill by judgement** when a
retraction turns on a quotation's scope — which is a decision, not a gate.

## What I would do instead, and it costs nothing

Three one-line habits, all of which address the classified root causes and **none of which is a
gate, a registry, an authority layer or a workflow**:

1. 🔴 **Before dispatching a read, `grep` the receipt ledger for the PMID — and when a delegate
   chooses the paper, put that check in the brief.** Addresses incidents 4 and 17, the most
   expensive class of the session.
2. **A copyright flag's `checked_sources` is part of the reading.** `is_open_access: false` with
   `["pubmed"]` alone means *not checked*. Addresses incidents 5 and 6.
3. **Name the endpoint before asserting a convergence.** Addresses incident 15.

**These are already written into `AUTONOMOUS_SESSION_STATE.md` with their worked failures.** That is
the whole implementation, and it is the right size.

---

*Orchestrator, 2026-09-21. No control implemented. Recommendations only.*
