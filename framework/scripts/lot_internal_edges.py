#!/usr/bin/env python3
"""What the papers in a lot are to each other - resolved at M0, not discovered at M5.

WHY THIS EXISTS
---------------
`scientist-b`'s closing sentence for wave 5 of the 2026-09-09 sweep:

    "A lot whose members cite each other should be read as a set and said to be one at M0,
     not discovered to be one at M5."

That sweep's sharpest cross-document finding - an editor's introduction reporting its own
author's chapter at a stronger epistemic grade than the chapter states, `we propose` turned
into `authors conclude` - exists ONLY because both papers happened to land in one wave, and
the actor "nearly wrote the first dossier as if it stood alone". The same shape recurred as
a debt closed four hours later by the next paper in the wave, and as a reagent-provenance
finding that made four apparently independent papers one.

The dispatch had the data to predict all three and did not look: baseline 0 of 3 task
contracts carried an `internal_edges` block, while at least four real edges existed. This
is the orchestrator's defect, in the retrospective's own classification (§ 4.5), and one
query over data the dispatch already has.

WHAT AN EDGE IS HERE
--------------------
    CITES               a member's reference list contains another member
    SAME_CONTAINER      same journal, volume and issue - a chapter and its editor's
                        introduction are related by the container, and NOT by citation
    SHARED_AUTHOR       identical first or last author
    REAGENT_CANDIDATE   a local dossier or manifest mentions another member's PMID within
                        a reagent context - a prompt to look, never an established edge

🔴 SAME_CONTAINER is not decoration. The four edges the retrospective named include
25238781 -> 25245215, and a citation-only detector finds it in neither direction: the
editorial's 11-item reference list does not contain the chapter it introduces. Measured
here before the tool was written. A detector built on citation alone would have reported
three of four and looked complete.

MEASURED SURFACE FACTS, 2026-09-10
----------------------------------
Europe PMC's `/references` endpoint returns **HTTP 503, "This API is temporarily
unavailable due to maintenance"** for every PMID tried. It is recorded here as a surface
fact rather than routed around silently. The route used instead is NCBI E-utilities
`elink` with `linkname=pubmed_pubmed_refs`, plus `esummary` for container and authorship -
both key-less, free, no registration and no external spend.

Positive control, reproduced by this tool: of the four edges the retrospective names,
`elink` supplies 27551470->25245215, 18460020->16223882 and 20530675->16223882, and
`esummary` supplies 25238781<->25245215 as SAME_CONTAINER + SHARED_AUTHOR.

    python3 framework/scripts/lot_internal_edges.py 25238781 25245215 27551470 ...
    python3 framework/scripts/lot_internal_edges.py --from-contract ledger/tasks/<a>/<T>.json
    python3 framework/scripts/lot_internal_edges.py --self-test        # offline, no network

Exit codes:
  0  the lot was screened and the edges reported (edges are NOT a failure)
  2  invalid invocation
  3  nothing could be screened - the result is void, not clean
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
DOSSIER_DIRS = (
    "disease-models/wwox/research/fulltext_dossiers",
    "disease-models/wwox/research/deepdive_manifests",
)
REAGENT_CONTEXT = re.compile(
    r"\b(antibod\w*|adenovir\w*|Ad-\w+|plasmid|construct|cell line|vector|"
    r"reagent|clone|siRNA|shRNA|primer)\b", re.I)
REAGENT_WINDOW = 300


@dataclass
class Edge:
    source: str
    target: str
    kind: str
    evidence: str


@dataclass
class Result:
    verdict: str
    lot: list[str] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    unscreenable: dict[str, str] = field(default_factory=dict)
    screened_refs: dict[str, int] = field(default_factory=dict)
    digest: str = ""
    missing: str = ""


def _get(url: str, timeout: int = 40) -> str:
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_references(pmid: str) -> tuple[list[str], str]:
    """PMIDs cited by `pmid`, or an empty list with the reason it could not be screened."""
    url = (f"{EUTILS}/elink.fcgi?dbfrom=pubmed&db=pubmed"
           f"&linkname=pubmed_pubmed_refs&id={pmid}&retmode=json")
    try:
        payload = json.loads(_get(url))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        return [], f"{type(exc).__name__}: {exc}"
    linksets = payload.get("linksets") or [{}]
    for linksetdb in linksets[0].get("linksetdbs") or []:
        if linksetdb.get("linkname") == "pubmed_pubmed_refs":
            return [str(x) for x in linksetdb.get("links") or []], ""
    # A record with no deposited reference list is UNSCREENABLE, not "cites nothing":
    # the distinction is the one this repository's worst near-error turned on.
    return [], "no pubmed_pubmed_refs linkset - reference list not deposited or not indexed"


def fetch_summaries(pmids: list[str]) -> tuple[dict[str, dict], str]:
    if not pmids:
        return {}, "empty lot"
    url = f"{EUTILS}/esummary.fcgi?db=pubmed&id={','.join(pmids)}&retmode=json"
    try:
        payload = json.loads(_get(url)).get("result", {})
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        return {}, f"{type(exc).__name__}: {exc}"
    return {uid: payload[uid] for uid in payload.get("uids", [])}, ""


def container_key(summary: dict) -> str:
    parts = [str(summary.get(field_name, "")).strip()
             for field_name in ("source", "volume", "issue")]
    return "|".join(parts) if all(parts) else ""


def local_reagent_edges(lot: list[str], root: Path) -> list[Edge]:
    """A member's local dossier or manifest naming another member near a reagent word."""
    edges: list[Edge] = []
    for source in lot:
        for directory in DOSSIER_DIRS:
            for path in (root / directory).glob(f"*{source}*"):
                try:
                    text = path.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                for target in lot:
                    if target == source:
                        continue
                    for match in re.finditer(re.escape(target), text):
                        window = text[max(0, match.start() - REAGENT_WINDOW):
                                      match.end() + REAGENT_WINDOW]
                        context = REAGENT_CONTEXT.search(window)
                        if context:
                            edges.append(Edge(
                                source, target, "REAGENT_CANDIDATE",
                                f"{path.name}: '{context.group(0)}' within "
                                f"{REAGENT_WINDOW} chars of {target}"))
                            break
    return edges


