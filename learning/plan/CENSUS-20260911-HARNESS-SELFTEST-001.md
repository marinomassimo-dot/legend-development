# Attribution census — `HARNESS-SELFTEST-001`, 2026-09-11

**Actor:** `plan` · **Task:** `HARNESS-SELFTEST-001` · **Recorded by:** `orchestrator`

**Provenance.** Persisted verbatim from the actor's closing report, under §21c's safe default for
reports that exist only in a transcript; the same block is in the task JSON (`83edd70`). Not re-graded.

**Task:** close the scripts blind on both self-test axes — 10 → 0 from the meta-test's own output,
two tool defects fixed with the cases that exposed them, 79 of 79 mutations killed.

**The actor's own reading.** The high-severity incident is its own: the mutation matrix wrote
`touched` into 54 real dossiers and made a dry run write a real manifest, caught by the actor
(`git status` after a killed mutant) and restored by the coordinator while the actor's session was
dead. Self-attributed, first and unprompted, on resumption. The correction it shipped refuses the
write before the bytes land rather than recording it afterwards.

```
ATTRIBUTION_CENSUS
incidents: 6
machine: 2   blind_auditor: 0   peer: 1   self: 3
severity_high: 1   of which self: 1
undetected_known: 0
```
