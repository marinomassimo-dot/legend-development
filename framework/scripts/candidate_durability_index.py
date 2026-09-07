#!/usr/bin/env python3
"""Measure what each commit candidate declares, so an integrator can route without opening all.

Reports six properties per candidate:

  TRACKED     the file is in git (an untracked candidate is inspected by no gate)
  COMMITTED   tracked AND no unstaged diff against HEAD
  BASE        declares a base/gate line (`Target WM`, `Batch gate`, `BASE_HEAD`)
  CLASS       declares an explicit `**Change class:**`
  TARGETS     names at least one canonical target (`CLAIM nnn` / `PAPER nnn`)
  AUDIT       declares a locator-audit trigger

🔴 THIS IS A DECLARATION SCAN, NOT AN ADJUDICATION. It reports what a document *says*,
never whether the document is right. In particular the MAJOR column is a keyword hit:
instruments and superseded copies mention MAJOR without proposing one, so a count from
this column is an upper bound and must not be routed on. Read CC-20260826-REVIEW-INDEX.md
for the adjudicated routing.

🔴 COMMITTED is measured against HEAD. A file staged in the same commit as the report reads
as uncommitted at measurement time and committed immediately after -- say which, or the
number looks like a defect when it is a timestamp.

Scale: linear in candidates, one `git diff` subprocess each. At a few hundred candidates the
subprocess-per-file dominates; batch with a single `git status --porcelain` before that hurts.

Usage:
    python3 framework/scripts/candidate_durability_index.py [--dir PATH]
"""
import argparse
import glob
import os
import re
import subprocess
import sys

DEFAULT_DIR = "disease-models/wwox/research/commit_candidates"

FIELDS = [
    ("tracked", "TRACKED", None),
    ("committed", "COMMITTED", None),
    ("base", "BASE_DECLARED", r"Target WM|BASE_HEAD|rebase required|Batch gate"),
    ("class", "CHANGE_CLASS_DECLARED", r"\*\*Change class:\*\*|CHANGE_CLASS"),
    ("targets", "CANONICAL_TARGETS_DECLARED", r"Canonical targets:|CLAIM \d{3}|PAPER \d{3}"),
    ("audit", "LOCATOR_AUDIT_TRIGGER_DECLARED",
     r"[Ll]ocator audit|locator-audit|LOCATOR_AUDIT|LOCATOR-PACKET"),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=DEFAULT_DIR)
    args = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(args.dir, "*.md")))
    if not paths:
        print("ERROR: no candidates under %s -- refusing to report '0 gaps' from an empty "
              "population." % args.dir, file=sys.stderr)
        return 2

    tracked = set(subprocess.run(["git", "ls-files", args.dir],
                                 capture_output=True, text=True).stdout.split())

    rows = []
    for p in paths:
        t = open(p, encoding="utf-8").read()
        is_tracked = p in tracked
        clean = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", p]).returncode == 0
        r = {"name": os.path.basename(p), "tracked": is_tracked,
             "committed": is_tracked and clean, "lines": len(t.splitlines()),
             "major": bool(re.search(r"MAJOR", t))}
        for key, _, pat in FIELDS:
            if pat:
                r[key] = bool(re.search(pat, t))
        rows.append(r)

    hdr = "%-52s %-4s %-4s %-5s %-6s %-8s %-6s %-6s %5s"
    print(hdr % ("CANDIDATE", "TRK", "CMT", "BASE", "CLASS", "TARGETS", "AUDIT", "MAJOR?", "LINES"))
    print("-" * 108)
    mark = lambda b: " Y " if b else " . "
    for r in rows:
        print(hdr % (r["name"][:52], mark(r["tracked"]), mark(r["committed"]), mark(r["base"]),
                     mark(r["class"]), mark(r["targets"]), mark(r["audit"]),
                     mark(r["major"]), r["lines"]))
    print("-" * 108)

    n = len(rows)
    for key, label, _ in FIELDS:
        c = sum(1 for r in rows if r[key])
        print("%-34s %2d/%d%s" % (label, c, n, "" if c == n else "   <-- GAP"))
    print("\nMAJOR keyword hits: %d of %d  (UPPER BOUND -- instruments and superseded copies "
          "mention MAJOR without proposing one)" % (sum(1 for r in rows if r["major"]), n))
    print("Population: %d candidate file(s) under %s at run time." % (n, args.dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
