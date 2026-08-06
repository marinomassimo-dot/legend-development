#!/usr/bin/env python3
"""Phase-3 dry run: turn eligible occurrences into DisMech YAML, in staging only.

This writes a proposal. It is not a submission, it opens no pull request, and it touches
no canonical file. Its job is to fail closed rather than to produce plausible YAML: every
rule the specification spent eleven revisions establishing is a refusal here, not a warning.

What it refuses to do
---------------------
* emit `mechanism_confidence: ESTABLISHED` for a single-source proposition, or derive
  confidence from claim status (Rules E1, E3);
* omit `mechanism_confidence` at all — the pinned schema treats absence as ESTABLISHED, so
  silence is an upgrade (Rule E2);
* emit a `modifier` where the evidence does not fix a direction (Rule C2);
* emit `conforms_to` for a module whose conformance has not been assessed (Rule M1);
* pair SUPPORT with REFUTE across incomparable systems (Rule C1);
* export an occurrence whose epistemic type would be strengthened on the way out (Rule F1);
* claim the schema pin was verified when it was not.

Usage
-----
    export_dismech_dryrun.py --out-dir staging/dismech_dryrun
    export_dismech_dryrun.py --out-dir <dir> --schema-sha <sha>   # assert the pin
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[0] / "data"

sys.path.insert(0, str(HERE.parents[3] / "framework" / "scripts"))
from fulltext_receipts import active_receipts as _standing  # noqa: E402
SIDECAR = DATA / "dismech_sidecar_016_024_035.jsonl"
SPEC_PIN = "e1a5bde3b0d35b23808018648a8fc267dc96b10c"   # dismech.yaml blob, §0 of the spec
SPEC_COMMIT = "c43343af4054eeeab847621eaab1e10da7efde84"

# §10: entry-local nodes, no shared module. Both disorders are declared so that an entry
# receiving nothing is visible as a gap rather than absent from the output.
TARGETS = {
    "MONDO:0014533": "WWOX-Related Developmental and Epileptic Encephalopathy",
    "MONDO:0013687": "Autosomal Recessive Spinocerebellar Ataxia 12",
}
# Which target an occurrence's evidence speaks to. Authored, because it is a judgement:
# a molecular finding about WWOX is not automatically a finding about either disorder.
# Empty means "not assigned to a disease entry", and that is a reportable outcome.
#
# All three claims route to BOTH entries. The justification is this repository's own
# CLAIM 008 and CLAIM 017, both `consolidated baseline` / `DATO`: WOREE and SCAR12 form one
# genotype-phenotype spectrum, severe to milder, and CLAIM 030 adds that severity tracks
# residual protein FUNCTION rather than abundance. A finding about how WWOX works therefore
# describes the mechanism of both ends of one spectrum, not of one disorder.
#
# The two entries differ in phenotype and severity, not in mechanism — which is why the
# molecular nodes are shared and the clinical content is not.
#
# 🔴 The claim that licenses this routing is itself NOT exportable. CLAIM 008 and CLAIM 017
# have no source with a complete-read receipt, so they terminate in ELIGIBILITY_DEBT. The
# reason we may place a node on both entries is a claim we cannot yet put in either.
CLAIM_TARGETS = {"016": ["MONDO:0014533", "MONDO:0013687"],
                 "024": ["MONDO:0014533", "MONDO:0013687"],
                 "035": ["MONDO:0014533", "MONDO:0013687"]}
# PMIDs of the papers the routing claims cite, per their `Wikilinks` in the claim registry.
# Kept explicit rather than parsed: the routing basis is an authored judgement, and which
# papers it rests on must be visible to a reviewer, not inferred at run time.
ROUTING_BASIS_PMIDS = {
    "36779245": "PAPER 018 — Oliver 2023, source of CLAIM 017",
    "39507621": "PAPER 015 — Teplyshova 2024, source of CLAIM 017",
}


def sidecar_staleness(path: Path | None = None) -> str | None:
    """Return a refusal reason if the committed sidecar no longer matches a fresh derivation.

    The exporter reads a sidecar file, not the registries. So when a reading lands, the
    sidecar is stale until someone re-derives it — and until then this script emits YAML from
    superseded state and prints `DRY_RUN_SCHEMA_VERIFIED`, which is a success message about
    the wrong data.

    That is not hypothetical. On 2026-08-04 a `complete_fulltext_read` for PAPER 019 moved two
    CLAIM 016 occurrences out of `ELIGIBILITY_DEBT`, and the dry run kept reporting them as
    eligibility debt, successfully, because the file it reads had not been regenerated. Every
    other gate in this pipeline fails closed; this one reported green on stale input.

    Returns None when current. Never raises on a missing derivation module — an environment
    that cannot re-derive gets a refusal, not a silent pass.
    """
    target = path or SIDECAR
    if not target.is_file():
        return f"sidecar not found: {target}"
    derive_path = HERE / "derive_dismech_sidecar.py"
    if not derive_path.is_file():
        return f"cannot verify sidecar freshness: {derive_path.name} is missing"
    spec = importlib.util.spec_from_file_location("_derive_for_freshness", derive_path)
    if spec is None or spec.loader is None:
        return f"cannot load {derive_path.name} to verify sidecar freshness"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    produced = module.serialise(module.derive()).encode("utf-8")
    on_disk = target.read_bytes()
    if produced == on_disk:
        return None
    # A refusal message that can itself raise is a refusal that does not arrive: `relative_to`
    # throws for any path outside the repository, which is exactly the case a test uses.
    def show(path: Path) -> str:
        try:
            return str(path.relative_to(HERE.parents[3]))
        except ValueError:
            return str(path)

    return (f"sidecar is stale: {len(on_disk)} bytes on disk, {len(produced)} produced by a "
            f"fresh derivation. Re-derive it before exporting:\n"
            f"    python3 {show(derive_path)} --out {show(target)}")


def routing_basis_receipts(ledger: Path | None = None) -> dict[str, str]:
    """Which routing-basis papers carry a persisted `complete_fulltext_read` receipt.

    Measured, never asserted. This value was hardcoded `False` until 2026-08-04, which was
    true when it was written and silently stopped being true the moment a reading landed —
    exactly the failure the test suite's own docstring warns about: a constant that encodes
    the data at authoring time keeps reporting it long after the data moved.
    """
    path = ledger or (HERE.parents[2] / "wwox/registries/fulltext_read_receipts.jsonl")
    if not path.is_file():
        return {}
    backed: dict[str, str] = {}
    # A withdrawn receipt is not a routing basis. This read the raw ledger, so an invalidated
    # complete read still backed the export — and the invalidation event, which copies the
    # depth it exists to negate, backed it a second time.
    #
    # 🔴 DECLARED DEBT, 2026-08-06. `derive_dismech_sidecar.py` and
    # `dismech_independent_protocol.py` carry the SAME defect and are deliberately left
    # uncorrected: their SHA-256 is sealed into `dismech_phase2_baseline.json`, so editing
    # them — even to add this comment — breaks the Phase-2 provenance seal, and re-sealing
    # without re-deriving the sidecar would assert that sealed numbers came from code that
    # produced them when they did not. The seal is working as designed; the fix belongs in
    # the next re-derivation cycle, together with a re-seal. No live exposure today: the
    # ledger's only invalidation targets a `partial_fulltext_read`, and neither script is
    # reached by it. This note lives here because the two scripts that need it cannot carry
    # a comment without invalidating themselves.
    events = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
              if line.strip()]
    for record in _standing(events):
        pmid = str((record.get("study_id") or {}).get("pmid") or "")
        if pmid in ROUTING_BASIS_PMIDS and record.get(
                "evidence_depth") == "complete_fulltext_read":
            backed[pmid] = record["event_id"]
    return backed


def routing_justification(ledger: Path | None = None) -> dict:
    backed = routing_basis_receipts(ledger)
    exportable = bool(backed)
    justification = {
        "decision": "molecular WWOX findings route to both disease entries",
        "basis": ["CLAIM 008 (consolidated baseline, DATO): WOREE and SCAR12 form a "
                  "genotype-phenotype spectrum",
                  "CLAIM 017 (consolidated baseline, DATO): the disease spans severe "
                  "WOREE/WWOX-DEE to milder SCAR12-like phenotypes",
                  "CLAIM 030 (in observation): severity tracks residual protein function"],
        "basis_is_exportable": exportable,
        "basis_receipts": {ROUTING_BASIS_PMIDS[p]: e for p, e in sorted(backed.items())},
    }
    if exportable:
        justification["consequence"] = (
            "the routing now rests on sources with persisted complete-read receipts. It "
            "remains a curation judgement about WHICH entries a molecular finding describes; "
            "a backed basis makes the judgement defensible, it does not make it a node. "
            "CLAIM 008 still has no source with a complete read."
        )
    else:
        justification["basis_blocked_by"] = (
            "no source of CLAIM 008 or CLAIM 017 carries a complete-read receipt")
        justification["consequence"] = (
            "the routing is a curation judgement recorded here, not an asserted node")
    return justification

RELATION_TO_SUPPORTS = {"SUPPORT": "SUPPORT", "PARTIAL": "PARTIAL", "REFUTE": "REFUTE"}
TYPE_TO_RELATION = {"DATO": {"SUPPORT", "PARTIAL"}, "INFERENZA": {"PARTIAL"}}
EVIDENCE_SOURCE = {"MODEL_ORGANISM": "MODEL_ORGANISM", "IN_VITRO": "IN_VITRO",
                   "HUMAN_CLINICAL": "HUMAN_CLINICAL", "COMPUTATIONAL": "COMPUTATIONAL"}


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def evidence_source_for(context: str) -> str:
    """Read off the recorded context, never guessed from the journal."""
    lowered = context.lower()
    if "mouse" in lowered or "mice" in lowered or "murine" in lowered:
        return "MODEL_ORGANISM"
    if "patient" in lowered or "human clinical" in lowered:
        return "HUMAN_CLINICAL"
    if "in silico" in lowered or "modelling" in lowered:
        return "COMPUTATIONAL"
    return "IN_VITRO"


def confidence_for(occurrences: list[dict]) -> tuple[str, dict]:
    """Rules E1-E3. ESTABLISHED needs the schema's own bar and a recorded justification."""
    sources = {o["source_id"] for o in occurrences}
    types = {o["epistemic_type"] for o in occurrences}
    criteria = {
        "at_least_two_complete_read_sources": len(sources) >= 2,
        "sources_independent": None,          # unassessed: never assumed true
        "each_bears_on_this_proposition": None,
        "directness_adequate_for_scope": None,
        "contexts_comparable": None,
        "no_substantial_contrary_evidence": None,
    }
    if all(criteria.values()) and types == {"DATO"}:
        return "ESTABLISHED", criteria
    if types == {"INFERENZA"}:
        return "HYPOTHETICAL", criteria
    return "PROVISIONAL", criteria


