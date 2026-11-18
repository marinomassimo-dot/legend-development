# Harness freeze digests received from HE and committed before any run (SCI, 2026-11-16; non-canonical)
Model and scans are the files of commit 9c22f6bd7bc41645c084bc99be700b10b247ca1a; each sha256 below was recomputed here and matches HE's message.
| file | sha256 |
|---|---|
| i1_harness_model.py | 7a58ce61288ccefe01ef6d4d8c313db6264c2c7e707a24dba007e5530156c3a9 |
| rebound_oscillator.py | c050b8ff0a1ba8fe5ef340f2a57168ecf578f161be12392c42fec98851b89419 |
| scan_oat.json | f54cca677e99d6fdc77b50203b067a9f072004f2ba7efaf4bb3b6d9f7f3628de |
| scan_grid.json | 2f857a13c7fa2fcaaf3ac596680e435175605dc8b9c16574b071b2ae1236c46d |
| scan_lhs.json | 5b0675455800590488894d6b8a03ea9f19259a75c9d20a31b95d7467b05206a5 |
Freeze digests (sha256 of freeze.json), 20 seeds, base seed 20261116 for all three: OAT e955e10f0e58eca3c1f94fdefe6116ae505a5630304af2cd98c1288a170326db (19 points, 380 calls); GRID 633ceb6145c20ebceb434f9bf9b44aa4fab49bd03d721ed05972c27edbdc0661 (6 points, 120 calls); LHS d00933d8c14b3e7767c604827b94ad03c79336601e021ef74d43d30a471dd809 (64 points, 1280 calls).
Note from HE, accepted: 10 of the 64 LHS points lie outside the adapter's declared bounds (0.5 to 1.5 times the default; the LHS J_T range is 0.2 to 0.4 against a default of 0.275); they run as specified.
Predictions in the scans: S1 to S7 (replications of the exploratory scan with fresh seeds), G1 (post-hoc extension), G2 (replication); the LHS has none.
