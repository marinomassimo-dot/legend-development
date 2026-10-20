#!/usr/bin/env python3
"""Run a thin slice of a Monarch + DGIdb repurposing workflow.

Given a gene seed, list selected knowledge-graph neighbours and the neighbours
with known drug interactions. The output is raw hypothesis material, never
evidence or medical advice.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.error
import urllib.parse
import urllib.request


MONARCH = "https://api-v3.monarchinitiative.org/v3/api"
DGIDB = "https://dgidb.org/api/graphql"

NEIGHBOR_CATEGORIES = {
    "biolink:PairwiseGeneToGeneInteraction",
    "biolink:GeneToPathwayAssociation",
}


def _get(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.load(response)


def _post(url: str, payload: dict) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def resolve_gene(symbol: str) -> str:
    query = urllib.parse.quote(symbol)
    hits = _get(f"{MONARCH}/search?q={query}&category=biolink:Gene&limit=10").get("items", [])
    for hit in hits:
        if hit.get("name", "").upper() == symbol.upper() and hit["id"].startswith("HGNC:"):
            return hit["id"]
    raise ValueError(f"Gene {symbol!r} did not resolve to an HGNC identifier in Monarch.")


def neighbor_packet(gene_id: str, limit: int) -> dict:
    url = f"{MONARCH}/association?subject={urllib.parse.quote(gene_id)}&limit={limit}"
    raw = _get(url)
    if not isinstance(raw.get("items"), list):
        raise ValueError("Monarch response missing items list")
    items = raw["items"]
    result = []
    for association in items:
        if association.get("category") not in NEIGHBOR_CATEGORIES:
            continue
        entity_id = association.get("object")
        label = association.get("object_label")
        if not label or entity_id == gene_id:
            continue
        # Pathways and unresolved/non-human identifiers never become DGIdb gene names.
        is_gene = (association.get("category") == "biolink:PairwiseGeneToGeneInteraction"
                   and isinstance(entity_id, str) and entity_id.startswith("HGNC:"))
        result.append({"id": entity_id, "label": label,
                       "type": "GENE" if is_gene else "PATHWAY_OR_UNRESOLVED",
                       "predicate": association.get("predicate"), "raw": association})
    total = raw.get("total")
    complete = (isinstance(total, int) and not isinstance(total, bool) and total == len(items))
    return {"query": url, "status": "OK" if complete else "INCOMPLETE",
            "entities": result, "raw_response": raw}


def neighbors(gene_id: str, limit: int) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for entity in neighbor_packet(gene_id, limit)["entities"]:
        if entity["type"] == "GENE":
            result.setdefault(entity["label"], set()).add(entity["predicate"] or "UNKNOWN")
    return result


def drug_packet(symbols: set[str]) -> dict:
    """Query DGIdb for all gene symbols in one request."""
    query = """
    query($names:[String!]!){
      genes(names:$names){
        nodes{
          name
          interactions{
            drug{ name conceptId approved }
            interactionScore
            interactionTypes{ type directionality }
          }
        }
      }
    }"""
    data = _post(DGIDB, {"query": query, "variables": {"names": sorted(symbols)}})
    if data.get("errors"):
        raise ValueError("DGIdb GraphQL errors: " + json.dumps(data["errors"]))
    nodes = ((data.get("data") or {}).get("genes") or {}).get("nodes")
    if not isinstance(nodes, list) or any(
        not isinstance(node, dict) or not isinstance(node.get("name"), str)
        or not isinstance(node.get("interactions"), list) for node in nodes
    ):
        raise ValueError("DGIdb response missing valid gene nodes/interactions")
    unmatched = sorted(symbols - {node["name"] for node in nodes})
    return {"endpoint": DGIDB, "request": {"query": query, "variables": {"names": sorted(symbols)}},
            "status": "NO_MATCH_FOUND" if not nodes else "INCOMPLETE" if unmatched else "OK",
            "unmatched_symbols": unmatched, "interaction_coverage": "UNKNOWN",
            "raw_response": data,
            "interactions": {node["name"]: node["interactions"] for node in nodes}}


def drugs_for(symbols: set[str]) -> dict[str, list[dict]]:
    return drug_packet(symbols)["interactions"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("gene", help="gene symbol used as the seed, for example WWOX")
    parser.add_argument("--limit", type=int, default=500, help="maximum Monarch associations to read")
    parser.add_argument("--json", action="store_true", help="retain raw responses, actions and query provenance")
    args = parser.parse_args()

    if args.limit < 1:
        parser.error("--limit must be positive")
    monarch = None
    try:
        gene_id = resolve_gene(args.gene)
        monarch = neighbor_packet(gene_id, args.limit)
        gene_neighbors: dict[str, set[str]] = {}
        for entity in monarch["entities"]:
            if entity["type"] == "GENE":
                gene_neighbors.setdefault(entity["label"], set()).add(entity["predicate"] or "UNKNOWN")
        dgidb = drug_packet(set(gene_neighbors) | {args.gene.upper()})
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        if args.json:
            print(json.dumps({"status": "QUERY_ERROR", "error": str(exc),
                              "monarch": monarch, "seed_query": args.gene}))
        else:
            print(f"QUERY_ERROR: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps({"schema_version": 1, "seed": {"id": gene_id, "label": args.gene},
                          "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                          "epistemic_status": "ESPANSIONE", "monarch": monarch, "dgidb": dgidb}, indent=2))
        return 0
    print(f"# thin slice — seed {args.gene} ({gene_id})")
    print(f"# Monarch coverage: {monarch['status']}; raw responses available with --json")
    print(f"# Monarch KG neighbours: {len(gene_neighbors)}\n")

    targets = set(gene_neighbors) | {args.gene.upper()}
    hits = dgidb["interactions"]

    druggable = {gene: interactions for gene, interactions in hits.items() if interactions}
    print(f"# neighbours with known DGIdb drugs: {len(druggable)}/{len(targets)}\n")

    for gene, interactions in sorted(druggable.items(), key=lambda item: -len(item[1])):
        relations = ",".join(sorted(gene_neighbors.get(gene, {"seed"})))
        approved = sorted(
            interaction["drug"]["name"]
            for interaction in interactions
            if interaction.get("drug", {}).get("approved")
        )
        print(
            f"## {gene}  [{relations}]  — {len(interactions)} interactions, "
            f"{len(approved)} approved"
        )
        if approved:
            print("   approved: " + ", ".join(approved[:15]))
        print()

    print("---")
    print("Output = raw HYPOTHESIS material. It is not a claim or medical advice.")
    print("Next: assess rationale with legend-hypothesis-forge, then apply")
    print("legend-safety-triage (BLOCK 1 / ADMET / BBB) before any promotion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
