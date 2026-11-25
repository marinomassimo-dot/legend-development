#!/usr/bin/env python3
"""The checks of a window handoff, printed as values: prepare the successor's brief, rename, verify.

Why it exists (2026-11-25, ADV). Every handoff was a ritual done by hand: recompute the checkpoint digests, fill a brief,
launch, wait for release and bind, then rename two sessions in the `claude agents` view with a private tmux script. A ritual
earns a tool only if the tool PRINTS what it checked, so each line below is a measured value, not a promise.

    prepare  digests recomputed from <remote>/main, the brief filled from a template, the launch commands PRINTED
    rename   demote the old window to PREVIOUS, then promote the new one to CURRENT; each step proved by the listing
    verify   released / bound / first action / labels, all read from `mandate_watch.py` (no logic of its own); then,
             report only, what keeps the old window's worktree and every worktree with no reason to keep
             (`branch_hygiene.py --removal`), so that a cleanup is seen at each handoff and not at the disk alarm

What it never does: it does not start a model (`claude --bg`), stop, retire or delete a session, or write a repository file.
The launch stays a command the launcher types, so a permission control judges that act itself and never a wrapper around it.
The only thing it drives is the runtime's own rename (ctrl+r in `claude agents`, in a tmux session it creates and closes):
the runtime has no headless rename. If the screen is not what it expects it stops before saving and says what it saw.

    python3 framework/scripts/window_handoff.py prepare --template T.txt --worktree he_o_YYYYMMDD --task <TASK_ID> \\
        --old <session id> --checkpoint K=<path on main> [--checkpoint M=<path>@<expected sha256>] [--set KEY=VALUE] --out brief.txt
    python3 framework/scripts/window_handoff.py rename --role HE --task <TASK_ID> --old <session> --new <session> [--dry-run]
    python3 framework/scripts/window_handoff.py verify --task <TASK_ID> --old <session> --new <session>

Template placeholders: `__CKPT_<KEY>__` and `__SHA_<KEY>__` per `--checkpoint`, `__OLD_SESSION__`, `__OLD8__`, `__OLD_NAME__`,
`__TASK__`, and `__<KEY>__` per `--set`. Exit 0 when every check passed, 1 when one refused.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from repo_root import add_root_argument, resolve_root_argument  # noqa: E402
import branch_hygiene as bh  # noqa: E402

HEX64 = re.compile(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")
PLACEHOLDER = re.compile(r"__[A-Z0-9][A-Z0-9_]*?__")
NAME_TAIL = 18          # the view cuts a long name column; the last 18 characters stay readable (measured 2026-11-25)
POINTER = "❯"
RENAME_HINT = "enter to save"


class Refused(Exception):
    """A check failed; nothing further is done."""


def claude_binary() -> str:
    return shutil.which("claude") or str(Path.home() / ".local" / "bin" / "claude")


def run(argv: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(argv, capture_output=True, text=True, **kw)


def inventory() -> list[dict]:
    done = run([claude_binary(), "agents", "--all", "--json"])
    if done.returncode:
        raise Refused(f"`claude agents --all --json` failed: {done.stderr.strip()[:200]}")
    return json.loads(done.stdout)


def watch(root: Path, *args: str) -> subprocess.CompletedProcess:
    return run([sys.executable, "-B", str(HERE / "mandate_watch.py"), *args], cwd=root, stdin=subprocess.DEVNULL)


def find_session(sessions: list[dict], given: str) -> dict:
    if len(given) < 8:
        raise Refused(f"session id '{given}' is shorter than 8 characters")
    found = [s for s in sessions if str(s.get("sessionId", "")).startswith(given)]
    if len(found) != 1:
        raise Refused(f"session '{given}': {len(found)} matches in the listing, need exactly 1")
    return found[0]


def pairs(values: list[str], flag: str) -> dict[str, str]:
    out = {}
    for value in values:
        key, sep, rest = value.partition("=")
        if not sep or not re.fullmatch(r"[A-Z0-9][A-Z0-9_]*", key) or not rest:
            raise Refused(f"{flag} wants KEY=VALUE with an upper-case KEY, got '{value}'")
        out[key] = rest
    return out


# ------------------------------------------------------------------------------------------------ prepare

def checkpoint_digest(root: Path, ref: str, path: str) -> str:
    done = subprocess.run(["git", "-C", str(root), "show", f"{ref}:{path}"], capture_output=True)
    if done.returncode:
        raise Refused(f"checkpoint not on {ref}: {path}")
    return hashlib.sha256(done.stdout).hexdigest()


def fill(template: str, values: dict[str, str], digests: dict[str, str], old_id: str) -> str:
    """The brief, or Refused: no placeholder left, no digest that was not recomputed, every checkpoint and the old id carried."""
    text = template
    for key, value in values.items():
        text = text.replace(f"__{key}__", value)
    left = sorted(set(PLACEHOLDER.findall(text)))
    if left:
        raise Refused(f"unfilled placeholders: {', '.join(left)}")
    stray = sorted(set(HEX64.findall(text)) - set(digests.values()))
    if stray:
        raise Refused("the brief carries a sha256 that no --checkpoint recomputed (stale or hand-typed): "
                      + ", ".join(s[:16] for s in stray))
    missing = sorted(path for path, value in digests.items() if value not in text)
    if missing:
        raise Refused(f"checkpoint digest not carried by the brief: {', '.join(missing)}")
    if old_id not in text:
        raise Refused("the brief does not carry the old session's full id")
    return text


def prepare(args, root: Path, say=print, sessions: list[dict] | None = None) -> None:
    ref = f"{args.remote}/main"
    if not args.no_fetch:
        done = run(["git", "-C", str(root), "fetch", "-q", args.remote, "main"])
        if done.returncode:
            raise Refused(f"fetch of {args.remote} main failed: {done.stderr.strip()[:200]}")
    say(f"ref            {ref} = {run(['git', '-C', str(root), 'rev-parse', '--short=12', ref]).stdout.strip()}"
        f"{' (NOT fetched now)' if args.no_fetch else ''}")
    values, digests = pairs(args.set, "--set"), {}
    for key, spec in pairs(args.checkpoint, "--checkpoint").items():
        path, _, expected = spec.partition("@")
        value = checkpoint_digest(root, ref, path)
        local = root / path
        copy = "absent" if not local.is_file() else "same" if hashlib.sha256(local.read_bytes()).hexdigest() == value else "DIFFERS"
        say(f"checkpoint {key:<4} sha256 {value}  working copy {copy}  {path}")
        if expected and expected != value:
            raise Refused(f"checkpoint {key}: expected {expected[:16]}, {ref} holds {value[:16]}")
        values[f"CKPT_{key}"], values[f"SHA_{key}"], digests[path] = path, value, value
    if not digests:
        raise Refused("no --checkpoint: a successor's brief without a digest cannot be checked")
    sessions = inventory() if sessions is None else sessions
    old = find_session(sessions, args.old)
    say(f"old session    {old['sessionId']}  name '{old.get('name')}'  state {old.get('state')}")
    released = watch(root, "released", "--session", old["sessionId"], "--task", args.task)
    say(f"old release    {released.stdout.split(' ', 1)[0].strip() or '(no output)'} (exit {released.returncode}; the successor waits for it)")
    worktree = root / ".claude" / "worktrees" / args.worktree
    taken = worktree.exists() or any(s.get("name") == args.worktree for s in sessions)
    say(f"worktree       {worktree}  {'TAKEN' if taken else 'free'}")
    if taken:
        raise Refused(f"worktree or session name already used: {args.worktree}")
    values.update(OLD_SESSION=old["sessionId"], OLD8=old["sessionId"][:8], OLD_NAME=str(old.get("name")), TASK=args.task)
    brief = fill(Path(args.template).read_text(encoding="utf-8"), values, digests, old["sessionId"])
    out = Path(args.out).resolve()
    out.write_text(brief, encoding="utf-8")
    say(f"brief          {out}  {len(brief)} chars, {len(digests)} digests carried, 0 placeholders left")
    say("\nTYPE THESE YOURSELF (this tool does not run them):")
    say(f"  git -C {shlex.quote(str(root))} worktree add --detach {shlex.quote(str(worktree))} {ref}")
    say(f"  cd {shlex.quote(str(worktree))} && {claude_binary()} --bg --name {args.worktree} --model {args.model} "
        f"--effort {args.effort} --autocompact {args.autocompact} \"$(cat {shlex.quote(str(out))})\"")


# ------------------------------------------------------------------------------------------------- rename

class Tmux:
    """The runtime's agents view in a tmux session of our own; closed on the way out."""

    def __init__(self, cwd: Path, pause: float = 0.8):
        self.name, self.cwd, self.pause = f"handoff{int(time.time())}", cwd, pause

    def __enter__(self):
        done = run(["tmux", "new-session", "-d", "-s", self.name, "-x", "220", "-y", "60", "-c", str(self.cwd),
                    f"{shlex.quote(claude_binary())} agents"])
        if done.returncode:
            raise Refused(f"tmux could not start: {done.stderr.strip()[:200]}")
        for _ in range(60):
            time.sleep(0.5)
            if POINTER in self.screen():
                return self
        self.__exit__()
        raise Refused("the agents view did not draw within 30 s")

    def __exit__(self, *exc):
        run(["tmux", "kill-session", "-t", self.name])

    def screen(self) -> str:
        return run(["tmux", "capture-pane", "-p", "-t", self.name]).stdout

    def key(self, key: str) -> None:
        run(["tmux", "send-keys", "-t", self.name, key])
        time.sleep(self.pause)

    def type(self, text: str) -> None:
        run(["tmux", "send-keys", "-t", self.name, "-l", text])
        time.sleep(self.pause)


