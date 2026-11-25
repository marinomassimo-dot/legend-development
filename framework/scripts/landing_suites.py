#!/usr/bin/env python3
"""Print the cheap guard suites that the paths changed by a branch can turn red. Advisory and print-only: it runs nothing, writes nothing and gates nothing.

Why this exists. A gate run on main takes more than an hour, and a landing runs the publication gate and the committed-view checks, not these suites, so a defect in one's own diff was
learned about an hour after it landed, with other landings stacked on a red main (ADV-237, measured on gate runs of 2026-11-22 to 2026-11-24; the numbers are in the HE record beside the
checkpoint). A SELECTION, never the release battery: running what it prints means "the suites these paths usually break did not break", nothing more.

    python3 framework/scripts/landing_suites.py                  # the diff since the merge base with development/main: the suites, then one command that runs them
    python3 framework/scripts/landing_suites.py --base <rev>     # another base

The change judged is `merge-base(base, HEAD)..HEAD`, the author's own work, not what others landed since; only committed changes are seen. The rules are RULES below, one line each, with the
red run that earned it. A suite already red on main stays red here too (`ci_runs.py status <sha>` says which). Not selected on purpose: the whole of `test_repurposing_view.py` (about 20 minutes; the
landing tool already checks the committed views; one 2-second class of it is selected for card, needs and ranking changes) and the other long suites.
Exit codes: 0 the selection was printed (possibly empty) · 2 invalid invocation or the base cannot be resolved.
"""
from __future__ import annotations

import argparse
import fnmatch
import subprocess
import sys
from pathlib import Path

def _any(paths: list[tuple[str, str]], *patterns: str, status: str = "") -> bool:
    return any((not status or st.startswith(status)) and any(fnmatch.fnmatch(p, pat) for pat in patterns) for st, p in paths)


# (suite path, predicate over [(git status letter, path)]); the comment names the red runs that earned the rule
RULES = [
    # the two quick suites of the README's pre-freeze habit that no 2026-11-22..24 episode needed: a link, a shebang without +x, a wrong relative path (2026-11-21)
    ("scripts/test_release_surface.py", lambda c: _any(c, "*", status="A")),
    ("scripts/test_fresh_clone_reader_journey.py", lambda c: _any(c, "*.md")),
    # #2237, #2277, #2285: a new document or script naming a command that does not exist
    ("scripts/test_documented_commands.py", lambda c: _any(c, "*.py", "*.md")),
    # #2067: a ragged TSV
    ("scripts/test_structured_data_integrity.py", lambda c: _any(c, "*.tsv", "*.csv", "*.json", "*.jsonl")),
    ("scripts/test_link_targets.py", lambda c: _any(c, "*.md")),
    ("scripts/test_section_references.py", lambda c: _any(c, "*.md")),
    ("scripts/test_tool_routing.py", lambda c: _any(c, "framework/scripts/*", "scripts/*")),
    # #2322, #2325 (ADV-252): a new test asserted an absence in a body naming a registry path. The paths are the guard's own SCOPES
    ("scripts/test_no_closed_world_assertions_on_live_state.py",
     lambda c: _any(c, "framework/scripts/test_*.py", "scripts/test_*.py", "disease-models/wwox/analysis/scripts/test_*.py")),
    # #2289-#2297: debt_report.py imported the Advisor
    ("framework/scripts/test_strategic_advisor.py", lambda c: _any(c, "framework/scripts/*.py")),
    # #1981, #2289-#2297: a registry changed and the batch queue or the pathograph was not satisfied or not regenerated
    ("framework/scripts/test_batch_queue.py", lambda c: _any(c, "disease-models/*/registries/*")),
    ("framework/scripts/test_pathograph.py", lambda c: _any(c, "disease-models/*/registries/*", "disease-models/*/analysis/*")),
    # #1994, #2109: a receipt recorded and the two derived pages not regenerated
    ("framework/scripts/test_coverage_report.py", lambda c: _any(c, "*fulltext_read_receipts.jsonl", "*coverage_report*")),
    ("framework/scripts/test_reading_state.py", lambda c: _any(c, "*fulltext_read_receipts.jsonl", "*reading_state*")),
    # #2404: a card changed and the suite that keeps its reviewed copy went red (0.1 s)
    ("disease-models/wwox/research/drug_repurposing/cards_early_it13_p22_20261031/test_cards_early_it13_p22.py",
     lambda c: _any(c, "disease-models/*/drug_repurposing/cards_early/*", "framework/scripts/repurposing_bridge.py")),
    # #2404: a card named a PMID the title cache does not hold. Only this class of the long view suite (about 2 s)
    ("framework/scripts/test_repurposing_view.py Titles",
     lambda c: _any(c, "disease-models/*/drug_repurposing/cards*", "disease-models/*/drug_repurposing/needs/*", "disease-models/*/drug_repurposing/ranking_it8*",
                    "disease-models/*/drug_repurposing/view/source_titles.json")),
    # #2353: needs.json changed and the ranking was not regenerated (about 30 s and 95 s)
    ("framework/scripts/test_candidate_tree_freshness.py", lambda c: _any(c, "disease-models/*/drug_repurposing/needs/*")),
    ("disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/test_ranking_it8.py",
     lambda c: _any(c, "disease-models/*/drug_repurposing/needs/*")),
]


def git(root: Path, *args: str) -> str:
    done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if done.returncode:
        raise ValueError((done.stderr or done.stdout).strip().splitlines()[0] if (done.stderr or done.stdout).strip() else f"git {args[0]} failed")
    return done.stdout


def changes(root: Path, base: str) -> list[tuple[str, str]]:
    fork = git(root, "merge-base", base, "HEAD").strip()
    out = []
    for line in git(root, "diff", "--name-status", "--no-renames", fork, "HEAD").splitlines():
        parts = line.split("\t")
        out.append((parts[0], parts[-1]))
    return out


def select(changed: list[tuple[str, str]], root: Path) -> list[str]:
    """Suites for the changed paths: a path, or a path and one class of it. A rule whose suite is not in this checkout is skipped; a `test_*.py` the change adds or edits under disease-models/ is named itself (#2023)."""
    picked = [suite for suite, wanted in RULES if (root / suite.split()[0]).is_file() and wanted(changed)]
    picked += [path for st, path in changed
               if st != "D" and path.startswith("disease-models/") and Path(path).name.startswith("test_") and path.endswith(".py") and (root / path).is_file()]
    return list(dict.fromkeys(picked))


def command_for(picked: list[str]) -> str:
    return " && ".join(f"python3 -B {path} < /dev/null" for path in picked)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", default="development/main", help="the branch the change will land on (default: development/main)")
    parser.add_argument("--repo", default=None, help="repository root (default: the checkout holding this file)")
    args = parser.parse_args(argv)
    root = Path(args.repo).resolve() if args.repo else Path(__file__).resolve().parents[2]
    try:
        changed = changes(root, args.base)
    except ValueError as error:
        print(f"REFUSED: cannot read the change against {args.base}: {error}")
        return 2
    picked = select(changed, root)
    print(f"LANDING SUITES (advisory) — {len(changed)} committed path(s) since the merge base with {args.base}; {len(picked)} suite(s) selected, none run")
    for path in picked:
        print(f"  {path}")
    if picked:
        print("run them: " + command_for(picked))
    return 0


if __name__ == "__main__":
    sys.exit(main())
