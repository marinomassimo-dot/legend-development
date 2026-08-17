#!/usr/bin/env python3
"""Determinism tests for candidate_content_hash.py.

The property under test: **the hash is a function of `(base, tip)` and of nothing else.** In
particular it must not depend on which branch happens to be checked out, because the domain rule
— the version prefix and the control-plane roots — lives in a governed file that different
branches may carry different versions of.

Every test builds its own throw-away git repository. Nothing here reads this repository's
history, so the suite passes in a clean clone and cannot be quietly satisfied by whatever commits
happen to exist locally. That matters more than usual here: the defect these tests exist to catch
was invisible for as long as every candidate was hashed from its own branch, and only appeared
once two branches carried different rules. A test that cannot mount that condition would have
reported green throughout.

    python3 governance/scripts/test_candidate_content_hash.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "candidate_content_hash.py"

PARAMS_TEMPLATE = """# Plan-defined parameters (fixture)

## P5 · CANDIDATE_CONTENT_HASH

```
CANDIDATE_HASH_VERSION: {version}
```

### P5.1 · The candidate content domain

```
CONTROL_PLANE_ROOTS:
{roots}
```

### P5.2 · The hash
"""


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    )
    return result.stdout


def _write(repo: Path, rel: str, text: str) -> None:
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _params(version: str, roots: list[str]) -> str:
    return PARAMS_TEMPLATE.format(
        version=version, roots="\n".join(f"- {r}" for r in roots)
    )


def _make_repo(tmp: Path) -> Path:
    """A repo with two commits whose domain RULES differ, which is the condition under test."""
    repo = tmp / "fixture"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "test@example.invalid")
    _git(repo, "config", "user.name", "test")

    # The script locates the repo from its own path, so it must live inside the fixture.
    dest = repo / "governance" / "scripts" / SCRIPT.name
    dest.parent.mkdir(parents=True)
    shutil.copy2(SCRIPT, dest)

    _write(repo, "content/a.md", "alpha\n")
    _write(repo, "governance/candidates/manifest.md", "control plane\n")
    _write(repo, "governance/plan_defined_parameters.md",
           _params("fixture-v1", ["governance/candidates/"]))
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "base: rule v1")
    base = _git(repo, "rev-parse", "HEAD").strip()

    # Second commit: same tree content, DIFFERENT rule. This is the whole point of the fixture.
    _write(repo, "governance/plan_defined_parameters.md",
           _params("fixture-v2", ["governance/candidates/", "ledger/"]))
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "tip: rule v2")
    tip = _git(repo, "rev-parse", "HEAD").strip()

    return repo, base, tip


def _run(repo: Path, base: str, tip: str, show: bool = False):
    args = [sys.executable, str(repo / "governance/scripts" / SCRIPT.name),
            "--base", base, "--tip", tip]
    if show:
        args.append("--show-domain")
    return subprocess.run(args, capture_output=True, text=True)


def test_rule_comes_from_the_tip_not_the_working_tree(repo, base, tip):
    """Hashing an OLD tip while the working tree carries a NEWER rule must use the old rule."""
    out = _run(repo, base, base, show=True).stdout
    assert "fixture-v1" in out, f"expected the base's own rule, got:\n{out}"
    assert "fixture-v2" not in out, "the working tree's rule leaked into an older tip's hash"

    out_tip = _run(repo, base, tip, show=True).stdout
    assert "fixture-v2" in out_tip, f"expected the tip's own rule, got:\n{out_tip}"
    return "rule read from the tip, not the checkout"


def test_hash_is_branch_independent(repo, base, tip):
    """The same (base, tip) must hash identically no matter what the checkout holds.

    Simulated by checking out the base — so the working tree carries rule v1 — and hashing the
    tip, whose own rule is v2. Under the defect this returned a v1-flavoured hash.
    """
    before = _run(repo, base, tip).stdout.strip()
    _git(repo, "checkout", "-q", base)
    after = _run(repo, base, tip).stdout.strip()
    _git(repo, "checkout", "-q", "-")
    assert before and before == after, (
        f"hash changed with the checkout: {before!r} vs {after!r}"
    )
    return f"branch-independent: {before[:16]}…"


def test_dirty_working_tree_does_not_move_the_hash(repo, base, tip):
    """A modified working-tree rule must not affect a committed tip's hash."""
    clean = _run(repo, base, tip).stdout.strip()
    params = repo / "governance" / "plan_defined_parameters.md"
    original = params.read_text(encoding="utf-8")
    params.write_text(_params("fixture-vSABOTAGE", ["governance/candidates/", "ledger/", "x/"]),
                      encoding="utf-8")
    dirty = _run(repo, base, tip).stdout.strip()
    params.write_text(original, encoding="utf-8")
    assert clean == dirty, f"a dirty working tree moved the hash: {clean!r} vs {dirty!r}"
    return "immune to a dirty working tree"


def test_missing_rule_at_tip_fails_explicitly(repo, base, tip):
    """A tip that carries no rule must fail loudly, never fall back to the checkout."""
    empty = repo / "empty"
    empty.mkdir()
    _git(empty, "init", "-q")
    _git(empty, "config", "user.email", "test@example.invalid")
    _git(empty, "config", "user.name", "test")
    dest = empty / "governance" / "scripts" / SCRIPT.name
    dest.parent.mkdir(parents=True)
    shutil.copy2(SCRIPT, dest)
    _write(empty, "content/a.md", "alpha\n")
    _git(empty, "add", "-A")
    _git(empty, "commit", "-q", "-m", "no governance rule here")
    oid = _git(empty, "rev-parse", "HEAD").strip()

    result = _run(empty, oid, oid)
    assert result.returncode != 0, "a tip without the rule must not succeed"
    assert "absent at" in result.stderr, f"expected an explicit absence error, got: {result.stderr}"
    return "absent rule fails explicitly, no fallback"


def test_determinism_across_runs(repo, base, tip):
    first = _run(repo, base, tip).stdout.strip()
    second = _run(repo, base, tip).stdout.strip()
    assert first == second and first, "two runs disagreed"
    return "stable across runs"


def main() -> int:
    tests = [
        test_rule_comes_from_the_tip_not_the_working_tree,
        test_hash_is_branch_independent,
        test_dirty_working_tree_does_not_move_the_hash,
        test_missing_rule_at_tip_fails_explicitly,
        test_determinism_across_runs,
    ]
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        repo, base, tip = _make_repo(Path(tmp))
        for test in tests:
            try:
                detail = test(repo, base, tip)
                print(f"  PASS  {test.__name__} — {detail}")
            except AssertionError as exc:
                failures += 1
                print(f"  FAIL  {test.__name__}: {exc}")
    print(f"\n{len(tests) - failures}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
