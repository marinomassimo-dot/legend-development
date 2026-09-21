# Batch self-evaluation — the second autonomous run, 2026-09-21

> Written after the analytical work and before capability growth or takeaways, because
> takeaways written first describe a session that went well.

## Scope and executable verdict

- **Batch/session:** second autonomous run, 2026-09-21, operator in transit. Orchestrator +
  two Scientists (never more than two concurrently, as instructed). Four waves each.
- **Studies and complete-read receipt IDs:** 🔴 **NONE. No receipt was persisted by this run.**
  Papers were fetched and quoted in-act (`22534828` complete body by the Orchestrator;
  `40327201`, `38378758`, `42422765`, `25866966`, `17289941`, `31704158`, `32000863`, and others
  by Scientists), and **every one is recorded as read-without-receipt** in `FT-113`, `FT-116`,
  `FT-118`. **This is the single largest process debt of the run** and is stated first for that
  reason. See *Persistence diagnosis*.
- **`session_self_eval.py`:** `PASS — every complete read has landed and every declared output
  resolves`. `receipts: 188 · complete_fulltext_events: 84 · active_complete_reads: 72 ·
  unread_premises: 0/0`.
- **Per-study manifest(s):** none created — no receipt, therefore no manifest. Existing manifests
  were *read* (notably `PMID42397075.json`, 30 entries) and one was measured against the registry.
- **Receipt verification:** `OK: 188 chained receipt(s), tail anchored`.
- **Structural LINT:** `PASS`.
- **Local verdict:** publication gate `PASS / BLOCKS 0`; growth anchors `PASS`;
  `test_tool_routing.py` `OK`.
- **Workspace/global verdict and concurrent conditions:** 🔴 `run_release_regressions.py` could
  **not be measured cleanly**: its guard reports *"WROTE 1 tracked file(s) under a guarded tree"*
  whenever a Scientist writes its deliverable mid-run, and Scientists were writing for most of the
  session. One run completed `exit 0` before the subagents were active. **Declared, not
  explained away: the clean-tree measurement was not obtained while subagents were live, and the
  release-suite state at session end is therefore unverified.** A Scientist agent also terminated
  on an **API session rate limit**, and the literature MCP disconnected and returned.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Bodies read and quoted in-act with **measured lengths** (48,780 · 82,755 · 111,350 · 71,480 chars). **Zero figures inspected** — no PDF tooling, and the extractor returns empty `()` for every callout | `partial` | Every figure-level number used came from **prior sessions' panel readings**, attributed as such at each use |
| Main message and original contribution | Six results that change something, each stated as one sentence before its evidence | `strong` | — |
| Hidden gold beyond keywords/abstract | 🔴 **`PMID 21476439`** — the only published WWOX catalytic assay — found inside LEGEND's own registry at Tier C, `background only` | `strong` | Root cause fixed: `MECHANISM_RE` had no catalysis vocabulary |
| Source parity: context, type and recency | `25662954` correctly identified as `Review` and scored at zero; `30783266` as `Published Erratum`; `22534828` bounded to fibroblast/cancer lines | `strong` | — |
| Team type, field density, observation vs interpretation | Lodz re-scored on one axis only (custodian of a dataset, **not** rehabilitated as a collaborator); Chang-corpus independence caution applied to `22534828` | `strong` | — |
| DATO / INFERENZA / IPOTESI separation | Exon-6 skip marked **MEASURED**, frame arithmetic **PREDICTED**, cryptic site **NOT ASSESSED** | `strong` | — |
| Existing claims touched; conflicts/revival triggers | `CLAIM 011` ↔ `CLAIM 032` tension surfaced; `CLAIM 030` ↔ `CLAIM 033` contradiction opened as a node | `strong` | Six candidates, **none propagated** |
| Multi-hop and corpus cross-query | Oppermann → SGC deorphanisation; erratum → cohort → `PAPER 025` conflation → `CORPUS-STUB-059` | `strong` | — |

## Persistence diagnosis

- **Durable ledger/registry IDs and wikilinks:** six commit candidates
  (`CC-20260921-*`), nine queue entries (`FT-113`–`FT-121`), one state-file rewrite. **No canonical
  scientific current file was edited.**
- **Reading queue/debt:** the `UNREAD_PREMISE` ratchet went above zero **four times** and was
  driven back to `0/0` each time **by declaring the debt in the queue, never by removing the
  citation**. 🔵 That is the ratchet doing its job on the session that invoked it against a claim.
- **Dossier and commit candidate:** candidates yes; dossiers no — consistent with no receipts.
- **Receipt source fingerprint, coverage and supplement state:** 🔴 **n/a — nothing persisted.**
- **Can a future run distinguish full text from abstract only? How:** yes, and only because it was
  written down by hand. Every queue entry states its depth explicitly (*"read, not receipted"*,
  *"abstract only"*, *"body 0 bytes"*) and names the artefact state. **Nothing mechanical enforces
  this**; it held because the rule was applied, not because it was checked.

