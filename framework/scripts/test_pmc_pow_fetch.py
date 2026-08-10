#!/usr/bin/env python3
"""Regression checks for the public PMC proof-of-work fetcher."""

from __future__ import annotations

import hashlib
import unittest

from pmc_pow_fetch import parse_interstitial, solve_pow


class PmcPowFetchTest(unittest.TestCase):
    def test_parses_declared_challenge(self) -> None:
        page = b'''<script>
        const POW_CHALLENGE = "fixture:token"
        const POW_DIFFICULTY = "3"
        const POW_COOKIE_NAME = "cloudpmc-viewer-pow"
        </script>'''
        self.assertEqual(
            parse_interstitial(page), ("fixture:token", 3, "cloudpmc-viewer-pow")
        )

    def test_solution_satisfies_declared_difficulty(self) -> None:
        nonce, digest = solve_pow("fixture:token", 3)
        self.assertTrue(digest.startswith("000"))
        self.assertEqual(
            digest, hashlib.sha256(f"fixture:token{nonce}".encode()).hexdigest()
        )

    def test_unrecognised_page_is_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "neither the requested binary"):
            parse_interstitial(b"<html>ordinary error</html>")


if __name__ == "__main__":
    unittest.main()
