#!/usr/bin/env python3
"""The consolidated view must be deterministic, lossless, and must refuse a real conflict.

The fixtures here are the THREE REAL LINEAGES, reduced to their structural skeleton: the same
identities, states, timestamps and lineage membership, with the long rationale prose replaced.
That keeps every property the consolidator reasons about — byte-identity of the shared prefix,
date-only precision on most records, date-disjoint suffixes — without pinning the test to prose
that is free to be reworded.

🔴 Every test that asserts a good outcome is paired with an arm that breaks the property and
requires the outcome to change. A determinism test that only ever sees deterministic input is a
test of nothing.
"""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from consolidate_approval_queue import (  # noqa: E402
    ConflictError, SourceError, consolidate, identity, timestamp,
)

HEADER = {"_schema": "LEGEND governance v3.1.1 · Annex J.3 HUMAN_APPROVAL_QUEUE",
          "_domain": "CONTROL PLANE"}


def approval(ident, when, state, precision_note=True):
    record = {"APPROVAL_ID": ident, "REQUESTED_AT": when, "STATE": state,
              "RATIONALE": f"structural fixture for {ident}"}
    if precision_note:
        record["TIMESTAMP_PRECISION"] = "date only — the runtime exposed no wall-clock time"
    return record


def resolution(ident, resolves, when, state):
    return {"RESOLUTION_ID": ident, "RESOLVES_APPROVAL_ID": resolves,
            "RESOLVED_AT": when, "STATE": state}


# --- the shared prefix: byte-identical in all three lineages -------------------------------
PREFIX = [
    HEADER,
    approval("APR-20260816-GOV311-001", "2026-08-16", "PENDING"),
    resolution("RES-20260816-GOV311-001", "APR-20260816-GOV311-001", "2026-08-16", "APPROVED"),
    approval("APR-20260816-GOV311-002", "2026-08-16", "PENDING"),
    resolution("RES-20260816-GOV311-002", "APR-20260816-GOV311-002", "2026-08-16", "APPROVED"),
    {"CORRECTION_ID": "COR-20260816-GOV311-001", "RECORDED_AT": "2026-08-16"},
]

L1 = copy.deepcopy(PREFIX)

L2 = copy.deepcopy(PREFIX) + [
    approval(f"APR-20260817-HA-{n}", "2026-08-17", "PENDING") for n in (1, 2, 3, 4)
] + [
    resolution(f"RES-20260817-HA-{n}", f"APR-20260817-HA-{n}", "2026-08-17", s)
    for n, s in ((1, "APPROVED"), (2, "DEFERRED"), (3, "RESOLVED"), (4, "DEFERRED"))
]

L3 = copy.deepcopy(PREFIX) + [
    approval("APR-20260818-SUNSET-DEC3-001", "2026-08-18", "APPROVED"),
    approval("APR-20260819-SCIAB-001", "2026-08-19T13:02:58Z", "APPROVED", precision_note=False),
    approval("APR-20260819-XPORT-001", "2026-08-19T17:05:17Z", "APPROVED", precision_note=False),
    approval("APR-20260819-P5DOMAIN-001", "2026-08-19T20:06:42Z", "APPROVED",
             precision_note=False),
]

SOURCES = {"L1": L1, "L2": L2, "L3": L3}


def fingerprint(records):
    return hashlib.sha256(
        "\n".join(json.dumps(r, sort_keys=True) for r in records).encode()).hexdigest()


class TheFixtureMatchesTheRealShape(unittest.TestCase):
    """If these drift, every test below is measuring something else."""

    def test_the_short_lineage_is_a_prefix_of_both_others(self):
        self.assertEqual(L2[:len(L1)], L1)
        self.assertEqual(L3[:len(L1)], L1)

    def test_the_suffixes_are_date_disjoint(self):
        days = lambda recs: {timestamp(r)[:10] for r in recs[len(L1):]}  # noqa: E731
        self.assertEqual(days(L2) & days(L3), set())

    def test_most_records_carry_a_date_only_timestamp(self):
        stamped = [timestamp(r) for src in SOURCES.values() for r in src if timestamp(r)]
        date_only = [t for t in stamped if "T" not in t]
        self.assertGreater(len(date_only), len(stamped) - len(date_only),
                           "the ordering problem this tool exists for has vanished")


class TheViewIsDeterministic(unittest.TestCase):
    def test_every_order_of_supplying_the_lineages_agrees(self):
        seen = set()
        for order in itertools.permutations(SOURCES):
            records, _, _ = consolidate({k: SOURCES[k] for k in order})
            seen.add(fingerprint(records))
        self.assertEqual(len(seen), 1, "the union depends on the order the lineages arrive in")

    def test_position_inside_a_lineage_is_load_bearing_and_that_is_declared(self):
        """The declared limitation, asserted so it cannot silently stop being true.

        Most records share a day, so their relative order comes from their position in an
        append-only file. Reversing that order MUST change the view — if it did not, the
        consolidator would be inventing an order the sources do not carry.
        """
        canonical, _, _ = consolidate(SOURCES)
        reversed_inputs = {k: list(reversed(v)) for k, v in SOURCES.items()}
        shuffled, _, _ = consolidate(reversed_inputs)
        self.assertNotEqual(fingerprint(canonical), fingerprint(shuffled))