def screen(lot: list[str], root: Path = ROOT, *, offline: bool = False,
           pause: float = 0.35) -> Result:
    lot = [p.strip() for p in lot if p.strip()]
    if len(lot) < 2:
        return Result(verdict="INSUFFICIENT_DATA",
                      missing="a lot of fewer than two members has no internal edges")

    result = Result(verdict="SCREENED", lot=lot)
    digest = hashlib.sha256("|".join(sorted(lot)).encode()).hexdigest()
    result.digest = digest

    if not offline:
        for pmid in lot:
            references, problem = fetch_references(pmid)
            if problem:
                result.unscreenable[pmid] = problem
            result.screened_refs[pmid] = len(references)
            for target in lot:
                if target != pmid and target in references:
                    result.edges.append(Edge(
                        pmid, target, "CITES",
                        f"elink pubmed_pubmed_refs, {len(references)} references"))
            time.sleep(pause)

        summaries, problem = fetch_summaries(lot)
        if problem:
            result.unscreenable["__summaries__"] = problem
        containers: dict[str, list[str]] = {}
        authors: dict[str, list[str]] = {}
        for pmid, summary in summaries.items():
            key = container_key(summary)
            if key:
                containers.setdefault(key, []).append(pmid)
            for role in ("sortfirstauthor", "lastauthor"):
                name = str(summary.get(role, "")).strip()
                if name:
                    authors.setdefault(name, []).append(pmid)
        for key, members in containers.items():
            for i, source in enumerate(sorted(members)):
                for target in sorted(members)[i + 1:]:
                    result.edges.append(Edge(source, target, "SAME_CONTAINER", key))
        for name, members in authors.items():
            unique = sorted(set(members))
            for i, source in enumerate(unique):
                for target in unique[i + 1:]:
                    result.edges.append(Edge(source, target, "SHARED_AUTHOR", name))

    result.edges.extend(local_reagent_edges(lot, root))
    result.edges = _dedupe(result.edges)
    return result


def _dedupe(edges: list[Edge]) -> list[Edge]:
    """One edge per (source, target, kind), carrying how many surfaces witnessed it.

    A dossier and its manifest are two surfaces of one reading, so the same reagent
    mention arrives twice. Reporting it twice would inflate the only number this tool
    exists to produce.
    """
    seen: dict[tuple[str, str, str], Edge] = {}
    counts: dict[tuple[str, str, str], int] = {}
    for edge in edges:
        key = (edge.source, edge.target, edge.kind)
        counts[key] = counts.get(key, 0) + 1
        seen.setdefault(key, edge)
    for key, edge in seen.items():
        if counts[key] > 1:
            edge.evidence = f"{edge.evidence} (+{counts[key] - 1} more surface(s))"
    return list(seen.values())


