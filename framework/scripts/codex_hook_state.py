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
import re
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

# ── revision 9: the states above could not tell two causes apart ───────────────────
#
# 🔴 `NOT_LOADED` was returned for BOTH "there is no config here" and "there is a config
# and the runtime declined to load it". Those need opposite repairs — the first wants a
# file placed, the second wants a trust decision — and a diagnostic that gives them one
# name sends the reader to fix the wrong thing. The runtime cannot separate them: an
# empty `hooks/list` with empty `warnings` and empty `errors` is what BOTH produce.
#
# So the discrimination cannot come from the runtime, and asking it harder was the wrong
# instinct. It comes from asking a SECOND, independent question that the filesystem can
# answer for free: is there a config layer here at all, and does it name hooks? The
# cross-product of "what the config says" and "what the runtime loaded" is what
# separates the causes.

CONFIG_ABSENT = "CONFIG_ABSENT"        # no config layer discoverable for this cwd
CONFIG_INVALID = "CONFIG_INVALID"      # a config exists and cannot be read
HOOKS_EMPTY = "HOOKS_EMPTY"            # a config exists, is readable, declares no hooks
HOOKS_LOADED_UNTRUSTED = "HOOKS_LOADED_UNTRUSTED"
HOOKS_LOADED_TRUSTED = "HOOKS_LOADED_TRUSTED"
TRUST_BLOCKED = "TRUST_BLOCKED"        # a config ON THE PATH names hooks, none loaded

#: 🔴 A fifth cause, and writing the first draft of this table is what found it.
#:
#: That draft called this repository's own worktree `TRUST_BLOCKED`: a `.codex` naming
#: five hooks, and `hooks/list` returning zero. Trust is a plausible story for that pair
#: and it is the WRONG one — the measured cause is in this module's own docstring.
#: codex-cli 0.147.0 resolves the project config layer through git to the SHARED
#: CHECKOUT, so a linked worktree's own `.codex` is never read, and no trust decision
#: was ever withheld because nothing was ever offered for review.
#:
#: The two need opposite repairs — this one wants a file moved, `TRUST_BLOCKED` wants a
#: human decision — which is the exact failure the P0 brief names: different causes
#: requiring different repairs must not collapse into one diagnostic state. The first
#: draft of the repair reproduced the defect it was repairing, one level in.
CONFIG_OFF_RESOLUTION_PATH = "CONFIG_OFF_RESOLUTION_PATH"

#: The vocabulary. `state_for` still returns the revision-8 value so nothing downstream
#: breaks; `diagnose` returns one of these, and the two are reported side by side so a
#: reader can see which distinction is new.
#:
#: 🔴 `CONFIG_DISCOVERED` was REMOVED in revision 10. It was declared with the comment
#: *"a config on the path names hooks, none loaded"* — which is, word for word, the
#: comment on `TRUST_BLOCKED`. Two names for one condition, and `classify_state` could
#: emit only the second, so the first was dead operational vocabulary: a state a reader
#: could find in the table, look for in a report, and never see. Removed rather than
#: made reachable, because inventing a transition to justify a name is how a vocabulary
#: grows past the distinctions it can actually draw.
#:
#: `test_runtime_diagnostics.py` now asserts that EVERY member of this tuple is produced
#: by a concrete `classify_state` fixture. A state that cannot be reached fails the suite
#: instead of sitting in the table.
DIAGNOSTIC_STATES = (
    CONFIG_ABSENT, CONFIG_INVALID, CONFIG_OFF_RESOLUTION_PATH,
    HOOKS_EMPTY, HOOKS_LOADED_UNTRUSTED, HOOKS_LOADED_TRUSTED, TRUST_BLOCKED,
    UNDERIVABLE,
)

#: 🔴 Never derivable from `hooks/list`. A hook that is loaded and trusted has still not
#: been shown to RUN, and one that has run has still not been shown to REFUSE anything.
#: Only a session probe reaches these, and that probe is a spend under Annex J.4.
NOT_DERIVABLE_WITHOUT_A_SESSION = ("FIRING", "ENFORCING")


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


