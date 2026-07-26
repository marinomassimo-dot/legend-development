#!/usr/bin/env python3
"""Run a thin slice of a Monarch + DGIdb repurposing workflow.

Given a gene seed, list selected knowledge-graph neighbours and the neighbours
with known drug interactions. The output is raw hypothesis material, never
evidence or medical advice.
"""

from __future__ import annotations

import argparse
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
    raise SystemExit(f"Gene {symbol!r} did not resolve to an HGNC identifier in Monarch.")


def neighbors(gene_id: str, limit: int) -> dict[str, set[str]]:
    items = _get(f"{MONARCH}/association?subject={gene_id}&limit={limit}").get("items", [])
    result: dict[str, set[str]] = {}
    for association in items:
        if association.get("category") not in NEIGHBOR_CATEGORIES:
            continue
        label = association.get("object_label")
        if not label or label.upper() == gene_id:
            continue
        result.setdefault(label, set()).add(association.get("predicate", "?").split(":")[-1])
    return result


def drugs_for(symbols: set[str]) -> dict[str, list[dict]]:
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
    nodes = data.get("data", {}).get("genes", {}).get("nodes", [])
    return {node["name"]: node.get("interactions", []) for node in nodes}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("gene", help="gene symbol used as the seed, for example WWOX")
    parser.add_argument("--limit", type=int, default=500, help="maximum Monarch associations to read")
    args = parser.parse_args()

    gene_id = resolve_gene(args.gene)
    gene_neighbors = neighbors(gene_id, args.limit)
    print(f"# thin slice — seed {args.gene} ({gene_id})")
    print(f"# Monarch KG neighbours: {len(gene_neighbors)}\n")

    targets = set(gene_neighbors) | {args.gene.upper()}
    try:
        hits = drugs_for(targets)
    except urllib.error.URLError as exc:
        print(f"DGIdb unavailable: {exc}", file=sys.stderr)
        return 1

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
