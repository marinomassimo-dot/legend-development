#!/usr/bin/env python3
"""Keep conclusions out of future wrapper-generated commit subjects.

`neutral` reads the author's complete message from stdin and puts it in the body.
The subject contains only fixed surface categories derived from path prefixes; neither
filenames, branch names, task names nor user prose are interpolated into the subject.
`scripts/legend_commit.sh` uses this route; `task_close.py` uses a fixed merge subject.

`check` and `scan` retain the earlier lexical screen for optional hooks and historical
inspection. That screen can miss conclusions and does not guarantee blind context.
Bare git commits, other merge routes, old history and other runtime-injected context
are outside this control. No runtime session-blindness guarantee is claimed.

Usage:
    commit_subject.py neutral -- <paths...>  # complete message on stdin
    commit_subject.py check --subject "<subject>"
    commit_subject.py check --message-file .git/COMMIT_EDITMSG
    commit_subject.py scan [--rev-range A..B] [--limit N]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

EXEMPT = re.compile(r"^(?:Merge (?:branch|remote-tracking branch|pull request)|Revert \"|fixup! |squash! )")

LOWER_SURFACE = r"[a-z0-9][a-z0-9_.\-/]*"
ID_SURFACE = r"[A-Z][A-Z0-9]*(?:[_-][A-Z0-9]+)+"
FIRST_TOKEN = re.compile(rf"^(?:{LOWER_SURFACE}|{ID_SURFACE})(?=$|[\s:,;+])")

# Verdict vocabulary. Word-bounded and not adjoining `-`, so `BLOCK-1` (a name) and
# `strict-PASS` inside an identifier are not verdicts, while `pass`, `refuted`, `sbagliato` are.
VERDICT_WORDS = (
    # English
    "pass", "passes", "passed", "fail", "fails", "failed", "blocked", "supported",
    "unsupported", "refuted", "refutes", "confirmed", "confirms", "contradicts", "contradicted",
    "overturn", "overturns", "overturned", "reverse", "reverses", "reversed", "withdrawn",
    "holds", "disproved", "proven", "proves", "wrong", "false", "true", "real", "invalid",
    "incorrect", "overshoot", "defective", "verified",
    # Italian
    "sbagliato", "sbagliata", "sbagliati", "falso", "falsa", "falsi", "vero", "vera", "veri",
    "reale", "regge", "confermato", "confermata", "smentito", "smentita", "errato", "errata",
    "difettosa", "difettoso", "corretto", "corretta",
)
COPULAS = (
    "is", "are", "was", "were", "isn't", "aren't", "wasn't", "weren't", "been",
    "è", "e'", "era", "erano", "sono", "fu",
)
_WORDS = "|".join(re.escape(word) for word in sorted(VERDICT_WORDS + COPULAS, key=len, reverse=True))
CONCLUSION = re.compile(rf"(?<![\w\-])({_WORDS})(?![\w\-])", re.IGNORECASE)


@dataclass(frozen=True)
class Violation:
    rule: str
    detail: str

    def __str__(self) -> str:
        return f"{self.rule}: {self.detail}"


def subject_of(message: str) -> str:
    """The first non-empty, non-comment line — what `git log --format=%s` will print."""
    for line in message.splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            return line.strip()
    return ""


def check_subject(subject: str) -> list[Violation]:
    subject = subject.strip()
    if not subject or EXEMPT.match(subject):
        return []
    found: list[Violation] = []
    if not FIRST_TOKEN.match(subject):
        first = re.split(r"[\s:,;]", subject, maxsplit=1)[0]
        found.append(Violation(
            "NO_SURFACE_FIRST",
            f"opens with {first!r}, which is not a module, file, directory or identifier; "
            "open with the surface touched (e.g. `ledger: …`, `BATCH_…: …`)"))
    words = sorted({match.group(1).lower() for match in CONCLUSION.finditer(subject)})
    if words:
        found.append(Violation(
            "CONCLUSION_IN_SUBJECT",
            f"carries {', '.join(repr(w) for w in words)}; the subject is printed into every "
            "fresh session's context, so state what was touched here and put the finding in "
            "the body"))
    return found


def check_message(message: str) -> list[Violation]:
    return check_subject(subject_of(message))


def _git_subjects(rev_range: str | None, limit: int) -> list[tuple[str, str]]:
    args = ["git", "log", "--format=%h%x09%s", f"-{limit}"]
    if rev_range:
        args.append(rev_range)
    done = subprocess.run(args, capture_output=True, text=True, check=True)
    return [tuple(line.split("\t", 1)) for line in done.stdout.splitlines() if "\t" in line]


# Closed surface vocabulary: filenames and task names can themselves contain conclusions.
SURFACES = {"framework": "harness", "scripts": "harness", "governance": "harness",
            "roles": "harness", "deployment": "harness", ".claude": "harness",
            "ledger": "ledger", "learning": "learning", "disease-models": "research"}

def neutral_message(message: str, paths: list[str]) -> str:
    """Preserve the entire author message in the body; emit no free-text subject."""
    surfaces = sorted({SURFACES.get(Path(p).parts[0] if Path(p).parts else "", "repository")
                       for p in paths})
    return "repository: update " + ", ".join(surfaces or ["repository"]) + "\n\n" + message


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    source = check.add_mutually_exclusive_group(required=True)
    source.add_argument("--subject")
    source.add_argument("--message-file")
    neutral = sub.add_parser("neutral")
    neutral.add_argument("paths", nargs="+")
    scan = sub.add_parser("scan")
    scan.add_argument("--rev-range")
    scan.add_argument("--limit", type=int, default=200)
    args = parser.parse_args(argv)

    if args.command == "neutral":
        print(neutral_message(sys.stdin.read(), args.paths), end="")
        return 0

    if args.command == "check":
        if args.subject is not None:
            violations = check_subject(args.subject)
        else:
            violations = check_message(Path(args.message_file).read_text(encoding="utf-8"))
        for violation in violations:
            print(violation)
        return 1 if violations else 0

    rows = _git_subjects(args.rev_range, args.limit)
    flagged = 0
    for sha, subject in rows:
        violations = check_subject(subject)
        if violations:
            flagged += 1
            print(f"{sha} {'|'.join(v.rule for v in violations)} {subject}")
    print(f"subjects: {len(rows)} | flagged: {flagged}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