## Process and capability diagnosis

- **Skills/gates/patterns used:** `legend_lint`, `session_self_eval`, `fulltext_receipts verify`,
  `growth_anchors check`, `public_release_gate`, `unread_gold`, `registry_records`,
  `test_tool_routing`, `run_release_regressions`.
- **Plausible skills deliberately declined, with reasons:** `legend-commit` — six candidates exist
  and `≥5` is a trigger, but **every one proposes touching a canonical file and the operator's
  brief says propagation is authorised only where existing rules permit**; several are `R3`, one
  touches a safety score, and the batch is better reviewed whole than propagated piecemeal by its
  author. `legend-locator-audit` — **not applicable**: no reading this run narrowed or reversed a
  `consolidated baseline` claim, and the premise being removed from `CLAIM 032` **has no locator to
  audit**, which is the defect. `legend-aso-designer` — `DL-MOL-011` asks for exactly this, and it
  was **declined deliberately**: the node in front of it was feasibility of an RNA measurement, and
  adjudicating a parked reclassification is a different task that deserves its own wave.
- **Failures, retries, extraction mismatches or concurrency events:**
  - 🔴 **Five first measurements wrong**, all the same shape: a **proxy** measured instead of the
    thing — `registry_records index --identities` (4% false positive, measured), `len()` on a dict
    (6 keys read as 6 locators, **twice, by two actors independently**), a record-id prefix (81
    "unpromoted" that were preserved placeholders).
  - 🔴 **Two DOIs reconstructed from memory instead of copied.** `10.1016/j.ymthe.2026.01.014` for
    `PMID 42422765` (true: `10.1016/j.omta.2026.201791`); one for `PMID 30853297`, which has **no
    DOI at all** in its PubMed record.
  - 🔴 **Two alleles conflated in a delegate brief** — `c.517-2A>G` (exon 6) treated as the
    acceptor LEGEND reasons about (`c.1057-2A>G`, exon 9, **last** exon); **opposite NMD regimes**.
  - 🔴 **A living researcher's e-mail** written into a public-edition file by a Scientist.
  - **Concurrency:** the release-regression guard fired repeatedly on subagent writes; see above.
  - **Resource:** one Scientist terminated on an **API session rate limit**; MCP dropped/returned.
- **What caught each failure before an overclaim:**
  - the proxy errors — **spot-checking my own number against the thing it measured**, four times
    self-caught, once prompted by a Scientist's independent count;
  - the first DOI — **flagging it `unverified` instead of letting it look finished**, then checking;
  - the second DOI — checking **because the first had just happened**;
  - the allele conflation — 🔵 **Scientist A, against its own brief.** The most valuable catch of
    the run, and it came from the delegate contradicting the Orchestrator;
  - the e-mail — 🔵 **`public_release_gate.py`**, which refused the batch. The only failure here
    caught by a machine.
- **Disease-agnostic micro-upgrade shipped:** two.
  1. `unread_gold.py` — both field spellings (its selectors matched **zero** live records), a
     **catalysis** clause, a **substrate-class** clause, and a **receipt-ledger cross-check** that
     annotates **19** stale rows rather than silently re-dispatching them. **13 tests; 5 fail on
     revert.**
  2. `locator_count_crosscheck.py` — **new, routed**, measuring **16 of 34** declarations wrong,
     all understating. **10 tests; 3 fail on revert.**
- **Regression/evidence that makes the upgrade persistent:** both suites mutation-tested; one test
  in each asserts **against the live repository** rather than a fixture, because a fixture test
  would have passed throughout the period each defect was live.
- **Residual risk and next decisive action:** 🔴 **the receipt debt.** This run produced six
  candidates and nine queue entries on readings that have **no receipts**, which is precisely the
  asymmetry `session_self_evaluation.md` was written about — the work is durable, the *evidence of
  how completely it was done* is not. **Next decisive action: `FT-117` / `PMID 30853297`, read to
  receipt depth**, since it carries a measured exon-6 skip, is a `Q230P` primary, and sits under a
  `consolidated baseline` claim at abstract depth.

## Attribution census — required, fixed, parseable

```
ATTRIBUTION_CENSUS
incidents: 10
machine: 1   blind_auditor: 0   peer: 1   self: 8
severity_high: 2   of which self: 1
undetected_known: 0
```

**Counting.** Ten incidents: five proxy-measurement errors (counted once per distinct proxy class:
identity index · `len()` on a dict · record-id prefix = 3), two DOI reconstructions, one allele
conflation, one e-mail exposure, one unmeasurable release suite, one receipt debt. `machine: 1` —
the publication gate. `peer: 1` — Scientist A on the allele conflation. `self: 8`.
**`severity_high: 2`** — the e-mail (**would have reached the public record**; refused by the gate,
so `machine`) and the allele conflation (**did reach a delegate brief and directed a wave**; caught
by a peer, so `of which self: 1` counts the DOI that reached a drafted candidate file).

