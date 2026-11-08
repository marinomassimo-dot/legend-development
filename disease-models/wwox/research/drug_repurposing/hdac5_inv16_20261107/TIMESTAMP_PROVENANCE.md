# Timestamp provenance of the three INV-16 staged receipts (suffix 91)

Corrected by the Orchestrator in IT36, before any of the three was written to the ledger (they were still staged, so no ledger correction record was needed).

What happened. The producer wrote the receipts at 2026-11-08T00:21:27Z (its own `date -u`), with `event_at` 00:22:00Z and `analysis_at` 00:21:00Z, both planned times. The checker passed on those values. The producer then moved both back by one minute (00:21:00Z / 00:20:00Z) so that `event_at` would not lie in the future, and did not rerun the checker. The shifted values were therefore neither the planned times nor the real ones.

Reconstruction (producer transcript, tool-call timestamps; second precision, the start of the call):

| Receipt | `analysis_at` (source access) | `event_at` (receipt written) |
|---|---|---|
| 15280364 | 00:17:47Z, PubMed metadata | 00:21:27Z |
| 17956988 | 00:18:38Z, PMC article page fetched after the Europe PMC full-text route failed at 00:18:30Z | 00:21:27Z |
| 32789766 | 00:19:09Z, PubMed metadata | 00:21:27Z |

Limits. `analysis_at` is the start of the access call, not the end of the reading; the span of reading each source is not recoverable below that. The files in `output/receipts/` and in `receipt_staging/inv16/` carry the same values. The checker passes on the corrected files.

Recorded (IT36, 2026-11-08): the ledger writer sets `event_at` to the moment of recording (about 08:52Z) for every receipt it appends, so the ledger rows carry the recording time as `event_at` and the corrected source-access time as `analysis_at` (second precision). The preparation time, 00:21:27Z, is kept only in this note.
