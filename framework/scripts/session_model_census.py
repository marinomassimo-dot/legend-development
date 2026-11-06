#!/usr/bin/env python3
"""What model actually ran, per turn, and what the run cost — read from a transcript.

WHY THIS EXISTS
---------------
On 2026-09-12 a pilot compared a new context policy against a baseline and reported "same model,
same reading policy; one variable". It was not the same model: the baseline ran on
`claude-fable-5-1` and every session of the new condition ran on `claude-opus-5`. Nobody could
tell, because the dispatch said so and nothing read it back. A re-test the same day pinned the
model explicitly and the runtime still moved one producer to another model after six turns — a
requested model is a request, not a guarantee.

So: a comparison that claims to isolate the effect of the context reads its own model back, per
turn, and a run whose model changed mid-way does not support that claim. This command makes that
mechanical instead of remembered.

    python3 framework/scripts/session_model_census.py <transcript.jsonl> [more.jsonl ...]
    python3 framework/scripts/session_model_census.py --dir <directory of transcripts>

Exit codes:
  0  every run named held one model throughout, and ran the model its dispatch asked for
  1  at least one run changed model mid-run, or ran none of the model its dispatch asked for —
     its measurement does not isolate the context
  2  invalid invocation
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _dispatch_meta(path: Path) -> dict[str, Any]:
    """What the dispatch asked for, from the `agent-<id>.meta.json` that sits beside a delegate's transcript."""
    sibling = path.with_suffix(".meta.json")
    try:
        meta = json.loads(sibling.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {key: meta[key] for key in ("agentType", "description", "model", "effort") if key in meta}


def _asked_not_ran(meta: dict[str, Any], models: dict[str, int]) -> str:
    """The alias the dispatch asked for, when no turn ran a model carrying that name."""
    asked = str(meta.get("model") or "")
    if asked and not any(asked in str(name) for name in models):
        return asked
    return ""


def census(path: Path) -> dict[str, Any]:
    """Per-turn model and context, from the assistant turns' own usage blocks."""
    turns: list[dict[str, Any]] = []
    prompt_chars = 0
    efforts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = row.get("message") or {}
        if row.get("type") == "user" and not prompt_chars:
            content = message.get("content")
            prompt_chars = len(content) if isinstance(content, str) else len(json.dumps(content))
        usage = message.get("usage") if isinstance(message, dict) else None
        if row.get("type") != "assistant" or not usage:
            continue
        if row.get("effort") is not None:
            efforts[str(row["effort"])] = efforts.get(str(row["effort"]), 0) + 1
        turns.append({
            "at": row.get("timestamp", ""),
            "model": message.get("model"),
            "context": (usage.get("input_tokens", 0)
                        + usage.get("cache_creation_input_tokens", 0)
                        + usage.get("cache_read_input_tokens", 0)),
            "cache_creation": usage.get("cache_creation_input_tokens", 0),
            "cache_read": usage.get("cache_read_input_tokens", 0),
            "output": usage.get("output_tokens", 0),
        })
    meta = _dispatch_meta(path)
    if not turns:
        return {"transcript": str(path), "turns": 0, "models": {}, "changed_mid_run": False}

    models: dict[str, int] = {}
    for turn in turns:
        models[str(turn["model"])] = models.get(str(turn["model"]), 0) + 1
    changes = [(turns[index - 1]["model"], turn["model"], turn["at"])
               for index, turn in enumerate(turns) if index and turn["model"] != turns[index - 1]["model"]]
    return {
        "transcript": str(path),
        "turns": len(turns),
        "models": models,
        "changed_mid_run": bool(changes),
        "changes": [{"from": before, "to": after, "at": at} for before, after, at in changes],
        "first_turn_context": turns[0]["context"],
        "peak_context": max(turn["context"] for turn in turns),
        "prompt_chars": prompt_chars,
        "efforts": efforts,
        "dispatch": meta,
        "asked_not_ran": _asked_not_ran(meta, models),
        "totals": {key: sum(turn[key] for turn in turns)
                   for key in ("cache_creation", "cache_read", "output")},
    }


def render(rows: list[dict[str, Any]]) -> str:
    lines = ["SESSION MODEL CENSUS — read from the transcripts, never from the dispatch", ""]
    for row in rows:
        name = Path(row["transcript"]).name
        if not row["turns"]:
            lines.append(f"  {name}: no assistant turn with a usage block")
            continue
        models = " · ".join(f"{model} ×{count}" for model, count in
                            sorted(row["models"].items(), key=lambda pair: -pair[1]))
        lines.append(f"  {name}")
        lines.append(f"    turns {row['turns']} · {models}")
        lines.append(f"    birth context {row['first_turn_context']:,} tokens "
                     f"(prompt {row['prompt_chars']:,} chars) · peak {row['peak_context']:,}")
        totals = row["totals"]
        lines.append(f"    cache written {totals['cache_creation']:,} · cache read "
                     f"{totals['cache_read']:,} · output {totals['output']:,}")
        asked = row.get("dispatch") or {}
        efforts = " · ".join(f"{name} ×{count}" for name, count in sorted(row.get("efforts", {}).items()))
        if asked or efforts:
            lines.append(f"    asked model {asked.get('model', '—')} · asked effort "
                         f"{asked.get('effort', '—')} · effort read back {efforts or '—'}")
        if row.get("asked_not_ran"):
            lines.append(f"    🔴 ASKED {row['asked_not_ran']}, NO TURN RAN IT")
        if row["changed_mid_run"]:
            for change in row["changes"]:
                lines.append(f"    🔴 MODEL CHANGED MID-RUN: {change['from']} → {change['to']} "
                             f"at {change['at']}")
    moved = [row for row in rows if row.get("changed_mid_run")]
    counted = [row for row in rows if row["turns"]]
    if len(counted) > 1:
        lines.append("")
        lines.append(f"  TOTAL {len(counted)} run(s) · turns {sum(r['turns'] for r in counted):,} · cache written "
                     f"{sum(r['totals']['cache_creation'] for r in counted):,} · cache read "
                     f"{sum(r['totals']['cache_read'] for r in counted):,} · output "
                     f"{sum(r['totals']['output'] for r in counted):,}  (tokens as logged; not a share of any plan)")
    lines.append("")
    if moved:
        lines.append(f"  🔴 {len(moved)} of {len(rows)} run(s) changed model mid-run. A comparison "
                     "that claims to isolate the")
        lines.append("     effect of the context is not supported by those runs, whatever their "
                     "numbers say.")
    else:
        lines.append(f"  {len(rows)} run(s), each on one model throughout. That is a precondition "
                     "of a context comparison,")
        lines.append("  not evidence that one was run.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("transcripts", nargs="*", help="transcript .jsonl files")
    parser.add_argument("--dir", default="", help="a directory of transcripts")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    paths = [Path(item).resolve() for item in args.transcripts]
    if args.dir:
        paths.extend(sorted(Path(args.dir).resolve().glob("*.jsonl")))
    paths = [path for path in paths if path.is_file()]
    if not paths:
        parser.error("name at least one transcript, or a --dir that holds some")

    rows = [census(path) for path in paths]
    print(json.dumps(rows, indent=1, ensure_ascii=False) if args.json else render(rows))
    return 1 if any(row.get("changed_mid_run") or row.get("asked_not_ran") for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
