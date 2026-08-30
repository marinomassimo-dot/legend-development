#!/usr/bin/env python3
"""The write-guard POLICY, stated once and independent of any runtime.

This module is the single source of truth for *what is forbidden*. It knows nothing
about hooks, payloads, JSON wire formats or which runtime is asking. Given a shell
command as text it returns a denial reason, or `None` to allow.

The two rules below are not hypothetical. Both were committed in this repository on
2026-08-04 by an agent that had every relevant instruction in front of it.

**1. Blanket staging.** `git add -A` staged another actor's uncommitted work — a blind
derivation run in progress — into a commit whose message described something else
entirely. The author never saw the files. Blanket staging assumes the working tree
belongs to one actor, and in this repository it does not: Claude and Codex work in it
concurrently. Stage paths you name.

**2. Shell writes onto repository files.** The `Write` tool refuses to overwrite a file
the session has not read. That guard was bypassed by doing the write from Bash instead —
`python3 - <<'PY' ... Path(x).write_text(...)` — which destroyed a file another actor had
authored and declared. The guard existed; the shell was the way around it. Use
`Write`/`Edit`, whose read-before-overwrite rule is the point, or invoke a committed
script by name.

Temp-only writes are allowed: scratchpad and `/tmp` work is not what went wrong.

## Why this is a parser and not a list of forbidden strings

Revision 1 matched substrings and blanked quoted spans, because a literal match blocked
the very commit that *documented* `git add -A`. That exemption was the hole: it is
exactly where `bash -c "git add -A"` hides, and eight further shapes with it. A blacklist
long enough to catch the wrappers is also long enough to catch the prose.

So the command is **parsed** instead. `echo "git add -A"` and `bash -c "git add -A"` carry
the same bytes and differ in structure: in the first the quoted span is an *argument to
`echo`*, in the second it is a *script argument to a shell*, and only the second is
re-analysed as a command. Nothing is exempted for being quoted, and nothing is condemned
for containing a word.

The classification has three outcomes, and the third is not a synonym for either:

```
PROHIBITED   a mutation is derivable AND its target is inside the repository,
             or the target is not named in the command at all
ALLOWED      no mutation is derivable, or every target is scratch space
UNDERIVABLE  a mutation is derivable and its target cannot be resolved —
             a substitution, a variable, a glob, or an unparseable command
```

🔴 `UNDERIVABLE` **fails closed**, and only for a command in which a write primitive was
already found. A read-only command containing `$(...)` stays allowed: refusing to reason
is not the same as having something to refuse.

## Scope, declared — what this still does NOT stop

The policy is about *content* mutation reachable from the shell. It does not police
`chmod`/`chown`, `git reset --hard` / `git checkout --` / `git clean`, `git push`, or a
committed script that writes when invoked by name — that last one is deliberate and is
the escape hatch every denial names. Those are separate entries, printed by
`framework/scripts/runtime_parity.py --characterize` and asserted open by
`framework/scripts/test_pre_tool_use_guard.py`.
"""
from __future__ import annotations

import posixpath
import re
import shlex
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
import effect_model as em  # noqa: E402
import repo_topology as rt  # noqa: E402
import runtime_config as rc  # noqa: E402
import session_binding as sb  # noqa: E402

# ── outcomes ───────────────────────────────────────────────────────────────────────

PROHIBITED = "PROHIBITED"
ALLOWED = "ALLOWED"
UNDERIVABLE = "UNDERIVABLE"

#: A target the command does not name at all — `xargs rm`, `find -delete`, a patch body
#: whose paths could not be read. Distinct from a named target that cannot be resolved.
UNNAMED = "\x00UNNAMED\x00"
#: A token whose value depends on expansion: `$(...)`, `` `...` ``, `$VAR`, a glob.
OPAQUE = "\x00OPAQUE\x00"


#: Every rule this policy can derive, mapped onto the closed effect vocabulary.
#:
#: 🔴 The mapping is total and `test_pre_tool_use_guard.py::EveryRuleMapsToAnEffect`
#: asserts it over the rules the module actually emits, not over this dictionary. A rule
#: added without an entry does not silently become harmless — `Finding.effect` returns
#: `UNKNOWN_EFFECT` for an unmapped rule, which is denied under every authority. The
#: failure direction of forgetting is refusal.
RULE_EFFECT = {
    "BLANKET_STAGING": em.STAGE,
    "NAMED_STAGING": em.STAGE,
    "COMMIT": em.COMMIT,
    "REDIRECTION": em.WRITE,
    "FILE_WRITE": em.WRITE,
    "FILE_DELETE": em.DELETE,
    "FILE_RENAME": em.RENAME,
    "IN_PLACE_EDIT": em.WRITE,
    "PATCH_APPLY": em.WRITE,
    "PROGRAM_WRITE": em.WRITE,
    "ARCHIVE_EXTRACT": em.ARCHIVE_EXTRACT,
    "PERMISSION_CHANGE": em.PERMISSION_CHANGE,
    "REF_MUTATION": em.REF_MUTATION,
    "NETWORK_WRITE": em.NETWORK_WRITE,
    "DELEGATE": em.DELEGATE,
    # Shapes whose effect is precisely what could not be derived.
    "OPAQUE_PROGRAM": em.UNKNOWN_EFFECT,
    "STDIN_SHELL": em.UNKNOWN_EFFECT,
    "WRAPPER_DEPTH": em.UNKNOWN_EFFECT,
    "SHELL_OUT": em.UNKNOWN_EFFECT,
    # 🔴 Revision 11. The command NAMES a protected object and the derivation produced
    # nothing about it. See `SILENCE_IS_NOT_ABSENCE` below.
    "UNDERIVED_OPERAND": em.UNKNOWN_EFFECT,
    "UNDERIVED_MODULE_OPERAND": em.UNKNOWN_EFFECT,
    "UNDERIVED_STDIN_CHILD": em.UNKNOWN_EFFECT,
    "EXECUTION_CONTROL": em.WRITE,
    "CONFIG_WRITE": em.WRITE,
}

#: 🔴 **A target-classification defence cannot protect against a derivation whose failure
#: mode is silence.** Revision 11 exists for this sentence.
#:
#: Revisions 9 and 10 wrote four scope defences — `RUNTIME_CONFIG`, `GIT_COMMON_DIR`,
#: `PEER_WORKTREE`, `SHARED_CHECKOUT` — and every one of them is DOWNSTREAM of deriving
#: an effect at all. A scope is a property of a derived TARGET: with no effect there is
#: no target, with no target there is no scope, and the defence never runs. Measured at
#: `e01d6d2`, four vectors that derive NOTHING reached the engine, the adapter, the
#: effect model, both registrations and the shim — 24 of 36 cells — while `echo x >` and
#: `rm` were refused against all six.
#:
#: The rules below are the repair, and they are stated as a threshold rather than as a
#: blanket invariant on purpose. A peer proposed `effects() == [] → DENY` for every
#: command; measured over this corpus's 59 runnable must-refuse cases it found ZERO
#: violations, and it newly refused **11 positive controls** — `git status --short`,
#: `cat <peer>/CLAUDE.md`, `codex --version`. Silence is the NORMAL condition of every
#: read, so the rule cannot be "silence denies". It has to be:
#:
#: > an invocation whose effect derivation this policy KNOWS to be incomplete, which
#: > NAMES an object in a scope no authority grants, must fail closed.
#:
#: Two thresholds, because the two populations differ in how closed they are:
_UNDERIVED_STRICT = frozenset({em.PEER_WORKTREE, em.SHARED_CHECKOUT,
                               em.GIT_COMMON_DIR, em.RUNTIME_CONFIG, em.UNDERIVABLE})
#: An UNCLASSIFIED program is open vocabulary — anything on `PATH` — so `INSIDE_REPO` is
#: deliberately NOT here. `shasum framework/x`, `jq . framework/a.json`, `pytest
#: framework/scripts/test_x.py` are ordinary work, and a guard that refuses ordinary work
#: is a guard that gets turned off. What it costs is stated as residual debt rather than
#: hidden: an unknown program writing INSIDE the assigned worktree is still underived.
#:
#: 🔴 And `UNDERIVABLE` is not here either, which the FIRST draft of this rule got wrong.
#: Measured over every fenced shell line in every committed markdown file of this
#: repository — 323 commands from 68 files, a population this candidate did not choose —
#: the draft newly refused:
#:
#: ```text
#: gh repo view "$OWNER/$REPO" --json nameWithOwner,visibility,url   ← release/PUBLISH_RUNBOOK.md
#: ```
#:
#: A variable operand under an unmodelled program is the ordinary shape of documented
#: work, not a reach at a protected object. The four scopes that remain are RESOLVED,
#: specific objects; `UNDERIVABLE` is *I could not tell*, and failing closed on it here
#: refuses `docker run $IMAGE` and its kin.
#:
#: The draft was also internally inconsistent, which is the sharper argument: `mytool
#: "$VAR"` ALLOWED and `mytool $VAR/x` DENIED — the same shape, two answers, decided by
#: whether the value happened to contain a slash. A threshold that answers differently
#: for one operand's spelling is not expressing a scope at all.
#:
#: The residual gap is DECLARED: `someunknowntool "$PEER/x"` — an unmodelled program
#: reaching a peer through a variable — is allowed. The spelled path is not.
UNDERIVED_OPERAND_SCOPES = _UNDERIVED_STRICT - frozenset({em.UNDERIVABLE})
#: A `-m` MODULE is a CLOSED set of fourteen whose members were each executed and
#: snapshotted, so `INSIDE_REPO` belongs here. The over-refusal — `python3 -m this
#: framework/x` now denies — is the point: refusing an inert command costs a sentence in
#: a denial message; allowing `python3 -m gzip .claude/settings.json` costs the guard.
UNDERIVED_MODULE_SCOPES = _UNDERIVED_STRICT | frozenset({em.INSIDE_REPO})


class Finding:
    """One derived mutation: what would write, where, and how that was decided.

    A finding is the policy's own vocabulary; `effect` projects it onto the shared one
    in `effect_model.py`, which is the only vocabulary `post_effect_verify.py` can also
    speak. The two are kept separate because a rule name says *how the guard decided*
    (`IN_PLACE_EDIT`) and an effect kind says *what would happen* (`WRITE`), and a
    filesystem delta can corroborate the second and never the first.
    """

    def __init__(self, rule: str, primitive: str, targets: Sequence[str], detail: str = "",
                 scope: Optional[str] = None):
        self.rule = rule
        self.primitive = primitive
        self.targets = list(targets)
        self.detail = detail
        # 🔴 A scope the finding DECLARES, overriding path classification. Needed
        # because a target is not always a path: `git push development` names a remote,
        # and classifying `development` as a path puts a publication at INSIDE_REPO —
        # the one scope where the guard would wave it through. Set it only where the
        # target is known not to be a working-tree path.
        self.scope = scope

    @property
    def effect(self) -> str:
        return RULE_EFFECT.get(self.rule, em.UNKNOWN_EFFECT)

    def __repr__(self) -> str:  # pragma: no cover - diagnostics only
        return f"Finding({self.rule!r}, {self.primitive!r}, {self.targets!r})"


# ── the command shapes that carry other commands ───────────────────────────────────

#: 🔴 `tcsh` and `csh` added in revision 12. They are not version spellings of anything —
#: they are separate shells with their own `-c` — so normalisation could not reach them
#: and this is a DECLARED list extension. Measured at revision 11: `tcsh -c '<blanket>'`
#: and `csh -c '<blanket>'` both ALLOWED. The shell family is one of the few genuinely
#: closed sets in this module, which is why extending it is defensible here and is not
#: the answer for `TRANSPARENT_WRAPPERS` — see `unclassified`.
SHELL_BINARIES = frozenset({"sh", "bash", "zsh", "dash", "ksh", "mksh", "ash", "fish",
                            "busybox", "tcsh", "csh"})
SHELL_SCRIPT_FLAGS = frozenset({"-c", "-lc", "-ic", "-lic", "-ilc", "-cl", "-li", "-il"})

#: Wrappers that run their remaining argv as a command, after their own options.
#: The value maps each wrapper's own value-taking flags — dropping every `-x` token
#: blindly is how `nohup bash -c '…'` loses the `-c` and stops looking like a shell.
TRANSPARENT_WRAPPERS = {
    "nohup": frozenset(),
    "nice": frozenset({"-n", "--adjustment"}),
    "ionice": frozenset({"-c", "-n", "-p", "--class", "--classdata", "--pid"}),
    "stdbuf": frozenset({"-i", "-o", "-e", "--input", "--output", "--error"}),
    "setsid": frozenset(),
    "time": frozenset({"-f", "-o", "--format", "--output"}),
    "command": frozenset(),
    "builtin": frozenset(),
    "exec": frozenset({"-a"}),
    "sudo": frozenset({"-u", "-g", "-U", "-C", "-p", "-r", "-t", "--user", "--group", "--prompt"}),
    "doas": frozenset({"-u", "-C"}),
    "caffeinate": frozenset({"-t", "-w"}),
    "script": frozenset({"-c"}),
    "arch": frozenset({"-arch"}),
    "unbuffer": frozenset(),
}
#: `timeout 30 CMD`, `chroot /dir CMD` — one positional operand before the child argv.
POSITIONAL_WRAPPERS = {
    "timeout": frozenset({"-k", "--kill-after", "-s", "--signal"}),
    "gtimeout": frozenset({"-k", "--kill-after", "-s", "--signal"}),
    "chroot": frozenset({"--userspec", "--groups"}),
}

#: Wrappers whose child receives its operands from stdin, so the command never names
#: the paths it acts on. That is the blanket-staging defect in a different costume.
STDIN_FED_WRAPPERS = frozenset({"xargs", "gxargs", "parallel"})

INTERPRETERS = frozenset({"python", "python2", "python3", "perl", "ruby", "node", "php", "deno", "bun"})
#: Interpreter flags whose value is a program body rather than a file.
INLINE_PROGRAM_FLAGS = frozenset({"-c", "-e", "-E", "--eval", "--exec"})

# ── delegation to another agent runtime ────────────────────────────────────────────

#: Binaries that can start an agent session which will act on this repository on its own.
#: Measured allowed on revision 8, 2026-08-29: `codex exec 'do it'`,
#: `codex exec --full-auto 'do it'` and `claude -p 'write it'` were ordinary shell.
#:
#: 🔴 The membership test is on the BINARY and the exemption list is what is enumerated,
#: not the other way round. `codex exec` and `codex resume` and whatever the next
#: subcommand is called all delegate; `codex --version` does not. Enumerating the
#: delegating subcommands would mean a new one ships allowed, and the whole point of a
#: fail-closed rule is which side of it a surprise lands on.
DELEGATING_BINARIES = frozenset({"codex", "claude"})

#: Invocations of those binaries that start no session. Everything else delegates.
#: `app-server` is here because `codex_hook_state.py` documents it as the way to ask the
#: runtime what hooks it would load — a local JSON-RPC service, no prompt, no turn, and
#: explicitly not a spend under Annex J.4.
DELEGATION_EXEMPT_SUBCOMMANDS = frozenset({
    "app-server", "mcp", "plugin", "login", "logout", "doctor", "hooks", "completion",
})
DELEGATION_EXEMPT_FLAGS = frozenset({"--version", "-V", "--help", "-h"})

#: 🔴 Revision 10. Nine launcher spellings reached `codex` and `claude` without ever
#: being read as delegation, because the binary this policy tests is `argv[0]` and
#: `argv[0]` was the launcher. Every one measured ALLOWED against the revision-9 engine
#: on 2026-08-29:
#:
#: ```text
#: npx codex exec 'go'        pnpm dlx codex exec 'go'    pipx run codex exec 'go'
#: npx -y codex exec 'go'     yarn dlx codex exec 'go'    npm exec codex exec 'go'
#: bunx codex exec 'go'       uvx codex exec 'go'         npx claude -p 'write x'
#: ```
#:
#: The repair is UNWRAPPING, not a blacklist. A launcher fetches a package and then runs
#: a program out of it, so whatever that program does, the launcher does — which is the
#: rule already applied to `nohup`, `timeout`, `env` and `sudo`. A name-based rule would
#: have to enumerate every launcher AND every delegating binary; unwrapping needs
#: neither, and `npx cowsay hi` stays allowed, which is the control that keeps this a
#: derivation rather than a ban on `npx`.
#:
#: The key is the launcher's OWN words: `("npx",)` consumes one, `("pnpm", "dlx")` two.
#: The value is that launcher's own value-taking flags, so `npx -p pkg codex exec` does
#: not read `pkg` as the program.
PACKAGE_LAUNCHERS = {
    ("npx",): frozenset({"-p", "--package", "-c", "--call", "--node-options",
                         "--node-arg", "--userconfig", "--shell"}),
    ("bunx",): frozenset({"--bun"}),
    ("uvx",): frozenset({"--from", "-p", "--python", "--with", "--index", "--index-url"}),
    ("pnpm", "dlx"): frozenset({"--package", "-p", "--shell-mode"}),
    ("yarn", "dlx"): frozenset({"--package", "-p"}),
    ("pipx", "run"): frozenset({"--spec", "--python", "--pip-args", "--index-url"}),
    ("npm", "exec"): frozenset({"-p", "--package", "-c", "--call", "--userconfig"}),
    ("pnpm", "exec"): frozenset(),
    ("yarn", "exec"): frozenset(),
    ("bun", "x"): frozenset({"--bun"}),
}

#: Launcher flags whose VALUE is a shell command rather than a package name. `npx -c
#: 'codex exec go'` is a shell string, and reading it as a package name would drop the
#: command inside it — the same defect as stringifying an argv, one level out.
LAUNCHER_COMMAND_FLAGS = frozenset({"-c", "--call"})

#: 🔴 A chmod MODE operand, which revision 9 read as an option and lost. `chmod -x
#: <scratch>` reported `PERMISSION_CHANGE` at `UNNAMED` scope, which no authority
#: grants — so it failed CLOSED, and refused a legitimate scratch act. `-R`, `-v`, `-f`,
#: `-h` and the rest are unambiguous because `R`, `v`, `f` and `h` are not mode letters;
#: `-r`, `-w`, `-x`, `-s`, `-t` and `-X` are modes because neither GNU nor BSD `chmod`
#: has an option by those names. The symbolic and octal forms are both here because
#: `chmod 755 f` had already been fixed by a different mechanism (a positional skip),
#: and one rule that finds the mode wherever it sits replaces both.
CHMOD_MODE = re.compile(r"^(?:[ugoa]*[-+=][rwxXstugo]*|[0-7]{1,4})$")

# ── residual command families (M-06) ───────────────────────────────────────────────

#: Editors that rewrite the file they are pointed at. Driven from a script flag they are
#: batch writers, and `ed -s f`, `ex -sc wq f` and `vim -es -c wq f` were all allowed on
#: revision 8. Their operands are their targets, whatever the script says.
BATCH_EDITORS = frozenset({"ed", "ex", "vi", "vim", "nvim", "emacs", "nano", "sponge"})

#: Programs whose in-place flag makes them rewrite their operands. `sed` keeps its own
#: branch above because BSD `sed -i ''` consumes an empty suffix as the option value;
#: this is the general family, and it closes `awk -i inplace` and `gawk -i inplace`.
IN_PLACE_PROGRAMS = frozenset({"awk", "gawk", "mawk", "nawk", "ruby", "rpl", "crudini"})

#: Programs that write a SERIES of files at a named prefix. The prefix is the target and
#: the suffixes are generated, so the write is to everything under it.
SPLITTERS = {"split": ("-a", "--suffix-length", "-b", "--bytes", "-C", "--line-bytes",
                       "-l", "--lines", "-n", "--number", "--additional-suffix"),
             "csplit": ("-f", "--prefix", "-b", "--suffix-format", "-n", "--digits")}

#: Package managers whose install verb writes into a directory the flags name — or, when
#: they do not, into a location the command never states.
PACKAGE_MANAGERS = frozenset({"npm", "pnpm", "yarn", "pip", "pip3", "uv", "gem",
                              "cargo", "bundle", "poetry", "composer"})
INSTALLING_SUBCOMMANDS = frozenset({"install", "i", "add", "ci", "update", "upgrade",
                                    "remove", "uninstall", "rm", "link", "sync"})
#: 🔴 Revision 12. The verbs under which a package manager EXECUTES rather than installs.
#: `uv run codex exec` allowed while `uvx codex exec` denied — the same act, split across
#: two branches because one spelling was a declared launcher and the other was not.
PACKAGE_RUN_SUBCOMMANDS = frozenset({"run", "exec", "x", "dlx", "tool"})
PACKAGE_TARGET_FLAGS = ("-t", "--target", "--prefix", "--root", "--install-dir",
                        "--path", "--dest", "--destination")