def selected_line(screen: str) -> str:
    return next((line for line in screen.splitlines() if POINTER in line), "")


def shows(line: str, name: str, end: str = r"(\s{2,}|\s*$)") -> bool:
    """The row's NAME COLUMN (pointer, state glyph, name) is this name, whole or cut with '…' keeping its readable tail.
    The summary on the same line never counts: on 2026-11-25 the old window's summary named the successor's temporary name and the old row was renamed."""
    row = re.match(r"^[\s" + POINTER + r"]*[^\w\s…]\s+", line)
    if not row:
        return False
    cell = line[row.end():]
    if re.match(re.escape(name) + end, cell):
        return True
    head, cut, rest = cell.partition("…")
    if not cut or len(name) <= NAME_TAIL or not name.startswith(head):
        return False
    return any(re.match(re.escape(name[-size:]) + end, rest) for size in range(len(name) - len(head) - 1, NAME_TAIL - 1, -1))


def rename_row(view, current: str, wanted: str, steps: int = 80) -> str:
    """Move to the row named `current`, type `wanted`, save only if the selected row then shows it. Returns the line saved."""
    for _ in range(steps):
        if shows(selected_line(view.screen()), current):
            break
        view.key("Down")
    if not shows(selected_line(view.screen()), current):
        raise Refused(f"row '{current}' not reached in {steps} keys; selected line: {selected_line(view.screen())[:100]!r}")
    view.key("C-r")
    if RENAME_HINT not in view.screen():
        view.key("Escape")
        raise Refused(f"not in rename mode ('{RENAME_HINT}' absent); nothing saved")
    view.key("C-a")
    view.key("C-k")
    view.type(wanted)
    line = selected_line(view.screen())
    if not shows(line, wanted, end=r"(\s|$)"):       # while typing, a name longer than the column may leave one space
        view.key("Escape")
        raise Refused(f"typed name not on the selected row; nothing saved. Seen: {line[:100]!r}")
    view.key("Enter")
    return line


