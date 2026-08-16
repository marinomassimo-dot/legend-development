---
artifact: LEGEND governance — ANNEX F · CHALLENGE & DISSENT
governance_version: 3.1.1
status: FROZEN
normative: yes
materialized_by: plan
materialized_on: 2026-08-16
materialized_from: operator-supplied annex text, transmitted verbatim
body: GOVERNANCE_v3.1.1.md
---

> **Materialization note (Plan).** The text below is the annex exactly as supplied. Nothing was
> added, summarized or reordered.

---

## ANNEX F — CHALLENGE & DISSENT

### F.1 · Severità

`ADVISORY (comply + record) | MATERIAL (comunica prima; timeout → si procede con la direttiva originale + record) | GOVERNANCE_BLOCK (stop + escalation)`.

### F.2 · ORCHESTRATOR_CHALLENGE

`CHALLENGE_ID / TASK_ID / DIRECTIVE_ID / ISSUE / EVIDENCE / RISK / ALTERNATIVE / SEVERITY`. Aggiudicazione obbligatoria con rationale: `ACCEPT | MODIFY | OVERRIDE_WITH_RATIONALE | ESCALATE`.

### F.3 · Lifecycle

`OPEN → ACCEPTED | OVERRIDDEN → VALIDATED_LATER | INVALIDATED_LATER → PROMOTED_TO_LEARNING | CLOSED`. Mirror: "quali classi di dissent Orchestrator tende a OVERRIDE che poi risultano VALIDATED_LATER?". Ex post, mai veto ex ante.

### F.4 · Non-compliance — con DIAGNOSE

```
ACKed instruction not executed
        ↓
DIAGNOSE (obbligatoria):
  1. delivery/runtime failure? (turno troncato, permission prompt, crash, sessione degradata)
  2. context failure? (rehydration incompleta, generation stale, checkpoint incompatibile [v3.1.1])
  3. task contract ambiguity? (acceptance criteria non verificabili;
     INTERACTION_MODE incoerente col comportamento atteso [v3.1.1])
  4. actual refusal?
        ↓
solo (4), ripetuto dopo chiarimento → NON_COMPLIANT → HUMAN_REQUIRED
(1)-(3) → recovery tecnico / chiarimento contratto, MAI insubordinazione
```
