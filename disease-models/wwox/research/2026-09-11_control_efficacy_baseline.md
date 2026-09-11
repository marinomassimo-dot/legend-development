# Control efficacy — the before-picture, measured before any wave uses the new controls

**Written:** 2026-09-11 · **By:** `orchestrator` (`ORCH-SCIENTIST-IMPROVEMENT-20260911`) ·
**Why this file exists:** the pilot results state that **no Scientist wave has yet used** the
controls that landed on 2026-09-10 and 2026-09-11
([`2026-09-10_scientist_pilot_results.md`](../analysis/orchestration_reviews/2026-09-10_scientist_pilot_results.md) § 4).
A control that has never met a real reading has an unknown false-alarm rate and an unknown cost.
This record fixes the **before** measurement so the next wave's **after** is a comparison and not
an impression. It changes nothing and blocks nothing.

---

## 1 · What the validator says about the corpus today

Re-derivable with the snippet in § 4: `deepdive_manifest.validate` run over every live manifest,
with the `warnings` and `ratchets` sinks collected and classed.

| Measure | Value |
|---|---|
| Manifests validated | 81 |
| Structural ERRORs | 0 |
| WARNs — identifier / count provenance undeclared | 40 |
| WARNs — provenance not checkable because the artefact is absent from this checkout | 54 |
| WARNs — `experimental_context` discordance (landed today) | **0** |
| RATCHET — `retraction_check.dependencies` absent | 81 |
| RATCHET — `acquisition_recipe` absent | 77 |

**The number that matters for the new control is the zero.** The false-alarm budget it adds to the
existing corpus is **0 of 81 manifests**, because 0 of 1,458 locator entries declare the field and
the check is silent unless *both* sides of a coupled relation declare it. It cannot become noisy
retroactively; it can only become informative as readers adopt it.

## 1b · The historical case, reproduced on the real manifest

The A9 incident was rebuilt in a **scratch copy** of `PMID15070730.json` — the real document, not a
fixture — by restoring the bridge exactly as it was committed on 2026-09-09: the Fig 6 panel
(`entries[29]`, whose bridge the blind audit withdrew) qualifying the Fig 5 dose sentence
(`entries[17]`), with the systems the dossier records: *"Fig 5 is NIH 3T3 … Fig 6 is the SAOS-2 p21
series."* The validator's answer:

```
BLOCKS: none (by design)
WARN: verbatim_locators.entries[29].experimental_context.cell_line: this `panel_qualifies_text`
      joins two locators measured in different systems — entries[29] declares 'SAOS-2',
      entries[17] declares 'NIH 3T3'.
```

Before 2026-09-11 the same manifest passed with nothing said. **No canonical file was modified**;
the reconstruction lived in memory and is re-derivable from the snippet above plus the dossier's
own § on the withdrawal.

What this does **not** establish: that the reader would have declared the two systems, and that a
declared discordance is illegitimate. The blind audit remains the control that caught the original,
and the warning's own text asks the reader to argue the bridge rather than delete it.

## 2 · What the next wave must report, and against what

Four numbers per wave, each with its denominator. They are the operator's own criterion —
*"errori intercettati, falsi allarmi e tempo aggiunto"* — made countable.

| Quantity | Denominator | Baseline today |
|---|---|---|
| Defects the controls caught before the reading landed | incidents in that wave's self-evaluation | the sweep's own: machines 0 of the 6 near-errors |
| False alarms — a control fired and the reader determined nothing was wrong | times the control fired | unmeasured; the corpus adds 0 `experimental_context` alarms |
| Readings where the pre-landing check refused a commit | readings that edited an existing manifest | `locator_contradiction_audit.py --working-tree` at HEAD: 81 manifests, 0 undeclared revisions |
| Added verification time | wall-clock per paper | `--working-tree` under 2 s over 81 manifests; `--history` ~40 s; the derived-surface guard one `git status` per write |

The controls to exercise, all wired into the entry points the brief's M2/M3 already name:
`deepdive_manifest.py` (contradiction shape, unaudited-contradiction gap, provenance WARN,
`experimental_context` discordance, intrusion check, queue-ID cross-check),
`locator_contradiction_audit.py --working-tree --fail-on-undeclared`, the seven screens' exit
codes, and the derived-surface input guard.

## 3 · A candidate control measured and NOT shipped — caveat preservation

The third priority asked whether qualifications, negatives and genotype survive the passage from
source to table to synthesis (the S3 and S4 shapes: a caveat alive in prose and dead in a table;
`propose` arriving as `conclude`). The obvious detector — compare the qualifier and genotype
vocabulary of a claim against that of the locators of its wikilinked papers, and report what the
evidence carries and the claim does not — was **measured before being built**, as § 9.1 of the
retrospective requires after the prose-grep measurement (261 hits over 1,458 locators).