def as_contract_block(result: Result) -> dict:
    return {
        "internal_edges": [
            {"source": e.source, "target": e.target, "kind": e.kind,
             "evidence": e.evidence} for e in result.edges
        ],
        "screened": {"lot_size": len(result.lot), "lot_digest": result.digest,
                     "references_seen": result.screened_refs},
        "unscreenable": result.unscreenable,
        "note": ("Edges resolved before assignment. A lot whose members cite each other, "
                 "share a container, an author or a reagent is read as a set and said to "
                 "be one at M0. UNSCREENABLE members are named, never treated as edgeless."),
    }


def render(result: Result) -> str:
    if result.verdict == "INSUFFICIENT_DATA":
        return f"INSUFFICIENT_DATA: {result.missing}"
    lines = [f"screened: lot={len(result.lot)} digest={result.digest[:16]} "
             f"references_seen={sum(result.screened_refs.values())}"]
    if result.unscreenable:
        lines.append(f"UNSCREENABLE members: {len(result.unscreenable)} "
                     f"({', '.join(sorted(result.unscreenable))})")
    if not result.edges:
        lines.append("no internal edges found - which is a result, not an absence of one, "
                     "only for the members that were screenable")
    for edge in sorted(result.edges, key=lambda e: (e.kind, e.source, e.target)):
        lines.append(f"  {edge.kind:<18} {edge.source} -> {edge.target}   {edge.evidence}")
    return "\n".join(lines)


def self_test() -> int:
    """Offline. Calls `screen` and `local_reagent_edges`, the module's entry points."""
    import tempfile

    passed, failed = 0, 0

    def check(name: str, condition: bool) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"  ok   {name}")
        else:
            failed += 1
            print(f"  FAIL {name}")

    check("a one-member lot is INSUFFICIENT_DATA, not edgeless",
          screen(["1"], offline=True).verdict == "INSUFFICIENT_DATA")
    check("an empty lot is INSUFFICIENT_DATA",
          screen([], offline=True).verdict == "INSUFFICIENT_DATA")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        dossiers = root / DOSSIER_DIRS[0]
        dossiers.mkdir(parents=True)
        (root / DOSSIER_DIRS[1]).mkdir(parents=True)
        (dossiers / "PMID111.md").write_text(
            "The adenovirus used here comes from PMID 222, as do both antibodies.",
            encoding="utf-8")
        (dossiers / "PMID333.md").write_text(
            "A discussion that merely cites 222 in passing about survival curves. " * 3,
            encoding="utf-8")
        edges = local_reagent_edges(["111", "222", "333"], root)
        check("a reagent word near a member's PMID is a REAGENT_CANDIDATE",
              any(e.source == "111" and e.target == "222" for e in edges))
        check("a bare mention with no reagent word is not an edge",
              not any(e.source == "333" for e in edges))

        (root / DOSSIER_DIRS[1] / "PMID111.json").write_text(
            '{"note": "the same adenovirus as PMID 222"}', encoding="utf-8")
        result = screen(["111", "222"], root=root, offline=True)
        check("offline screening still returns the local edges",
              result.verdict == "SCREENED" and len(result.edges) == 1)
        check("one edge per source/target/kind, with the surface count carried",
              "+1 more surface" in result.edges[0].evidence)
        block = as_contract_block(result)
        check("the contract block names what was screened",
              block["screened"]["lot_size"] == 2 and "internal_edges" in block)

    check("container_key refuses a partial container",
          container_key({"source": "J", "volume": "1"}) == ""
          and container_key({"source": "J", "volume": "1", "issue": "2"}) == "J|1|2")

    print(f"\nself-test: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pmids", nargs="*")
    parser.add_argument("--from-contract", type=Path,
                        help="task contract JSON carrying SCOPE.assigned_pmids")
    parser.add_argument("--json", action="store_true",
                        help="emit the internal_edges block for the task contract")
    parser.add_argument("--offline", action="store_true",
                        help="local evidence only; no network call")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    lot = list(args.pmids)
    if args.from_contract:
        contract = json.loads(args.from_contract.read_text(encoding="utf-8"))
        lot.extend(str(p) for p in (contract.get("SCOPE") or {}).get("assigned_pmids", []))
    if not lot:
        parser.error("give PMIDs or --from-contract")

    result = screen(lot, root=args.root, offline=args.offline)
    if args.json:
        print(json.dumps(as_contract_block(result), indent=1))
    else:
        print(render(result))
    return 3 if result.verdict == "INSUFFICIENT_DATA" else 0


if __name__ == "__main__":
    sys.exit(main())