#: Python `-m` modules that only read. Everything else run through `-m` is UNKNOWN_EFFECT.
#:
#: 🔴 The list is positive and short on purpose. `python3 -m pip install -t framework/ x`
#: was ALLOWED on revision 8 — `-m` was not read at all, so a module that installs into
#: the repository looked like an interpreter with no inline program. Enumerating the
#: WRITING modules instead would have to enumerate every module anyone might ever run.
#:
#: 🔴 **Four of the fourteen WRITE, and one of them was cited as this list's own
#: control.** All fourteen were executed in a disposable directory, snapshotted before
#: and after:
#:
#: ```text
#: python3 -m json.tool a.json out.json   → NEW out.json    🔴 THE CITED CONTROL
#: python3 -m pydoc -w os                 → NEW os.html     🔴
#: python3 -m gzip a.txt                  → NEW a.txt.gz    🔴
#: python3 -m py_compile m.py             → __pycache__, with sys.pycache_prefix cleared
#: the other ten                          → wrote nothing, rc=0
#: ```
#:
#: One-argument `json.tool` prints to stdout, which is what made it look safe; the
#: two-argument form is `json.tool INFILE OUTFILE` and it writes. `pydoc` is the same
#: shape — read-only until one flag makes it a writer.
#:
#: **The class is not "host-dependent" and it is not four deletions.** Membership is
#: judged per MODULE; write capability is a property of the module's ARGV. A module-name
#: allowlist cannot express "read-only" for anything that takes an output operand, and
#: four of fourteen take one. So the repair is per-module ARGV DERIVATION — the mapping
#: below — plus `UNDERIVED_MODULE_OPERAND` behind it, which fails closed for a member
#: that names a protected object and derives nothing, whether or not anyone measured it.
#: `py_compile` is host-dependent (Apple's CommandLineTools Python sets
#: `sys.pycache_prefix`, which MASKS the write on this machine and on no other); the
#: other three are argv-dependent and wrong on every host including this one.
READ_ONLY_MODULES = frozenset({
    "json.tool", "pydoc", "this", "site", "sysconfig", "platform", "timeit",
    "calendar", "base64", "gzip", "tokenize", "dis", "ast", "py_compile",
})

#: How each argv-conditioned member derives its own write targets, given the module's
#: own argv. `None` from a model means *this invocation writes nothing*; a list means
#: those paths are written. The backstop still runs either way.
#:
#: `UNNAMED` is used where the destination is real but the command does not state it —
#: `pydoc -w os` writes `os.html` into the working directory, which is not in the argv.


def _model_json_tool(rest: Sequence[str]) -> List[str]:
    """`json.tool [INFILE [OUTFILE]]` — the SECOND positional is written."""
    positional = [t for t in rest if not t.startswith("-")]
    return positional[1:2]


def _model_pydoc(rest: Sequence[str]) -> List[str]:
    """`pydoc -w NAME` writes `NAME.html` into the working directory, unnamed."""
    return [UNNAMED] if any(t == "-w" for t in rest) else []


def _model_gzip(rest: Sequence[str]) -> List[str]:
    """`gzip FILE` writes `FILE.gz` AND removes `FILE`; `-d` reverses it.

    Both ends are reported, because a compression that deletes its input is a mutation
    of the input whatever it does with the output — the same reasoning `mv` gets.
    """
    positional = [t for t in rest if not t.startswith("-")]
    out: List[str] = []
    for path in positional:
        out.append(path)
        out.append(path[:-3] if path.endswith(".gz") else path + ".gz")
    return out or ([UNNAMED] if not positional else [])


def _model_py_compile(rest: Sequence[str]) -> List[str]:
    """`py_compile SRC` writes `__pycache__/…` BESIDE each source, unless the host
    interpreter sets `sys.pycache_prefix`. The guard cannot read the host interpreter's
    build, so the destination is the source's own directory and the answer does not
    depend on which machine is asking."""
    positional = [t for t in rest if not t.startswith("-")]
    return [posixpath.join(posixpath.dirname(p) or ".", "__pycache__")
            for p in positional] or [UNNAMED]


MODULE_WRITE_MODEL = {
    "json.tool": _model_json_tool,
    "pydoc": _model_pydoc,
    "gzip": _model_gzip,
    "py_compile": _model_py_compile,
}

#: 🔴 Programs whose entire effect is READ, whatever their argv — revision 11.
#:
#: This exists so that `UNDERIVED_OPERAND` can fail closed on an UNCLASSIFIED program
#: without refusing the reads that are this repository's declared positive controls:
#: `cat <peer>/CLAUDE.md`, `grep -rn x <peer>/framework`, `head <git-common-dir>/config`.
#: Every member is a program that has no write mode reachable from its own argv, or
#: whose write mode is already branched on above (`sed -i`, `awk -i`, `find -delete`).
#:
#: It is a POSITIVE list and it is the new frontier: a reading tool absent from it that
#: names a peer worktree, the shared checkout, the common dir or the runtime
#: registration now fails closed. That is the correct direction for a surprise to land,
#: and the cost is one entry.
#: 🔴 **Split in revision 12, and the split is the repair.**
#:
#: Revision 11 had ONE reader set and exempted it BEFORE the `UNDERIVED_OPERAND`
#: threshold, so a member with a write mode reached every confined scope. Measured
#: against revision 11 — 15 of 15 cells, `tee` denying at the same path in all of them:
#:
#: ```text
#:                     PEER_WORKTREE   SHARED_CHECKOUT   RUNTIME_CONFIG
#: sort -o             ALLOW           ALLOW             ALLOW
#: sed -n 'w FILE'     ALLOW           ALLOW             ALLOW
#: awk '{print > F}'   ALLOW           ALLOW             ALLOW
#: xxd -r in out       ALLOW           ALLOW             ALLOW
#: xmllint --output    ALLOW           ALLOW             ALLOW
#: control  tee        DENY            DENY              DENY   ✓
#: ```
#:
#: Revision 11 measured these only at `INSIDE_REPO`, where it argued the failure
#: direction is refusal, and carried them as declared debt. At a confined scope the
#: direction is ALLOW — so that debt row was a true sentence standing beside a hole,
#: which is the exact move revision 11 warned about and then made.
#:
#: The repair is the one this bridge already applies to `-m` modules: a program whose
#: write capability depends on its ARGV gets its argv DERIVED, and only a program with no
#: reachable write mode is exempt. Two sets, and the boundary between them is a claim
#: about each program rather than a convenience.
#:
#: 🔴 What is NOT claimed: that this membership is complete. A program's write mode is a
#: property of its CLI and is not derivable from command text — no rule can close this
#: family. What IS closed is the DEFAULT: anything outside both sets falls to
#: `UNDERIVED_OPERAND` and fails closed at every ungranted scope. The residual risk is
#: therefore bounded by `PURE_READERS` membership alone, and that set is deliberately
#: small, justified per line, and asserted by the family suite at all three confined
#: scopes.
PURE_READERS = frozenset({
    "cat", "bat", "head", "tail", "less", "more", "nl", "rev", "strings",
    "grep", "egrep", "fgrep", "rg", "ag", "ack", "ripgrep",
    "ls", "dir", "stat", "file", "du", "df", "wc", "basename", "dirname",
    "realpath", "readlink", "pwd", "which", "type", "command_not_found",
    "uniq", "cut", "paste", "join", "column", "fold", "expand", "unexpand",
    "tr", "comm", "diff", "diff3", "cmp", "colordiff", "delta", "od", "hexdump",
    "md5", "md5sum", "shasum", "sha1sum", "sha256sum", "sha512sum", "cksum", "b2sum",
    "echo", "printf", "true", "false", "date", "seq", "yes", "sleep",
    # 🔴 The shell TEST builtin, whose name really is a bracket. Without it,
    # `printf "%s\n" "$([ 1 = 1 ] && echo "A -> B")"` — a committed negative control —
    # reads `[` as a program produced by a glob and refuses ordinary work. Found by
    # running this repository's own control set, not by reading the pattern.
    "[", "[[", "test",
    "csvlook", "wdiff", "glow", "man", "info", "whatis", "apropos",
})

#: Programs that READ by default and WRITE under a specific argv. Each entry derives its
#: own targets; an empty derivation means this invocation reads, and the program stays
#: allowed. Same contract as `MODULE_WRITE_MODEL`, one layer out.
#:
#: Every member below was moved OUT of the revision-11 reader set because Mirror
#: demonstrated it writing, or because its own manual documents a write mode.


def _model_sort(argv: Sequence[str]) -> List[str]:
    """`sort -o FILE` writes FILE. Verified truncating a file to zero bytes."""
    into = flag_value(argv, "-o", "--output")
    return [into] if into else []


def _model_xxd(argv: Sequence[str]) -> List[str]:
    """`xxd [-r] INFILE OUTFILE` writes the SECOND operand."""
    positional = [t for t in argv[1:] if not t.startswith("-")]
    return positional[1:2]


def _model_flag_output(argv: Sequence[str]) -> List[str]:
    """`--output FILE` / `-o FILE` — xmllint, tree, pygmentize and their kin."""
    into = flag_value(argv, "--output", "-o")
    return [into] if into else []


def _model_in_place(argv: Sequence[str]) -> List[str]:
    """`yq -i` / `jq -i` rewrite every operand they are given."""
    if not has_flag(argv, "-i", "--in-place"):
        return []
    return [t for t in argv[1:] if not t.startswith("-")][1:] or [UNNAMED]


#: `w FILE` as a sed command, and the `w` flag on a substitution. Both write.
SED_WRITE = re.compile(r"(?:^|[;\n])\s*\d*\s*w\s+(\S+)|s/(?:[^/\\]|\\.)*/(?:[^/\\]|\\.)*/[a-z]*w\s+(\S+)")


def _model_sed(argv: Sequence[str]) -> List[str]:
    """A `w` command inside a sed script names a file sed writes.

    The `-i` form is caught by its own branch above; this is the OTHER write mode, which
    revision 11 did not derive at all.
    """
    out: List[str] = []
    for token in argv[1:]:
        if token.startswith("-"):
            continue
        for match in SED_WRITE.finditer(token):
            out.extend(g for g in match.groups() if g)
    return out


#: `print > "file"` / `printf … >> "file"` inside an awk program.
AWK_WRITE = re.compile(r">>?\s*\"([^\"]+)\"|>>?\s*'([^']+)'")


def _model_awk(argv: Sequence[str]) -> List[str]:
    """A redirection inside an awk PROGRAM writes the file it names."""
    out: List[str] = []
    for token in argv[1:]:
        if token.startswith("-"):
            continue
        for match in AWK_WRITE.finditer(token):
            out.extend(g for g in match.groups() if g)
    return out


def _model_git_lfs(argv: Sequence[str]) -> List[str]:
    """`git-lfs install` writes hooks into the shared `.git`."""
    verb = next((t for t in argv[1:] if not t.startswith("-")), "")
    return [UNNAMED] if verb in ("install", "uninstall") else []


READER_WRITE_MODEL = {
    "sort": _model_sort,
    "xxd": _model_xxd,
    "xmllint": _model_flag_output,
    "tree": _model_flag_output,
    "pygmentize": _model_flag_output,
    "yq": _model_in_place,
    "jq": _model_in_place,
    "sed": _model_sed,
    "gsed": _model_sed,
    "awk": _model_awk,
    "gawk": _model_awk,
    "mawk": _model_awk,
    "nawk": _model_awk,
    "git-lfs": _model_git_lfs,
}

#: Kept as the union so existing call sites and tests keep one name for "does not need
#: an UNDERIVED_OPERAND finding on its own account".
KNOWN_READERS = PURE_READERS | frozenset(READER_WRITE_MODEL)

#: A program name this guard can classify at all. `{}`, `$CMD` and a leftover
#: substitution marker are not names — they are a program the command does not state.
#:
#: 🔴 `~` is deliberately absent: `~/bin/tool` is an ordinary invocation of a named
#: program, and reading a home-relative path as an unstateable program would refuse it.
OPAQUE_PROGRAM_NAME = re.compile(r"[$`*?\[\]{}]|\x00")

#: Every bare program name any table in this module is keyed on — revision 12.
#:
#: `normalise_program` collapses a version suffix ONLY onto a member of this set, so
#: `python3.12` becomes `python3` while `report2` stays `report2`. Derived from the
#: tables rather than spelled again: a name added to a table below is covered without
#: anybody remembering to add it here, and `test_guard_families_rev12.py` asserts the
#: derivation is non-empty so an empty set cannot silently disable normalisation.
_KNOWN_PROGRAM_NAMES = frozenset(
    set(SHELL_BINARIES)
    | set(INTERPRETERS)
    | set(TRANSPARENT_WRAPPERS)
    | set(POSITIONAL_WRAPPERS)
    | set(STDIN_FED_WRAPPERS)
    | set(DELEGATING_BINARIES)
    | set(BATCH_EDITORS)
    | set(IN_PLACE_PROGRAMS)
    | set(SPLITTERS)
    | set(PACKAGE_MANAGERS)
    | set(KNOWN_READERS)
    | {"git", "patch", "apply_patch", "applypatch", "find", "dd", "eval", "env",
       "chmod", "chown", "chgrp", "chflags", "xattr", "setfacl",
       "touch", "mkdir", "mktemp", "curl", "wget", "wget2", "aria2c", "http", "https",
       "scp", "sftp", "ftp", "rclone", "tar", "gtar", "bsdtar", "unzip", "7z", "7za",
       "unrar", "gunzip", "bunzip2", "unxz", "zstd", "sed", "gsed", "node", "python",
       "perl", "ruby", "bash", "sh"}
)


# ── write primitives, by argv[0] ───────────────────────────────────────────────────

#: Commands whose non-option operands are all written to.
WRITES_ALL_OPERANDS = frozenset({"tee", "truncate", "shred", "unlink", "mkfifo"})
#: Commands that read every operand but the last and write the last.
#: 🔴 `ditto` added in revision 12, and it is a CORRECTION TO MIRROR as well as a repair.
#: Mirror listed `ditto` among the exec-wrappers of D2, "verified to execute a command in
#: cwd". Its manual says otherwise — `ditto [options] src ... dst_directory` copies — so
#: it executes nothing and the wrapper classification is wrong. It IS an unmodelled
#: WRITER of its last operand, which is a real defect of the other kind, and that is what
#: this entry repairs.
WRITES_LAST_OPERAND = frozenset({"cp", "mv", "install", "rsync", "ln", "ditto"})
#: Commands that destroy every operand.
DESTROYS_OPERANDS = frozenset({"rm", "rmdir", "srm"})

OPTIONS_WITH_VALUE = {
    "truncate": frozenset({"-s", "--size", "-r", "--reference"}),
    "cp": frozenset({"-t", "--target-directory", "-S", "--suffix"}),
    "mv": frozenset({"-t", "--target-directory", "-S", "--suffix"}),
    "install": frozenset({"-m", "--mode", "-o", "--owner", "-g", "--group", "-t"}),
    "rsync": frozenset({"-e", "--rsh", "--exclude", "--include", "--files-from"}),
    "sed": frozenset({"-e", "--expression", "-f", "--file", "-l"}),
    "perl": frozenset({"-e", "-E", "-I", "-m", "-M"}),
    "tee": frozenset({}),
    # Added in revision 8, with the families they belong to. An option-value that is not
    # listed here arrives in `operands()` as if it were a path, which is how `chmod 755`
    # reported a mode as a write target.
    "ln": frozenset({"-S", "--suffix", "-t", "--target-directory"}),
    "touch": frozenset({"-r", "--reference", "-t", "-d", "--date"}),
    "mkdir": frozenset({"-m", "--mode"}),
    "chmod": frozenset({"--reference"}),
    "chown": frozenset({"--reference", "--from"}),
    "chgrp": frozenset({"--reference"}),
    "curl": frozenset({"-o", "--output", "-T", "--upload-file", "-d", "--data", "-H",
                       "--header", "-X", "--request", "-u", "--user", "-F", "--form",
                       "-A", "--user-agent", "-b", "--cookie", "-c", "--cookie-jar",
                       "-e", "--referer", "-m", "--max-time", "--data-binary",
                       "--data-raw", "-w", "--write-out", "-K", "--config"}),
    "wget": frozenset({"-O", "--output-document", "-P", "--directory-prefix",
                       "-o", "--output-file", "-U", "--user-agent", "-T", "--timeout",
                       "--header", "--post-data", "--post-file", "-i", "--input-file"}),
    "tar": frozenset({"-f", "--file", "-C", "--directory", "-T", "--files-from",
                      "--exclude", "--transform", "--strip-components"}),
    "unzip": frozenset({"-d", "-x", "-P"}),
    "7z": frozenset({"-o", "-p", "-x"}),
    "rm": frozenset({}),
    "git": frozenset({"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path"}),
    # 🔴 Revision 11. Without this, `git config -f /tmp/x.cfg a b` read `/tmp/x.cfg` as
    # the KEY and `a` as the value — the option/operand family inside git's own porcelain.
    "config": frozenset({"-f", "--file", "--type", "--default", "--blob"}),
    # 🔴 Added in revision 9. Without these, `split -l 5 /tmp/a framework/part-` had `5`
    # read as an operand, which pushed the real prefix out of the position the rule looked
    # at and left the command ALLOWED. An option-value not listed here arrives in
    # `operands()` as if it were a path — the same defect that reported a chmod mode as a
    # write target, one family further on.
    "split": frozenset({"-a", "--suffix-length", "-b", "--bytes", "-C", "--line-bytes",
                        "-l", "--lines", "-n", "--number", "--additional-suffix",
                        "--filter", "-d", "--numeric-suffixes"}),
    "csplit": frozenset({"-f", "--prefix", "-b", "--suffix-format", "-n", "--digits"}),
    # 🔴 Revision 11. Without this, `patch -p1 -i /tmp/p.diff` read the DIFF as the file
    # being written — an external input reported as the destination, in the direction
    # that allows. See the `patch` branch in `analyse_argv`.
    "patch": frozenset({"-i", "--input", "-o", "--output", "-d", "--directory",
                        "-p", "--strip", "-B", "--prefix", "-r", "--reject-file",
                        "-D", "--ifdef", "-F", "--fuzz", "-V", "--version-control",
                        "-b", "--suffix", "-z", "-g", "--get", "--basename-prefix"}),
    "awk": frozenset({"-v", "-f", "--file", "--source", "-i"}),
    "gawk": frozenset({"-v", "-f", "--file", "--source", "-i", "--include", "--load"}),
    "ed": frozenset({"-p", "--prompt"}),
    "ex": frozenset({"-c", "--cmd", "-u", "-s"}),
    "vim": frozenset({"-c", "--cmd", "-u", "-U", "-i", "-s", "-w", "-W", "-T"}),
    "nvim": frozenset({"-c", "--cmd", "-u", "-i", "-s", "-w", "-W"}),
    "npm": frozenset({"--prefix", "--registry", "--userconfig", "--globalconfig",
                      "-w", "--workspace", "--cache"}),
    "pip": frozenset({"-t", "--target", "--prefix", "--root", "-r", "--requirement",
                      "-i", "--index-url", "--cache-dir", "--find-links", "-c",
                      "--constraint"}),
    "pip3": frozenset({"-t", "--target", "--prefix", "--root", "-r", "--requirement",
                       "-i", "--index-url", "--cache-dir", "--find-links", "-c",
                       "--constraint"}),
}

#: Python/Perl/Ruby/Node source that opens a file for writing. Applied ONLY to a program
#: body already established as such — an inline `-c`/`-e` script or a heredoc fed to an
#: interpreter — never to arbitrary command text.
PROGRAM_WRITES = re.compile(
    r"""\.write_text\s*\(
      | \.write_bytes\s*\(
      | \bopen\s*\([^)]*['"][wax]b?\+?['"]
      | \bopen\s*\([^)]*['"]\s*>            # perl: open(F, '>', $path) / open(F, ">$path")
      | \bjson\.dump\s*\(
      | \bshutil\.(?:copy|move|copyfile|copy2|rmtree)\s*\(
      | \bos\.(?:replace|rename|remove|unlink|rmdir|truncate)\s*\(
      | \bPath\s*\([^)]*\)\s*\.\s*(?:write|unlink|rename|replace|mkdir|touch)
      | \bfs\.(?:write|append|unlink|rename|copy|rm)
      | \bwriteFileSync\b | \bcreateWriteStream\b
      | \bFile\.(?:write|open|delete|rename)\b
      | \bopen\s*\(\s*[A-Za-z_$][\w$]*\s*,\s*['"][wax]
      | >\s*\$?\w                      # a shell redirect inside an interpreted body
    """,
    re.VERBOSE,
)
#: String literals inside a program body, used to name that body's write targets.
PROGRAM_STRING = re.compile(r"""['"]([^'"\n]{1,300})['"]""")

#: A program body that shells out. Its ARGUMENT is a command and is judged as one.
#:
#: 🔴 `\bsubprocess\.` used to sit in `PROGRAM_WRITES`, treating every shell-out as a write.
#: That denied `python3 - <<PY … subprocess.run([sys.executable, "framework/scripts/x.py"]) … PY`
#: — invoking a committed script by name, which is the escape hatch every denial message
#: offers. A rule that forbids the alternative it recommends is not a rule an actor can
#: follow. Analysing the argument instead is both more permissive HERE and stricter where it
#: matters: `subprocess.run(["rm", "-rf", "framework"])` is now read as `rm -rf framework`.
SHELL_OUT = re.compile(
    r"\b(?:subprocess\.(?:run|call|check_call|check_output|Popen)|os\.(?:system|popen)"
    r"|commands\.getoutput|child_process\.(?:exec|execSync|spawn|spawnSync))\s*\(")