| Measure | Value |
|---|---|
| Claims with at least one linked, read paper | 29 of 39 |
| Claims the detector would flag | **27 of 29** |
| Claims with no lost token at all | 2 |
| Largest single flag | CLAIM 030, 19 distinct tokens |

**A detector that fires on 93 % of its population is noise**, and it is noise for a structural
reason rather than a tuning one: a claim is a *summary of many locators*, so most qualifier tokens
in the evidence legitimately do not appear in it. Comparing the two vocabularies asks a question
the granularity cannot answer.

🔴 **The finding is the prerequisite, not the detector.** Caveat preservation is checkable only
between *the same passage* before and after synthesis — and that link does not exist: the claim
registry cites **0 locators by `entries[N]`** (it cites 29 PMIDs and 9 receipt IDs), and dossiers
cite one in 6 files of 54. Until a claim names the locator it stands on, no machine can ask
whether that locator's qualification survived. The minimum step is therefore an **addressed
evidence link on the claim**, not a text detector; the check becomes cheap and exact the moment the
address exists, and stays impossible without it.

Recorded as `MEASURED — REJECTED AT THIS GRANULARITY`, with the prerequisite named, rather than
shipped and switched off later.

## 3b · The pilot: a per-paper work packet and one call for the checks

Built 2026-09-11 as `framework/scripts/paper_packet.py`, two subcommands, no new state, reusing
the scripts that already exist. `packet` assembles what the repository knows **technically** about
one PMID — identity, artefacts with digests verified rather than quoted, what a prior receipt
covered and which sections a resume owes, which acquisition routes were already tried and what
each returned, which checks the actual surfaces make runnable. `check` runs the runnable ones in
one call, prints one line each and writes the full output to `files/check_runs/` (gitignored), so
it is read only when a check has something to say.

**The firewall is the load-bearing part.** `scientist_reading_modes.md` § 3.1 gives the reader the
source packet *"and nothing else about the paper"*, and § 3.3 forbids reading prior LEGEND output
during a blind first pass. The packet therefore carries no claim, no dossier, no commit candidate,
no prior locator and no interpretation, and the regression asserts the absence against the real
claim registry and the real manifest rather than trusting the docstring. A context saving that
arrives as anticipation of the laboratory's conclusions is not a saving.

**Measured on five real papers**, the commands run back to back:

| | Value |
|---|---|
| Compact output returned to the reader, 5 papers, packet + check | 10,400 characters |
| Full check output written to disk instead | 16,019 characters |
| Technical calls a reader makes | 2 per paper, against 5–7 run separately before |
| Wall clock, all ten commands | 13.4 s |
| Packet assembly | 0.1 s per paper |

🔴 **No saving percentage is claimed, and the reason is in the record.** These are characters of
tool output and counts of calls, not provider-billed tokens: the earlier startup-context audit
measured text sizes and not consumption
([`learning/plan/SLR-plan-20260909-startup-context-audit.md`](../../../learning/plan/SLR-plan-20260909-startup-context-audit.md)).
What can be said honestly is the shape of the change: the same facts now arrive once, in a fixed
compact form, instead of being re-derived by reading registries into the reading context, and the
verbose half of every check stays on disk unless a verdict sends the reader to it.

**What the first real wave must report against § 2**, now that the instrument exists: the four
numbers there, plus input and output tokens with cached tokens separated where the provider's
telemetry gives them. Until then this is an instrument with a measured cost and an unmeasured
benefit, and it is recorded as such.

## 4 · Re-deriving § 1 and § 3

```bash
python3 - <<'PY'
import json, glob, sys, collections, re
sys.path.insert(0, 'framework/scripts'); import deepdive_manifest as g
from pathlib import Path
warn = collections.Counter(); ratch = collections.Counter(); n = 0
for p in sorted(glob.glob('disease-models/wwox/research/deepdive_manifests/PMID*.json')):
    n += 1; w = []; r = []
    errors, _ = g.validate(json.load(open(p)), root=Path('.'), warnings=w, ratchets=r)
    for x in w: warn[re.sub(r'\[\d+\]', '[N]', x.split(':')[0])] += 1
    for x in r: ratch[x.split(':')[0]] += 1
print(n, dict(warn), dict(ratch))
PY
```

The § 3 probe is deliberately not kept as a script: a rejected detector left executable in
`framework/scripts/` is a detector someone runs.
