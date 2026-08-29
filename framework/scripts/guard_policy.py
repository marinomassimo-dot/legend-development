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
}


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

SHELL_BINARIES = frozenset({"sh", "bash", "zsh", "dash", "ksh", "mksh", "ash", "fish", "busybox"})
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
PACKAGE_TARGET_FLAGS = ("-t", "--target", "--prefix", "--root", "--install-dir",
                        "--path", "--dest", "--destination")

#: Python `-m` modules that only read. Everything else run through `-m` is UNKNOWN_EFFECT.
#:
#: 🔴 The list is positive and short on purpose. `python3 -m pip install -t framework/ x`
#: was ALLOWED on revision 8 — `-m` was not read at all, so a module that installs into
#: the repository looked like an interpreter with no inline program. Enumerating the
#: WRITING modules instead would have to enumerate every module anyone might ever run.
READ_ONLY_MODULES = frozenset({
    "json.tool", "pydoc", "this", "site", "sysconfig", "platform", "timeit",
    "calendar", "base64", "gzip", "tokenize", "dis", "ast", "py_compile",
})


# ── write primitives, by argv[0] ───────────────────────────────────────────────────

#: Commands whose non-option operands are all written to.
WRITES_ALL_OPERANDS = frozenset({"tee", "truncate", "shred", "unlink", "mkfifo"})
#: Commands that read every operand but the last and write the last.
WRITES_LAST_OPERAND = frozenset({"cp", "mv", "install", "rsync", "ln"})
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
    # 🔴 Added in revision 9. Without these, `split -l 5 /tmp/a framework/part-` had `5`
    # read as an operand, which pushed the real prefix out of the position the rule looked
    # at and left the command ALLOWED. An option-value not listed here arrives in
    # `operands()` as if it were a path — the same defect that reported a chmod mode as a
    # write target, one family further on.
    "split": frozenset({"-a", "--suffix-length", "-b", "--bytes", "-C", "--line-bytes",
                        "-l", "--lines", "-n", "--number", "--additional-suffix",
                        "--filter", "-d", "--numeric-suffixes"}),
    "csplit": frozenset({"-f", "--prefix", "-b", "--suffix-format", "-n", "--digits"}),
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
    """
    bodies: List[str] = []
    lines = command.split("\n")
    out: List[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        out.append(line)
        starts = HEREDOC_START.findall(line)
        index += 1
        for _, delimiter in starts:
            body: List[str] = []
            while index < len(lines) and lines[index].strip() != delimiter:
                body.append(lines[index])
                index += 1
            index += 1  # consume the terminator
            bodies.append("\n".join(body))
    return "\n".join(out), bodies


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
    piped_in = False
    next_piped = False
    for token in tokens:
        if pending_redirect:
            writes.append(token)
            pending_redirect = False
            continue
        if token in REDIRECT_WRITE:
            pending_redirect = True
            continue
        if token in REDIRECT_READ:
            pending_redirect = False
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
    program = base(argv[0]) if argv else ""
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
    while argv and ASSIGNMENT.match(argv[0]) and not argv[0].startswith("-"):
        argv = argv[1:]
    if not argv:
        return
    program = base(argv[0])

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
        elsewhere = flag_value(argv, "-C", "--git-dir", "--work-tree")
        if elsewhere is not None:
            here: List[Finding] = []
            analyse_argv([argv[0]] + strip_wrapper_options(
                argv[1:], frozenset({"-C", "--git-dir", "--work-tree"})),
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
        findings.append(Finding("PATCH_APPLY", "patch", operands(argv, "patch") or [UNNAMED],
                                "writes the files the diff names"))
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
    "fetch", "remote", "config", "archive", "bundle", "instaweb", "citool", "gui",
})


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
        if module in READ_ONLY_MODULES:
            return
        # `python3 -m pip install --target X` — the module's own argv is a command in
        # its own right and the family rules above already read it.
        rest = argv[argv.index(module) + 1:] if module in argv else []
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
    stripped, heredocs = extract_heredocs(command)
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