def visible_name(role: str, label: str, session: str) -> str:
    return f"{role} - {label} {session[:8]}"


def rename_plan(sessions: list[dict], role: str, old: dict, new: dict) -> list[tuple[str, dict, str]]:
    """[(label, session, wanted name)], demotion first; Refused if another window already claims CURRENT for the role."""
    others = [s.get("name") for s in sessions if str(s.get("name", "")).startswith(f"{role} - CURRENT ")
              and s["sessionId"] not in (old["sessionId"], new["sessionId"])]
    if others:
        raise Refused(f"another window already carries CURRENT for {role}: {', '.join(others)}")
    if old["sessionId"] == new["sessionId"]:
        raise Refused("old and new are the same session")
    plan = [("demote", old, visible_name(role, "PREVIOUS", old["sessionId"])),
            ("promote", new, visible_name(role, "CURRENT", new["sessionId"]))]
    return [step for step in plan if step[1].get("name") != step[2]]


def unambiguous(sessions: list[dict], name: str) -> None:
    tail = name[-NAME_TAIL:]
    same = [s.get("name") for s in sessions
            if s.get("name") == name or (len(name) > NAME_TAIL and str(s.get("name", "")).endswith(tail))]
    if len(same) != 1:
        raise Refused(f"'{name}' selects {len(same)} rows by its last {NAME_TAIL} characters ({same}); rename that one by hand")


