# Context / usage audit — did the slimming work, and why is the week expensive?

**Actor:** Orchestrator · **Date:** 2026-09-23 · **Class:** operational measurement
**Verdict, stated first:** 🟢 **The −82% is real and survives.** 🔴 **It was never the dominant cost.**

> 🔴 **Non-canonical operational artefact.** READ-ONLY toward the four scientific current files, every
> registry, every queue, the receipt ledger and the state manifest. Nothing promoted. No receipt claimed.
> 🔴 **Nothing here is medical advice.** 🔵 **Public edition.**

---

## § 0 · Method, and its bound — stated before any number

Everything below comes from **git history, the receipt ledger, file sizes, and this session's own
transcript**. No paper was re-read. No Scientist was launched. No four-way fan-out.

🔴 **Two bounds that limit what any number here can mean:**

1. **`PROVIDER TOKEN BREAKDOWN UNAVAILABLE` for Windows A, B and C.** The container was cloned fresh;
   `/root/.claude/projects/` holds **only this session's transcript**. The historical sessions' token
   counts do not exist anywhere reachable. They are **`UNMEASURED`** and are not estimated from characters.
2. **Tool-usage figures in § 3 are a PROXY.** They count *mentions of a tool inside the analysis files a
   window produced*, not runtime invocations. These files are unusually self-documenting — they record
   their own commands — so the proxy is better than usual, but a file can use a tool without naming it
   and name one without using it. Treated as **direction, not magnitude**.

🟢 **One measurement bound was LIFTED this session.** The previous run recorded that *"every commit older
than the shallow clone's 50-commit horizon"* was unverifiable. The clone was **unshallowed** (72 → **1,094
commits**), so the window comparison below rests on complete history rather than a truncated tail.

---

## § 1 · Did the −82% survive in real use? 🟢 **YES — and it is better than −82% per paper**

Re-measured today against the current registries:

| Quantity | 2026-09-11 | **2026-09-23** |
|---|---|---|
| Whole-registry payload (`paper_registry` + `literature_tracking_log`) | 1,066,618 chars | **942,972 chars** (the registries **shrank 11.6%**) |
| Per-paper selective retrieval, 6 real PMIDs | ~33,471 median | **median ≈ 28,575 · mean 42,812** |
| Reduction vs a whole-registry load | −82% (NEW MINIMAL vs OLD MINIMAL) | 🟢 **−95.5%** (mean per-paper vs whole-registry) |

Measured payloads: `36828035` 12,318 · `30362252` 13,806 · `33255508` 24,019 · `34634460` 33,131 ·
`30290271` 71,204 · `19936220` 102,399 chars.

🟢 **`registry_records.py` works exactly as designed.** The transport saving is real and reproducible.

🔴 **What this does NOT establish, and the distinction is the whole point:**
**`CONTEXT TRANSPORT REDUCTION = MEASURED`. `PROVIDER WEEKLY-USAGE REDUCTION = NOT MEASURED`.**
Characters are not provider-billed tokens, and § 4 shows why the two barely interact.

---

## § 2 · The three windows, measured

Window A **predates the slim tools** — both `registry_records.py` and `paper_packet.py` were first
committed **2026-09-11** (`83ec6be`, `e791b33`). A is therefore the **pre-intervention baseline**, and only
B and C are valid tests of adoption.

| | **A — Aqeilan** 09-08→09-09 | **B — Aldaz** 09-20 | **C — high-agency** 09-21→09-23 |
|---|---|---|---|
| Slim tools existed? | 🔴 **NO** | 🟢 yes | 🟢 yes |
| Commits | 118 | 39 | **151** |
| Files touched | 382 | 155 | 399 |
| Lines inserted | 37,489 | 14,233 | **71,905** |
| **Receipts earned (papers read)** | **26** | **26** | 🔴 **19** |
| **New analysis files** | 22 | 33 | 🔴 **117** |
| **Analysis bytes written** | 623,733 | 989,849 | 🔴 **5,264,794** |
| Mean analysis file size | 28,352 | 29,995 | **45,000** (+59%) |
| **Analysis files per paper read** | 0.85 | 1.27 | 🔴 **6.2** |
| **Analysis bytes per paper read** | 23,990 | 38,071 | 🔴 **277,094** |

