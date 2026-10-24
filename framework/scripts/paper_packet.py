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
    surfaces — every figure, table and supplement surface: present, missing or unreadable, its
              real pixel size measured by two instruments, whether a better surface for THIS
              paper exists unused, which routes were already tried, and which page-adjudication
              crops are already on disk. It classifies nothing as marginal.
    rank    — the same figure-bearing surfaces, ORDERED BEST-FIRST FOR READING A FIGURE: measured
              pixel size, effective ppi where a printed size on disk makes it computable, and the
              route to open each one. It flags a figure that is probably part VECTOR — whose
              embedded raster is a fragment, so the PAGE must be rendered instead — and it never
              ranks a surface that is absent from disk. It names WHICH FIGURE each figure file
              is, from the JATS `<fig>` graphics rather than from the filename (which does not
              track the figure order), and says so when no JATS is on disk to decide.
              Writes nothing, gates nothing, exits 0.
    claim   — say "I am reading this PMID now" in the repository's common git directory, which
              every worktree sees; `packet` lists claims and every other worktree's in-flight
              manifest or staged receipt for the PMID. A marker, never a lock (N5, 2026-10-20).
              Exit 1 when someone else is already on it.
    check   — run the checks that apply to that PMID's actual surfaces, in one call, and print
              one line per check. Full output goes to a file under `files/` (gitignored) and is
              read only when a check has something to say.
    procedures — which SPECIALIST procedures this paper makes pertinent, from the same facts:
              the packet, the last `check` run's recorded signals, and conditions the reader
              observed and declares from a closed vocabulary (`--observed`). Three states per
              procedure and only one of them is "open it": `open` (a deterministic trigger
              fired), `not needed` (the data that would fire it exist and say no), and
              `to ascertain` (the data do not exist yet — and that is NOT a dismissal). The
              mandatory scientific method is never in this list: it is always loaded.

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
    python3 framework/scripts/paper_packet.py rank   --pmid 29724996
    python3 framework/scripts/paper_packet.py check  --pmid 29724996
    python3 framework/scripts/paper_packet.py procedures --pmid 29724996
    python3 framework/scripts/paper_packet.py procedures --pmid 29724996 --observed suspect_text_layer

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
import struct
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
import registry_records  # noqa: E402

# Surfaces whose presence decides which checks apply. Nothing here is a scientific judgement:
# it is "there is a PDF, so the text-layer screens are runnable".
PDF_SUFFIXES = {".pdf", ".txt"}   # a .txt here is a PDF-derived text layer, never an author surface
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
    declared_digests: set[str] = set()
    for item in (manifest or {}).get("source_artifacts") or []:
        if not isinstance(item, dict):
            continue
        rel = str(item.get("path") or "")
        declared_paths.add(rel)
        if re.fullmatch(r"[a-f0-9]{64}", str(item.get("sha256") or "").strip().lower()):
            declared_digests.add(str(item["sha256"]).strip().lower())
        path = root / rel
        row = {"path": rel, "kind": str(item.get("kind") or ""), "declared": True,
               "present": path.is_file(), "digest": "",
               "recipe": bool(item.get("acquisition_recipe"))}
        if row["present"]:
            declared = str(item.get("sha256") or "").strip().lower()
            if re.fullmatch(r"[a-f0-9]{64}", declared):
                row["digest"] = "match" if sha256_file(path) == declared else "MISMATCH"
            else:
                row["digest"] = "UNVERIFIABLE"   # absent or malformed: not "agree", not "mismatch"
        rows.append(row)
    for folder in ("fulltext", "figures", "supplement", "supplements"):
        base = root / "files" / folder
        if not base.is_dir():
            continue
        # 🔴 The PMID may be in the FILE name or in a DIRECTORY name above it. The first cut
        # matched `*{pmid}*` and skipped matched directories without descending, so the three
        # undeclared .pptx of PMID38499540_…_supplement/ and the two recovered figures under
        # figures/PMID20146584/ were invisible to the packet — the exact files the binary
        # supplement procedure exists for. Measured 2026-09-12, fixed at the root.
        for path in sorted(base.rglob("*")):
            if not path.is_file() or pmid not in str(path.relative_to(base)):
                continue
            rel = str(path.relative_to(root))
            if rel in declared_paths:
                continue
            row = {"path": rel, "kind": "", "declared": False, "present": True,
                   "digest": "", "recipe": False}
            # 🔴 A BYTE COPY OF A DECLARED CONTAINER IS NOT AN UNDECLARED CONTAINER. A re-acquisition
            # (PMID34268881, R2, 2026-10-22: files/supplement/PMID34268881_r2/ re-downloaded the six
            # Expanded View files already declared under _assets/) lands the same bytes under a new
            # path; the binary-supplement procedure exists so that a container is fingerprinted, and
            # these bytes already are. Only an exact sha256 match to a declared digest qualifies;
            # a different file, or the same name with different bytes, stays undeclared.
            if declared_digests and path.suffix.lower() in BINARY_SUPPLEMENT_SUFFIXES \
                    and sha256_file(path) in declared_digests:
                row["copy_of_declared"] = True
            rows.append(row)
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


CLAIMS_DIR = "legend-reading-claims"


def _git_out(cwd: Path, *args: str) -> str:
    done = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)
    return done.stdout if done.returncode == 0 else ""


def claims_dir(root: Path) -> Path | None:
    common = _git_out(root, "rev-parse", "--path-format=absolute", "--git-common-dir").strip()
    return Path(common) / CLAIMS_DIR if common else None


def claim(root: Path, pmid: str, actor: str, note: str = "") -> Path:
    """Say "I am reading this PMID now", where every worktree of the repository sees it.

    N5 (metabolic batch 2026-10-19): two Scientists read the same paper twice, and both
    duplicates were found only at landing; one actor had checked its peers' staging
    directories, and the peer staged afterwards. The marker is a file in the COMMON git
    directory — shared by every worktree, never committed, never a lock: nothing refuses on
    it, and `packet` shows it to the next reader of the same PMID. A stale marker costs one
    line of reading; a missing one cost an hour of duplicated reading.
    """
    directory = claims_dir(root)
    if directory is None:
        raise ValueError(f"{root} is not inside a git repository")
    target = directory / pmid / actor
    target.parent.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    target.write_text(json.dumps({"actor": actor, "pmid": pmid, "claimed_at": stamp,
                                  "worktree": str(root), "note": note}) + "\n",
                      encoding="utf-8")
    return target


def peer_work(root: Path, disease: str, pmid: str) -> list[dict[str, str]]:
    """Every other worktree's in-flight work on this PMID, plus the claim markers.

    In flight = a work manifest or a staged receipt for this PMID that is uncommitted in a
    worktree, or committed on its branch and not yet on main. Paths and states only: no
    content is read, so nothing crosses the packet's firewall.
    """
    rows: list[dict[str, str]] = []
    directory = claims_dir(root)
    if directory is not None and (directory / pmid).is_dir():
        for marker in sorted((directory / pmid).iterdir()):
            try:
                data = json.loads(marker.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                data = {}
            rows.append({"kind": "claim", "actor": marker.name,
                         "at": str(data.get("claimed_at", "")),
                         "where": str(data.get("worktree", "")),
                         "note": str(data.get("note", ""))})
    patterns = [f"disease-models/{disease}/research/deepdive_manifests/PMID{pmid}.json",
                f"disease-models/{disease}/research/receipt_staging/*/*-{pmid}-*.json"]
    here = root.resolve()
    current = None
    for line in _git_out(root, "worktree", "list", "--porcelain").splitlines() + [""]:
        if line.startswith("worktree "):
            current = {"path": line[9:], "branch": ""}
        elif line.startswith("branch ") and current is not None:
            current["branch"] = line[7:].removeprefix("refs/heads/")
        elif not line and current is not None:
            path = Path(current["path"])
            if path.resolve() != here and path.is_dir():
                pathspec = ["--", *[f":(glob){p}" for p in patterns]]
                for entry in _git_out(path, "status", "--porcelain", "--untracked-files=all",
                                      *pathspec).splitlines():
                    rows.append({"kind": "uncommitted", "actor": "", "at": "",
                                 "where": f"{path} [{current['branch'] or 'detached'}]",
                                 "note": entry[3:]})
                if current["branch"] and current["branch"] != "main":
                    for name in sorted(set(_git_out(path, "log", "main..HEAD", "--name-only",
                                                    "--format=", *pathspec).split())):
                        rows.append({"kind": "on branch, not on main", "actor": "", "at": "",
                                     "where": f"{path} [{current['branch']}]", "note": name})
            current = None
    return rows


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
        "technical_facts": technical_facts(root, disease, pmid, manifest, rows),
        "peer_work": peer_work(root, disease, pmid),
        "excludes": list(FORBIDDEN_SOURCES),
        # 🔴 WHICH TREE THIS PACKET DESCRIBES. Every other field here is a fact about a file at
        # a moment; without the commit, a packet read in a transcript tomorrow cannot be tied to
        # a checkout, and `DIRTY` says at least one of its inputs exists in no clone. Reported,
        # never refused: `refuse_if_dirty` is deliberately not called, because a packet is most
        # wanted exactly when a BATCH_COMMIT has the sources open.
        "repository": registry_records.repository_state(root, [
            manifest_path(root, disease, pmid),
            receipts.default_ledger_path(root, disease),
            root / "disease-models" / disease / "research" / "retrieval_manifest.jsonl",
            root / "disease-models" / disease / "research" / "corpus" / "pubmed_corpus.jsonl",
        ]),
        "firewall": ("technical state only — no claim, dossier, commit candidate, prior locator "
                     "or interpretation (scientist_reading_modes.md 3.1, 3.3)"),
    }
    packet["procedures"] = procedures(packet["technical_facts"])
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
    peers = packet.get("peer_work") or []
    if peers:
        lines.append(f"  PEER WORK  : {len(peers)} sign(s) that someone else is on this paper "
                     "— look before reading it twice")
        for row in peers[:8]:
            lines.append(f"      {row['kind']} · {row['actor'] or '-'} {row['at']} · "
                         f"{row['note'] or ''} · {row['where']}")
    else:
        lines.append(f"  peer work  : none in flight (claim it: `paper_packet.py claim --pmid "
                     f"{packet['pmid']} --actor <ACTOR_ID>`)")
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
    opened = [row for row in packet["procedures"] if row["state"] == OPEN]
    pending = [row for row in packet["procedures"] if row["state"] == TO_ASCERTAIN]
    lines.append(f"  procedures : {len(opened)} open, {len(pending)} to ascertain, "
                 f"{len(packet['procedures']) - len(opened) - len(pending)} not needed "
                 f"(`paper_packet.py procedures --pmid {packet['pmid']}` for the reasons and files)")
    for row in opened:
        lines.append(f"      OPEN {row['phase']:<6} {row['name']}")
    for row in pending:
        lines.append(f"      ??   {row['phase']:<6} {row['name']} — {row['to_ascertain']}")
    lines.append(f"  firewall   : {packet['firewall']}")
    lines.append(registry_records.repository_line(packet.get("repository", {})))
    return "\n".join(lines)


