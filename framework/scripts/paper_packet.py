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
    for item in (manifest or {}).get("source_artifacts") or []:
        if not isinstance(item, dict):
            continue
        rel = str(item.get("path") or "")
        declared_paths.add(rel)
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
        "technical_facts": technical_facts(root, disease, pmid, manifest, rows),
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
                                    and not row["declared"]),
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
    parser.add_argument("action", choices=("packet", "check", "procedures", "surfaces"))
    parser.add_argument("--pmid", required=True)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--observed", action="append", default=[],
                        choices=sorted(OBSERVED_CONDITIONS),
                        help="a condition the reading itself surfaced after the packet was built; "
                             "repeatable; closed vocabulary, so it cannot carry free text")
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

    if args.action == "surfaces":
        report = surfaces(root, args.disease, args.pmid)
        print(json.dumps(report, indent=1, ensure_ascii=False) if args.json
              else render_surfaces(report))
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
                        Path(args.out_dir).resolve() if args.out_dir else None)
    print(json.dumps(report, indent=1, ensure_ascii=False) if args.json else render_checks(report))
    return 1 if any(row["exit"] != 0 for row in report["results"]) else 0


if __name__ == "__main__":
    sys.exit(main())
