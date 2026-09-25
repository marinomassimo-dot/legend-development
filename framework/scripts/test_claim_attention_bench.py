#!/usr/bin/env python3
"""Benchmark I · I2 machinery: answer parsing and the blind job list, pinned on toy input.

No model is called here. What is pinned is what decides a score: how an answer is parsed into
claim ids, and that the job list is a fixed, shuffled order whose ids reveal neither the arm nor
the fixture.

Run: `python3 framework/scripts/test_claim_attention_bench.py`
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import claim_attention_bench as bench  # noqa: E402


class Parsing(unittest.TestCase):
    def test_a_fenced_answer_parses_and_ids_are_normalised(self) -> None:
        answer = ('```json\n{"affected": [{"claim_id": "CLAIM 5", "relationship": '
                  '"Narrows / qualifies", "reason": "x"}]}\n```')
        parsed, problem = bench.parse_answer(answer)
        self.assertEqual(problem, "")
        self.assertEqual(parsed, [{"claim_id": "CLAIM 005",
                                   "relationship": "narrows / qualifies"}])

    def test_an_empty_list_is_a_no_change_answer_not_a_failure(self) -> None:
        self.assertEqual(bench.parse_answer('{"affected": []}'), ([], ""))

    def test_prose_is_unparseable_and_says_so(self) -> None:
        parsed, problem = bench.parse_answer("I think CLAIM 005 is affected.")
        self.assertIsNone(parsed)
        self.assertTrue(problem.startswith("unparseable"))


class Jobs(unittest.TestCase):
    CTX = {"fixtures": [{"fixture_id": "X1"}, {"fixture_id": "X2"}]}

    def test_the_order_is_fixed_and_complete(self) -> None:
        first, second = bench.jobs(self.CTX), bench.jobs(self.CTX)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 2 * 2 * bench.REPETITIONS)
        self.assertEqual(len({j["job_id"] for j in first}), len(first))

    def test_a_job_id_reveals_neither_arm_nor_fixture(self) -> None:
        import re
        for job in bench.jobs(self.CTX):
            self.assertRegex(job["job_id"], r"^J[0-9a-f]{10}$")


class Cli(unittest.TestCase):
    def test_invalid_action_is_exit_two(self) -> None:
        done = subprocess.run([sys.executable, str(HERE / "claim_attention_bench.py"), "nope"],
                              capture_output=True, text=True)
        self.assertEqual(done.returncode, 2)


if __name__ == "__main__":
    unittest.main()
