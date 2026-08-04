#!/usr/bin/env python3
"""Derive the Phase-2 DisMech sidecar for CLAIM 016 / 024 / 035.

Non-canonical. Reads the claim registry, writes a sidecar of assertion
candidates, occurrences and representation items. It is **not** the exporter:
it emits no YAML, no node, and nothing addressed to DisMech.

Division of labour, enforced by construction:

  authored  — the anchor of each candidate, the atomic propositions, their
              context and epistemic type, and the verbatim source snippets.
  computed  — every identifier, dedup key, evidence-assertion grouping,
              terminal state and accounting total.

The sidecar is **environment-independent**: it records the artefact fingerprint
*declared by the receipt*, never a hash measured on disk. A clean export has no
`files/` directory, and a derivation whose output depended on that would not be
reproducible in public. Re-hashing local artefacts is a separate audit,
`--audit-local-sources`, whose result never enters the records.

`raw_registry_span` is never authored: it is read out of the registry at the
declared anchor, and an anchor that does not resolve is a hard failure.

Usage
-----
    python3 derive_dismech_sidecar.py --out <file.jsonl>   # emit the sidecar
    python3 derive_dismech_sidecar.py --report             # accounting only
    python3 derive_dismech_sidecar.py --verify-bytes <file.jsonl>     # exact bytes
    python3 derive_dismech_sidecar.py --verify-semantic <file.jsonl>  # parsed records
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REGISTRY = Path(__file__).resolve().parents[2] / "registries" / "claim_registry_current.md"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

PAPER_REGISTRY = Path(__file__).resolve().parents[2] / "registries" / "paper_registry_current.md"
RECEIPT_LEDGER = Path(__file__).resolve().parents[2] / "registries" / "fulltext_read_receipts.jsonl"
REPO_ROOT = Path(__file__).resolve().parents[4]

SIDECAR_NAME = "dismech_sidecar_016_024_035.jsonl"

DEPTH_RANK = {"abstract_only": 0, "retrieved_not_read": 1, "queried_not_full_read": 2,
              "partial_fulltext_read": 3, "complete_fulltext_read": 4}


def read_claim_status(claim_id: str) -> str:
    """Claim status, read from the registry. Never authored."""
    text = REGISTRY.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n## CLAIM ", text)[1:] if b[:3] == claim_id]
    if not blocks:
        raise SystemExit(f"provenance failure: CLAIM {claim_id} not in the registry")
    m = re.search(r"\*\*Status:\*\*(.*)", blocks[0])
    if not m:
        raise SystemExit(f"provenance failure: CLAIM {claim_id} has no Status field")
    return m.group(1).strip()


def read_paper_block(paper_id: str) -> str:
    text = PAPER_REGISTRY.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n#+ PAPER ", text)[1:] if b[:3] == paper_id[-3:]]
    if not blocks:
        raise SystemExit(f"provenance failure: {paper_id} not in the paper registry")
    return blocks[0]


def read_paper_pmid(paper_id: str) -> str | None:
    m = re.search(r"PMID[:\s]*([0-9]{7,8})", read_paper_block(paper_id))
    return m.group(1) if m else None


def read_link(claim_id: str, paper_id: str) -> tuple[str | None, str | None, str]:
    """Return (raw role from paper->claim, raw role from claim->paper, direction)."""
    fwd = None
    m = re.search(r"\*\*Claim links:\*\*(.*)", read_paper_block(paper_id))
    if m:
        for part in m.group(1).split("\u00b7"):
            got = re.match(r"\s*(\d{3})\s*(?:\((.*?)\))?", part.strip())
            if got and got.group(1) == claim_id:
                fwd = (got.group(2) or "unqualified").strip()
    text = REGISTRY.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n## CLAIM ", text)[1:] if b[:3] == claim_id]
    body = blocks[0] if blocks else ""
    token = f"PAPER {paper_id[-3:]}"
    src_field = re.search(r"\*\*Source:\*\*(.*)", body)
    source_text = src_field.group(1).strip() if src_field else ""
    if token in source_text:
        back = "source_field"          # the claim names this paper as a source
    elif token in body:
        back = "wikilink_only"         # referenced somewhere, but not as a source
    else:
        back = None
    if fwd and back:
        direction = "both"
    elif fwd:
        direction = "paper->claim"
    elif back:
        direction = "claim->paper"
    else:
        raise SystemExit(
            f"provenance failure: no link recorded in either direction between "
            f"CLAIM {claim_id} and {paper_id}")
    return fwd, back, direction, source_text


def read_receipts(pmid: str) -> tuple[str | None, str | None, str | None, str | None]:
    """Return (best depth, eligibility event, locator-extraction event, fingerprint)."""
    if not RECEIPT_LEDGER.exists():
        raise SystemExit("provenance failure: receipt ledger missing")
    best_depth = best_event = fingerprint = None
    locator_event = None
    candidates: list[dict] = []
    for line in RECEIPT_LEDGER.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if r.get("study_id", {}).get("pmid") != pmid:
            continue
        depth = r.get("evidence_depth")
        if depth == "complete_fulltext_read" and (
                best_depth is None or DEPTH_RANK[depth] >= DEPTH_RANK[best_depth]):
            best_depth, best_event = depth, r["event_id"]
            fingerprint = r.get("source_fingerprint")
        elif best_depth is None or DEPTH_RANK.get(depth, -1) > DEPTH_RANK.get(best_depth, -1):
            best_depth, best_event = depth, r["event_id"]
            fingerprint = r.get("source_fingerprint")
        if r.get("workflow") == "phase2_locator_extraction":
            candidates.append(r)
    for r in candidates:
        problems = []
        if r.get("evidence_depth") != "queried_not_full_read":
            problems.append(f"depth is {r.get('evidence_depth')!r}, expected queried_not_full_read")
        if best_event and r.get("prior_receipt") != best_event:
            problems.append(f"prior_receipt {r.get('prior_receipt')!r} does not name the "
                            f"selected complete read {best_event!r}")
        if fingerprint and r.get("source_fingerprint") != fingerprint:
            problems.append("source_fingerprint differs from the complete read")
        if not any(str(o).endswith(SIDECAR_NAME) for o in r.get("outputs", [])):
            problems.append(f"outputs do not name {SIDECAR_NAME}")
        if problems:
            raise SystemExit(
                "provenance failure: locator-extraction receipt "
                f"{r['event_id']} for PMID {pmid} is not a valid child of the complete read — "
                + "; ".join(problems))
        locator_event = r["event_id"]
    return best_depth, best_event, locator_event, fingerprint


def verify_artefact(path_str: str | None, expected_sha: str | None) -> str:
    """Hash the artefact on disk and compare with the receipt fingerprint."""
    if not path_str or not expected_sha:
        return "not_applicable"
    path = REPO_ROOT / path_str
    if not path.exists():
        return "artefact_absent"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return "match" if digest == expected_sha else "MISMATCH"



# Hash contract: sha256 over the UTF-8 encoding of the parts joined by "|",
# each part str()-ed, no normalisation, truncated to 12 hex characters.
HASH_ALGO, HASH_JOIN, HASH_LEN = "sha256", "|", 12


def loc_status_seed(snippet: str | None, src_anchor: str | None) -> str:
    """Distinguish 'not extracted' from 'sought and not found' inside the key."""
    return "sought" if src_anchor else "unsought"


def fp(*parts: object) -> str:
    joined = HASH_JOIN.join(str(p) for p in parts)
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()[:HASH_LEN]


# --------------------------------------------------------------- registry ---
def _plain_label(label: str) -> str:
    """A heading without its decoration: no emoji, backticks or bold markers."""
    stripped = re.sub(r"[`*]", "", label)
    stripped = re.sub(r"[^\w\s()/.,'’\-–—]", " ", stripped, flags=re.UNICODE)
    return re.sub(r"\s+", " ", stripped).strip()


def _field_bodies(block: str) -> list[dict[str, str]]:
    """Split a claim block into its fields.

    A field ends at the next `**Label:**` *or at a horizontal rule*. Omitting the rule made
    the last field of every claim swallow the `---` separator, so its final sentence never
    compared equal to the same sentence read by anyone else.
    """
    fields: list[dict[str, str]] = []
    # The heading must start its line. Inline bold mid-sentence — CLAIM 035 carries
    # `**(2) Un avvertimento di misura:**` inside a field body — is not a new field, and
    # treating it as one silently truncates the field it sits in.
    matches = list(re.finditer(r"^\*\*([^*\n]{2,90}?):\*\*", block, re.M))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        body = block[start:end]
        rule = re.search(r"\n\s*---\s*(?:\n|$)", body)
        if rule:
            body = body[: rule.start()]
        fields.append({"label": match.group(1),
                       "plain": _plain_label(match.group(1)),
                       "body": body.strip()})
    return fields


def read_anchor(claim_id: str, field_label: str, sentence: int | None) -> str:
    """Return the verbatim registry text at an anchor, or raise."""
    text = REGISTRY.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n## CLAIM ", text)[1:] if b[:3] == claim_id]
    if not blocks:
        raise SystemExit(f"anchor failure: CLAIM {claim_id} not found")
    # Field headings carry markup: CLAIM 016 has `🔴 **\`PREMISE_TAG\` sul claim
    # esistente**`. An anchor may name the heading with or without that decoration — the
    # independent run wrote the plain form, and a verbatim-only match rejected it as a
    # missing field. Resolve on the decoration-free form, which is what a reader would
    # write, and keep the verbatim form working.
    body = None
    for candidate in _field_bodies(blocks[0]):
        if candidate["label"] == field_label or candidate["plain"] == _plain_label(field_label):
            body = candidate["body"]
            break
    if body is None:
        raise SystemExit(f"anchor failure: CLAIM {claim_id} has no field {field_label!r}")
    if sentence is None:
        return body
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\U0001F534⚠(«*])", body)
    # `sentence` is ZERO-BASED: the first sentence of a field is sent[0]. Left unstated in
    # the first contract, an independent run indexed from 1, and every anchor it produced
    # pointed one sentence late — 16 of 16 shared anchors compared different text, which
    # read as total semantic disagreement until the offset was found. A negative ordinal is
    # rejected rather than silently wrapping to the end of the list.
    if sentence < 0:
        raise SystemExit(
            f"anchor failure: sent[{sentence}] is negative — ordinals are zero-based, "
            f"the first sentence of a field is sent[0]")
    if sentence >= len(parts):
        raise SystemExit(
            f"anchor failure: CLAIM {claim_id} | {field_label} has "
            f"{len(parts)} sentences, sent[{sentence}] requested (ordinals are zero-based, "
            f"so the last is sent[{len(parts) - 1}])")
    return parts[sentence].strip()


def anchor_str(claim_id: str, field_label: str, sentence: int | None) -> str:
    """Build an anchor. The sentence ordinal is zero-based; see `read_anchor`."""
    tail = "" if sentence is None else f"|sent[{sentence}]"
    return f"claim_registry_current.md#CLAIM {claim_id}|{field_label}{tail}"


# --------------------------------------------------------------- authored ---
CLAIM_IDS = ("016", "024", "035")

# Only the artefact *path* is authored; its PMID, receipts, depth and fingerprint
# are read from the registries and the ledger, and the bytes are re-hashed on disk.
# A bare wikilink is a cross-reference, not a declaration of support: it must not
# silently become evidence. Only a paper named in the claim's Source field, or a
# qualified role declared by the paper registry, counts as supporting.
ROLE_NORM = {"source_field": "SUPPORTING", "wikilink_only": "UNQUALIFIED_REFERENCE",
             "unqualified": "SUPPORTING",
             "primary": "SUPPORTING", "new": "SUPPORTING", "enriches": "SUPPORTING",
             "Source: Cheng et al. 2020": "SUPPORTING", "secondary": "SUPPORTING",
             "supports": "SUPPORTING", "supplies the functional assay": "SUPPORTING",
             "tensions": "NON_SUPPORTING"}


AUTHORED = DATA_DIR / "dismech_authored_assertions.json"


def load_authored(path: Path = None) -> tuple[dict[str, str | None], list[tuple]]:
    """Load the authored judgement: which text becomes an assertion, and its locator.

    Kept outside the code deliberately. Everything the derivation computes — identifiers,
    dedup keys, grouping, terminal states — is derived from the registries and the ledger;
    this file holds the part that requires a reader. Adding claims is then data entry
    rather than editing a Python literal, which is what a corpus of hundreds of claims
    needs.
    """
    document = json.loads((path or AUTHORED).read_text(encoding="utf-8"))
    artefacts = document["artefact_path"]
    candidates: list[tuple] = []
    for entry in document["candidates"]:
        outcome = entry["outcome"]
        if outcome == "ATOMIZED":
            payload = [(o["proposition"], o["context"], o["epistemic_type"],
                        o["evidence_relation"], o["source_id"],
                        o.get("snippet"), o.get("source_anchor"))
                       for o in entry["occurrences"]]
        elif outcome == "NOT_EVIDENCE":
            payload = [(i["construct_type"], i["content"],
                        i["representation_state"], i["mitigation"])
                       for i in entry["items"]]
        else:
            payload = []
        candidates.append((entry["claim_id"], entry["field_label"],
                           entry["sentence"], outcome, payload))
    return artefacts, candidates


ARTEFACT_PATH, CANDIDATES = load_authored()

LEDGER_A_ORDER = ["STATUS_INELIGIBLE", "ATOMIZATION_REQUIRED", "IDENTIFIER_UNRESOLVED",
                  "ELIGIBILITY_DEBT", "LINK_ROLE_NON_SUPPORTING",
                  "LOCATOR_NOT_EXTRACTED", "LOCATOR_PROVENANCE_MISSING",
                  "SOURCE_SUPPORT_NOT_FOUND", "ELIGIBLE_FOR_EXPORT"]
LOSS_STATES = LEDGER_A_ORDER[:-1]


# --------------------------------------------------------------- computed ---
def derive() -> list[dict]:
    records: list[dict] = []
    for claim, label, sent, outcome, payload in CANDIDATES:
        span_text = read_anchor(claim, label, sent)          # fails closed
        anchor = anchor_str(claim, label, sent)
        claim_status = read_claim_status(claim)              # read, never authored
        cand_id = "CAND-" + fp(claim, anchor)
        cand = {"record_kind": "assertion_candidate", "candidate_id": cand_id,
                "claim_id": claim, "claim_status": claim_status,
                "registry_anchor": anchor, "raw_registry_span": span_text,
                "source_ids_observed": sorted({p[4] for p in payload}) if outcome == "ATOMIZED" else [],
                "atomization_outcome": outcome,
                "derived_occurrence_ids": [], "derived_item_ids": []}
        records.append(cand)

        if outcome == "ATOMIZED":
            for ordinal, (prop, ctx, etype, rel, src, snippet, src_anchor) in enumerate(payload):
                pmid = read_paper_pmid(src)
                depth, elig_r, loc_r, sha = read_receipts(pmid) if pmid else (None, None, None, None)
                artefact = ARTEFACT_PATH.get(src)
                fwd_role, back_role, direction, source_text = read_link(claim, src)
                raw_role = fwd_role if fwd_role else back_role
                norm_role = ROLE_NORM.get(raw_role, "UNMAPPED_ROLE")
                loc_fp = ("LF-" + fp(snippet, src_anchor)) if snippet else f"LF-none:{loc_status_seed(snippet, src_anchor)}"
                if snippet:
                    loc_status = "PRESENT"
                elif src_anchor:
                    loc_status = "SUPPORT_SOUGHT_NOT_FOUND"
                else:
                    loc_status = "NOT_EXTRACTED"

                if claim_status not in ("consolidated baseline", "in observation"):
                    state = "STATUS_INELIGIBLE"
                elif pmid is None:
                    state = "IDENTIFIER_UNRESOLVED"
                elif depth != "complete_fulltext_read":
                    state = "ELIGIBILITY_DEBT"
                elif norm_role != "SUPPORTING":
                    state = "LINK_ROLE_NON_SUPPORTING"
                elif loc_status == "NOT_EXTRACTED":
                    state = "LOCATOR_NOT_EXTRACTED"
                elif loc_status in ("PRESENT", "SUPPORT_SOUGHT_NOT_FOUND") and not loc_r:
                    state = "LOCATOR_PROVENANCE_MISSING"
                elif loc_status == "SUPPORT_SOUGHT_NOT_FOUND":
                    state = "SOURCE_SUPPORT_NOT_FOUND"
                else:
                    state = "ELIGIBLE_FOR_EXPORT"

                occ_id = "OCC-" + fp(claim, anchor, ordinal)
                records.append({
                    "record_kind": "assertion_occurrence", "occurrence_id": occ_id,
                    "candidate_id": cand_id, "claim_id": claim,
                    "claim_status": claim_status,
                    "registry_anchor": anchor, "registry_ordinal": ordinal,
                    "source_id": src, "pmid": pmid,
                    "eligibility_receipt_event": elig_r,
                    "eligibility_receipt_depth": depth,
                    "locator_extraction_receipt_event": loc_r if snippet or src_anchor else None,
                    "artefact": artefact, "artefact_sha256": sha,
                    "link_direction": direction, "raw_link_role": raw_role,
                    "raw_link_role_paper_to_claim": fwd_role,
                    "raw_link_role_claim_to_paper": None,
                    "claim_link_basis": back_role,
                    "claim_source_field": source_text or None,
                    "normalised_role": norm_role,
                    "proposition": prop, "context": ctx,
                    "content_fingerprint": "CF-" + fp(prop, ctx),
                    "locator": ({"snippet": snippet, "anchor": src_anchor,
                                 "artefact": artefact, "artefact_sha256": sha}
                                if snippet else {"snippet": None, "reason": src_anchor}),
                    "locator_status": loc_status,
                    "epistemic_type": etype, "evidence_relation": rel,
                    "locator_fingerprint": loc_fp,
                    "dedup_key": "DK-" + fp(src, prop, ctx, loc_fp, etype, rel),
                    "evidence_assertion_id": None,
                    "terminal_state": state,
                    "unreached_tests": LEDGER_A_ORDER[LEDGER_A_ORDER.index(state) + 1:]})
                cand["derived_occurrence_ids"].append(occ_id)

        elif outcome == "NOT_EVIDENCE":
            for ctype, content, rstate, mitigation in payload:
                item_id = "REP-" + fp(claim, anchor, ctype)
                records.append({"record_kind": "representation_item", "item_id": item_id,
                                "claim_id": claim, "occurrence_id": None,
                                "registry_anchor": anchor,
                                "construct_type": ctype, "content": content,
                                "representation_state": rstate,
                                "mitigation": mitigation, "flags": []})
                cand["derived_item_ids"].append(item_id)

    for src in sorted(ARTEFACT_PATH):
        pmid = read_paper_pmid(src)
        _d, elig_r, loc_r, _s = read_receipts(pmid) if pmid else (None, None, None, None)
        if elig_r:
            records.append({"record_kind": "representation_item",
                            "item_id": "REP-" + fp("lineage", src, elig_r),
                            "claim_id": None, "occurrence_id": None,
                            "registry_anchor": None,
                            "construct_type": "RECEIPT_LINEAGE",
                            "content": f"{src} eligibility {elig_r} / locator extraction {loc_r}",
                            "representation_state": "SCHEMA_LOSS",
                            "mitigation": "retained in the export report only", "flags": []})

    records.insert(0, {
        "record_kind": "derivation_manifest",
        "hash_contract": {"algorithm": HASH_ALGO, "join": HASH_JOIN,
                          "truncation": HASH_LEN, "encoding": "utf-8",
                          "canonicalisation": "none"},
        "dedup_key_components": ["source_id", "proposition", "context",
                                 "locator_fingerprint", "epistemic_type",
                                 "evidence_relation"],
        "occurrence_id_components": ["claim_id", "registry_anchor", "ordinal"],
        "anchor_format": {
            "shape": "claim_registry_current.md#CLAIM NNN|<field heading>|sent[n]",
            "sentence_ordinal_base": 0,
            "occurrence_ordinal_base": 0,
            "note": "Both ordinals are zero-based. Stated explicitly because leaving the "
                    "sentence base unstated made two independent derivations index from "
                    "different origins and compare different text.",
        },
        "provenance_sources": {
            "claim_status": "claim_registry_current.md",
            "pmid": "paper_registry_current.md",
            "link_paper_to_claim": "paper_registry_current.md, Claim links field",
            "link_claim_to_paper": "claim_registry_current.md — classified as "
                                   "claim_link_basis: source_field (supporting) or "
                                   "wikilink_only (cross-reference). This is a "
                                   "derived classification, not a verbatim role; the "
                                   "Source field text is kept as claim_source_field",
            "receipt_lineage_check": "prior_receipt must name the selected complete "
                                     "read. Direct parentage only — a full ancestry "
                                     "walk is not yet implemented, so a locator whose "
                                     "parent was later superseded by a receipt "
                                     "correction would be rejected rather than "
                                     "re-anchored",
            "receipts_and_fingerprints": "fulltext_read_receipts.jsonl",
            "artefact_bytes": "not re-hashed during derivation; the fingerprint is "
                              "the one declared by the receipt. Use "
                              "--audit-local-sources to compare against disk"},
        "serialisation": "one JSON object per line, sort_keys=True, ensure_ascii=False, "
                         "separators default, trailing newline per record",
    })

    groups: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        if r["record_kind"] == "assertion_occurrence" and r["terminal_state"] == "ELIGIBLE_FOR_EXPORT":
            groups[r["dedup_key"]].append(r)
    for key, members in groups.items():
        for r in members:
            r["evidence_assertion_id"] = "EA-" + fp(key)
    return records


def audit_local_sources() -> tuple[int, list[tuple[str, str]], dict[str, int]]:
    """Compare local artefacts against their receipt fingerprints.

    Returns (exit_code, per-source states, tallies). Exit codes:
      0 every expected artefact was compared and matched;
      1 at least one mismatch;
      2 audit incomplete — an expected artefact is absent. Absence is not a pass.
    """
    states: list[tuple[str, str]] = []
    tally = {"expected": 0, "match": 0, "mismatch": 0, "absent": 0}
    for src in sorted(ARTEFACT_PATH):
        pmid = read_paper_pmid(src)
        _d, _e, _l, sha = read_receipts(pmid) if pmid else (None, None, None, None)
        state = verify_artefact(ARTEFACT_PATH.get(src), sha)
        states.append((src, state))
        if state == "not_applicable":
            continue
        tally["expected"] += 1
        if state == "match":
            tally["match"] += 1
        elif state == "MISMATCH":
            tally["mismatch"] += 1
        elif state == "artefact_absent":
            tally["absent"] += 1
    if tally["mismatch"]:
        code = 1
    elif tally["absent"] or not tally["expected"]:
        code = 2
    else:
        code = 0
    return code, states, tally


def serialise(records: list[dict]) -> str:
    """The one serialisation the byte comparison is defined against."""
    return "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in records)


def accounting(records: list[dict]) -> dict:
    cands = [r for r in records if r["record_kind"] == "assertion_candidate"]
    occs = [r for r in records if r["record_kind"] == "assertion_occurrence"]
    items = [r for r in records if r["record_kind"] == "representation_item"]
    states = Counter(o["terminal_state"] for o in occs)
    all_keys: dict[str, list[dict]] = defaultdict(list)
    for o in occs:
        all_keys[o["dedup_key"]].append(o)
    return {
        "hash_contract": {"algorithm": HASH_ALGO, "join": HASH_JOIN,
                          "truncation": HASH_LEN, "encoding": "utf-8",
                          "canonicalisation": "none"},
        "candidates": len(cands),
        "candidate_outcomes": dict(Counter(c["atomization_outcome"] for c in cands)),
        "occurrences": len(occs),
        "ledger_a": {s: states.get(s, 0) for s in ["ELIGIBLE_FOR_EXPORT"] + LOSS_STATES},
        "identity_A_holds": len(occs) == sum(states.get(s, 0) for s in LEDGER_A_ORDER),
        "evidence_assertions": len({o["evidence_assertion_id"] for o in occs
                                    if o["evidence_assertion_id"]}),
        "node_evidence_attachments": 0,
        "ledger_b_items": len(items),
        "ledger_b_states": dict(Counter(i["representation_state"] for i in items)),
        "identity_B_holds": all(i.get("representation_state") for i in items),
        "candidate_closure_holds": all(
            (c["atomization_outcome"] == "ATOMIZED") == bool(c["derived_occurrence_ids"])
            and (c["atomization_outcome"] == "NOT_EVIDENCE") == bool(c["derived_item_ids"])
            for c in cands),
        "dedup_groups_multi_lineage": {
            k: sorted({o["claim_id"] for o in g}) for k, g in all_keys.items()
            if len({o["claim_id"] for o in g}) > 1},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, help="write the sidecar as JSONL")
    ap.add_argument("--report", action="store_true", help="print accounting only")
    ap.add_argument("--audit-local-sources", action="store_true",
                    help="re-hash the local full-text artefacts against the receipt "
                         "fingerprints (requires files/, absent from a clean export)")
    ap.add_argument("--verify-bytes", type=Path, metavar="FILE",
                    help="re-derive and compare the serialised bytes exactly")
    ap.add_argument("--verify-semantic", type=Path, metavar="FILE",
                    help="re-derive and compare the parsed records, ignoring serialisation")
    args = ap.parse_args()

    records = derive()

    if args.audit_local_sources:
        code, states, tally = audit_local_sources()
        for src, state in states:
            print(f"  {src:<12} {state}")
        if code == 1:
            print(f"AUDIT FAILED: {tally['mismatch']} of {tally['expected']} "
                  "artefacts do not match")
        elif code == 2:
            print(f"AUDIT INCOMPLETE: {tally['match']} of {tally['expected']} expected "
                  f"artefacts verified, {tally['absent']} absent — absence is not a pass")
        else:
            print(f"AUDIT PASSED: {tally['match']} of {tally['expected']} artefacts verified")
        return code

    if args.verify_bytes:
        produced = serialise(records)
        on_disk = args.verify_bytes.read_bytes()
        if produced.encode("utf-8") == on_disk:
            print(f"BYTES IDENTICAL: {len(records)} records serialise to the same bytes")
            return 0
        print(f"BYTES DIFFER: {len(on_disk)} bytes on disk vs "
              f"{len(produced.encode('utf-8'))} produced")
        return 1

    if args.verify_semantic:
        existing = [json.loads(l) for l in
                    args.verify_semantic.read_text(encoding="utf-8").splitlines() if l.strip()]
        if json.dumps(existing, sort_keys=True) == json.dumps(records, sort_keys=True):
            print(f"SEMANTICALLY IDENTICAL: {len(records)} records re-derive to equal objects "
                  f"(serialisation not compared — use --verify-bytes for that)")
            return 0
        ka = {r.get("occurrence_id") for r in existing if r["record_kind"] == "assertion_occurrence"}
        kb = {r.get("occurrence_id") for r in records if r["record_kind"] == "assertion_occurrence"}
        print(f"DIVERGENT: {len(existing)} vs {len(records)} records; "
              f"occurrence ids stable {len(ka & kb)}/{len(ka | kb)}")
        return 1

    if args.out:
        args.out.write_text(serialise(records), encoding="utf-8")
        print(f"written: {args.out} ({len(records)} records)")

    print(json.dumps(accounting(records), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