### 🎯 The single most informative row

**Window C read FEWER papers than Window A (19 vs 26) and wrote 8.4× more analysis (5.26 MB vs 624 KB).**
Per paper read, it produced **11.6× more written output**.

⇒ 🔴 **The expensive thing is not reading. It is writing, reasoning and verifying about what was read.**

---

## § 3 · Was the slim path actually used? 🔴 **`PARTIALLY BYPASSED`**

Measured over the analysis files each window produced (proxy — see § 0):

| Signal | A (pre-tool) | B | **C** |
|---|---|---|---|
| `registry_records.py` | 0% | 15% | 🔴 **12%** |
| `paper_packet.py` | 0% | **0%** | 🔴 **1%** (1 file of 112) |
| whole `paper_registry_current.md` named | 9% | 13% | 🔴 **27%** |
| whole `literature_tracking_log_current.md` named | 0% | 10% | 5% |
| ad-hoc `grep` | 22% | 18% | 🔴 **44%** |
| ad-hoc `rg` | 4% | 10% | 🔴 **33%** |

### Verdict

- `registry_records.py` → 🟡 **`PARTIALLY BYPASSED`** — reached ~12–15% of work after twelve days.
- `paper_packet.py` → 🔴 **`MOSTLY BYPASSED`** — **1 appearance in 150 post-intervention analysis files.**

🔴 **And the bypass route is visible, not inferred.** Between A and C, ad-hoc `grep` **doubled** (22% → 44%)
and direct whole-registry references **tripled** (9% → 27%). The slim path was built; the traffic largely
went around it, into exactly the ad-hoc registry grepping `framework/scripts/README.md` warns against.

---

## § 4 · Why weekly usage is high — the mechanism, measured on this session

This session is a **deliberately cheap audit**: zero papers read, zero Scientists, no fan-out.
Its own transcript carries the provider counters:

| Counter | This session, 125 turns |
|---|---|
| `input_tokens` (uncached) | **244** |
| `cache_creation_input_tokens` | 402,257 |
| 🔴 **`cache_read_input_tokens`** | 🔴 **15,870,946** |
| `output_tokens` | 79,431 |
| **Total context re-read** | 🔴 **16,844,353** |

### The shape

| Turn | Context re-read that turn |
|---|---|
| 1 | 62,232 |
| 25 | 93,581 |
| 49 | 118,836 |
| 73 | 147,605 |
| 97 | 176,576 |
| 125 | **190,302** |

**Mean 134,754 tokens per turn. Second half cost 1.67× the first half for the same number of turns.**

### 🎯 The finding

**Every turn re-reads the entire accumulated conversation.** Context grows monotonically, so total cost
over a session is **the sum of a growing quantity — roughly quadratic in turn count**, and it is dominated
by `cache_read_input_tokens`, which had **nothing to do with registry payload size**.

⇒ 🔴 **Context slimming reduces the *increment* a single retrieval adds. It cannot reduce the *re-reading*
of everything already in the context.** A 95% cut to a 33 KB retrieval saves ~8 K tokens **once**; that same
retrieval is then re-read on **every subsequent turn** at full price, and the number of subsequent turns is
what a four-Scientist wave multiplies.

**This audit — which read no papers and launched nobody — still cost 16.8 M tokens of context re-read.**
Recorded against myself, because it is the cleanest available demonstration of the mechanism.

---

## § 5 · Ranking the eight candidate explanations

Ranked **after** measurement, as the brief required.

