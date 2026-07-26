#!/usr/bin/env python3
"""Resumable matrix runner for the optional exploratory MD helix screen."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


SCRIPT = Path(__file__).with_name("md_helix_screen.py")
DEFAULT_VARIANTS = ("WT", "Q230P", "P252A", "P282A")
DEFAULT_SEEDS = (1, 2, 3)


def parse_csv_strings(value: str) -> tuple[str, ...]:
    parsed = tuple(item.strip() for item in value.split(",") if item.strip())
    if not parsed:
        raise argparse.ArgumentTypeError("at least one value is required")
    return parsed


def parse_csv_ints(value: str) -> tuple[int, ...]:
    try:
        parsed = tuple(int(item.strip()) for item in value.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("seeds must be integers") from exc
    if not parsed or any(seed < 0 for seed in parsed):
        raise argparse.ArgumentTypeError("seeds must be non-negative")
    return parsed


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--variants",
        type=parse_csv_strings,
        default=DEFAULT_VARIANTS,
        help="comma-separated variants",
    )
    parser.add_argument(
        "--seeds",
        type=parse_csv_ints,
        default=DEFAULT_SEEDS,
        help="comma-separated random seeds",
    )
    parser.add_argument("--ns", type=float, default=10.0)
    parser.add_argument("--temp-k", type=float, default=400.0)
    parser.add_argument("--output-root", type=Path, default=Path("md-output/helix-screen"))
    parser.add_argument("--screen-script", type=Path, default=SCRIPT)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--implicit", action="store_true")
    parser.add_argument("--platform", default="auto")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="stop the matrix after the first failed run",
    )
    return parser.parse_args(argv)


def plan(args: argparse.Namespace) -> list[dict[str, object]]:
    return [
        {
            "variant": variant,
            "seed": seed,
            "directory": str(args.output_root / f"{variant}_seed{seed}"),
        }
        for variant in args.variants
        for seed in args.seeds
    ]


def command(args: argparse.Namespace, variant: str, seed: int) -> list[str]:
    result = [
        args.python,
        str(args.screen_script),
        "--variant",
        variant,
        "--seed",
        str(seed),
        "--ns",
        str(args.ns),
        "--temp-k",
        str(args.temp_k),
        "--output-root",
        str(args.output_root),
        "--platform",
        args.platform,
    ]
    if args.implicit:
        result.append("--implicit")
    return result


def append_log(log: Path, message: str) -> None:
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as handle:
        handle.write(message + "\n")


def execute(args: argparse.Namespace) -> dict[str, object]:
    if args.ns <= 0:
        raise ValueError("--ns must be positive")
    if not args.screen_script.is_file():
        raise ValueError(f"screen script does not exist: {args.screen_script}")
    matrix = plan(args)
    if args.dry_run:
        return {
            "status": "EXPLO",
            "mode": "dry-run",
            "planned_runs": len(matrix),
            "runs": [
                item
                | {
                    "command": command(
                        args, str(item["variant"]), int(item["seed"])
                    )
                }
                for item in matrix
            ],
        }

    log = args.output_root / "run.log"
    append_log(
        log,
        f"START_MATRIX {time.strftime('%Y-%m-%dT%H:%M:%S%z')} "
        f"runs={len(matrix)} ns={args.ns} temp_k={args.temp_k}",
    )
    results = []
    for item in matrix:
        variant, seed = str(item["variant"]), int(item["seed"])
        summary = Path(str(item["directory"])) / "summary.json"
        if summary.is_file():
            results.append(item | {"status": "skipped_complete"})
            append_log(log, f"SKIP {variant} seed={seed} summary_exists")
            continue
        invocation = command(args, variant, seed)
        append_log(log, f"START {variant} seed={seed}")
        with log.open("a", encoding="utf-8") as handle:
            completed = subprocess.run(
                invocation,
                check=False,
                stdout=handle,
                stderr=subprocess.STDOUT,
                text=True,
            )
        status = "complete" if completed.returncode == 0 else "failed"
        results.append(
            item | {"status": status, "returncode": completed.returncode}
        )
        append_log(
            log,
            f"{status.upper()} {variant} seed={seed} "
            f"returncode={completed.returncode}",
        )
        if completed.returncode != 0 and args.stop_on_error:
            break
    failures = sum(item["status"] == "failed" for item in results)
    append_log(
        log,
        f"END_MATRIX {time.strftime('%Y-%m-%dT%H:%M:%S%z')} "
        f"attempted={len(results)} failures={failures}",
    )
    return {
        "status": "EXPLO",
        "mode": "execute",
        "planned_runs": len(matrix),
        "processed_runs": len(results),
        "failures": failures,
        "runs": results,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        payload = execute(args)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(payload, indent=2))
    return 1 if payload.get("failures") else 0


if __name__ == "__main__":
    raise SystemExit(main())