#: `*** Update File: path` — the apply_patch envelope names its own targets.
PATCH_TARGET = re.compile(r"^\*\*\*\s+(?:Add|Update|Delete)\s+File:\s*(.+?)\s*$", re.MULTILINE)
#: `+++ b/path` — a unified diff names its targets too, and `git apply` reads them.
DIFF_TARGET = re.compile(r"^\+\+\+\s+(?:b/)?(\S+)\s*$", re.MULTILINE)


# ── target classification ──────────────────────────────────────────────────────────

SCRATCH_PREFIXES = ("/tmp/", "/private/tmp/", "/var/tmp/", "/var/folders/", "/dev/")
SCRATCH_EXACT = frozenset({"/tmp", "/private/tmp", "/var/tmp", "/dev/null", "/dev/stdout",
                           "/dev/stderr", "-"})
SCRATCH_SEGMENT = "scratchpad"

EXPANDS = re.compile(r"[$`*?\[\]~{}]|\x00")

INSIDE_REPO = "INSIDE_REPO"
OUTSIDE_REPO = "OUTSIDE_REPO"
SCRATCH = "SCRATCH"
PEER_WORKTREE = "PEER_WORKTREE"
SHARED_CHECKOUT = "SHARED_CHECKOUT"
GIT_COMMON_DIR = "GIT_COMMON_DIR"
RUNTIME_CONFIG = "RUNTIME_CONFIG"

#: `repo_topology`'s vocabulary onto this module's. Only the three confined scopes are
#: new; the rest already had names here.
_FROM_TOPOLOGY = {
    rt.ASSIGNED_WORKTREE: INSIDE_REPO,
    rt.PEER_WORKTREE: PEER_WORKTREE,
    rt.SHARED_CHECKOUT: SHARED_CHECKOUT,
    rt.GIT_COMMON_DIR: GIT_COMMON_DIR,
    rt.EXTERNAL_SCRATCH: SCRATCH,
    rt.EXTERNAL_OTHER: OUTSIDE_REPO,
    rt.UNDERIVABLE: UNDERIVABLE,
}

#: The four scopes the SESSION topology owns. A path that lands in one of them is
#: answered by the topology and by nothing after it.
_REPOSITORY_SCOPES = (rt.ASSIGNED_WORKTREE, rt.PEER_WORKTREE,
                      rt.SHARED_CHECKOUT, rt.GIT_COMMON_DIR)


class _AskSession:
    """The default value of `assigned`: *go and derive it from the session binding*.

    🔴 A sentinel rather than `None`, because `None` has to keep meaning *there is no
    assignment* — the state in which every repository-space mutation is refused. A
    single value for "not supplied" and "supplied as nothing" would make the fail-closed
    branch unreachable from a test, which is how a fail-closed branch stops being one.
    """

    __slots__ = ()

    def __repr__(self) -> str:  # pragma: no cover - diagnostics only
        return "ASK_SESSION"


ASK_SESSION = _AskSession()


def session_topology(assigned: object = ASK_SESSION) -> Optional[rt.Topology]:
    """The repository as seen from the ASSIGNED worktree, or None when there is none.

    🔴 This is the whole revision-10 repair in one function, and the thing it must never
    do is fall back to `rt.of(cwd)`. `cwd` here is the effective workdir, the model
    writes it, and deriving the assignment from it is what let a peer worktree be staged
    and committed at ordinary `SHELL_DEFAULT`. `None` means the perimeter is
    `UNDERIVABLE`, and `UNDERIVABLE` denies.
    """
    if isinstance(assigned, _AskSession):
        assigned = sb.cached().worktree
    if not assigned or not isinstance(assigned, str):
        return None
    topology = rt.cached_for(assigned)
    return topology if topology.ok else None


def classify_target(token: str, cwd: Optional[str], repo_root: Optional[str],
                    assigned: object = ASK_SESSION) -> str:
    """Where does this operand point? `UNDERIVABLE` when the answer needs a shell.

    Two different directories decide two different things, and revision 9 used one for
    both:

    ```text
    cwd       EFFECTIVE_WORKDIR — model-selected. Anchors a RELATIVE operand, and
              nothing else. `pre_tool_use_guard.derive_workdir` establishes it.
    assigned  SESSION_ASSIGNED_WORKTREE — session-bound. Decides which subdivision of
              the repository is this actor's, and therefore what the authority table is
              consulted about. `session_binding.derive` establishes it.
    ```

    🔴 Collapsing them is Mirror's REV9 finding. With the assignment read out of `cwd`,
    `workdir=<PEER_WORKTREE> git add framework/probe.md` made the peer the assignment,
    so the target was `INSIDE_REPO`, so `SHELL_DEFAULT`'s named-staging grant applied —
    while the identical `git -C <PEER_WORKTREE> …` was refused. Rotating the frame did
    not defeat the authority table; it removed the target from the class the table
    refuses, before the table was ever asked.
    """
    if token == UNNAMED:
        return UNNAMED
    if token == OPAQUE or not token:
        return UNDERIVABLE
    if EXPANDS.search(token):
        return _classify_by_prefix(token, cwd, repo_root, assigned)
    if token in SCRATCH_EXACT:
        return SCRATCH

    path = token if posixpath.isabs(token) else posixpath.join(cwd or "", token)
    path = posixpath.normpath(path)
    topology = session_topology(assigned)
    unbound = topology is None

    # 🔴 The repository is the set of worktrees sharing one object store, and asking
    # only "is this under my toplevel?" answered NO for every peer worktree, for the
    # shared checkout and for `.git` itself. The topology is consulted FIRST, before the
    # scratch prefixes and before the root comparison, because a peer worktree living
    # under `/var/folders` is still a peer worktree — the same ordering mistake, one
    # level out, that revision 8 fixed for the assigned worktree.
    #
    # 🔴 ASSIGNED_WORKTREE is taken from the topology too, and that is a REPAIR and not
    # tidiness. The prefix comparison below is lexical, and on macOS `git rev-parse
    # --show-toplevel` answers `/private/var/folders/...` while the cwd a runtime sends
    # is `/var/folders/...` — the same directory through the `/private` symlink. The
    # comparison failed, the path fell through to the scratch prefixes, and a fixture
    # repository under TMPDIR was writable. Revision 8 believed it had closed exactly
    # this case; it closed the spelling where the two agree. Found by running the
    # committed corpus against BOTH engines, which is what the corpus is for.
    if posixpath.isabs(path):
        if topology is not None:
            placed = topology.classify(path)
            if placed in _REPOSITORY_SCOPES:
                # The session's own repository. Nothing after this can widen it, and
                # nothing after this needs to: every worktree of it is covered here,
                # whatever directory the command runs in.
                return _FROM_TOPOLOGY[placed]

        # 🔴 The runtime's own registration, checked AFTER the repository and before
        # everything else. After, because a control file inside the assigned worktree
        # already has a governance surface — a shell write to it is refused, and the
        # only route in is Write/Edit plus a named `git add` plus a commit, which is a
        # review. Before everything else, because outside the repository there is no
        # such surface at all, and `~/.claude/settings.json` is where the hook that
        # enforces this policy is named.
        if rc.cached().contains(path):
            return RUNTIME_CONFIG

        # 🔴 No assignment, no perimeter. Scratch survives — it is a property of the
        # path rather than of the repository — and everything else is UNDERIVABLE,
        # which denies every mutation and no read. Falling back to the effective
        # workdir here is precisely the defect this parameter exists to remove.
        outside = (SCRATCH if _is_scratch_path(path) else UNDERIVABLE) if unbound \
            else _FROM_TOPOLOGY[topology.classify(path)]
        return _stricter(outside, _workdir_repository_overlay(path, repo_root, unbound))

    # A path that is still relative here had no `cwd` to anchor it.
    if repo_root is not None:
        root = posixpath.normpath(repo_root)
        if path == root or path.startswith(root.rstrip("/") + "/"):
            return INSIDE_REPO
    if _is_scratch_path(path):
        return SCRATCH
    if repo_root is None:
        # 🔴 Without a root, "outside the repository" is not derivable, and guessing
        # outward is guessing in the unsafe direction. Everything non-scratch is treated
        # as repository space.
        return INSIDE_REPO
    return OUTSIDE_REPO


#: How much a wrong ALLOW would cost, per scope. Used ONLY to combine two readings of
#: one path, never to decide anything on its own — `repo_topology.STRICTNESS` is the same
#: idea over that module's vocabulary, and `test_pre_tool_use_guard.py` asserts every
#: scope appears here so one added later cannot default to zero.
_STRICTNESS = {
    SCRATCH: 0, OUTSIDE_REPO: 1, INSIDE_REPO: 2, PEER_WORKTREE: 3,
    SHARED_CHECKOUT: 4, GIT_COMMON_DIR: 5, RUNTIME_CONFIG: 6, UNDERIVABLE: 7,
}


def _stricter(left: str, right: str) -> str:
    return left if _STRICTNESS.get(left, 7) >= _STRICTNESS.get(right, 7) else right


def _workdir_repository_overlay(path: str, repo_root: Optional[str],
                                unbound: bool) -> str:
    """A STRICTNESS-ONLY reading of *is this path inside the effective workdir's own
    working tree*, for a path outside the session's repository entirely.

    🔴 It can only ever raise strictness, never lower it, and that is what makes it safe
    to derive from `repo_root` — which comes from the effective workdir, which the model
    writes. A rotation into a peer still classifies `PEER_WORKTREE` (stricter than
    `INSIDE_REPO`) and still denies; the overlay cannot demote it, because the caller
    takes the maximum.

    Why it exists: revision 9 derived the whole topology from the effective workdir, and
    so happened to protect an UNRELATED repository the actor had cd'd into — case
    `K1-repo-under-tmp`, a working tree under `TMPDIR`. Pinning the assignment took that
    away as a side effect, and the corpus caught it as a 🔴 regression on the first run
    after the repair. Restoring it as a strictness-only overlay keeps both properties
    instead of trading one for the other.

    Both spellings are compared. `git rev-parse --show-toplevel` answers
    `/private/var/folders/…` on macOS while a runtime's `cwd` is `/var/folders/…`, and a
    lexical comparison between them is exactly the K1 defect that revision 9's topology
    was hiding.

    🔴 When the session is UNBOUND the overlay is `UNDERIVABLE`, not `INSIDE_REPO`. With
    no assignment, "inside the effective workdir's repository" does not say WHICH
    repository — and `INSIDE_REPO` is a GRANT for `STAGE` and `COMMIT`. An unbound
    session committing into a working tree under `TMPDIR` was the second finding of that
    same corpus run: `SCRATCH` was rewritten to `INSIDE_REPO` by the index rule, and
    `SHELL_DEFAULT` grants a commit there.
    """
    if repo_root is None:
        return SCRATCH  # the weakest value: contributes nothing to the maximum
    root = posixpath.normpath(repo_root)
    inside = _under(root, path) or _under(rt.realpath(root), rt.realpath(path))
    if not inside:
        return SCRATCH
    return UNDERIVABLE if unbound else INSIDE_REPO


def _under(directory: str, path: str) -> bool:
    directory = directory.rstrip("/")
    return bool(directory) and (path == directory or path.startswith(directory + "/"))


def _is_scratch_path(path: str) -> bool:
    """Scratch by the shape of the path alone, in both macOS spellings.

    Factored out because revision 10 needs the same answer on a branch that has no
    topology to consult, and a second inline copy of a prefix list is the shape that
    drifts. Both tuples are consulted: `repo_topology`'s carries `/private/var/tmp/` and
    `/private/var/folders/`, which this module's does not, and taking the union means a
    resolved `/private` spelling is scratch under both readings rather than under
    whichever list the caller happened to reach.
    """
    if SCRATCH_SEGMENT in path.split("/"):
        return True
    if path in SCRATCH_EXACT or path in rt.SCRATCH_EXACT:
        return True
    return path.startswith(SCRATCH_PREFIXES) or path.startswith(rt.SCRATCH_PREFIXES)


def _classify_by_prefix(token: str, cwd: Optional[str], repo_root: Optional[str],
                        assigned: object = ASK_SESSION) -> str:
    """A path whose FILENAME expands but whose directory does not.

    `SC=/tmp/work; git show "$rev":x > "$SC/out/gp_$rev.py"` is a scratch write, and calling
    it `UNDERIVABLE` denies one of the most ordinary shapes an agent types — a loop writing
    one file per iteration into a directory it just named. That is the failure mode this
    policy's own docstring warns about: a guard that blocks ordinary work gets turned off.

    So the *resolvable prefix* decides, under three conditions that keep it honest:

      - every segment before the last must be free of expansion, so the DIRECTORY is known;
      - the expansion may appear only in the final segment, so it cannot walk elsewhere;
      - no segment may be `..`, so the known prefix cannot be escaped literally.

    🔴 This is a deliberate narrowing of fail-closed, and it is not airtight: a variable
    whose *value* begins `../` still escapes a scratch prefix. It is accepted because the
    threat this policy names is an actor clobbering repository files it has not read, not an
    adversary choosing a value to defeat the guard — and because a prefix inside the
    repository still denies, which is the direction that matters.
    """
    segments_ = token.split("/")
    if any(part == ".." for part in segments_):
        return UNDERIVABLE
    if any(EXPANDS.search(part) for part in segments_[:-1]):
        return UNDERIVABLE
    prefix = "/".join(segments_[:-1])
    if not prefix:
        # A bare expanding filename in the current directory.
        return classify_target(".", cwd, repo_root, assigned)
    where = classify_target(prefix, cwd, repo_root, assigned)
    # The confined scopes propagate rather than collapsing to UNDERIVABLE. Both refuse,
    # so the outcome is the same; only the SENTENCE differs, and `<peer>/out_$n.md`
    # deserves the denial that says which peer rather than the one that says the guard
    # could not resolve a glob.
    if where in (SCRATCH, INSIDE_REPO, PEER_WORKTREE, SHARED_CHECKOUT, GIT_COMMON_DIR,
                 RUNTIME_CONFIG):
        return where
    return UNDERIVABLE


# ── lexing ─────────────────────────────────────────────────────────────────────────

