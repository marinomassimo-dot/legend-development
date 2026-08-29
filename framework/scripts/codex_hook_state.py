#!/usr/bin/env python3
"""Does the Codex hook registration this repository ships actually LOAD?

Revisions 2–7 could not answer this. `codex doctor --json` reports eighteen checks and
not one is about hooks — the word occurs once in its whole output — so the protocol
recorded `TRUST_PENDING`: configured, and gated behind a per-hook review nobody here
could read. It was careful to say the trust gate was an inference from a flag's
existence and must not be reported as the cause of a peer's probe not firing.

There is a way to read it, it costs nothing, and it needs no session: the installed
app-server answers a `hooks/list` JSON-RPC method, returning one `HookMetadata` per
loaded hook with `source`, `sourcePath` and `trustStatus`. This script asks.

## What it found on 2026-08-29, codex-cli 0.147.0

```
cwd = any LEGEND worktree     hooks: []   warnings: []   errors: []
```

Zero, with no error. And the positive controls fire, so it is a real zero:

```
.codex/config.toml at a TRUSTED PROJECT ROOT, this repository's own file, verbatim
                                                          → 5 hooks, source "project"
the same file in a trusted NESTED git repository          → 5 hooks
the same file in a git WORKTREE                           → 0 hooks
the same file at the worktree's SHARED CHECKOUT           → 5 hooks
```

🔴 **In a git worktree, codex-cli 0.147.0 resolves the project config layer through git
to the SHARED CHECKOUT, and collects project hooks from `<shared checkout>/.codex`. A
`.codex/config.toml` in the worktree itself contributes nothing, silently.**

Every LEGEND actor works in a worktree — that is the operating convention, adopted
because ten sessions on one `HEAD` had one of them commit another's unfinished work. So
the Codex registration policed **nothing, in every worktree, for every actor**, and no
surface in the repository could say so.

This is a MEASURED cause for the `HOOK_NOT_FIRING` a peer observed, and it replaces the
trust-gate inference rather than confirming it. Directory trust is satisfied: the ancestor
IS trusted, the layer IS discovered, and no error is raised.

🔴 It also corrects this repository's own reasoning about paths. `.codex/config.toml`
says its command path is relative because "Codex resolves the repository root per working
directory — `codex doctor` reported `repo root` as the worktree". That is `doctor`'s
notion of a repo root. The CONFIG LAYER uses a different one, and the file reasoned from
the wrong one.

## What this does NOT establish

`hooks/list` reports what is LOADED. A loaded hook still carries `trustStatus`, and every
hook this script has seen load reports `"untrusted"` — the per-hook review gate is real
and is a second, independent condition. Loaded is not trusted, and trusted is not fired:
only a session probe that records a REFUSAL can reach `DEMONSTRATED`, and that remains a
spend under Annex J.4.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

#: What `hooks/list` says about this repository's registration.
NOT_LOADED = "NOT_LOADED"        # the runtime sees no hook here at all
LOADED_UNTRUSTED = "LOADED_UNTRUSTED"   # present, awaiting the per-hook review
LOADED_TRUSTED = "LOADED_TRUSTED"       # present and reviewed; still not proof it FIRES
UNDERIVABLE = "UNDERIVABLE"      # the app-server could not be asked


def hooks_list(cwd: str, env: Optional[dict] = None,
               timeout: float = 25.0) -> Tuple[Optional[dict], str]:
    """Ask the installed app-server to enumerate the hooks it would load for `cwd`.

    No prompt, no turn, no model call — this is a local JSON-RPC service, so it is not
    a spend under Annex J.4. If the binary is absent or does not answer, that is
    UNDERIVABLE and never an empty result.
    """
    try:
        proc = subprocess.Popen(
            ["codex", "app-server"], cwd=cwd,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, bufsize=1, env=env or {**os.environ})
    except (OSError, subprocess.SubprocessError) as exc:
        return None, f"could not start `codex app-server`: {exc}"

    try:
        for ident, method, params in (
            (1, "initialize", {"clientInfo": {"name": "legend-hook-state",
                                              "title": "LEGEND", "version": "1"}}),
            (2, "hooks/list", {}),
        ):
            proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": ident,
                                         "method": method, "params": params}) + "\n")
            proc.stdin.flush()
        deadline = time.time() + timeout
        answer = None
        while time.time() < deadline:
            line = proc.stdout.readline()
            if not line:
                break
            try:
                message = json.loads(line)
            except ValueError:
                continue
            if message.get("id") == 2:
                answer = message
                break
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    stderr = proc.stderr.read() if proc.stderr else ""
    if answer is None:
        return None, "the app-server did not answer `hooks/list`" + (
            f"\n{stderr[:400]}" if stderr else "")
    return answer, stderr


def hooks_for(cwd: str, env: Optional[dict] = None) -> Tuple[List[dict], str]:
    answer, stderr = hooks_list(cwd, env)
    if answer is None:
        return [], stderr
    data = answer.get("result", {}).get("data", [])
    entry = data[0] if data else {}
    return entry.get("hooks", []), stderr


def state_for(cwd: str) -> Tuple[str, List[dict], str]:
    """`(state, hooks, detail)` for one working directory."""
    hooks, stderr = hooks_for(cwd)
    if not hooks:
        if "did not answer" in stderr or "could not start" in stderr:
            return UNDERIVABLE, [], stderr
        return NOT_LOADED, [], stderr
    if all(hook.get("trustStatus") == "trusted" for hook in hooks):
        return LOADED_TRUSTED, hooks, stderr
    return LOADED_UNTRUSTED, hooks, stderr


def repo_root_of(cwd: str) -> Optional[str]:
    try:
        result = subprocess.run(["git", "-C", cwd, "rev-parse", "--show-toplevel"],
                                capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() or None


def common_checkout_of(cwd: str) -> Optional[str]:
    """The SHARED checkout behind a worktree — the directory codex resolves to."""
    try:
        result = subprocess.run(["git", "-C", cwd, "rev-parse", "--git-common-dir"],
                                capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    common = result.stdout.strip()
    if not common:
        return None
    return str(Path(cwd, common).resolve().parent) if not Path(common).is_absolute() \
        else str(Path(common).parent)


def report(cwd: str) -> Dict[str, object]:
    root = repo_root_of(cwd)
    shared = common_checkout_of(cwd)
    state, hooks, stderr = state_for(cwd)
    is_worktree = bool(root and shared and Path(root).resolve() != Path(shared).resolve())
    registration = Path(root or cwd) / ".codex" / "config.toml"
    shared_registration = Path(shared) / ".codex" / "config.toml" if shared else None
    return {
        "cwd": cwd,
        "worktree_root": root,
        "shared_checkout": shared,
        "is_git_worktree": is_worktree,
        "registration_in_worktree": registration.exists(),
        "registration_in_shared_checkout": bool(
            shared_registration and shared_registration.exists()),
        "state": state,
        "hooks": [{k: hook.get(k) for k in
                   ("eventName", "matcher", "source", "sourcePath", "trustStatus")}
                  for hook in hooks],
        # 🔴 The diagnosis, and it is only offered when its two premises HOLD. A cause
        # printed whenever the answer is zero would be a story, not a measurement.
        "diagnosis": (
            "this cwd is a git WORKTREE and the registration lives in the worktree "
            "rather than in the shared checkout that codex resolves the project layer "
            "to; run --explain for the controlled experiment"
            if state == NOT_LOADED and is_worktree and registration.exists()
            and not (shared_registration and shared_registration.exists())
            else ""),
        "stderr": stderr.strip()[:1000],
    }


def explain() -> int:
    """Re-run the controlled experiment, with its positive control, in scratch space.

    Nothing here touches the operator's `~/.codex`: `CODEX_HOME` is redirected to a
    temporary directory for the duration.
    """
    import shutil
    import tempfile

    source = Path(__file__).resolve().parent.parent.parent / ".codex" / "config.toml"
    if not source.exists():
        print(f"no registration to test at {source}")
        return 1

    home = Path(tempfile.mkdtemp(prefix="codex-home-")).resolve()
    root = Path(tempfile.mkdtemp(prefix="codex-root-")).resolve()
    env = {**os.environ, "CODEX_HOME": str(home)}
    try:
        subprocess.run(["git", "init", "-q", "-b", "main", str(root)], capture_output=True)
        for key, value in (("user.email", "t@example.invalid"), ("user.name", "t")):
            subprocess.run(["git", "-C", str(root), "config", key, value],
                           capture_output=True)
        (root / "a.txt").write_text("a\n")
        subprocess.run(["git", "-C", str(root), "add", "a.txt"], capture_output=True)
        subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "base"],
                       capture_output=True)
        worktree = root / ".claude" / "worktrees" / "wt"
        worktree.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "-C", str(root), "worktree", "add", "-q", "-b", "wtb",
                        str(worktree)], capture_output=True)
        (home / "config.toml").write_text(
            f'[projects."{root}"]\ntrust_level = "trusted"\n\n'
            f'[projects."{worktree}"]\ntrust_level = "trusted"\n')

        rows = []
        (root / ".codex").mkdir()
        shutil.copyfile(source, root / ".codex" / "config.toml")
        rows.append(("CONTROL   .codex at a trusted project root",
                     len(hooks_for(str(root), env)[0])))
        shutil.rmtree(root / ".codex")

        (worktree / ".codex").mkdir()
        shutil.copyfile(source, worktree / ".codex" / "config.toml")
        rows.append(("WORKTREE  .codex in the worktree only",
                     len(hooks_for(str(worktree), env)[0])))

        (root / ".codex").mkdir()
        shutil.copyfile(source, root / ".codex" / "config.toml")
        rows.append(("WORKTREE  .codex at the shared checkout",
                     len(hooks_for(str(worktree), env)[0])))

        for label, count in rows:
            print(f"  {label:<46} hooks={count}")
        control, in_worktree, at_shared = (count for _, count in rows)
        print()
        if control == 0:
            print("🔴 the control did not fire; this run settles nothing")
            return 1
        if in_worktree == 0 and at_shared > 0:
            print("🔴 In a git WORKTREE, project hooks are collected from the SHARED")
            print("   CHECKOUT. A registration in the worktree contributes nothing,")
            print("   with no warning and no error.")
            return 0
        print("The worktree's own registration DOES load; the finding does not reproduce.")
        return 1
    finally:
        shutil.rmtree(home, ignore_errors=True)
        subprocess.run(["git", "-C", str(root), "worktree", "remove", "--force",
                        str(root / ".claude" / "worktrees" / "wt")], capture_output=True)
        shutil.rmtree(root, ignore_errors=True)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--cwd", default=".")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true",
                        help="re-run the controlled experiment in scratch space")
    args = parser.parse_args(argv)

    if args.explain:
        return explain()

    result = report(str(Path(args.cwd).resolve()))
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"CODEX_HOOK_LOAD_STATE   {result['state']}")
        print()
        print(f"  cwd                          {result['cwd']}")
        print(f"  git worktree                 {result['is_git_worktree']}")
        print(f"  shared checkout              {result['shared_checkout']}")
        print(f"  .codex here                  {result['registration_in_worktree']}")
        print(f"  .codex at shared checkout    {result['registration_in_shared_checkout']}")
        print(f"  hooks loaded                 {len(result['hooks'])}")
        for hook in result["hooks"]:
            print(f"    {hook['eventName']} {hook['matcher']} "
                  f"source={hook['source']} trust={hook['trustStatus']}")
        if result["diagnosis"]:
            print()
            print(f"  🔴 {result['diagnosis']}")
    return 0 if result["state"] in (LOADED_TRUSTED, LOADED_UNTRUSTED) else 1


if __name__ == "__main__":
    sys.exit(main())
