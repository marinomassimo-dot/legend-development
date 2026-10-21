# P4 early-benefit cards: what was made, what the cards make visible, what the bridge could not carry

> **Actor** `scientist-d` - **Task** `REPURP-10H-P4-EARLY-D-20261022` - 2026-10-21. Non-canonical research record. It touches none of the four scientific current files, `disease_model.md`, `repurposing_bridge.py` or any file of `drug_repurposing/` outside `cards_early/`.
>
> **Every adjacent source named below is NOT WWOX EVIDENCE.** No dose, route, schedule or paediatric suitability is carried or presumed for anything; accessibility of a diet, drug or supplement does not prove paediatric suitability. Nothing here is medical advice; it supports discussion with a treating clinical team and never substitutes for one.
>
> **Context policy** `QUESTION_DRIVEN`: the R4 note (mine), the early-benefit note, the known-roads note, the R3 note and, from its branch, the R2 note were read first and are held. **No paper was newly read and no receipt was recorded or staged.** The brief said a card is previously qualified material shaped for a decision; that is what was done.

## 1. Output

Nine cards under `disease-models/wwox/research/drug_repurposing/cards_early/` (packet plus the card the unmodified bridge builds from it, a README and a mechanical checker). **Three candidate cards** (ketogenic diet, vigabatrin, ethosuximide as the T-type contrast) and **six abstention cards** (growth axis, development or disease-modification axis, pharmacodynamic anchor axis, hormonal and phenobarbital regimens, cannabidiol, mTOR-inhibitor class). The table of the nine, with the ONE endpoint each pursues and what is not known, is in the README of that directory and is not repeated here.

## 2. What the cards make visible that a one-line summary would not

1. **The diet card.** The only human signal in WOREE has no denominator, no count, no latency, an identical developmental row in every column, two of three responders who had died, and two of the three responders (patients 2 and 4) who are previously published individuals named by the source. The reference genotype class has no diet entry at all.
2. **The vigabatrin card.** Efficacy and exposure limit sit on one card. Two reports of no effect and one of clinical freedom with persisting electrographic attacks cannot be signed in the bridge (gap 1 below), which is itself informative about how often this literature records the null.
3. **The T-type card.** Against the lead as filed ("the drug the paper did not favour behaved genotype-specifically"), the card carries the R2 re-reading: late-phase restriction, a control-cohort difference as large as the effect, non-T-type routes for the drug in other models and no T-type measurement in any Wwox system. That narrowing is **unaudited** (declared OWED in the R2 note) and the card says so. A class-level developmental safety line (research T-type blockers reduce progenitor viability in vitro, ethosuximide untested) is carried as hypothesis-generating only.
4. **The abstentions.** Growth is the first plausible endpoint row, and the datum that blocks it is a native surface of one article. Development, the pharmacodynamic anchor, hormonal regimens, cannabidiol and the mTOR class each name the missing datum. The mTOR card shows that an infant safety record can exist while the benefit axis is empty: safety visibility is not candidacy.

## 3. Gaps in the bridge exposed by the cards (not patched)

Full list of seven in the README. The two that matter most: **(1) no "no change" sign**, so a reported null effect and an unmeasured cell are both UNKNOWN; **(2) `translation` is hard-coded UNKNOWN and nothing in a packet reaches it**, so time to access and time to benefit, which the roadmap requires apart, cannot appear in the card's own translation block and live only under `input`. Also: the 19 roadmap rows without a bridge field cannot be validated by it; abstention has no state of its own; shared origin is not grouped; no evidence-class field. A Harness agent owns `repurposing_bridge.py`; this note and the README are the record.

## 4. DEFAULTS_TAKEN

| Condition | Default | Why safe |
|---|---|---|
| No label client exists and the bridge has no network | `label_lookup` omitted, so `NOT_ATTEMPTED` on all nine; never `NO_MATCH_FOUND` | the state says no search was run, which is true |
| R2 note not on `main` | built the T-type card from the branch copy (`task/repurp-10h-r2-b`, commit `2de3fd28`), narrowing carried as proposed and unaudited, citations by section number | the card is labelled; a section-number check is owed after landing |
| The bridge needs a `disease_assertion` even for an axis with no disease direction | an honest UNKNOWN assertion | the alternative was to invent a direction |
| The bridge has no field for most roadmap rows | `p4_roadmap_fields`, `not_known`, `evaluation_frame`, `must_never` as extras kept verbatim under `input`; presence enforced by `check_cards.py` | the extras survive unchanged and are checkable |
| Whole-organism endpoints have no cell type | context value `NOT_APPLICABLE_WHOLE_ORGANISM`, stated on each assertion | a context mismatch would have blocked every comparison for a reason that is not biology |
| Mouse age is not carried in the notes read | `developmental_stage: UNKNOWN`, so the T-type comparison is UNRESOLVED | the age is a datum nobody here read |
| The R3 note's mTOR rows belong to the deep path | one abstention card, benefit axis empty, pathway rationale left to the deep-recovery cards | no overlap with `cards/` |
| `session_self_eval.py` returns FAIL on 22 `ORPHAN_COMPLETE_READ` lines | not mine: they are the R3 and R4 receipts awaiting registry records; this task recorded no receipt | reported, not fixed |

## 5. STOP_LOG

No stop. No act reserved to the operator was needed.

## 6. OWED

* Blind audit of every card by someone other than the author, with priority on three sentences: the previously-published-individuals boundary on the diet card, the shared-origin handling on the vigabatrin card, the use of the unaudited R2 narrowing on the T-type card.
* After the R2 note lands: check that the section numbers cited in the T-type packet still point where they say (`check_cards.py --extra-source` is no longer needed once it is on `main`).
* A Harness decision on the seven bridge gaps.
* A blind audit of ten of the R4 manifests is queued by the Orchestrator; none was edited here.

## 7. A question for discussion, never advice

If a native surface of the one WOREE series reporting a response were available: how many children were placed on the diet, what was each child's seizure count before and after it, over what interval, on what co-medication? Until that is read, the three-of-five figure cannot be told apart from the base rate, and none of the three candidate cards can say which early-benefit card, if any, is worth taking to a clinical team as more than a question.