def build(records: list[dict]) -> tuple[dict, list[dict]]:
    occurrences = [r for r in records if r["record_kind"] == "assertion_occurrence"]
    items = [r for r in records if r["record_kind"] == "representation_item"]
    losses: list[dict] = []

    eligible = [o for o in occurrences if o["terminal_state"] == "ELIGIBLE_FOR_EXPORT"]
    for o in occurrences:
        if o["terminal_state"] != "ELIGIBLE_FOR_EXPORT":
            losses.append({"kind": "ledger_a", "occurrence_id": o["occurrence_id"],
                           "claim_id": o["claim_id"], "state": o["terminal_state"],
                           "proposition": o["proposition"]})
    for i in items:
        losses.append({"kind": "ledger_b", "item_id": i["item_id"], "claim_id": i.get("claim_id"),
                       "state": i["representation_state"], "construct": i["construct_type"]})

    groups: dict[str, list[dict]] = defaultdict(list)
    for o in eligible:
        groups[o["evidence_assertion_id"]].append(o)

    entries = {mondo: {"name": name, "disease_term": {"id": mondo, "label": name},
                       "pathophysiology": []} for mondo, name in TARGETS.items()}
    attachments = 0
    unassigned: list[dict] = []
    provenance: list[dict] = []
    confidence_records: list[dict] = []

    for assertion_id, members in sorted(groups.items()):
        first = members[0]
        targets = sorted({t for m in members for t in CLAIM_TARGETS.get(m["claim_id"], [])})
        confidence, criteria = confidence_for(members)

        evidence = []
        for m in sorted(members, key=lambda x: x["occurrence_id"]):
            relation = m["evidence_relation"]
            if relation not in TYPE_TO_RELATION.get(m["epistemic_type"], {relation}):
                raise SystemExit(
                    f"REFUSED (Rule F1): {m['occurrence_id']} would export "
                    f"{m['epistemic_type']} as '{relation}'")
            locator = m.get("locator") or {}
            if not locator.get("snippet"):
                raise SystemExit(f"REFUSED: {m['occurrence_id']} is eligible without a snippet")
            evidence.append({
                "reference": f"PMID:{m['pmid']}",
                "supports": RELATION_TO_SUPPORTS[relation],
                "evidence_source": evidence_source_for(m.get("context") or ""),
                "snippet": locator["snippet"],
                "explanation": m["context"],
            })
            # Provenance is not a DisMech slot, and inventing one would produce YAML a
            # permissive reader silently ignores. It travels in a companion file instead,
            # keyed by occurrence, so the entry stays schema-clean and the receipt lineage
            # stays auditable. Losing it to satisfy a schema would discard the one thing
            # this pipeline exists to carry.
            provenance.append({
                "evidence_assertion_id": assertion_id,
                "occurrence_id": m["occurrence_id"],
                "originating_claim_id": m["claim_id"],
                "pmid": m["pmid"],
                "eligibility_receipt": m["eligibility_receipt_event"],
                "locator_extraction_receipt": m["locator_extraction_receipt_event"],
                "source_anchor": locator.get("anchor"),
                "raw_link_role_paper_to_claim": m.get("raw_link_role_paper_to_claim"),
                "claim_link_basis": m.get("claim_link_basis"),
                "epistemic_type": m["epistemic_type"],
                "evidence_relation": relation,
            })

        claims = sorted({m["claim_id"] for m in members})
        node = {
            "name": first["proposition"],
            "description": first["proposition"],
            "mechanism_confidence": confidence,        # Rule E2: never omitted
            # `notes` is a real slot, so the reviewer sees where this came from without
            # the entry carrying invented keys.
            "notes": (f"LEGEND {assertion_id}; from CLAIM {', '.join(claims)}. "
                      f"Provenance and receipt lineage in provenance.json."),
            "evidence": evidence,
        }
        confidence_records.append({"evidence_assertion_id": assertion_id,
                                   "mechanism_confidence": confidence,
                                   "criteria": criteria,
                                   "originating_claim_ids": claims})
        # Rule C2: no modifier is emitted at all — no occurrence records a signed direction.
        # Rule M1: no conforms_to — every candidate module is UNASSESSED.

        if not targets:
            unassigned.append({"evidence_assertion_id": assertion_id,
                               "proposition": first["proposition"],
                               "originating_claim_ids": claims})
            continue
        for mondo in targets:
            entries[mondo]["pathophysiology"].append(node)
            attachments += 1

    report = {
        "run_kind": "phase3_dry_run",
        "schema_pin": {"commit": SPEC_COMMIT, "blob_sha256": SPEC_PIN},
        "occurrences_enumerated": len(occurrences),
        "eligible": len(eligible),
        "evidence_assertions": len(groups),
        "node_evidence_attachments": attachments,
        "unassigned_to_any_disease_entry": unassigned,
        "routing_justification": routing_justification(),
        "ledger_a_losses": Counter(l["state"] for l in losses if l["kind"] == "ledger_a"),
        "ledger_b_losses": Counter(l["state"] for l in losses if l["kind"] == "ledger_b"),
        "losses": losses,
        "entries_emitted": {m: len(e["pathophysiology"]) for m, e in entries.items()},
        "provenance_records": len(provenance),
        "confidence_records": len(confidence_records),
    }

    # §5.4, identity one: every occurrence lands somewhere, exported or classified.
    accounted = len(eligible) + sum(1 for l in losses if l["kind"] == "ledger_a")
    if accounted != len(occurrences):
        raise SystemExit(f"REFUSED: identity A violated — {accounted} != {len(occurrences)}")
    # identity two: attachments are counted, never compared with assertion count.
    exported_members = sum(len(m) for a, m in groups.items()
                           if any(CLAIM_TARGETS.get(x["claim_id"]) for x in m))
    if attachments and exported_members == 0:
        raise SystemExit("REFUSED: attachments emitted with no exported member")
    return ({"entries": entries, "report": report, "provenance": provenance,
             "confidence": confidence_records}, losses)


