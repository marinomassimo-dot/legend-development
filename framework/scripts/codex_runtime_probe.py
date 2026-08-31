#!/usr/bin/env python3
"""Re-derive, from the INSTALLED runtime, every Codex fact `runtime_bridge.md` asserts.

Every runtime claim in that protocol was originally established by hand — reading schemas
out of a shipped binary, reading a session's rollout, running `codex doctor`. A fact
established by hand is a fact nobody else can check, and it decays silently when the
runtime is upgraded. This script re-derives all of them and prints each with its class, so
the protocol's tables can be *re-run* rather than believed.

    python3 framework/scripts/codex_runtime_probe.py            # every probe
    python3 framework/scripts/codex_runtime_probe.py --json
    python3 framework/scripts/codex_runtime_probe.py --sessions 5

It reads only. It never launches a Codex session — that is a spend under Annex J.4 — and it
is therefore incapable of answering the one question that matters most, `CODEX_HOOK_FIRES`.
It says so rather than approximating it.

🔴 **Absence here is `UNDERIVABLE`, never a negative.** If the binary cannot be found, the
answer is that the probe could not run, not that the runtime lacks the feature. The two are
printed differently on purpose.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

OBSERVED = "OBSERVED"
DOCUMENTED = "DOCUMENTED"
UNDERIVABLE = "UNDERIVABLE"

#: Where the platform binary lives inside the npm package, per platform triple.
VENDOR_GLOB = "node_modules/@openai/codex-*/vendor/*/bin/codex"

#: The per-hook trust gate, in the runtime's own words. Their PRESENCE is the claim; which
#: side of the gate a given registration sits on is not readable from here.
TRUST_STRINGS = (
    "New hook - review required",
    "Modified since last trusted - review required",
    "Managed hooks are always on",
    "hook needs review before it can run.",
    "bypass_hook_trust",
)

SESSION_ROOT = Path.home() / ".codex" / "sessions"
USER_CONFIG = Path.home() / ".codex" / "config.toml"


def find_binary():
    """The platform binary, not the node shim that execs it."""
    which = subprocess.run(["which", "codex"], capture_output=True, text=True)
    shim = which.stdout.strip()
    if not shim:
        return None, "`codex` is not on PATH"
    real = Path(shim).resolve()
    if real.stat().st_size > 10_000_000:
        return real, "resolved directly"
    for parent in [real.parent, *real.parents]:
        matches = sorted(parent.glob(VENDOR_GLOB))
        if matches:
            return matches[0], f"vendored under {parent}"
    return None, f"{real} is a shim and no vendored binary was found beside it"


def binary_strings(path: Path) -> str:
    out = subprocess.run(["strings", "-a", str(path)], capture_output=True, text=True)
    if out.returncode != 0:
        return ""
    return out.stdout


def extract_schema(blob: str, title: str):
    """Pull one JSON-schema object out of the binary by its `title`."""
    marker = f'"title": "{title}"'
    at = blob.find(marker)
    if at == -1:
        return None
    start = blob.rfind('{\n  "$schema"', 0, at)
    if start == -1:
        return None
    depth = 0
    for index in range(start, len(blob)):
        if blob[index] == "{":
            depth += 1
        elif blob[index] == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(blob[start : index + 1])
                except ValueError:
                    return None
    return None


MATCHER_LINE = re.compile(r"""matcher\s*=\s*["']([^"']+)["']""")


def codex_matchers(repo_root: Path) -> set:
    """The matcher VALUES `.codex/config.toml` declares, as whole strings."""
    path = repo_root / ".codex" / "config.toml"
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8", errors="replace")
    body = text.split("[hooks]", 1)[-1] if "[hooks]" in text else text
    return set(MATCHER_LINE.findall(body))


def probe_version():
    out = subprocess.run(["codex", "--version"], capture_output=True, text=True)
    if out.returncode != 0:
        return UNDERIVABLE, "codex --version failed"
    return OBSERVED, out.stdout.strip()


def probe_doctor():
    """`codex doctor --json` — and the negative that matters: it says nothing about hooks."""
    out = subprocess.run(["codex", "doctor", "--json"], capture_output=True, text=True)
    if out.returncode != 0 or not out.stdout.strip():
        return UNDERIVABLE, "codex doctor --json produced no report", {}
    try:
        report = json.loads(out.stdout)
    except ValueError:
        return UNDERIVABLE, "codex doctor --json is not JSON", {}
    checks = report.get("checks", {})
    hooky = [name for name in checks if "hook" in name.lower()]
    blob = json.dumps(report).lower()
    return OBSERVED, (
        f"{len(checks)} checks, overall={report.get('overallStatus')}, "
        f"codexVersion={report.get('codexVersion')}; "
        f"checks naming hooks: {len(hooky)}; "
        f"the word 'hook' occurs {blob.count('hook')} time(s) in the whole report"
    ), checks


def probe_directory_trust(repo_root: Path):
    if not USER_CONFIG.exists():
        return UNDERIVABLE, f"{USER_CONFIG} does not exist"
    text = USER_CONFIG.read_text(encoding="utf-8", errors="replace")
    trusted = re.findall(r'^\[projects\."([^"]+)"\]\s*\n\s*trust_level\s*=\s*"([^"]+)"',
                         text, re.MULTILINE)
    covering = [(path, level) for path, level in trusted
                if str(repo_root) == path or str(repo_root).startswith(path.rstrip("/") + "/")]
    if not covering:
        return OBSERVED, f"{len(trusted)} trusted project root(s), NONE covering {repo_root}"
    return OBSERVED, (f"{len(trusted)} trusted project root(s); "
                      + "; ".join(f"{p} -> {lv}" for p, lv in covering)
                      + " — inherited by every worktree beneath it")


CALL_TYPES = ("custom_tool_call", "function_call", "local_shell_call")


def read_rollout(path: Path):
    meta, tools = {}, {}
    try:
        # A context manager, not a bare `path.open(...)` in a for-clause: the corpus is 62
        # files and counting, and a leaked handle per rollout is a probe that stops being
        # able to read the corpus it is measuring.
        with path.open(encoding="utf-8", errors="replace") as handle:
            for line in handle:
                try:
                    record = json.loads(line)
                except ValueError:
                    continue
                payload = record.get("payload") or {}
                if not isinstance(payload, dict):
                    continue
                if record.get("type") == "session_meta" and not meta:
                    meta = payload
                if payload.get("type") in CALL_TYPES:
                    name = payload.get("name") or payload.get("type")
                    tools[name] = tools.get(name, 0) + 1
    except OSError:
        return None
    return {"rollout": path.name, "cli_version": meta.get("cli_version"),
            "originator": meta.get("originator"), "cwd": meta.get("cwd"), "tools": tools}


def probe_sessions(limit: int, repo_root: Path):
    """What tools real sessions actually call. The matcher list depends on this.

    🔴 **The whole corpus, not the latest session.** A count taken from one live rollout is
    a number that changes while you write it down — this script's first use recorded 20
    calls in a session that was still running and reached 27 an hour later. The claim that
    survives growth is the *proportion*: which tool names appear at all, and which appear
    zero times. That is what the matcher list actually depends on.
    """
    if not SESSION_ROOT.exists():
        return UNDERIVABLE, f"{SESSION_ROOT} does not exist", {}
    rollouts = sorted(SESSION_ROOT.rglob("rollout-*.jsonl"),
                      key=lambda p: p.stat().st_mtime, reverse=True)
    if not rollouts:
        return UNDERIVABLE, "no session rollouts on disk", {}

    everywhere, here, versions = {}, {}, {}
    local, recent = 0, []
    for path in rollouts:
        row = read_rollout(path)
        if row is None:
            continue
        for name, count in row["tools"].items():
            everywhere[name] = everywhere.get(name, 0) + count
            versions.setdefault(row["cli_version"], {})
            versions[row["cli_version"]][name] = (
                versions[row["cli_version"]].get(name, 0) + count)
        if str(repo_root.parent.parent) in (row["cwd"] or "") or "legend-public" in (row["cwd"] or ""):
            local += 1
            for name, count in row["tools"].items():
                here[name] = here.get(name, 0) + count
        if len(recent) < limit:
            recent.append(row)

    return OBSERVED, (f"{len(rollouts)} rollouts on disk, {local} with cwd inside this "
                      f"repository"), {
        "rollouts": len(rollouts), "in_this_repository": local,
        "tool_calls_everywhere": dict(sorted(everywhere.items(), key=lambda x: -x[1])),
        "tool_calls_in_this_repository": dict(sorted(here.items(), key=lambda x: -x[1])),
        "by_version": versions, "recent": recent,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--sessions", type=int, default=3)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    result = {}

    version_class, version = probe_version()
    result["CODEX_VERSION"] = {"class": version_class, "value": version}

    binary, how = find_binary()
    if binary is None:
        result["SCHEMAS"] = {"class": UNDERIVABLE, "value": how}
        result["TRUST_GATE"] = {"class": UNDERIVABLE, "value": how}
    else:
        blob = binary_strings(binary)
        if not blob:
            result["SCHEMAS"] = {"class": UNDERIVABLE, "value": "`strings` produced nothing"}
            result["TRUST_GATE"] = {"class": UNDERIVABLE, "value": "`strings` produced nothing"}
        else:
            schemas = {}
            for title in ("pre-tool-use.command.input", "pre-tool-use.command.output"):
                schema = extract_schema(blob, title)
                schemas[title] = (
                    {"required": schema.get("required", []),
                     "additionalProperties": schema.get("additionalProperties"),
                     "properties": sorted((schema.get("properties") or {}))}
                    if schema else None)
            decision = None
            output = extract_schema(blob, "pre-tool-use.command.output")
            if output:
                definitions = output.get("definitions", {})
                decision = (definitions.get("PreToolUsePermissionDecisionWire", {})
                            .get("enum"))
            result["SCHEMAS"] = {
                "class": DOCUMENTED if all(schemas.values()) else UNDERIVABLE,
                "value": schemas,
                "permissionDecision_enum": decision,
                "binary": str(binary), "resolution": how,
            }
            found = [s for s in TRUST_STRINGS if s in blob]
            result["TRUST_GATE"] = {
                "class": DOCUMENTED if found else UNDERIVABLE,
                "value": found,
                "note": "their PRESENCE is the claim; which side of the gate a given "
                        "registration is on is NOT readable from here",
            }

    doctor_class, doctor_detail, _ = probe_doctor()
    result["DOCTOR"] = {"class": doctor_class, "value": doctor_detail}

    trust_class, trust_detail = probe_directory_trust(repo_root)
    result["DIRECTORY_TRUST"] = {"class": trust_class, "value": trust_detail}

    session_class, session_detail, corpus = probe_sessions(args.sessions, repo_root)
    result["SESSIONS"] = {"class": session_class, "value": session_detail, **corpus}

    #: The registration is only a control over tools the runtime actually calls.
    declared = codex_matchers(repo_root)
    used_here = set((corpus.get("tool_calls_in_this_repository") or {}))
    used_ever = set((corpus.get("tool_calls_everywhere") or {}))
    result["MATCHER_COVERAGE"] = {
        "class": OBSERVED if corpus else UNDERIVABLE,
        "declared": sorted(declared),
        "used_in_this_repository": sorted(used_here),
        "UNCOVERED_here": sorted(used_here - declared),
        "declared_but_never_seen": sorted(declared - used_ever),
        "note": "a matcher for a tool no session ever calls is not a control; a tool called "
                "here and not declared is an uncovered path",
    }

    result["CODEX_HOOK_FIRES"] = {
        "class": UNDERIVABLE,
        "value": "NOT ANSWERABLE BY THIS SCRIPT. It requires a Codex session, which is a "
                 "spend under Annex J.4 and needs HUMAN_APPROVAL (TYPE: SPEND). See "
                 "framework/protocols/runtime_bridge.md § 5.1 for the one action and the "
                 "one test, and record the outcome at framework/state/codex_hook_probe.json.",
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print("CODEX RUNTIME PROBE — read-only, no session, no spend\n")
    for key, entry in result.items():
        print(f"[{entry['class']:<12}] {key}")
        value = entry.get("value", "")
        if key == "SCHEMAS" and isinstance(value, dict):
            for title, schema in value.items():
                if schema is None:
                    print(f"        {title}: NOT FOUND in the binary")
                    continue
                print(f"        {title}")
                print(f"          required             {', '.join(schema['required'])}")
                print(f"          additionalProperties {schema['additionalProperties']}")
            print(f"        permissionDecision enum  {entry.get('permissionDecision_enum')}")
        elif key == "SESSIONS":
            print(f"        {value}")
            for label in ("tool_calls_in_this_repository", "tool_calls_everywhere"):
                counts = entry.get(label) or {}
                head = ", ".join(f"{n}×{c}" for n, c in list(counts.items())[:8])
                print(f"        {label:<32} {head or '(none)'}")
            for row in entry.get("recent", []):
                tools = ", ".join(f"{n}×{c}" for n, c in sorted(row["tools"].items()))
                print(f"        - {row['rollout']}")
                print(f"          cli_version {row['cli_version']}  "
                      f"originator {row['originator']}")
                print(f"          cwd    {row['cwd']}")
                print(f"          tools  {tools or '(none)'}")
        elif key == "MATCHER_COVERAGE":
            for label in ("declared", "used_in_this_repository", "UNCOVERED_here",
                          "declared_but_never_seen"):
                shown = ", ".join(entry.get(label) or []) or "(none)"
                print(f"        {label:<26} {shown}")
            print(f"        🔴 {entry['note']}")
        elif isinstance(value, list):
            for item in value:
                print(f"        - {item}")
            if entry.get("note"):
                print(f"        🔴 {entry['note']}")
        else:
            for line in str(value).splitlines():
                print(f"        {line}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
