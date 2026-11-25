# Publication gate: the three cross-file scans run in a second process (HE 9c2cb46c, 2026-11-25)

ADV GO with five conditions, 2026-11-25. Report on stdout unchanged; harness only.

## What changed

`scripts/public_release_gate.py`: the links, provenance and README scans run in a forked process beside the privacy
scan. Findings are joined in the old order. `LEGEND_GATE_SERIAL=1` runs them in one process. Each full run says on
stderr which way it ran (`GATE_SIDE_SCANS:`), and `safe_push.py` copies that line and any `GATE_ERROR:` into the
landing log. The pre-check is unchanged.

## Fail closed

A second process that raises, is killed, exits without a result, returns a cut result or a bad wait status makes the
gate exit 3, with no VERDICT. It never falls back after it has started. Only when no second process can be started
(no `fork`, or `fork` fails) do the scans run serially; the line says `FALLBACK` and the serial result is the one
reported. A killed gate takes the second process with it (Linux).

Tests: `SideScanTests` in `scripts/test_public_release_gate.py` (a planted tree with the six BLOCK codes of the four
scans, report equal to the serial one; nine failure modes; the opt-out line) and one test in `test_safe_push.py`.

## Measured before the change (prototype, same logic)

Five runs per arm beside a landing-like load with 0 to 4 other real pushes: serial median 122.3 s (102.6 to 142.0),
two processes 83.2 s (76.6 to 112.6); stdout byte identical in all ten runs and on the planted tree.

On the final code, one run each on the worktree: serial 126 s, two processes 65 s, both PASS, stdout identical.

## What it is worth, and what it is not

The landing lock gets shorter **only when the gate is the longest of the parallel landing checks** (3 of 4 pushes of
HE on 2026-11-25). When the suites are longer the lock does not move. Expected about 30 s per push on average; this
figure is **not counted** until the read of the first ten landings.

## Read of the first ten landings (open)

For each of the first ten published commits after the change: the old serial gate and the new one on that commit,
outside the lock, stdout compared byte for byte
(`files/coordination/he_gate_proto_20261125/read_ten_landings.sh`). Any difference stops the change: revert the
commit. Lock-held seconds and gate seconds are read from the same ten logs.