class TheViewIsLossless(unittest.TestCase):
    def test_every_input_record_reaches_the_view(self):
        records, _, _ = consolidate(SOURCES)
        out = {identity(r) for r in records}
        for lineage, source in SOURCES.items():
            for record in source:
                self.assertIn(identity(record), out, f"{lineage} lost {identity(record)}")

    def test_the_shared_prefix_is_deduped_exactly_once(self):
        records, provenance, _ = consolidate(SOURCES)
        self.assertEqual(len(records), 18)
        shared = [p for p in provenance if len(p["lineages"]) == 3]
        self.assertEqual(len(shared), len(PREFIX))

    def test_the_four_approvals_that_live_on_one_ref_survive(self):
        """The whole point: an approval must not be invisible for living on a side ref."""
        records, _, _ = consolidate(SOURCES)
        out = {identity(r) for r in records}
        for ident in ("APR-20260818-SUNSET-DEC3-001", "APR-20260819-SCIAB-001",
                      "APR-20260819-XPORT-001", "APR-20260819-P5DOMAIN-001"):
            self.assertIn(ident, out)


class ProvenanceIsPreservedWithoutTouchingTheRecords(unittest.TestCase):
    def test_records_are_returned_unmodified(self):
        before = json.dumps(SOURCES, sort_keys=True)
        consolidate(SOURCES)
        self.assertEqual(before, json.dumps(SOURCES, sort_keys=True))

    def test_no_provenance_field_is_injected_into_any_record(self):
        records, _, _ = consolidate(SOURCES)
        for record in records:
            self.assertNotIn("lineages", record)
            self.assertNotIn("_lineage", record)

    def test_the_sidecar_names_every_lineage_a_record_came_from(self):
        _, provenance, _ = consolidate(SOURCES)
        by_id = {p["identity"]: p for p in provenance}
        self.assertEqual(by_id["APR-20260816-GOV311-001"]["lineages"], ["L1", "L2", "L3"])
        self.assertEqual(by_id["APR-20260819-XPORT-001"]["lineages"], ["L3"])
        self.assertEqual(by_id["APR-20260817-HA-1"]["lineages"], ["L2"])


class AConflictIsRefused(unittest.TestCase):
    def test_one_identity_with_two_different_bodies_does_not_merge(self):
        poisoned = copy.deepcopy(SOURCES)
        poisoned["L3"][1]["RATIONALE"] = "this lineage disagrees about an approved record"
        with self.assertRaises(ConflictError) as caught:
            consolidate(poisoned)
        self.assertIn("APR-20260816-GOV311-001", str(caught.exception))

    def test_the_same_call_succeeds_without_the_mutation(self):
        """The control. Without it the test above could be passing for any reason at all."""
        records, _, _ = consolidate(copy.deepcopy(SOURCES))
        self.assertEqual(len(records), 18)

    def test_a_state_change_alone_is_enough_to_conflict(self):
        poisoned = copy.deepcopy(SOURCES)
        poisoned["L2"][2]["STATE"] = "REJECTED"
        with self.assertRaises(ConflictError):
            consolidate(poisoned)


class RecordsWithoutADeclaredIdentity(unittest.TestCase):
    def test_an_unidentified_record_is_kept_and_content_addressed(self):
        extra = {"RATIONALE": "no id field of any kind", "REQUESTED_AT": "2026-08-20"}
        sources = copy.deepcopy(SOURCES)
        sources["L2"] = sources["L2"] + [extra]
        records, _, _ = consolidate(sources)
        self.assertIn(identity(extra), {identity(r) for r in records})

    def test_two_identical_unidentified_records_collapse_rather_than_duplicate(self):
        extra = {"RATIONALE": "no id field of any kind", "REQUESTED_AT": "2026-08-20"}
        sources = copy.deepcopy(SOURCES)
        sources["L2"] = sources["L2"] + [copy.deepcopy(extra)]
        sources["L3"] = sources["L3"] + [copy.deepcopy(extra)]
        records, _, _ = consolidate(sources)
        self.assertEqual(sum(1 for r in records if identity(r) == identity(extra)), 1)