def rename(args, root: Path, say=print, listing=inventory, view_factory=Tmux, state=None) -> None:
    sessions = listing()
    old, new = find_session(sessions, args.old), find_session(sessions, args.new)
    state = state or (lambda sid: watch(root, "released", "--session", sid, "--task", args.task).stdout.split(" ", 1)[0].strip())
    old_state, new_state = state(old["sessionId"]), state(new["sessionId"])
    say(f"old {old['sessionId'][:8]}  '{old.get('name')}'  mandate {old_state}")
    say(f"new {new['sessionId'][:8]}  '{new.get('name')}'  mandate {new_state}")
    if old_state != "RELEASED" or new_state != "BOUND":
        raise Refused("rename only after the old window is RELEASED and the new one is BOUND")
    plan = rename_plan(sessions, args.role, old, new)
    for label, session, wanted in plan:
        say(f"plan  {label:<7} '{session.get('name')}' -> '{wanted}'")
    if not plan:
        say("nothing to rename: the listing already shows both names")
    if args.dry_run or not plan:
        return
    for label, session, wanted in plan:
        before = listing()
        current = find_session(before, session["sessionId"]).get("name")
        unambiguous(before, current)
        with view_factory(root) as view:
            rename_row(view, current, wanted)
        for _ in range(10):
            named = find_session(listing(), session["sessionId"]).get("name")
            if named == wanted:
                break
            time.sleep(args.settle)
        say(f"proof {label:<7} listing now names {session['sessionId'][:8]} '{named}'  {'OK' if named == wanted else 'NOT AS PLANNED'}")
        after = {s["sessionId"]: s.get("name") for s in listing()}
        others = [f"{s['sessionId'][:8]} '{s.get('name')}' -> '{after[s['sessionId']]}'" for s in before
                  if s["sessionId"] != session["sessionId"] and after.get(s["sessionId"], s.get("name")) != s.get("name")]
        if others:
            raise Refused(f"{label}: ANOTHER ROW CHANGED NAME, repair by hand before anything else: {'; '.join(others)}")
        if named != wanted:
            raise Refused(f"{label} not proved by the listing; later steps not run")


# ------------------------------------------------------------------------------------------------- verify

