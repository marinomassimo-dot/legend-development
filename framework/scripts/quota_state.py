#!/usr/bin/env python3
"""What the runtime actually says about quota, with a timestamp — and when it says nothing.

WHY THIS EXISTS
---------------
Audited 2026-09-12 on Claude Code VS Code extension 2.1.269. A quota-aware stop/resume path needs
an answer to one question — how much of the 5-hour and 7-day windows is spent, and when do they
reset — and the runtime answers it on four different surfaces with four different guarantees:

    UI            the panel receives `rate_limit_event` carrying `rate_limit_info.unifiedWindows`,
                  relays it as `panel_usage_update`, and draws a bar per window with a percentage
                  and a reset time. Live, and not reachable by a local process.
    SOFTWARE      two surfaces, both indirect. `~/.claude.json.cachedUsageUtilization` carries
                  `utilization` and `resets_at` per window with its OWN `fetchedAtMs`; and a
                  transcript record carries `quotaLimits` only at the moment a request is REFUSED.
    MODEL         nothing. No tool returns quota, and there is no documented subcommand for it.
    STOP/RESUME   see `learning/plan/SLR-plan-20260911-quota-resume.md`.

🔴 THE CACHE IS NOT A LIVE READING, AND ITS FILE MTIME IS NOT ITS AGE. On 2026-09-12 at 21:08 UTC
`~/.claude.json` had been written 26 seconds earlier while `cachedUsageUtilization.fetchedAtMs` was
**23.5 hours old**, both windows' `resets_at` lay in the past, and a `weekly_scoped` entry stood at
90 % `critical` with `is_active: true`. Anything that reads the percentage without reading
`fetchedAtMs` will act on a number from the previous day. So this command reports the age FIRST and
refuses to present a stale reading as a measurement.

🔴 IT NEVER ESTIMATES QUOTA FROM CONTEXT TOKENS. Context size and quota consumption are different
quantities; a conversion between them would produce a number that looks measured and is not.

    python3 framework/scripts/quota_state.py read                 # one reading, with its age
    python3 framework/scripts/quota_state.py record --log <path>   # append it, timestamped
    python3 framework/scripts/quota_state.py read --max-age-min 30

Exit codes:
  0  a reading was found and is within --max-age-min
  1  a reading was found and is STALE, or a window's reset time has already passed
  2  no reading is available at all (key absent, file unreadable, malformed)
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

CONFIG = Path.home() / ".claude.json"
DEFAULT_MAX_AGE_MIN = 30.0


def _iso(epoch: float) -> str:
    return datetime.fromtimestamp(epoch, timezone.utc).isoformat(timespec="seconds")


def read_state(config: Path = CONFIG) -> dict:
    """The cached reading, its age, and every window — or an explicit absence."""
    out: dict = {"record_kind": "quota_state", "read_at": _iso(time.time()),
                 "source": str(config), "available": False, "windows": [], "notes": []}
    try:
        raw = json.loads(config.read_text(encoding="utf-8"))
    except FileNotFoundError:
        out["notes"].append("no config file at that path")
        return out
    except (json.JSONDecodeError, OSError) as problem:
        out["notes"].append(f"unreadable: {problem}")
        return out

    block = raw.get("cachedUsageUtilization")
    if not isinstance(block, dict):
        # 🔴 ABSENCE IS A RESULT, NOT A ZERO. The key is written by the client; a fresh profile, a
        # different config dir, or a client that has not yet fetched leaves it missing entirely.
        out["notes"].append("cachedUsageUtilization absent: the client has not cached a reading "
                            "here. That is not evidence that quota is unspent.")
        return out

    fetched = block.get("fetchedAtMs")
    if not isinstance(fetched, (int, float)):
        out["notes"].append("the cached block carries no fetchedAtMs: its age cannot be "
                            "established, so it must not be used as a measurement")
        return out

    now = time.time()
    out["available"] = True
    out["fetched_at"] = _iso(fetched / 1000)
    out["age_minutes"] = round((now - fetched / 1000) / 60, 1)
    out["config_mtime"] = _iso(config.stat().st_mtime)
    out["notes"].append("file mtime is NOT the reading's age: the config is rewritten for other "
                        "reasons while this block is not")

    utilization = block.get("utilization") or {}
    for name, window in sorted(utilization.items()):
        if not isinstance(window, dict) or window.get("utilization") is None:
            continue
        resets_at = window.get("resets_at")
        row = {"window": name, "percent": window.get("utilization"), "resets_at": resets_at,
               "reset_passed": None}
        if isinstance(resets_at, str):
            try:
                row["reset_passed"] = datetime.fromisoformat(resets_at).timestamp() < now
            except ValueError:
                row["resets_at"] = f"unparseable: {resets_at}"
        out["windows"].append(row)

    # The `limits` array is the panel's own view and carries a severity and an is_active flag that
    # the per-window dict does not. A scoped weekly limit can be the binding one while the two
    # headline windows look calm, so it is reported and never folded into them.
    for entry in utilization.get("limits") or []:
        if not isinstance(entry, dict):
            continue
        out["windows"].append({"window": f"limit:{entry.get('kind')}",
                               "group": entry.get("group"), "percent": entry.get("percent"),
                               "severity": entry.get("severity"), "resets_at": entry.get("resets_at"),
                               "is_active": entry.get("is_active"),
                               "scope": (entry.get("scope") or {}).get("model", {}).get("display_name")})
    return out


def verdict(state: dict, max_age_min: float) -> tuple[int, str]:
    if not state["available"]:
        return 2, "NO READING AVAILABLE — treat quota as unknown, never as unspent"
    if state["age_minutes"] > max_age_min:
        return 1, (f"STALE — the reading is {state['age_minutes']} minutes old "
                   f"(limit {max_age_min}); it is not a measurement of now")
    if any(row.get("reset_passed") for row in state["windows"]):
        return 1, ("A WINDOW'S RESET TIME HAS ALREADY PASSED in this reading — the cache predates "
                   "the reset and its percentages describe the previous window")
    return 0, "FRESH"


def render(state: dict, code: int, line: str) -> str:
    out = [f"QUOTA STATE — read {state['read_at']}", ""]
    if state["available"]:
        out.append(f"  reading fetched {state['fetched_at']} · age {state['age_minutes']} min "
                   f"· config mtime {state['config_mtime']}")
    out.append(f"  VERDICT: {line}")
    out.append("")
    for row in state["windows"]:
        flags = []
        if row.get("reset_passed"):
            flags.append("RESET ALREADY PASSED")
        if row.get("severity") and row["severity"] != "normal":
            flags.append(str(row["severity"]).upper())
        if row.get("is_active"):
            flags.append("BINDING")
        if row.get("scope"):
            flags.append(f"scope {row['scope']}")
        out.append(f"   {str(row['window']):24s} {str(row['percent']):>5}%  "
                   f"resets {row.get('resets_at')}" + ("  [" + " · ".join(flags) + "]" if flags else ""))
    out.append("")
    for note in state["notes"]:
        out.append(f"  note: {note}")
    out.append("  This command reads a cache the client writes. It never estimates quota from "
               "context size.")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("action", choices=("read", "record"))
    parser.add_argument("--config", default=str(CONFIG))
    parser.add_argument("--log", default="")
    parser.add_argument("--max-age-min", type=float, default=DEFAULT_MAX_AGE_MIN)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    state = read_state(Path(args.config))
    code, line = verdict(state, args.max_age_min)
    state["verdict"] = line
    state["exit"] = code

    if args.action == "record":
        if not args.log:
            parser.error("--log is required for record")
        path = Path(args.log)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(state, ensure_ascii=False) + "\n")
        print(f"appended to {path} · {line}")
        return code

    print(json.dumps(state, indent=1, ensure_ascii=False) if args.json
          else render(state, code, line))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
