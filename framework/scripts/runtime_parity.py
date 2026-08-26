#!/usr/bin/env python3
"""The runtime-bridge falsifier: same actor, same worktree, same HEAD, different runtime.

`framework/protocols/runtime_bridge.md` states the property. This script is the thing that
can *refuse* it. Every check fails for exactly one reason, and the reason is printed, so a
red run tells the operator what broke rather than that something did.

    python3 framework/scripts/runtime_parity.py                  # the eight checks
    python3 framework/scripts/runtime_parity.py --bootstrap      # the Codex bootstrap contract
    python3 framework/scripts/runtime_parity.py --skills         # the skill-bridge proof
    python3 framework/scripts/runtime_parity.py --characterize   # the open guard gaps

Exit `0` only when every check passes. `--bootstrap` exits non-zero while any field an
actor owes before its first write is unresolved, because a bootstrap that reports a
problem and exits 0 is a bootstrap nobody reads.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "framework" / "scripts"
GUARD_ENTRY = SCRIPTS / "pre_tool_use_guard.py"

CLAUDE_REGISTRATION = ROOT / ".claude" / "settings.json"
CODEX_REGISTRATION = ROOT / ".codex" / "config.toml"
ROUTER = ROOT / "CLAUDE.md"
CODEX_ROUTER = ROOT / "AGENTS.md"
BRIDGE_PROTOCOL = ROOT / "framework" / "protocols" / "runtime_bridge.md"

# The chain AGENTS.md § 1 promises. If Codex cannot traverse it, it is not on the core.
ROUTER_CHAIN = (
    Path("framework/state/state_manifest_current.md"),
    Path("CLAUDE.md"),
    Path("BOOTSTRAP.md"),
    Path("governance/ANNEX_INDEX.md"),
    Path("roles"),
    Path("framework/protocols/index.md"),
)

ROLE_CONTRACTS = {
    "orchestrator": Path("roles/orchestrator.md"),
    "plan": Path("roles/plan.md"),
    "mirror": Path("roles/mirror.md"),
    "scientist": Path("roles/scientist.md"),
}

# One mandatory bootstrap skill, one scientific skill, one governance/review skill.
PROBE_SKILLS = ("legend-start", "legend-deepdive", "legend-locator-audit")

# Sources an ACTOR_ID may legitimately come from. A runtime, a session, a directory and a
# branch are not among them, and that is the whole of NO_SELF_ELECTION.
ACTOR_ID_ENV = "LEGEND_ACTOR_ID"

_spec = importlib.util.spec_from_file_location("pre_tool_use_guard", GUARD_ENTRY)
_guard = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = _guard
_spec.loader.exec_module(_guard)


# ── plumbing ──────────────────────────────────────────────────────────────────────

def _git(*args: str) -> str:
    out = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else ""


def _hook(payload: dict) -> str:
    """Run the shared engine exactly as a runtime would, and name its decision."""
    result = subprocess.run(
        [sys.executable, str(GUARD_ENTRY)], input=json.dumps(payload),
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return "ERROR"
    if not result.stdout.strip():
        return "allow"
    return json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"]


def claude_payload(command: str) -> dict:
    return {"hook_event_name": "PreToolUse", "tool_name": "Bash",
            "cwd": str(ROOT), "tool_input": {"command": command}}


def codex_payload(command: str) -> dict:
    return {"hook_event_name": "PreToolUse", "tool_name": "shell_command",
            "cwd": str(ROOT), "tool_input": {"cmd": command, "workdir": str(ROOT)}}


PROBE_COMMANDS = (
    "git add -A",
    "git add --all",
    'git commit -am "x"',
    "git status --short",
    "git add scripts/foo.py",
    "python3 - <<'PY'\nfrom pathlib import Path\nPath(\"x.md\").write_text(\"y\")\nPY",
    "python3 framework/scripts/legend_lint.py .",
    "rg --files",
)

GUARD_GAPS = (
    ("shell -c wrapper", 'bash -c "git add -A"'),
    ("sed -i", "sed -i '' 's/x/y/' FILE"),
    ("redirection >", "echo x > FILE"),
    ("append >>", "echo x >> FILE"),
    ("tee", "echo x | tee FILE"),
    ("cp over a tracked file", "cp /tmp/x FILE"),
    ("mv over a tracked file", "mv /tmp/x FILE"),
    ("python -c write", "python3 -c \"open('FILE','w')\""),
    ("perl -pi", "perl -pi -e 's/a/b/' FILE"),
)


class Result:
    def __init__(self) -> None:
        self.rows: list[tuple[str, bool, str]] = []

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.rows.append((name, ok, detail))

    @property
    def ok(self) -> bool:
        return all(ok for _, ok, _ in self.rows)

    def render(self) -> str:
        lines = []
        for name, ok, detail in self.rows:
            lines.append(f"{'PASS' if ok else 'FAIL':<5} {name:<34} {detail}")
        failed = [n for n, ok, _ in self.rows if not ok]
        lines.append("")
        lines.append(f"VERDICT: {'PASS' if self.ok else 'FAIL'}   "
                     f"{len(self.rows) - len(failed)}/{len(self.rows)} checks")
        if failed:
            lines.append("FAILED: " + ", ".join(failed))
        return "\n".join(lines)


# ── the eight checks ──────────────────────────────────────────────────────────────

def check_router_reachability(r: Result) -> None:
    if not CODEX_ROUTER.exists():
        r.add("ROUTER_REACHABILITY", False, "AGENTS.md is absent")
        return
    text = CODEX_ROUTER.read_text(encoding="utf-8")
    if "CLAUDE.md" not in text:
        r.add("ROUTER_REACHABILITY", False, "AGENTS.md no longer routes to CLAUDE.md")
        return
    missing = [str(p) for p in ROUTER_CHAIN if not (ROOT / p).exists()]
    if missing:
        r.add("ROUTER_REACHABILITY", False, "chain unresolvable: " + ", ".join(missing))
        return
    unlinked = [str(p) for p in ROUTER_CHAIN if p.name not in text and str(p) not in text]
    if unlinked:
        r.add("ROUTER_REACHABILITY", False, "chain member not named in AGENTS.md: "
              + ", ".join(unlinked))
        return
    r.add("ROUTER_REACHABILITY", True, f"{len(ROUTER_CHAIN)} surfaces named and present")


def check_role_contract_reachability(r: Result) -> None:
    missing = [f"{role}->{p}" for role, p in ROLE_CONTRACTS.items() if not (ROOT / p).exists()]
    if missing:
        r.add("ROLE_CONTRACT_REACHABILITY", False, ", ".join(missing))
        return
    unreadable = []
    for role, p in ROLE_CONTRACTS.items():
        try:
            if not (ROOT / p).read_text(encoding="utf-8").strip():
                unreadable.append(role)
        except OSError:
            unreadable.append(role)
    r.add("ROLE_CONTRACT_REACHABILITY", not unreadable,
          ", ".join(unreadable) or f"{len(ROLE_CONTRACTS)} contracts readable by path")


def skill_report() -> list[dict]:
    """One copy of each probed skill, reachable by path from the repository root."""
    tracked = _git("ls-files").splitlines()
    digests: dict[str, list[str]] = {}
    for rel in tracked:
        if rel.endswith("SKILL.md"):
            path = ROOT / rel
            if path.exists():
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                digests.setdefault(digest, []).append(rel)

    rows = []
    for name in PROBE_SKILLS:
        rel = f".claude/skills/{name}/SKILL.md"
        path = ROOT / rel
        present = path.exists()
        digest = hashlib.sha256(path.read_bytes()).hexdigest() if present else ""
        copies = digests.get(digest, []) if present else []
        rows.append({
            "skill": name,
            "path": rel,
            "sha256": digest[:16],
            "SOURCE_BYTES_IDENTICAL": present and len(copies) == 1,
            "CLAUDE_REACHABLE": present,        # .claude/skills is Claude's discovery root
            "CODEX_REACHABLE": present and os.access(path, os.R_OK),
            "NO_DUPLICATED_NORMATIVE_COPY": len(copies) <= 1,
            "copies": copies,
        })
    return rows


def check_skill_reachability(r: Result) -> None:
    rows = skill_report()
    bad = [row["skill"] for row in rows
           if not (row["CLAUDE_REACHABLE"] and row["CODEX_REACHABLE"]
                   and row["NO_DUPLICATED_NORMATIVE_COPY"])]
    r.add("SKILL_REACHABILITY", not bad,
          ", ".join(bad) or f"{len(rows)} probed, one copy each, readable by path")


def check_write_guard_parity(r: Result) -> None:
    divergent = []
    for command in PROBE_COMMANDS:
        a, b = _hook(claude_payload(command)), _hook(codex_payload(command))
        if a != b or a == "ERROR":
            divergent.append(f"{command.splitlines()[0][:28]!r}: claude={a} codex={b}")
    r.add("WRITE_GUARD_PARITY", not divergent,
          "; ".join(divergent) or f"{len(PROBE_COMMANDS)} commands, identical verdicts")


def check_authority_parity(r: Result) -> None:
    """A fingerprint that moves with the runtime would be authority following the host."""
    tool = ROOT / "governance" / "scripts" / "governance_fingerprint.py"
    if not tool.exists():
        r.add("AUTHORITY_PARITY", False, "governance_fingerprint.py is absent")
        return
    values = {}
    for runtime in ("claude", "codex"):
        env = {**os.environ, "LEGEND_RUNTIME": runtime}
        out = subprocess.run([sys.executable, str(tool), "compose", "--all"],
                             capture_output=True, text=True, env=env, cwd=str(ROOT))
        if out.returncode != 0:
            r.add("AUTHORITY_PARITY", False, f"compose failed under {runtime}")
            return
        values[runtime] = out.stdout
    if values["claude"] != values["codex"]:
        r.add("AUTHORITY_PARITY", False, "fingerprints differ between runtimes")
        return
    n = len([ln for ln in values["claude"].splitlines() if ln.strip()])
    r.add("AUTHORITY_PARITY", True, f"{n} role fingerprints, runtime-invariant")


def check_fail_closed(r: Result) -> None:
    cases = {
        "malformed stdin": "not json",
        "empty stdin": "",
        "no tool_name": json.dumps({"hook_event_name": "PreToolUse", "tool_input": {}}),
        "unknown tool": json.dumps({"hook_event_name": "PreToolUse", "tool_name": "Shell",
                                    "tool_input": {"command": "ls"}}),
        "wrong event": json.dumps({"hook_event_name": "PostToolUse", "tool_name": "Bash",
                                   "tool_input": {"command": "ls"}}),
        "uncextractable command": json.dumps({"hook_event_name": "PreToolUse",
                                              "tool_name": "shell_command",
                                              "tool_input": {"workdir": "/tmp"}}),
    }
    leaks = []
    for label, raw in cases.items():
        result = subprocess.run([sys.executable, str(GUARD_ENTRY)], input=raw,
                                capture_output=True, text=True)
        decision = ("allow" if not result.stdout.strip()
                    else json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"])
        if decision != "deny":
            leaks.append(f"{label}->{decision}")
    for path, label in ((CLAUDE_REGISTRATION, "claude registration"),
                        (CODEX_REGISTRATION, "codex registration")):
        if not path.exists():
            leaks.append(f"{label} absent")
    if not GUARD_ENTRY.exists():
        leaks.append("shared engine absent")
    r.add("FAIL_CLOSED_ON_MISSING_BRIDGE", not leaks,
          "; ".join(leaks) or f"{len(cases)} undecidable inputs all denied")


SELF_ELECTION = re.compile(
    r"ACTOR_ID\s*(?:=|:|is\s+)?\s*(?:derived|inferred|taken)\s+from\s+"
    r"(?:the\s+)?(?:runtime|session|worktree|branch|directory|cwd)",
    re.IGNORECASE,
)


def check_no_self_election(r: Result) -> None:
    offenders = []
    for rel in (_git("ls-files", "AGENTS.md", "CLAUDE.md", "BOOTSTRAP.md", "roles",
                     "framework/protocols", "governance").splitlines()):
        path = ROOT / rel
        if path.suffix != ".md" or not path.exists():
            continue
        if SELF_ELECTION.search(path.read_text(encoding="utf-8", errors="replace")):
            offenders.append(rel)
    declared = CODEX_ROUTER.read_text(encoding="utf-8") if CODEX_ROUTER.exists() else ""
    if "assigned by the operator" not in declared:
        offenders.append("AGENTS.md no longer states that ACTOR_ID is assigned")
    r.add("NO_SELF_ELECTION", not offenders,
          ", ".join(offenders) or "no artifact derives ACTOR_ID from its host")


def codex_hook_fires() -> tuple[str, str]:
    """The one thing no local, no-cost probe can reach. Reported, never assumed."""
    receipt = ROOT / "framework" / "state" / "codex_hook_probe.json"
    if not receipt.exists():
        return ("UNVERIFIED",
                "no session probe recorded; a registration that parses is not a control "
                f"(record one at {receipt.relative_to(ROOT)})")
    try:
        data = json.loads(receipt.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return "UNVERIFIED", f"probe receipt unreadable: {exc}"
    if data.get("blocked_blanket_staging") is True and data.get("codex_version"):
        return "OBSERVED", f"blocked under codex {data['codex_version']}"
    return "UNVERIFIED", "probe receipt does not record a refusal"


def check_no_runtime_authority_escalation(r: Result) -> None:
    problems = []
    if not CODEX_REGISTRATION.exists():
        problems.append("Codex has no registration, so the guard is Claude-only")
    else:
        text = CODEX_REGISTRATION.read_text(encoding="utf-8")
        if "pre_tool_use_guard.py" not in text:
            problems.append("the Codex registration does not name the shared engine")
        for tool in ("shell_command", "unified_exec"):
            if tool not in text:
                problems.append(f"no matcher for Codex tool {tool}")
    if CLAUDE_REGISTRATION.exists():
        settings = json.loads(CLAUDE_REGISTRATION.read_text(encoding="utf-8"))
        commands = json.dumps(settings.get("hooks", {}))
        if "guard_bash_command.py" not in commands and "pre_tool_use_guard.py" not in commands:
            problems.append("the Claude registration does not name the shared engine")
    status, detail = codex_hook_fires()
    if status != "OBSERVED":
        problems.append(f"CODEX_HOOK_FIRES={status}: {detail}")
    r.add("NO_RUNTIME_AUTHORITY_ESCALATION", not problems,
          "; ".join(problems) or "both adapters register one engine, firing observed")


CHECKS = (
    check_router_reachability,
    check_role_contract_reachability,
    check_skill_reachability,
    check_write_guard_parity,
    check_authority_parity,
    check_fail_closed,
    check_no_self_election,
    check_no_runtime_authority_escalation,
)


def run_battery() -> Result:
    r = Result()
    for check in CHECKS:
        check(r)
    return r


# ── bootstrap contract ────────────────────────────────────────────────────────────

def lease_state() -> tuple[str, str]:
    """🔴 `exit == 0` is the wrong predicate, in BOTH directions.

    `lease_state.py` has a four-valued exit contract, and a bootstrap that reduces it to
    ok/not-ok gets the answer wrong twice:

        0  clean
        1  --check found DISAGREEMENT / EXPIRED_WITHOUT_RENEWAL on a historical row
        2  the record could not be read at all — UNDERIVABLE
        3  more than one lease derives ACTIVE — the Annex I.3 singleton, checked in every
           mode before --check is consulted, and fatal

    Reading `rc != 0` as "cannot bootstrap" halts on `1`, which is a finding about a row
    written on 2026-08-18 and no reason for anyone to stop today. Reading `rc == 0` as
    "safe to proceed" is worse, because `3` is the one condition that must always stop a
    session and it is not `0`. So the exit code is consulted for what only it can say —
    `2` and `3` — and the question a bootstrap actually asks, *is a laboratory running*,
    is answered by the derived `ACTIVE` count, which is the tool's own recipe.
    """
    tool = ROOT / "framework" / "scripts" / "lease_state.py"
    if not tool.exists():
        return "UNDERIVABLE", "lease_state.py absent"
    out = subprocess.run([sys.executable, str(tool), "--check"],
                         capture_output=True, text=True, cwd=str(ROOT))
    if out.returncode == 3:
        return "SINGLETON_VIOLATION", "two leases derive ACTIVE — Annex I.3 broken, fatal"
    if out.returncode == 2:
        return "UNDERIVABLE", (out.stderr.strip().splitlines() or ["record unreadable"])[0]
    match = re.search(r"ACTIVE by derivation:\s*(\d+)", out.stdout)
    if not match:
        return "UNDERIVABLE", "derivation printed no ACTIVE count"
    count = int(match.group(1))
    findings = len(re.findall(r"^FINDING:", out.stdout, re.MULTILINE))
    tail = f"{count} ACTIVE by derivation, {findings} finding(s), rc={out.returncode}"
    if count == 0:
        return "NO_ACTIVE_LEASE", tail
    if count == 1:
        return "ACTIVE", tail
    return "SINGLETON_VIOLATION", tail


def bootstrap(actor_id: str | None) -> tuple[dict, list[str]]:
    runtime = os.environ.get("LEGEND_RUNTIME", "CODEX").upper()
    actor = actor_id or os.environ.get(ACTOR_ID_ENV)
    branch = _git("rev-parse", "--abbrev-ref", "HEAD")
    head = _git("rev-parse", "HEAD")
    dirty = _git("status", "--porcelain=v1")
    role_path = ROLE_CONTRACTS.get((actor or "").split("-")[0], None)

    fingerprint = "UNDERIVABLE"
    if role_path:
        role = (actor or "").split("-")[0]
        out = subprocess.run(
            [sys.executable, str(ROOT / "governance/scripts/governance_fingerprint.py"),
             "compose", "--role", role],
            capture_output=True, text=True, cwd=str(ROOT),
        )
        if out.returncode == 0 and out.stdout.strip():
            fingerprint = out.stdout.strip().split()[-1][:16]

    lease, lease_detail = lease_state()
    hook_status, hook_detail = codex_hook_fires()
    battery = run_battery()

    unavailable = [
        ".claude/skills — readable by path, NOT auto-applied",
        ".claude/agents — not dispatchable",
        "launch/legend_launch.sh — claude-bound, does not run",
        "SendMessage / ListAgents — Claude-side transport",
        "PubMed MCP connectors — not configured for this runtime",
    ]

    fields = {
        "RUNTIME": runtime,
        "ACTOR_ID": actor or "UNASSIGNED — operator must assign it; never self-elected",
        "WORKTREE": str(ROOT),
        "BRANCH": branch or "UNDERIVABLE",
        "HEAD": head or "UNDERIVABLE",
        "DIRTY_STATE": f"{len(dirty.splitlines())} path(s)" if dirty else "clean",
        "ROLE_CONTRACT": str(role_path) if role_path else "UNRESOLVED — follows ACTOR_ID",
        "GOVERNANCE_FINGERPRINT": fingerprint,
        "AUTHORITY_STATUS": ("ON_DEMAND_LEGEND_COLLABORATOR (body § 33.4) — a runtime "
                             "confers no authority; the operator and the lease do"),
        "LEASE_STATE": f"{lease} — {lease_detail}",
        "REQUIRED_GATES": ("legend_lint.py · public_release_gate.py · "
                           "run_release_regressions.py · fulltext_receipts.py verify"),
        "CLAUDE_ONLY_CAPABILITIES_UNAVAILABLE": unavailable,
        "CODEX_BRIDGE_STATUS": "PASS" if battery.ok else "FAIL",
        "WRITE_GUARD_STATUS": f"CODEX_HOOK_FIRES={hook_status} — {hook_detail}",
    }

    blockers = []
    if not actor:
        blockers.append("ACTOR_ID is unassigned")
    if not head:
        blockers.append("HEAD is underivable")
    if lease == "SINGLETON_VIOLATION":
        blockers.append("two ACTIVE leases")
    if not battery.ok:
        blockers.append("the parity battery does not pass")
    if hook_status != "OBSERVED":
        blockers.append("the Codex write guard is unverified — READ-ONLY until it is")
    return fields, blockers


# ── entry point ───────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--bootstrap", action="store_true")
    parser.add_argument("--skills", action="store_true")
    parser.add_argument("--characterize", action="store_true")
    parser.add_argument("--actor", default=None, help="ACTOR_ID, assigned by the operator")
    args = parser.parse_args()

    if args.characterize:
        print("GUARD_HARDENING_DEBT — shapes the policy does NOT stop, both runtimes\n")
        print(f"{'SHAPE':<26} {'CLAUDE':<8} {'CODEX':<8} PARITY")
        for label, command in GUARD_GAPS:
            a, b = _hook(claude_payload(command)), _hook(codex_payload(command))
            print(f"{label:<26} {a:<8} {b:<8} {'same' if a == b else 'DIVERGENT'}")
        print("\nThese predate the bridge and are identical on both sides. Widening the "
              "policy is GUARD_HARDENING_DEBT, a separate change.")
        return 0

    if args.skills:
        print("SKILL BRIDGE — one copy, reachable by path from both runtimes\n")
        ok = True
        for row in skill_report():
            print(f"{row['skill']}  ({row['path']}, sha {row['sha256']})")
            for key in ("SOURCE_BYTES_IDENTICAL", "CLAUDE_REACHABLE",
                        "CODEX_REACHABLE", "NO_DUPLICATED_NORMATIVE_COPY"):
                print(f"    {key:<32} {row[key]}")
                ok = ok and row[key]
            if len(row["copies"]) > 1:
                print("    COPIES: " + ", ".join(row["copies"]))
            print()
        return 0 if ok else 1

    if args.bootstrap:
        fields, blockers = bootstrap(args.actor)
        print("CODEX BOOTSTRAP CONTRACT — derived, never declared from memory\n")
        for key, value in fields.items():
            if isinstance(value, list):
                print(f"{key}:")
                for item in value:
                    print(f"    - {item}")
            else:
                print(f"{key:<38} {value}")
        print()
        if blockers:
            print("BLOCKED_BY_GOVERNANCE — resolve before any write:")
            for item in blockers:
                print(f"    - {item}")
            return 1
        print("READY")
        return 0

    result = run_battery()
    print("RUNTIME PARITY BATTERY — claude-code ↔ codex\n")
    print(result.render())
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