def yaml_dump(value, indent: int = 0) -> str:
    """Minimal deterministic YAML. No library, so the bytes are ours and reproducible."""
    pad = "  " * indent
    if isinstance(value, dict):
        out = []
        for k, v in value.items():
            if isinstance(v, (dict, list)) and v:
                out.append(f"{pad}{k}:\n{yaml_dump(v, indent + 1)}")
            elif isinstance(v, (dict, list)):
                out.append(f"{pad}{k}: {{}}" if isinstance(v, dict) else f"{pad}{k}: []")
            else:
                out.append(f"{pad}{k}: {scalar(v)}")
        return "\n".join(out)
    if isinstance(value, list):
        out = []
        for element in value:
            if isinstance(element, (dict, list)):
                body = yaml_dump(element, indent + 1)
                out.append(f"{pad}-\n{body}")
            else:
                out.append(f"{pad}- {scalar(element)}")
        return "\n".join(out)
    return f"{pad}{scalar(value)}"


def scalar(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if any(ch in text for ch in ':#\n"\'') or text.strip() != text or not text:
        return json.dumps(text, ensure_ascii=False)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--schema-sha", help="assert the pinned dismech.yaml blob SHA")
    arguments = parser.parse_args()

    if "staging" not in arguments.out_dir.parts:
        raise SystemExit("REFUSED: the dry run writes to staging/ only")

    stale = sidecar_staleness()
    if stale:
        raise SystemExit(f"REFUSED: {stale}")

    verified = False
    if arguments.schema_sha:
        if arguments.schema_sha != SPEC_PIN:
            raise SystemExit(f"REFUSED (criterion 2): schema pin mismatch — "
                             f"expected {SPEC_PIN}, got {arguments.schema_sha}")
        verified = True

    built, _losses = build(load(SIDECAR))
    built["report"]["schema_pin"]["verified_at_run_time"] = verified
    built["report"]["run_status"] = ("DRY_RUN_SCHEMA_VERIFIED" if verified
                                     else "DRY_RUN_SCHEMA_UNVERIFIED")

    arguments.out_dir.mkdir(parents=True, exist_ok=True)
    for mondo, entry in sorted(built["entries"].items()):
        name = mondo.replace(":", "_") + ".yaml"
        (arguments.out_dir / name).write_text(yaml_dump(entry) + "\n", encoding="utf-8")

    report = built["report"]
    report["ledger_a_losses"] = dict(report["ledger_a_losses"])
    report["ledger_b_losses"] = dict(report["ledger_b_losses"])
    (arguments.out_dir / "provenance.json").write_text(
        json.dumps(built["provenance"], indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8")
    (arguments.out_dir / "confidence_criteria.json").write_text(
        json.dumps(built["confidence"], indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8")
    (arguments.out_dir / "loss_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"{report['run_status']}")
    print(f"  occurrences {report['occurrences_enumerated']} · eligible {report['eligible']} "
          f"· evidence assertions {report['evidence_assertions']} "
          f"· attachments {report['node_evidence_attachments']}")
    for mondo, count in sorted(report["entries_emitted"].items()):
        print(f"  {mondo}: {count} pathophysiology node(s)")
    if report["unassigned_to_any_disease_entry"]:
        print(f"  unassigned to any entry: {len(report['unassigned_to_any_disease_entry'])}")
    print(f"  losses — ledger A {report['ledger_a_losses']} · ledger B {report['ledger_b_losses']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
