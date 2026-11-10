#!/usr/bin/env python3
"""Which compound a name reaches, how sure that is, and what each source says it acts on — kept apart.

compound_catalog.find() answers "which records contain this string". A tool name needs more: a record whose display
name differs from the query (a synonym hit), a record whose ChEMBL twin is outside the catalogue selection, a
ChEMBL molecule that has no name at all, and a source that gives the same label to two structures. This module
adds that, over the existing catalogue, the existing ligand reconciliation and the existing chembl adapter. It
builds no catalogue and no exception list: the only hand-written input is `catalog/tool_identity_declarations.tsv`,
each row carrying its basis, source and date.

Two answers, never merged:

  identity   NAME_EXACT / SYNONYM_EXACT / SEPARATOR_VARIANT (equal only without spaces and hyphens) / NAME_PARTIAL / SYNONYM_PARTIAL / DECLARED (a declaration row) /
             NOT_FOUND_BY_NAME (says nothing about the compound), plus the ChEMBL ids the record points at, whether
             they are in the catalogue, and a `label_conflict` when a declaration says the label sits on two structures.
  target     per expected gene, the highest evidence LEVEL that was read: CURATED_MECHANISM (ChEMBL mechanism table),
             SOURCE_INTERACTION (DGIdb/GtoPdb row in the catalogue), MEASURED_ACTIVITY_HUMAN, MEASURED_ACTIVITY_OTHER_SPECIES,
             or one of EMPTY_RESULT (read, nothing under the filters) / NOT_READ (no ChEMBL id to read) /
             READ_ERROR (the query failed). Selectivity is always NOT_ASSESSED, and the other genes measured are listed.

Empty, not read and error are three states; none is evidence against a compound.

  python3 framework/scripts/compound_identity.py "Ro 25-6981" --genes GRIN2B
  python3 framework/scripts/compound_identity.py ifenprodil --genes GRIN2B --offline
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import compound_catalog as cc  # noqa: E402

CAT_DIR = cc.DEFAULT_CATALOG.parent
DECLARATIONS = CAT_DIR / "tool_identity_declarations.tsv"
RECON = CAT_DIR / "ligand_reconciliation.tsv"
LEVELS = ("CURATED_MECHANISM", "SOURCE_INTERACTION", "MEASURED_ACTIVITY_HUMAN", "MEASURED_ACTIVITY_OTHER_SPECIES")


def _rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def match_kind(entry: dict, name: str) -> str | None:
    q = cc._norm(name)
    if not q:
        return None
    if cc._norm(entry.get("name") or "") == q:
        return "NAME_EXACT"
    syn = [cc._norm(s) for s in entry.get("synonyms", [])]
    if q in syn:
        return "SYNONYM_EXACT"
    compact = q.replace(" ", "")
    if compact == cc._norm(entry.get("name") or "").replace(" ", "") or compact in [x.replace(" ", "") for x in syn]:
        return "SEPARATOR_VARIANT"   # equal only after removing spaces and hyphens: Gyki53655 for GYKI 53655
    if q in cc._norm(entry.get("name") or ""):
        return "NAME_PARTIAL"
    if any(q in s for s in syn):
        return "SYNONYM_PARTIAL"
    return None


def resolve(es: list[dict], name: str, recon: list[dict] | None = None, declarations: list[dict] | None = None) -> dict:
    recon = _rows(RECON) if recon is None else recon
    declarations = _rows(DECLARATIONS) if declarations is None else declarations
    by_lig = collections.defaultdict(list)
    for r in recon:
        by_lig[r["candidate"]].append(r)
    cands = []
    for e in es:
        k = match_kind(e, name)
        if not k:
            continue
        ids = e.get("ids", {})
        refs = []
        for cid, basis in ([(ids.get("chembl"), "record")] + [(c, "dgidb_concept") for c in ids.get("chembl_from_dgidb_concept_not_enumerated") or []]):
            if cid:
                refs.append({"chembl_id": cid, "basis": basis})
        for r in by_lig.get(e["id"], []):
            refs.append({"chembl_id": r["chembl_ref"], "basis": "gtopdb_ligand_reconciliation", "in_catalogue": r["chembl_ref_in_catalogue"],
                         "decision": r["decision"], "gtopdb_inchikey": r["gtopdb_inchikey"]})
        cands.append({"catalogue_id": e["id"], "record_name": e.get("name"), "match_kind": k, "origin": e.get("origin"),
                      "parent": (e.get("relations") or {}).get("parent"), "chembl_refs": refs})
    decl = [d for d in declarations if cc._norm(d["query_name"]) == cc._norm(name)]
    rank = {"NAME_EXACT": 0, "SYNONYM_EXACT": 1, "SEPARATOR_VARIANT": 2, "NAME_PARTIAL": 3, "SYNONYM_PARTIAL": 4}
    cands.sort(key=lambda c: (rank[c["match_kind"]], c["catalogue_id"]))
    best = cands[0]["match_kind"] if cands else None
    declared = [d for d in decl if d["role"] == "identity"]
    state = best or ("DECLARED" if declared else "NOT_FOUND_BY_NAME")
    if best in ("NAME_PARTIAL", "SYNONYM_PARTIAL", "SEPARATOR_VARIANT") and declared:
        state = "DECLARED"
    return {"query": name, "identity_state": state, "candidates": cands, "declarations": decl,
            "label_conflict": [d for d in decl if d["role"] == "label_conflict"],
            "note": "NOT_FOUND_BY_NAME is a statement about the name and the sources read, not about the compound"}


def _chembl_ids(res: dict) -> list[str]:
    """ChEMBL ids to read: declared identities first (they are the reviewed ones), then the references of the best match kind."""
    ids = [d["chembl_id"] for d in res["declarations"] if d["role"] == "identity"]
    best = res["candidates"][0]["match_kind"] if res["candidates"] else None
    if best in ("NAME_EXACT", "SYNONYM_EXACT", "SEPARATOR_VARIANT"):
        ids += [r["chembl_id"] for c in res["candidates"] if c["match_kind"] == best for r in c["chembl_refs"]]
    return list(dict.fromkeys(i for i in ids if i and i != "-"))


def target_evidence(res: dict, genes: list[str], es: list[dict], chembl_query=None) -> dict:
    """Per expected gene, the highest evidence level read. chembl_query(request) -> adapter answer; None means do not read ChEMBL."""
    want = [g.upper() for g in genes]
    level = {g: None for g in want}
    detail = {g: [] for g in want}
    other = collections.Counter()
    unattributed = []
    ids = _chembl_ids(res)
    read = []
    # catalogue rows (already in hand): curated mechanism and source interaction
    best = res["candidates"][0]["match_kind"] if res["candidates"] else None
    for c in (c for c in res["candidates"] if c["match_kind"] == best and best in ("NAME_EXACT", "SYNONYM_EXACT", "SEPARATOR_VARIANT")):
        e = next(x for x in es if x["id"] == c["catalogue_id"])
        for t in e.get("targets", []):
            syms = {s.upper() for s in (t.get("gene_symbols") or [])} | ({t["gene"].upper()} if t.get("gene") else set())
            lv = "CURATED_MECHANISM" if t.get("source") == "ChEMBL curated mechanism" else "SOURCE_INTERACTION"
            for g in want:
                if g in syms and res["label_conflict"] and c["match_kind"] != "NAME_EXACT":
                    unattributed.append(f"{g}: {c['catalogue_id']} ({lv}) not attributed: the label of this record sits on two structures")
                elif g in syms:
                    level[g] = _best(level[g], lv)
                    detail[g].append(f"{lv}: {c['catalogue_id']}")
            if not syms & set(want):
                other.update(syms)
    state = "NOT_READ" if chembl_query is None or not ids else "READ"
    errors = 0
    for cid in ids if chembl_query else []:
        mech = chembl_query({"drug": res["query"], "molecule_id": cid})
        act = chembl_query({"molecule": cid})
        read.append({"chembl_id": cid, "mechanism_status": mech.get("status"), "activity_status": act.get("status"),
                     "activity_coverage": act.get("coverage"), "activity_rows": act.get("total_count")})
        if mech.get("status") == "QUERY_ERROR" or act.get("status") == "QUERY_ERROR":
            errors += 1
        for h in mech.get("hits") or []:
            syms = {s.upper() for s in (h.get("target_gene_symbols") or [])}
            for g in want:
                if h.get("kind") == "mechanism" and g in syms:
                    level[g] = _best(level[g], "CURATED_MECHANISM")
                    detail[g].append(f"CURATED_MECHANISM: {cid}")
        for h in act.get("hits") or []:
            syms = {s.upper() for s in (h.get("target_gene_symbols") or [])}
            human = h.get("target_organism") == "Homo sapiens"
            hit = False
            for g in want:
                if g in syms:
                    hit = True
                    lv = "MEASURED_ACTIVITY_HUMAN" if human else "MEASURED_ACTIVITY_OTHER_SPECIES"
                    level[g] = _best(level[g], lv)
                    detail[g].append(f"{lv}: {cid} {h.get('standard_type')} {h.get('target_organism')}")
            if not hit:
                other.update(syms)
    if state == "READ" and errors and not all(level.values()):
        state = "READ_ERROR"
    per_gene = {}
    for g in want:
        if level[g]:
            per_gene[g] = {"level": level[g], "n_rows": len(detail[g]), "rows": detail[g][:6]}
        else:
            per_gene[g] = {"level": {"READ": "EMPTY_RESULT", "NOT_READ": "NOT_READ", "READ_ERROR": "READ_ERROR"}[state], "n_rows": 0, "rows": []}
    return {"expected_genes": want, "per_gene": per_gene, "chembl_read": read, "selectivity": "NOT_ASSESSED", "unattributed_source_rows": unattributed,
            "other_genes_seen": dict(other.most_common(8)),
            "note": "a record or activity row naming a gene shows the gene was reported for the compound, not that the compound is selective for it"}


def _best(cur, new):
    return new if cur is None or LEVELS.index(new) < LEVELS.index(cur) else cur


# --- joining free-text names to a table of resolved identities --------------------------------------------------
# A substring test between a name and a table key proposes a search; it is not an identity. "GYKI 52466 / GYKI 53655"
# contains two keys, "Brilliant Blue" is a prefix of one, "Ro" is inside "ifenprodil": any of them silently gets the
# first key's row. Here a name reaches a row only through EXACT, QUALIFIED (a salt, a stereo or a label prefix the
# table key does not carry, stated in `qualifier`) or MULTI_PART (a cell naming several compounds, each resolved alone).
# Everything else is PROPOSED_ONLY: the candidate keys are listed, no row is attached.
import re  # noqa: E402

_SPLIT = re.compile(r"\s*(?:/|\+|&|,|\band\b|\bvs\.?\b|\bversus\b)\s*", re.I)
_PREFIX = re.compile(r"^\s*(?:\((?:[RS]|[+\-\u00b1]|rac|[dl]|\d+[RS])\)-?|\[\d*[A-Za-z]{1,2}\]\s*|rac-|[RS]-)\s*", re.I)
_SUFFIX = re.compile(r"[\s\-]+(?:hydrochloride|hydrobromide|maleate|tartrate|mesylate|besylate|citrate|sulfate|phosphate|"
                     r"disodium|dipotassium|sodium|potassium|hcl|hydrate|monohydrate|salt|d\d{1,2})\s*$", re.I)


_COMMENT = re.compile(r"\s*\((?!(?:[RS]|[+\-\u00b1]|rac|[dl]|\d+[RS])\))[^)]*\)", re.I)


def _key(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def join_names(name: str, table_keys) -> list[dict]:
    """[{part, link, key, qualifier}] for one cell. link is EXACT / QUALIFIED / PROPOSED_ONLY / NO_CANDIDATE; key is set only
    for EXACT and QUALIFIED; PROPOSED_ONLY carries `proposed_keys` and attaches nothing."""
    keys = {_key(k): k for k in table_keys}
    name = _COMMENT.sub("", name).strip() or name      # "(a different structure, not ...)" is a comment; "(R)-" stays a qualifier
    parts = [p for p in _SPLIT.split(name) if p.strip()] if _key(name) not in keys else [name]
    multi = len(parts) > 1
    out = []
    for part in parts or [name]:
        part = re.sub(r"\s*\(.*?\)\s*$", "", part).strip() or part   # trailing parenthetical: a comment, not a name
        k = _key(part)
        link, hit, qual = None, None, []
        if k in keys:
            link, hit = "EXACT", keys[k]
        else:
            q, changed = k, True
            while changed:
                changed = False
                for rx in (_PREFIX, _SUFFIX):
                    m = rx.search(q)
                    if m and m.group(0).strip():
                        qual.append(m.group(0).strip()); q = rx.sub("", q, count=1).strip(); changed = True
            if qual and q in keys:
                link, hit = "QUALIFIED", keys[q]
        if link:
            out.append({"part": part, "link": link, "key": hit, "qualifier": ";".join(qual), "multi_part": multi})
            continue
        prop = sorted(orig for kk, orig in keys.items() if kk and (kk in k or k in kk))
        out.append({"part": part, "link": "PROPOSED_ONLY" if prop else "NO_CANDIDATE", "key": None, "qualifier": "",
                    "proposed_keys": prop, "multi_part": multi})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("name")
    ap.add_argument("--genes", default="", help="comma-separated expected gene symbols")
    ap.add_argument("--offline", action="store_true", help="do not call the ChEMBL adapter")
    a = ap.parse_args(argv)
    es = cc.load(cc.DEFAULT_CATALOG)
    res = resolve(es, a.name)
    q = None
    if not a.offline:
        import repurposing_adapter as ad
        q = lambda req: ad.load("chembl").query(req)  # noqa: E731
    out = {"identity": res, "target": target_evidence(res, [g for g in a.genes.split(",") if g], es, q)}
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