# --------------------------------------------------------------------------- surfaces

# 🔴 THE COST THIS ANSWERS IS REPEATED TECHNICAL WORK, NOT READING. The 2026-09-11 due-diligence
# record classifies 14 of the sweep's 52 incidents as visual or tabular, and its finding is the
# design of this inventory: *"The difference between the good and the bad figure readings is not
# care; it is whether a measurement had a second instrument to disagree with."* Two of those
# incidents are transport, not science, and both are answered here:
#   B1  bars counted at a 667 px PMC rendering that the publisher PDF holds as vector art. The
#       asset measures 667x385 on this host today; the reader started from the convenient asset
#       because nothing told it a better surface existed.
#   B15 `pdfimages` returned a 1447x1521 Separation LAYER that is not the figure, while the real
#       figure is a 697x565 JPEG. Bigger is not better; the layer is not the figure.
# Measured over the corpus on 2026-09-12: 175 raster figures, median width 974 px, 46 of them
# (26 %) at or below 700 px, and 61 above 1500 px. So there is no universal threshold to set —
# what is decidable is whether a BETTER SURFACE FOR THIS PAPER EXISTS AND WAS NOT USED.
#
# Nothing here classifies a surface as marginal, and nothing skips one. It reports what exists,
# what is missing, what cannot be read, what was already tried, and what a crop would cost that
# is already on disk. The scientific class of a surface — DETERMINANTE, QUALIFICANTE,
# ILLUSTRATIVA, NON CLASSIFICABILE — is the reader's declaration after inspection, never this
# file's guess: `scientist_standing_brief.md` M2 holds that rule, and a file name never decides it.

RASTER_SUFFIXES = {".png", ".jpg", ".jpeg"}
# Below this width a full-figure raster cannot carry a bar count or a blot lane reliably: the
# 667 px incident is the measured case, and it is a PROMPT to check for a better surface, never
# a verdict on the figure. A panel crop is legitimately small, so the flag names the reason.
THIN_RASTER_PX = 700


