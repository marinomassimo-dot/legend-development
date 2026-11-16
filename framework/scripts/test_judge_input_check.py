#!/usr/bin/env python3
"""Regressions for judge_input_check.py: the 2026-11-16 invalid judge run reproduced on a fixture with no model call."""
import hashlib, subprocess, sys, tempfile, unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "judge_input_check.py"
REPO = Path(__file__).resolve().parents[2]
BODY = "The knockout network fails the homeostatic response to its own bursting; rejecting observation: the burst rate does not rise with age. " * 6


def run(*args: str):
    return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True)


def original() -> str:
    """Two authors' files in the shapes of the round: a heading with the body on the next lines, and a one-paragraph hypothesis whose perspective label sits on the SAME line as its text."""
    return (f"## H1. Title one\nPerspective used: data and measurement.\n{BODY}\n\n"
            f"## H2. Perspective used: ion gradients. Statement: {BODY}\n")


def faulty_anonymiser(text: str) -> str:
    """What produced run 1: delete every line that contains the word."""
    return "\n".join(l for l in text.splitlines() if "Perspective" not in l) + "\n"


def fixed_anonymiser(text: str) -> str:
    """The repair: remove the perspective line and only the inline label span."""
    out = []
    for l in text.splitlines():
        if l.startswith("Perspective used:"):
            continue
        out.append(l.replace("Perspective used: ion gradients. Statement: ", ""))
    return "\n".join(out) + "\n"


def number(text: str) -> str:
    """Relabel to the judge's J ids."""
    return text.replace("## H1.", "## J01.").replace("## H2.", "## J02.")


class JudgeInputCheck(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def write(self, name: str, text: str) -> str:
        p = self.tmp / name
        p.write_text(text, encoding="utf-8")
        return str(p)

    def test_the_faulty_anonymiser_of_2026_11_16_is_refused_before_any_judge_runs(self) -> None:
        bad = self.write("bad.md", number(faulty_anonymiser(original())))
        r = run("--input", bad, "--forbidden", "Perspective", "--expect-blocks", "2")
        self.assertEqual(r.returncode, 1)
        self.assertIn("1 blocks found, 2 expected", r.stderr)                    # the one-paragraph hypothesis lost its heading line altogether (J02 absent)
        self.assertIn("no judge should be launched", r.stdout)
        titled = self.write("titled.md", number(original()).replace("Perspective used: data and measurement.\n", "").replace(BODY, "", 1))     # a title with its body deleted (the other shape of the same defect)
        r2 = run("--input", titled, "--expect-blocks", "2")
        self.assertEqual(r2.returncode, 1); self.assertIn("below the floor", r2.stderr)

    def test_the_repaired_anonymiser_passes(self) -> None:
        good = self.write("good.md", number(fixed_anonymiser(original())))
        r = run("--input", good, "--forbidden", "Perspective,ion gradients")
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        self.assertIn("complete by the stated thresholds", r.stdout)

    def test_a_manifest_of_original_lengths_catches_a_partial_loss_that_the_floor_misses(self) -> None:
        orig = original()
        manifest = self.write("m.tsv", "block_id\toriginal_chars\nJ01\t%d\nJ02\t%d\n" % (len(BODY) * 3, len(BODY)))       # J01 originally three times longer
        r = run("--input", self.write("good.md", number(fixed_anonymiser(orig))), "--manifest", manifest, "--min-share", "0.6")
        self.assertEqual(r.returncode, 1)
        self.assertIn("block J01: kept", r.stderr)
        ok = run("--input", self.write("good2.md", number(fixed_anonymiser(orig))), "--manifest", self.write("m2.tsv", "J01\t%d\nJ02\t%d\n" % (len(BODY), len(BODY))), "--min-share", "0.6")
        self.assertEqual(ok.returncode, 0, ok.stderr)

    def test_a_leftover_label_and_a_changed_criteria_file_are_refused(self) -> None:
        text = self.write("t.md", number(fixed_anonymiser(original())).replace("The knockout", "Perspective: The knockout", 1))
        self.assertEqual(run("--input", text, "--forbidden", "Perspective").returncode, 1)
        crit = self.write("criteria.md", "four yes/no/partial criteria, fixed")
        digest = hashlib.sha256(Path(crit).read_bytes()).hexdigest()
        good = self.write("g.md", number(fixed_anonymiser(original())))
        self.assertEqual(run("--input", good, "--criteria", crit, "--expect-criteria-sha256", digest).returncode, 0)
        Path(crit).write_text("four criteria, one loosened after the first look", encoding="utf-8")
        r = run("--input", good, "--criteria", crit, "--expect-criteria-sha256", digest)
        self.assertEqual(r.returncode, 1); self.assertIn("a change of criteria is a new round", r.stderr)

    def test_the_committed_inputs_of_the_valid_runs_pass_and_help_is_safe(self) -> None:
        real = REPO / "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_leap_judge_20261116/JUDGE_INPUT.md"
        if real.exists():
            r = run("--input", str(real), "--forbidden", "Perspective", "--expect-blocks", "24")
            self.assertEqual(r.returncode, 0, r.stderr)                           # the run-2 input: 24 blocks, the smallest of 809 characters
        self.assertEqual(run("--help").returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