def hooks_for(cwd: str, env: Optional[dict] = None) -> Tuple[Optional[List[dict]], str]:
    """The hooks the runtime reports, or `None` when it did not successfully answer.

    🔴 `None` and `[]` are DIFFERENT ANSWERS and revision 9 had only one of them.
    `answer.get("result", {}).get("data", [])` reduced a JSON-RPC **error** to an empty
    hook list, which `state_for` reported as `NOT_LOADED`, which `classify_state` then
    crossed with the filesystem and turned into `CONFIG_ABSENT` or `TRUST_BLOCKED` —
    sending the operator to place a file or to make a trust decision on the strength of
    a query that failed. Mirror injected `{"error":{"code":-32601}}` and watched it
    happen. A non-dict `result` did worse: it raised `AttributeError` out of a
    diagnostic.

    The whole of the repair is that a malformed, errored or absent answer is a FAILURE
    TO MEASURE, and a failure to measure is `UNDERIVABLE`:

    ```text
    transport failure / no answer      →  None   (UNDERIVABLE)
    an `error` member                  →  None   (UNDERIVABLE)
    no `result`, or `result` not an object  →  None
    `result.data` missing or not a list     →  None
    an entry with no `hooks` list           →  None
    `result.data == []`                →  []     a genuine, well-formed empty answer
    ```

    The last two lines are the boundary and they are drawn deliberately: an empty `data`
    is a complete answer meaning *no layer reported hooks*, while an entry that omits
    `hooks` is a shape this parser was not written against, and reading it leniently
    would be guessing about the field the whole diagnosis rests on.
    """
    answer, stderr = hooks_list(cwd, env)
    if answer is None:
        return None, stderr
    if not isinstance(answer, dict):
        return None, stderr + "\nthe app-server's reply was not a JSON object"
    if answer.get("error") is not None:
        return None, stderr + f"\n`hooks/list` returned a JSON-RPC error: {answer['error']!r}"
    if "result" not in answer:
        return None, stderr + "\n`hooks/list` replied with neither `result` nor `error`"
    result = answer.get("result")
    if not isinstance(result, dict):
        return None, stderr + "\n`hooks/list` replied with a `result` that is not an object"
    data = result.get("data")
    if not isinstance(data, list):
        return None, stderr + "\n`hooks/list` replied with a `result.data` that is not a list"
    if not data:
        return [], stderr
    entry = data[0]
    if not isinstance(entry, dict) or not isinstance(entry.get("hooks"), list):
        return None, stderr + "\n`hooks/list` replied with an entry carrying no `hooks` list"
    return entry["hooks"], stderr


def _count(hooks: Optional[List[dict]]) -> int:
    """How many hooks, with a NON-ANSWER reported as `-1` rather than as zero.

    The reachability experiment in `explain()` compares counts across three placements,
    and `0` there means *the runtime read the config and found no hooks* — the finding
    itself. A query that failed must not be able to produce that number.
    """
    return -1 if hooks is None else len(hooks)


def state_for(cwd: str) -> Tuple[str, List[dict], str]:
    """`(state, hooks, detail)` for one working directory."""
    hooks, stderr = hooks_for(cwd)
    if hooks is None:
        # 🔴 The runtime did not answer. Never tell the operator to make a trust
        # decision — or to place a config file — on the strength of a query that failed.
        return UNDERIVABLE, [], stderr
    if not hooks:
        return NOT_LOADED, [], stderr
    if all(hook.get("trustStatus") == "trusted" for hook in hooks):
        return LOADED_TRUSTED, hooks, stderr
    return LOADED_UNTRUSTED, hooks, stderr


# ── the second, independent question: what does the CONFIG say? ────────────────────

#: Where a Codex project config layer can live, in the order the runtime resolves them.
#: The SHARED CHECKOUT entry is not an extra guess: codex-cli 0.147.0 resolves the
#: project layer through git to the shared checkout, which is the measured finding this
#: module was written to record, so a worktree's own `.codex` is listed after it and
#: reported separately rather than being treated as the answer.
CONFIG_CANDIDATES = ("shared_checkout", "worktree", "user")

#: A `[[hooks...]]` table, or a `hooks` key. Read textually rather than with a TOML
#: parser: the standard library has `tomllib` only from 3.11, the guard has to run on
#: whatever interpreter the runtime brings, and the question here is "does this file
#: name hooks at all", not "what exactly do they say".
HOOK_TABLE = re.compile(r"^\s*\[+\s*hooks\b|^\s*hooks\s*=", re.M)


def config_layer(cwd: str) -> Dict[str, object]:
    """Which config files exist for this cwd, and do they name hooks?

    🔴 This is the half of the diagnostic the runtime cannot supply. `hooks/list`
    returning `[]` is the same observation whether the cause is a missing file or a
    withheld trust decision; the file's existence is what tells them apart, and it costs
    a `stat`.
    """
    shared = common_checkout_of(cwd)
    worktree = repo_root_of(cwd)
    #: 🔴 Measured for codex-cli 0.147.0, with the positive controls in this module's
    #: docstring, and version-bound: a linked worktree's own `.codex` is NOT read, the
    #: shared checkout's is. When the worktree IS the shared checkout the same directory
    #: is both, and it is on the path.
    linked_worktree = bool(shared and worktree and Path(shared) != Path(worktree))

    found: List[Dict[str, object]] = []
    seen = set()
    for name, base, on_path in (("shared_checkout", shared, True),
                                ("worktree", worktree, not linked_worktree),
                                ("user", os.path.expanduser("~"), True)):
        if not base:
            continue
        path = Path(base) / ".codex" / "config.toml"
        if str(path) in seen:
            continue
        seen.add(str(path))
        if not path.is_file():
            continue
        entry: Dict[str, object] = {"layer": name, "path": str(path),
                                    "on_resolution_path": on_path}
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            entry.update({"readable": False, "names_hooks": False, "detail": str(exc)})
        else:
            entry.update({"readable": True,
                          "names_hooks": bool(HOOK_TABLE.search(text)), "detail": ""})
        found.append(entry)

    on_path = [e for e in found if e["on_resolution_path"]]
    return {
        "layers": found,
        "linked_worktree": linked_worktree,
        "on_path_names_hooks": any(e.get("names_hooks") for e in on_path),
        "off_path_names_hooks": any(e.get("names_hooks") for e in found
                                    if not e["on_resolution_path"]),
        "any_unreadable": any(not e.get("readable") for e in found),
    }