def cleanup(root: Path, old: dict, say, projects: Path) -> None:
    """Report only. A check that cannot run says so; it never changes the verdict of the handoff."""
    try:
        rows = bh.removal_rows(root, bh.worktrees(root), bh.resolve_base(root, None)["ref"], projects)
    except (bh.GitError, OSError) as why:
        say(f"cleanup        not checked: {str(why)[:200]}")
        return
    where = old.get("cwd")
    mine = next((r for r in rows if r["path"] == where), None)
    if mine:
        say(f"old worktree   {where}  keep: {'; '.join(mine['keep']) or 'no reason found'}")
    else:
        say(f"old worktree   no linked worktree ({where or 'no directory in the listing'})")
    free = [r["path"] for r in rows if not r["keep"]]
    say(f"removable      {len(free)} worktree(s) with no reason found to keep; nothing is removed, ask the owner first")
    for path in free:
        say(f"               {path}")


def verify(args, root: Path, say=print, sessions: list[dict] | None = None) -> None:
    sessions = inventory() if sessions is None else sessions
    old, new = find_session(sessions, args.old), find_session(sessions, args.new)
    for label, session in (("old", old), ("new", new)):
        done = watch(root, "released", "--session", session["sessionId"], "--task", args.task)
        say(f"{label} {session['sessionId'][:8]}  '{session.get('name')}'  mandate {done.stdout.split(' ', 1)[0].strip()}")
    done = watch(root, "handoff", "--task", args.task, "--old", old["sessionId"], "--new", new["sessionId"])
    try:
        report = json.loads(done.stdout)
    except ValueError:
        raise Refused(f"mandate_watch handoff gave no report: {(done.stdout + done.stderr).strip()[:300]}") from None
    say(f"handoff        {report.get('verdict')}  first action {report.get('first_action_after_bind_min')} min after bind  "
        f"successor tool calls {report.get('new', {}).get('tool_calls_after_bind')}")
    names = report.get("session_names") or {}
    say(f"labels         {names.get('state')}  pending renames {len(names.get('renames') or [])}")
    cleanup(root, old, say, Path(getattr(args, "projects_dir", "~/.claude/projects")).expanduser())
    if report.get("verdict") != "RUNNING" or names.get("state") != "CURRENT":
        raise Refused(f"handoff not complete: {report.get('next')}")


# ----------------------------------------------------------------------------------------------------- main

def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Window handoff checks printed as values: prepare, rename, verify. Never launches, stops or retires a session.")
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare", help="recompute checkpoint digests, fill the brief, PRINT the launch commands")
    p.add_argument("--template", required=True)
    p.add_argument("--worktree", required=True, help="new worktree and temporary session name")
    p.add_argument("--checkpoint", action="append", default=[], metavar="KEY=PATH[@SHA256]")
    p.add_argument("--set", action="append", default=[], metavar="KEY=VALUE")
    p.add_argument("--out", required=True)
    p.add_argument("--remote", default="development")
    p.add_argument("--no-fetch", action="store_true")
    p.add_argument("--model", default="sonnet")
    p.add_argument("--effort", default="high")
    p.add_argument("--autocompact", default="400000")
    r = sub.add_parser("rename", help="demote the old window, then promote the new one, each proved by the listing")
    r.add_argument("--role", required=True, help="visible role, for example HE, SCI, 'IT Orchestrator'")
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--settle", type=float, default=1.0, help=argparse.SUPPRESS)
    v = sub.add_parser("verify", help="released, bound, first action and labels, from mandate_watch")
    for each in (p, r, v):
        add_root_argument(each)
        each.add_argument("--task", required=True)
        each.add_argument("--old", required=True, help="old session id (full, or a unique prefix of 8)")
    for each in (r, v):
        each.add_argument("--new", required=True, help="new session id")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        root = resolve_root_argument(getattr(args, "root", None))
        done = run(["git", "-C", str(root), "rev-parse", "--path-format=absolute", "--git-common-dir"])
        if args.command == "prepare" and done.returncode == 0:
            root = Path(done.stdout.strip()).parent      # worktrees are created under the primary checkout
        {"prepare": prepare, "rename": rename, "verify": verify}[args.command](args, root)
    except Refused as why:
        print(f"REFUSED: {why}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