| Rank | Hypothesis | Verdict |
|---|---|---|
| **1** | 🔴 **C — OUTPUT/REASONING DOMINANCE** | 🟢 **CONFIRMED.** 5.26 MB of analysis written in Window C vs 624 KB in A, on **fewer** papers read. Output is the most expensive token class and it grew 8.4× |
| **2** | 🔴 **D — PARALLELISM MULTIPLIER** | 🟢 **CONFIRMED in mechanism, bounded in magnitude.** Four Scientists + Orchestrator = **five** independently accumulating contexts, each paying § 4's growing per-turn cost. Orchestrator first-hand re-verification **re-reads primaries the Scientists already read** — duplicating the single most expensive input by design |
| **3** | 🟡 **G — TOOL/HARNESS OVERHEAD** | 🟡 **PARTLY.** Gates ran at every landing across 151 commits. Real, but small beside § 4 |
| **4** | 🟡 **B — SLIM PATH BYPASS** | 🟡 **REAL BUT SECOND-ORDER.** § 3 proves the bypass (12% / 1% adoption). It costs the increment, not the re-read |
| **5** | 🟡 **A — THROUGHPUT EXPANSION** | 🟡 **PARTLY, AND NOT WHERE EXPECTED.** More *analysis* (117 files vs 22), **not** more *reading* (19 receipts vs 26) |
| **6** | 🟢 **F — LARGE NON-REGISTRY INPUTS** | 🟢 **CONFIRMED, and it reframes the target — see § 6** |
| — | **E — REPEATED RECONSTRUCTION** | 🟡 **ONE CONFIRMED INSTANCE**, operational not scientific: the frontier was not on `main`, and the previous session records that it *"nearly re-derived a completed census"* because of it. Fixed by this session's promotion |
| — | **H — UNKNOWN** | 🔴 **APPLIES to the historical windows only.** Provider telemetry for A/B/C does not exist |

---

## § 6 · The top five context consumers — measured, and the brief's own ranking is refuted

`SIZE × FREQUENCY`, over Window C's 112 analysis files (frequency = share of files naming the file):

| Rank | File | Bytes | Named in | Size×Freq | Scientific value | Safe to reduce? |
|---|---|---|---|---|---|---|
| **1** | 🔴 **`discovery_ledger_current.md`** | 598,289 | **47%** | **31.7** | 🟢 HIGH — the compounding capital | 🔴 **NO — but it is NOT covered by the slim path** |
| **2** | `corpus_seed_pubmed_20260806.jsonl` | 3,924,509 | 4% | 19.6 | 🟡 census only, not evidence | 🟢 **YES — never needs whole-file loading** |
| **3** | `paper_registry_current.md` | 449,135 | 27% | 13.9 | 🟢 HIGH | 🟡 already covered by `registry_records.py` — **adoption is the gap, not capability** |
| **4** | `full_text_queue_current.md` | 544,760 | 18% | 11.4 | 🟢 HIGH | 🟡 `--source` covers it; under-used |
| **5** | `fulltext_read_receipts.jsonl` | 1,048,329 | 8% | 10.5 | 🟢 HIGH (chain integrity) | 🟢 **YES — query it, never load it** |
| 6 | `claim_registry_current.md` | 127,862 | 25% | 3.6 | 🟢 HIGHEST | 🔴 **NO — small and load-bearing** |
| … | … | | | | | |
| **12** | 🔴 **`working_model_current.md`** | **53,902** | 8% | **0.5** | 🟢 HIGHEST | 🔴 **NO — and no need** |

### 🔴 Two of the brief's own hypotheses are refuted by measurement

The brief ranked `working_model_current.md` **#1** and `claim_registry_current.md` **#2**.
**Measured, they rank #12 and #6.** Together they are **54 KB and 128 KB** — among the *smallest*
canonical surfaces. They are not a cost problem and must not be touched.

### 🎯 And the real #1 is outside the slim path entirely

