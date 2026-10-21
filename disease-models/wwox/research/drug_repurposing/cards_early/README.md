# cards_early — first candidate cards for the BENEFICIO_PRECOCE path

> **Owner** `scientist-d`, task `REPURP-10H-P4-EARLY-D-20261022`, 2026-10-21. This subdirectory is
> written by one actor; the deep-recovery cards live in `cards/` (scientist-a) and are not touched.
> **Non-canonical, hypothesis-grade (IPOTESI).** Nothing here touches the four scientific current files or
> `disease_model.md`. **Nothing here is medical advice.** A card supports a discussion with a treating
> clinical team and never substitutes for one. This is **public, disease-level and de-identified**.

## What a card is here

Previously qualified material shaped so that a decision can be made about it, and so that **what is not
known stays visible**. This is not a literature sweep: no paper was newly read for these cards. Every card
rests on a repository note, claim, lead or dismissal entry, and every adjacent source stays labelled
**NOT WWOX EVIDENCE**.

Each candidate has two files:

| File | What it is |
|---|---|
| `<id>.packet.json` | The input packet in the shape of `framework/scripts/repurposing_bridge.py` (schema 1): one `disease_assertion`, the `drug_assertions`, `label_lookup`, `p4_fields`, plus the extra blocks the bridge keeps verbatim under `input`: `p4_roadmap_fields` (the 19 roadmap P4 rows that have no bridge field), `not_known`, `evaluation_frame`, `must_never`, `card_kind` |
| `<id>.card.json` | The card **the unmodified bridge builds** from the packet, byte for byte |

`check_cards.py` rebuilds every card from its packet and compares, then checks the rules below. Regenerate
one card with `python3 framework/scripts/repurposing_bridge.py <id>.packet.json > <id>.card.json`.

## The nine cards (three candidates, six abstentions)

Time to access and time to benefit are separate fields on every card; both are UNKNOWN on every card.
Label search: `NOT_ATTEMPTED` on every card (see defaults). The clinical census carries its own caution:
no registered WOREE interventional study on ClinicalTrials.gov v2 on 2026-10-20, and a missing hit is not
proof that none exists.

| Card | Kind | The ONE endpoint it pursues | Status | What is NOT known (headline) |
|---|---|---|---|---|
| `EB-KD-01` ketogenic diet | candidate | clinician-reported seizure control (symptomatic only) | IPOTESI | the number of children placed on the diet; any seizure count, latency or duration; the reference genotype class (no diet entry); the text says two of the five patients were previously published and the table makes patients 2 and 4 the candidates (an inference; the source does not name them), so a pooled count may double-count them; development unchanged in every column and two of the three responders had died |
| `EB-VGB-01` vigabatrin | candidate | clinical cessation of epileptic spasms with a stated criterion | CONTROVERSA | electrographic outcome in any WWOX report; whether hormonal therapy was concurrent in the WWOX MRI-abnormality reports (the anchor has no receipt); the exposure limit (VABAM) is on the same card as the efficacy reports; CLAIM 031 forbids reading any of it as disease modification |
| `EB-ETX-01` ethosuximide (T-type contrast, DL-MECH-170) | candidate | late-phase PTZ-provoked seizure score in an interaction-tested three-genotype design (preclinical; no human endpoint defined) | IPOTESI | the drug-by-genotype interaction; exact mouse age (preweaning per the R2 note); any T-type current or protein measurement in a Wwox system (an mRNA observation exists); a class-level developmental safety signal (research T-type blockers reduce progenitor viability in vitro, not ethosuximide) |
| `EB-GROWTH-AX-01` growth | abstention | head circumference, height, weight against age-expected SD scores | ASTENSIONE | the growth values (the held extraction strips signs and ranges) and any intervention measured against them |
| `EB-DEV-AX-01` development / disease modification | abstention | a within-patient developmental measure against a repeated baseline | ASTENSIONE | any developmental instrument ever applied in a WWOX cohort; untreated scatter |
| `EB-PDANCHOR-AX-01` pharmacodynamic anchor | abstention | none can be named | ASTENSIONE | a calibrated WWOX read-out with a limit of detection in a living-patient matrix (CLAIM 046) |
| `EB-HORM-AX-01` ACTH, corticosteroids, phenobarbital regimens | abstention | spasm cessation, if a comparator exists | ASTENSIONE | a defined response and a matched West-syndrome base rate |
| `EB-CBD-AX-01` cannabidiol | abstention | seizure control, if a response is first defined | ASTENSIONE | any WWOX-system test of cannabidiol; a review sentence attributes an organoid effect to WWOX-deficient organoids and its own citation does not support it |
| `EB-MTOR-AX-01` mTOR-inhibitor class | abstention | none supported | ASTENSIONE | direction of mTOR activity in a WWOX system; the infant safety record is in tuberous sclerosis and does not transfer |

**The T-type card and the R2 note.** The R2 note has landed on `main` (integration commit `190b389e`; closure
commit `743f9914`, three blind audits collected at closure). Its narrowing of DL-MECH-170 and its wording repairs
remain owed a blind audit by someone else, and the card carries that narrowing as **proposed and unaudited**.
Section 28 of that note (an mRNA observation in an adult P47T knock-in hippocampus) is carried on the card.
**2026-10-22 repair:** after the blind audit of these cards the packets were corrected as the audit named (the
repairs are themselves unaudited): the KD source-naming sentence is now an inference; the VGB shared-origin
and sign handling; the ETX dependency; and the evaluation frame's categorical negatives are restated as
'not established here'.