class HostileInputs(unittest.TestCase):
    """Nine adversarial cases. Five of them found a real defect; all nine are held here.

    🔴 The distinction these tests enforce is between a CONFLICT and a SOURCE ERROR. A conflict
    means two lineages disagree about an approval and only a human can choose. A source error
    means one file is malformed or contradicts itself, and there is nothing to choose between.
    Reporting the second as the first sends a typo to an operator as a decision.
    """

    def test_an_exact_duplicate_inside_one_lineage_collapses(self):
        sources = copy.deepcopy(SOURCES)
        sources["L2"] = sources["L2"] + [copy.deepcopy(sources["L2"][1])]
        records, _, _ = consolidate(sources)
        self.assertEqual(len(records), 18)

    def test_a_lineage_contradicting_ITSELF_is_a_source_error_not_a_conflict(self):
        """It said "Two lineages disagree" and printed "differs between L2 and L2"."""
        sources = copy.deepcopy(SOURCES)
        sources["L2"] = sources["L2"] + [
            {"APPROVAL_ID": "APR-ONLY-HERE", "REQUESTED_AT": "2026-08-17", "STATE": "PENDING"},
            {"APPROVAL_ID": "APR-ONLY-HERE", "REQUESTED_AT": "2026-08-17", "STATE": "APPROVED"},
        ]
        with self.assertRaises(SourceError) as caught:
            consolidate(sources)
        self.assertIn("appears twice inside L2", str(caught.exception))

    def test_a_cross_lineage_disagreement_is_still_a_conflict(self):
        """The control for the test above: the two must not collapse into one class."""
        sources = copy.deepcopy(SOURCES)
        sources["L3"][1]["RATIONALE"] = "L3 disagrees"
        with self.assertRaises(ConflictError):
            consolidate(sources)

    def test_a_non_object_record_is_refused_rather_than_crashing(self):
        sources = copy.deepcopy(SOURCES)
        sources["L2"] = sources["L2"] + ["this is a string, not an object"]
        with self.assertRaises(SourceError):
            consolidate(sources)

    def test_a_non_string_timestamp_is_refused_rather_than_sorted_first(self):
        """🔴 `20260817` became `""`, and `""` sorts before every real date.

        The record whose date could not be read was emitted at position 1, ahead of every
        record whose date was legible. The tool was ordering by whether it could parse the
        timestamp, and saying nothing about it.
        """
        sources = copy.deepcopy(SOURCES)
        sources["L2"] = sources["L2"] + [{"APPROVAL_ID": "APR-BAD-TS", "REQUESTED_AT": 20260817}]
        with self.assertRaises(SourceError) as caught:
            consolidate(sources)
        self.assertIn("not a string", str(caught.exception))

    def test_a_record_declaring_no_timestamp_at_all_is_still_allowed(self):
        """The control: absent is not the same as unreadable, and only one is an error."""
        sources = copy.deepcopy(SOURCES)
        sources["L2"] = sources["L2"] + [{"APPROVAL_ID": "APR-NO-TS", "STATE": "PENDING"}]
        records, _, _ = consolidate(sources)
        self.assertIn("APR-NO-TS", {identity(r) for r in records})

    def test_lineages_sharing_no_record_are_reported_and_not_refused(self):
        """Two disjoint append-only files ARE unitable. Doing it silently is what is not."""
        left = {"L1": copy.deepcopy(SOURCES["L1"])}
        right = {"LX": [r for r in copy.deepcopy(SOURCES["L2"]) if "_schema" not in r][6:]}
        records, _, warnings = consolidate({**left, **right})
        self.assertTrue(records)
        self.assertTrue(any("share no record" in w for w in warnings), warnings)

    def test_overlapping_lineages_produce_no_such_warning(self):
        """The control. Without it the warning could be firing on every input."""
        _, _, warnings = consolidate(copy.deepcopy(SOURCES))
        self.assertEqual(warnings, [])

    def test_an_unknown_STATE_is_carried_through_untouched(self):
        """The consolidator unites records; it does not police a vocabulary it does not own."""
        sources = copy.deepcopy(SOURCES)
        odd = {"APPROVAL_ID": "APR-ODD", "REQUESTED_AT": "2026-08-20", "STATE": "MOON_PHASE"}
        sources["L2"] = sources["L2"] + [odd]
        records, provenance, _ = consolidate(sources)
        self.assertIn(odd, records)
        self.assertEqual(next(p for p in provenance if p["identity"] == "APR-ODD")["state"],
                         "MOON_PHASE")

    def test_an_unexpected_future_field_is_carried_through_untouched(self):
        sources = copy.deepcopy(SOURCES)
        future = {"APPROVAL_ID": "APR-FUTURE", "REQUESTED_AT": "2026-08-20",
                  "FIELD_FROM_A_LATER_SCHEMA": {"nested": [1, 2]}}
        sources["L2"] = sources["L2"] + [future]
        records, _, _ = consolidate(sources)
        self.assertIn(future, records)

    def test_the_sort_invents_no_order_among_same_day_records(self):
        """Three records, one day, no time: the emitted order must be the file order.

        If it came out sorted by id, the tool would be asserting a sequence the schema does
        not carry — which is the failure this whole ordering design exists to avoid.
        """
        sources = copy.deepcopy(SOURCES)
        tie = [{"APPROVAL_ID": f"APR-20260817-TIE-{n}", "REQUESTED_AT": "2026-08-17",
                "STATE": "PENDING"} for n in (3, 1, 2)]
        sources["L2"] = sources["L2"] + tie
        records, _, _ = consolidate(sources)
        emitted = [identity(r) for r in records if "TIE" in identity(r)]
        self.assertEqual(emitted, [t["APPROVAL_ID"] for t in tie])
        self.assertNotEqual(emitted, sorted(emitted))


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