**`discovery_ledger_current.md` is the single largest context consumer (31.7, more than double
`paper_registry`'s 13.9)** — 598 KB named in **47%** of Window C's files. The −82% intervention targeted
`paper_registry` and `literature_tracking_log`, which rank **#3 and #7**. `registry_records.py` already
accepts `--source discovery_ledger_current`; nothing routes work through it.

---

## § 7 · Cost per unit of verified science

🔴 **In provider tokens: `UNMEASURABLE` for the historical windows.** No telemetry exists. Not estimated.

🟢 **In every proxy that can be measured, cost per unit rose:**

| Normalised metric | A | B | **C** |
|---|---|---|---|
| Analysis files / paper read | 0.85 | 1.27 | **6.2** (7.3× A) |
| Analysis bytes / paper read | 23,990 | 38,071 | **277,094** (11.6× A) |
| Commits / paper read | 4.5 | 1.5 | **7.9** |
| Papers read / day | 13.0 | 26.0 | **6.3** |

### The honest two-sided answer

🔴 **Against LEGEND:** it is **unambiguously more expensive per paper read**, on every proxy.

🟢 **For LEGEND:** *papers read* is the wrong denominator, and Window C is the proof. That window produced
**six accepted contradictions of the dispatching brief**, **two of them against the Orchestrator's own
reasoning**; it **withdrew** an NMD premise that had wrongly closed a therapeutic axis; it **killed** a
proposed cross-tissue convergence rather than publishing it; it caught a `consolidated baseline` claim
resting on an **extra-cerebellar** evidential block; and it established the Wiley routing rule at
**sensitivity 15/15, specificity 29/29, n = 44**. **Refutations and narrowings are the expensive output —
and they are the output that prevents wrong science.**

⇒ 🔴 **Not measurable as stated. What IS measured: the cost moved from reading to verifying, and the
verification kept finding real errors.** A cheaper Window C would have had to stop verifying.

---

## § 8 · What fraction is attributable to parallel throughput? — **bounded, not measured**

🔴 **Cannot be measured.** It requires per-agent turn counts, and no historical transcript survives.

🟡 **Bounded qualitatively, with the assumption stated.** Committed analysis text is a **lower bound** on
output tokens (it excludes reasoning, discarded drafts and tool output): C ≈ 1.32 M output tokens
(5.26 MB ÷ 4) vs A ≈ 156 K. At this session's measured 635 output tokens/turn, and allowing up to
~2,000/turn for long analysis files, that is **≈ 660–2,080 agent turns in Window C against ≈ 80–245 in A**.

At § 4's measured mean of ~135 K context tokens per turn — and Scientist contexts carrying full paper
bodies are **larger**, so this is conservative — Window C's total context re-read lands in the
**~10⁸ token range**, roughly **8× Window A**.

⇒ 🟡 **Bounded conclusion: the increase is dominated by TURN COUNT × FIVE ACCUMULATING CONTEXTS, not by
per-call context size.** 🔴 **Stated as a bound with its assumptions, not as a measurement, and deliberately
not converted into billing.**

---

## § 9 · What I could NOT verify — exhaustive

1. 🔴 Provider token counts for Windows A, B and C. The transcripts do not exist in this container.
2. 🔴 Per-agent turn counts, peak parallel Scientists, and wave boundaries — inferable from commit
   clustering only, which does not separate agents.
3. 🔴 Whether a tool named in an analysis file was actually invoked (§ 0 bound 2).
4. 🔴 Rate/usage interruptions per window — no record survives.
5. 🔴 Reasoning-token volume in any window, including this one: the transcript reports `output_tokens`
   without separating reasoning.
6. 🟡 Whether `discovery_ledger_current.md` is **loaded whole** or merely **cited** in the 47% of files
   that name it. Its rank as #1 consumer rests on the § 0 bound-2 proxy and should be confirmed before
   any change is made to it.

---

## § 10 · The one change this audit would justify — **proposed only, not built**

🔴 **No new index, RAG layer, cache, registry, graph, context manager, receipt schema, gate or daemon.**
§ 19 of the brief is respected: nothing below was implemented.

The measured dominant costs are **(a) turns × accumulating context** and **(b) a #1 consumer outside the
slim path**. (a) is architectural and must not be touched before more measurement. (b) is a **routing**
change, lean and reversible, and it is the only thing § 6 licenses:

> **Route `discovery_ledger_current.md` through `registry_records.py --source discovery_ledger_current`,
> the way `paper_registry` already is — and fix the adoption gap, which is 12% / 1%, not a capability gap.**

🔴 **Verify § 9 item 6 first.** If the ledger is cited rather than loaded, the change buys nothing, and
this audit would have talked itself into exactly the redesign the brief forbids.
