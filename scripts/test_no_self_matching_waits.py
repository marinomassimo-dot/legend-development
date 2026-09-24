#!/usr/bin/env python3
"""No repository-owned wait loop may use a process NAME as its exit condition.

The defect this pins recurred three times (2026-09-22 twice, 2026-09-24 once): a waiter
looping on `pgrep -f <job>` had `<job>` in its own command line, matched itself, and waited
hours for itself. Waiting now has one sanctioned route — framework/scripts/process_wait.py,
by PID, PID:START, pid file or completion file, always with a timeout.

Scope is deliberately narrow, so this does not become a shell-style linter:
  - shell: tracked `.sh`/`.bash` files and files with a sh/bash shebang — a `while`/`until`
    loop whose CONDITION queries `pgrep -f`/`pkill -f` is a finding (comments are stripped);
  - Python: a `while` loop that runs `pgrep`/`pkill` with `-f` and whose test has no deadline
    (no comparison against time.monotonic()/time.time()) is a finding.
Documentation, comments and this file's own fixtures are not code and are not scanned. The
detector is proven able to fire on planted copies of the real defect before it is trusted.
"""
from __future__ import annotations

import ast
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
EXCLUDED_TREES = ("_external_repos/",)

LOOP = re.compile(r"\b(while|until)\b(?P<cond>[^\n]*?)(?:;\s*do\b|\n\s*do\b)", re.S)
NAME_QUERY = re.compile(r"\bp(?:grep|kill)\b[^;|&\n]*?\s-[A-Za-z]*f")


def shell_code(text: str) -> str:
    """Comment-free text with continuations joined; a shebang line is kept out of the code."""
    lines = []
    for line in text.replace("\\\n", " ").splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            continue
        lines.append(re.sub(r"\s+#.*$", "", line))
    return "\n".join(lines)


def shell_findings(text: str) -> list[str]:
    return [m.group(0).strip()[:120] for m in LOOP.finditer(shell_code(text))
            if NAME_QUERY.search(m.group("cond"))]


def _is_name_query(call: ast.Call) -> bool:
    for arg in call.args:
        if isinstance(arg, (ast.List, ast.Tuple)):
            words = [e.value for e in arg.elts
                     if isinstance(e, ast.Constant) and isinstance(e.value, str)]
            if words and words[0] in ("pgrep", "pkill") and any(
                    w.startswith("-") and "f" in w for w in words[1:]):
                return True
    return False


def _has_deadline(test: ast.expr) -> bool:
    for node in ast.walk(test):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and \
                node.func.attr in ("monotonic", "time"):
            return True
    return False


def python_findings(text: str) -> list[str]:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    found = []
    for loop in (n for n in ast.walk(tree) if isinstance(n, ast.While)):
        if _has_deadline(loop.test):
            continue
        if any(isinstance(n, ast.Call) and _is_name_query(n) for n in ast.walk(loop)):
            found.append(f"line {loop.lineno}: unbounded while-loop on a process-name query")
    return found


def is_shell(path: Path, text: str) -> bool:
    return path.suffix in (".sh", ".bash") or bool(re.match(r"#!.*\b(ba)?sh\b", text))


def scan(root: Path, paths: list[str]) -> list[str]:
    findings = []
    for relative in paths:
        path = root / relative
        if path.resolve() == SELF or relative.startswith(EXCLUDED_TREES) or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if path.suffix == ".py":
            findings += [f"{relative}: {f}" for f in python_findings(text)]
        elif is_shell(path, text):
            findings += [f"{relative}: {f}" for f in shell_findings(text)]
    return findings


class NoSelfMatchingWaits(unittest.TestCase):
    def test_the_repository_has_no_process_name_wait_loop(self) -> None:
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True,
                                 check=True).stdout.splitlines()
        findings = scan(ROOT, tracked)
        self.assertEqual([], findings,
                         "wait by identity with framework/scripts/process_wait.py instead:\n"
                         + "\n".join(findings))

    def test_the_detector_fires_on_the_defect_itself(self) -> None:
        planted = {
            "waiter.sh": 'until ! pgrep -f "run_release_regressions" >/dev/null; do sleep 3; done\n',
            "waiter2.sh": "while pgrep -fl job_x; do\n  sleep 5\ndone\n",
            "noext": "#!/usr/bin/env bash\nwhile pkill -0 -f worker\ndo sleep 1; done\n",
            "waiter.py": ("import subprocess, time\n"
                          "while subprocess.run(['pgrep', '-f', 'job']).returncode == 0:\n"
                          "    time.sleep(1)\n"),
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, text in planted.items():
                (root / name).write_text(text, encoding="utf-8")
            findings = scan(root, list(planted))
        self.assertEqual(sorted({f.split(":")[0] for f in findings}), sorted(planted))

    def test_what_is_not_a_process_name_wait_loop_is_left_alone(self) -> None:
        benign = {
            "notes.md": 'until ! pgrep -f "job"; do sleep 3; done\n',
            "commented.sh": '# until ! pgrep -f "job"; do sleep 3; done\necho ok\n',
            "file_wait.sh": "timeout 600 bash -c 'until [ -f out/DONE ]; do sleep 5; done'\n",
            "bounded.py": ("import subprocess, time\ndeadline = time.monotonic() + 60\n"
                           "while time.monotonic() < deadline:\n"
                           "    subprocess.run(['pgrep', '-f', 'job'])\n"),
            "oneshot.py": "import subprocess\nsubprocess.run(['pgrep', '-f', 'job'])\n",
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, text in benign.items():
                (root / name).write_text(text, encoding="utf-8")
            self.assertEqual([], scan(root, list(benign)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
