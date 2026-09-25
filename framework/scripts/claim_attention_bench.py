#!/usr/bin/env python3
"""Benchmark I · I2 — given the affected claim IS in context, does a model find it as reliably?

WHY THIS IS A SEPARATE COMMAND
------------------------------
I1 (`claim_retrieval_bench.py`) is frozen: its fixtures, seeds, algorithm and results were
committed before this file existed, and nothing here may move them. I2 reads I1's frozen output
and asks a different question — attention, not retrieval — so a model that reads poorly can
never be answered by retrieving differently, and a retriever that misses can never be excused
by a model that guesses well.

THE TWO ARMS DIFFER IN ONE THING
--------------------------------
  A  the whole `claim_registry_current.md` at the event's parent commit, verbatim;
  C  that file's preamble (the bytes before its first `##`, which `registry_records.py` ships
     with every answer) + the records PROGRESSIVE retrieved in I1, whole, in registry order.
Same system prompt, same task text, same `PMID` line, same first-pass observations (the I1
snippet seed). No target label reaches either arm. Every context is hashed before any run.

    python3 framework/scripts/claim_attention_bench.py contexts     # build + hash, no model call
    python3 framework/scripts/claim_attention_bench.py run --workers 4
    python3 framework/scripts/claim_attention_bench.py grade

`run` resumes: a job whose record is already in `i2_runs.jsonl` is not run again, so an
interrupted run is continued rather than restarted with a different sample.

`grade` is deterministic and blind: it reads an opaque job id, the fixture's target set and the
parsed answer; the arm is joined only after every run is scored. No model grades anything.

Exit codes: 0 done · 1 a job failed or an answer was unparseable · 2 invalid invocation.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import random
import re
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import registry_records  # noqa: E402

BENCH = ROOT / "framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL"
FIXTURES = BENCH / "fixtures.json"
I1_RESULTS = BENCH / "i1_results.json"
CONTEXTS = BENCH / "i2_contexts.json"
RUNS = BENCH / "i2_runs.jsonl"
GRADES = BENCH / "i2_grades.json"
CLAIMS = "disease-models/wwox/registries/claim_registry_current.md"

# Pre-registered (PREREGISTRATION.md § 5). Not changed after any output is read.
MODEL = "claude-opus-5-5"
REPETITIONS = 3
ORDER_SEED = 20260925
RELATIONSHIPS = ("supports / strengthens", "narrows / qualifies", "contradicts / weakens",
                 "requires review")
SYSTEM = ("You assist a biomedical knowledge system. You compare the first-pass reading of a new "
          "source with existing canonical claim records. Use only the text you are given. "
          "Answer with a single JSON object and nothing else.")
TASK = """## TASK
Identify which of the existing claims in CLAIM RECORDS, if any, are affected by the first-pass observations above: the observations would give a reason to change, narrow, qualify, strengthen, contradict or review that claim's current text.

For each affected claim give:
- "claim_id": exactly as in its heading, e.g. "CLAIM 007";
- "relationship": one of "supports / strengthens", "narrows / qualifies", "contradicts / weakens", "requires review";
- "reason": one or two sentences grounded in the observations.

If no existing claim is affected, return an empty list.

