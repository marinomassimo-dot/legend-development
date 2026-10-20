#!/usr/bin/env python3
"""Regressions for eutils.py — the shared NCBI throttle, back-off and cache (N8, 2026-10-20).

No network: the opener is injected. The throttle is exercised across real processes, because
the defect it answers was per-process pacing that did not add up across four Scientists.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import eutils  # noqa: E402

URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=1"


class SharedThrottle(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        patcher = mock.patch.dict(os.environ, {"LEGEND_EUTILS_DIR": self.tmp.name,
                                               "LEGEND_EUTILS_CACHE_TTL": "0"})
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_four_processes_are_paced_as_one_client(self) -> None:
        code = ("import sys,time; sys.path.insert(0, %r); import eutils; "
                "[eutils.wait_turn(gap=0.2) for _ in range(3)]; print(time.time())") % str(HERE)
        started = time.time()
        procs = [subprocess.Popen([sys.executable, "-c", code], env=dict(os.environ))
                 for _ in range(4)]
        for proc in procs:
            self.assertEqual(0, proc.wait(timeout=60))
        # 12 requests at 0.2 s apart cannot finish in less than 11 gaps.
        self.assertGreaterEqual(time.time() - started, 11 * 0.2 - 0.05)

    def test_a_429_is_retried_with_retry_after_and_a_404_is_not(self) -> None:
        calls = []

        def opener(url, timeout, agent):
            calls.append(agent)
            return (429, b"", {"Retry-After": "0"}) if len(calls) == 1 else (200, b"ok", {})
        with mock.patch.object(eutils.time, "sleep"):
            self.assertEqual((200, b"ok"), eutils.fetch(URL, opener=opener))
        self.assertEqual(["", ""], calls, "empty User-Agent, two attempts")
        missing = []
        with mock.patch.object(eutils.time, "sleep"):
            code, _ = eutils.fetch(URL, opener=lambda *a: missing.append(1) or (404, b"", {}))
        self.assertEqual((404, 1), (code, len(missing)))
        with mock.patch.object(eutils.time, "sleep"):
            with self.assertRaisesRegex(RuntimeError, "HTTP 503"):
                eutils.get(URL, retries=2, opener=lambda *a: (503, b"", {}))

    def test_the_cache_answers_a_second_identical_request(self) -> None:
        calls = []
        with mock.patch.dict(os.environ, {"LEGEND_EUTILS_CACHE_TTL": "3600"}):
            for _ in range(2):
                self.assertEqual(b"body", eutils.get(
                    URL, opener=lambda *a: calls.append(1) or (200, b"body", {})))
        self.assertEqual(1, len(calls))


if __name__ == "__main__":
    unittest.main(verbosity=2)
