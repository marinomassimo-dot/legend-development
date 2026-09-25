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
  0  every run named held one model throughout
  1  at least one run changed model mid-run — its measurement does not isolate the context
  2  invalid invocation
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def census(path: Path) -> dict[str, Any]:
    """Per-turn model and context, from the assistant turns' own usage blocks."""
    turns: list[dict[str, Any]] = []
    prompt_chars = 0
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
        if row["changed_mid_run"]:
            for change in row["changes"]:
                lines.append(f"    🔴 MODEL CHANGED MID-RUN: {change['from']} → {change['to']} "
                             f"at {change['at']}")
    moved = [row for row in rows if row.get("changed_mid_run")]
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
    return 1 if any(row.get("changed_mid_run") for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