HEREDOC_START = re.compile(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")

#: A file-descriptor **duplication**: `2>&1`, `>&2`, `1<&0`. It names no path, so there
#: is nothing to police and deleting it keeps it out of the argv.
#:
#: 🔴 The digits must begin a token. `echo hi2>/tmp/f` writes "hi2" to the file — bash
#: binds the `2` to the WORD, verified against bash itself on 2026-08-29 — and revision
#: 7's unanchored `\d+>` ate it, turning `--tip <any tip ≥ e839db38>` into
#: `--tip < any tip ≥ e839db >`. That is how two documented lines in this repository
#: passed the guard: the same expression that hid `1>` also swallowed the `38` and the
#: `>` with it. The lookbehind is negative-for-a-non-separator so it also holds at
#: position 0, where a lookbehind for a separator would fail.
_FD_START = r"(?<![^\s;&|()])"
FD_DUP = re.compile(_FD_START + r"\d*>&\d*|" + _FD_START + r"\d*<&\d*")
#: A file-descriptor **redirection that takes a path**: `1> f`, `2>> f`, `&> f`, `&>> f`.
#:
#: 🔴 These used to be deleted by the same expression that deletes a duplication, and
#: that was a bypass of this policy's own redirection rule by one character.
#: `echo x 1> framework/scripts/guard_policy.py` had the `1>` erased before lexing, so
#: the target arrived as a harmless argument to `echo` and the command was ALLOWED —
#: while `echo x > …`, which does exactly the same thing, was denied. Measured on
#: revision 7 on 2026-08-29, together with `2>`, `1>>`, `&>` and `exec 3>`.
#:
#: They are now rewritten to the plain form the segmenter already understands, rather
#: than deleted. Dups are stripped FIRST, so `2>&1` never reaches this pattern.
FD_WRITE = re.compile(r"&>>|&>|" + _FD_START + r"\d+>>|" + _FD_START + r"\d+>")
SUBSTITUTION = re.compile(r"\$\(|\`|<\(|>\(")


class Unparseable(Exception):
    """The command could not be read as a command. Undecidable, therefore denied."""


def extract_heredocs(command: str) -> Tuple[str, List[str]]:
    """Strip heredoc bodies out of the command text and return them separately.

    A heredoc body is program text, not command text: lexing it as a command produces
    nonsense, and leaving it in place makes every quote in it a lexing hazard.

    🔴 **The OPERATOR is removed too, and for revisions 1–10 it was not.** This is the
    root cause of the stdin-program family, and it is not a missing spelling. The body
    was lifted out and `<<` and its delimiter were left behind as argv residue:

    ```text
    python3 - <<'PY'   heredocs=1  argv ['python3','-','<<','PY']  "-" found  → DENY
    python3   <<'PY'   heredocs=1  argv ['python3','<<','PY']      len 3      → ALLOW
    cat <<'PY' | python3            argv ['python3']               len 1      → DENY
    ```

    `analyse_interpreter`'s `len(argv) == 1` clause is written for exactly the bare form
    and could never hold while the residue was there — while the same body arriving
    through a PIPE, where the interpreter's argv really is `['python3']`, was refused.
    The clause was correct; its own preprocessing removed the condition it depends on.
    Measured at `e01d6d2` over 4 interpreters × 4 forms: 12 of 16 cells open, with
    `cat <<EOF | <interp>` and `<interp> -c <body>` denying for all four.

    So the residue is deleted rather than the downstream clause being widened, and the
    invariant that says so is executable:

    > `cat <<EOF | python3` and `python3 <<EOF` MUST receive the same verdict.
    """
    bodies: List[str] = []
    lines = command.split("\n")
    out: List[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        starts = HEREDOC_START.findall(line)
        # 🔴 The operator and its delimiter leave the command text with the body.
        out.append(HEREDOC_START.sub(" ", line) if starts else line)
        index += 1
        for _, delimiter in starts:
            body: List[str] = []
            while index < len(lines) and lines[index].strip() != delimiter:
                body.append(lines[index])
                index += 1
            index += 1  # consume the terminator
            bodies.append("\n".join(body))
    return "\n".join(out), bodies


def extract_herestrings(command: str) -> Tuple[str, List[str]]:
    """Lift `<<< word` bodies out of the command text, operator and word together.

    🔴 The second cause of the stdin-program family, and it fails a step EARLIER than
    the heredoc residue: `extract_heredocs` returns no body at all for `<<<`, so there
    was never anything to attribute. Repairing only the residue closes the eight heredoc
    cells and none of the four herestring cells.

    One precision, because it misleads whoever repairs this by pattern: `HEREDOC_START`
    *does* reach inside `<<<` — at an offset, reading a bare word as a quoted delimiter —
    and registers a PHANTOM heredoc with an EMPTY body. That phantom is inert only
    because `PROGRAM_WRITES.search("")` is `None`. "Make the pattern match `<<<`" is
    therefore not the repair: the herestring needs a body extractor of its own, and it
    must run BEFORE `extract_heredocs` so the phantom never forms.

    Quote state is tracked because `echo "a <<< b"` is an argument, not a redirection —
    the same rule `extract_substitutions` applies, and for the same reason.
    """
    bodies: List[str] = []
    out: List[str] = []
    i, n = 0, len(command)
    quote = ""
    while i < n:
        char = command[i]
        if quote:
            out.append(char)
            if char == "\\" and quote == '"' and i + 1 < n:
                out.append(command[i + 1])
                i += 2
                continue
            if char == quote:
                quote = ""
            i += 1
            continue
        if char in "'\"":
            quote = char
            out.append(char)
            i += 1
            continue
        if command.startswith("<<<", i):
            j = i + 3
            while j < n and command[j] in " \t":
                j += 1
            word, j = _read_word(command, j)
            bodies.append(word)
            out.append(" ")
            i = j
            continue
        out.append(char)
        i += 1
    return "".join(out), bodies


def _read_word(text: str, start: int) -> Tuple[str, int]:
    """One shell word from `start`, quotes honoured, returning (content, end).

    The content is the word with its outer quoting removed, because that is what the
    interpreter receives on stdin — `python3 <<< "open('x','w')"` feeds the interpreter
    the inside of the double quotes, and judging the quotes as part of the program is how
    a body stops matching `PROGRAM_WRITES`.
    """
    out: List[str] = []
    i, n = start, len(text)
    quote = ""
    while i < n:
        char = text[i]
        if quote:
            if char == "\\" and quote == '"' and i + 1 < n:
                out.append(text[i + 1])
                i += 2
                continue
            if char == quote:
                quote = ""
                i += 1
                continue
            out.append(char)
            i += 1
            continue
        if char in "'\"":
            quote = char
            i += 1
            continue
        if char in " \t\n;&|()<>":
            break
        if char == "\\" and i + 1 < n:
            out.append(text[i + 1])
            i += 2
            continue
        out.append(char)
        i += 1
    return "".join(out), i


def extract_substitutions(command: str) -> Tuple[str, List[str]]:
    """Replace `$(…)`, `` `…` ``, `<(…)` and `>(…)` with an opaque token.

    The bodies are returned so they can be analysed as commands in their own right — a
    substitution is a place a command hides, and `echo $(git add -A)` must not be read as
    a harmless `echo`.

    🔴 **A substitution inside DOUBLE quotes is still a substitution.** The shell expands
    `"$(…)"` and `` "`…`" `` and leaves `'$(…)'` alone, so only the single-quoted case is
    inert. Skipping both — which this function did — was a bypass, not a nicety:
    `echo "$(git add -A)"` runs blanket staging and was `ALLOWED`. It was found by the
    guard refusing an unrelated diagnostic command of my own, whose `->` inside a quoted
    substitution fragmented under the lexer; the false positive and the bypass are the same
    defect seen from its two sides.
    """
    bodies: List[str] = []
    out: List[str] = []
    i = 0
    n = len(command)
    quote = ""
    while i < n:
        char = command[i]
        if quote == "'":
            # Single quotes are literal: nothing expands, so nothing is extracted.
            out.append(char)
            if char == "'":
                quote = ""
            i += 1
            continue
        if quote == '"':
            if char == "\\" and i + 1 < n:
                out.append(char)
                out.append(command[i + 1])
                i += 2
                continue
            if char == '"':
                quote = ""
                out.append(char)
                i += 1
                continue
            # fall through: `$(` and backticks below are live inside double quotes
        elif char == "'":
            quote = "'"
            out.append(char)
            i += 1
            continue
        elif char == '"':
            quote = '"'
            out.append(char)
            i += 1
            continue
        if char == "`":
            end = command.find("`", i + 1)
            if end == -1:
                raise Unparseable("an unterminated backtick substitution")
            bodies.append(command[i + 1 : end])
            out.append(OPAQUE)
            i = end + 1
            continue
        if command.startswith(("$(", "<(", ">("), i):
            depth = 0
            j = i + 1
            while j < n:
                if command[j] == "(":
                    depth += 1
                elif command[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j >= n:
                raise Unparseable("an unterminated command substitution")
            bodies.append(command[i + 2 : j])
            out.append(OPAQUE)
            i = j + 1
            continue
        out.append(char)
        i += 1
    if quote:
        raise Unparseable("an unterminated quoted string")
    return "".join(out), bodies


CONTROL_TOKENS = frozenset({";", "&&", "||", "|", "&", "|&", "(", ")", "{", "}", "\n"})
REDIRECT_WRITE = frozenset({">", ">>", ">|", "<>"})
REDIRECT_READ = frozenset({"<", "<<", "<<<"})


#: 🔴 A NEWLINE IS A COMMAND SEPARATOR, and for revisions 1–7 it was not.
#:
#: `CONTROL_TOKENS` has contained `"\n"` since revision 1, and the lexer below was
#: `shlex(punctuation_chars=True)` with `whitespace_split=True` — under which a newline
#: is *whitespace* and is never emitted as a token. So the entry was unreachable for
#: every real newline, and two lines were lexed into ONE argv. Only the first line's
#: program was ever analysed:
#:
#:     echo hi                                  ALLOWED   — measured 2026-08-29
#:     rm framework/scripts/guard_policy.py               on revision 7
#:
#:     echo hi                                  ALLOWED
#:     git add -A                                         the documented harm itself
#:
#: A multi-line block is the ordinary shape of agent shell use — every Bash call in the
#: session that found this was multi-line — so this is not an exotic bypass. It is the
#: default one. `;` split correctly, `|` split correctly, and a newline did not.
#:
#: The entry was not merely dead, either: it fired in exactly one case, a BACKSLASH
#: continuation, where the two lines are one command and must NOT be split. Hence the
#: substitution below runs first.
CONTINUATION = re.compile(r"\\\n")
NEWLINE_RUN = re.compile(r"\A\n+\Z")


def lex(command: str) -> List[str]:
    """Tokenise, with an unescaped newline emitted as its own separator token.

    `punctuation_chars` cannot be changed after construction and `whitespace` can, so
    the newline joins the punctuation set at construction and leaves the whitespace set
    afterwards. Quoting is unaffected: `'a\\nb'` and `"one\\ntwo"` stay single tokens,
    which `test_pre_tool_use_guard.py::ANewlineSeparatesCommands` pins in both
    directions.
    """
    lexer = shlex.shlex(command, posix=True, punctuation_chars="();<>|&\n")
    lexer.whitespace_split = True
    lexer.whitespace = " \t\r"
    try:
        return list(lexer)
    except ValueError as exc:
        raise Unparseable(f"the shell lexer refused it: {exc}") from exc


def segments(tokens: Sequence[str]) -> List[Tuple[List[str], List[str], bool]]:
    """Split a token stream into (argv, write-redirect-targets, fed-from-a-pipe) triples.

    The pipe flag is not decoration: `echo 'git add -A' | sh` runs a script this guard can
    read, and the only thing that distinguishes it from a harmless `sh` is that something
    upstream is writing to its stdin.
    """
    result: List[Tuple[List[str], List[str], bool]] = []
    argv: List[str] = []
    writes: List[str] = []
    pending_redirect = False
    pending_read = False
    piped_in = False
    next_piped = False
    for token in tokens:
        if pending_redirect:
            writes.append(token)
            pending_redirect = False
            continue
        # 🔴 A READ redirection's source is an INPUT, never an operand — revision 11.
        # Revisions 1–10 dropped the `<` and left the filename in the argv, so
        # `patch -p1 < /tmp/p.diff` derived a WRITE on the DIFF at `SCRATCH` and was
        # allowed. That is the option/operand confusion spelled with shell syntax, and
        # repairing only `-i` would have left it standing.
        if pending_read:
            pending_read = False
            continue
        if token in REDIRECT_WRITE:
            pending_redirect = True
            continue
        if token in REDIRECT_READ:
            pending_redirect = False
            pending_read = True
            continue
        if token in CONTROL_TOKENS or NEWLINE_RUN.match(token):
            if argv or writes:
                result.append((argv, writes, piped_in))
            argv, writes = [], []
            piped_in = next_piped = token in ("|", "|&")
            continue
        argv.append(token)
    if pending_redirect:
        writes.append(UNNAMED)
    if argv or writes:
        result.append((argv, writes, piped_in))
    return result


# ── argv analysis ──────────────────────────────────────────────────────────────────

def base(token: str) -> str:
    return posixpath.basename(token)


#: 🔴 A VERSION SUFFIX is not a different program — revision 12.
#:
#: Every table in this module is keyed on a bare name, and revision 11 handled the
#: DIRECTORY (`/usr/bin/python3` and `./python3` both resolve through `base()`) while
#: leaving the version. Measured against the revision-11 engine, all of these ALLOWED a
#: repository write through a heredoc, a `-c` body and a `-m` module:
#:
#: ```text
#: python3.12  python3.9  perl5.34  node20      ← a trailing version
#: nodejs                                        ← a distribution's alias
#: bash5  sh5.2                                  ← the same, for shells
#: control  /usr/bin/python3  ./python3  python3  DENY on all three ✓
#: ```
#:
#: That defeats the Family-II repair and the `-m` repair at once, and it is not a gap in
#: the interpreter LIST — the list is right and the KEY was wrong. So this is a
#: normalisation, applied everywhere a program name is derived, rather than fourteen more
#: entries: `python3.12` and `python3` are one program spelled two ways, and a table that
#: cannot say so will be defeated by the next release of anything.
_VERSION_SUFFIX = re.compile(r"^(.*?)-?[\d.]+$")

#: Distribution aliases, where the alternate name is NOT a version and cannot be derived.
#: This IS a list, and it is declared as one: an alias is a fact about a packaging
#: decision, not a property of the text.
PROGRAM_ALIASES = {
    "nodejs": "node",
    "python3m": "python3",
    "pypy": "python",
    "pypy3": "python3",
}


def normalise_program(token: str) -> str:
    """The program name every table in this module is keyed on.

    `basename` first — the directory was revision 11's repair — then the alias map, then
    the version suffix. Order matters: `nodejs` must alias before a suffix rule could see
    a trailing `s`, and `/usr/local/bin/python3.12` must lose its directory first.

    🔴 A name that normalises to nothing keeps its original: `3.12` alone is not
    `python`, and a rule that invented a program out of a version string would classify
    an operand as an interpreter.
    """
    name = posixpath.basename(token)
    if name in PROGRAM_ALIASES:
        return PROGRAM_ALIASES[name]
    if name in _KNOWN_PROGRAM_NAMES:
        return name
    # 🔴 LONGEST known prefix wins, not the first cut. A non-greedy strip turns
    # `python3.12` into `python`, which happens to classify the same here and is still
    # the wrong answer to report: `python3` is a name this policy knows and is one
    # character of information away. Peeling one trailing version character at a time and
    # stopping at the first KNOWN name keeps `python3.12 -> python3` and `perl5.34 ->
    # perl`, and leaves `report2` alone because no prefix of it is a program.
    candidate = name
    while _VERSION_SUFFIX.match(candidate):
        candidate = candidate[:-1]
        trimmed = candidate.rstrip("-.")
        if trimmed in PROGRAM_ALIASES:
            return PROGRAM_ALIASES[trimmed]
        if trimmed in _KNOWN_PROGRAM_NAMES:
            return trimmed
    return name


def operands(argv: Sequence[str], program: str) -> List[str]:
    """Non-option arguments, with option-values skipped for the programs that take them."""
    takes_value = OPTIONS_WITH_VALUE.get(program, frozenset())
    out: List[str] = []
    skip = False
    for token in argv[1:]:
        if skip:
            skip = False
            continue
        if token == "--":
            continue
        if token.startswith("-") and token != "-":
            if token in takes_value:
                skip = True
            continue
        out.append(token)
    return out


def chmod_operands(argv: Sequence[str]) -> Tuple[Optional[str], List[str]]:
    """`(mode, paths)` for a chmod invocation, with the mode LOCATED rather than counted.

    Revision 9 dropped every `-`-leading token as an option and then discarded the first
    survivor as the mode. Both halves are wrong for `chmod -x <path>`: the mode is
    dropped as an option, and then the path is discarded as the mode, leaving nothing —
    `UNNAMED`, which no authority grants. It failed closed and refused ordinary scratch
    work, which is the failure mode that gets a guard turned off.

    `--reference=<file>` supplies the mode instead, and then there is no mode operand at
    all; returning `None` for it is right, and the old positional rule would have eaten
    the path.
    """
    value_flags = OPTIONS_WITH_VALUE.get("chmod", frozenset())
    mode: Optional[str] = None
    paths: List[str] = []
    index = 1
    while index < len(argv):
        token = argv[index]
        index += 1
        if token == "--":
            continue
        if mode is None and CHMOD_MODE.match(token):
            mode = token
            continue
        if token.startswith("-") and token != "-":
            if token in value_flags:
                index += 1
            continue
        paths.append(token)
    return mode, paths


def launcher_key(argv: Sequence[str]) -> "Optional[Tuple[int, frozenset]]":
    """`(words consumed, that launcher's value flags)` when argv[0] starts a launcher.

    Two-word forms are tried first: `pnpm dlx` must not be read as bare `pnpm`, whose
    branch is about installing, and `npm exec` must not fall through to `npm install`'s.
    """
    program = normalise_program(argv[0]) if argv else ""
    if not program:
        return None
    if len(argv) > 1:
        two = (program, argv[1])
        if two in PACKAGE_LAUNCHERS:
            return 2, PACKAGE_LAUNCHERS[two]
    one = (program,)
    if one in PACKAGE_LAUNCHERS:
        return 1, PACKAGE_LAUNCHERS[one]
    return None


def launcher_child(argv: Sequence[str], words: int,
                   value_flags: Iterable[str]) -> Tuple[List[str], List[str]]:
    """`(child argv, inline shell strings)` after the launcher's own options.

    The child is everything from the first non-option operand onward — its own argv,
    untouched — because that is what the launcher will actually execute.
    """
    value_flags = frozenset(value_flags)
    rest = list(argv[words:])
    inline: List[str] = []
    index = 0
    while index < len(rest):
        token = rest[index]
        if token == "--":
            index += 1
            continue
        if token.startswith("-") and token != "-":
            if token in value_flags and index + 1 < len(rest):
                if token in LAUNCHER_COMMAND_FLAGS:
                    inline.append(rest[index + 1])
                index += 2
                continue
            index += 1
            continue
        return rest[index:], inline
    return [], inline


def has_flag(argv: Sequence[str], *names: str) -> bool:
    """True if any short flag letter or long option among `names` is present.

    `-pi` and `-i` and `--in-place` are the same instruction to `perl` and `sed`, and a
    guard that only knows the spelling it was shown is a guard with a spelling bypass.
    """
    for token in argv[1:]:
        if not token.startswith("-") or token == "-" or token == "--":
            continue
        if token.startswith("--"):
            if token.split("=")[0] in names:
                return True
            continue
        for name in names:
            if len(name) == 2 and name.startswith("-") and name[1] in token[1:]:
                return True
    return False


def flag_value(argv: Sequence[str], *names: str) -> Optional[str]:
    """The value of `-o VALUE`, `--output=VALUE` or `--output VALUE`, or None.

    🔴 This exists because of a bypass measured on revision 7: `cp -t framework/scripts
    /tmp/a /tmp/b` writes into `framework/scripts`, but `-t` is an option-with-value, so
    `operands()` skipped both the flag AND its value — and the destination the policy
    then reported was `/tmp/b`, a *source*. The command was ALLOWED. A destination that
    travels in a flag has to be read out of the flag; skipping it names a read as a
    write and calls the result derived. Same shape for `mv -t`, `install -t`,
    `curl -o`, `wget -O`, `wget -P`, `tar -C` and `unzip -d`.
    """
    index = 1
    while index < len(argv):
        token = argv[index]
        for name in names:
            if token == name and index + 1 < len(argv):
                return argv[index + 1]
            if name.startswith("--") and token.startswith(name + "="):
                return token[len(name) + 1:]
            # `-ofile`, `-Cdir` — a short flag with its value attached.
            if (len(name) == 2 and name.startswith("-") and not name.startswith("--")
                    and token.startswith(name) and len(token) > 2
                    and not token.startswith("--")):
                return token[2:]
        index += 1
    return None


def strip_wrapper_options(argv: Sequence[str], value_flags: Iterable[str],
                          assignments: bool = False) -> List[str]:
    """Drop a wrapper's OWN leading options and reach the child argv untouched.

    🔴 The child argv is returned verbatim, flags included. Filtering `-`-prefixed tokens
    out of the whole tail is what turned `nohup bash -c 'git add -A'` into `bash 'git add
    -A'` — a shell with no script flag, which this guard then had nothing to follow.
    """
    value_flags = frozenset(value_flags)
    rest = list(argv)
    while rest:
        token = rest[0]
        if assignments and "=" in token and not token.startswith("-"):
            rest.pop(0)
            continue
        if not token.startswith("-") or token == "-":
            break
        rest.pop(0)
        if token == "--":
            break
        if token.split("=")[0] in value_flags and "=" not in token and rest:
            rest.pop(0)
    return rest


def git_subcommand(argv: Sequence[str]) -> Tuple[str, List[str]]:
    """Skip git's global options — `-C <dir>`, `-c k=v` — to reach the subcommand."""
    index = 1
    value_options = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path"}
    while index < len(argv):
        token = argv[index]
        if token in value_options:
            index += 2
            continue
        if token.startswith("--") and "=" in token:
            index += 1
            continue
        if token.startswith("-"):
            index += 1
            continue
        return token, list(argv[index + 1 :])
    return "", []


#: Always blanket: they stage the whole tree no matter what else is on the line, and
#: `git add -A` is the documented harm this policy exists for.
BLANKET_ADD = frozenset({"-A", "--all", "--no-ignore-removal"})
#: Blanket ONLY without a path operand. `git add -u` stages every tracked modification;
#: `git add -u framework/scripts/` stages the ones under a path the author named, which is
#: what the rule asks for. Refusing the second would be the guard blocking the behaviour it
#: is trying to teach.
BLANKET_WITHOUT_PATH = frozenset({"-u", "--update"})


def analyse_argv(argv: List[str], redirect_targets: List[str], heredocs: List[str],
                 findings: List[Finding], depth: int, piped_in: bool = False) -> None:
    """Classify one simple command, recursing through every wrapper that carries one."""
    if depth > 8:
        findings.append(Finding("WRAPPER_DEPTH", " ".join(argv[:2]), [UNNAMED],
                                "nesting deeper than this guard will follow"))
        return

    for target in redirect_targets:
        findings.append(Finding("REDIRECTION", "> / >>", [target],
                                "shell redirection writes the file it names"))

    # 🔴 A leading `NAME=VALUE` is an assignment prefix, not the program. Two defects lived
    # here at once, found together: reading it AS the program made `FOO=1 git add -A`
    # allowed — a bypass anyone would find by accident — while a *pure* assignment whose
    # value came from a substitution, `a=$(git rev-parse HEAD)`, was denied as an opaque
    # program. Both are the same missing step. The substitution's body is analysed
    # separately either way, so nothing hides inside the value.
    # 🔴 The prefixes are ANALYSED before they are stripped — revision 12. Revision 11
    # parsed them and threw them away, which is how `GIT_CONFIG_KEY_0=core.hooksPath`
    # reached a commit that `git -c core.hooksPath=` could not. See `analyse_env_prefix`.
    assignments: List[str] = []
    while argv and ASSIGNMENT.match(argv[0]) and not argv[0].startswith("-"):
        assignments.append(argv[0])
        argv = argv[1:]
    if assignments:
        analyse_env_prefix(assignments, findings)
    if not argv:
        return
    program = normalise_program(argv[0])

    if OPAQUE in argv[0]:
        # `$(echo git) add -A` — the program itself is the result of an expansion, so
        # nothing about what runs is derivable. Fail closed rather than read the operands.
        findings.append(Finding("OPAQUE_PROGRAM", "expansion", [OPAQUE],
                                "the program name is produced by an expansion"))
        return

    # ── delegation to another agent runtime ──
    #
    # Placed before every wrapper and every write primitive: `codex exec` names no path
    # and writes nothing itself, so every branch below reads it as a harmless program
    # with a string argument, which is exactly how revision 8 allowed it.
    if program in DELEGATING_BINARIES:
        rest = [t for t in argv[1:] if t not in ("--",)]
        first = next((t for t in rest if not t.startswith("-")), "")
        only_flags = all(t.startswith("-") for t in rest) if rest else True
        exempt = (
            (first and first in DELEGATION_EXEMPT_SUBCOMMANDS)
            or (only_flags and rest and all(t in DELEGATION_EXEMPT_FLAGS for t in rest))
        )
        if not exempt:
            findings.append(Finding("DELEGATE", " ".join(argv[:2]), [UNNAMED],
                                    "starts another agent runtime, whose effects this "
                                    "guard never sees"))
        return

    # ── a launcher that fetches a package and runs a program out of it ──
    #
    # Placed immediately after delegation and before every other wrapper, for the same
    # reason delegation is placed before them: `npx codex exec 'go'` names no path and
    # writes nothing itself, so without this branch the package-manager rule below reads
    # `npx` as an unclassified program and the whole line is allowed.
    launcher = launcher_key(argv)
    if launcher is not None:
        words, value_flags = launcher
        child, inline = launcher_child(argv, words, value_flags)
        for body in inline:
            analyse_command(body, findings, depth + 1)
        if child:
            analyse_argv(child, [], heredocs, findings, depth + 1)
        elif not inline:
            findings.append(Finding(
                "SHELL_OUT", " ".join(argv[:words]), [UNNAMED],
                "fetches and runs a program this command does not name"))
        return

    # ── wrappers that carry another command ──
    if program in SHELL_BINARIES:
        for index, token in enumerate(argv[1:], start=1):
            if token in SHELL_SCRIPT_FLAGS and index + 1 < len(argv):
                analyse_command(argv[index + 1], findings, depth + 1)
                return
        operands_ = [t for t in argv[1:] if not t.startswith("-")]
        # 🔴 A heredoc or herestring fed to a SHELL is that shell's script — revision 11.
        # The stdin-program family is not confined to interpreters, and the shell half of
        # it was worse: all four cells were open, not three.
        #
        # ```text
        # bash <<'EOF' … git add -A … EOF        ALLOW  🔴  the founding harm itself
        # bash - <<'EOF' … git add -A … EOF      ALLOW  🔴
        # sh <<< 'git add -A'                    ALLOW  🔴
        # control  echo 'git add -A' | sh        DENY   STDIN_SHELL ✓
        # control  sh -c 'git add -A'            DENY   BLANKET_STAGING ✓
        # ```
        #
        # Analysed as a COMMAND rather than reported as opaque, because it is one and the
        # guard can read it — `bash <<EOF … git add -A` now denies for BLANKET_STAGING,
        # the same sentence the actor already knows, and not for an unnameable effect.
        if heredocs and not operands_:
            for body in heredocs:
                analyse_command(body, findings, depth + 1)
            return
        if piped_in and not operands_:
            # `echo 'git add -A' | sh` — the script arrives on stdin, so the command
            # names nothing about what will run. `sh script.sh` is the declared escape
            # hatch and stays allowed: a committed script invoked by name is reviewable.
            findings.append(Finding("STDIN_SHELL", program, [UNNAMED],
                                    "a shell reading its script from a pipe"))
        return  # an interactive shell, or a named script, carries nothing to police here

    if program == "eval":
        # `eval "git add -A"` is a shell wrapper spelled without a flag.
        for token in argv[1:]:
            analyse_command(token, findings, depth + 1)
        return
    if program in TRANSPARENT_WRAPPERS or program in POSITIONAL_WRAPPERS or program == "env":
        value_flags = TRANSPARENT_WRAPPERS.get(program) or POSITIONAL_WRAPPERS.get(
            program, frozenset({"-u", "--unset"}))
        rest = strip_wrapper_options(argv[1:], value_flags, assignments=(program == "env"))
        if program in POSITIONAL_WRAPPERS:
            rest = rest[1:]  # the duration, or the new root
        analyse_argv(rest, [], heredocs, findings, depth + 1)
        return
    if program in STDIN_FED_WRAPPERS:
        rest = list(argv[1:])
        value_flags = {"-n", "-P", "-I", "-i", "-L", "-s", "-d", "-a", "-E", "--max-args",
                       "--max-procs", "--replace", "--delimiter", "--arg-file"}
        while rest and rest[0].startswith("-"):
            flag = rest.pop(0)
            if flag in value_flags and rest:
                rest.pop(0)
        child = list(rest)
        # Every operand this child acts on arrives on stdin, so the command names none.
        sub: List[Finding] = []
        analyse_argv(child + [UNNAMED], [], heredocs, sub, depth + 1)
        for finding in sub:
            finding.detail = (finding.detail + " · operands arrive on stdin, so the "
                              "command names none of them").strip(" ·")
            finding.targets = [UNNAMED]
        # 🔴 PAYLOAD AS COMMAND — revision 11. Retargeting only runs over findings that
        # EXIST, and for the shape below there are none:
        #
        # ```text
        # echo 'rm framework/x' | xargs -I{} sh -c '{}'        ALLOW  no effects derived
        # echo 'rm framework/x' | xargs -0 -I{} bash -c '{}'   ALLOW  no effects derived
        # cat /tmp/cmds        | xargs -n1 sh -c               ALLOW  no effects derived
        # control  echo framework/x | xargs rm                 DENY   DELETE @ UNNAMED ✓
        # ```
        #
        # `-I` is in the value-flag loop, so `-I` and `{}` are both popped and the child
        # becomes `['sh','-c','{}']` — a shell whose script is the literal replacement
        # marker. The COMMAND arrives on stdin, exactly as the operands do, and this
        # wrapper's whole reason for existing is that what arrives on stdin is not named.
        #
        # A survivor of four revisions of hardening. This repository's own corpus row
        # `S8-xargs-payload` is `… xargs -I{} sh -c 'echo y > {}'` and DENIES — because
        # its script carries a redirection the parser can see. Delete the visible command
        # and the identical wrapper allows: the row tests a spelling.
        if not sub and normalise_program(child[0] if child else "") not in KNOWN_READERS:
            findings.append(Finding(
                "UNDERIVED_STDIN_CHILD", " ".join(argv[:2]), [UNNAMED],
                "runs a child whose command AND operands both arrive on stdin, so this "
                "command states neither"))
        findings.extend(sub)
        return

    # ── git ──
    if program == "git":
        # 🔴 `git -C <peer> …` moves the whole subcommand into another working tree, and
        # every branch below derives paths relative to the one the command runs in.
        # Without this, confinement holds for `echo x > <peer>/f` and not for
        # `git -C <peer> commit -a`, which is the same act with better tooling.
        #
        # The repair is to RETARGET the subcommand's findings, not to add a finding of
        # its own. `git -C <peer> status` must stay allowed — reading a peer is granted —
        # and a standalone finding for the `-C` value could only be READ (which denies
        # nothing) or a write (which would deny every cross-worktree read). Retargeting
        # asks the right question: whatever this subcommand MUTATES, it mutates over
        # there.
        # 🔴 `git -c <key>=<value> <subcommand>` sets configuration for ONE invocation,
        # writing no file at all — revision 11. Measured at `e01d6d2`:
        #
        # ```text
        # git -c core.hooksPath=/tmp/h commit -m x CLAUDE.md   ALLOW  🔴
        #     STAGE @ INSIDE_REPO · COMMIT @ INSIDE_REPO — and a hook out of /tmp/h
        # ```
        #
        # That is the whole `git config core.hooksPath` → scratch hook → `chmod +x` →
        # `git commit` chain collapsed into ONE command, with every part of it granted:
        # writing and `chmod`-ing under `/tmp` are `SCRATCH`, staging and committing a
        # named path are `SHELL_DEFAULT`'s own grants, and `-c` was an option whose value
        # `operands()` skipped. No file is written, so no scope defence could ever fire,
        # and no composability test that looked at each step could see it.
        #
        # Judged as the execution-control redirection it is, and NOT as a config write:
        # nothing is persisted, and a receipt has to name what was actually touched.
        for index, token in enumerate(argv[1:], start=1):
            inline = None
            if token == "-c" and index + 1 < len(argv):
                inline = argv[index + 1]
            elif token.startswith("-c") and len(token) > 2 and not token.startswith("--"):
                inline = token[2:]
            if inline is not None and is_execution_control_key(inline):
                findings.append(Finding(
                    "EXECUTION_CONTROL", f"git -c {inline.split('=', 1)[0]}",
                    [f"git -c: {inline.split('=', 1)[0]}"],
                    "sets a configuration key whose value is a PROGRAM git executes, "
                    "for this invocation — changing what runs without writing any file",
                    scope=em.RUNTIME_CONFIG))

        elsewhere = flag_value(argv, "-C", "--git-dir", "--work-tree")
        if elsewhere is not None:
            here: List[Finding] = []
            # `-c` is stripped here too: the loop above has already emitted its finding,
            # and leaving it in would emit a second one from the recursion.
            analyse_argv([argv[0]] + strip_wrapper_options(
                argv[1:], frozenset({"-C", "--git-dir", "--work-tree", "-c"})),
                [], heredocs, here, depth + 1)
            for finding in here:
                if finding.effect in (em.READ,):
                    continue
                finding.targets = [posixpath.join(elsewhere, t)
                                   if t not in (UNNAMED, OPAQUE) and not posixpath.isabs(t)
                                   else t for t in finding.targets] or [elsewhere]
                finding.detail = (finding.detail
                                  + f" · in the working tree at `{elsewhere}`").strip()
            findings.extend(here)
            return
        sub, rest = git_subcommand(argv)
        if sub == "add":
            paths = [t for t in rest if not t.startswith("-")]
            named = [t for t in paths if t not in (".", "./", "*", UNNAMED)]
            blanket = (
                any(t in BLANKET_ADD for t in rest)
                or any(t in (".", "./", "*") for t in paths)
                or (any(t in BLANKET_WITHOUT_PATH for t in rest) and not named)
            )
            if blanket or not paths or UNNAMED in paths:
                findings.append(Finding("BLANKET_STAGING", "git add", [UNNAMED],
                                        "stages paths the command does not name"))
            else:
                # 🔴 An ALLOWED staging is still an EFFECT, and revisions 1–7 emitted
                # nothing for it. That was invisible while the only question was
                # allow/deny; under post-effect verification it is the whole game — an
                # authorised effect set that omits the STAGE cannot match an observed
                # index change, so every legitimate `git add <path>` would have been
                # reported as an unexplained side effect.
                findings.append(Finding("NAMED_STAGING", "git add", named,
                                        "stages the paths it names"))
        elif sub == "commit":
            if has_flag(["git"] + rest, "-a", "--all"):
                findings.append(Finding("BLANKET_STAGING", "git commit -a", [UNNAMED],
                                        "stages every tracked change, named or not"))
            paths = [t for t in rest if not t.startswith("-")]
            # `git commit -m msg` — the message is the value of `-m`, not a path.
            message = flag_value(["git"] + rest, "-m", "--message", "-F", "--file",
                                 "-C", "--reuse-message", "--author", "--date")
            paths = [t for t in paths if t != message]
            if paths:
                findings.append(Finding("NAMED_STAGING", "git commit <path>", paths,
                                        "commits the paths it names, staging them first"))
            findings.append(Finding("COMMIT", "git commit", ["HEAD"],
                                    "creates a commit and advances HEAD"))
        elif sub == "stage":
            findings.append(Finding("BLANKET_STAGING", "git stage", [UNNAMED],
                                    "an alias of `git add` with the same reach"))
        else:
            analyse_git(sub, rest, heredocs, findings)
        return

    # ── in-place editors ──
    if program in ("sed", "gsed") and has_flag(argv, "-i", "--in-place"):
        targets = operands(argv, "sed")
        # BSD `sed -i ''` consumes the empty suffix as the option value.
        targets = [t for t in targets if t != ""]
        findings.append(Finding("IN_PLACE_EDIT", "sed -i", targets[1:] or targets or [UNNAMED],
                                "rewrites the files it names, unread"))
        return
    if program in IN_PLACE_PROGRAMS and (
            has_flag(argv, "-i", "--in-place") or "inplace" in argv):
        # `gawk -i inplace '{print}' f` — the `-i` value is the extension library name,
        # not a suffix, so the operands after the program text are the targets.
        targets = [t for t in operands(argv, program)
                   if t not in ("inplace", "") and not t.startswith("{")]
        findings.append(Finding("IN_PLACE_EDIT", f"{program} -i",
                                targets[1:] or targets or [UNNAMED],
                                "rewrites the files it names, unread"))
        return
    if program in BATCH_EDITORS:
        findings.append(Finding("FILE_WRITE", program, operands(argv, program) or [UNNAMED],
                                "an editor writes the file it is pointed at"))
        return
    if program in SPLITTERS:
        into = flag_value(argv, "-f", "--prefix")
        targets = operands(argv, program)
        # `split [OPTS] INPUT PREFIX` puts the prefix LAST and defaults it to `x` in the
        # working directory when it is absent — which the command does not name, so that
        # case is UNNAMED rather than "no write". `csplit -f PREFIX INPUT …` carries it
        # in the flag and defaults to `xx`, the same way.
        if into is not None:
            destination = [into]
        elif program == "split" and len(targets) >= 2:
            destination = targets[-1:]
        else:
            destination = [UNNAMED]
        findings.append(Finding("FILE_WRITE", program, destination,
                                "writes a series of files at the prefix it names"))
        return
    if program in PACKAGE_MANAGERS:
        rest = [t for t in argv[1:] if not t.startswith("-")]
        # 🔴 A package manager's RUN verb executes a child — revision 12.
        #
        # `uv run codex exec 'go'` ALLOWED at revision 11 while `uvx codex exec 'go'`
        # DENIED, because `uvx` is a declared launcher and `uv` is a package manager whose
        # branch only ever looked for an INSTALL verb. `npm run` had the same split from
        # `npm exec`. The tail is a command, so it is analysed as one — the rule already
        # applied to `npx` and to every launcher in `PACKAGE_LAUNCHERS`.
        if rest and rest[0] in PACKAGE_RUN_SUBCOMMANDS:
            child = argv[argv.index(rest[0]) + 1:]
            if child:
                analyse_argv(list(child), [], heredocs, findings, depth + 1)
            else:
                findings.append(Finding(
                    "SHELL_OUT", f"{program} {rest[0]}", [UNNAMED],
                    "runs a program this command does not name"))
            return
        if rest and rest[0] in INSTALLING_SUBCOMMANDS or program.startswith("pip"):
            into = flag_value(argv, *PACKAGE_TARGET_FLAGS)
            findings.append(Finding("FILE_WRITE", f"{program} install",
                                    [into] if into else [UNNAMED],
                                    "unpacks packages this command does not enumerate "
                                    "into a directory it may not name"))
        return
    if program in INTERPRETERS:
        analyse_interpreter(argv, program, heredocs, findings)
        return
    if program in ("apply_patch", "applypatch"):
        targets: List[str] = []
        for body in heredocs:
            targets.extend(PATCH_TARGET.findall(body))
        findings.append(Finding("PATCH_APPLY", program, targets or [UNNAMED],
                                "writes every file its envelope names"))
        return
    if program == "patch":
        # 🔴 OPTION/OPERAND CONFUSION — revision 11. `operands()` had no entry for
        # `patch`, so every option value arrived as if it were a path and the DIFF was
        # read as the destination:
        #
        # ```text
        # patch -p1 -i /tmp/p.diff     ALLOW   WRITE '/tmp/p.diff' @ SCRATCH   🔴
        # patch -p1  < /tmp/p.diff     ALLOW   WRITE '/tmp/p.diff' @ SCRATCH   🔴
        # patch --input /tmp/p.diff    ALLOW   WRITE '/tmp/p.diff' @ SCRATCH   🔴
        # patch --input=/tmp/p.diff    DENY    UNNAMED    ← right answer, by accident
        # control  patch framework/x /tmp/p.diff          DENY  @ INSIDE_REPO  ✓
        # ```
        #
        # The input is not the target. `patch [OPTS] [ORIGFILE [PATCHFILE]]` names its
        # destination only in the FIRST positional; with `-i`/`<` the destination is
        # stated inside a diff this guard cannot read, and `-o` overrides it entirely.
        # An unnamed destination is UNNAMED, which fails closed — the same answer the
        # `--input=` spelling reached for the wrong reason.
        into = flag_value(argv, "-o", "--output")
        directory = flag_value(argv, "-d", "--directory")
        positional = operands(argv, "patch")
        if into is not None:
            destination = [into]
        elif positional:
            destination = positional[:1]
        else:
            destination = [UNNAMED]
        if directory is not None:
            destination = [posixpath.join(directory, t) if t not in (UNNAMED, OPAQUE)
                           and not posixpath.isabs(t) else t for t in destination]
        findings.append(Finding("PATCH_APPLY", "patch", destination,
                                "writes the file it is applied to — which the diff "
                                "names, and this command may not"))
        return

    # ── plain filesystem writes ──
    if program in WRITES_ALL_OPERANDS:
        targets = operands(argv, program)
        findings.append(Finding("FILE_WRITE", program, targets or [UNNAMED],
                                "writes every operand"))
        return
    if program in WRITES_LAST_OPERAND:
        targets = operands(argv, program)
        # 🔴 `-t DIR` / `--target-directory=DIR` moves the destination OUT of the
        # operand list and into a flag, and `operands()` skips option values — so the
        # "destination" derived here used to be the last SOURCE. `cp -t framework/scripts
        # /tmp/a /tmp/b` reported `/tmp/b`, classified it SCRATCH, and allowed a write
        # into the repository. Measured on revision 7, 2026-08-29, for cp, mv and install.
        into = flag_value(argv, "-t", "--target-directory")
        if into is not None:
            destination = [into]
        else:
            destination = targets[-1:] or [UNNAMED]
        if program == "mv":
            # A move mutates BOTH ends: the source ceases to exist where it was. Both
            # are authorised, so `mv framework/a /tmp/b` is refused for the source even
            # though its destination is scratch.
            sources = targets if into is not None else targets[:-1]
            findings.append(Finding("FILE_RENAME", "mv", (sources + destination) or [UNNAMED],
                                    "moves its operands, mutating source and destination"))
        else:
            findings.append(Finding("FILE_WRITE", program, destination,
                                    "writes its destination operand"))
        return

    # ── permission and ownership ──
    if program in ("chmod", "chown", "chgrp", "chflags", "xattr", "setfacl"):
        if program == "chmod":
            # 🔴 The mode is LOCATED, not counted off the front. `chmod -x <scratch>`
            # lost its path to the option filter and then lost the filter's survivor to
            # the positional skip — see `chmod_operands`.
            _, targets = chmod_operands(argv)
        else:
            targets = operands(argv, program)
            # The first operand is the owner or flag spec, not a path. Reporting it as a
            # write target would deny for the right reason and name the wrong thing, and
            # a receipt has to name what was actually touched.
            targets = targets[1:] if program in ("chown", "chgrp", "chflags") else targets
        findings.append(Finding("PERMISSION_CHANGE", program, targets or [UNNAMED],
                                "changes mode, ownership or attributes of every operand"))
        return

    # ── creation without content ──
    if program in ("touch", "mkdir", "mktemp"):
        targets = operands(argv, program)
        if program == "mktemp" and not targets:
            return  # `mktemp` with no template writes into the system temp directory
        findings.append(Finding("FILE_WRITE", program, targets or [UNNAMED],
                                "creates the path, or moves its mtime"))
        return

    # ── network transfers that name a local destination ──
    if program in ("curl", "wget", "wget2", "aria2c", "http", "https"):
        into = flag_value(argv, "-o", "--output", "-O", "--remote-name",
                          "--output-document", "-P", "--directory-prefix", "-d", "--dir")
        remote_name = has_flag(argv, "-O", "--remote-name") and into is None
        if program.startswith("wget") and has_flag(argv, "-O"):
            into = flag_value(argv, "-O") or into
        if remote_name:
            # `curl -O url` writes the URL's basename into the CURRENT directory, which
            # the command never names. Unnamed, therefore refused.
            findings.append(Finding("FILE_WRITE", f"{program} -O", [UNNAMED],
                                    "writes the URL's basename into the working directory"))
        elif into is not None:
            findings.append(Finding("FILE_WRITE", program, [into],
                                    "writes the fetched bytes to its destination"))
        elif program.startswith("wget"):
            # Bare `wget url` also writes into the working directory.
            findings.append(Finding("FILE_WRITE", program, [UNNAMED],
                                    "writes into the working directory by default"))
        upload = flag_value(argv, "-T", "--upload-file", "-d", "--data", "--data-binary",
                            "-F", "--form")
        if upload is not None or has_flag(argv, "-T", "--upload-file"):
            findings.append(Finding("NETWORK_WRITE", program, [upload or UNNAMED],
                                    "sends local bytes to a remote host",
                                    scope=em.NONLOCAL))
        return

    if program in ("scp", "sftp", "ftp", "rclone"):
        findings.append(Finding("NETWORK_WRITE", program,
                                operands(argv, program) or [UNNAMED],
                                "copies between this machine and a remote host",
                                scope=em.NONLOCAL))
        return

    # ── archive extraction ──
    if program in ("tar", "gtar", "bsdtar"):
        extracting = has_flag(argv, "-x", "--extract", "--get") or any(
            t.startswith("x") and not t.startswith("-") for t in argv[1:2])
        if not extracting:
            return  # creating or listing an archive writes only what `-f` names, below
        into = flag_value(argv, "-C", "--directory")
        findings.append(Finding("ARCHIVE_EXTRACT", "tar", [into] if into else [UNNAMED],
                                "expands members this command does not enumerate; a member "
                                "path may contain `..` and land outside the destination"))
        return
    if program in ("unzip", "7z", "7za", "unrar", "gunzip", "bunzip2", "unxz", "zstd"):
        into = flag_value(argv, "-d", "-o", "--output-dir", "-C")
        findings.append(Finding("ARCHIVE_EXTRACT", program, [into] if into else [UNNAMED],
                                "expands members this command does not enumerate"))
        return
    if program in DESTROYS_OPERANDS:
        findings.append(Finding("FILE_DELETE", program, operands(argv, program) or [UNNAMED],
                                "removes every operand"))
        return
    if program == "dd":
        outs = [t.split("=", 1)[1] for t in argv[1:] if t.startswith("of=")]
        findings.append(Finding("FILE_WRITE", "dd", outs or [UNNAMED], "writes `of=`"))
        return
    if program == "find":
        if "-delete" in argv:
            findings.append(Finding("FILE_DELETE", "find -delete", [UNNAMED],
                                    "deletes whatever the traversal matched"))
        for flag in ("-exec", "-execdir", "-ok", "-okdir"):
            if flag in argv:
                child = argv[argv.index(flag) + 1 :]
                cut = next((i for i, t in enumerate(child) if t in (";", "+", "{}")), len(child))
                sub = []
                analyse_argv(child[:cut] + [UNNAMED], [], heredocs, sub, depth + 1)
                for finding in sub:
                    finding.targets = [UNNAMED]
                    finding.detail = (finding.detail + " · run per traversal match").strip()
                findings.extend(sub)
        return

    # ── nothing above classified this program ─────────────────────────────────────
    #
    # 🔴 For revisions 1–10 this was an unconditional `return`, and that silence IS the
    # defect class. "No effect derived" was read as "no effect", which is the
    # open-vocabulary failure `effect_model`'s own docstring says must never happen.
    unclassified(argv, program, findings, depth, heredocs)


def _env_value_is_actor_controlled(value: str) -> bool:
    """Does this value name something the ACTOR can put a program into?

    🔴 The discriminator that keeps `GIT_PAGER=cat git log --oneline -5` working — a
    COMMITTED positive control of this repository. `cat` is a bare name resolved through
    `PATH` to a system binary; `/tmp/evil` is a file the actor just wrote. A rule that
    refused both would close the family and break the control, which is the trade this
    whole revision exists to avoid making blindly.

    A value carrying a path separator, a `~`, or an expansion is actor-controlled. A bare
    word is not. `PATH` is handled by its caller, because for `PATH` the hazard is the
    LIST it prepends rather than the value as a whole.
    """
    if not value:
        return False
    return ("/" in value or value.startswith("~") or EXPANDS.search(value) is not None
            or value.startswith("."))


def analyse_env_prefix(assignments: Sequence[str], findings: List[Finding]) -> None:
    """Judge `NAME=VALUE` prefixes by the CONSEQUENCE of the variable — revision 12.

    Four rules, and the first is the one that repairs invariant A:

    ```text
    GIT_CONFIG_KEY_<n>=<key>   ->  the same question `git -c <key>=` asks, so the same
                                   answer: is_execution_control_key(<key>)
    GIT_CONFIG_GLOBAL=<file>   ->  a config file the actor chose, which can carry
                                   core.hooksPath or an alias with a `!` body
    LD_PRELOAD=<anything>      ->  no benign value exists in a guarded shell
    <name naming a program>    ->  execution control WHEN the value is actor-controlled
    ```

    Everything else is left alone. That is a declared boundary, not an oversight: the
    variable space is open, and a rule that denied every unrecognised assignment would
    refuse `FOO=1 make` and be removed within a day.
    """
    values = {}
    for token in assignments:
        match = ASSIGNMENT.match(token)
        if match:
            values[match.group(1)] = match.group(2)

    for name, value in values.items():
        # 1 · a git configuration KEY delivered through the environment
        if ENV_GIT_CONFIG_KEY.match(name):
            if is_execution_control_key(value):
                findings.append(Finding(
                    "EXECUTION_CONTROL", f"{name}={value}", [f"git config: {value}"],
                    "sets a git configuration key through the environment whose value is "
                    "a PROGRAM git executes — the same object `git -c` reaches, and it "
                    "must get the same answer",
                    scope=em.RUNTIME_CONFIG))
            continue
        # 2 · a configuration FILE the actor chose
        if name in ENV_CONFIG_FILE:
            findings.append(Finding(
                "EXECUTION_CONTROL", f"{name}={value}", [f"git config file: {value}"],
                "points git at a configuration file this command names, which can carry "
                "`core.hooksPath`, an `alias.*` with a `!` body, or a `filter.*` program",
                scope=em.RUNTIME_CONFIG))
            continue
        # 3 · loader injection, which has no benign form here
        if name in ENV_ALWAYS_EXECUTION_CONTROL:
            findings.append(Finding(
                "EXECUTION_CONTROL", f"{name}={value}", [f"loader: {name}"],
                "injects code into every process this command starts",
                scope=em.RUNTIME_CONFIG))
            continue
        # 4 · a variable naming a program or a startup file, enumerated OR shaped
        known = name in ENV_EXECUTION_CONTROL or ENV_CONTROL_SHAPE.search(name)
        if known and _env_value_is_actor_controlled(value):
            findings.append(Finding(
                "EXECUTION_CONTROL", f"{name}={value}", [f"env: {name}"],
                "names a program or startup file this command chose, which the runtime "
                "will execute — changing what runs without writing any file",
                scope=em.RUNTIME_CONFIG))


#: The names `wrapper_tail` will re-analyse from. Derived by SUBTRACTION — every program
#: this module models, minus the pure readers — so a program added to a table below is
#: reachable through an unknown wrapper without anybody remembering this set exists.
#: `test_guard_families_rev12.py` asserts it is non-empty and excludes the readers, so it
#: cannot silently become the empty set and stop firing.
#: 🔴 Subtracted from PURE_READERS, not from KNOWN_READERS: a CONDITIONAL reader hiding
#: in an unknown wrapper's tail — `xcrun sort -o <peer>/f in` — must still be reached.
WRAPPER_TAIL_PROGRAMS = frozenset(_KNOWN_PROGRAM_NAMES) - frozenset(PURE_READERS)


def unclassified(argv: Sequence[str], program: str, findings: List[Finding],
                 depth: int = 0, heredocs: Sequence[str] = ()) -> None:
    """The last branch: a program this policy has no model for.

    Three outcomes, and the middle one is the revision-11 repair:

    ```text
    a KNOWN_READER                       nothing — a read is granted everywhere
    a program the command does not STATE  UNKNOWN_EFFECT — `{}`, `$CMD`, an expansion
    anything else                         UNDERIVED_OPERAND over its operands, which
                                          denies only where no authority grants a write
    ```

    The third is not "deny unknown programs". It is *this command names an object that
    belongs to a peer, to the shared checkout, to the common `.git`, or to the
    registration that decides whether this guard runs — and I derived nothing about it.*
    Reaching such an object through a program nobody classified is the same act as
    reaching it with `rm`, and SAME OBJECT → SAME AUTHORIZATION ANSWER.
    """
    # 🔴 THE READERS ARE ANSWERED FIRST, and the order is load-bearing.
    #
    # A first draft of this revision put the opaque-name test above them, and `[` — the
    # shell TEST builtin, whose name really is a bracket — was read as a program produced
    # by a glob. That refused `printf "%s\n" "$([ 1 = 1 ] && echo "A -> B")"`, a
    # COMMITTED negative control, for the SECOND time in two revisions. The same control
    # caught it both times.
    if program in PURE_READERS:
        return

    # A CONDITIONAL reader — revision 12. Its argv is derived before it is exempted,
    # because `sort` reads and `sort -o FILE` truncates FILE, and revision 11 exempted
    # both. An empty derivation means this invocation really is a read.
    model = READER_WRITE_MODEL.get(program)
    if model is not None:
        written = [t for t in model(argv) if t]
        if written:
            findings.append(Finding(
                "FILE_WRITE", program, written,
                "writes a file its ARGV names — this program reads by default, and the "
                "write mode is a property of how it was invoked"))
        return

    if OPAQUE_PROGRAM_NAME.search(program):
        findings.append(Finding("OPAQUE_PROGRAM", program, [OPAQUE],
                                "the program is not a name this command states"))
        return

    # 🔴 THE WRAPPER TAIL — revision 12, and it is the repair for `TRANSPARENT_WRAPPERS`
    # being a list.
    #
    # Measured at revision 11, each verified to execute its child on this host:
    #
    # ```text
    # xcrun <blanket>              script -q /dev/null <blanket>     screen -dm <blanket>
    # uv run codex exec 'go'       npm run <blanket>
    # control  nohup <blanket> · env <blanket> · timeout 5 <blanket>   DENY ✓
    # ```
    #
    # Adding eight names would close eight commands. The FAMILY is *a program this policy
    # has no model for, whose argv contains a command this policy DOES model* — and that
    # is derivable from the text without knowing the wrapper. So the tail is re-analysed
    # from the first token that names a modelled, non-reading program.
    #
    # The failure direction is refusal and the cost is over-refusal when an OPERAND
    # happens to be spelled like a program: `mytool rm` re-reads as `rm` with no operand
    # and is refused. That is the trade this policy has always made for an unmodelled
    # program, and it is bounded by only scanning names the tables already carry.
    child = wrapper_tail(argv)
    if child is not None:
        sub: List[Finding] = []
        analyse_argv(list(child), [], list(heredocs), sub, depth + 1)
        for finding in sub:
            finding.detail = (finding.detail + f" · carried by `{program}`, a program "
                              "this guard has no model for").strip(" ·")
        findings.extend(sub)
        return

    targets = [t for t in operands(argv, program) if t not in (UNNAMED, OPAQUE)]
    if targets:
        findings.append(Finding(
            "UNDERIVED_OPERAND", program, targets,
            "names an object this guard derived no effect on, through a program it has "
            "no model for"))


def wrapper_tail(argv: Sequence[str]) -> "Optional[List[str]]":
    """The child command hiding in an unmodelled program's argv, or None.

    Scans for the first token that NORMALISES to a program some table in this module
    models and that is not a pure reader. `xcrun git add -A` yields `['git','add','-A']`;
    `xcrun --version` yields None because no token names a program.

    🔴 Position 0 is skipped — that is the unmodelled program itself. And a token that is
    an OPTION is skipped, so `script -q /dev/null git …` reaches `git` rather than
    stopping at a flag that happens to share a name.
    """
    for index in range(1, len(argv)):
        token = argv[index]
        if not token or token.startswith("-") or token in (UNNAMED, OPAQUE):
            continue
        name = normalise_program(token)
        if name in WRAPPER_TAIL_PROGRAMS:
            return list(argv[index:])
    return None


#: `git <sub>` families beyond add/commit/stage. Revision 7 derived NOTHING for any of
#: these: a probe of 46 shapes on 2026-08-29 found `git rm`, `git mv`, `git restore`,
#: `git apply`, `git checkout -- .`, `git reset --hard`, `git clean -fd`, `git push`,
#: `git tag`, `git branch -D`, `git update-ref`, `git stash`, `git notes` and
#: `git worktree remove` ALL allowed. Six of those were declared open debt; the other
#: eight were not declared anywhere, which is the difference between a scope boundary
#: and a hole.
GIT_REF_SUBCOMMANDS = frozenset({
    "tag", "update-ref", "symbolic-ref", "branch", "notes", "stash", "reflog",
    "rebase", "cherry-pick", "revert", "merge", "am", "filter-branch", "replace",
    "worktree", "gc", "prune", "fast-import",
})
GIT_NETWORK_SUBCOMMANDS = frozenset({"push", "send-pack", "send-email", "request-pull"})
#: `git branch` / `git tag` flags that move or delete a ref that ALREADY EXISTS. Naming
#: a new ref without one of these is a creation, and a creation loses nothing.
REF_DESTRUCTIVE_FLAGS = ("-d", "-D", "--delete", "-m", "-M", "--move", "-c", "-C",
                         "--copy", "-f", "--force", "--set-upstream-to", "-u",
                         "--unset-upstream", "--edit-description")
#: 🔴 Families whose FIRST non-flag operand is a VERB and not a ref — revision 10.
#:
#: `git worktree add --detach /tmp/base <sha>` predicted three ref mutations, on `add`,
#: on `/tmp/base` and on `<sha>`. Only the middle one names anything, and `add` is the
#: subcommand's own verb. This is the `git update-ref <ref> <sha>` defect in a second
#: place — a receipt has to name what was actually touched, and two of those three could
#: never be observed, so an authorised call would report them MISSING forever.
#:
#: 🔴 It does not change a single VERDICT and is not meant to. Measured against the
#: revision-9 engine at `6fb7a83`, `git worktree add` is REF_MUTATION at `INSIDE_REPO`
#: and refused; it still is. What changes is what the refusal, and any receipt of it,
#: says was touched. The wider question — whether adding a worktree should be
#: `FILE_WRITE` at its destination rather than a ref mutation, which is what the
#: `elif sub == "worktree" and second == "add"` branch below was written to do and which
#: is UNREACHABLE because `worktree` is also in `GIT_SUB_READ` — is a revision-9
#: behaviour this candidate found and deliberately did NOT repair. It is outside R1–R12,
#: the denial it produces is defensible on its own terms (a new worktree writes
#: `.git/worktrees/<name>`, which § 4.7 confines), and changing it here would be a
#: behaviour change nobody reviewed.
GIT_VERB_SUBCOMMANDS = frozenset({"worktree", "stash", "notes", "reflog", "replace",
                                  "submodule", "bisect", "remote"})

#: Families whose SECOND word decides whether anything is mutated at all.
GIT_SUB_READ = {
    "worktree": frozenset({"list"}),
    "stash": frozenset({"list", "show"}),
    "notes": frozenset({"list", "show", ""}),
    "reflog": frozenset({"show", ""}),
    "rebase": frozenset(),
    "replace": frozenset({"-l", "--list", ""}),
}
#: Read-only plumbing and porcelain. Listed positively: everything NOT here and not in
#: a table above is UNKNOWN_EFFECT, which denies. A new git subcommand is refused until
#: someone classifies it, which is the failure direction this policy wants.
GIT_READ_SUBCOMMANDS = frozenset({
    "status", "log", "show", "diff", "cat-file", "rev-parse", "rev-list", "ls-files",
    "ls-tree", "ls-remote", "for-each-ref", "describe", "blame", "grep", "shortlog",
    "show-ref", "name-rev", "merge-base", "hash-object", "var", "count-objects",
    "verify-commit", "verify-tag", "check-ignore", "check-attr", "whatchanged",
    "annotate", "cherry", "difftool", "help", "version", "bisect", "range-diff",
    "fetch", "instaweb", "citool", "gui",
})

#: 🔴 Revision 11. `config`, `remote`, `archive` and `bundle` were on the READ list, and
#: all four write. Measured at `e01d6d2`, at ordinary `SHELL_DEFAULT`:
#:
#: ```text
#: git config user.name x                      ALLOW  🔴  mutates .git/config
#: git config --global core.hooksPath /tmp/h   ALLOW  🔴  redirects every hook
#: git config --add alias.zz '!sh -c …'        ALLOW  🔴  binds a shell command to a word
#: git remote set-url origin https://evil/x    ALLOW  🔴  moves the publication route
#: git archive -o framework/a.tar HEAD         ALLOW  🔴  writes into the repository
#: git bundle create framework/a.bundle HEAD   ALLOW  🔴  writes into the repository
#: control  echo x > <repo>/.git/config        DENY   CONFINED_GIT_COMMON_DIR  ✓
#: ```
#:
#: The control is the whole finding: the PATH route to `.git/config` was refused and the
#: TOOL route to the same bytes was granted. SAME OBJECT → SAME AUTHORIZATION ANSWER.
#:
#: `fetch` is deliberately still a read, and that is DECLARED rather than repaired: it
#: does move `refs/remotes/*`, which is a ref mutation this policy does not derive.
#: Changing it would refuse a command the orchestration runs constantly, on a family
#: outside this revision's four, and a behaviour change nobody reviewed is what revision
#: 10 declined to make in the same position. It is carried as residual debt.
GIT_CONFIG_READ_FLAGS = frozenset({
    "--get", "--get-all", "--get-regexp", "--get-urlmatch", "--list", "-l",
    "--get-color", "--get-colorbool", "--show-origin", "--show-scope", "--default",
})
GIT_CONFIG_WRITE_FLAGS = frozenset({
    "--add", "--unset", "--unset-all", "--replace-all", "--rename-section",
    "--remove-section", "--edit", "-e",
})
#: Which FILE a `git config` invocation lands in. The default is the repository's own
#: config, which for every worktree is one shared file under the common dir.
GIT_CONFIG_SCOPE_FLAGS = ("--global", "--system", "--local", "--worktree")

#: 🔴 Config keys whose VALUE is a program git will execute, or a location git will look
#: for programs in. This is the "model the consequence, not the filename" half: setting
#: one of these redirects execution no matter which config file it is written to, and
#: `git -c <key>=<value> <cmd>` sets one for a single invocation without writing any file
#: at all — which is how a complete hook installation fits in ONE allowed command.
#:
#: Matched as a prefix on the dotted key, lowercased, because git's section names are
#: case-insensitive and the middle component of `filter.<name>.clean` is arbitrary.
EXECUTION_CONTROL_KEYS = (
    "core.hookspath", "core.editor", "core.pager", "core.sshcommand", "core.gitproxy",
    "core.fsmonitor", "core.askpass", "core.symlinks", "core.filemode",
    "alias.", "filter.", "diff.", "merge.", "difftool.", "mergetool.",
    "credential.helper", "credential.", "init.templatedir", "protocol.",
    "uploadpack.", "receivepack.", "http.proxy", "remote.", "url.",
    "sequence.editor", "gpg.program", "ssh.variant", "safe.directory",
    "include.path", "includeif.",
    # 🔴 Revision 12 · SECTIONS whose every key names a program, so the family is the
    # section and not the leaf. `pager.<subcommand>` was ALLOW at revision 11 and is not
    # reachable by a suffix rule, because its last component is the subcommand's own name.
    "pager.", "man.", "browser.", "guitool.", "instaweb.", "sendemail.", "web.",
)

#: 🔴 The STRUCTURAL half of the same question — revision 12. A git configuration key
#: whose LAST component is one of these names something git executes, in whatever section
#: it appears. This is what reaches `man.<viewer>.cmd` and `pager.<subcommand>` — both
#: measured ALLOW at revision 11 and both verified to execute — without enumerating the
#: sections, and what will reach the section git adds next.
EXECUTION_CONTROL_KEY_SUFFIXES = frozenset({
    "cmd", "command", "tool", "helper", "program", "editor", "pager", "path",
    "textconv", "clean", "smudge", "process", "driver", "proxy", "askpass",
    "sshcommand", "hookspath", "templatedir", "binary", "exec", "shell", "script",
})


#: 🔴 ENVIRONMENT INDIRECTION — revision 12, and it refutes revision 11's own invariant A
#: at the sharpest point there is.
#:
#: ```text
#: git -c core.hooksPath=/tmp/h commit …                              DENY   RUNTIME_CONFIG
#: GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.hooksPath \
#:   GIT_CONFIG_VALUE_0=/tmp/h git commit …                           ALLOW  🔴
#: ```
#:
#: Same object, same primitive, two spellings, two answers — and the second was verified
#: by execution, with the hook firing. `SAME OBJECT → SAME AUTHORIZATION ANSWER` is the
#: invariant revision 11 published; this is it failing.
#:
#: `resolve_assignments` already PARSES these prefixes — `FOO=1 git add -A` has been
#: handled since revision 8 — and `analyse_argv` then throws them away. So this is not new
#: architecture: it is revision 11's own "model the consequence, not the filename" rule
#: applied to a surface the parser already sees.
#:
#: **This family is OPEN and is declared so.** Any program may read any variable, so no
#: enumeration can be complete. What is closed is the DIRECTION: a variable that names a
#: program to run, or a configuration file to read, is judged by that consequence, and a
#: variable whose value is not actor-controlled is left alone so `GIT_PAGER=cat git log`
#: — a committed positive control — keeps working.

#: Variables whose value IS a git configuration file. A config file can carry
#: `core.hooksPath`, an `alias.*` with a `!` body, or a `filter.*` program, so pointing
#: git at one the actor chose is the same act as writing those keys.
ENV_CONFIG_FILE = frozenset({
    "GIT_CONFIG", "GIT_CONFIG_GLOBAL", "GIT_CONFIG_SYSTEM",
})

#: Variables whose value names a PROGRAM the runtime will execute, or a file it will
#: source at startup. Judged only when the value is actor-controlled — see
#: `_env_value_is_actor_controlled`.
ENV_EXECUTION_CONTROL = frozenset({
    "GIT_EDITOR", "GIT_SEQUENCE_EDITOR", "GIT_PAGER", "GIT_EXTERNAL_DIFF",
    "GIT_SSH", "GIT_SSH_COMMAND", "GIT_ASKPASS", "GIT_PROXY_COMMAND",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_TEMPLATE_DIR", "GIT_EXEC_PATH",
    "GIT_HOOKS_PATH", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY", "GIT_DIR",
    "GIT_WORK_TREE", "GIT_NAMESPACE", "GIT_ATTR_NOSYSTEM", "GIT_CEILING_DIRECTORIES",
    "EDITOR", "VISUAL", "PAGER",
    "BASH_ENV", "ENV", "SHELLOPTS", "PROMPT_COMMAND", "ZDOTDIR",
    "PYTHONSTARTUP", "PYTHONPATH", "PYTHONHOME", "PERL5OPT", "PERL5LIB",
    "RUBYOPT", "RUBYLIB", "NODE_OPTIONS", "NODE_PATH",
    "PATH",
})

#: Variables that redirect execution unconditionally — there is no benign value for them
#: in a guarded shell, so the actor-controlled test is not applied.
ENV_ALWAYS_EXECUTION_CONTROL = frozenset({
    "LD_PRELOAD", "LD_LIBRARY_PATH", "LD_AUDIT",
    "DYLD_INSERT_LIBRARIES", "DYLD_LIBRARY_PATH", "DYLD_FRAMEWORK_PATH",
})

#: The STRUCTURAL half: a name this policy has never seen, whose SHAPE says its value is
#: a program or a startup file. Matched so that a variable nobody enumerated is still
#: judged — which is what stops this being another list standing in for a family.
ENV_CONTROL_SHAPE = re.compile(
    r"(?:^|_)(?:EDITOR|PAGER|VIEWER|BROWSER|SHELL)$"
    r"|_(?:COMMAND|CMD|PROG|PROGRAM|BIN|EXE|LAUNCHER|WRAPPER|HOOK|HOOKS)$"
    r"|(?:^|_)(?:PRELOAD|STARTUP|RCFILE|PROFILE|INIT)$"
    r"|^(?:GIT|HG|SVN)_.*_(?:COMMAND|CMD|PATH)$"
)

#: `GIT_CONFIG_KEY_<n>` carries an arbitrary configuration KEY, so the answer is the one
#: `is_execution_control_key` already gives for `git -c` — the same question, reached
#: through the environment.
ENV_GIT_CONFIG_KEY = re.compile(r"^GIT_CONFIG_KEY_(\d+)$")


def is_execution_control_key(key: str) -> bool:
    """Does setting this config key change WHAT RUNS?

    Prefix-matched on the lowercased dotted name. `alias.` and `filter.` are families —
    `alias.zz` is an arbitrary shell command bound to a git word, and `filter.x.clean` is
    a program git runs over file contents on checkout.

    🔴 **Revision 12 adds the SUFFIX half, and that is the repair.** The prefix list is a
    list, and Mirror defeated it with keys nobody had enumerated — each verified to
    execute:

    ```text
    git -c man.<viewer>.cmd=…    ALLOW at revision 11, no tty needed
    git -c pager.<subcommand>=…  ALLOW at revision 11
    control  core.pager · core.editor · alias.* · filter.*   DENY ✓
    ```

    Git's configuration space has a SHAPE: a key whose last component is `cmd`,
    `command`, `tool`, `helper`, `program`, `editor`, `pager`, `path`, `textconv`,
    `clean`, `smudge`, `process`, `driver` or `proxy` names something git executes,
    whatever section it sits in. Matching that suffix reaches `man.x.cmd` and
    `pager.log` without anyone having listed them, and it will reach the next section git
    adds. The prefix list stays for the keys whose hazard is NOT in their name —
    `init.templatedir`, `safe.directory`, `protocol.*`, `include.path`.
    """
    if not key or "=" in key:
        key = key.split("=", 1)[0]
    lowered = key.strip().lower()
    if any(lowered == p or lowered.startswith(p) for p in EXECUTION_CONTROL_KEYS):
        return True
    last = lowered.rsplit(".", 1)[-1] if "." in lowered else ""
    return last in EXECUTION_CONTROL_KEY_SUFFIXES


#: The ref namespace each subcommand operates in. `update-ref`, `reflog` and the
#: history-rewriting subcommands are absent on purpose: they take an already-qualified
#: ref, or they take a commit-ish that is not a ref at all, and inventing a namespace
#: for those would be guessing which one.
REF_NAMESPACE = {"branch": "refs/heads/", "tag": "refs/tags/"}


def qualify_ref(sub: str, target: str) -> str:
    """Write a predicted ref in the namespace its subcommand implies.

    🔴 Only when the subcommand SAYS which namespace, and never across namespaces: a
    bare name under `git branch` is a branch, a bare name under `git tag` is a tag, and
    a name that is already qualified is left exactly as written — including one
    qualified into the *other* namespace, because `git branch -D refs/tags/v1` failing
    to match an observed tag mutation is the correct answer, not a spelling to smooth over.
    """
    prefix = REF_NAMESPACE.get(sub)
    if not prefix or not target or target in (UNNAMED, OPAQUE):
        return target
    if target.startswith("refs/") or target == "HEAD":
        return target
    # A slash in the name is NOT a sign of qualification — `feature/x` is an ordinary
    # branch name and `refs/heads/feature/x` is what the ref snapshot will show. An
    # earlier draft treated any slash as "already qualified" and left exactly the
    # branches whose names have a slash unmatched.
    return prefix + target


def analyse_git(sub: str, rest: List[str], heredocs: List[str],
                findings: List[Finding]) -> None:
    """Every `git` subcommand but add/commit/stage, projected onto the effect model."""
    argv = ["git"] + rest

    if sub in GIT_NETWORK_SUBCOMMANDS:
        remote = next((t for t in rest if not t.startswith("-")), "<default remote>")
        findings.append(Finding(
            "NETWORK_WRITE", f"git {sub}", [remote],
            "🔴 sends objects to a remote. `development` and `origin` are both PUBLIC "
            "repositories, so this publishes",
            scope=em.NONLOCAL))
        return

    if sub == "rm":
        paths = [t for t in rest if not t.startswith("-")]
        findings.append(Finding("FILE_DELETE", "git rm", paths or [UNNAMED],
                                "deletes the working-tree file and stages the removal"))
        findings.append(Finding("NAMED_STAGING", "git rm", paths or [UNNAMED],
                                "stages the removal"))
        return

    if sub == "mv":
        paths = [t for t in rest if not t.startswith("-")]
        findings.append(Finding("FILE_RENAME", "git mv", paths or [UNNAMED],
                                "moves the working-tree file and stages the move"))
        return

    if sub == "apply":
        # The diff names its targets, but it lives in a FILE this guard cannot read.
        # A heredoc-fed diff is the one case where the targets are in the command text.
        targets: List[str] = []
        for body in heredocs:
            targets.extend(PATCH_TARGET.findall(body))
            targets.extend(DIFF_TARGET.findall(body))
        findings.append(Finding("PATCH_APPLY", "git apply", targets or [UNNAMED],
                                "writes every file the diff names"))
        return

    if sub in ("restore", "checkout", "switch"):
        paths = [t for t in rest if not t.startswith("-")]
        if "--" in rest:
            paths = rest[rest.index("--") + 1:]
        elif sub in ("checkout", "switch"):
            # 🔴 CREATING a branch and SWITCHING to one are different acts and the first
            # draft of this rule called both REF_MUTATION, which denied
            # `git checkout -b <new>` — the very command an actor runs to stop sharing
            # a branch with another session, and the remedy for the harm this
            # repository has actually suffered. A creation is additive: no ref moves,
            # no file changes, nothing is lost.
            #
            # Switching to an EXISTING branch is the destructive one, and the honest
            # name for it is not REF_MUTATION either — it rewrites every file in the
            # working tree that differs between the two commits, and the command names
            # none of them.
            if has_flag(argv, "-b", "-B", "-c", "-C", "--orphan"):
                return
            findings.append(Finding("FILE_WRITE", f"git {sub}", [UNNAMED],
                                    "rewrites every working-tree file that differs "
                                    "between the two commits, naming none of them"))
            return
        findings.append(Finding("FILE_WRITE", f"git {sub}",
                                paths or [UNNAMED],
                                "overwrites working-tree files from the index or a commit, "
                                "discarding what is there unread"))
        return

    if sub == "clone":
        # The destination is the second operand, or derived from the URL when absent.
        positional = [t for t in rest if not t.startswith("-")]
        findings.append(Finding("FILE_WRITE", "git clone",
                                positional[1:2] or [UNNAMED],
                                "writes a whole checkout into its destination"))
        return

    if sub == "reset":
        hard = has_flag(argv, "--hard")
        paths = [t for t in rest if not t.startswith("-")]
        if hard:
            findings.append(Finding("FILE_WRITE", "git reset --hard", [UNNAMED],
                                    "discards every uncommitted change in the working tree"))
        findings.append(Finding("REF_MUTATION", "git reset", ["HEAD"],
                                "moves HEAD and rewrites the index"))
        if paths and not hard:
            findings.append(Finding("NAMED_STAGING", "git reset <path>", paths,
                                    "unstages the paths it names"))
        return

    if sub == "clean":
        findings.append(Finding("FILE_DELETE", "git clean", [UNNAMED],
                                "deletes untracked files, which is where another actor's "
                                "in-flight work lives"))
        return

    if sub == "config":
        analyse_git_config(rest, findings)
        return

    if sub == "remote":
        verb = next((t for t in rest if not t.startswith("-")), "")
        if verb in ("", "show", "get-url", "-v", "--verbose"):
            return
        findings.append(Finding(
            "CONFIG_WRITE", f"git remote {verb}", ["<repository config>"],
            "rewrites the `remote.*` section of the repository config, which every "
            "worktree of this repository shares — and `remote.*.url` is where the "
            "objects of this repository would be sent",
            scope=em.GIT_COMMON_DIR))
        return

    # 🔴 Revision 12 · three git subcommands that RUN A PROGRAM the command names, and
    # one that writes into the object store. All four were ALLOW at revision 11 and all
    # four verified by Mirror. They are branches rather than config keys because the
    # program travels in an OPTION or an operand, where `is_execution_control_key` — which
    # reads keys — can never see it.
    if sub == "difftool":
        runner = flag_value(argv, "--extcmd", "-x")
        if runner is not None:
            findings.append(Finding(
                "EXECUTION_CONTROL", "git difftool --extcmd",
                [f"git difftool: {runner}"],
                "runs the program it names once per differing path",
                scope=em.RUNTIME_CONFIG))
        return

    if sub == "bisect":
        verb = next((t for t in rest if not t.startswith("-")), "")
        if verb == "run":
            after = rest[rest.index(verb) + 1:] if verb in rest else []
            findings.append(Finding(
                "EXECUTION_CONTROL", "git bisect run",
                [f"git bisect run: {after[0] if after else UNNAMED}"],
                "runs the program it names once per revision, and rewrites HEAD between "
                "each run",
                scope=em.RUNTIME_CONFIG))
        return

    if sub == "hash-object":
        if has_flag(argv, "-w", "--stdin-paths") or "-w" in rest:
            findings.append(Finding(
                "FILE_WRITE", "git hash-object -w", ["<git object store>"],
                "writes a loose object into the shared object store, which every "
                "worktree of this repository reads",
                scope=em.GIT_COMMON_DIR))
        return

    if sub == "archive":
        into = flag_value(argv, "-o", "--output")
        into = into or next((t.split("=", 1)[1] for t in rest
                             if t.startswith("--output=")), None)
        if into is not None:
            findings.append(Finding("FILE_WRITE", "git archive -o", [into],
                                    "writes the archive to its output operand"))
        return

    if sub == "bundle":
        verb = next((t for t in rest if not t.startswith("-")), "")
        if verb != "create":
            return
        after = rest[rest.index(verb) + 1:] if verb in rest else []
        into = next((t for t in after if not t.startswith("-")), UNNAMED)
        findings.append(Finding("FILE_WRITE", "git bundle create", [into],
                                "writes the bundle to the file it names"))
        return

    if sub in GIT_REF_SUBCOMMANDS:
        named = [t for t in rest if not t.startswith("-")]
        second = named[0] if named else ""

        # 🔴 A subcommand whose SECOND word decides. `git worktree list` and
        # `git stash list` are reads, and the first draft of this rule denied both —
        # `git worktree list` appears in this repository's own documented corpus, and
        # `git branch --show-current` is in the pre-flight every actor is told to run.
        # Classifying a family by its first word only is the same error as classifying
        # a command by its first word only, one level down.
        if sub in GIT_SUB_READ:
            if second in GIT_SUB_READ[sub]:
                return
        elif sub in ("branch", "tag"):
            # Listing (`git branch`, `git tag -l`, `--show-current`) reads. Naming a new
            # ref CREATES one, which destroys nothing. Only the destructive flags move
            # or remove a ref that already exists.
            if not has_flag(argv, *REF_DESTRUCTIVE_FLAGS):
                return
        elif sub == "worktree" and second == "add":
            # Additive, but it writes a whole checkout, so it is judged by where.
            findings.append(Finding("FILE_WRITE", "git worktree add",
                                    named[1:2] or [UNNAMED],
                                    "writes a whole checkout into its destination"))
            return

        # 🔴 `git update-ref <ref> <newvalue> [<oldvalue>]` names ONE ref. Revision 9
        # took every non-flag operand, so `git update-ref refs/heads/x deadbeef`
        # predicted a second REF_MUTATION on a ref called `deadbeef` — a target that
        # does not exist, cannot be observed, and would be reported MISSING by
        # `post_effect_verify` for every authorised update-ref there could ever be.
        if sub == "update-ref" and named:
            named = named[:1]
        # The verb families: `add`, `push`, `remove`, `show` are the subcommand's own
        # word, never a ref. See GIT_VERB_SUBCOMMANDS.
        if sub in GIT_VERB_SUBCOMMANDS and named:
            named = named[1:]

        # 🔴 A predicted ref is written in the namespace its subcommand implies, so that
        # the prediction and the observation are the same string. `git branch -D other`
        # predicted `other`; `post_effect_verify` observes `refs/heads/other` out of the
        # ref snapshot, and the two never met — a legitimate authorised deletion
        # verified INVALID. Branch and tag namespaces are qualified SEPARATELY and never
        # into each other: a `git tag -d` that moved a branch is a mismatch and must
        # stay one.
        named = [qualify_ref(sub, t) for t in named] if named else ["HEAD"]
        findings.append(Finding("REF_MUTATION", f"git {sub}", named,
                                "moves or deletes a ref, or rewrites history"))
        return

    if sub in GIT_READ_SUBCOMMANDS or not sub:
        return

    # 🔴 Positive listing, and this is the branch that makes it one. An unclassified
    # subcommand is not "probably a read": `git` grows, and the last three additions to
    # this repository's vocabulary were all mutations.
    findings.append(Finding("SHELL_OUT", f"git {sub}", [UNNAMED],
                            "a git subcommand this policy has not classified"))


def analyse_git_config(rest: List[str], findings: List[Finding]) -> None:
    """`git config` — a WRITE to a named file, judged as that file.

    The read forms stay read. Everything else writes, and WHICH file it writes decides
    the scope: the repository config is one file shared by every worktree
    (`GIT_COMMON_DIR`), `--global` is `~/.gitconfig` (a `RUNTIME_CONFIG` member since
    revision 11), `-f` is whatever it names.

    🔴 The key is judged SEPARATELY from the file, because the consequence of setting
    `core.hooksPath` does not depend on which file carries it.
    """
    argv = ["git", "config"] + rest
    if any(t in GIT_CONFIG_READ_FLAGS for t in rest):
        return
    positional = [t for t in operands(argv, "config") if t not in ("config",)]
    explicit_write = any(t in GIT_CONFIG_WRITE_FLAGS for t in rest)
    # `git config` with no positional and no write flag lists or errors; it never writes.
    if not explicit_write and len(positional) < 2:
        return
    key = positional[0] if positional else ""

    home = rc.cached().sources.get("home")
    if "--global" in rest:
        target, scope = (posixpath.join(home, ".gitconfig") if home else UNNAMED), None
    elif "--system" in rest:
        target, scope = "/etc/gitconfig", em.RUNTIME_CONFIG
    elif flag_value(argv, "-f", "--file") is not None:
        target, scope = flag_value(argv, "-f", "--file"), None
    else:
        target, scope = "<repository config>", em.GIT_COMMON_DIR
    findings.append(Finding("CONFIG_WRITE", "git config", [target],
                            "writes the git configuration file it is scoped to",
                            scope=scope))
    if is_execution_control_key(key) and flag_value(argv, "-f", "--file") is None:
        findings.append(Finding(
            "EXECUTION_CONTROL", f"git config {key}", [f"git config: {key}"],
            "sets a configuration key whose value is a PROGRAM git executes, or a "
            "location git looks for programs in — changing what runs, in every worktree "
            "of this repository or for this whole account",
            scope=em.RUNTIME_CONFIG))


def analyse_interpreter(argv: List[str], program: str, heredocs: List[str],
                        findings: List[Finding]) -> None:
    """`python3 -c …`, `perl -pi -e …`, `node -e …`, and the heredoc-fed forms."""
    if program == "perl" and has_flag(argv, "-i"):
        findings.append(Finding("IN_PLACE_EDIT", "perl -i",
                                operands(argv, "perl") or [UNNAMED],
                                "rewrites the files it names, unread"))
        return

    # 🔴 `-m MODULE` runs a whole program this guard has not read.
    #
    # Revision 8 read `-c`/`-e` bodies and ignored `-m` entirely, so
    # `python3 -m pip install -t framework/ pkg` arrived here as an interpreter with no
    # inline program and produced NO finding at all — allowed. The module is not the
    # command's argument, it IS the command, and the only module whose effect is
    # derivable from its name is one on a list someone checked.
    module = flag_value(argv, "-m", "--module")
    if module is not None:
        rest = argv[argv.index(module) + 1:] if module in argv else []
        if module in READ_ONLY_MODULES:
            # 🔴 Membership is per MODULE; write capability is per ARGV. Both are asked.
            model = MODULE_WRITE_MODEL.get(module)
            written = model(rest) if model else []
            if written:
                findings.append(Finding(
                    "FILE_WRITE", f"{program} -m {module}", written,
                    "this module writes an operand its NAME does not reveal — "
                    "membership of the read-only list is per module, write capability "
                    "is per argv"))
                return
            # The backstop, for every member including the ten that were measured
            # inert: an allowlisted module that NAMES a protected object and derived
            # nothing about it is exactly the silent-derivation shape.
            targets = [t for t in rest if not t.startswith("-")]
            if targets:
                findings.append(Finding(
                    "UNDERIVED_MODULE_OPERAND", f"{program} -m {module}", targets,
                    "an allowlisted module naming an object this guard derived no "
                    "effect on"))
            return
        # `python3 -m pip install --target X` — the module's own argv is a command in
        # its own right and the family rules above already read it.
        if base(module) in PACKAGE_MANAGERS or module.split(".")[0] in PACKAGE_MANAGERS:
            analyse_argv([module] + rest, [], heredocs, findings, depth=7)
            return
        findings.append(Finding("OPAQUE_PROGRAM", f"{program} -m {module}", [UNNAMED],
                                "a module run as a program, whose effect is not "
                                "derivable from its name"))
        return

    bodies: List[str] = []
    for index, token in enumerate(argv[1:], start=1):
        if token in INLINE_PROGRAM_FLAGS and index + 1 < len(argv):
            bodies.append(argv[index + 1])
    reads_stdin = any(t == "-" for t in argv[1:]) or len(argv) == 1
    if reads_stdin:
        bodies.extend(heredocs)

    for body in bodies:
        for match in SHELL_OUT.finditer(body):
            _analyse_shell_out(body, match.end(), findings)
        if not PROGRAM_WRITES.search(body):
            continue
        targets = [s for s in PROGRAM_STRING.findall(body) if "/" in s or "." in s]
        findings.append(Finding("PROGRAM_WRITE", f"{program} program", targets or [UNNAMED],
                                "an interpreted body that opens a file for writing"))


def _analyse_shell_out(body: str, start: int, findings: List[Finding]) -> None:
    """Judge what a program body hands to the shell, as the command it is.

    A literal list becomes an argv; a literal string becomes a command line. Anything
    computed is `UNNAMED`: a shell-out whose argument this guard cannot read is a shell-out
    it cannot clear.
    """
    cursor = start
    while cursor < len(body) and body[cursor] in " \t\n":
        cursor += 1
    if cursor >= len(body):
        return
    char = body[cursor]
    if char == "[":
        depth, index = 0, cursor
        while index < len(body):
            if body[index] == "[":
                depth += 1
            elif body[index] == "]":
                depth -= 1
                if depth == 0:
                    break
            index += 1
        parts = PROGRAM_STRING.findall(body[cursor : index + 1])
        if parts:
            analyse_command(shlex.join(parts), findings, depth=7)
        else:
            findings.append(Finding("SHELL_OUT", "subprocess", [UNNAMED],
                                    "a shell-out whose argv is computed"))
        return
    if char in "\"'":
        end = body.find(char, cursor + 1)
        if end != -1:
            analyse_command(body[cursor + 1 : end], findings, depth=7)
            return
    findings.append(Finding("SHELL_OUT", "subprocess", [UNNAMED],
                            "a shell-out whose argument is computed"))


ASSIGNMENT = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)=(.*)$", re.S)
VARIABLE = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}|\$([A-Za-z_][A-Za-z0-9_]*)")

#: Variables whose scratch-ness is definitional rather than derived from an assignment.
SCRATCH_VARIABLES = {"TMPDIR": "/tmp/", "TMP": "/tmp/", "TEMP": "/tmp/"}


def resolve_assignments(tokens: Sequence[str]) -> List[str]:
    """Expand `$NAME` using assignments made in this same command, and nothing else.

    `SC=/tmp/work; cmd > "$SC/out.json"` is fully derivable — the value is right there in
    the text being judged — and refusing it would deny the single most common way an
    agent writes to scratch space. A variable assigned in an *earlier* command, or by the
    environment, stays opaque: this resolves what the command says, never what the shell
    happens to know.
    """
    known = dict(SCRATCH_VARIABLES)
    out: List[str] = []
    for token in tokens:
        match = ASSIGNMENT.match(token)
        if match and not token.startswith("-"):
            known[match.group(1)] = _expand(match.group(2), known)
            out.append(token)
            continue
        out.append(_expand(token, known))
    return out


def _expand(token: str, known: dict) -> str:
    def replace(match: "re.Match[str]") -> str:
        name = match.group(1) or match.group(2)
        return known.get(name, match.group(0))
    return VARIABLE.sub(replace, token)


#: `$'git add -A'` is ANSI-C quoting: the `$` is syntax, not part of the word. Left in
#: place it made `bash -c $'git add -A'` parse as a program called `$git`.
ANSI_C_QUOTE = re.compile(r"\$(?=')")


def analyse_command(command: str, findings: List[Finding], depth: int = 0) -> None:
    # 🔴 Herestrings FIRST. `HEREDOC_START` reaches inside `<<<` and registers a phantom
    # heredoc with an empty body; extracting the herestring removes the span before that
    # can happen, so the two extractors never see the same characters.
    stripped, herestrings = extract_herestrings(command)
    stripped, heredocs = extract_heredocs(stripped)
    heredocs = heredocs + herestrings
    # A backslash-continuation joins two LINES into one COMMAND; every newline that
    # survives this substitution separates two commands. Order matters — heredoc bodies
    # are already out of the text, so a continuation inside one is untouched.
    stripped = CONTINUATION.sub(" ", stripped)
    stripped, subs = extract_substitutions(stripped)
    stripped = FD_DUP.sub(" ", stripped)
    stripped = FD_WRITE.sub(lambda m: " >> " if ">>" in m.group(0) else " > ", stripped)
    stripped = ANSI_C_QUOTE.sub("", stripped)
    for body in subs:
        analyse_command(body, findings, depth + 1)
    for argv, writes, piped_in in segments(resolve_assignments(lex(stripped))):
        analyse_argv(argv, writes, heredocs, findings, depth, piped_in)


# ── verdict ────────────────────────────────────────────────────────────────────────

DENY_STAGING = (
    "Blanket staging is blocked in this repository.\n\n"
    "`git add -A` / `git add .` / `git commit -a` / `… | xargs git add` stage everything "
    "in the working tree, including work another actor has in flight. That is not "
    "hypothetical here: it already happened, and put an unreviewed blind-derivation run "
    "inside a commit whose message described unrelated work.\n\n"
    "Stage the paths you actually changed:  git add <path> [<path> ...]\n"
    "Check first with:  git status --short"
)

DENY_SHELL_WRITE = (
    "Writing a repository file from the shell is blocked.\n\n"
    "The Write and Edit tools refuse to overwrite a file this session has not read. Doing "
    "the same write from Bash bypasses that guard — which is how a file authored and "
    "declared by another actor was destroyed unread. The shape does not matter: a "
    "redirection, `sed -i`, `tee`, `cp`, `mv`, `rm`, an interpreter one-liner and a shell "
    "wrapper around any of them are the same act.\n\n"
    "Use Write or Edit (they enforce read-before-overwrite), or invoke a committed script "
    "by name. Writes confined to /tmp or the scratchpad are allowed."
)

DENY_UNNAMED = (
    "A write whose target this command does not name is blocked.\n\n"
    "`xargs`, `find -exec`, a patch envelope and a bare redirection can all mutate files "
    "the command never mentions, so neither you nor a reviewer can tell from the command "
    "what it touched. That is the same defect as blanket staging.\n\n"
    "Name the paths, or do the write with Write/Edit, or confine it to /tmp or the "
    "scratchpad."
)

DENY_UNDERIVABLE = (
    "A write whose target cannot be resolved without running it is blocked.\n\n"
    "The target came from a substitution, a variable or a glob, so this guard cannot tell "
    "whether it lands in the repository or in scratch space. It answers no rather than "
    "assuming, which is the declared failure direction.\n\n"
    "Write the path literally, or do the write with Write/Edit, or confine it to /tmp or "
    "the scratchpad."
)

DENY_UNPARSEABLE = (
    "This command could not be parsed, so the guard cannot say what it writes, and "
    "answers no.\n\n"
)


DENY_REF = (
    "A command that moves git refs or rewrites history is blocked.\n\n"
    "`git reset --hard`, `git checkout -- .`, `git clean`, `git branch -D`, "
    "`git update-ref`, `git rebase` and `git stash` discard or relocate work that is not "
    "yours to discard: other actors share this repository's object store and its stash "
    "stack, and untracked files are exactly where their in-flight work lives.\n\n"
    "This needs REF_WRITE authority, which no runtime, role or lease grants. Ask the "
    "operator, or do the narrow thing: `git restore <path>` names what it touches."
)

DENY_NETWORK = (
    "A command that sends bytes off this machine is blocked.\n\n"
    "🔴 `development` and `origin` are BOTH public GitHub repositories. Pushing a branch "
    "to either one PUBLISHES it, and a bare `git push` goes to `origin`, which is a "
    "different repository from the one most work here targets.\n\n"
    "Publication is an operator act and needs PUBLISH authority, which is never granted "
    "by a runtime. Commit locally; the operator pushes."
)

DENY_PERMISSION = (
    "A command that changes file mode or ownership is blocked.\n\n"
    "`chmod` and `chown` change what every later actor may do to a file, and the change "
    "is invisible in a diff of its contents. That needs REF_WRITE authority.\n\n"
    "If a script needs to be executable, add it with the mode set, or ask the operator."
)

DENY_ARCHIVE = (
    "An archive extraction whose destination this command does not name is blocked.\n\n"
    "`tar -xf` and `unzip` write members the command never enumerates, and a member path "
    "may contain `..` and land outside wherever you thought it would. Neither you nor a "
    "reviewer can tell from the command what it wrote.\n\n"
    "Extract into a named directory outside the repository: `tar -xf a.tar -C /tmp/x`."
)

DENY_UNKNOWN_EFFECT = (
    "This command's effect could not be derived, so the guard cannot say what it would "
    "do, and answers no.\n\n"
    "UNKNOWN_EFFECT denies under every authority class. That is the whole fail-closed "
    "rule and it has no override: a command whose effect nobody can name is a command "
    "nobody can review.\n\n"
    "Write the command so its effect is readable, or invoke a committed script by name."
)

DENY_CONFINED = (
    "This command mutates state that belongs to the WHOLE repository, not to this "
    "worktree, and no authority class grants that from the shell.\n\n"
    "A peer's worktree, the shared checkout, and the shared `.git` — its config, its "
    "hooks, its refs, its worktree administration — are reachable from here because "
    "every worktree shares one object store. Being reachable is not being yours: the "
    "files under a peer worktree are another actor's uncommitted work, and a hook or a "
    "ref under the common dir changes what happens in every worktree at once.\n\n"
    "Read them freely — READ is granted in all three. To CHANGE one, the owning actor "
    "makes the change in its own worktree, or the operator does it deliberately. There "
    "is no rung of this ladder that reaches across."
)

DENY_NO_ASSIGNMENT = (
    "This actor's assigned worktree could not be established, so the guard cannot say "
    "which repository state is this actor's to change, and answers no.\n\n"
    "The assignment is SESSION-BOUND on purpose: it is read from the operator binding "
    "`LEGEND_ASSIGNED_WORKTREE`, from the runtime's own project directory, or from the "
    "payload envelope — never from `workdir`, `cwd` or a `-C` operand, all of which the "
    "model writes. With none of them readable there is no perimeter, and every mutation "
    "outside scratch space is refused.\n\n"
    "READS are unaffected, and so are writes to /tmp and the scratchpad. To restore "
    "write authority, start the session so the runtime sets its project directory, or "
    "have the operator set LEGEND_ASSIGNED_WORKTREE."
)

DENY_RUNTIME_CONFIG = (
    "This command mutates the configuration that decides whether this guard runs, and "
    "no authority class grants that from the shell.\n\n"
    "`~/.claude/settings.json` and the active Codex `config.toml` are where a runtime is "
    "told which PreToolUse hook to load, and the first of them also carries the `env` "
    "block this guard reads its own session binding out of. An actor that can rewrite "
    "them can switch the control off and then act unguarded, and nothing would look "
    "wrong until the next process start.\n\n"
    "Only the RESOLVED ACTIVE registration is confined — not `~/.claude` or `~/.codex` "
    "wholesale. Caches, sessions and scratch beside them stay writable.\n\n"
    "Changing a registration is an operator act on a separate governance surface. Inside "
    "the repository the surface already exists: edit with Write/Edit, stage the path by "
    "name, and let the commit be reviewed."
)

DENY_DELEGATE = (
    "This command hands the work to another agent runtime, and the guard cannot follow "
    "it there.\n\n"
    "A delegated session runs with its own permissions, its own hooks — or none — and "
    "its effects land in this repository without ever passing this policy. Allowing the "
    "handoff would authorise an unbounded effect set behind a single name, which is the "
    "one thing the effect model exists to refuse.\n\n"
    "Do the work in this session, or invoke a committed script by name. A delegated "
    "runtime becomes usable when it has demonstrated its OWN write floor — not before, "
    "and not by being invoked from a session that has one."
)

#: The authority a shell command is judged under when no attestation names another.
#: 🔴 Not a permissive default: it is the third rung of six, and it is the rung that
#: grants named staging and commit — because that is how work lands in this repository —
#: and nothing else inside it.
DEFAULT_AUTHORITY = "SHELL_DEFAULT"

#: Primitives whose hazard is history and other actors' uncommitted work, rather than
#: the named file. They derive FILE_WRITE / FILE_DELETE with an UNNAMED target, so
#: without this set they would be explained by the generic unnamed-target message.
DESTRUCTIVE_GIT = frozenset({
    "git reset --hard", "git clean", "git checkout", "git switch", "git restore",
    "git rebase", "git branch", "git update-ref", "git stash", "git notes",
    "git worktree", "git tag", "git reflog", "git cherry-pick", "git revert",
    "git merge", "git am", "git filter-branch", "git replace", "git gc", "git prune",
})

_SCOPE = {
    INSIDE_REPO: em.INSIDE_REPO,
    OUTSIDE_REPO: em.OUTSIDE_REPO,
    SCRATCH: em.SCRATCH,
    PEER_WORKTREE: em.PEER_WORKTREE,
    SHARED_CHECKOUT: em.SHARED_CHECKOUT,
    GIT_COMMON_DIR: em.GIT_COMMON_DIR,
    RUNTIME_CONFIG: em.RUNTIME_CONFIG,
    UNDERIVABLE: em.UNDERIVABLE,
    UNNAMED: em.UNNAMED,
}


def effects(command: object, cwd: Optional[str] = None,
            repo_root: Optional[str] = None,
            assigned: object = ASK_SESSION) -> Tuple[List[em.Effect], List[Finding],
                                                     Optional[str]]:
    """Derive the PREDICTED effect set for one command.

    Returns `(effects, findings, parse_error)`. `findings` are the policy's own
    reasoning, kept for characterisation; `effects` is the projection every other
    module in the bridge speaks. A parse failure yields a single `UNKNOWN_EFFECT`
    rather than an empty set — an empty set means "no mutation", and those are the two
    answers that must never be confused.
    """
    if not isinstance(command, str):
        return ([em.Effect(em.UNKNOWN_EFFECT, None, em.UNDERIVABLE, "input",
                           "the command is not text")], [], "it is not text.")

    findings: List[Finding] = []
    try:
        analyse_command(command, findings)
    except Unparseable as exc:
        return ([em.Effect(em.UNKNOWN_EFFECT, None, em.UNDERIVABLE, "parser", str(exc))],
                [], str(exc))

    derived: List[em.Effect] = []
    for finding in findings:
        for target in finding.targets:
            scope = finding.scope or _SCOPE.get(
                classify_target(target, cwd, repo_root, assigned), em.UNDERIVABLE)
            # 🔴 The silence rules are the only ones whose THRESHOLD is a scope, and
            # they are applied here because here is where the scope exists. Below the
            # threshold the operand is dropped entirely rather than emitted as a
            # harmless effect: `wc -l framework/x` must produce an EMPTY set, not a
            # `READ`, or every characterisation of an ordinary read changes shape.
            if finding.rule == "UNDERIVED_OPERAND":
                if scope not in UNDERIVED_OPERAND_SCOPES:
                    continue
            elif finding.rule == "UNDERIVED_MODULE_OPERAND":
                if scope not in UNDERIVED_MODULE_SCOPES:
                    continue
            # The index and HEAD are repository objects whatever path is named, so a
            # STAGE of a scratch path is still a mutation of the repository's index.
            # This runs only for a target that RESOLVED — UNNAMED and UNDERIVABLE fall
            # through unchanged, so `git rm` with no operand stays refused.
            if finding.effect in (em.STAGE, em.COMMIT) and scope in (em.SCRATCH,
                                                                     em.OUTSIDE_REPO):
                scope = em.INSIDE_REPO
            named = None if target in (UNNAMED, OPAQUE) else target
            derived.append(em.Effect(finding.effect, named, scope,
                                     finding.primitive, finding.detail))
    return derived, findings, None


#: 🔴 A stable, machine-readable name for WHY a command was refused — revision 10.
#:
#: The denial prose is for the reader. This is for the live probe, which has to
#: establish *which engine* answered before it can conclude anything, and cannot do that
#: from a sentence the legacy guard also contains. `test_runtime_diagnostics.py` asserts
#: that no code here appears anywhere in the legacy blob.
CODE_ALLOWED = ""
CODE_UNPARSEABLE = "UNPARSEABLE"
CODE_NO_ASSIGNMENT = "SESSION_ASSIGNMENT_UNDERIVABLE"
CODE_RUNTIME_CONFIG = "RUNTIME_CONFIG"
CODE_DELEGATE = "DELEGATE"
CODE_BLANKET_STAGING = "BLANKET_STAGING"
CODE_SHELL_WRITE = "SHELL_WRITE_IN_ASSIGNED_WORKTREE"
CODE_REF_WRITE = "REF_WRITE_REQUIRED"
CODE_NETWORK = "NETWORK_WRITE"
CODE_PERMISSION = "PERMISSION_CHANGE"
CODE_ARCHIVE = "ARCHIVE_EXTRACT"
CODE_UNKNOWN = "UNKNOWN_EFFECT"
CODE_UNNAMED = "UNNAMED_TARGET"
CODE_UNDERIVABLE = "UNDERIVABLE_TARGET"
CODE_SHORTFALL = "AUTHORITY_SHORTFALL"

_CONFINED_CODE = {
    em.PEER_WORKTREE: "CONFINED_PEER_WORKTREE",
    em.SHARED_CHECKOUT: "CONFINED_SHARED_CHECKOUT",
    em.GIT_COMMON_DIR: "CONFINED_GIT_COMMON_DIR",
}

def confined_code(scope: str) -> str:
    """The decision code for one confined scope. `UNKNOWN` for anything else, never a
    silent empty string: a probe that matched on `""` would match every denial."""
    return _CONFINED_CODE.get(scope, "CONFINED_UNKNOWN_SCOPE")


DECISION_CODES: Tuple[str, ...] = (
    CODE_UNPARSEABLE, CODE_NO_ASSIGNMENT, CODE_RUNTIME_CONFIG, CODE_DELEGATE,
    CODE_BLANKET_STAGING, CODE_SHELL_WRITE, CODE_REF_WRITE, CODE_NETWORK,
    CODE_PERMISSION, CODE_ARCHIVE, CODE_UNKNOWN, CODE_UNNAMED, CODE_UNDERIVABLE,
    CODE_SHORTFALL, *sorted(_CONFINED_CODE.values()),
)


def classify(command: object, cwd: Optional[str] = None, repo_root: Optional[str] = None,
             authority: str = DEFAULT_AUTHORITY,
             assigned: object = ASK_SESSION) -> Tuple[str, Optional[str], List[Finding]]:
    """Return `(outcome, reason, findings)` for one shell command.

    `outcome` is `ALLOWED`, `PROHIBITED` or `UNDERIVABLE`; `reason` is the denial text, or
    `None` when allowed. `findings` are the derived mutations, for characterisation.

    The decision itself is `effect_model.authorize`; everything below it is choosing
    which sentence to say. That split is the revision-8 change: the *rule* now lives in
    a table of effects and authorities that another module can also read, and this
    function no longer holds any policy of its own.
    """
    outcome, reason, _code, findings = adjudicate(
        command, cwd, repo_root, authority, assigned)
    return outcome, reason, findings


def adjudicate(command: object, cwd: Optional[str] = None,
               repo_root: Optional[str] = None, authority: str = DEFAULT_AUTHORITY,
               assigned: object = ASK_SESSION
               ) -> Tuple[str, Optional[str], str, List[Finding]]:
    """`classify`, plus the machine-readable code the live probe reads.

    Split out rather than widening `classify`'s tuple, because every existing caller
    unpacks three values and a fourth would have to be added to each of them for a field
    only the probe uses.
    """
    derived, findings, parse_error = effects(command, cwd, repo_root, assigned)
    if parse_error is not None:
        return UNDERIVABLE, DENY_UNPARSEABLE + parse_error, CODE_UNPARSEABLE, findings

    decision = em.authorize(derived, authority)
    if decision.authorized:
        return ALLOWED, None, CODE_ALLOWED, findings

    denied = [effect for effect, _ in decision.denials]
    kinds = {effect.kind for effect in denied}
    scopes = {effect.scope for effect in denied}
    primitives = {effect.primitive for effect in denied}

    # 🔴 The message follows the DERIVATION, not just the scope.
    #
    # `git clean -fd` derives FILE_DELETE with an UNNAMED target, and the generic
    # unnamed-target message is what an actor used to get: true, and silent about the
    # thing that makes `git clean` dangerous — that untracked files are exactly where
    # another actor's in-flight work lives. Same for `git reset --hard`. A denial that
    # does not name the hazard is a denial the reader will try to route around.
    # 🔴 Checked BEFORE every other sentence, including the destructive-git one.
    #
    # `git -C <peer> reset --hard` is both a history rewrite and a cross-worktree act,
    # and the reader needs the second: the first tells them to be careful with a command
    # they may repeat correctly in their own worktree, and only the second says the
    # target was never theirs. The most specific true sentence goes first.
    # 🔴 Before the cross-worktree sentence, because it is the more specific true one.
    # A reader told "this belongs to the whole repository" would look for the owning
    # actor; the file in question has no owning actor, it is the switch that decides
    # whether this guard runs at all, and the reader needs to be told that instead.
    if em.RUNTIME_CONFIG in scopes:
        return PROHIBITED, DENY_RUNTIME_CONFIG, CODE_RUNTIME_CONFIG, findings
    if scopes & em.CONFINED:
        confined = sorted(scopes & em.CONFINED)
        code = (_CONFINED_CODE[confined[0]] if len(confined) == 1
                else "CONFINED_MULTIPLE_SCOPES")
        return PROHIBITED, DENY_CONFINED, code, findings
    if em.DELEGATE in kinds:
        return PROHIBITED, DENY_DELEGATE, CODE_DELEGATE, findings

    # 🔴 Before the generic underivable-target sentence: when the SESSION ASSIGNMENT is
    # what could not be derived, every repository path is UNDERIVABLE at once, and the
    # message "write the path literally" is unactionable advice for a guard that lost
    # its perimeter. Two causes, two sentences.
    if em.UNDERIVABLE in scopes and session_topology(assigned) is None:
        return PROHIBITED, DENY_NO_ASSIGNMENT, CODE_NO_ASSIGNMENT, findings

    if primitives & DESTRUCTIVE_GIT:
        return PROHIBITED, DENY_REF, CODE_REF_WRITE, findings

    # Blanket staging keeps its own sentence and its own priority, because it is the
    # documented harm this policy was built for and its message is the one an actor has
    # already learned to read.
    if any(f.rule == "BLANKET_STAGING" for f in findings):
        return PROHIBITED, DENY_STAGING, CODE_BLANKET_STAGING, findings
    if any(e.kind in (em.WRITE, em.DELETE, em.RENAME) and e.scope == em.INSIDE_REPO
           for e in denied):
        return PROHIBITED, DENY_SHELL_WRITE, CODE_SHELL_WRITE, findings
    if em.NETWORK_WRITE in kinds:
        return PROHIBITED, DENY_NETWORK, CODE_NETWORK, findings
    if em.REF_MUTATION in kinds:
        return PROHIBITED, DENY_REF, CODE_REF_WRITE, findings
    if em.PERMISSION_CHANGE in kinds:
        return PROHIBITED, DENY_PERMISSION, CODE_PERMISSION, findings
    if em.ARCHIVE_EXTRACT in kinds:
        return PROHIBITED, DENY_ARCHIVE, CODE_ARCHIVE, findings
    if em.UNKNOWN_EFFECT in kinds:
        return UNDERIVABLE, DENY_UNKNOWN_EFFECT, CODE_UNKNOWN, findings
    if em.UNNAMED in scopes:
        return PROHIBITED, DENY_UNNAMED, CODE_UNNAMED, findings
    if em.UNDERIVABLE in scopes:
        return UNDERIVABLE, DENY_UNDERIVABLE, CODE_UNDERIVABLE, findings
    return (PROHIBITED, DENY_SHELL_WRITE + "\n\n" + decision.reason(),
            CODE_SHORTFALL, findings)


def verdict(command: object, cwd: Optional[str] = None, repo_root: Optional[str] = None,
            authority: str = DEFAULT_AUTHORITY,
            assigned: object = ASK_SESSION) -> Optional[str]:
    """Return a denial reason, or None to allow. `UNDERIVABLE` denies — it fails closed."""
    outcome, reason, _ = classify(command, cwd, repo_root, authority, assigned)
    return None if outcome == ALLOWED else reason


def authorized_effects(command: object, cwd: Optional[str] = None,
                       repo_root: Optional[str] = None,
                       authority: str = DEFAULT_AUTHORITY,
                       assigned: object = ASK_SESSION) -> List[em.Effect]:
    """The effect set an execution of this command is permitted to produce.

    Empty when the command is refused — a refused command is authorised for nothing,
    and `post_effect_verify` comparing against an empty set is exactly right: if it ran
    anyway, every effect it produced is EXTRA.
    """
    derived, _, parse_error = effects(command, cwd, repo_root, assigned)
    if parse_error is not None:
        return []
    return em.authorize(derived, authority).authorized_effects
