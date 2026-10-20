#!/usr/bin/env python3
"""Run a thin slice of a Monarch + DGIdb repurposing workflow.

Given a gene seed, list selected knowledge-graph neighbours and the neighbours with known
drug interactions. The output is raw hypothesis material, never evidence or medical advice.

🔴 WHAT THIS TOOL GUARANTEES, AND WHAT IT REFUSES TO GUESS
----------------------------------------------------------
* **Entity resolution is explicit.** A symbol is resolved to one stable identifier of one
  declared type in one declared species. `WWOX` alone matches human (`HGNC:12799`), dog and
  pig genes in Monarch; a thin slice that silently mixed them would be comparing species.
  The species filter is `--taxon` (human by default) and the resolution record keeps the
  candidates it rejected.
* **Pathways never become gene symbols.** Associations are typed before any DGIdb request:
  `GENE` (a pairwise gene-gene interaction carrying an HGNC identifier), `PATHWAY`
  (a gene-to-pathway association) or `UNRESOLVED`. Only `GENE` labels are sent to DGIdb.
  Pathways stay in the packet.
* **Truncation is stated, never silent.** Monarch associations are paginated by offset until
  the registry's own `total` is reached or `--limit` is hit; hitting the ceiling yields
  `INCOMPLETE` with the numbers that justify it.
* **Pharmacological actions and sources are preserved.** DGIdb interaction types (with
  directionality), source databases with their versions, and supporting publications are
  retained in the packet and summarised in the text output.
* **Errors are states, not zeros.** `QUERY_ERROR` (transport/shape), `API_ERROR` (a GraphQL
  `errors` block) and `INCOMPLETE` are each distinct from `NO_MATCH_FOUND`. An empty
  answer is an empty answer, never "there are no drugs".
* **Approved-only is a choice, not a default.** `--drug-approval {all,approved,
  investigational}` selects the view and the chosen value is printed with the result; the
  packet always carries every interaction returned. Different routes need different views:
  a repurposing route wants approved agents, a mechanism route wants the tool compounds too.

Network: public Monarch v3 and DGIdb GraphQL. Only the gene symbol and neighbour symbols
travel; no key, no account, no private data, zero spend.

Exit: 0 complete · 1 `QUERY_ERROR`/`API_ERROR`/unresolved seed · 3 `INCOMPLETE`
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SCHEMA_VERSION = 2
TOOL_VERSION = "kg_thin_slice/2.0.0"

MONARCH = "https://api-v3.monarchinitiative.org/v3/api"
DGIDB = "https://dgidb.org/api/graphql"
HUMAN = "NCBITaxon:9606"

GENE_GENE = "biolink:PairwiseGeneToGeneInteraction"
GENE_PATHWAY = "biolink:GeneToPathwayAssociation"
NEIGHBOR_CATEGORIES = {GENE_GENE, GENE_PATHWAY}

DGIDB_QUERY = """
query($names:[String!]!){
  genes(names:$names){
    nodes{
      name
      longName
      conceptId
      interactions{
        drug{ name conceptId approved }
        interactionScore
        interactionTypes{ type directionality }
        sources{ sourceDbName sourceDbVersion }
        publications{ pmid }
      }
    }
  }
}"""


class SliceError(ValueError):
    """A request did not complete. Distinct from a request that completed with no results.

    Derived from ``ValueError`` on purpose: `framework/scripts/test_repurposing_bridge.py`
    pins that an unusable Monarch/DGIdb document raises ``ValueError`` here, and that suite
    belongs to another tool. A refactor of this file may not quietly retire its contract.
    """


class ApiError(SliceError):
    """The service answered with an error document rather than data."""


def _get(url: str, timeout: int = 60) -> dict:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:  # pragma: no cover - network shape
        raise SliceError(f"HTTP {exc.code} for {url}") from exc
    except (urllib.error.URLError, OSError) as exc:  # pragma: no cover - network shape
        raise SliceError(f"transport failure for {url}: {exc}") from exc
    try:
        return json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SliceError(f"undecodable response for {url}: {exc}") from exc


def _post(url: str, payload: dict, timeout: int = 60) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:  # pragma: no cover - network shape
        raise SliceError(f"HTTP {exc.code} for {url}") from exc
    except (urllib.error.URLError, OSError) as exc:  # pragma: no cover - network shape
        raise SliceError(f"transport failure for {url}: {exc}") from exc
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SliceError(f"undecodable response for {url}: {exc}") from exc


def keep_original(raw_dir: Path | None, name: str, payload: dict) -> str | None:
    """Persist one original response and return the recorded path."""
    if raw_dir is None:
        return None
    raw_dir.mkdir(parents=True, exist_ok=True)
    safe = "".join(character if character.isalnum() else "_" for character in name)
    target = raw_dir / f"{safe}.json"
    target.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return str(target)


def resolve_gene(symbol: str, *, taxon: str = HUMAN, raw_dir: Path | None = None,
                 get=None) -> dict:
    """Resolve a gene symbol to one identifier of one type in one species.

    The returned record carries the identifier, the biolink type, the taxon and the
    candidates that were considered and not chosen — so a later reader can see that the
    non-human orthologues were present and were excluded on purpose.
    """
    get = get or _get
    url = f"{MONARCH}/search?q={urllib.parse.quote(symbol)}&category=biolink:Gene&limit=20"
    raw = get(url)
    items = raw.get("items")
    if not isinstance(items, list):
        raise SliceError(f"Monarch search response for {symbol!r} carries no items list")
    considered = [{"id": item.get("id"), "name": item.get("name"),
                   "category": item.get("category"), "taxon": item.get("in_taxon"),
                   "taxon_label": item.get("in_taxon_label")} for item in items]
    for item in items:
        if (str(item.get("name", "")).upper() == symbol.upper()
                and item.get("category") == "biolink:Gene"
                and item.get("in_taxon") == taxon
                and str(item.get("id", "")).startswith("HGNC:")):
            return {"query": url, "status": "OK", "id": item["id"], "label": item["name"],
                    "type": item["category"], "taxon": item.get("in_taxon"),
                    "taxon_label": item.get("in_taxon_label"),
                    "full_name": item.get("full_name"),
                    "identifier_namespace": "HGNC",
                    "candidates_considered": considered,
                    "original_response_path": keep_original(raw_dir,
                                                            f"monarch_search_{symbol}", raw)}
    raise SliceError(
        f"{symbol!r} did not resolve to a stable HGNC gene identifier in taxon {taxon} "
        f"({len(considered)} candidates considered). This is an UNRESOLVED seed, not an "
        f"absence of neighbours.")


def neighbor_packet(gene_id: str, limit: int, *, page_size: int = 100,
                    raw_dir: Path | None = None, get=None) -> dict:
    """Page through Monarch associations, typing each one, up to an EXPLICIT ceiling."""
    get = get or _get
    collected: list[dict] = []
    collected_raw: dict | list[dict] | None = None
    raw_pages: list[dict] = []
    pages: list[dict] = []
    total: int | None = None
    offset = 0
    while len(collected) < limit:
        want = min(page_size, limit - len(collected))
        url = (f"{MONARCH}/association?subject={urllib.parse.quote(gene_id)}"
               f"&limit={want}&offset={offset}")
        raw = get(url)
        items = raw.get("items")
        if not isinstance(items, list):
            raise SliceError("Monarch response missing items list")
        if isinstance(raw.get("total"), int) and not isinstance(raw.get("total"), bool):
            total = raw["total"]
        pages.append({"url": url, "offset": offset, "returned": len(items),
                      "original_response_path": keep_original(
                          raw_dir, f"monarch_assoc_{gene_id}_{offset}", raw)})
        raw_pages.append(raw)
        collected_raw = raw if len(raw_pages) == 1 else raw_pages
        collected.extend(items)
        offset += len(items)
        if not items or (total is not None and offset >= total):
            break

    entities = []
    for association in collected:
        if association.get("category") not in NEIGHBOR_CATEGORIES:
            continue
        entity_id = association.get("object")
        label = association.get("object_label")
        if not label or entity_id == gene_id:
            continue
        # Pathways and unresolved/non-human identifiers never become DGIdb gene names.
        if (association.get("category") == GENE_GENE and isinstance(entity_id, str)
                and entity_id.startswith("HGNC:")):
            entity_type = "GENE"
        elif association.get("category") == GENE_PATHWAY:
            entity_type = "PATHWAY"
        else:
            entity_type = "UNRESOLVED"
        entities.append({"id": entity_id, "label": label, "type": entity_type,
                         "predicate": association.get("predicate"), "raw": association})

    truncated = total is not None and len(collected) < total
    if truncated:
        status = "INCOMPLETE"
    elif not collected:
        status = "NO_MATCH"
    else:
        status = "OK"
    return {
        "query": pages[0]["url"] if pages else None,
        "pages": pages,
        "status": status,
        "registry_total": total,
        "associations_read": len(collected),
        "truncation": {
            "truncated": truncated,
            "statement": (f"read {len(collected)} of {total} associations — ceiling --limit="
                          f"{limit}; the remainder was NOT read"
                          if truncated else
                          f"read all {len(collected)} associations the registry reported"),
        },
        "counts_by_type": {kind: sum(1 for item in entities if item["type"] == kind)
                           for kind in ("GENE", "PATHWAY", "UNRESOLVED")},
        "entities": entities,
        "raw_response": collected_raw,
        "raw_response_pages": [page["original_response_path"] for page in pages],
    }


def neighbors(gene_id: str, limit: int) -> dict[str, set[str]]:
    """Gene-typed neighbour labels mapped to the predicates that reached them."""
    result: dict[str, set[str]] = {}
    for entity in neighbor_packet(gene_id, limit)["entities"]:
        if entity["type"] == "GENE":
            result.setdefault(entity["label"], set()).add(entity["predicate"] or "UNKNOWN")
    return result


def drug_packet(symbols: set[str], *, batch_size: int = 50, raw_dir: Path | None = None,
                post=None) -> dict:
    """Query DGIdb for gene symbols, in batches, preserving actions and sources."""
    post = post or _post
    ordered = sorted(symbols)
    batches: list[dict] = []
    interactions: dict[str, list[dict]] = {}
    long_names: dict[str, str | None] = {}
    for index in range(0, len(ordered), batch_size):
        names = ordered[index:index + batch_size]
        variables = {"names": names}
        data = post(DGIDB, {"query": DGIDB_QUERY, "variables": variables})
        if data.get("errors"):
            raise ApiError("DGIdb GraphQL errors: " + json.dumps(data["errors"]))
        nodes = ((data.get("data") or {}).get("genes") or {}).get("nodes")
        if not isinstance(nodes, list) or any(
            not isinstance(node, dict) or not isinstance(node.get("name"), str)
            or not isinstance(node.get("interactions"), list) for node in nodes
        ):
            raise SliceError("DGIdb response missing valid gene nodes/interactions")
        batches.append({"endpoint": DGIDB, "variables": variables,
                        "returned_nodes": len(nodes),
                        "original_response_path": keep_original(
                            raw_dir, f"dgidb_batch_{index // batch_size}", data)})
        for node in nodes:
            interactions.setdefault(node["name"], []).extend(node["interactions"])
            long_names[node["name"]] = node.get("longName")

    unmatched = sorted(symbols - set(interactions))
    if not symbols or not interactions:
        status = "NO_MATCH_FOUND"
    elif unmatched:
        status = "INCOMPLETE"
    else:
        status = "OK"
    return {
        "endpoint": DGIDB,
        "request": {"query": DGIDB_QUERY, "batch_size": batch_size,
                    "symbols_requested": ordered},
        "batches": batches,
        "status": status,
        "unmatched_symbols": unmatched,
        "coverage_statement": (
            f"{len(interactions)} of {len(symbols)} requested symbols were returned by DGIdb; "
            f"{len(unmatched)} were not. A symbol DGIdb does not know is UNMATCHED, which is "
            f"not the same as a gene with no drugs."),
        "interaction_coverage": "UNKNOWN",
        "long_names": long_names,
        "interactions": interactions,
    }


def drugs_for(symbols: set[str]) -> dict[str, list[dict]]:
    return drug_packet(symbols)["interactions"]


def select_by_approval(items: list[dict], approval: str) -> list[dict]:
    """The approval view is a CHOICE. 'all' is the default and nothing is dropped silently."""
    if approval == "all":
        return list(items)
    want = approval == "approved"
    return [item for item in items
            if bool((item.get("drug") or {}).get("approved")) is want]


def describe_actions(interaction: dict) -> str:
    actions = interaction.get("interactionTypes") or []
    if not actions:
        return "action UNKNOWN"
    return "; ".join(
        f"{(action.get('type') or 'UNKNOWN')}"
        f"/{(action.get('directionality') or 'UNKNOWN direction')}" for action in actions)


def describe_sources(interaction: dict) -> str:
    sources = interaction.get("sources") or []
    if not sources:
        return "source UNKNOWN"
    return ", ".join(f"{(source.get('sourceDbName') or 'UNKNOWN')}"
                     f"@{(source.get('sourceDbVersion') or 'unversioned')}"
                     for source in sources)


def main(argv: list[str] | None = None, get=None, post=None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("gene", help="gene symbol used as the seed, for example WWOX")
    parser.add_argument("--limit", type=int, default=500,
                        help="ceiling on Monarch associations read; reaching it reports "
                             "INCOMPLETE with the numbers, never a silent cut")
    parser.add_argument("--page-size", type=int, default=100,
                        help="Monarch association page size (offset pagination)")
    parser.add_argument("--taxon", default=HUMAN,
                        help=f"species the seed must resolve in (default {HUMAN}, human)")
    parser.add_argument("--drug-approval", choices=("all", "approved", "investigational"),
                        default="all",
                        help="which approval view the TEXT output shows; the packet always "
                             "keeps every interaction (default: all)")
    parser.add_argument("--batch-size", type=int, default=50,
                        help="gene symbols per DGIdb request")
    parser.add_argument("--raw-dir",
                        help="directory for the original responses; their paths are recorded")
    parser.add_argument("--json", action="store_true",
                        help="retain raw responses, actions and query provenance")
    args = parser.parse_args(argv)

    if args.limit < 1 or args.page_size < 1 or args.batch_size < 1:
        parser.error("--limit, --page-size and --batch-size must be positive")
    raw_dir = Path(args.raw_dir) if args.raw_dir else None

    seed = None
    monarch = None
    try:
        seed = resolve_gene(args.gene, taxon=args.taxon, raw_dir=raw_dir, get=get)
        monarch = neighbor_packet(seed["id"], args.limit, page_size=args.page_size,
                                  raw_dir=raw_dir, get=get)
        gene_neighbors: dict[str, set[str]] = {}
        for entity in monarch["entities"]:
            if entity["type"] == "GENE":
                gene_neighbors.setdefault(entity["label"], set()).add(
                    entity["predicate"] or "UNKNOWN")
        dgidb = drug_packet(set(gene_neighbors) | {args.gene.upper()},
                            batch_size=args.batch_size, raw_dir=raw_dir, post=post)
    # ValueError covers SliceError and a plain ValueError from a replaced resolver
    # (framework/scripts/test_repurposing_bridge.py drives exactly that case).
    except (ApiError, SliceError, ValueError, KeyError, TypeError,
            AttributeError) as exc:
        state = "API_ERROR" if isinstance(exc, ApiError) else "QUERY_ERROR"
        if args.json:
            print(json.dumps({"schema_version": SCHEMA_VERSION, "tool": TOOL_VERSION,
                              "status": state, "error": str(exc), "seed": seed,
                              "monarch": monarch, "seed_query": args.gene,
                              "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat()},
                             indent=2))
        else:
            print(f"{state}: {exc}", file=sys.stderr)
        return 1

    status = "INCOMPLETE" if "INCOMPLETE" in (monarch["status"], dgidb["status"]) else "OK"
    if args.json:
        print(json.dumps({
            "schema_version": SCHEMA_VERSION,
            "tool": TOOL_VERSION,
            "status": status,
            "seed": seed,
            "provenance": {"monarch_endpoint": MONARCH, "dgidb_endpoint": DGIDB,
                           "taxon": args.taxon, "limit": args.limit,
                           "page_size": args.page_size, "batch_size": args.batch_size,
                           "drug_approval_view": args.drug_approval},
            "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "epistemic_status": "ESPANSIONE",
            "monarch": monarch,
            "dgidb": dgidb,
        }, indent=2))
        return 0 if status == "OK" else 3

    print(f"# thin slice — seed {seed['label']} ({seed['id']}, {seed['type']}, "
          f"{seed['taxon_label']} / {seed['taxon']})")
    print(f"# Monarch coverage: {monarch['status']} — {monarch['truncation']['statement']}")
    print(f"# typed neighbours: {monarch['counts_by_type']} "
          f"(PATHWAY and UNRESOLVED never reach DGIdb)")
    print(f"# DGIdb coverage: {dgidb['status']} — {dgidb['coverage_statement']}")
    print(f"# approval view: --drug-approval {args.drug_approval} "
          f"(the packet keeps every interaction; use --json)\n")

    targets = set(gene_neighbors) | {args.gene.upper()}
    shown = {gene: select_by_approval(items, args.drug_approval)
             for gene, items in dgidb["interactions"].items()}
    druggable = {gene: items for gene, items in shown.items() if items}
    print(f"# neighbours with interactions in this view: {len(druggable)}/{len(targets)}\n")

    for gene, items in sorted(druggable.items(), key=lambda item: -len(item[1])):
        relations = ",".join(sorted(gene_neighbors.get(gene, {"seed"})))
        print(f"## {gene}  [{relations}]  — {len(items)} interactions in view "
              f"({len(dgidb['interactions'].get(gene, []))} total)")
        for interaction in items[:15]:
            drug = interaction.get("drug") or {}
            print(f"   - {drug.get('name', 'UNKNOWN')} "
                  f"({drug.get('conceptId', 'no concept id')}; "
                  f"{'approved' if drug.get('approved') else 'not approved'}) — "
                  f"{describe_actions(interaction)} — sources: "
                  f"{describe_sources(interaction)}")
        if len(items) > 15:
            print(f"   … {len(items) - 15} further interactions withheld from this printout "
                  f"only; all are in --json")
        print()

    print("---")
    print("Output = raw HYPOTHESIS material. It is not a claim or medical advice.")
    print("A status of NO_MATCH_FOUND, INCOMPLETE or UNMATCHED is not an absence of drugs.")
    print("Next: assess rationale with legend-hypothesis-forge, then apply")
    print("legend-safety-triage (BLOCK 1 / ADMET / BBB) before any promotion.")
    return 0 if status == "OK" else 3


if __name__ == "__main__":
    raise SystemExit(main())
