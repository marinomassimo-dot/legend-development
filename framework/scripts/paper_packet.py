#!/usr/bin/env python3
"""The technical half of a reading, prepared before the Scientist opens the paper.

WHY THIS EXISTS
---------------
A reading spends its first minutes re-discovering facts the repository already holds: which
artefacts exist and where, what a prior receipt covered, which acquisition routes were already
tried and how they failed, which checks apply to the surfaces at hand. Every one of those is a
lookup, and every one of them was being done by re-reading registries into the reading context —
the most expensive way to answer a question a command can answer. The 2026-09-09 sweep also ran
each check separately and read each check's full output, which is how a wave's closing costs as
much as its reading.

Two subcommands, one file, no new state:

    packet  — assemble what is known TECHNICALLY about one PMID, from the registries that
              already hold it. Compact by default, `--json` for a machine.
    check   — run the checks that apply to that PMID's actual surfaces, in one call, and print
              one line per check. Full output goes to a file under `files/` (gitignored) and is
              read only when a check has something to say.

🔴 THE FIREWALL, AND IT IS THE REASON THIS FILE IS SHORT
--------------------------------------------------------
`scientist_reading_modes.md` § 3.1: *"The reader receives a source packet — article binary,
article text surface, supplements … — and nothing else about the paper."* § 3.3 forbids reading
prior LEGEND output on the paper during a first pass declared blind.

So the packet carries **identity, bytes, coverage state, acquisition history and applicable
checks** — facts about the ARTEFACTS and about this repository's own reading state, which the
standing brief's M0 already requires the reader to look up by hand. It carries **no claim, no
dossier, no commit candidate, no prior locator, no prior proposition, no interpretation**. A
saving in context that arrives as anticipation of the laboratory's conclusions is not a saving;
it is contamination with a smaller token count, and `test_paper_packet.py` asserts the absence
rather than trusting this docstring.

Prior COVERAGE is in and prior CONCLUSIONS are out, and the line is not arbitrary: the brief's
M0 makes the coverage lookup mandatory (*"resume from the uncovered sections"*), while the
reading-modes protocol forbids the conclusions. This command automates the first and refuses the
second.

    python3 framework/scripts/paper_packet.py packet --pmid 29724996
    python3 framework/scripts/paper_packet.py packet --pmid 29724996 --json
    python3 framework/scripts/paper_packet.py check  --pmid 29724996

Exit codes:
  0  assembled / every applicable check screened something and none refused
  1  a check refused, errored, or established nothing — the three are printed apart and none
     of them is a pass, but all three mean this paper is not clear yet
  2  invalid invocation, or no such PMID anywhere in the workspace
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import fulltext_receipts as receipts  # noqa: E402

# Surfaces whose presence decides which checks apply. Nothing here is a scientific judgement:
# it is "there is a PDF, so the text-layer screens are runnable".
PDF_SUFFIXES = {".pdf"}
STRUCTURED_SUFFIXES = {".xml", ".nxml", ".html", ".htm"}
BINARY_SUPPLEMENT_SUFFIXES = {".pptx", ".xlsx", ".docx", ".zip"}

# 🔴 The firewall as a list a test can read. These surfaces carry the laboratory's conclusions
# about the paper, and the packet never opens them.
FORBIDDEN_SOURCES = (
    "disease-models/{disease}/registries/claim_registry_current.md",
    "disease-models/{disease}/registries/working_model_current.md",
    "disease-models/{disease}/research/fulltext_dossiers/",
    "disease-models/{disease}/research/commit_candidates/",
    "disease-models/{disease}/research/discovery_ledger_current.md",
)

COVERAGE_KEYS = ("abstract", "introduction", "methods", "results", "figures", "tables",
                 "discussion", "limitations", "supplementary", "references")


def manifest_path(root: Path, disease: str, pmid: str) -> Path:
    return root / "disease-models" / disease / "research" / "deepdive_manifests" / f"PMID{pmid}.json"


def load_manifest(root: Path, disease: str, pmid: str) -> dict[str, Any] | None:
    path = manifest_path(root, disease, pmid)
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def identity(root: Path, disease: str, pmid: str, manifest: dict | None) -> dict[str, Any]:
    """PMID, DOI and title only — the three fields that name the paper.

    Taken from the work manifest when one exists (it is the reading's own record of identity),
    and otherwise from the abstract corpus seed, which is a bibliographic census and carries no
    LEGEND conclusion. The paper registry is NOT read: it is where the laboratory writes what it
    thinks of the paper.
    """
    found = {"pmid": pmid, "doi": "", "title": "", "identity_source": "none"}
    if manifest:
        found["doi"] = str(manifest.get("doi") or "")
        found["title"] = str(manifest.get("title") or "")
        found["identity_source"] = "work manifest"
    if found["doi"] and found["title"]:
        return found
    seed = root / "disease-models" / disease / "research" / "corpus" / "pubmed_corpus.jsonl"
    if seed.is_file():
        for line in seed.read_text(encoding="utf-8", errors="replace").splitlines():
            if pmid not in line:
                continue
            try:
                record = json.loads(line)
            except ValueError:
                continue
            if str(record.get("pmid")) != pmid:
                continue
            found["doi"] = found["doi"] or str(record.get("doi") or "")
            found["title"] = found["title"] or str(record.get("title") or "")
            found["identity_source"] = (found["identity_source"] + " + abstract corpus seed"
                                        ).replace("none + ", "")
            break
    return found


def artefacts(root: Path, disease: str, pmid: str, manifest: dict | None) -> list[dict[str, Any]]:
    """Declared artefacts with their presence and digest agreement, plus undeclared files on disk.

    The digest question is the one a reader otherwise answers by hand and sometimes skips: is the
    file here the file the manifest fingerprinted?
    """
    rows: list[dict[str, Any]] = []
    declared_paths: set[str] = set()
    for item in (manifest or {}).get("source_artifacts") or []:
        if not isinstance(item, dict):
            continue
        rel = str(item.get("path") or "")
        declared_paths.add(rel)
        path = root / rel
        row = {"path": rel, "kind": str(item.get("kind") or ""), "declared": True,
               "present": path.is_file(), "digest": "",
               "recipe": bool(item.get("acquisition_recipe"))}
        if row["present"] and re.fullmatch(r"[a-f0-9]{64}", str(item.get("sha256") or "")):
            row["digest"] = "match" if sha256_file(path) == item["sha256"] else "MISMATCH"
        rows.append(row)
    for folder in ("fulltext", "figures", "supplement", "supplements"):
        base = root / "files" / folder
        if not base.is_dir():
            continue
        for path in sorted(base.rglob(f"*{pmid}*")):
            if not path.is_file():
                continue
            rel = str(path.relative_to(root))
            if rel in declared_paths:
                continue
            rows.append({"path": rel, "kind": "", "declared": False, "present": True,
                         "digest": "", "recipe": False})
    return rows


def prior_reading(root: Path, disease: str, pmid: str) -> dict[str, Any]:
    """What a previous receipt covered — the M0 lookup the standing brief already mandates.

    Coverage and depth only. The receipt's own findings are not read and are not in the packet.
    """
    state: dict[str, Any] = {"receipts": [], "depth": "none", "uncovered": [], "chain": "unread"}
    path = receipts.default_ledger_path(root, disease)
    if not path.is_file():
        return state
    try:
        ledger = receipts.load_ledger(path)
        state["chain"] = "ok"
    except Exception as error:  # noqa: BLE001 - a broken chain is a fact for the packet
        state["chain"] = f"UNREADABLE: {type(error).__name__}"
        return state
    standing = receipts.active_receipts(ledger)
    def names_this_paper(event: dict[str, Any]) -> bool:
        study = event.get("study_id")
        if isinstance(study, dict):
            return str(study.get("pmid") or "") == pmid
        return str(study or "") == pmid or str(event.get("pmid") or "") == pmid

    mine = [event for event in standing if names_this_paper(event)]
    for event in mine:
        coverage = event.get("coverage") or {}
        state["receipts"].append({
            "event_id": event.get("event_id"),
            "event_at": event.get("event_at"),
            "evidence_depth": event.get("evidence_depth"),
            "record_kind": event.get("record_kind"),
        })
        depth = str(event.get("evidence_depth") or "")
        if depth:
            state["depth"] = depth
        if isinstance(coverage, dict):
            # `read` and `not_present` are settled; `captions_only`, `unavailable` and
            # `not_read` are the sections a resumed reading owes, and the brief's M0 says so.
            state["uncovered"] = sorted(
                f"{key}={str(value).strip()}" for key, value in coverage.items()
                if str(value).strip() not in {"read", "not_present"})
    return state


def acquisition_history(root: Path, disease: str, pmid: str) -> list[dict[str, Any]]:
    """Routes already tried, with the verdict each returned — so none is tried blindly twice."""
    path = root / "disease-models" / disease / "research" / "retrieval_manifest.jsonl"
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if pmid not in line:
            continue
        try:
            record = json.loads(line)
        except ValueError:
            continue
        if str(record.get("pmid") or "") != pmid and pmid not in str(record.get("artifact_path") or ""):
            continue
        recipe = record.get("recipe") or {}
        # Two record kinds live in this ledger: a back-fill row that DECLARES the route an
        # artefact came from, and a replay row that RAN it and carries a verdict. Calling the
        # first "(no verdict)" reads as a failure; it is a declaration that was never replayed.
        verdict = str(record.get("verdict") or record.get("handoff") or "").strip()
        if not verdict:
            verdict = ("declared, never replayed" if recipe
                       else f"no recipe — {record.get('no_recipe_reason') or 'reason unrecorded'}")
        rows.append({
            "artifact_path": record.get("artifact_path"),
            "verdict": verdict[:90],
            "tier": recipe.get("tier") or ("derived" if recipe.get("derived") else ""),
            "acquired_on": recipe.get("acquired_on") or "",
            "url": recipe.get("resolved_url") or recipe.get("url") or "",
        })
    return rows


def applicable_checks(rows: list[dict[str, Any]], identity_row: dict[str, Any],
                      manifest: dict | None) -> list[dict[str, str]]:
    """Which checks this paper's surfaces make runnable. Presence of a surface, nothing more."""
    suffixes = {Path(str(row["path"])).suffix.lower() for row in rows if row["present"]}
    checks: list[dict[str, str]] = []
    if manifest is not None:
        checks.append({"name": "manifest validator",
                       "cmd": "deepdive_manifest.py --disease {disease} --pmid {pmid} "
                              "--verify-artifacts --require-current-schema"})
        checks.append({"name": "flag drift", "cmd": "manifest_flag_drift.py --pmid {pmid}"})
        checks.append({"name": "erratum scope",
                       "cmd": "erratum_scope_check.py --disease {disease} --pmid {pmid}"})
    if identity_row.get("doi"):
        checks.append({"name": "dependency integrity",
                       "cmd": "dependency_integrity.py screen --pmid {pmid}"})
    if suffixes & STRUCTURED_SUFFIXES:
        checks.append({"name": "genre discriminator",
                       "cmd": "genre_discriminator.py --artifact <the structured deposit>"})
    if suffixes & PDF_SUFFIXES:
        checks.append({"name": "text-surface intrusion",
                       "cmd": "text_surface_intrusion_check.py <the extracted text>"})
    if suffixes & BINARY_SUPPLEMENT_SUFFIXES:
        checks.append({"name": "binary supplement",
                       "cmd": "declare as supplement_binary; text through the verifier"})
    checks.append({"name": "undeclared locator revision",
                   "cmd": "locator_contradiction_audit.py --working-tree --fail-on-undeclared"})
    return checks


def build(root: Path, disease: str, pmid: str) -> dict[str, Any]:
    manifest = load_manifest(root, disease, pmid)
    identity_row = identity(root, disease, pmid, manifest)
    rows = artefacts(root, disease, pmid, manifest)
    packet = {
        "record_kind": "paper_work_packet",
        "pmid": pmid,
        "disease": disease,
        "identity": identity_row,
        "manifest": str(manifest_path(root, disease, pmid).relative_to(root)) if manifest else None,
        "artefacts": rows,
        "prior_reading": prior_reading(root, disease, pmid),
        "acquisition_history": acquisition_history(root, disease, pmid),
        "applicable_checks": applicable_checks(rows, identity_row, manifest),
        "excludes": list(FORBIDDEN_SOURCES),
        "firewall": ("technical state only — no claim, dossier, commit candidate, prior locator "
                     "or interpretation (scientist_reading_modes.md 3.1, 3.3)"),
    }
    return packet


def render(packet: dict[str, Any]) -> str:
    ident = packet["identity"]
    lines = [f"PAPER WORK PACKET — PMID {packet['pmid']}  ({packet['disease']})",
             f"  identity   : DOI {ident['doi'] or '(none recorded)'} · {ident['title'][:70] or '(no title recorded)'}"
             f"  [{ident['identity_source']}]",
             f"  manifest   : {packet['manifest'] or 'none — this is a first reading'}"]
    present = [row for row in packet["artefacts"] if row["present"]]
    absent = [row for row in packet["artefacts"] if not row["present"]]
    mismatch = [row for row in present if row["digest"] == "MISMATCH"]
    undeclared = [row for row in present if not row["declared"]]
    lines.append(f"  artefacts  : {len(present)} present, {len(absent)} declared-and-absent, "
                 f"{len(mismatch)} digest MISMATCH, {len(undeclared)} on disk and undeclared")
    for row in mismatch:
        lines.append(f"      MISMATCH {row['path']}")
    for row in undeclared:
        lines.append(f"      undeclared {row['path']}")
    for row in absent[:6]:
        lines.append(f"      absent {row['path']}")
    if len(absent) > 6:
        lines.append(f"      … and {len(absent) - 6} more absent")
    prior = packet["prior_reading"]
    lines.append(f"  prior read : depth={prior['depth']} · receipts={len(prior['receipts'])} "
                 f"· chain={prior['chain']}")
    if prior["uncovered"]:
        lines.append(f"      sections a resumed reading owes: {', '.join(prior['uncovered'])}")
    history = packet["acquisition_history"]
    if history:
        lines.append(f"  acquisition: {len(history)} route(s) already recorded")
        for row in history[:5]:
            lines.append(f"      {row['verdict'] or '(no verdict)'} · {row['tier'] or '-'} "
                         f"· {row['acquired_on'] or '-'} · {Path(str(row['artifact_path'] or '')).name}")
    else:
        lines.append("  acquisition: no route recorded — nothing has been tried and logged")
    lines.append(f"  checks     : {len(packet['applicable_checks'])} applicable "
                 f"(`paper_packet.py check --pmid {packet['pmid']}` runs the runnable ones)")
    for check in packet["applicable_checks"]:
        lines.append(f"      {check['name']}")
    lines.append(f"  firewall   : {packet['firewall']}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- check

def classify(code: int, output: str, headline: str) -> tuple[str, str]:
    """(state, the one line worth printing) for a finished check.

    🔴 A REFUSAL AND A REACH LIMIT ARE BOTH NON-ZERO AND ARE NOT THE SAME THING, and neither of
    them is a pass (MF-6). `manifest_flag_drift` exits 2 on every single-revision manifest —
    correctly: a flag cannot drift across one revision — and a reader who meets that red on every
    first reading learns to ignore reds. So the two are named apart, the reach limit carries the
    `missing=` clause the screen already wrote, and the caller's exit code stays non-zero for
    both, because in both cases something was not established.

    A pure function on purpose: the integration case that exercises it can only assert what the
    live corpus happens to produce, and a test that passes because nothing fired proves nothing.
    """
    if code == 0:
        return "ok", headline[:170]
    if "INSUFFICIENT_DATA" not in output:
        return "refused", headline[:170]
    missing = re.search(r"missing=([^|]+?)(?:\s+This is|$)", output, re.S)
    return "nothing-to-screen", (missing.group(1).strip() if missing else headline)[:170]


def _runnable(root: Path, disease: str, pmid: str, packet: dict[str, Any]) -> list[tuple[str, list[str]]]:
    """The checks whose command this file can build with no human choice left in it."""
    names = {check["name"] for check in packet["applicable_checks"]}
    jobs: list[tuple[str, list[str]]] = []
    if "manifest validator" in names:
        jobs.append(("manifest validator",
                     [sys.executable, str(HERE / "deepdive_manifest.py"), "--disease", disease,
                      "--pmid", pmid, "--verify-artifacts", "--require-current-schema"]))
        jobs.append(("flag drift",
                     [sys.executable, str(HERE / "manifest_flag_drift.py"), "--pmid", pmid]))
        jobs.append(("erratum scope",
                     [sys.executable, str(HERE / "erratum_scope_check.py"), "--root", str(root),
                      "--disease", disease, "--pmid", pmid]))
    jobs.append(("undeclared locator revision",
                 [sys.executable, str(HERE / "locator_contradiction_audit.py"), "--working-tree"]))
    return jobs


def run_checks(root: Path, disease: str, pmid: str, out_dir: Path | None = None) -> dict[str, Any]:
    packet = build(root, disease, pmid)
    out_dir = out_dir or (root / "files" / "check_runs")
    out_dir.mkdir(parents=True, exist_ok=True)
    detail = out_dir / f"PMID{pmid}.txt"
    started = time.monotonic()
    results = []
    with detail.open("w", encoding="utf-8") as handle:
        for name, argv in _runnable(root, disease, pmid, packet):
            began = time.monotonic()
            try:
                done = subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=600)
                code, output = done.returncode, (done.stdout + done.stderr)
            except (OSError, subprocess.SubprocessError) as error:
                code, output = 2, f"{type(error).__name__}: {error}"
            elapsed = time.monotonic() - began
            handle.write(f"\n===== {name} — exit {code} — {elapsed:.1f}s\n{' '.join(argv)}\n{output}\n")
            headline = next((line.strip() for line in reversed(output.splitlines())
                             if line.strip()), "(no output)")
            # 🔴 A REFUSAL AND A REACH LIMIT ARE BOTH NON-ZERO AND ARE NOT THE SAME THING, and
            # neither of them is a pass (MF-6). `manifest_flag_drift` exits 2 on every
            # single-revision manifest — correctly: a flag cannot drift across one revision —
            # and a reader who sees that red on every first reading learns to ignore reds. So
            # the compact line carries the `missing=` clause the screen already wrote, and the
            # summary counts the two classes apart. The exit code stays non-zero for both,
            # because the caller's contract is "something here was not established".
            state, line = classify(code, output, headline)
            results.append({"check": name, "exit": code, "seconds": round(elapsed, 1),
                            "state": state, "headline": line})
    try:
        shown = str(detail.relative_to(root))
    except ValueError:          # an --out-dir outside the workspace, as the suite uses
        shown = str(detail)
    return {"pmid": pmid, "detail": shown,
            "calls": len(results), "seconds": round(time.monotonic() - started, 1),
            "results": results}


def render_checks(report: dict[str, Any]) -> str:
    lines = [f"CHECKS — PMID {report['pmid']} · {report['calls']} call(s) · {report['seconds']}s "
             f"· detail: {report['detail']}"]
    marks = {"ok": "ok ", "nothing-to-screen": "·· ", "refused": "!! "}
    for row in report["results"]:
        lines.append(f"  {marks[row['state']]}{row['check']:<28} {row['headline']}")
    refused = [row for row in report["results"] if row["state"] == "refused"]
    void = [row for row in report["results"] if row["state"] == "nothing-to-screen"]
    if refused:
        lines.append(f"  OPEN THE DETAIL for: {', '.join(row['check'] for row in refused)}")
    if void:
        lines.append(f"  established nothing (not a pass): {', '.join(row['check'] for row in void)}")
    if not refused and not void:
        lines.append("  every applicable check screened something and none refused")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("action", choices=("packet", "check"))
    parser.add_argument("--pmid", required=True)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out-dir", default="")
    args = parser.parse_args(argv)

    if not re.fullmatch(r"\d{6,9}", args.pmid):
        parser.error("--pmid must be a PubMed identifier")
    root = Path(args.root).resolve()

    if args.action == "packet":
        packet = build(root, args.disease, args.pmid)
        known = (packet["manifest"] or packet["artefacts"] or packet["prior_reading"]["receipts"]
                 or packet["acquisition_history"] or packet["identity"]["doi"])
        print(json.dumps(packet, indent=1, ensure_ascii=False) if args.json else render(packet))
        return 0 if known else 2

    report = run_checks(root, args.disease, args.pmid,
                        Path(args.out_dir).resolve() if args.out_dir else None)
    print(json.dumps(report, indent=1, ensure_ascii=False) if args.json else render_checks(report))
    return 1 if any(row["exit"] != 0 for row in report["results"]) else 0


if __name__ == "__main__":
    sys.exit(main())
