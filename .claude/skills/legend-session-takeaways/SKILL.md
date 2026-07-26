---
name: legend-session-takeaways
description: 'Mandatory communicative closing for LEGEND sessions: synthesizes for the operator what the session learned, which useful leads emerge for the disease model/WWOX, biomarkers, therapies, drug repurposing, strategy, inferences, data and next steps. Uses compact, tabular, fluid output with icons and immediate takeaways. Always use it at the end of a LEGEND session, after the operational tasks and after/together with legend-capability-scout, even if the operator does not name it.'
---

# legend-session-takeaways — Cognitive closing for the operator

## Purpose

Return to the operator, at the end of a session, the cognitive value that would otherwise stay fragmented across processes, logs, scripts, lint, commit candidates and internal analyses.

This skill does not modify canonical current files and creates no claims. It is a communicative synthesis: what we learned, what matters, what it suggests for the disease model, and which leads deserve attention.

## Mandatory rule

At the end of every LEGEND session, beyond the completed technical tasks, return a final `Session takeaway` section.

For an analytical batch or full-text run, this skill is downstream of
`framework/protocols/session_self_evaluation.md`. Do not compose a green summary before the
executable checks and written diagnosis. The closing must state any blocked check, skipped
or waived analytical obligation, process failure/retry, residual debt and the concrete
micro-upgrade it caused. A polished summary must never erase a failed diagnosis.

It must be:
- concise;
- tabular when useful;
- readable in 30-60 seconds;
- high information density;
- oriented to the disease model/WWOX, biomarkers, therapies, drug repurposing, strategy, safety, inferences, data;
- clear on what is `DATO`, `INFERENZA`, `IPOTESI`, `ESPANSIONE`.

Use icons soberly to guide the eye. Avoid long text.

## Sources of the synthesis

Collect only from what happened in the session:
- studies triaged or analyzed;
- reports generated;
- new candidates, discoveries, insights or conflicts;
- lint/test/script results;
- updates to skills, agents, repos, procedures;
- leads that emerged from reasoning;
- limits, uncertainties, next questions.

Do not invent content. If a point is only a hypothesis, mark it.

## Recommended format

Use this schema when the session has scientific or strategic content:

```markdown
**Session Takeaway**

| Area | What emerged | Why it matters | State |
|---|---|---|---|
| 🧬 Disease model/WWOX | ... | ... | IPOTESI/INFERENZA |
| 🧪 Biomarkers | ... | ... | DATO/INFERENZA |
| 💊 Therapies/repurposing | ... | ... | IPOTESI |
| 🧭 Strategy | ... | ... | INFERENZA |
| 🛠️ Repo capability | ... | ... | OPERATIONAL |

**3 things to remember**
1. ...
2. ...
3. ...

**Next useful step**
...
```

If the session is purely technical/administrative, use the short version:

```markdown
**Session Takeaway**

| What improved | Impact | Next step |
|---|---|---|
| ... | ... | ... |
```

## Categories to consider

- 🧬 **Disease model/alleles/phenotype:** Q230P, c.1057-2A>G, WOREE/SCAR12, seizures, development, glia, myelin, excitability.
- 🧪 **Biomarkers/endpoints:** WWOX-linked biomarkers, cellular proxies, clinical endpoints, experimental readability.
- 💊 **Therapies/repurposing:** drugs, chaperones, lithium/GSK3b, MYC/WNT, neuroinflammation, Zfra/peptides, ASO/SSO, AAV/GT, window protection.
- 🧠 **Inferences/mechanisms:** pathways, interactome, stress response, p73/p53, HIF1A, JNK, tau, microglia, metabolism.
- 🧭 **Strategy:** evolutionary priorities, what to analyze next, what to down-rank, what to monitor.
- 🛠️ **Repo capability:** skills, agents, scripts, imported repos, process improvements.
- ⚠️ **Safety/uncertainty:** limits, false-positive risk, what is not yet demonstrated, what requires a clinician/treating team.

## Style

- English (or the operator's working language).
- Short sentences.
- No sermons.
- Prefer tables, 3 strong bullets, keywords.
- Do not exceed 1 screen unless requested.
- Highlight practical value: "why it matters".
- If there is a strong insight, put it on top.

## Guardrails

- Do not present IPOTESI as DATO.
- Do not give medical advice.
- Do not turn takeaways into canonical claims.
- Do not cite every technical detail: choose what helps the operator understand and decide.
- If the session was long, prioritize high-impact leads and defer the rest to the files/reports.

## Minimal closing

Every LEGEND session final response must include at least:
- what was done;
- what was learned;
- 1-3 useful leads for the disease model or the strategy;
- the self-diagnosis verdict and any declared gap;
- micro-upgrade/capability gained, if any;
- recommended next step.
