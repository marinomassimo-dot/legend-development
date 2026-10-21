# Repair of the deep-recovery cards after the blind audit

> **Actor** `scientist-a`, 2026-10-22. Non-canonical research record. **Not medical advice.** No dose,
> route, schedule or paediatric suitability. Every adjacent source is NOT WWOX EVIDENCE. The repair is
> **not certified by its author**; a second blind pass by someone else is OWED.

Source of the defects: `page_adjudications/locator_audit_deep_cards_20261022.md` (109 claims: 75
supported, 13 overshoot, 5 undershoot, 16 unverifiable). Repaired in the packets, cards rebuilt with
`repurposing_bridge.py`, `cards/check_cards.py`: 12 packets, 0 problems. No manifest was changed, so no
`contradicts_locator` is owed.

## 1 · What changed, by card

| Card | Repair |
|---|---|
| A01, A02 | "six measured divergences" replaced by a wording that counts nothing; `formal_checks` now says the R1 audit has run (95 triples) and its repairs are unaudited |
| A02 | `DR-A02-003` direction NO_CHANGE becomes UNKNOWN (activity could not be measured, which is not a measured null); "inactive" replaced in five places; "undetectable" replaced by "barely detectable (about 3 percent of control)"; the "normal mRNA" label carries the R1 repair |
| A03, A04, A05 | search records now name the query, source, date (session clock 2026-10-21) and limits, and say "not established here"; A03 no longer says "no ligand": one unreplicated crude-extract steroid-substrate screen exists and is not a binder; A04 records that the ER idea is an unmeasured Discussion remark in the first Q230P report and that the only measured route for a sibling SDR missense is lysosomal; A05 records the HSC70 co-immunoprecipitation with one missense variant and no manipulation; "inactive" corrected |
| B01 | `DR-B01-002` retargeted to the phenotypic endpoint so the FANCA protein induction (about 9 percent) is stated and not hidden under NO_CHANGE; the 57 percent null/null figure is located (56.8 percent in the abstract of the 2025 Neurology cohort) and flagged as a pooled null class, not a nonsense count |
| B02 | the zero is bounded to the WWOX-literature body sweep; the two repository documents that do name a read-through class are cited |
| C01 | survival wording follows the CLAIM 011 adjudication (a step and a steep continuum are indistinguishable; step strengthened, not established); replication negative scoped to the repository; internal contradiction removed |
| C02 | the antisense zero is bounded to the 20-record census set; the two repository papers with an antisense construct or a morpholino are named |
| D01 | withdrawn "sub-proportional" replaced; the DL-MECH-086 sentence (about WWOX re-expression) removed; "normalised" replaced by the ledger word; "stated, not demonstrated" added for Myc; the R3 audit is described as run |
| D02 | "never administered" reconciled with D01 (CK1-alpha-inhibiting compound in knockout organoids) and with an acute GSK3-inhibitor administration in knockout mice with a measured GSK3 phospho-state (read from the stored text) |

## 2 · What a card author must check by hand, and what a Harness check could do mechanically

`check_cards.py` passed every defective card because it tests form. The hand checks that remain, with a
proposed mechanical form of each (a proposal, not code):

1. **Verbatim quotation**: every quoted string of twelve characters or more must occur in a named
   repository file. Mechanical: the audit's own extraction script, run in CI over `drug_repurposing/`.
2. **Repaired versus withdrawn wording**: keep a small file of withdrawn phrases, each with the document that
   withdrew it (for example "sub-proportional", "inactive" next to ASPA, "threshold, not a continuum",
   "six measured divergences"); fail a packet that contains one. Mechanical and cheap; it would have caught five of the eight defects.
3. **Stale status lines**: a phrase such as "audit is running", "OWED" or "proposed" next to a record that
   exists. Mechanical: match the phrase against `page_adjudications/` and the claim registry.
4. **Negative scope**: a negative (`NON_TROVATO`, "0 across") must carry a query, a source, a date and a
   limit. Mechanical: a field-presence check on the search record; the audit found three that were not searches.
5. **Direction codes**: a measured null (`NO_CHANGE`) must not sit on a source sentence that says "could not
   be measured". Mechanical: flag a `NO_CHANGE` whose note contains "not measur" or "could not".
6. **Internal consistency between cards**: a claim of "never administered" against a sibling card that
   records an administration. Mechanical: only partially; a shared list of administered agents per system would do it.
7. **Receipt content and digests**: check that a cited receipt names the cited paper and its manifest verifies
   (`deepdive_manifest.py --verify-artifacts`), not only that the id string exists.
8. **Source support** of a synthesis sentence cannot be made mechanical; it stays a blind human audit.

## 3 · Self-evaluation (honest)

The cards were written from the notes of the day and not re-read against the repairs that landed during the
build, which is the staleness no structural check sees. I trusted a counted phrase ("six") and a status line
("running in parallel") that I had not re-derived. The upgrade is item 2 and 3 above, which is cheap.
`DEFAULTS_TAKEN`: dates use the session clock; the queries named in A03 to A05 were run by me and are
title/abstract only. `STOP_LOG`: empty.

## 4 · Findings from the paused abstention-gap search that bear on the cards (not yet a full note)

Work paused for this repair; the gap-fill task is resumed on its own branch. Findings so far, each from a
source opened this session: a read-through context paper read in full (aminoglycoside data, NOT WWOX
EVIDENCE; manifest PASS, receipt staged) ranks UGA over UAG over UAA and a pyrimidine at the position after the stop above a
purine; a census I derived from the repository's ClinVar table and the RefSeq coding sequence lists 32
single-nucleotide nonsense entries, 20 with G after the stop; a sibling SDR missense (P252A) is lost
through a lysosome-sensitive route and is not raised by a proteasome inhibitor, which the A02 card does not carry.
