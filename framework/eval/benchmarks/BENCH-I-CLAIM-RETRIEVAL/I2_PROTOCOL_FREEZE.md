# Benchmark I · I2 — protocol freeze (recorded before the first model run)

> Harness evidence, non-scientific. Complements [`PREREGISTRATION.md`](PREREGISTRATION.md) § 5;
> where they differ, this file records what was actually fixed at execution.

| Item | Value |
|---|---|
| Eligible fixtures | 21 (18 STRONG + 3 USABLE_WITH_LIMITATION whose every target PROGRESSIVE retrieved in the frozen I1) + the I00 no-change control = **22**. No further selection. |
| Excluded by I1 (retrieval failures, not attention questions) | I03, I06, I09, I24 |
| Arms | **A** whole claim registry at the event's parent · **C** preamble + PROGRESSIVE records, whole, in registry order |
| Shared text | the same system prompt, `PMID <P>` line, snippet seed and task (hashes in [`i2_contexts.json`](i2_contexts.json): `system_sha256`, `task_sha256`, and one `prompt_sha256` per fixture × arm) |
| Model | `claude-opus-5-5` |
| Runner | `claude -p --model claude-opus-5-5 --tools "" --strict-mcp-config --setting-sources "" --no-session-persistence --output-format json --system-prompt <SYSTEM>`, prompt on stdin, an empty temporary working directory per call; Claude Code 2.1.282 |
| Stochastic setting | temperature / top-p **not exposed** by the runner; provider defaults; effort = CLI default |
| Repetitions | **3** per fixture per arm → **132** independent calls |
| Order | the full job list shuffled with `random.Random(20260925)`; 4 concurrent workers |
| Retry | one retry of a call that errors, recorded (`retried`); a second failure is a failure, not re-sampled |
| Token accounting | native, from the runner's `modelUsage[claude-opus-5-5]` (input + cache read + cache write). The CLI also makes a small auxiliary call on another model; it is excluded and never mixed in |
| Grading | deterministic exact `CLAIM nnn` match, blind (opaque job id; arm joined after scoring); no model grader |
| Context size (median over the 21 target fixtures) | A 97,830 B / 39 records · C 83,704 B / 33 records (C/A 0.87); control I00: A 97,830 B · C 19,807 B |

A pre-run check was made on a trivial non-fixture prompt only (`Reply with exactly: RUNNER_OK`),
to confirm the model id resolves; no fixture prompt was sent before this file was committed.