## The evaluation frame (R4 note, DESIGN TABLES A and B)

Carried identically in every packet under `evaluation_frame`. A WOREE evaluation would have to measure a
repeated pre-dose baseline in an instrument form that can move, a pharmacodynamic anchor (which does not
exist: CLAIM 046), one prespecified endpoint with a rescue or withdrawal rule, survival, and seizures only as
a separate declared family. It could **not** claim disease modification or developmental benefit, nor that
seizure control protects development (CLAIM 031), nor benefit from a pharmacodynamic move, a global
impression or an own-baseline comparison, nor any effect smaller than the instrument's untreated scatter.
That frame is `INFERENZA` from precedents in other diseases.

## How to read a bridge result on these cards

The bridge's `directional_summary` is `UNRESOLVED` on all nine, and that is the intended reading: it is
what the cards are designed to show. `OPPOSES_DISEASE_CHANGE` on `A-KD-1` or on `A-VGB-1..3` is a sign
comparison on one endpoint in one source, **not efficacy**: the diet comparison is a single series, and
`A-VGB-1` and `A-VGB-2` come from one report that describes two children: one reporting origin, two patients (corrected 2026-10-22; the earlier wording conflated report and patient). The
assertions that make the card unresolved (other genotype class, other endpoint, harm, development) were
**put in on purpose**, so that the unmeasured cells sit beside the measured one.

## Gaps in the bridge that these cards exposed (not patched; the bridge belongs to a Harness agent)

1. **No sign for "no change".** `SIGNS` has INCREASE, DECREASE, UNKNOWN. A reported null effect (two
   vigabatrin reports; the identical development row of the diet series) can only be encoded UNKNOWN, which
   conflates *no effect found* with *not measured*. Exposed by `EB-VGB-01` (`A-VGB-5`, `A-VGB-6`).
2. **`translation` is hard-coded UNKNOWN and cannot be filled.** `access` and `time_to_benefit` are in the
   card, but nothing in the packet reaches them, so a card whose packet states a qualified time to access and a
   separate time to benefit still prints `UNKNOWN` in the place a reader looks first. The two time fields
   survive only under `input.p4_roadmap_fields`. Exposed by all three candidate cards.
3. **Only three P4 text fields and the cellular-context block are validated.** The other 19 roadmap rows
   survive as unvalidated extras, so the UNKNOWN-rather-than-absent rule cannot be enforced by the bridge;
   `check_cards.py` enforces it from outside.
4. **No distinct abstention state.** `abstention` only means an empty assertion list; "abstention naming the
   missing datum" has no field, and a `disease_assertion` is mandatory even for an endpoint or assay axis with
   no disease direction (the abstention cards carry an honest UNKNOWN one).
5. **Shared origin is not grouped.** Two assertions from one paper both count as OPPOSES in `comparisons`; the
   limits line says shared sources are not independent but nothing in the structure shows which.
6. **No evidence-class field.** NOT WWOX EVIDENCE is only enforceable through `context.disease_id` and an extra
   key; the bridge would accept an adjacent-disease assertion as comparable if its context strings matched.
7. **`endpoint_pursued` is free text**, neither checked against the disease assertion's endpoint nor required
   to name one endpoint.

A context value such as `NOT_APPLICABLE_WHOLE_ORGANISM` for a whole-organism endpoint passes the bridge's
"UNKNOWN blocks the comparison" rule by being a string; that is an author's choice and is stated on each
assertion, not a bridge property.

## Rules the cards obey, and what enforces them

| Rule | Enforced by |
|---|---|
| No score, rank, probability or blended index; no dose, route, schedule or paediatric suitability | `check_cards.py` (keys and dose-like quantities) and the bridge's own rejection of unknown keys in its two blocks |
| Quotes verbatim, never stitched with an ellipsis | `check_cards.py` finds every «quoted» passage in the repository source files |
| Non-WWOX sources labelled | `check_cards.py` (label required when the context is outside WWOX) |
| No e-mail string, no truncated digest | `check_cards.py` |
| A missing hit is not proof of absence; `NOT_ATTEMPTED` is not `NO_MATCH_FOUND` | the bridge's `limits` lines on every card |
| Symptomatic benefit is not disease modification | `evaluation_frame`, `must_never` and each card's expected-contribution row |

`check_cards.py` verifies that cards are well formed. It does not verify that they are true.

## Defaults taken and owed work

* **Label search not attempted** on any card: no label client exists in the repository, the bridge has no
  network, and a new external lookup was outside this task. `NOT_ATTEMPTED` is stated, never `NO_MATCH_FOUND`.
* **No new reading and no receipt.** Where an assertion rests on a reading by another actor the receipt id is
  quoted; none was recorded or staged here.
* **Blind audit OWED on every card**, by someone other than the author, with priority on: the "double-counted
  published individuals" sentence on `EB-KD-01`, the shared-origin handling on `EB-VGB-01`, and the T-type
  card's use of the unaudited R2 narrowing. The first audit (2026-10-22) is in `page_adjudications/locator_audit_R4_cards_20261022.md`.
* Mechanical check: `python3 check_cards.py`; `--extra-source <path>` is no longer needed for the R2 note, which has landed.
