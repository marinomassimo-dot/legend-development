#!/usr/bin/env python3
"""Measured ChEMBL activities reached by TARGET, for a molecule that has no mechanism row and so is missed by the by-symbol catalogue lookup.

WHY THIS EXISTS (2026-11-10, HE44 H1)
-------------------------------------
`repurposing_search.py need` reaches a molecule through the catalogue's target rows (ChEMBL curated mechanism, DGIdb, GtoPdb interactions). A molecule with a ChEMBL
record and a measured activity on the target, but no mechanism row, has no target row and is not reached: azetukalner (CHEMBL5095264) had zero rows on KCNQ2 while ChEMBL
holds a human EC50 on KCNQ2 (SCI43). The ChEMBL adapter already knows how to read a target by UniProt accession and the activities of a target with a coverage state; this
layer only composes them and keeps what they return. It adds no table of names and no vocabulary.

  gene symbol -> UniProt accession (the pinned GtoPdb target table; it must be unique) -> ChEMBL targets by accession (single protein, complex and organism kept apart)
  -> the activities of each human target (the adapter's coverage state kept) -> rows grouped by molecule, each row a `measurement` (original value, unit, relation kept)

Kept per row: molecule id, parent and name, target id and type, organism, assay organism-context, quantity (type, relation, value, unit, p-value), document, data-validity comment.
NOT assigned: an activity is not agonism, antagonism, selectivity or efficacy; `direction` and `selectivity` stay empty. A target of type complex is marked: which subunit carries
the activity is not decided here. `reached_by_target_path` says whether the catalogue's own target rows for the gene already name the molecule.

States of the answer (existing words): UNRESOLVED_SYMBOL (no unique accession: not an empty list), READ_ERROR (the adapter failed: not "no compounds"), READ_INCOMPLETE (a
truncated or partly failed read: not "all compounds"), NO_ACTIVITY_ROWS (a complete read of the scope that found none: said for this scope and release, not for the compound), OK.

  python3 framework/scripts/target_activity.py KCNQ2 --max-rows 400 --cache /tmp/chembl_cache_<release>
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import measurement as ms  # noqa: E402


def accession_for(symbol: str, rows: list[dict]) -> tuple[str | None, str]:
    """(UniProt accession, state). The pinned GtoPdb target table must carry exactly one human accession for the symbol."""
    s = symbol.strip().upper()
    acc = sorted({r["Human SwissProt"] for r in rows if r.get("HGNC symbol", "").strip().upper() == s and r.get("Human SwissProt", "").strip()})
    if len(acc) == 1:
        return acc[0], "OK"
    return None, "UNRESOLVED_SYMBOL" if not acc else "UNRESOLVED_SYMBOL_AMBIGUOUS"


def load_gtopdb_targets(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        if not f.readline().lstrip('"').startswith("#"):
            f.seek(0)
        return list(csv.DictReader(f))


def catalogue_reach(entries: list[dict], symbol: str) -> set[str]:
    """ChEMBL ids of the catalogue records that already carry a target row naming the gene: the molecules the by-symbol path reaches."""
    s = symbol.upper()
    out = set()
    for e in entries:
        for t in e.get("targets") or []:
            syms = {x.upper() for x in (t.get("gene_symbols") or [])} | ({t["gene"].upper()} if t.get("gene") else set())
            if s in syms:
                cid = (e.get("ids") or {}).get("chembl") or (e["id"].split(":", 1)[1] if e["id"].startswith("CAT:CHEMBL") else None)
                parent = ((e.get("relations") or {}).get("parent") or "").replace("CAT:", "")     # a salt record reaches its parent too: the activity row may sit on either
                out |= {x for x in (cid, parent) if x}
                break
    return out


def activities_for_gene(symbol: str, query, accessions: list[dict], *, reached: set[str] | None = None, catalogue_ids: set[str] | None = None, types=None, max_rows: int = 400,
                        organism: str = "Homo sapiens") -> dict:
    """`query(request) -> adapter answer`. `accessions` is the GtoPdb target table."""
    out = {"gene": symbol, "state": "OK", "accession": None, "targets": [], "reads": [], "molecules": [], "note": ""}
    acc, st = accession_for(symbol, accessions)
    if not acc:
        out["state"] = st
        out["note"] = "the pinned GtoPdb target table does not give exactly one human accession for this symbol; nothing was read"
        return out
    out["accession"] = acc
    tg = query({"uniprot": acc})
    if tg.get("status") not in ("MATCH_FOUND", "NO_MATCH_FOUND"):
        out["state"], out["note"] = "READ_ERROR", f"target lookup by accession failed: {str(tg.get('error'))[:160]}"
        return out
    targets = [h for h in tg.get("hits") or [] if h.get("kind") == "target"]
    out["targets"] = [{k: h.get(k) for k in ("target_chembl_id", "pref_name", "organism", "target_type", "accessions")} for h in targets]
    out["source_version"] = tg.get("source_version")
    todo = [h for h in targets if h.get("organism") == organism]
    if not todo:
        out["state"], out["note"] = "NO_ACTIVITY_ROWS", f"no {organism} ChEMBL target carries accession {acc}"
        return out
    by_mol: dict[str, dict] = {}
    errors = incomplete = 0
    for h in todo:
        ans = query({"target": h["target_chembl_id"], "types": types, "max_rows": max_rows} if types else {"target": h["target_chembl_id"], "max_rows": max_rows})
        cov = ans.get("coverage")
        out["reads"].append({"target_chembl_id": h["target_chembl_id"], "status": ans.get("status"), "coverage": cov, "retrieved": ans.get("retrieved"), "total_count": ans.get("total_count")})
        if ans.get("status") not in ("MATCH_FOUND", "NO_MATCH_FOUND"):
            errors += 1
            continue
        if cov in ("TRUNCATED", "PARTIAL_ERROR", "COMPLETE_TARGET_GENES_MISSING"):
            incomplete += 1
        for r in ans.get("hits") or []:
            if r.get("kind") != "activity":
                continue
            m = by_mol.setdefault(r["molecule_chembl_id"], {"molecule_chembl_id": r["molecule_chembl_id"], "parent_molecule_chembl_id": r.get("parent_molecule_chembl_id"),
                                                             "name": r.get("molecule_pref_name"), "rows": []})
            q = ms.measure(r.get("standard_type") or "", r.get("standard_value"), r.get("standard_units"), r.get("standard_relation") or "=",
                           target=r.get("target_pref_name") or "", species=r.get("target_organism") or "", system=json.dumps(r.get("assay_context"), sort_keys=True) if r.get("assay_context") else "",
                           conditions=r.get("assay_description") or "", source=r.get("document_chembl_id") or "")
            m["rows"].append({"measurement": q, "pchembl_value": r.get("pchembl_value"), "target_chembl_id": r.get("target_chembl_id"), "target_type": r.get("target_type"),
                              "target_is_complex": (r.get("target_type") or "") != "SINGLE PROTEIN", "assay_chembl_id": r.get("assay_chembl_id"), "document_year": r.get("document_year"),
                              "data_validity_comment": r.get("data_validity_comment"), "potential_duplicate": r.get("potential_duplicate"),
                              "direction": "", "selectivity": "NOT_ASSESSED"})
    for m in by_mol.values():
        m["n_rows"] = len(m["rows"])
        m["reached_by_target_path"] = None if reached is None else (m["molecule_chembl_id"] in reached or (m["parent_molecule_chembl_id"] in reached))
        m["in_catalogue"] = None if catalogue_ids is None else ("CAT:" + m["molecule_chembl_id"] in catalogue_ids)   # identity: a catalogue record exists to join to
    out["molecules"] = sorted(by_mol.values(), key=lambda m: (-m["n_rows"], m["molecule_chembl_id"]))
    if errors and not out["molecules"]:
        out["state"], out["note"] = "READ_ERROR", "every activity read failed"
    elif errors or incomplete:
        out["state"] = "READ_INCOMPLETE"
        out["note"] = "a read was truncated, partly failed or lacked target genes: the molecules listed are the part read, not all of them"
    elif not out["molecules"]:
        out["state"], out["note"] = "NO_ACTIVITY_ROWS", f"complete read of {len(todo)} target(s) under the activity types asked: none; a statement about this scope and release, not about any compound"
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("gene")
    ap.add_argument("--max-rows", type=int, default=400)
    ap.add_argument("--cache", default=None, help="explicit directory for the adapter's response cache (one per ChEMBL release)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    import compound_catalog as cc
    from adapters import _http, chembl
    path, digest = cc.cache_file("gtopdb/targets_and_families.csv")
    es = cc.load(cc.DEFAULT_CATALOG)
    fetch = _http.make_fetch(a.cache) if a.cache else _http.make_fetch()
    q = lambda req: chembl.query(req, fetch=fetch)  # noqa: E731
    res = activities_for_gene(a.gene, q, load_gtopdb_targets(path), reached=catalogue_reach(es, a.gene), catalogue_ids={e["id"] for e in es}, max_rows=a.max_rows)
    res["inputs"] = {"gtopdb_targets": str(path), "sha256": digest}
    if a.json:
        print(json.dumps(res, indent=1, ensure_ascii=False))
        return 0
    print(f"{res['gene']} state={res['state']} accession={res['accession']} release={res.get('source_version')}  {res['note']}")
    for r in res["reads"]:
        print(f"  read {r['target_chembl_id']}: {r['status']} {r['coverage']} {r['retrieved']} of {r['total_count']}")
    for m in res["molecules"]:
        types = sorted({r["measurement"]["kind"] for r in m["rows"]})
        print(f"  {m['molecule_chembl_id']:14s} rows={m['n_rows']:3d} types={','.join(types):12s} by_target_path={m['reached_by_target_path']} in_catalogue={m['in_catalogue']}  {m['name'] or ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
