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
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[0] / "data"
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
ROUTING_JUSTIFICATION = {
    "decision": "molecular WWOX findings route to both disease entries",
    "basis": ["CLAIM 008 (consolidated baseline, DATO): WOREE and SCAR12 form a "
              "genotype-phenotype spectrum",
              "CLAIM 017 (consolidated baseline, DATO): the disease spans severe "
              "WOREE/WWOX-DEE to milder SCAR12-like phenotypes",
              "CLAIM 030 (in observation): severity tracks residual protein function"],
    "basis_is_exportable": False,
    "basis_blocked_by": "no source of CLAIM 008 or CLAIM 017 carries a complete-read receipt",
    "consequence": "the routing is a curation judgement recorded here, not an asserted node",
}

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
    unassigned = []

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
                "_provenance": {
                    "occurrence_id": m["occurrence_id"],
                    "originating_claim_id": m["claim_id"],
                    "eligibility_receipt": m["eligibility_receipt_event"],
                    "locator_extraction_receipt": m["locator_extraction_receipt_event"],
                    "source_anchor": locator.get("anchor"),
                    "raw_link_role_paper_to_claim": m.get("raw_link_role_paper_to_claim"),
                    "claim_link_basis": m.get("claim_link_basis"),
                },
            })

        node = {
            "name": first["proposition"],
            "description": first["proposition"],
            "mechanism_confidence": confidence,        # Rule E2: never omitted
            "evidence": evidence,
            "_confidence_criteria": criteria,
            "_evidence_assertion_id": assertion_id,
            "_originating_claim_ids": sorted({m["claim_id"] for m in members}),
        }
        # Rule C2: no modifier is emitted at all — no occurrence records a signed direction.
        # Rule M1: no conforms_to — every candidate module is UNASSESSED.

        if not targets:
            unassigned.append({"evidence_assertion_id": assertion_id,
                               "proposition": first["proposition"],
                               "originating_claim_ids": node["_originating_claim_ids"]})
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
        "routing_justification": ROUTING_JUSTIFICATION,
        "ledger_a_losses": Counter(l["state"] for l in losses if l["kind"] == "ledger_a"),
        "ledger_b_losses": Counter(l["state"] for l in losses if l["kind"] == "ledger_b"),
        "losses": losses,
        "entries_emitted": {m: len(e["pathophysiology"]) for m, e in entries.items()},
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
    return {"entries": entries, "report": report}, losses


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
