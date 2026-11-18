# IT57: INV-04 and INV-09 next tests carry the design consequences of the day's strands (2026-11-18)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. No ranking, need, card, tier or direction was changed (order digest of the ranking unchanged, `ff38fcaa61295a5a`).

* `result_it57.md`: the finding (the generator `conditional_proposals.py` reads only registered packages and covers INV-05 and INV-18; the day's strands reached no generation path; the consumer of INV-04 and INV-09 is `investigations.tsv`), the before/after reader test (0 of 8 criteria against 8 of 8, no harm triggered: IMPROVED by the rule fixed beforehand), the trace table, the limits.
* `PREREG_IT57_READER_TEST.md` (criteria, harms and outcome rule hashed before any reader ran, with one dated addendum before reader C), `READER_TASK.txt`, `card_BEFORE.txt`, `card_AFTER.txt`, `card_AFTER2.txt`, `reader_A_BEFORE.md`, `reader_B_AFTER.md`, `reader_C_AFTER2.md` (messages copied unchanged; each read back as claude-sonnet-5-5 on every turn, one turn, no tool use).
* `cells_it57.py` (exact wording), `apply_it57_wording.py` (idempotent, `--check`; edits `investigations.tsv` and `investigations_it20.tsv`), `translate_it57_wording.py` (it, fr, es, de; assistant translations, not native-reviewed).
* Regenerated once, together: `ranking_it8.py run`, `repurposing_view.py i18n --what collect`, `run --lang all`, `run --source shareable --lang all`, `package`. Checks: i18n 0 stale on every language; `audit-shareable` PASS on every page; `check` current.
