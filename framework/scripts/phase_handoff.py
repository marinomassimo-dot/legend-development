#!/usr/bin/env python3
"""The packet that lets a phase start in a NEW context, derived from artefacts and verified.

WHY THIS EXISTS
---------------
Research outlives a conversation. A reading, its comparison, its independent verification and its
integration are four phases, and today they are carried by one context that grows across all of
them: measured on 2026-09-12, a single comparison session reached 210,815 tokens of which 37,443
were fixed at birth, and the rest was instructions, the paper's own product, and records. Nothing
in that history is needed by the NEXT phase except what the artefacts already hold.

So the boundary between phases is where a context should be renewed, and the only thing that may
cross it is a packet DERIVED FROM PERSISTED ARTEFACTS — never a free summary, and never the
previous transcript. `scientist_reading_modes.md` §3.3 already forbids carrying prior LEGEND
output into a blind pass; this file generalises the same discipline to every boundary and makes
the crossing checkable.

🔴 WHAT "LOSSLESS" MEANS HERE, AND WHAT IT DOES NOT
--------------------------------------------------
It means every source and artefact stays whole, addressable and reopenable, and that the packet
carries the digest of each so a later phase can prove it is looking at the same bytes. It does
NOT mean the selection is scientifically complete: a packet cannot promise that no relevant record
was missed. Every packet says so in its own text, and `discovery` carries identifiers rather than
bodies precisely so that the next phase opens what it needs rather than trusting a précis.

TWO-STEP MEMORY
---------------
    discovery  — identifiers, why each is relevant, its kind, its digest, its links. Navigation.
    opening    — the command that returns the WHOLE record or the whole surface. Evidence.
An index is never evidence. An empty discovery is not evidence of absence, and says so.

PHASES, AND THE FIREWALL EACH KEEPS
-----------------------------------
    reading       refused here by design — the blind first pass takes `paper_packet.py packet`,
                  which carries technical state and no LEGEND conclusion.
    comparison    the reading's own product (manifest, dossier, receipt) + record DISCOVERY.
    verification  propositions, their quotes, their anchors and the source artefacts — and NOT
                  the producer's dossier, commit candidate or verdict.
    integration   everything persisted, plus the open questions nobody has closed.

    python3 framework/scripts/phase_handoff.py prepare --pmid 21731849 --phase comparison
    python3 framework/scripts/phase_handoff.py check --packet files/handoffs/PMID21731849-comparison.json

Exit codes:
  0  prepared / the packet still matches the artefacts
  1  drift: a reference is missing, a source changed, or an open question is no longer the same
  2  invalid invocation, or nothing to hand over
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import fulltext_receipts as receipts        # noqa: E402
import paper_packet as packet               # noqa: E402
import registry_records as records          # noqa: E402

PHASES = ("comparison", "verification", "integration")

# 🔴 The producer's conclusions. A verifier that reads these is not verifying, it is agreeing —
# the 2026-09-11 and 2026-09-12 verifications were worth what they were worth because the
# delegate never saw them. Named as data so a test can assert the absence.
PRODUCER_VERDICT_SURFACES = (
    "disease-models/{disease}/research/fulltext_dossiers/PMID{pmid}.md",
    "disease-models/{disease}/research/commit_candidates/",
)

NEXT_OPERATION = {
    "comparison": ("python3 framework/scripts/registry_records.py get --pmid {pmid} --hops 1"
                   "   # whole records; expand with --hops 2 / --theme / --id when a question opens"),
    "verification": ("open each artefact below at its declared digest and judge each proposition "
                     "against it; build your expected answers before reading anything else"),
    "integration": ("python3 framework/scripts/legend_lint.py .   # then the commit candidate, "
                    "then BATCH_COMMIT"),
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def reference(root: Path, rel: str, why: str) -> dict[str, Any]:
    """A reference is a path, a digest and a reason — never a copy of the thing."""
    path = root / rel
    return {"path": rel, "why": why, "present": path.is_file(),
            "sha256": sha256_file(path) if path.is_file() else "",
            "bytes": path.stat().st_size if path.is_file() else 0}


def receipt_for(root: Path, disease: str, pmid: str) -> dict[str, Any]:
    ledger = receipts.default_ledger_path(root, disease)
    if not ledger.is_file():
        return {}
    try:
        events = receipts.active_receipts(receipts.load_ledger(ledger))
    except Exception as error:                       # noqa: BLE001 - a broken chain is a fact
        return {"chain": f"UNREADABLE: {type(error).__name__}"}
    mine = [event for event in events
            if str((event.get("study_id") or {}).get("pmid")
                   if isinstance(event.get("study_id"), dict) else event.get("study_id")) == pmid]
    if not mine:
        return {}
    last = mine[-1]
    coverage = last.get("coverage") or {}
    return {"event_id": last.get("event_id"), "evidence_depth": last.get("evidence_depth"),
            "event_at": last.get("event_at"), "coverage": coverage,
            "owed": sorted(f"{key}={value}" for key, value in coverage.items()
                           if str(value).strip() not in {"read", "not_present"}),
            "ledger": str(ledger.relative_to(root)), "chain": "ok"}


def results_with_status(manifest: dict) -> list[dict[str, Any]]:
    """The reading's results as ADDRESSES, not as prose: proposition, surface, anchor, artifact.

    The epistemic tag (DATO / INFERENZA / IPOTESI) lives in the dossier, which the packet
    REFERENCES rather than copies — duplicating it here would create a second, drifting copy of
    a thing that is already addressable.
    """
    entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
    out = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue
        # 🔴 WHOLE, and the quote travels with the address. The first cut truncated every
        # proposition at 300 characters — mid-word — and carried no `snippet` at all, so two
        # condition-B readers (2026-09-12) could not write section A or E from the packet and
        # had to open the manifest anyway. A packet that ships pointers where the phase needs
        # content is a summary with a digest field.
        row = {"entry": index, "proposition": str(entry.get("proposition") or ""),
               "snippet": str(entry.get("snippet") or ""),
               "surface": entry.get("surface"), "anchor": entry.get("anchor"),
               "artifact": entry.get("artifact"),
               "relation": entry.get("panel_text_relation") or entry.get("relation") or "",
               # 🔴 ABSENT IS NOT FALSE. Rendering a missing key as `false` made a re-test reader
               # write "all 18 entries carry contradicts_locator: false" over a manifest in which
               # no entry carries the key at all — a false mechanism under a true conclusion.
               "contradicts_locator": (bool(entry.get("contradicts_locator"))
                                       if "contradicts_locator" in entry else "undeclared")}
        for extra in ("qualifies", "qualifies_needle", "experimental_context", "adjudicates"):
            if entry.get(extra):
                row[extra] = entry[extra]
        out.append(row)
    return out


# 🔴 WHAT THE READING LEAVES OPEN, THE COMPARISON MAY NOT CLOSE. On 2026-09-12 a comparison
# wrote that two secondary sources "place the same patients" in a phenotype block, where the
# dossier of the reading it was comparing says the identity "cannot be settled from either
# secondary source". The dossier was open in the reader's context; the sentence was still
# overwritten by a stronger one. So the packet names every point the reading itself declares
# unsettled — as an ADDRESS (dossier line, the marker phrase), never as a copy of the dossier's
# prose, which the comparison packet references and does not carry. The reader opens the line.
LEFT_OPEN_MARKERS = ("cannot be settled", "not adjudicated", "not adjudicable", "left unresolved",
                     "not resolved here", "registered, not adjudicated", "remains open",
                     "cannot be decided", "unresolved, deliberately", "cannot be separated",
                     # added 2026-09-12 after a survey over every landed dossier: a reading that
                     # writes `UNRESOLVED_AMBIGUITY, recorded and not resolved` was declaring
                     # exactly this and the list did not see it.
                     "unresolved_ambiguity", "recorded and not resolved",
                     "registrato e non risolto", "non risolto qui")


def left_open_by_the_reading(root: Path, disease: str, pmid: str) -> list[dict[str, str]]:
    dossier = root / f"disease-models/{disease}/research/fulltext_dossiers/PMID{pmid}.md"
    if not dossier.is_file():
        return []
    out: list[dict[str, str]] = []
    for number, line in enumerate(dossier.read_text(encoding="utf-8").splitlines(), start=1):
        lowered = line.lower()
        hits = [marker for marker in LEFT_OPEN_MARKERS if marker in lowered]
        if hits:
            out.append({"kind": "left open by the reading",
                        "what": f"{dossier.relative_to(root)}:{number} «{hits[0]}»",
                        "why": ("the reading declares this point unsettled at that line; the "
                                "comparison quotes the sentence from the dossier and may not "
                                "settle it, whatever a locator or a record seems to allow")})
    return out


def open_questions(root: Path, disease: str, pmid: str, manifest: dict,
                   receipt: dict, phase: str = "comparison") -> list[dict[str, str]]:
    """Everything nobody has closed — derived, so it cannot be forgotten by being unmentioned."""
    out: list[dict[str, str]] = []
    for owed in receipt.get("owed", []):
        out.append({"kind": "coverage", "what": owed,
                    "why": "a resumed reading owes this section; the receipt is not complete"})
    facts = packet.technical_facts(root, disease, pmid, manifest,
                                   packet.artefacts(root, disease, pmid, manifest))
    signals, _source = packet.load_check_signals(root, pmid)
    for row in packet.procedures(facts, signals):
        if row["state"] in (packet.OPEN, packet.TO_ASCERTAIN):
            out.append({"kind": f"procedure {row['state']}", "what": row["name"],
                        "why": row["reason"] + (f" — {row['to_ascertain']}" if row["to_ascertain"] else "")})
    surfaces = packet.surfaces(root, disease, pmid)
    for row in surfaces["surfaces"]:
        flags = [flag for flag in row["flags"] if flag != "MISDECLARED_CROP"]
        if flags:
            out.append({"kind": "surface", "what": row["path"], "why": "; ".join(flags)[:220]})
    for entry in results_with_status(manifest):
        if entry["contradicts_locator"] is True:
            out.append({"kind": "contradiction", "what": f"entries[{entry['entry']}]",
                        "why": "this entry contradicts a persisted locator; the audit travels with it"})
    dossier = root / f"disease-models/{disease}/research/fulltext_dossiers/PMID{pmid}.md"
    if dossier.is_file() and phase != "verification":
        out.append({"kind": "not in any field",
                    "what": "the reading's own self-corrections",
                    "why": ("withdrawn premises, hypotheses measured and discarded, contested "
                            "locators and their adjudication live as PROSE in "
                            f"{dossier.relative_to(root)} and in no structured field. M4b binds a "
                            "comparison to carry them: open the dossier")})
    if phase != "verification":
        # the verifier builds its expectations from the sources and never sees the dossier
        out.extend(left_open_by_the_reading(root, disease, pmid))
    check = manifest.get("retraction_check")
    if isinstance(check, dict):
        token = packet.notice_token(str(check.get("result") or ""))
        if token or check.get("corrected_items"):
            out.append({"kind": "integrity", "what": token or "corrected items declared",
                        "why": "an integrity notice bears on how this paper's evidence may be used"})
        dependencies = check.get("dependencies")
        if not isinstance(dependencies, dict):
            out.append({"kind": "integrity", "what": "retraction_check.dependencies absent",
                        "why": "the reference list has never been screened for this paper"})
    return out


# 🔴 THE BLOCKS M4b BINDS A COMPARISON TO CARRY. Both condition-B readers of 2026-09-12 reported
# the same gap: the packet named the manifest and the phase needed its CONTENT. These three are
# structured fields, small, and copied verbatim. The fourth thing M4b binds — the reading's own
# self-corrections — exists as PROSE in the dossier and in no structured field anywhere, so the
# packet names the gap instead of pretending to fill it (see `open_questions`).
MANDATED_BLOCKS = ("group_assessment", "retraction_check", "multihop")
# `group_assessment` is the reading's judgement of the authors, so a verifier does not get it.
VERIFICATION_WITHHOLDS = ("group_assessment",)


def mandated_blocks(manifest: dict, phase: str) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for name in MANDATED_BLOCKS:
        if phase == "verification" and name in VERIFICATION_WITHHOLDS:
            continue
        if manifest.get(name) is not None:
            out[name] = manifest[name]
    return out


def discovery(root: Path, disease: str, pmid: str, manifest: dict | None = None) -> dict[str, Any]:
    """Step one of two: identifiers and why, never bodies. Navigation, not evidence."""
    found = records.select(root, disease, pmid=pmid, hops=1)
    rows = []
    for record, why in found.hits:
        rows.append({"id": record.record_id[:90], "source": record.source, "line": record.line,
                     "why": why, "kind": record.kind, "digest": record.digest,
                     "bytes": len(record.text)})
    # 🔴 HOP 1 DOES NOT REACH A PAPER'S OWN REFERENCES. On 2026-09-12 a reader found the primary
    # its whole fidelity test ran against — the review's ref 23 — only through a `--theme`
    # expansion it chose to run; three of that comparison's load-bearing findings came from
    # records the packet never named. The manifest already enumerates the gene-direct references:
    # they are named here as identifiers to look up, which is navigation, not evidence.
    cited = []
    multihop = (manifest or {}).get("multihop") or {}
    for key in ("gene_direct_refs_in_source", "resolved", "queued", "references_enumerated"):
        value = multihop.get(key)
        if isinstance(value, list):
            for item in value:
                # A receipt id carries a date — `FTR-20260810-24550385-02` — and a date is eight
                # digits. On 2026-09-12 a packet named "20260810" as a PMID to look up. Receipt
                # ids are removed before the scan; a PMID that looks like a date is still a PMID.
                text = re.sub(r"\bFTR-\d{8}-\d+-\d+\b", " ", str(item))
                for candidate in re.findall(r"\b(\d{7,8})\b", text):
                    if candidate != pmid and candidate not in cited:
                        cited.append(candidate)
    # 🔴 AND THE CLAIMS THE READING ITSELF NAMES. Hop 1 from a PMID cannot reach a claim the
    # reading corroborated but was never written into: four of the five claims one reader needed
    # on 2026-09-12 were unreachable that way. `corpus_crossquery` and the manifest's own prose
    # already name them; they are seeded here as identifiers to look up.
    claims: list[str] = []
    blob = json.dumps((manifest or {}).get("corpus_crossquery") or {}) + json.dumps(
        (manifest or {}).get("landing") or []) + json.dumps((manifest or {}).get("multihop") or {})
    for candidate in re.findall(r"CLAIM\s+(\d{3})", blob):
        identifier = f"CLAIM {candidate}"
        if identifier not in claims:
            claims.append(identifier)
    return {"records": rows, "ambiguous": list(found.ambiguous), "unresolved": list(found.unresolved),
            "cited_by_this_paper": cited,
            "claims_named_by_the_reading": claims,
            "cited_note": ("PMIDs this paper's own manifest declares as gene-direct references. "
                           "Hop 1 does not reach them: look each up with `--pmid`, and expand by "
                           "`--theme` when the comparison opens a question"),
            "source_digests": dict(found.file_digests),
            "open_with": f"python3 framework/scripts/registry_records.py get --pmid {pmid} --hops 1",
            "limit": ("identifiers only. An index is not evidence: open the record. An empty "
                      "discovery is a statement about this query over these files, never evidence "
                      "that the laboratory does not know the paper.")}


def technical_history(root: Path, disease: str, pmid: str) -> dict[str, Any]:
    """What crosses the boundary from a finished technical history, and nothing else.

    The full logs stay where they are and are named here. What travels is: the valid artefact,
    the recipe that reproduces it, the limit that still applies, and the route that already
    failed — the four things that stop the next context repeating the work.
    """
    manifest = packet.load_manifest(root, disease, pmid)
    rows = packet.artefacts(root, disease, pmid, manifest)
    # The artefacts are already listed once, with digests, under `references`. Repeating them
    # here made the same 24 paths appear three times in one packet — about half its bytes, and a
    # reader reported it. What this section adds is the COUNT and the recipe availability.
    valid = {"count": sum(1 for row in rows if row["present"]),
             "with_recipe": sum(1 for row in rows if row["present"] and row["recipe"]),
             "listed_in": "references[] — each with its path and sha256"}
    failed = []
    for row in packet.acquisition_history(root, disease, pmid):
        verdict = str(row.get("verdict") or "")
        if verdict.startswith(("FAILED", "DIGEST_DIFFERS", "EXTRACTOR_DRIFT", "RECAPTCHA")):
            failed.append({"artifact": row.get("artifact_path"), "verdict": verdict,
                           "tier": row.get("tier"), "url": row.get("url")})
    surfaces = packet.surfaces(root, disease, pmid)
    limits = [f"{row['path']}: {'; '.join(f for f in row['flags'] if f != 'MISDECLARED_CROP')}"
              for row in surfaces["surfaces"]
              if [f for f in row["flags"] if f != "MISDECLARED_CROP"]]
    return {"valid_artefacts": valid, "failed_routes": failed, "standing_limits": limits,
            "full_logs": [f"disease-models/{disease}/research/retrieval_manifest.jsonl",
                          f"files/check_runs/PMID{pmid}.txt"],
            "note": ("a verified file does not certify the correctness of its interpretation; "
                     "reproduce with the recipe, do not re-derive the route")}


def prepare(root: Path, disease: str, pmid: str, phase: str) -> dict[str, Any]:
    manifest = packet.load_manifest(root, disease, pmid)
    receipt = receipt_for(root, disease, pmid)
    if manifest is None and not receipt:
        raise SystemExit(f"nothing persisted for PMID {pmid}: there is no phase to hand over")
    manifest_rel = str(packet.manifest_path(root, disease, pmid).relative_to(root))

    refs = []
    if manifest is not None:
        refs.append(reference(root, manifest_rel, "the reading's own record: locators, coverage, "
                                                  "retraction_check, group_assessment"))
    for artefact in (manifest or {}).get("source_artifacts") or []:
        if isinstance(artefact, dict) and artefact.get("path"):
            refs.append(reference(root, str(artefact["path"]),
                                  f"source artefact ({artefact.get('kind') or 'unknown kind'})"))
    if phase != "verification":
        dossier = f"disease-models/{disease}/research/fulltext_dossiers/PMID{pmid}.md"
        if (root / dossier).is_file():
            refs.append(reference(root, dossier, "the reading's dossier: epistemic tags, negatives, "
                                                 "limits — open it for the DATO/INFERENZA/IPOTESI status"))

    out: dict[str, Any] = {
        "record_kind": "phase_handoff",
        "phase": phase,
        "pmid": pmid,
        "disease": disease,
        "objective": {
            "comparison": "compare a landed reading against the laboratory's records (M4b), "
                          "after the receipt and never before it",
            "verification": "judge these propositions against their sources, independently",
            "integration": "carry the verified result into the record through the gates",
        }[phase],
        "boundary_crossed": "a phase finished, its artefacts are persisted, this context is new",
        "work_state": {"receipt": receipt, "manifest": manifest_rel if manifest else None,
                       "schema_version": (manifest or {}).get("schema_version"),
                       "landing": (manifest or {}).get("landing")},
        "results": results_with_status(manifest or {}),
        "open_questions": open_questions(root, disease, pmid, manifest or {}, receipt, phase),
        "coverage": {"receipt_coverage": receipt.get("coverage", {}),
                     "sections_owed": receipt.get("owed", []),
                     "surfaces_flagged": [row["path"] for row in
                                          packet.surfaces(root, disease, pmid)["surfaces"]
                                          if [f for f in row["flags"] if f != "MISDECLARED_CROP"]],
                     "surfaces_in_full": f"python3 framework/scripts/paper_packet.py surfaces --pmid {pmid}",
                     "cannot_promise": ("coverage of the SOURCES is stated here. Completeness of "
                                        "the record selection is not, and cannot be")},
        "technical_history": technical_history(root, disease, pmid),
        "references": refs,
        "next_operation": NEXT_OPERATION[phase].format(pmid=pmid),
        "excludes": [],
    }
    out["mandated_blocks"] = mandated_blocks(manifest or {}, phase)
    if phase == "comparison":
        out["discovery"] = discovery(root, disease, pmid, manifest)
    if phase == "verification":
        out["excludes"] = [surface.format(disease=disease, pmid=pmid)
                           for surface in PRODUCER_VERDICT_SURFACES]
        out["firewall"] = ("the producer's dossier, commit candidate and verdict are excluded by "
                           "construction: establish the expected answers from the sources first")
    if phase == "integration":
        out["discovery"] = discovery(root, disease, pmid, manifest)
    return out


def check(root: Path, packet_path: Path) -> dict[str, Any]:
    """Does the packet still describe the workspace? Drift is reported, never absorbed."""
    saved = json.loads(packet_path.read_text(encoding="utf-8"))
    drift: list[str] = []
    for ref in saved.get("references", []):
        path = root / ref["path"]
        # 🔴 Drift is a CHANGE OF STATE, not a state. An artefact that was already absent when the
        # packet was prepared — `files/` is gitignored, so on a fresh checkout most of them are —
        # is not drift: the packet said so and still says so. Reporting it as MISSING made every
        # packet on such a host read REBUILD, which is how a real warning gets ignored.
        was_present = bool(ref.get("present"))
        if was_present and not path.is_file():
            drift.append(f"MISSING: {ref['path']} — present when the packet was prepared, gone now")
            continue
        if not was_present and path.is_file():
            drift.append(f"APPEARED: {ref['path']} — absent when the packet was prepared and "
                         "readable now; the packet understates what this phase can open")
            continue
        if not path.is_file():
            continue
        if ref.get("sha256") and sha256_file(path) != ref["sha256"]:
            drift.append(f"CHANGED: {ref['path']} — digest differs from the one the packet recorded")
    fresh = prepare(root, saved["disease"], saved["pmid"], saved["phase"])
    was = {(item["kind"], item["what"]) for item in saved.get("open_questions", [])}
    now = {(item["kind"], item["what"]) for item in fresh["open_questions"]}
    for kind, what in sorted(now - was):
        drift.append(f"OPEN QUESTION NOT IN THE PACKET: {kind} — {what}")
    for kind, what in sorted(was - now):
        drift.append(f"OPEN QUESTION CLOSED SINCE PREPARATION: {kind} — {what}")
    return {"packet": str(packet_path), "phase": saved.get("phase"), "pmid": saved.get("pmid"),
            "drift": drift,
            "verdict": "USABLE" if not drift else "REBUILD — the inputs moved under the packet"}


def render(handover: dict[str, Any]) -> str:
    lines = [f"PHASE HANDOFF — PMID {handover['pmid']} → {handover['phase'].upper()}",
             f"  objective  : {handover['objective']}",
             f"  boundary   : {handover['boundary_crossed']}"]
    state = handover["work_state"]
    receipt = state.get("receipt") or {}
    lines.append(f"  work state : receipt {receipt.get('event_id') or '(none)'} · "
                 f"{receipt.get('evidence_depth') or 'no depth'} · chain {receipt.get('chain') or '-'}")
    if receipt.get("owed"):
        lines.append(f"      sections a resumed reading owes: {', '.join(receipt['owed'])}")
    lines.append(f"  results    : {len(handover['results'])} persisted locator(s) — "
                 "proposition, surface, anchor, artifact; epistemic tags in the dossier")
    lines.append(f"  open       : {len(handover['open_questions'])} question(s) nobody has closed")
    left_open = [item for item in handover["open_questions"] if item["kind"] == "left open by the reading"]
    if left_open:
        lines.append(f"  left open  : {len(left_open)} point(s) the reading itself declares unsettled — "
                     "open each dossier line; the comparison may not settle them")
    for item in handover["open_questions"][:8]:
        lines.append(f"      [{item['kind']}] {item['what']}")
    if len(handover["open_questions"]) > 8:
        lines.append(f"      … and {len(handover['open_questions']) - 8} more, in the packet")
    history = handover["technical_history"]
    lines.append(f"  technical  : {history['valid_artefacts']['count']} valid artefact(s), "
                 f"{len(history['failed_routes'])} route(s) already failed, "
                 f"{len(history['standing_limits'])} standing limit(s); full logs named, not carried")
    if handover.get("mandated_blocks"):
        lines.append(f"  carried    : {', '.join(sorted(handover['mandated_blocks']))} "
                     "(verbatim from the manifest — M4b binds the comparison to them)")
    if "discovery" in handover:
        found = handover["discovery"]
        lines.append(f"  discovery  : {len(found['records'])} record identifier(s), "
                     f"{len(found['ambiguous'])} ambiguity, {len(found['unresolved'])} unresolved link(s)")
        lines.append(f"      open them with: {found['open_with']}")
        if found.get("cited_by_this_paper"):
            lines.append(f"      hop 1 does NOT reach this paper's own references — look these up: "
                         f"{', '.join(found['cited_by_this_paper'][:9])}")
        if found.get("claims_named_by_the_reading"):
            lines.append(f"      claims the reading itself names: "
                         f"{', '.join(found['claims_named_by_the_reading'][:8])}")
    if handover.get("excludes"):
        lines.append(f"  excluded   : {', '.join(handover['excludes'])}")
    lines.append(f"  references : {len(handover['references'])} path(s), each with its digest")
    missing = [ref["path"] for ref in handover["references"] if not ref["present"]]
    if missing:
        lines.append(f"      ABSENT ON THIS HOST: {len(missing)} — {', '.join(missing[:3])}")
    lines.append(f"  next       : {handover['next_operation']}")
    lines.append("  lossless means the sources are whole and reopenable. It does NOT mean the "
                 "record selection is scientifically complete.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("action", choices=("prepare", "check"))
    parser.add_argument("--pmid", default="")
    parser.add_argument("--phase", choices=PHASES + ("reading",), default="comparison")
    parser.add_argument("--packet", default="")
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--out", default="")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--replace", action="store_true",
                        help="overwrite a packet already on disk; refused by default because a "
                             "packet a run was measured against is that run's evidence")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()

    if args.action == "check":
        if not args.packet:
            parser.error("--packet is required for check")
        report = check(root, Path(args.packet).resolve())
        if args.json:
            print(json.dumps(report, indent=1, ensure_ascii=False))
        else:
            print(f"HANDOFF CHECK — {report['packet']}")
            for line in report["drift"]:
                print(f"  {line}")
            print(f"  VERDICT: {report['verdict']}")
        return 0 if not report["drift"] else 1

    if args.phase == "reading":
        parser.error("a blind first reading takes `paper_packet.py packet --pmid <PMID>`: "
                     "this packet carries the reading's own product, which a blind pass may not see")
    if not re.fullmatch(r"\d{6,9}", args.pmid):
        parser.error("--pmid must be a PubMed identifier")
    handover = prepare(root, args.disease, args.pmid, args.phase)
    text = json.dumps(handover, indent=1, ensure_ascii=False)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if args.out:
        out = Path(args.out).resolve()
        # 🔴 A PACKET A RUN WAS MEASURED AGAINST IS EVIDENCE, AND EVIDENCE IS NOT OVERWRITTEN.
        # On 2026-09-12 the packets three pilot sessions had read were regenerated in place a few
        # minutes after those sessions closed. What the readers actually received could then be
        # reconstructed only from one reader's dump and another's transcript, and the analysis of
        # that pilot rests on those two accidents. Refuse, and name both digests.
        if out.is_file() and not args.replace:
            existing = sha256_file(out)
            if existing != digest:
                print(f"REFUSED: {out} already holds a different packet\n"
                      f"  on disk : {existing[:16]}\n"
                      f"  derived : {digest[:16]}\n"
                      f"  A packet a run was measured against is evidence. Write the new one "
                      f"beside it (--out <name>-v2.json) or pass --replace if nothing has read "
                      f"the one on disk.", file=sys.stderr)
                return 1
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    print(text if args.json else render(handover))
    if args.out and not args.json:
        print(f"  packet written: {args.out}")
        print(f"  packet sha256 : {digest}   # quote this in the run's log")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
