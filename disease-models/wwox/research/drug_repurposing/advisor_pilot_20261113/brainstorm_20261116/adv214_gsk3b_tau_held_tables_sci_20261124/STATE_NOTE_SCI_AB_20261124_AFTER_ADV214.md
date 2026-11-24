# State note, SCI window AB, after ADV-214 (2026-11-24, written at the request of ADV; idle until ADV names the next item)

Hypothesis level; reference genotype class; nothing is medical advice. Checkpoint AC and its addendum AD are untouched and remain the restart base; this note adds only what happened after addendum AD.

**Bound mandate:** ORCH-SCI-ADV065-DEEPEN-20261118 (worktree `.claude/worktrees/sci_ab_20261123`, session ff316249). Not released; do not write MANDATE_RELEASED unless HE asks. Peers: ADV a5e6f2ad, HE 1d88b230, IT 748d7ec5. ADV picks the next item at the 20:47Z round; successor launch is blocked by the permission control.

**Delivered and on main since addendum AD (all gate PASS):**
| item | folder under brainstorm_20261116/ | disposition |
|---|---|---|
| ADV-210 L-ascorbic acid resume steps 1 and 2 | adv210_ascorbate_resume_sci_20261124 | (c) parked; missing anchor = measured extracellular ascorbate time course in the assay; human SLC23A2 sign halves on CPM normalisation and organoids lack oligodendroglia; mouse sign composition-sensitive but collinear with genotype; CSF baseline abstract-level; receipt FTR-20261124-29423921-02; pointer line in the ascorbic acid README |
| ADV-213 unmapped phenotypes vs the 58 dossiers | adv213_unmapped_phenotypes_sci_20261124 | 16 classes, three ranked gaps (GSK3B-Tau 4, Golgi/glycosylation 3, genome stability 2); recommend S1; drop genome stability; do not extend myelin; shared open anchor across the dossiers |
| ADV-214 GSK3B-Tau held-table search | adv214_gsk3b_tau_held_tables_sci_20261124 | (b) with the searched list; no held phospho-protein table; total proteome GSK3B +0.02; minimum assay named; NOTE_SHARED_ANCHOR for ADV to route |

**Landing recipe that worked today:** merge origin/main; new receipts only with surfaces regenerated (reading_state with --inputs-dirty-because, coverage_report with the same flag, ranking_it8 from its folder, verify); lint 0 BLOCK; reader-journey and unread-gold; then `safe_push.py development main --expect-sha <12> --serialize --regenerate-derived` in the background with a PUSH_EXIT log and a Monitor; gate about 40 min; no worktree edits during the gate.

**Open waits (unchanged):** step L blocked on operator supply of papers; S540E and the E-MTAB-14792 Table EV1 not before 2026-12-06; AES poster 2026-12-05; RP-004 Sze 2004 full text (relevant: wave 1 says it would settle whether the enhanced phosphorylation was pS9 or pY216); RP-038, RP-018, RP-044 parked; sealed ADV-174/175, frozen RP-045 and the ketamine pack not touched.

**Lessons from today (also in memory sci-ab-pitfalls):** read a peer's decision-line format before promising a "Current decision" extraction (2 of 58 matched); a sweep token like "pS9" matches RPS9, so every hit needs the row opened; the human raw-count bulk delta overstates by about 0.4 from depth (use CPM); a peer-named table can be the lane's own earlier work (the i18 proteome was already used by ADV-095).

**For a successor, if one is ever launched:** read checkpoint AC, addendum AD, this note and the three RESULT files; restart line for this window is crossed; ask ADV for the item.
