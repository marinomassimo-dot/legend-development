#!/usr/bin/env python3
"""Regression checks for the public PMC proof-of-work fetcher."""

from __future__ import annotations

import hashlib
import io
import sys
import tempfile
import unittest
import urllib.parse
from contextlib import redirect_stdout
from pathlib import Path

import pmc_pow_fetch as pmc
from pmc_pow_fetch import is_supported_binary, parse_interstitial, solve_pow

PDF = b"%PDF-1.4\n%fixture bytes\n%%EOF\n"
INTERSTITIAL = b"""<html><script>
const POW_CHALLENGE = "fixture:token"
const POW_DIFFICULTY = "1"
const POW_COOKIE_NAME = "cloudpmc-viewer-pow"
</script></html>"""


class _Response:
    def __init__(self, body: bytes, content_type: str, status: int = 200) -> None:
        self.body, self.status = body, status
        self.headers = {"content-type": content_type}

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self) -> bytes:
        return self.body


class _Transport:
    """Stands in for ``urllib.request.urlopen``; keeps every request it was handed."""

    def __init__(self, responses: list[_Response]) -> None:
        self.responses, self.requests = list(responses), []

    def __call__(self, request, timeout=0):
        self.requests.append(request)
        return self.responses.pop(0)

    def header(self, index: int, name: str) -> str | None:
        return dict((k.lower(), v) for k, v in self.requests[index].header_items()).get(name.lower())


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


class TheEntryPointIsDriven(unittest.TestCase):
    """``main`` -> ``fetch`` with the network stubbed at ``urlopen``, so the whole protocol runs.

    The helpers were tested one at a time and the tool — one URL, one output, the cookie it
    sets, what it writes — by nothing (retrospective § 9.3). The stub replaces the wire only:
    ``fetch``, the challenge parse, the solve and the retry are the real code.
    """

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output = Path(self.tmp.name) / "nested" / "out.pdf"
        self._urlopen = pmc.urllib.request.urlopen
        self.addCleanup(setattr, pmc.urllib.request, "urlopen", self._urlopen)

    def run_main(self, transport: _Transport) -> tuple[int, str]:
        pmc.urllib.request.urlopen = transport
        argv, buffer = sys.argv, io.StringIO()
        sys.argv = ["pmc_pow_fetch.py", "https://pmc.example/article.pdf", str(self.output)]
        try:
            with redirect_stdout(buffer):
                code = pmc.main()
        finally:
            sys.argv = argv
        return code, buffer.getvalue()

    def test_a_direct_binary_is_written_and_reported_with_its_digest(self) -> None:
        transport = _Transport([_Response(PDF, "application/pdf")])
        code, out = self.run_main(transport)
        self.assertEqual(code, 0)
        self.assertEqual(self.output.read_bytes(), PDF)
        self.assertIn(f"written: {self.output}", out)
        self.assertIn(f"sha256: {hashlib.sha256(PDF).hexdigest()}", out)
        self.assertIn("pow_used: False", out)
        self.assertEqual(len(transport.requests), 1)
        self.assertEqual(transport.header(0, "User-Agent"), pmc.USER_AGENT)

    def test_the_interstitial_is_solved_and_the_cookie_carries_the_solution(self) -> None:
        transport = _Transport([_Response(INTERSTITIAL, "text/html"),
                                _Response(PDF, "application/pdf")])
        code, out = self.run_main(transport)
        self.assertEqual(code, 0)
        self.assertEqual(self.output.read_bytes(), PDF)
        self.assertIn("pow_used: True", out)
        self.assertIn("difficulty: 1", out)
        self.assertEqual(len(transport.requests), 2)
        cookie = transport.header(1, "Cookie")
        self.assertIsNotNone(cookie)
        name, _, value = cookie.partition("=")
        self.assertEqual(name, "cloudpmc-viewer-pow")
        challenge, nonce = urllib.parse.unquote(value).split(",")
        self.assertEqual(challenge, "fixture:token")
        self.assertTrue(hashlib.sha256(f"{challenge}{nonce}".encode()).hexdigest().startswith("0"))
        self.assertIn(f"nonce: {nonce}", out)

    def test_a_retry_that_is_still_html_is_refused_and_nothing_is_written(self) -> None:
        transport = _Transport([_Response(INTERSTITIAL, "text/html"),
                                _Response(b"<html>still a page</html>", "application/pdf")])
        with self.assertRaisesRegex(ValueError, "not a supported binary"):
            self.run_main(transport)
        self.assertFalse(self.output.exists(), "an HTML page was written as the article")


if __name__ == "__main__":
    unittest.main()
