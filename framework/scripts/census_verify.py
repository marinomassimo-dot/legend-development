#!/usr/bin/env python3
"""Re-measure a claimed term census against a git ref, and name the contamination.

WHY THIS EXISTS
---------------
On 2026-09-22 a delegate returned a census asserting eleven reagent terms were absent
from the repository. Verifying it, the orchestrator grepped the working tree — which by
then held the delegate's own 474-line census, naming every one of those eleven terms.
The re-count came back non-zero and the census looked wrong. It was not wrong. The
*verification surface* was contaminated by the artefact under verification.

The second attempt used ``grep --exclude``, which this deployment's grep silently ignores,
and produced the same false mismatch. Only counting against the committed tree resolved it:
every claimed count was exact.

Two distinct failure modes, one root cause — **the surface you verify on is not the surface
the claim was made about.** This tool removes the judgement call by measuring at a git ref,
and, when the working tree disagrees, naming the files responsible instead of leaving the
reader to guess.

A SECOND ambiguity, found by running this tool on that same incident: "count" is not one
quantity. ``grep -c`` counts matching LINES; ``grep -o | wc -l`` counts OCCURRENCES. For the
same census the two differ (cycloheximide: 78 lines, 91 occurrences; UPF1: 22 lines, 27
occurrences) — and a census almost never says which it used. Two people can therefore agree
on "78" while measuring different things, which is what happened here. This tool refuses the
guess: ``--metric`` is explicit and the metric is printed on every line of output.

It answers: "is the tree I am about to grep a trustworthy surface for checking this claim,
and are we even counting the same quantity?"

NOT a gate and NOT an auditor (LEGEND_CORE § 26). It measures and reports; it authorises
nothing and blocks nothing. A non-zero exit means a claim did not reproduce at the ref —
which is a finding for a human to read, not an enforcement action.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import defaultdict


def _git(args: list[str], cwd: str | None = None) -> tuple[int, str]:
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return p.returncode, p.stdout


def count_at_ref(term: str, ref: str, paths: list[str], *, word: bool, icase: bool,
                 metric: str = "occurrences", cwd: str | None = None) -> tuple[int, set[str]]:
    """Count `term` at `ref`. Returns (count, files).

    metric="occurrences": git grep -o prints one line per MATCH, so lines == occurrences.
    metric="lines":       count distinct matching lines, which is what ``grep -c`` reports
                          and what most hand-written censuses actually contain.
    """
    args = ["grep", "-o"] if metric == "occurrences" else ["grep", "-n"]
    if word:
        args.append("-w")
    if icase:
        args.append("-i")
    args += ["-e", term, ref, "--", *paths]
    rc, out = _git(args, cwd)
    if rc not in (0, 1):                      # 1 == no matches, which is a real answer
        raise RuntimeError(f"git grep failed for {term!r} at {ref!r}")
    files: set[str] = set()
    n = 0
    for line in out.splitlines():
        if not line:
            continue
        n += 1
        # "<ref>:<path>:<rest>" — split off ref, then path
        rest = line.split(":", 1)[1] if ":" in line else line
        files.add(rest.split(":", 1)[0] if ":" in rest else rest)
    return n, files


def count_in_worktree(term: str, paths: list[str], *, word: bool, icase: bool,
                      metric: str = "occurrences", cwd: str | None = None) -> tuple[int, set[str]]:
    """The same measurement on the working tree, including untracked files."""
    args = ["grep", "-o", "--untracked"] if metric == "occurrences" else ["grep", "-n", "--untracked"]
    if word:
        args.append("-w")
    if icase:
        args.append("-i")
    args += ["-e", term, "--", *paths]
    rc, out = _git(args, cwd)
    if rc not in (0, 1):
        raise RuntimeError(f"git grep failed for {term!r} in the working tree")
    files: set[str] = set()
    n = 0
    for line in out.splitlines():
        if not line:
            continue
        n += 1
        files.add(line.split(":", 1)[0] if ":" in line else line)
    return n, files


def parse_claim(raw: str) -> tuple[str, int]:
    """'cycloheximide=78' -> ('cycloheximide', 78). Splits on the LAST '=' so a term
    may itself contain one."""
    if "=" not in raw:
        raise argparse.ArgumentTypeError(f"claim {raw!r} must be TERM=COUNT")
    term, _, n = raw.rpartition("=")
    if not term:
        raise argparse.ArgumentTypeError(f"claim {raw!r} has an empty term")
    try:
        return term, int(n)
    except ValueError:
        raise argparse.ArgumentTypeError(f"claim {raw!r} has a non-integer count {n!r}")


def verify(claims: list[tuple[str, int]], ref: str, paths: list[str], *, word: bool,
           icase: bool, metric: str = "occurrences", cwd: str | None = None) -> dict:
    rows = []
    contaminants: dict[str, set[str]] = defaultdict(set)
    for term, claimed in claims:
        at_ref, ref_files = count_at_ref(term, ref, paths, word=word, icase=icase,
                                         metric=metric, cwd=cwd)
        in_wt, wt_files = count_in_worktree(term, paths, word=word, icase=icase,
                                            metric=metric, cwd=cwd)
        extra = wt_files - ref_files
        for f in extra:
            contaminants[f].add(term)
        rows.append({
            "term": term,
            "claimed": claimed,
            "at_ref": at_ref,
            "in_worktree": in_wt,
            "reproduces": at_ref == claimed,
            "worktree_would_mislead": in_wt != at_ref,
            "contaminating_files": sorted(extra),
        })
    return {"ref": ref, "metric": metric, "rows": rows,
            "contaminants": {k: sorted(v) for k, v in contaminants.items()}}


def render(result: dict) -> str:
    out = [f"census surface: {result['ref']}   metric: {result['metric']}", ""]
    out.append(f"{'term':<28} {'claimed':>8} {'at ref':>8} {'worktree':>9}  verdict")
    for r in result["rows"]:
        v = "REPRODUCES" if r["reproduces"] else "DOES NOT REPRODUCE"
        if r["worktree_would_mislead"]:
            v += "  [worktree disagrees]"
        out.append(f"{r['term']:<28} {r['claimed']:>8} {r['at_ref']:>8} {r['in_worktree']:>9}  {v}")
    bad = [r for r in result["rows"] if not r["reproduces"]]
    misled = [r for r in result["rows"] if r["worktree_would_mislead"]]
    out.append("")
    if result["contaminants"]:
        out.append("CONTAMINATION — present in the working tree but not at the ref:")
        for f, terms in sorted(result["contaminants"].items()):
            out.append(f"  {f}  ({len(terms)} term(s): {', '.join(terms[:6])}"
                       f"{'…' if len(terms) > 6 else ''})")
        out.append("")
        out.append("  A census cannot be verified on a tree that already holds the census.")
        out.append("")
    out.append(f"VERDICT: {'PASS' if not bad else 'FAIL'} — "
               f"{len(result['rows']) - len(bad)}/{len(result['rows'])} claims reproduce at {result['ref']}"
               + (f"; {len(misled)} would have been misread against the working tree" if misled else ""))
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--claim", type=parse_claim, action="append", required=True, metavar="TERM=COUNT",
                    help="a claimed occurrence count; repeatable")
    ap.add_argument("--ref", default="HEAD", help="git ref to measure against (default HEAD)")
    ap.add_argument("--path", action="append", default=None,
                    help="pathspec to restrict the count to; repeatable (default: whole repo)")
    ap.add_argument("-w", "--word", action="store_true", help="word-boundary match")
    ap.add_argument("-i", "--icase", action="store_true", help="case-insensitive match")
    ap.add_argument("--metric", choices=("occurrences", "lines"), default="occurrences",
                    help="occurrences (grep -o) or matching lines (grep -c). A census that does "
                         "not say which it used should be checked under BOTH — they differ.")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a table")
    a = ap.parse_args(argv)

    result = verify(a.claim, a.ref, a.path or ["."], word=a.word, icase=a.icase, metric=a.metric)
    if a.json:
        import json
        print(json.dumps(result, indent=2))
    else:
        print(render(result))
    return 0 if all(r["reproduces"] for r in result["rows"]) else 1


if __name__ == "__main__":
    sys.exit(main())
