# COMMIT CANDIDATE — CC-20260914-PLACEHOLDER-IDENTITY-01

**Actor:** `orchestrator` · **Date:** 2026-09-14, **rewritten the same day after `SCI-CONSULT-20260914`**
**Mandate:** `SCIENCE-EXEC-20260914` step I2 · **Class:** MINOR · **Scientific delta:** none — no promotion, no claim link
Public, disease-level, de-identified. **Nothing here is medical advice.**

> 🔴 **This candidate's first version was wrong and the consultation refused it.** It claimed that
> `CORPUS P363` and `CORPUS P295` "do not say" the promotion happened. They do: each carries a
> `Resolved (BATCH_20260806_002)` field naming the `PAPER` record and its receipt, two lines below
> the stale sentence my measurement had quoted. My census read the `Status` field only. Both records
> are removed from the subjects, and the census is re-run below with its rules published.

## 1 · The census, with its exclusion rules stated

1. Population: PMIDs with `evidence_depth == complete_fulltext_read` in `fulltext_read_receipts.jsonl`,
   keyed on `study_id.pmid` (87 PMIDs).
2. Registry records parsed with `coverage_report.parse_entries` (the shared parser).
3. A record's PMIDs are the 7–8-digit runs of its `Identifier` field **only**.
4. "States the promotion" = anywhere in the **whole record body**: promoted, superseded, audit trail,
   do not duplicate, Resolved, duplicate of, normalized to.
5. **No status value is excluded**, and `deep-dived` is counted separately (class B below), because it
   records that a reading happened without naming which record is live.

Result: **37** placeholder/`PAPER` pairs on a completed read — **35** state it under these rules and
**2** say nothing at all. The consultation's Identifier-keyed join gave 45 / 40 / 5; the difference is
the rule set, not the records, and both rule sets are now published (see class B).

### Class A — silent records, the subjects of this candidate

| PMID | Placeholder | Owning record | Current `Status` |
|---|---|---|---|
| 21115974 | `CORPUS P305` | `PAPER 086` | screened — corpus placeholder |
| 36828035 | `CORPUS-STUB-053` | `PAPER 007` | not_processed |

### Class B — the rule disagreement, stated instead of a verdict

**Empty under my rules, and that is the disagreement.** The consultation named `CORPUS P182`
(30619736 → `PAPER 032`) and `CORPUS P210` (34634460 → `PAPER 031`) as silent, and as the sharper
harm — `P182` is the interactome placeholder behind `CLAIM 026`. Under the rules published above they
count as **stating it**, because each body contains *"normalized to [[paper_registry_current#PAPER
032]]"* — my rule 4 accepts "normalized to" as a statement of which record is live.

🔴 **Which reading is right is a real question and I do not settle it here.** *"deep-dived — registry
placeholder (lint restored)"* in the `Status` field, with the pointer only in another field, is
exactly the shape that made my own first census wrong in the opposite direction. Both records are
therefore **routed as their own item**, not annotated in this candidate and not declared clean: their
status was set by a LINT repair, and changing it without reading that repair's record risks undoing a
deliberate act.

## 2 · The proposed change — class A only, in the form the other records use

For each class-A record, set `Status` to the dominant marked form, which names **the act that did it**:

> `promoted — see `paper_registry_current#PAPER <n>` (wikilink placeholder) (`BATCH_<id>`, `CC-20260914-PLACEHOLDER-IDENTITY-01`); placeholder kept as audit trail, do not duplicate`

and neutralise the field that would otherwise stay false beside it:

> `**Next action:** none — promotion completed; see the PAPER record`

`Claim links` stays `none`: filling it would be the promotion that was refused. No pathway,
transferability, relevance or role is written.

## 3 · 🔴 Collision to resolve before propagation

`CORPUS-STUB-053` is named in five other candidates on disk, and `CC-20260826-PROVENANCE-01` §A
proposes writing its identity as part of the `PAPER 007` repair. Two candidates writing one record in
different batches is the collision class worth checking at a 45-candidate backlog. **Either** this
candidate defers `CORPUS-STUB-053` to `PROVENANCE-01` §A, **or** §A is propagated first and this
candidate annotates only `CORPUS P305`. Not decidable here without the `PAPER 007` decision, and
recorded rather than assumed.

## 4 · Predicted measurable effect

**No LINT delta:** `legend_lint` validates `Status` for `CLAIM` and `PAPER` kinds only, which is why
existing free-text *"promoted — see …"* strings pass. `growth_anchors` unchanged (corpus counts
headings). `support_linkage` unchanged. `public_release_gate` PASS · BLOCKS 0. **Falsifier:** any LINT
change after this lands means something outside these records moved.

---

## BATCH DISPOSITION — appended by the integrator, append-only

**Status:** **RE-QUEUED** — recovered 2026-09-26 from the VPS backup (`06ee25a`). The VPS batch that disposed of this candidate never reached `main`: re-queued for `BATCH_20260926_ALDAZ`. Identifiers written on the VPS are annotated in place as `(VPS numbering)` / `(VPS batch, never on main)`; full-text queue ids were renumbered (see `disease-models/wwox/research/vps_recovery_20260925/README.md`).