def raster_size_from_header(path: Path) -> tuple[int, int] | None:
    """Pixel size straight from the container header — stdlib only, so it always runs."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) >= 24:
        width, height = struct.unpack(">II", data[16:24])
        return int(width), int(height)
    if data[:2] == b"\xff\xd8":
        index = 2
        while index < len(data) - 9:
            if data[index] != 0xFF:
                index += 1
                continue
            marker = data[index + 1]
            if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD,
                          0xCE, 0xCF}:
                height, width = struct.unpack(">HH", data[index + 5:index + 9])
                return int(width), int(height)
            if marker in {0xD8, 0xD9} or 0xD0 <= marker <= 0xD7:
                index += 2
                continue
            try:
                segment = struct.unpack(">H", data[index + 2:index + 4])[0]
            except struct.error:
                return None
            index += 2 + segment
    return None


def raster_size_second_instrument(path: Path) -> tuple[int, int] | None:
    """The disagreeing instrument. Absent PyMuPDF is reported, never silently treated as agreement.

    🔴 Both `file(1)`'s first `NxN` and a PyMuPDF PAGE rectangle report DENSITY or POINTS, not
    pixels — each was tried on 2026-09-12 and each produced a different, wrong table. `Pixmap`
    is the one that reports pixels, and the header parser above is what proves it.
    """
    try:
        import pymupdf                                    # noqa: PLC0415 - optional by design
    except ImportError:
        return None
    try:
        pixmap = pymupdf.Pixmap(str(path))
        return int(pixmap.width), int(pixmap.height)
    except Exception:                                     # noqa: BLE001 - a broken image is a fact
        return None


def acquisition_by_artefact(root: Path, disease: str, pmid: str) -> dict[str, list[str]]:
    """Routes already tried per artefact, so a failed one is not repeated without a reason."""
    out: dict[str, list[str]] = {}
    for row in acquisition_history(root, disease, pmid):
        name = Path(str(row.get("artifact_path") or "")).name
        if name:
            out.setdefault(name, []).append(str(row.get("verdict") or ""))
    return out


def surfaces(root: Path, disease: str, pmid: str) -> dict[str, Any]:
    """Every figure, table and supplement surface: present, missing, or unreadable — and why."""
    manifest = load_manifest(root, disease, pmid)
    rows = artefacts(root, disease, pmid, manifest)
    tried = acquisition_by_artefact(root, disease, pmid)
    kinds = {str(item.get("path") or ""): str(item.get("kind") or "")
             for item in (manifest or {}).get("source_artifacts") or [] if isinstance(item, dict)}
    has_pdf = any(Path(str(row["path"])).suffix.lower() == ".pdf" and row["present"] for row in rows)
    adjudications = sorted(
        path.name for path in
        (root / f"disease-models/{disease}/research/page_adjudications/PMID{pmid}").glob("*")
        if path.is_file()) if (root / f"disease-models/{disease}/research/page_adjudications/PMID{pmid}").is_dir() else []

    out: list[dict[str, Any]] = []
    for row in rows:
        path = Path(str(row["path"]))
        if path.suffix.lower() not in RASTER_SUFFIXES | BINARY_SUPPLEMENT_SUFFIXES | {".pdf", ".tif", ".tiff"}:
            continue
        kind = kinds.get(str(path), "")
        entry: dict[str, Any] = {
            "path": str(path), "kind": kind, "declared": row["declared"], "present": row["present"],
            "digest": row["digest"], "width": 0, "height": 0, "measured": "",
            "flags": [], "already_tried": tried.get(path.name, []),
        }
        if not row["present"]:
            entry["flags"].append("ABSENT — unreadable, and its relevance stays unknown")
            out.append(entry)
            continue
        if path.suffix.lower() in RASTER_SUFFIXES:
            first = raster_size_from_header(root / path)
            second = raster_size_second_instrument(root / path)
            if first:
                entry["width"], entry["height"] = first
                entry["measured"] = ("two instruments agree" if second == first
                                     else f"DISAGREEMENT header={first} pixmap={second}"
                                     if second else "header only (PyMuPDF absent)")
            else:
                entry["measured"] = "unreadable header"
                entry["flags"].append("UNREADABLE — the container header does not parse")
            # 🔴 A PAGE-ADJUDICATION CROP IS NOT A FIGURE, and three of them are declared `figure`
        # in this corpus (blind legibility assessment, 2026-09-12): they carry a band of body
        # TEXT and no figure content at all, and one truncates mid-clause the very sentence it
        # exists to carry. The note beside them describes them correctly; the `kind` does not.
        # This is deterministic — the path says what it is — so it is named here. Whether a crop
        # is TRUNCATED is not deterministic and is not claimed.
        if "page_adjudications/" in str(path) and kind == "figure":
            # One line per paper, not per crop: the same sentence thirteen times is the noise
            # that trains a reader to skim. The names are carried; the reason is said once.
            entry["flags"].append("MISDECLARED_CROP")
        if entry["width"] and entry["width"] <= THIN_RASTER_PX:
                entry["flags"].append(
                    f"{entry['width']}x{entry['height']} px"
                    + (" — a page render from the PDF on disk is the native surface"
                       if has_pdf else " — no PDF on disk to render from; acquisition (M1) first"))
        # Only a FAILURE is worth a line here. The purpose is "do not repeat a failed operation
        # without a concrete reason", and a flag that fires on every successful acquisition
        # trains the reader to skim past the one that matters.
        # A verdict, not a silence. `no recipe — <reason>` means the route was never RECORDED,
        # which is a replay debt the packet already reports; it is not a failed attempt, and
        # flagging it fired on 13 of 13 surfaces of one paper — noise that hides the one line
        # that matters.
        failed = [verdict for verdict in entry["already_tried"]
                  if verdict.startswith(("FAILED", "DIGEST_DIFFERS", "EXTRACTOR_DRIFT",
                                         "RECAPTCHA", "HANDOFF"))]
        if failed:
            entry["flags"].append("a route already returned: " + "; ".join(sorted(set(failed))[:2])
                                  + " — repeat it only with a new route, method or information")
        out.append(entry)
    return {"pmid": pmid, "disease": disease, "surfaces": out,
            "page_adjudications": adjudications, "pdf_on_disk": has_pdf,
            "figure_count": sum(1 for item in out if item["kind"] == "figure"),
            "note": ("what is present, missing or unreadable, and what a better surface would be. "
                     "The scientific class of a surface is the reader's, after inspection."),
            "cannot_see": ("a crop that is a PARTIAL figure — one arm, no scale bar, no "
                           "comparator — and a crop truncated mid-sentence. Both were found in "
                           "this corpus by looking, on surfaces this inventory leaves unflagged "
                           "because they are large. Only the initial inspection catches them.")}


def render_surfaces(report: dict[str, Any]) -> str:
    rows = report["surfaces"]
    present = [row for row in rows if row["present"]]
    absent = [row for row in rows if not row["present"]]
    flagged = [row for row in present if any(not f.startswith("routes already") for f in row["flags"])]
    lines = [f"SURFACES — PMID {report['pmid']} · {len(present)} present, {len(absent)} absent, "
             f"{len(flagged)} flagged · {len(report['page_adjudications'])} page-adjudication "
             f"crop(s) already on disk"]
    misdeclared = [Path(row["path"]).name for row in rows if "MISDECLARED_CROP" in row["flags"]]
    for row in rows:
        shown = [flag for flag in row["flags"] if flag != "MISDECLARED_CROP"]
        if not shown:
            continue
        size = f"{row['width']}x{row['height']}" if row["width"] else "-"
        lines.append(f"  {Path(row['path']).name[:44]:<44} {row['kind'][:16]:<16} {size:>10}")
        for flag in shown:
            lines.append(f"       {flag}")
    if misdeclared:
        lines.append(f"  {len(misdeclared)} surface(s) declared `figure` that are "
                     "page-adjudication crops — read each as the page region it is, and check it "
                     "carries its whole sentence or panel:")
        lines.append("       " + ", ".join(misdeclared[:8])
                     + (f" … and {len(misdeclared) - 8} more" if len(misdeclared) > 8 else ""))
    if not rows:
        lines.append("  NO SURFACE declared or on disk. That is not 'no figures': it is a paper "
                     "whose surfaces have not been acquired (M1), and their relevance is unknown")
    elif not flagged and not absent:
        lines.append("  every declared surface is present and readable at its own size")
    lines.append("  a crop is read with its labels, controls, scale and legend, or it is not read")
    lines.append(f"  this inventory CANNOT see: {report['cannot_see']}")
    lines.append("  NOTHING here classifies a surface as marginal: that is your declaration "
                 "after inspection (brief M2)")
    return "\n".join(lines)


# ---------------------------------------------------------------- rank (which surface to read)
#
# 🔴 WHY THIS EXISTS, with the measurement that bought it (PMID 42422765, 2026-10-21).
# `surfaces` above lists what is on disk. It does not say which of thirty-five surfaces to open,
# and on that paper all sixteen persisted figure attestations were written on 726x708-class PMC
# CDN JPEGs at about 111 effective ppi, while the publisher PDF — on disk and undeclared since
# 2026-10-19 — carried the same figures as 300 dpi embedded rasters. Nobody chose the worse
# surface; nobody compared them, because nothing asked. A reader cannot choose the best surface
# it cannot see.
#
# 🔴 AND "EXTRACT THE EMBEDDED IMAGE" IS THE WRONG RULE — trap (a). On the same paper it would
# have been wrong for exactly one figure of eight: Figure 7's quantitative panels are VECTOR and
# its only embedded raster is 759x515, carrying the ECoG traces alone. An extracted read of
# Figure 7 returns a surface with no numbers on it at all, which a careful reader would plausibly
# write up as "panel unreadable" — a false negative about an endpoint family, produced by a
# correct-looking method. What detected it was ASPECT RATIO, and the separation is three orders of
# magnitude wide: the paper's six whole-figure embedded rasters matched a declared figure raster
# to between 0.0001 and 0.0011 relative (p3 1993x1968 ↔ gr1 738x729, p4 ↔ gr2, p6 ↔ gr3,
# p7 ↔ gr4, p9 ↔ gr5, p10 ↔ gr6), while page 11's 759x515 matched nothing closer than 0.106.
# So an UNPAIRED figure-sized raster is reported as a probable FRAGMENT of a composite figure and
# the PAGE RENDER is ranked above it. The flag is directional on purpose: a declared figure with
# no counterpart inside a PDF is "no better surface on disk", NOT a vector figure — the graphical
# abstract `ga1.jpg` is exactly that case, and a symmetric flag would have libelled it.
#
# 🔴 AND A SURFACE THAT IS NOT ON DISK IS NEVER A CANDIDATE — trap (b). A declared-but-absent
# artefact cannot be read however large its declaration says it is, so it is kept out of the
# ranked list entirely and reported under `absent` with the acquisition route. Ranking it would
# recommend a file that is not there, silently.
#
# NOT A GATE. `rank` writes nothing — not into a manifest, not anywhere — blocks nothing, and
# always exits 0. It answers one question, which surface carries the most readable copy of a
# figure, from measurements only. What the figure SHOWS, and whether it is marginal, stays the
# reader's declaration after inspection (brief M2).

# Relative aspect-ratio tolerance for calling two rasters the same picture. Measured pairs on
# PMID 42422765 sat at 0.0001-0.0011 and the fragment at 0.106; 0.01 is two orders of magnitude
# of margin on each side, and it is relative so a very wide figure is not held to a tighter
# absolute bound than a square one.
ASPECT_TOLERANCE = 0.01
# 🔴 A SECOND, STRICTER TOLERANCE, because the two questions are not the same question and one
# number cannot answer both. PAIRING asks "is this the same figure", and an answer that is one
# figure out is visible to the reader the moment the surface opens. A PPI MEASUREMENT asks "how
# wide was this printed", and a wrong answer is invisible and reorders the ranking. At 0.01,
# `gr7.jpg` (729x442, aspect 1.64932) matched an unrelated 454x274 supplement panel printed 163 pt
# wide, to 0.0046 — and was reported at 321 ppi, three times its real resolution, which lifted the
# very CDN raster this sub-command exists to demote. At 0.002 that match is refused, the ppi falls
# back to the stated assumption, and the assumption returns 104 ppi — the figure the paper's own
# manifest recorded by hand. True pairs on this corpus sit at 0.0001-0.0011, so 0.002 keeps every
# one of them.
MEASURE_GAP = 0.002
# A figure occupies a real share of its page. Page 1 of that publisher PDF places a 67x67 px
# journal logo at 16 pt, whose aspect is 1.0000 and would otherwise have "paired" with the
# 664x664 graphical abstract. Both bounds are needed: the pixel bound alone keeps a small
# full-width banner, the placement bound alone keeps a large but low-resolution ornament. The pixel
# bound applies to the SHORTER side, so a 1100x90 banner strip is not a figure however wide it is.
MIN_PLACEMENT_FRACTION = 0.20
MIN_FIGURE_PIXELS = 200
# What a page render of a vector figure actually delivers, and the dpi the native renders on disk
# for this corpus were made at. It is a RECOMMENDATION, not a measurement, and is labelled so.
RECOMMENDED_RENDER_DPI = 400
# Vector drawing commands on a page, outside its placed rasters, above which the page's figure is
# reported as probably part VECTOR. Measured on PMID 42422765's publisher PDF: 0 on each of the six
# pages whose figure is one whole embedded raster, 0 or 1 on every text page, 365 on the figure-7
# page whose quantitative panels are vector, and 27-757 on the supplement's figure pages. 12 is an
# order of magnitude above the text-page noise and well below the lowest true positive.
VECTOR_DRAWING_FLOOR = 12
# Printed width assumed for a raster with no on-disk PDF to measure against. Never printed
# without the `~` and the word `assumed`: it orders the list, it does not report a fact.
ASSUMED_PRINTED_WIDTH_IN = 7.0


def aspect_ratio(width: int, height: int) -> float:
    return width / height if width > 0 and height > 0 else 0.0


def aspect_gap(first: float, second: float) -> float:
    """Relative distance between two aspect ratios; 1.0 when either is unusable."""
    if first <= 0 or second <= 0:
        return 1.0
    return abs(first - second) / max(first, second)


def pdf_geometry(path: Path) -> dict[str, Any] | None:
    """Page sizes and every figure-sized PLACED image, in points — the only honest ppi basis.

    🔴 A raster's pixel count is not a resolution. 1993x1968 px is 300 ppi when it is printed
    across 478 pt and 1196 ppi when it is printed across 120 pt, and the two readings of the same
    figure are not equally legible. The placement rectangle is where the printed size lives, and
    PyMuPDF is the instrument that reports it; `raster_size_second_instrument` already records
    why `file(1)` and a page rectangle are not (density; points, not pixels).

    Returns None when PyMuPDF is absent or the file does not open as a PDF — reported as absent,
    never silently treated as "no better surface exists".
    """
    try:
        import pymupdf                                    # noqa: PLC0415 - optional by design
    except ImportError:
        return None
    try:
        document = pymupdf.open(str(path))
    except Exception:                                     # noqa: BLE001 - a broken PDF is a fact
        return None
    pages: list[dict[str, Any]] = []
    try:
        for number, page in enumerate(document, start=1):
            rect = page.rect
            entry: dict[str, Any] = {
                "number": number, "width_pt": float(rect.width), "height_pt": float(rect.height),
                "aspect": aspect_ratio(int(rect.width), int(rect.height)), "images": [],
            }
            try:
                images = page.get_images(full=True)
            except Exception:                             # noqa: BLE001
                images = []
            placed_rects = []
            for item in images:
                try:
                    placed_rects.extend(page.get_image_rects(int(item[0])))
                except Exception:                         # noqa: BLE001
                    continue
            # 🔴 THE SECOND INSTRUMENT, and the one that actually decides. Vector drawing commands
            # on the page that are NOT behind a placed raster. On PMID 42422765's publisher PDF the
            # separation is not a judgement call: the six pages whose figure is a whole embedded
            # raster carry 0 such commands each, the figure-7 page carries 365, and the text pages
            # carry 0 or 1. Aspect-ratio pairing found the same defect and needs a whole-figure
            # counterpart on disk to do it; this one needs nothing but the PDF, so it also works on
            # a supplement whose figures were never published as separate files.
            try:
                drawings = page.get_drawings()
            except Exception:                             # noqa: BLE001
                drawings = []
            outside = 0
            for drawing in drawings:
                box = drawing.get("rect")
                if box is None or box.width <= 0 or box.height <= 0:
                    continue
                if any((placed & box).get_area() > 0.9 * box.get_area()
                       for placed in placed_rects):
                    continue
                outside += 1
            entry["vector_drawings_outside_rasters"] = outside
            for item in images:
                xref, width, height = int(item[0]), int(item[2]), int(item[3])
                try:
                    rects = page.get_image_rects(xref)
                except Exception:                         # noqa: BLE001
                    rects = []
                for placed in rects:
                    placed_w, placed_h = float(placed.width), float(placed.height)
                    if placed_w <= 0 or placed_h <= 0:
                        continue
                    # 🔴 BOTH AXES, and the reason is measured. The first cut bounded the WIDTH
                    # only and ranked a 1100x90 banner strip on page 10 of PMID 29724996's article
                    # PDF first, at 600 ppi: 1100 px wide, printed 132 pt wide, and 90 px tall. A
                    # rule, a header band and a journal masthead are all wide; a figure is big on
                    # its SHORTER side too.
                    if (placed_w < MIN_PLACEMENT_FRACTION * float(rect.width)
                            or min(width, height) < MIN_FIGURE_PIXELS):
                        continue
                    entry["images"].append({
                        "xref": xref, "width": width, "height": height,
                        "aspect": aspect_ratio(width, height),
                        "placed_w_pt": placed_w, "placed_h_pt": placed_h,
                        "ppi": width / (placed_w / 72.0),
                        "ppi_height": height / (placed_h / 72.0),
                    })
            pages.append(entry)
    finally:
        document.close()
    return {"path": str(path), "pages": pages}


def measure_ppi(width: int, height: int, geometries: list[dict[str, Any]]) -> dict[str, Any]:
    """Effective ppi of a raster on disk, measured against a printed size that is also on disk.

    Two routes, both deterministic and both naming what they measured against:
      page render — the raster's aspect matches a PDF PAGE, so its printed size is that page;
      placed image — the raster's aspect matches an image PLACED in a PDF, so its printed size
                     is that placement.
    Neither route is available for, say, a bare CDN JPEG of a paper whose PDF was never acquired.
    Then the ppi is ASSUMED from a printed width and says so; it orders the list and asserts
    nothing.

    🔴 THE MATCH IS CHOSEN BY THE TIGHTEST ASPECT GAP, NEVER BY THE LARGEST PPI. The first cut
    took the maximum ppi among all matches within tolerance and reported the 400 dpi page render
    of `mmc1.pdf` p.9 as 585 ppi, because a figure PLACEMENT in a different supplement happened
    to sit 0.0041 away while its own page sat 0.0002 away. Maximising the number being reported
    is not measuring it: 585 ppi was a coincidence dressed as a fact, and it put that surface at
    the top of the ranking for the wrong reason.

    🔴 AND A TIE IS REPORTED AS A TIE. Every page of a PDF usually has the same aspect, so a page
    render matches all of them equally, and `mmc1.pdf` here has page 1 at 603x783 pt and pages
    2-10 at 612x791 — the same aspect as every page of two OTHER PDFs on disk. The first cut named
    whichever tied basis it happened to visit first and reported the 400 dpi render of the
    publisher PDF's page 11 as "page render of mmc1.pdf p.1". The ppi was right and the
    attribution was invented. So the tied bases are collected, the ppi is reported only when they
    AGREE on it, and the page is named only when one page matches.
    """
    own = aspect_ratio(width, height)
    found: list[tuple[float, float, str, str]] = []   # gap, ppi, where, kind
    for geometry in geometries:
        name = Path(geometry["path"]).name
        for page in geometry["pages"]:
            where = f"{name} p.{page['number']}"
            if page["width_pt"] > 0:
                found.append((aspect_gap(own, page["aspect"]),
                              width / (page["width_pt"] / 72.0), where, "page render"))
            for image in page["images"]:
                found.append((aspect_gap(own, image["aspect"]),
                              width / (image["placed_w_pt"] / 72.0), where,
                              f"printed {image['placed_w_pt']:.0f} pt wide"))
    found = [item for item in found if item[0] <= MEASURE_GAP]
    if found:
        tightest = min(item[0] for item in found)
        # A tie is anything that matches as tightly, within a slack far below the tolerance.
        tied = [item for item in found if item[0] <= tightest + 0.0005]
        ppis = [item[1] for item in tied]
        kind = tied[0][3]
        wheres = sorted({item[2] for item in tied})
        place = wheres[0] if len(wheres) == 1 else (
            f"{len(wheres)} equally-matching page(s)/placement(s) "
            f"({', '.join(sorted({w.split(' p.')[0] for w in wheres})[:3])}) — which one is not "
            f"determined by aspect")
        if max(ppis) - min(ppis) <= 0.02 * max(ppis):
            return {"ppi": min(ppis), "assumed": False, "gap": tightest, "against": place,
                    "basis": f"measured: {kind} in {place} (aspect to {tightest:.4f} relative)"}
        # The tied bases disagree on the printed size. The smallest is the conservative reading,
        # and the disagreement is reported rather than averaged away.
        return {"ppi": min(ppis), "assumed": True, "gap": tightest, "against": place,
                "basis": f"~AMBIGUOUS BASIS: {len(tied)} surfaces match this aspect to "
                         f"{tightest:.4f} and imply {min(ppis):.0f}-{max(ppis):.0f} ppi; the "
                         f"lowest is reported ({place})"}
    return {"ppi": width / ASSUMED_PRINTED_WIDTH_IN, "assumed": True, "against": "", "gap": 1.0,
            "basis": f"~assumed: no printed size on disk to measure against; "
                     f"{ASSUMED_PRINTED_WIDTH_IN:.0f} in printed width"}


# 🔴 THE FILENAME IS NOT THE FIGURE NUMBER, and nothing said so before 2026-10-24. In
# PMID 42157447 the publisher's own numbering runs Figure 1 = `ACN3-9999-0-g005.jpg`,
# Figure 5 = `g004.jpg`: eight files whose numeric order crosses the figure order in six of
# eight places. A reader who opens `g005.jpg` for Figure 5 is reading Figure 1 and has no way
# to notice, which is the error class the blind audits keep finding — a locator anchored to the
# wrong panel passes every existing check, because every existing check matches text.
#
# The mapping is not a guess: JATS declares it, one `<graphic>` inside each `<fig>` beside that
# fig's `<label>`. So it is read from the article XML the manifest already declares, and when no
# JATS is on disk the ranking says the question is UNDECIDED rather than letting the filename
# answer it. Figure labels are reported for FILES ONLY: an embedded raster or a page render is
# identified by its page, and no `<fig>` names it.
def jats_figure_labels(root: Path, disease: str, pmid: str,
                       manifest: dict | None = None) -> tuple[dict[str, str], str]:
    """({figure file basename: its JATS label}, the XML it came from) — ({}, "") with no JATS."""
    import xml.etree.ElementTree as ET                     # noqa: PLC0415 - one call site

    if manifest is None:
        manifest = load_manifest(root, disease, pmid)
    for item in (manifest or {}).get("source_artifacts") or []:
        if not isinstance(item, dict) or str(item.get("kind")) != "article_text":
            continue
        path = root / str(item.get("path") or "")
        if path.suffix.lower() != ".xml" or not path.is_file():
            continue
        try:
            tree = ET.parse(path)
        except (OSError, ET.ParseError):
            continue
        labels: dict[str, str] = {}
        for element in tree.iter():
            if element.tag.rsplit("}", 1)[-1] != "fig":
                continue
            found = [child for child in element.iter()
                     if child.tag.rsplit("}", 1)[-1] == "label"]
            label = re.sub(r"\s+", " ", "".join(found[0].itertext())).strip() if found else ""
            if not label:
                continue
            for child in element.iter():
                if child.tag.rsplit("}", 1)[-1] not in {"graphic", "inline-graphic"}:
                    continue
                for key, value in child.attrib.items():
                    if key.rsplit("}", 1)[-1] == "href" and value:
                        labels.setdefault(Path(str(value)).name.lower(), label)
        if labels:
            return labels, str(item.get("path") or "")
    return {}, ""


def rank_surfaces(root: Path, disease: str, pmid: str) -> dict[str, Any]:
    """Every figure-bearing surface for one PMID, ordered best-first for READING a figure."""
    manifest = load_manifest(root, disease, pmid)
    rows = artefacts(root, disease, pmid, manifest)
    kinds = {str(item.get("path") or ""): str(item.get("kind") or "")
             for item in (manifest or {}).get("source_artifacts") or [] if isinstance(item, dict)}
    labels, labels_from = jats_figure_labels(root, disease, pmid, manifest)

    def label_of(path: str) -> str:
        """The JATS label of a figure FILE; the extensionless stem is tried too, because a
        `<graphic>` href legitimately omits the suffix."""
        name = Path(path).name.lower()
        return labels.get(name) or labels.get(Path(name).stem, "")

    absent: list[dict[str, Any]] = []
    rasters: list[dict[str, Any]] = []
    pdfs: list[dict[str, Any]] = []
    for row in rows:
        path = Path(str(row["path"]))
        suffix = path.suffix.lower()
        if suffix not in RASTER_SUFFIXES | {".pdf", ".tif", ".tiff"}:
            continue
        shared = {"path": str(path), "kind": kinds.get(str(path), ""), "declared": row["declared"],
                  "figure_label": label_of(str(path))}
        if not row["present"]:
            # 🔴 trap (b). Not a candidate at any size: it cannot be opened.
            absent.append({**shared, "note": "ABSENT from disk — never ranked; acquire it first "
                                             "(M1, `find-fulltext` / `reacquire.py`)"})
            continue
        if suffix == ".pdf":
            pdfs.append(shared)
            continue
        size = raster_size_from_header(root / path)
        if not size:
            absent.append({**shared, "note": "UNREADABLE header — never ranked; its pixel size "
                                             "could not be measured, so it cannot be compared"})
            continue
        rasters.append({**shared, "width": size[0], "height": size[1],
                        "aspect": aspect_ratio(*size), "digest": sha256_file(root / path)})

    # Same reason as the PDF dedupe below: this corpus holds each of the seven CDN figure JPEGs
    # twice, under `files/figures/PMID<pmid>_r2/` and `files/fulltext/figures/PMID<pmid>/`,
    # byte-identical. Two rows for one surface is one row of noise.
    duplicate_rasters: list[str] = []
    unique_rasters: list[dict[str, Any]] = []
    raster_digests: dict[str, str] = {}
    for entry in rasters:
        first = raster_digests.get(entry["digest"])
        if first:
            duplicate_rasters.append(f"{entry['path']} == {first}")
            continue
        raster_digests[entry["digest"]] = entry["path"]
        unique_rasters.append(entry)
    rasters = unique_rasters

    # 🔴 ONE GEOMETRY PER DISTINCT PDF, keyed by digest. `mmc2.pdf` is on this corpus's disk three
    # times — under `files/fulltext/<slug>_assets/`, `files/supplement/PMID<pmid>/` and
    # `files/supplement/PMID<pmid>_r2/` — byte-identical, and enumerating each copy produced the
    # same 27 pages three times: 504 candidates where there were 168, with every real figure
    # listed three times running. A duplicate row is not a conservative error; it is the noise
    # that trains a reader to skim past the one line that matters.
    geometries: list[dict[str, Any]] = []
    seen: dict[str, str] = {}
    duplicate_pdfs: list[str] = []
    unopened: list[str] = []
    for entry in pdfs:
        digest = sha256_file(root / Path(entry["path"]))
        if digest in seen:
            duplicate_pdfs.append(f"{entry['path']} == {seen[digest]}")
            continue
        seen[digest] = entry["path"]
        geometry = pdf_geometry(root / Path(entry["path"]))
        if geometry:
            geometries.append(geometry)
        else:
            unopened.append(entry["path"])
    pdfs = [entry for entry in pdfs if entry["path"] in set(seen.values())]

    candidates: list[dict[str, Any]] = []
    for entry in rasters:
        # 🔴 A PAGE-ADJUDICATION CROP IS NOT A FIGURE — the same deterministic fact `surfaces`
        # already names as MISDECLARED_CROP, and here it decides the ranking rather than a flag.
        # It is a band cut out of a rendered page, so the printed-width assumption that orders
        # everything else is simply wrong for it: a 2924x145 caption strip came out at ~418
        # assumed ppi and ranked FIRST for PMID 16223882, above every real figure surface. So no
        # ppi is claimed for it, assumed or measured, and it is ranked last on purpose.
        crop = "page_adjudications/" in entry["path"]
        measured = measure_ppi(entry["width"], entry["height"], geometries)
        candidates.append({
            "surface": entry["path"], "route": "on_disk", "kind": entry["kind"],
            "declared": entry["declared"], "figure_label": entry.get("figure_label", ""),
            "width": entry["width"], "height": entry["height"],
            "aspect": round(entry["aspect"], 5),
            "ppi": 0.0 if crop else round(measured["ppi"], 1),
            "ppi_basis": ("PAGE CROP — a band of a rendered page, not a whole figure; its printed "
                          "width is unknown, so no ppi is claimed for it"
                          if crop else measured["basis"]),
            "ppi_assumed": True if crop else measured["assumed"],
            "score": 0.0 if crop else measured["ppi"],
            "flags": (["PAGE_CROP — ranked last on purpose. Read it as the page region it is, and "
                       "check it carries its whole sentence or panel; the figure itself is on the "
                       "page render or the figure surfaces above"] if crop else []),
            "read_this": f"open {Path(entry['path']).name} as it is",
        })

    # The reference set for pairing: whole-figure rasters on disk. A raster whose aspect matches a
    # PDF PAGE is a page render of that page, not a figure, and is excluded — otherwise a page
    # render would "pair" with a figure-sized image on its own page and silence the flag.
    references = [entry for entry, candidate in zip(rasters, candidates)
                  if "page render" not in candidate["ppi_basis"]
                  and "page_adjudications/" not in entry["path"]]

    for geometry in geometries:
        name = Path(geometry["path"]).name
        for page in geometry["pages"]:
            if not page["images"]:
                # A page with no figure-sized raster is NOT asserted to carry a figure. See
                # `cannot_see`: a wholly vector figure page and a title page with rules are not
                # separable by the drawing count alone — page 1 of this corpus's publisher PDF
                # carries 34 drawing commands and no figure at all.
                continue
            where = f"{name} p.{page['number']}"
            vectors = int(page.get("vector_drawings_outside_rasters") or 0)
            vector_page = vectors >= VECTOR_DRAWING_FLOOR
            paired: list[tuple[dict[str, Any], str, float]] = []
            for image in page["images"]:
                nearest, gap = "", 1.0
                for reference in references:
                    this = aspect_gap(image["aspect"], reference["aspect"])
                    if this < gap:
                        nearest, gap = Path(reference["path"]).name, this
                paired.append((image, nearest, gap))

            if vector_page:
                # 🔴 trap (a), and ONE candidate for the page however many rasters sit on it. The
                # first cut emitted one page render per unpaired raster and printed the same page
                # three times with three different nearest-neighbours — the duplication that makes
                # a reader skim.
                unpaired = [(image, nearest, gap) for image, nearest, gap in paired
                            if gap > ASPECT_TOLERANCE]
                if unpaired:
                    image, nearest, gap = min(unpaired, key=lambda item: item[2])
                    corroborated = (
                        f"and its closest unpaired raster, {image['width']}x{image['height']}, "
                        f"matches no whole-figure surface on disk (nearest {nearest} at "
                        f"{gap:.3f} relative, tolerance {ASPECT_TOLERANCE})" if nearest else
                        f"and there is NO whole-figure surface on disk to compare its "
                        f"{image['width']}x{image['height']} raster against, so the pairing "
                        f"instrument has nothing to say either way")
                else:
                    image, nearest, gap = min(paired, key=lambda item: item[2])
                    # Two instruments, and they disagree. Said, not resolved by picking one.
                    corroborated = (f"BUT every raster on it pairs with a whole-figure surface "
                                    f"(closest {nearest} at {gap:.4f}) — the two instruments "
                                    f"disagree, so the raster may well be a whole panel; render "
                                    f"the page to see what the vectors are")
                candidates.append({
                    "surface": f"{where} · PAGE RENDER at {RECOMMENDED_RENDER_DPI} dpi",
                    "route": "page_render", "kind": "figure", "declared": False,
                    "figure_label": "",
                    "width": 0, "height": 0, "aspect": round(page["aspect"], 5),
                    "ppi": float(RECOMMENDED_RENDER_DPI),
                    "ppi_basis": f"~recommended render dpi; vector content is resolution-"
                                 f"independent, page is {page['width_pt'] / 72:.2f} x "
                                 f"{page['height_pt'] / 72:.2f} in",
                    "ppi_assumed": True, "score": float(RECOMMENDED_RENDER_DPI),
                    "vector_drawings": vectors,
                    "flags": [f"LIKELY_VECTOR_FIGURE — this page carries {vectors} vector drawing "
                              f"command(s) outside its rasters {corroborated}. Extracting the "
                              f"raster returns part of the figure — plausibly the part with no "
                              f"numbers on it. RENDER THE PAGE."],
                    "read_this": f"render {where} at >= 300 dpi (`pdftoppm -r 400` / PyMuPDF "
                                 f"`get_pixmap(dpi=400)`); do NOT extract the raster",
                })

            for image, nearest, gap in paired:
                whole = gap <= ASPECT_TOLERANCE
                skew = (abs(image["ppi"] - image["ppi_height"]) / max(image["ppi"], 1e-9) > 0.02)
                flags = []
                if whole:
                    flags.append(f"pairs with {nearest} to {gap:.4f} relative — the same whole "
                                 f"figure at higher resolution")
                else:
                    flags.append((f"no whole-figure counterpart on disk (nearest {nearest} at "
                                  f"{gap:.3f} relative)" if nearest else
                                  "no whole-figure surface on disk to compare against at all")
                                 + ". That alone is not a vector figure: a supplement figure and "
                                   "a graphical abstract legitimately have no counterpart")
                if skew:
                    flags.append("AXES DISAGREE — the placement is not square to the pixels; "
                                 "render the page instead")
                if vector_page:
                    flags.append("PROBABLE FRAGMENT — ranked below the page render of its own "
                                 "page on purpose, because that page carries vector content")
                elif not whole:
                    flags.append(f"this page carries {vectors} vector drawing command(s) outside "
                                 f"its rasters, below the floor of {VECTOR_DRAWING_FLOOR}, so the "
                                 f"raster is probably the whole figure")
                candidates.append({
                    "surface": f"{where} · embedded {image['width']}x{image['height']}",
                    "route": "embedded", "kind": "figure", "declared": False,
                    "figure_label": "",
                    "width": image["width"], "height": image["height"],
                    "aspect": round(image["aspect"], 5), "ppi": round(image["ppi"], 1),
                    "ppi_basis": f"measured: printed {image['placed_w_pt']:.0f} pt wide in {where}",
                    "ppi_assumed": False, "vector_drawings": vectors,
                    # A fragment's ppi is high and its CONTENT is partial, and ppi is the axis this
                    # list sorts on — so it is demoted explicitly rather than trusted to sort low.
                    "score": -1.0 if vector_page else image["ppi"],
                    "flags": flags,
                    "read_this": (f"read only to confirm which panel it carries; the figure is on "
                                  f"the page render of {where}") if vector_page else
                                 (f"extract the embedded image from {where} (`pdfimages -list` / "
                                  f"PyMuPDF), do not re-download"),
                })

    candidates.sort(key=lambda row: (-row["score"], -row["width"], row["surface"]))
    for position, row in enumerate(candidates, start=1):
        row["position"] = position
    unpaired = [row["surface"] for row in candidates if row["route"] == "page_render"]
    # The clause that becomes false the moment a JATS decides it — and stays true, loudly, when
    # there is no JATS. The two facts are different and are never printed as one.
    unseen_figure = ("WHICH FIGURE a surface actually carries: no JATS article XML is on disk "
                     "for this PMID, so nothing here decides it and the FILENAME IS NOT "
                     "EVIDENCE of the figure number (measured on PMID 42157447: Figure 1 is "
                     "g005.jpg and Figure 5 is g004.jpg); " if not labels else
                     "which figure an EMBEDDED raster or a PAGE RENDER carries — a `<fig>` names "
                     "a file, not a page, so only the file rows above are labelled; ")
    return {
        "pmid": pmid, "disease": disease, "candidates": candidates, "absent": absent,
        "figure_labels": dict(sorted(labels.items())), "figure_labels_from": labels_from,
        "pdfs_on_disk": [entry["path"] for entry in pdfs],
        "duplicate_pdfs": duplicate_pdfs, "unopened_pdfs": unopened,
        "duplicate_rasters": duplicate_rasters,
        "geometry_instrument": ("PyMuPDF" if geometries else
                                "NONE — no PDF on disk, so no printed size to measure against"
                                if not pdfs else
                                "NONE — a PDF is on disk but PyMuPDF did not open it"),
        "pymupdf_absent": bool(unopened),
        "likely_vector_pages": unpaired,
        "note": "ordered best-first for READING a figure, on measured ppi. It writes nothing, "
                "gates nothing and classifies no figure as marginal: that is the reader's "
                "declaration after inspection (brief M2).",
        "cannot_see": (unseen_figure + "a panel cropped out of an "
                       "otherwise whole raster; and a figure that is ENTIRELY vector on a page "
                       "carrying no figure-sized raster — the drawing count does not separate "
                       "that from a title page with rules (page 1 of this corpus's publisher PDF: "
                       "34 drawing commands, no figure), so such a page is not listed. Only the "
                       "inspection catches those."),
    }


RANK_RENDER_LIMIT = 15


def render_rank(report: dict[str, Any], limit: int = RANK_RENDER_LIMIT) -> str:
    """The human view. `--json` always carries EVERY candidate; this one is a reading decision.

    The limit applies to the ordinary best-first tail only. Every `page_render` candidate — the
    ones carrying trap (a)'s LIKELY_VECTOR_FIGURE flag — and every surface that is not rankable
    are shown whatever the limit, because they are the two things a reader must not miss and the
    two things a truncated list would drop first.
    """
    rows = report["candidates"]
    shown = [row for row in rows if row["route"] == "page_render"]
    shown += [row for row in rows if row["route"] != "page_render"][:limit or len(rows)]
    shown.sort(key=lambda row: row["position"])
    lines = [f"RANK — PMID {report['pmid']} · {len(rows)} figure-bearing candidate(s) on disk, "
             f"{len(report['absent'])} not rankable · geometry by {report['geometry_instrument']}"]
    if report.get("figure_labels"):
        lines.append(f"  which figure each FILE is, from the JATS <fig> graphics of "
                     f"{Path(report['figure_labels_from']).name} — not from the filename, which "
                     f"does not track the figure order")
    elif any(row["route"] == "on_disk" for row in rows) or report["absent"]:
        lines.append("  🔴 which figure each file carries is UNDECIDED here: no JATS article XML "
                     "on disk. Do NOT read the figure number off the filename — acquire the XML "
                     "or read each file's own caption")
    if report["pymupdf_absent"]:
        lines.append("  🔴 a PDF on disk could not be opened for geometry — effective ppi below "
                     "may be ASSUMED where it would otherwise have been measured: "
                     + ", ".join(report["unopened_pdfs"][:3]))
    duplicates = report["duplicate_pdfs"] + report["duplicate_rasters"]
    if duplicates:
        lines.append(f"  {len(duplicates)} byte-identical duplicate surface(s) on disk collapsed "
                     "to one row each: " + "; ".join(duplicates[:2])
                     + (f" … and {len(duplicates) - 2} more" if len(duplicates) > 2 else ""))
    for row in shown:
        size = f"{row['width']}x{row['height']}" if row["width"] else "page"
        ppi = f"{'~' if row['ppi_assumed'] else ''}{row['ppi']:.0f} ppi"
        lines.append(f"  {row['position']:>2}. {row['surface'][:62]:<62} {size:>11} {ppi:>11}")
        if row.get("figure_label"):
            lines.append(f"       this file is {row['figure_label']} (JATS)")
        lines.append(f"       {row['ppi_basis']}")
        lines.append(f"       → {row['read_this']}")
        for flag in row["flags"]:
            lines.append(f"       {flag}")
    for row in report["absent"]:
        lines.append(f"  --  {Path(row['path']).name[:62]:<62} {'-':>11} {'-':>11}")
        if row.get("figure_label"):
            lines.append(f"       this file is {row['figure_label']} (JATS)")
        lines.append(f"       {row['note']}")
    if len(shown) < len(rows):
        lines.append(f"  … {len(rows) - len(shown)} further candidate(s) ranked below these; "
                     "`--json` carries every one, `--limit 0` prints them all")
    if not rows:
        lines.append("  NO figure-bearing surface on disk. That is not 'no figures': it is a "
                     "paper whose figure surfaces have not been acquired (M1)")
    if report["likely_vector_pages"]:
        lines.append(f"  {len(report['likely_vector_pages'])} page(s) carry a figure that is "
                     "probably part VECTOR — render the page, do not extract its raster")
    lines.append(f"  this ranking CANNOT see: {report['cannot_see']}")
    lines.append("  it writes nothing and gates nothing; the scientific class of a surface is "
                 "yours after inspection (brief M2)")
    return "\n".join(lines)


# --------------------------------------------------------------------------- procedures

# 🔴 THE ONE CANONICAL TABLE of specialist procedures and what activates them. The standing
# brief and the skills REFER to this table; they do not restate it. A rule stated twice drifts.
#
# Each entry: the procedure, the phase it belongs to (M1 acquisition, before the blind read;
# M2 the reading; M3 the manifest, after the read and before the receipt; M4b the comparison,
# after the receipt), the canonical file(s) a reader opens when it is `open`, and the observed
# condition — from OBSERVED_CONDITIONS — that a reader may declare when the reading itself
# surfaces the trigger after the packet was built. The predicate lives in `_evaluate`, one
# branch per key, on TECHNICAL facts only: artefact presence and suffixes, counts, the verdict
# tokens a check printed, the closed vocabulary. No reason string is ever built from a claim,
# a proposition, a dossier or the prose of a `retraction_check.result`; `test_paper_packet.py`
# plants markers in every one of those and asserts they never surface.
PROCEDURES: tuple[dict[str, Any], ...] = (
    {"key": "acquisition", "phase": "M1",
     "name": "acquisition / recovery of a missing surface",
     "files": (".claude/skills/find-fulltext/SKILL.md",
               "framework/scripts/reacquire.py (docstring: replay and verdicts)",
               "framework/protocols/fulltext_read_receipt.md § Acquisition recipes"),
     "observed": "missing_surface"},
    {"key": "page_adjudication", "phase": "M2",
     "name": "suspect PDF text layer — anchor to the rendered page",
     "files": ("framework/protocols/fulltext_read_receipt.md § A text layer is not its page",
               "framework/scripts/regenerate_adjudications.py (docstring: recipe, needle, digest)"),
     "observed": "suspect_text_layer"},
    {"key": "binary_supplement", "phase": "M1",
     "name": "binary supplement container — declare, fingerprint, reach its text",
     "files": ("framework/scripts/deepdive_manifest.py (comment at ARTIFACT_KINDS on supplement_binary, ~25 lines)",
               "framework/protocols/scientist_standing_brief.md M2, the .pptx paragraph"),
     "observed": "binary_supplement"},
    {"key": "integrity_notice", "phase": "M3",
     "name": "erratum / correction / expression of concern / retraction on THIS paper",
     "files": ("framework/scripts/erratum_scope_check.py (docstring: corrected_items, three outcomes)",
               "framework/instruction/LEGEND_CORE.md (URGENT_COMMIT_REQUEST, retraction category)"),
     "observed": "integrity_notice"},
    {"key": "dependency_integrity", "phase": "M3",
     "name": "integrity of what this paper depends on (reference-list screen)",
     "files": ("framework/scripts/dependency_integrity.py (docstring: known failure modes)",
               "framework/protocols/fulltext_read_receipt.md § Acquisition recipes "
               "(retraction_check.dependencies, declared at reading time)"),
     "observed": "dependency_flagged"},
    {"key": "locator_contradiction", "phase": "M3/M4b",
     "name": "contradicting a persisted locator — re-inspect, declare, blind audit",
     "files": (".claude/skills/legend-locator-audit/SKILL.md",
               "framework/scripts/locator_contradiction_audit.py (docstring; run with --working-tree --fail-on-undeclared)",
               "framework/protocols/scientist_standing_brief.md M2, the contradicts_locator rule"),
     "observed": "contradicts_locator"},
)

# The closed vocabulary a reader may declare. Free text is refused at the parser, so the
# `--observed` channel cannot carry a claim into a reason string.
OBSERVED_CONDITIONS: dict[str, str] = {
    "missing_surface": "a surface the reading needs is absent or unreadable on this host",
    "suspect_text_layer": "the PDF text layer disagrees with the rendered page",
    "binary_supplement": "a supplement is a binary container (.pptx / .xlsx / .docx / .zip)",
    "integrity_notice": "an erratum, correction, expression of concern or retraction was found",
    "dependency_flagged": "a paper this one depends on carries an integrity notice",
    "contradicts_locator": "the reading contradicts a locator already persisted",
}

OPEN, NOT_NEEDED, TO_ASCERTAIN = "open", "not_needed", "to_ascertain"

# Tokens a `retraction_check.result` carries when a notice EXISTS. Negations ("no erratum",
# "no expression of concern") do not match: every pattern requires the PubMed RefType form or
# the "<kind> in <Journal>" form. The matched TOKEN is all that ever reaches a reason string.
NOTICE_TOKENS = re.compile(
    r"(ErratumIn|ExpressionOfConcernIn|RetractionIn|CorrectionIn|RetractedIn"
    r"|Erratum in[:' \"]+[A-Z]|Expression of Concern in[:' \"]+[A-Z]|Retraction in[:' \"]+[A-Z]"
    r"|Author Correction)", re.I)
# 🔴 A token inside a negated clause is not a notice. Independent verification (2026-09-12) found
# three corpus manifests whose result says "there is no RetractionIn, RetractionOf or
# expression-of-concern link" and the bare token opened the procedure. The clause is the text
# since the last sentence boundary; a negation word in it withdraws the match.
NEGATION_IN_CLAUSE = re.compile(r"\b(no|not|never|neither|nor|without|absent)\b", re.I)


def notice_token(result: str) -> str:
    """The first notice token in a `retraction_check.result` that is not negated, else ''."""
    for match in NOTICE_TOKENS.finditer(result):
        clause = re.split(r"[.;\n]", result[:match.start()])[-1]
        if NEGATION_IN_CLAUSE.search(clause):
            continue
        return match.group(1).split(" in")[0].split(" In")[0].strip(":'\" ")
    return ""

# What a finished check's output says, reduced to tokens. Recorded by `run_checks` beside each
# result so that `procedures` reads signals and never re-reads the detail file.
CHECK_SIGNALS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("SUSPECT_TEXT_SURFACE", re.compile(r"SUSPECT text surface|SUSPECT_FONTS|UNTRUSTWORTHY")),
    ("ERRATUM_REVIEW_REQUIRED", re.compile(r"\[REVIEW_REQUIRED\]")),
    ("ERRATUM_SCOPE_UNDECLARED", re.compile(r"\[SCOPE_UNDECLARED\]")),
    ("UNDECLARED_LOCATOR_REVISION", re.compile(r"undeclared (locator )?revision", re.I)),
)


def check_signals(name: str, code: int, output: str) -> list[str]:
    """The tokens a check's output carries, plus its own refusal — nothing else is kept."""
    found = [token for token, pattern in CHECK_SIGNALS if pattern.search(output)]
    if name == "undeclared locator revision":
        # The audit prints "no undeclared locator revision" on the clean path; only a non-zero
        # exit means one was found.
        found = [token for token in found if token != "UNDECLARED_LOCATOR_REVISION"]
        if code != 0:
            found.append("UNDECLARED_LOCATOR_REVISION")
    if name == "manifest validator" and code == 0:
        found.append("VALIDATOR_OK")
    return found


