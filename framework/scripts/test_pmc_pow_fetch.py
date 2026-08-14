#!/usr/bin/env python3
"""Regression checks for the public PMC proof-of-work fetcher."""

from __future__ import annotations

import hashlib
import unittest

from pmc_pow_fetch import is_supported_binary, parse_interstitial, solve_pow


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

    def test_accepts_declared_legacy_office_supplements(self) -> None:
        ole = b"\xd0\xcf\x11\xe0" + b"fixture"
        self.assertTrue(is_supported_binary(ole, "application/msword; charset=utf-8"))
        self.assertTrue(
            is_supported_binary(ole, "application/vnd.ms-powerpoint; charset=utf-8")
        )

    def test_accepts_spreadsheets_and_images_with_matching_magic(self) -> None:
        self.assertTrue(
            is_supported_binary(
                b"PK\x03\x04fixture",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        )
        self.assertTrue(is_supported_binary(b"\xff\xd8\xfffixture", "image/jpeg"))
        self.assertTrue(
            is_supported_binary(b"\x89PNG\r\n\x1a\nfixture", "image/png")
        )

    def test_refuses_html_even_with_a_binary_mime(self) -> None:
        self.assertFalse(is_supported_binary(b"<html>challenge</html>", "application/msword"))


if __name__ == "__main__":
    unittest.main()
