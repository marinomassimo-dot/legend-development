#!/usr/bin/env python3
"""The control fixtures in `surface_properties.py` must not be real identities.

`check()` opens with a control battery: each property family is exercised against a
value it MUST reject, so that a battery whose families cannot fire is caught reporting
PASS on everything. Those fixture values carry no information beyond "differs from the
required one" — and one of them was, for the life of this branch, the operator's real
personal email address, which every clone of the branch published.

    🔴 The defect was not that the value was wrong. It was that the value was RIGHT
    about a real person. A fixture only has to differ; it must never identify.

This suite pins both halves: the fixtures stay non-identifying, AND the battery stays
able to fire. Testing only the first would let someone satisfy it by making the control
equal to the required value, which silences the battery instead of fixing it.
"""
from __future__ import annotations

import io
import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "surface_properties.py")
APPROVALS = os.path.join(HERE, "cases", "approved_inputs.json")

#: Deliberately matches a DOTLESS domain too (`someone-else@invalid`). Requiring a
#: dot made this scan match nothing at all once the fixture was repaired, and a scan
#: that matches nothing reports clean -- which the positive control below caught.
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+")

#: RFC 2606 reserves these; they can never resolve to a real mailbox. `users.noreply`
#: is GitHub's own non-deliverable identity and is the project's commit identity.
NON_IDENTIFYING = ("invalid", "example", "test", "localhost",
                   "example.com", "example.org", "example.net",
                   "users.noreply.github.com")


def _is_reserved(domain: str) -> bool:
    """RFC 2606 reserves these names at any depth, so `invalid` and `x.invalid` both
    qualify. GitHub's `users.noreply` is non-deliverable by construction."""
    domain = domain.rstrip(".").lower()
    return any(domain == s or domain.endswith("." + s) for s in NON_IDENTIFYING)


class ControlFixturesAreNotRealIdentities(unittest.TestCase):

    def test_no_email_literal_in_the_module_could_reach_a_person(self) -> None:
        found = EMAIL.findall(io.open(SOURCE, encoding="utf-8").read())
        offenders = [a for a in found
                     if not _is_reserved(a.split("@", 1)[1])]
        self.assertEqual(
            offenders, [],
            "email literals that could identify a real person: %r. A control fixture "
            "only has to DIFFER from the required value; use an RFC 2606 reserved "
            "domain such as someone-else@invalid." % offenders)

    def test_the_positive_control_finds_the_addresses_that_are_there(self) -> None:
        """If the regex stopped matching, the test above would pass on anything."""
        found = EMAIL.findall(io.open(SOURCE, encoding="utf-8").read())
        self.assertTrue(found, "no email literal matched at all — the scan is dead, "
                               "and a dead scan reports clean")

    def test_the_identity_control_still_fires(self) -> None:
        """The repair must not silence the battery it was cleaning."""
        source = io.open(SOURCE, encoding="utf-8").read()
        m = re.search(r"'identity':\s*'([^']+)'\s*!=", source)
        self.assertIsNotNone(m, "the identity control is no longer a literal comparison")
        fixture = m.group(1)
        required = json.load(io.open(APPROVALS, encoding="utf-8"))
        required = required["required_surface_constants"]["git_user_email"]
        self.assertNotEqual(
            fixture, required,
            "the identity control fixture equals the required value, so the control "
            "evaluates False and check() returns VOID — the family can no longer fire")


if __name__ == "__main__":
    unittest.main(verbosity=2)