def classify_state(runtime_state: str, hooks: List[dict],
                   config: Dict[str, object]) -> str:
    """The decision itself, as a PURE function of the two observations.

    🔴 Separated from `diagnose` so a test can drive every branch without a runtime.
    It was inline, and the only test of the `CONFIG_OFF_RESOLUTION_PATH` branch asserted
    that two CONSTANTS were unequal — which is true however the branch is written.
    A mutation that reported an off-path config as `TRUST_BLOCKED` survived the suite,
    because nothing in it ever ran this decision.
    """
    if runtime_state == UNDERIVABLE:
        return UNDERIVABLE
    if hooks:
        return (HOOKS_LOADED_TRUSTED if runtime_state == LOADED_TRUSTED
                else HOOKS_LOADED_UNTRUSTED)
    if config.get("any_unreadable"):
        return CONFIG_INVALID
    if not config.get("layers"):
        return CONFIG_ABSENT
    if config.get("on_path_names_hooks"):
        # A file the runtime DOES read, naming hooks, and none loaded. Trust is the
        # remaining condition — the runtime does not say so, so the name records what
        # was derived and `config` records the evidence it was derived from.
        return TRUST_BLOCKED
    if config.get("off_path_names_hooks"):
        return CONFIG_OFF_RESOLUTION_PATH
    return HOOKS_EMPTY


def diagnose(cwd: str) -> Dict[str, object]:
    """Cross the config layer with the runtime's answer, and name ONE cause.

    The whole table, so the reasoning is inspectable rather than implied:

    ```text
    config                        hooks/list     diagnostic         repair
    ───────────────────────────   ───────────    ────────────────   ──────────────────
    no config file anywhere       []             CONFIG_ABSENT      place a config layer
    a file that cannot be read    []             CONFIG_INVALID     fix the file
    files, none naming hooks      []             HOOKS_EMPTY        declare the hook
    hooks named only OFF the      []             CONFIG_OFF_        move the file to a
      resolution path                            RESOLUTION_PATH      layer that is read
    hooks named ON the path       []             TRUST_BLOCKED      a trust decision is
                                                                      owed by a human
    any                           [h] untrusted  HOOKS_LOADED_      the per-hook review
                                                   UNTRUSTED
    any                           [h] trusted    HOOKS_LOADED_      nothing; and still
                                                   TRUSTED            not FIRING
    any                           no answer      UNDERIVABLE        app-server did not run
    ```

    The last two rows of the "loaded" column are where the honesty is: neither says the
    hook FIRES, and `firing`/`enforcing` are returned as `NOT_TESTED` from every branch
    because no amount of `hooks/list` can reach them.
    """
    runtime_state, hooks, detail = state_for(cwd)
    config = config_layer(cwd)
    state = classify_state(runtime_state, hooks, config)

    return {
        "cwd": cwd,
        "diagnostic_state": state,
        "runtime_state": runtime_state,
        "config": config,
        "hooks": hooks,
        "hook_sources": [h.get("sourcePath") or h.get("source") for h in hooks],
        "trust_status": sorted({str(h.get("trustStatus")) for h in hooks}) or [],
        "codex_version": codex_version(),
        # 🔴 Both streams, always, and never only on the failure path. Revision 8
        # returned stderr and then classified on two substrings that only its own
        # failure messages contained, so on the success path the stream was carried and
        # never read — which is the same as discarding it, with a longer signature.
        "stderr": (detail or "").strip()[:1000],
        "firing": "NOT_TESTED",
        "enforcing": "NOT_TESTED",
    }


def codex_version() -> str:
    try:
        out = subprocess.run(["codex", "--version"], capture_output=True, text=True,
                             timeout=15)
    except (OSError, subprocess.SubprocessError) as exc:
        return f"<underivable: {exc}>"
    return (out.stdout or out.stderr).strip() or "<no version reported>"


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
                     _count(hooks_for(str(root), env)[0])))
        shutil.rmtree(root / ".codex")

        (worktree / ".codex").mkdir()
        shutil.copyfile(source, worktree / ".codex" / "config.toml")
        rows.append(("WORKTREE  .codex in the worktree only",
                     _count(hooks_for(str(worktree), env)[0])))

        (root / ".codex").mkdir()
        shutil.copyfile(source, root / ".codex" / "config.toml")
        rows.append(("WORKTREE  .codex at the shared checkout",
                     _count(hooks_for(str(worktree), env)[0])))

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
