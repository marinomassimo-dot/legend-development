# Orchestrator self-evaluation — ten-hour repurposing batch (ORCH-REPURPOSING-10H-20261021)

Part 1 (machine): `session_self_eval.py` PASS; receipts verify OK (848 chained); release battery on a fresh
clone of 771155d0: PASS WITH SKIPS (154 targets, 12 environmental skips); gate PASS; pushed and verified.

Part 2 (judgement, process separate from outcome):
- Content held: P5 comparison, GSE156243 qualification, R1c/R1d/R2c–R2f/R4c–R4d readings, cards, strength-scan.
- Process failures: (1) blind audits found adverse rates of 7.2% (R1c/R2c), 11.3% (R1d repairs + first readings;
  15% on first readings), 18.8% on the text control of R2d — repairs always followed audits, the practice
  of the Scientists writing a proposition wider than its quote persists; the word scan has recall 31% only.
  (2) Image reads degraded ("media removed: request limit"); Scientist B wrote figure values after a failed
  read; the auditor could not verify 53 of 84 figure attestations. Owed: rerun in a session where reads work.
  (3) Session limit 429 stopped integrator, auditor and B for about three hours (05:10–08:10 UTC) and the
  hourly watch could not run; the last watch happened at 08:16 UTC, after END. (4) I swapped agent ids earlier
  and repeated a wrong summary; both corrected.
- Caught by others: audits (blind auditors), the battery (Harness reds), the integrator (counts).
- Micro-upgrades delivered: locator_audit --strength-scan, record_staged_receipts.py, docx_media_extract.py,
  paper_packet copy-of-declared-container fix, the repoint of receipt fields. Debt: figure-attestation rerun;
  audits of the 3 R1d corrected entries, R2f repairs and the 21 narrowed R2 entries.
