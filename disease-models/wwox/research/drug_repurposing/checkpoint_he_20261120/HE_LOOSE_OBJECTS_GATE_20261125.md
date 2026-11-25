# Suite clone objects and gate seconds per check (HE 9c2cb46c, 2026-11-25). Report only; nothing changed

Asked by ADV. Two measurements of the landing path.

## 1 Decision on the suite clone: KEEP `--no-hardlinks`

**ADV, 2026-11-25: NO GO on a hard-linked or alternates clone. Measured: the saving is below the cost of the risk.**
The saving is a transient 0.7 GiB per push and at most 1.4 s; free space is 20 GB. Do not reopen without a new
reason; the one ADV names is free space under 8 GB. No prune of the unreachable objects either.

Method: pre-registered; two throwaway copies of the shared `.git` (the live one only read), peak scratch 2.25 GiB,
removed by the same command chain; three rounds with the arm order rotated; warm cache, load 4.3 to 4.8.

| Arm | Clone recipe | New unique disk | Seconds (median of 3) |
|---|---|---:|---:|
| A (today) | `clone --no-hardlinks` | 1.14 GiB | 3.1 |
| B | the same, from a copy after `git repack -d` | 1.08 GiB | 2.2 |
| C | default local clone (`.git/objects` hard-linked) | 0.43 GiB | 1.7 |
| D | `clone --shared` (alternates) | 0.43 GiB | 1.7 |

* **Rejected prediction:** B was expected to save at least 200 MiB and saved 65 MB. Of 4,532 loose objects 2,260 are
  unreachable (320 of 399 MiB); `repack -d` cannot pack them, and removing them is a prune, an irreversible deletion.
* D failure probe, on a toy repository: source `repack -a -d` and `gc` with default expiry leave the clone working;
  reflog expiry followed by `prune --expire=now` of an object the clone needs kills it (`fatal: bad object HEAD`).
  A hard-linked clone survives that.
* C risk: object inodes are shared with the live store. git does not rewrite an object in place; a test that changed
  the mode of one and rewrote it would damage the live store. A grep of the `test_*.py` files showed no writer of
  `.git/objects`, which is not proof.
* Not measured: C or D under landing contention, and the landing suites under either.

Evidence: `files/coordination/he_loose_objects_20261125/`.

## 2 Gate seconds per check

**Premise corrected.** Landings do not use the gate's cache: `safe_push` starts the gate without `--cache` and
`LEGEND_GATE_CACHE` is unset. The opt-in cache is keyed on the whole gate script's bytes and the Python version; what
is keyed on the scan's own digest is the search guards (bb3c81129). Using the cache on a push is the operator's
decision (`framework/scripts/README.md`, the gate cache row; design note ADV-057; decision item 9).

Method: the gate's own `main()` with each top-level check timed, run on one clean checkout of 6ec3693ad, five runs
back to back, load 3.6 to 8.5; the cache runs used a private cache file in the job folder. All five outputs are byte
identical.

| Check, seconds | no cache (as landings), 2 runs | warm private cache, 2 runs | cold private cache, 1 run |
|---|---|---|---|
| total | 130, 113 | 34, 41 | 116 |
| privacy scan | 100, 74 | 3, 4 | 85 |
| README consistency | 23, 31 | 24, 27 | 23 |
| links | 5, 6 | 5, 7 | 5 |
| provenance | 3, 2 | 2, 3 | 2 |

* Top two: the privacy scan and the README consistency check.
* The estimate behind decision item 9 today: about 80 s less per landing with a warm cache.
* Inside the README consistency check (two more timings): the `patient_markers` search over a joined corpus of
  286 million characters takes 16 to 17 s and matches nothing on this tree; the two tree walks take 1 to 3 s each,
  reading and joining the corpus about 1 s.

Equivalent forms of that search, one run, nothing applied: the six alternatives searched one at a time sum to 18.5 s
against 17.7 s combined (no gain); the first alternative with its literal moved before the look-behind takes 0.35 s
against 4.9 s, but that timing was taken **without** the original case flag, so it is not yet an equivalence.

Evidence: `files/coordination/he_gate_checks_20261125/`.