🔴 **`undetected_known: 0` is the limit of this census, not a result.** Eight of ten incidents were
self-caught, which is the number a self-graded diagnosis always produces, and **one machine catch
in ten** is the honest measure of how little of this run was checked by anything other than the
actor doing it. The blind-auditor column is empty because no reading this run qualified for `R4`.
**A later wave attributing a defect back to this one should raise this line rather than reporting
it clean.**

## §21c output

**STOP_LOG:** zero stops. No class-1 reserved act was reached; no class-2 condition without a safe
default arose. Two conditions took safe defaults rather than stopping — an unmeasurable release
suite (**proceed, declare**) and a delegate's rate-limit termination (**salvage the deliverable it
had written, continue**).

**DEFAULTS_TAKEN:**
- *release regressions unmeasurable under concurrent subagent writes* → **proceed and declare**;
  safe because LINT, the publication gate, receipts, growth anchors and tool routing were all
  measured clean on the exact landed tree, and because the alternative — idling the Scientists to
  get a clean tree — trades science for a measurement. **What would have been different:** a
  verified release-suite state at session end.
- *a Scientist terminated mid-task on a rate limit* → **take the deliverable it had already
  written, verify its claims independently, continue**; safe because the file was complete and its
  two headline claims were re-verified from source. **What would have been different:** nothing —
  the two false alarms in its list were caught by the ordinary check.
- *six candidates accumulated, `≥5` is a `legend-commit` trigger* → **do not propagate**; safe
  because the operator authorises routine propagation *"where existing repository rules permit"*,
  and these touch canonical files, one lowers a safety score, and their author is not their
  reviewer. **What would have been different:** the corrections would be live rather than queued.

**DECISIONS_TAKEN:** node selection (a fresh scout, rejecting the previous run's proposed wave, on
expected therapeutic information gain rather than paper count) · two harness repairs at T0 with
regressions · refusal to grade `TX-007`'s progenitor caveat by genotype class despite the
favourable reading being available · refusal to bulk-create ~300 corpus placeholders · removal of
a contact e-mail from a public file. All reversible; all recorded in the commits that carry them.

---

*No canonical scientific current file was edited by this run. Not medical advice.*

---

## Append-only correction — the one gate this diagnosis left unverified is now measured

**Added after the diagnosis above, same session.** The *Scope* section recorded
`run_release_regressions.py` as **unmeasurable**, because its guard reports *"WROTE 1 tracked
file(s) under a guarded tree"* whenever a Scientist writes its deliverable mid-run, and Scientists
were writing for most of the session. That was true when written, and it was the honest thing to
declare. **It was not a reason to leave it there.**

With every Scientist idle and the tree clean, the run completed and named **exactly two** failures —
**no write-guard noise at all**, which independently confirms the earlier six were concurrency
artefacts rather than defects:

| Suite | Cause | Mine? |
|---|---|---|
| `framework/scripts/test_batch_queue.py` | `batch_queue.md` is a **derived surface** and drifted the moment this session added six commit candidates | 🔴 **yes** |
| `scripts/test_release_surface.py` | the three scripts shipped this run carry shebangs and **were not executable** | 🔴 **yes** |

**Both repaired**: `batch_queue.py --out …` regenerated the surface (**regenerate, never edit** —
the same rule the sixteen locator counts are about, arriving from the other direction, and here the
derivation was already wired so it cost one command rather than a commit candidate); `chmod +x` on
the three scripts. **`test_release_surface` 11/11 · `test_batch_queue` 49/49 · LINT PASS ·
publication gate PASS / 0 blocks.**

### What this does to the census above

🔴 **It adds two incidents, both `self`, and it changes the shape of the finding rather than the
count's flattery.** Both were **my own defects**, neither was an environment absence, and **neither
would have been found without the clean measurement I had declared impossible.** The diagnosis
above was right to record the gate as unverified and wrong to leave it as a standing condition —
*"cannot be measured while the lab is running"* is an argument for measuring it when the lab stops,
not for not measuring it.

```
ATTRIBUTION_CENSUS (revised)
incidents: 12
machine: 3   blind_auditor: 0   peer: 1   self: 8
severity_high: 2   of which self: 1
undetected_known: 0
```

**`machine` moves 1 → 3.** The two repairs above were caught by **executable suites**, not by
reading — which lifts the machine-caught share from **one in ten to one in four** and is the single
most encouraging number in this diagnosis. The self-caught share is unchanged in absolute terms;
what changed is that the denominator grew in the right column.

🔵 **The lesson is narrow and worth keeping:** *a measurement that concurrency makes impossible is
not an unmeasurable quantity — it is a measurement with a scheduling constraint.* This run declared
the constraint and then, with an hour of quiet, simply took the measurement.