Return exactly one JSON object: {"affected": [{"claim_id": "...", "relationship": "...", "reason": "..."}]}"""
CLAIM_REF = re.compile(r"CLAIM\s*0*(\d{1,3})", re.I)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def show(rev: str, path: str) -> str:
    return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


def claim_records_at(rev: str) -> tuple[str, str, dict[str, str]]:
    """(whole file, preamble, id -> whole record) parsed by `registry_records` itself."""
    whole = show(rev, CLAIMS)
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / CLAIMS
        path.parent.mkdir(parents=True)
        path.write_text(whole, encoding="utf-8")
        preamble = registry_records.surface_preamble(path)
        records = {r.identity_id.upper(): r.text
                   for r in registry_records.parse_records(Path(tmp), "wwox",
                                                           "claim_registry_current")
                   if r.kind == "record"}
    return whole, preamble, records


def prompt(context: str, pmid: str, seed: str) -> str:
    return (f"## CLAIM RECORDS\n\n{context.rstrip()}\n\n## NEW SOURCE\n\nPMID {pmid}\n\n"
            f"## FIRST-PASS OBSERVATIONS\n(verbatim locator snippets recorded while the source "
            f"was open, before any comparison)\n\n{seed.strip()}\n\n{TASK}\n")


def contexts() -> int:
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    by_id = {f["fixture_id"]: f for f in fixtures["fixtures"]}
    by_id[fixtures["no_change_control"]["fixture_id"]] = fixtures["no_change_control"]
    i1 = json.loads(I1_RESULTS.read_text(encoding="utf-8"))
    eligible = [row for row in i1["rows"]
                if (row["class"] in ("STRONG", "USABLE_WITH_LIMITATION")
                    and row["strategies"]["PROGRESSIVE"]["all_targets_retrieved"])
                or row["class"] == "NO_CHANGE_CONTROL"]
    out: dict[str, Any] = {"_schema": "LEGEND Benchmark I · I2 contexts v1",
                           "i1_results_sha256": sha(I1_RESULTS.read_text(encoding="utf-8")),
                           "model": MODEL, "repetitions": REPETITIONS, "order_seed": ORDER_SEED,
                           "system_sha256": sha(SYSTEM), "task_sha256": sha(TASK),
                           "fixtures": []}
    cache: dict[str, tuple[str, str, dict[str, str]]] = {}
    for row in eligible:
        fixture = by_id[row["fixture_id"]]
        parent = fixture["parent"]
        cache.setdefault(parent, claim_records_at(parent))
        whole, preamble, records = cache[parent]
        chosen = [cid for cid in records if cid in row["strategies"]["PROGRESSIVE"]["candidates"]]
        missing = [t for t in fixture["targets"] if t not in chosen]
        if missing:
            raise ValueError(f"{row['fixture_id']}: target(s) {missing} not in Arm C context")
        arm_c = preamble.rstrip() + "\n\n" + "".join(records[cid] for cid in chosen)
        seed = fixture["seed"]["snippet_text"]
        entry = {"fixture_id": row["fixture_id"], "class": row["class"], "pmid": row["pmid"],
                 "parent": parent, "targets": fixture["targets"],
                 "relationship": fixture.get("relationship"),
                 "pmid_route_hit_all": all(t in row["strategies"]["CURRENT"]["candidates"]
                                          for t in fixture["targets"]) if fixture["targets"]
                 else None, "arms": {}}
        for arm, context, claim_ids in (("A", whole, list(records)), ("C", arm_c, chosen)):
            text = prompt(context, row["pmid"], seed)
            entry["arms"][arm] = {"claim_ids": claim_ids, "claim_records": len(claim_ids),
                                  "claim_context_bytes": len(context.encode("utf-8")),
                                  "prompt_bytes": len(text.encode("utf-8")),
                                  "prompt_sha256": sha(text)}
        out["fixtures"].append(entry)
    CONTEXTS.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(out['fixtures'])} fixtures x 2 arms x {REPETITIONS} repetitions = "
          f"{len(out['fixtures']) * 2 * REPETITIONS} jobs -> {CONTEXTS.relative_to(ROOT)}")
    return 0


def rebuild_prompt(entry: dict[str, Any], arm: str, fixtures: dict[str, Any]) -> str:
    """The prompt is rebuilt from the frozen inputs and must hash to what `contexts` recorded."""
    whole, preamble, records = claim_records_at(entry["parent"])
    ids = entry["arms"][arm]["claim_ids"]
    context = whole if arm == "A" else preamble.rstrip() + "\n\n" + "".join(records[c] for c in ids)
    text = prompt(context, entry["pmid"], fixtures[entry["fixture_id"]]["seed"]["snippet_text"])
    if sha(text) != entry["arms"][arm]["prompt_sha256"]:
        raise ValueError(f"{entry['fixture_id']}/{arm}: rebuilt prompt does not match its hash")
    return text


def jobs(ctx: dict[str, Any]) -> list[dict[str, Any]]:
    out = [{"fixture_id": e["fixture_id"], "arm": arm, "rep": rep}
           for e in ctx["fixtures"] for arm in ("A", "C") for rep in range(1, REPETITIONS + 1)]
    random.Random(ORDER_SEED).shuffle(out)
    for index, job in enumerate(out):
        # Opaque to the grader: the id carries neither the arm nor the fixture.
        job["job_id"] = "J" + sha(f"{ORDER_SEED}:{index}:{job['fixture_id']}:{job['arm']}:"
                                  f"{job['rep']}")[:10]
        job["order"] = index
    return out


def call_model(text: str, workdir: Path) -> dict[str, Any]:
    command = ["claude", "-p", "--model", MODEL, "--tools", "", "--strict-mcp-config",
               "--setting-sources", "", "--no-session-persistence", "--output-format", "json",
               "--system-prompt", SYSTEM]
    started = time.time()
    done = subprocess.run(command, input=text, capture_output=True, text=True, cwd=workdir,
                          timeout=900)
    elapsed = round(time.time() - started, 1)
    try:
        payload = json.loads(done.stdout)
    except json.JSONDecodeError:
        return {"ok": False, "elapsed_s": elapsed, "error": (done.stderr or done.stdout)[-500:]}
    return {"ok": not payload.get("is_error") and done.returncode == 0, "elapsed_s": elapsed,
            "payload": payload}


def run(workers: int, raw_dir: Path) -> int:
    ctx = json.loads(CONTEXTS.read_text(encoding="utf-8"))
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    by_fixture = {f["fixture_id"]: f for f in fixtures["fixtures"]}
    by_fixture[fixtures["no_change_control"]["fixture_id"]] = fixtures["no_change_control"]
    entries = {e["fixture_id"]: e for e in ctx["fixtures"]}
    done_ids = set()
    if RUNS.exists():
        done_ids = {json.loads(line)["job_id"] for line in RUNS.read_text().splitlines()
                    if line.strip() and json.loads(line).get("ok")}
    todo = [j for j in jobs(ctx) if j["job_id"] not in done_ids]
    prompts = {(fid, arm): rebuild_prompt(entries[fid], arm, by_fixture)
               for fid in entries for arm in ("A", "C")}
    raw_dir.mkdir(parents=True, exist_ok=True)
    lock = threading.Lock()
    failures = 0
    print(f"{len(todo)} jobs to run ({len(done_ids)} already recorded), {workers} workers",
          flush=True)

    def one(job: dict[str, Any]) -> bool:
        entry = entries[job["fixture_id"]]
        text = prompts[(job["fixture_id"], job["arm"])]
        with tempfile.TemporaryDirectory(dir=raw_dir) as work:
            result = call_model(text, Path(work))
            if not result["ok"]:        # one retry, recorded; a second failure is a failure
                result = call_model(text, Path(work)) | {"retried": True}
        payload = result.get("payload") or {}
        (raw_dir / f"{job['job_id']}.json").write_text(json.dumps(payload or result),
                                                       encoding="utf-8")
        record = {**job, "ok": result["ok"], "retried": result.get("retried", False),
                  "elapsed_s": result["elapsed_s"],
                  "prompt_sha256": entry["arms"][job["arm"]]["prompt_sha256"],
                  "prompt_bytes": entry["arms"][job["arm"]]["prompt_bytes"],
                  "claim_context_bytes": entry["arms"][job["arm"]]["claim_context_bytes"],
                  "claim_records": entry["arms"][job["arm"]]["claim_records"],
                  "model_usage": payload.get("modelUsage"), "usage": payload.get("usage"),
                  "answer": payload.get("result"), "error": result.get("error"),
                  "finished_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        with lock:
            with RUNS.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(f"{record['finished_at']} {job['job_id']} ok={record['ok']} "
                  f"{record['elapsed_s']}s", flush=True)
        return record["ok"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for ok in pool.map(one, todo):
            failures += 0 if ok else 1
    print(f"finished: {failures} failed")
    return 1 if failures else 0


def parse_answer(answer: str | None) -> tuple[list[dict[str, str]] | None, str]:
    if not answer:
        return None, "empty answer"
    text = answer.strip()
    fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.S)
    if fenced:
        text = fenced.group(1)
    start, end = text.find("{"), text.rfind("}")
    try:
        data = json.loads(text[start:end + 1])
    except (ValueError, json.JSONDecodeError) as error:
        return None, f"unparseable: {error}"
    items = data.get("affected")
    if not isinstance(items, list):
        return None, "no 'affected' list"
    out = []
    for item in items:
        match = CLAIM_REF.search(str(item.get("claim_id", "")))
        if match:
            out.append({"claim_id": f"CLAIM {int(match.group(1)):03d}",
                        "relationship": str(item.get("relationship", "")).strip().lower()})
    return out, ""


def grade() -> int:
    ctx = json.loads(CONTEXTS.read_text(encoding="utf-8"))
    entries = {e["fixture_id"]: e for e in ctx["fixtures"]}
    records = [json.loads(line) for line in RUNS.read_text().splitlines() if line.strip()]
    latest = {r["job_id"]: r for r in records}
    expected = {j["job_id"] for j in jobs(ctx)}
    unparseable = 0
    # PASS 1 — blind. The grader sees the job id, the target set and the answer, nothing else.
    scored: dict[str, dict[str, Any]] = {}
    for job_id in sorted(latest):
        record = latest[job_id]
        entry = entries[record["fixture_id"]]
        targets, label = entry["targets"], (entry["relationship"] or "").lower()
        answer, problem = parse_answer(record.get("answer")) if record.get("ok") else (None,
                                                                                      "run failed")
        if answer is None:
            unparseable += 1
            scored[job_id] = {"outcome": "OTHER", "problem": problem}
            continue
        named = {a["claim_id"]: a["relationship"] for a in answer}
        hit = [t for t in targets if t in named]
        extras = sorted(c for c in named if c not in targets)
        if targets:
            outcome = ("correct" if len(hit) == len(targets) else "partial" if hit
                       else "incorrect")
        else:
            outcome = "correct" if not named else "incorrect"
        errors: list[str] = []
        for target in targets:
            if target in named:
                if named[target] != label:
                    errors.append("RELATIONSHIP_WRONG")
            elif target not in entries[record["fixture_id"]]["arms"][record["arm"]]["claim_ids"]:
                errors.append("TARGET_NOT_IN_CONTEXT")
            elif extras:
                errors.append("WRONG_NEARBY_CLAIM")
            else:
                errors.append("TARGET_IN_CONTEXT_NOT_SELECTED")
        if extras:
            errors.append("EXTRA_UNSUPPORTED_CLAIMS")
        scored[job_id] = {"outcome": outcome, "targets_identified": len(hit),
                          "targets": len(targets), "extras": extras,
                          "relationship_matches": sum(named[t] == label for t in hit),
                          "errors": errors, "named": sorted(named)}
    # PASS 2 — unblind: join the arm only now.
    per_fixture: dict[str, dict[str, Any]] = {}
    for job_id, score in scored.items():
        record = latest[job_id]
        cell = per_fixture.setdefault(record["fixture_id"], {"A": [], "C": []})
        cell[record["arm"]].append({"job_id": job_id, "rep": record["rep"], **score,
                                    "input_tokens_total": token_total(record)})
    table, favour_a, favour_c, pooled = [], [], [], {"A": 0, "C": 0}
    taxonomy = {arm: {} for arm in ("A", "C")}
    for fid, cell in sorted(per_fixture.items()):
        entry = entries[fid]
        row: dict[str, Any] = {"fixture_id": fid, "class": entry["class"],
                               "targets": entry["targets"], "relationship": entry["relationship"],
                               "pmid_route_hit_all": entry["pmid_route_hit_all"]}
        for arm in ("A", "C"):
            runs = sorted(cell[arm], key=lambda r: r["rep"])
            ident = sum(r.get("targets_identified", 0) for r in runs)
            denom = max(1, len(entry["targets"])) * len(runs)
            score = (ident / denom if entry["targets"] else
                     sum(r["outcome"] == "correct" for r in runs) / max(1, len(runs)))
            row[arm] = {"outcomes": [r["outcome"] for r in runs], "score": round(score, 3),
                        "targets_identified": ident, "of": denom if entry["targets"] else None,
                        "relationship_matches": sum(r.get("relationship_matches", 0)
                                                    for r in runs),
                        "extras_per_run": [len(r.get("extras", [])) for r in runs],
                        "extras": sorted({c for r in runs for c in r.get("extras", [])}),
                        "claim_records": entry["arms"][arm]["claim_records"],
                        "claim_context_bytes": entry["arms"][arm]["claim_context_bytes"],
                        "input_tokens_total": [r["input_tokens_total"] for r in runs]}
            if entry["targets"]:
                pooled[arm] += ident
            for r in runs:
                for error in r.get("errors", []) + ([r["outcome"]] if r["outcome"] == "OTHER"
                                                    else []):
                    taxonomy[arm][error] = taxonomy[arm].get(error, 0) + 1
        if entry["targets"]:
            if row["A"]["score"] - row["C"]["score"] >= 0.5:
                favour_a.append(fid)
            if row["C"]["score"] - row["A"]["score"] >= 0.5:
                favour_c.append(fid)
        table.append(row)
    missing = sorted(expected - set(latest))
    out = {"_schema": "LEGEND Benchmark I · I2 grades v1", "grader": "deterministic exact "
           "CLAIM_ID match, blind to arm (arm joined after scoring)",
           "jobs_expected": len(expected), "jobs_recorded": len(latest), "jobs_missing": missing,
           "unparseable_or_failed": unparseable, "pooled_targets_identified": pooled,
           "pooled_denominator": sum(max(1, len(e["targets"])) * REPETITIONS
                                     for e in entries.values() if e["targets"]),
           "fixtures_favouring_A": favour_a, "fixtures_favouring_C": favour_c,
           "error_taxonomy": taxonomy, "rows": table, "blind_scores": scored}
    GRADES.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("jobs_recorded", "jobs_missing",
                                          "unparseable_or_failed", "pooled_targets_identified",
                                          "pooled_denominator", "fixtures_favouring_A",
                                          "fixtures_favouring_C", "error_taxonomy")}, indent=1))
    return 1 if missing or unparseable else 0


def token_total(record: dict[str, Any]) -> int | None:
    """Native input tokens of the main model call (uncached + cache read + cache write)."""
    usage = (record.get("model_usage") or {}).get(MODEL)
    if not usage:
        return None
    return (usage.get("inputTokens", 0) + usage.get("cacheReadInputTokens", 0)
            + usage.get("cacheCreationInputTokens", 0))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("action", choices=("contexts", "run", "grade"))
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--raw-dir", default="",
                        help="where the raw CLI payloads go (default: a temporary directory)")
    args = parser.parse_args(argv)
    try:
        if args.action == "contexts":
            return contexts()
        if args.action == "run":
            raw = Path(args.raw_dir) if args.raw_dir else Path(tempfile.mkdtemp(prefix="bench-i2-"))
            return run(args.workers, raw)
        return grade()
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(f"TOOL ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