def technical_facts(root: Path, disease: str, pmid: str, manifest: dict | None,
                    rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Counts, suffixes and tokens. The one place the manifest is read for the procedures, and
    it returns nothing a reader could mistake for a finding about the paper."""
    present = [row for row in rows if row["present"]]
    suffixes = {Path(str(row["path"])).suffix.lower() for row in present}
    facts: dict[str, Any] = {
        "manifest": manifest is not None,
        "present": len(present),
        "declared_absent": sum(1 for row in rows if row["declared"] and not row["present"]),
        "digest_mismatch": sum(1 for row in present if row["digest"] == "MISMATCH"),
        "digest_unverifiable": sum(1 for row in present if row["digest"] == "UNVERIFIABLE"),
        "declared_present": sum(1 for row in present if row["declared"]),
        "structured_surface": bool(suffixes & STRUCTURED_SUFFIXES),
        "pdf_surface": bool(suffixes & PDF_SUFFIXES),
        "binary_containers": sorted(Path(str(row["path"])).name for row in present
                                    if Path(str(row["path"])).suffix.lower() in BINARY_SUPPLEMENT_SUFFIXES),
        "binary_undeclared": sorted(Path(str(row["path"])).name for row in present
                                    if Path(str(row["path"])).suffix.lower() in BINARY_SUPPLEMENT_SUFFIXES
                                    and not row["declared"] and not row.get("copy_of_declared")),
        "supplement_declared": any("supplement" in str(row["path"]).lower()
                                   or str(row.get("kind", "")).startswith("supplement")
                                   for row in rows if row["declared"]),
        "adjudication_artefacts": sum(1 for row in rows if "page_adjudications/" in str(row["path"])),
        # 🔴 A closed question must not be reopened by a rule that cannot see the closure. The
        # reading of 21731849 recorded "hasSuppl=N" from the indexed record; the procedure still
        # said "to ascertain", and a re-test comparison on 2026-09-12 repeated that over the
        # manifest's own statement. The indexed record's negative is a fact the rule may use.
        "indexed_no_supplement": bool(re.search(r"hasSuppl\s*=\s*N\b", json.dumps(
            (manifest or {}).get("source_fulltext_indexed_evidence") or "")
            + json.dumps((manifest or {}).get("figure_extractions") or {}))),
        "locator_entries": 0,
        "retraction_check": "absent",
        "notice_token": "",
        "corrected_items": 0,
        "dependencies_verdict": "",
    }
    if manifest:
        entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
        facts["locator_entries"] = len(entries) if isinstance(entries, list) else 0
        check = manifest.get("retraction_check")
        if isinstance(check, dict) and check:
            facts["retraction_check"] = "recorded"
            items = check.get("corrected_items")
            facts["corrected_items"] = len(items) if isinstance(items, list) else 0
            facts["notice_token"] = notice_token(str(check.get("result") or ""))
            deps = check.get("dependencies")
            if isinstance(deps, dict):
                # The first TOKEN only: a verdict is one word, and whatever follows it is prose.
                facts["dependencies_verdict"] = (str(deps.get("paper_verdict") or "").split() or [""])[0].strip(":")[:40]
    return facts


def _evaluate(key: str, facts: dict[str, Any], signals: set[str],
              observed: set[str]) -> tuple[str, str, str]:
    """(state, reason, condition still to ascertain) for one procedure.

    Precedence: an observed condition opens the procedure whatever the data say — the reader
    saw it; a check signal decides next; the packet's facts last. A missing datum yields
    TO_ASCERTAIN with the datum named, never NOT_NEEDED.
    """
    procedure = next(item for item in PROCEDURES if item["key"] == key)
    if procedure["observed"] in observed:
        return OPEN, f"declared by the reader: {OBSERVED_CONDITIONS[procedure['observed']]}", ""

    if key == "acquisition":
        if facts["present"] == 0:
            return OPEN, "no artefact is present on this host", ""
        if facts["declared_absent"] or facts["digest_mismatch"]:
            return OPEN, (f"{facts['declared_absent']} declared artefact(s) absent, "
                          f"{facts['digest_mismatch']} digest MISMATCH"), ""
        digests = ("digests agree" if not facts["digest_unverifiable"]
                   else f"{facts['digest_unverifiable']} digest(s) unverifiable (absent or malformed)")
        return NOT_NEEDED, (f"{facts['declared_present']} declared artefact(s) present, none absent, "
                            f"{digests}; {facts['present'] - facts['declared_present']} undeclared on disk"), ""

    if key == "page_adjudication":
        if facts["adjudication_artefacts"]:
            return OPEN, (f"{facts['adjudication_artefacts']} page-adjudication crop(s) already "
                          "declared — the recipe chain must be kept"), ""
        if "SUSPECT_TEXT_SURFACE" in signals:
            return OPEN, "the validator refused a text surface as SUSPECT", ""
        if facts["structured_surface"]:
            return NOT_NEEDED, "a structured surface (XML/HTML) is present; it has no page to diverge from", ""
        if facts["pdf_surface"] and "VALIDATOR_OK" in signals:
            return NOT_NEEDED, "PDF-derived text is the only surface and the validator's SUSPECT screen passed it", ""
        if facts["pdf_surface"]:
            return TO_ASCERTAIN, "PDF-derived text is the only surface and no screen has examined it yet", \
                "run `paper_packet.py check`: the validator's SUSPECT screen decides"
        return TO_ASCERTAIN, "no text surface is present to screen", "acquire a surface first (M1)"

    if key == "binary_supplement":
        if facts["binary_undeclared"]:
            return OPEN, (f"{len(facts['binary_undeclared'])} binary container(s) on disk and "
                          "undeclared: " + ", ".join(facts["binary_undeclared"][:4])), ""
        if facts["binary_containers"]:
            return NOT_NEEDED, (f"{len(facts['binary_containers'])} binary container(s), all declared "
                                "— the validator verifies their kind and digest"), ""
        if facts["supplement_declared"]:
            return NOT_NEEDED, "supplements are declared and none is a binary container", ""
        if facts.get("indexed_no_supplement"):
            return NOT_NEEDED, ("the indexed record the reading quotes says hasSuppl=N: there is "
                                "no supplement, by fact and not by omission"), ""
        return TO_ASCERTAIN, "no supplement declared or on disk", \
            "the article's own supplementary listing, at acquisition, says whether one exists"

    if key == "integrity_notice":
        if "ERRATUM_REVIEW_REQUIRED" in signals or "ERRATUM_SCOPE_UNDECLARED" in signals:
            token = "REVIEW_REQUIRED" if "ERRATUM_REVIEW_REQUIRED" in signals else "SCOPE_UNDECLARED"
            return OPEN, f"erratum scope check returned {token}", ""
        if facts["corrected_items"] or facts["notice_token"]:
            return OPEN, (f"retraction_check records a notice ({facts['notice_token'] or 'corrected items'}; "
                          f"{facts['corrected_items']} corrected item(s) declared)"), ""
        if facts["retraction_check"] == "recorded":
            return NOT_NEEDED, "retraction_check is recorded and names no notice", ""
        return TO_ASCERTAIN, "no retraction_check recorded", \
            "PubMed ESummary CommentsCorrections for this PMID (M3, retraction_check)"

    if key == "dependency_integrity":
        verdict = facts["dependencies_verdict"]
        if verdict.upper().startswith("FLAGGED"):
            return OPEN, f"retraction_check.dependencies verdict {verdict}", ""
        if verdict:
            return NOT_NEEDED, f"retraction_check.dependencies verdict {verdict}", ""
        return TO_ASCERTAIN, "the reference list has not been screened for this paper", \
            "`dependency_integrity.py screen --pmid <PMID> --manifest-block` (network: Crossref)"

    if key == "locator_contradiction":
        if "UNDECLARED_LOCATOR_REVISION" in signals:
            return OPEN, "the working tree changes a persisted locator without a declaration", ""
        if facts["locator_entries"]:
            # Whether THIS reading changes a persisted entry is not knowable before M3: the
            # datum that fires the trigger does not exist yet. So: to ascertain, not open —
            # opening it on every paper with a manifest is the indiscriminate activation.
            return TO_ASCERTAIN, (f"an existing manifest holds {facts['locator_entries']} persisted "
                                  "locator entries; whether this reading changes one is known at M3"), \
                ("`locator_contradiction_audit.py --working-tree --fail-on-undeclared` before any "
                 "manifest edit, or declare `--observed contradicts_locator`")
        if facts["manifest"]:
            return NOT_NEEDED, "an existing manifest holds no persisted locator", ""
        return NOT_NEEDED, "no manifest exists: nothing persisted can be contradicted", ""

    raise KeyError(key)


def procedures(facts: dict[str, Any], signals: set[str] | None = None,
               observed: set[str] | None = None) -> list[dict[str, str]]:
    signals = signals or set()
    observed = observed or set()
    unknown = observed - set(OBSERVED_CONDITIONS)
    if unknown:
        raise ValueError(f"observed condition outside the vocabulary: {sorted(unknown)}")
    rows = []
    for item in PROCEDURES:
        state, reason, pending = _evaluate(item["key"], facts, signals, observed)
        rows.append({"key": item["key"], "name": item["name"], "phase": item["phase"],
                     "state": state, "reason": reason, "to_ascertain": pending,
                     "files": list(item["files"])})
    return rows


def load_check_signals(root: Path, pmid: str, out_dir: Path | None = None) -> tuple[set[str], str]:
    """Signals recorded by the last `check` run, if any — and the file they came from."""
    report = (out_dir or (root / "files" / "check_runs")) / f"PMID{pmid}.json"
    if not report.is_file():
        return set(), ""
    try:
        data = json.loads(report.read_text(encoding="utf-8"))
    except ValueError:
        return set(), ""
    signals = {token for row in data.get("results", []) for token in row.get("signals", [])}
    try:
        shown = str(report.relative_to(root))
    except ValueError:
        shown = str(report)
    return signals, shown


def render_procedures(pmid: str, rows: list[dict[str, str]], inputs: list[str]) -> str:
    marks = {OPEN: "OPEN", NOT_NEEDED: "--  ", TO_ASCERTAIN: "??  "}
    lines = [f"PROCEDURES — PMID {pmid} · inputs: {' + '.join(inputs)}"]
    for row in rows:
        lines.append(f"  {marks[row['state']]} {row['phase']:<6} {row['name']}")
        lines.append(f"       {row['reason']}")
        if row["state"] == OPEN:
            for path in row["files"]:
                lines.append(f"       → {path}")
        elif row["to_ascertain"]:
            lines.append(f"       to ascertain: {row['to_ascertain']}")
    opened = [row["key"] for row in rows if row["state"] == OPEN]
    pending = [row["key"] for row in rows if row["state"] == TO_ASCERTAIN]
    lines.append(f"  open: {', '.join(opened) or 'none'} · to ascertain: {', '.join(pending) or 'none'}")
    lines.append("  OPEN = open the procedure · -- = not needed, on data that exist · "
                 "?? = unknown, and unknown is not 'not needed'")
    lines.append("  the mandatory method (brief § 0) is not in this list: it is always loaded")
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


def _shared_checkout(root: Path) -> Path | None:
    """The checkout that holds `files/` when `root` is a linked task worktree, else None."""
    try:
        done = subprocess.run(["git", "-C", str(root), "rev-parse", "--git-common-dir"],
                              capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    if done.returncode != 0 or not done.stdout.strip():
        return None
    common = Path(done.stdout.strip())
    common = common if common.is_absolute() else (root / common)
    top = common.resolve().parent
    return top if (top / "files").is_dir() else None


def _runnable(root: Path, disease: str, pmid: str, packet: dict[str, Any],
              artifact_workspace: str = "") -> list[tuple[str, list[str]]]:
    """The checks whose command this file can build with no human choice left in it."""
    names = {check["name"] for check in packet["applicable_checks"]}
    jobs: list[tuple[str, list[str]]] = []
    if "manifest validator" in names:
        # No explicit root given: from a linked task worktree that carries no files/fulltext,
        # default to the shared checkout that holds the gitignored bytes (2026-10-19, scientist-c).
        if not artifact_workspace and not (root / "files" / "fulltext").is_dir():
            shared = _shared_checkout(root)
            if shared is not None and shared != root.resolve():
                artifact_workspace = str(shared)
        jobs.append(("manifest validator",
                     [sys.executable, str(HERE / "deepdive_manifest.py"), "--disease", disease,
                      "--pmid", pmid, "--verify-artifacts", "--require-current-schema"]
                     # A task worktree holds the manifest but not the gitignored files/ tree;
                     # the validator already accepts a separate artifact root (2026-10-19, scientist-d).
                     # Resolved HERE, against the invoker's cwd: the child process runs from the
                     # repository root, so a relative value ("." typed inside a worktree) silently
                     # named the worktree and turned every locator into "No such file" (2026-10-19, scientist-a).
                     + (["--artifact-workspace", str(Path(artifact_workspace).resolve())] if artifact_workspace else [])))
        jobs.append(("flag drift",
                     [sys.executable, str(HERE / "manifest_flag_drift.py"), "--pmid", pmid]))
        jobs.append(("erratum scope",
                     [sys.executable, str(HERE / "erratum_scope_check.py"), "--root", str(root),
                      "--disease", disease, "--pmid", pmid]))
    jobs.append(("undeclared locator revision",
                 [sys.executable, str(HERE / "locator_contradiction_audit.py"), "--working-tree"]))
    return jobs


def run_checks(root: Path, disease: str, pmid: str, out_dir: Path | None = None,
               artifact_workspace: str = "") -> dict[str, Any]:
    packet = build(root, disease, pmid)
    out_dir = out_dir or (root / "files" / "check_runs")
    out_dir.mkdir(parents=True, exist_ok=True)
    detail = out_dir / f"PMID{pmid}.txt"
    started = time.monotonic()
    results = []
    with detail.open("w", encoding="utf-8") as handle:
        for name, argv in _runnable(root, disease, pmid, packet, artifact_workspace):
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
                            "state": state, "headline": line,
                            "signals": check_signals(name, code, output)})
    try:
        shown = str(detail.relative_to(root))
    except ValueError:          # an --out-dir outside the workspace, as the suite uses
        shown = str(detail)
    report = {"pmid": pmid, "detail": shown,
              "calls": len(results), "seconds": round(time.monotonic() - started, 1),
              "results": results}
    # The signals live beside the detail so `procedures` can read tokens, never the outputs.
    (out_dir / f"PMID{pmid}.json").write_text(json.dumps(report, indent=1, ensure_ascii=False),
                                               encoding="utf-8")
    signals = {token for row in results for token in row["signals"]}
    report["procedures_opened_by_checks"] = [
        row["key"] for row in procedures(packet["technical_facts"], signals)
        if row["state"] == OPEN and row["key"] not in {
            item["key"] for item in packet["procedures"] if item["state"] == OPEN}]
    return report


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
    opened = report.get("procedures_opened_by_checks") or []
    if opened:
        lines.append(f"  procedures opened by these results: {', '.join(opened)} "
                     f"(`paper_packet.py procedures --pmid {report['pmid']}`)")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("action", choices=("packet", "check", "procedures", "surfaces",
                                           "rank", "claim"))
    parser.add_argument("--actor", default="", help="claim only: your ACTOR_ID")
    parser.add_argument("--note", default="", help="claim only: one line, e.g. the task id")
    parser.add_argument("--pmid", required=True)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--artifact-workspace", default="",
                        help="check only: root that holds the gitignored files/ tree when --root is a task worktree")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--limit", type=int, default=RANK_RENDER_LIMIT,
                        help="rank only: how many ordinary candidates the human view prints; "
                             "0 prints them all. Likely-vector pages and unrankable surfaces are "
                             "always printed, and --json always carries every candidate")
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--observed", action="append", default=[],
                        choices=sorted(OBSERVED_CONDITIONS),
                        help="a condition the reading itself surfaced after the packet was built; "
                             "repeatable; closed vocabulary, so it cannot carry free text")
    args = parser.parse_args(argv)

    if not re.fullmatch(r"\d{6,9}", args.pmid):
        parser.error("--pmid must be a PubMed identifier")
    root = Path(args.root).resolve()

    if args.action == "claim":
        if not re.fullmatch(r"[a-z0-9-]+", args.actor):
            parser.error("claim needs --actor <ACTOR_ID>")
        others = [row for row in peer_work(root, args.disease, args.pmid)
                  if row["actor"] != args.actor]
        print(f"CLAIMED {args.pmid} for {args.actor}: {claim(root, args.pmid, args.actor, args.note)}")
        for row in others:
            print(f"  ALSO: {row['kind']} · {row['actor'] or '-'} · {row['note']} · {row['where']}")
        return 1 if others else 0

    if args.action == "packet":
        packet = build(root, args.disease, args.pmid)
        known = (packet["manifest"] or packet["artefacts"] or packet["prior_reading"]["receipts"]
                 or packet["acquisition_history"] or packet["identity"]["doi"])
        print(json.dumps(packet, indent=1, ensure_ascii=False) if args.json else render(packet))
        return 0 if known else 2

    if args.action == "surfaces":
        report = surfaces(root, args.disease, args.pmid)
        print(json.dumps(report, indent=1, ensure_ascii=False) if args.json
              else render_surfaces(report))
        return 0

    if args.action == "rank":
        # Always 0. `rank` is an answer, not a gate: nothing downstream may become conditional on
        # its exit status, and nothing it says is written anywhere.
        report = rank_surfaces(root, args.disease, args.pmid)
        print(json.dumps(report, indent=1, ensure_ascii=False) if args.json
              else render_rank(report, args.limit))
        return 0

    if args.action == "procedures":
        packet = build(root, args.disease, args.pmid)
        signals, source = load_check_signals(root, args.pmid,
                                             Path(args.out_dir).resolve() if args.out_dir else None)
        observed = set(args.observed)
        rows = procedures(packet["technical_facts"], signals, observed)
        inputs = ["packet"] + ([f"check run {source}"] if source else []) \
            + ([f"observed: {', '.join(sorted(observed))}"] if observed else [])
        if args.json:
            print(json.dumps({"pmid": args.pmid, "inputs": inputs, "procedures": rows},
                             indent=1, ensure_ascii=False))
        else:
            print(render_procedures(args.pmid, rows, inputs))
        return 0

    report = run_checks(root, args.disease, args.pmid,
                        Path(args.out_dir).resolve() if args.out_dir else None,
                        args.artifact_workspace)
    print(json.dumps(report, indent=1, ensure_ascii=False) if args.json else render_checks(report))
    return 1 if any(row["exit"] != 0 for row in report["results"]) else 0


if __name__ == "__main__":
    sys.exit(main())
