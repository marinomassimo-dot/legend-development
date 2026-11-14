#!/usr/bin/env python3
"""IT44 P2: a by-target ACTIVITY path for what the mechanism tables do not hold.
The mechanism path (action_search.py) reads curated mechanism rows and registry interactions; a compound with only measured activities on the target (azetukalner on KCNQ2 is the control found by SCI43) is invisible to it.
This path reads ChEMBL's public activity endpoint for the target records that carry a relation's gene symbols, through the shared ChEMBL adapter (HE45: one cache, keyed by the full request and kept in one directory per ChEMBL release; assay context and target genes come with the rows),
and writes one row per measured activity plus one row per molecule. Principles kept apart (a measured activity is NOT an action):
  identity of the molecule (ChEMBL id, parent, name as served) | target record and organism | quantity as reported (type, relation, value, unit, assay type, assay text) | direction: never taken from the activity type | transfer to WWOX: always open.
Every molecule verdict is ACTIVITY_ONLY with named unknown fields; it can enter a comparison as a candidate for a primary-source read, never as a favourable compound. A truncated read is coverage TRUNCATED, never absence.
HE45: two reads per target, each with its own coverage. The dose-response types (IC50, EC50, Ki, Kd) are read to completion within --max-rows; `Potency` (qHTS AC50 depositions: 92,628 of the 93,391 rows of the NFE2L2 record) is read as a bounded sample (--max-potency-rows) and its coverage never taints the dose-response rows.
A molecule's `measure_summary` is a range per comparable group (type, target, organism, assay type) with the activity id of the lowest value; there is no single best potency across groups.
No third-party raw data is committed: the derived tables carry only values and ids; the raw pages stay in LEGEND_ACTIVITY_CACHE (default catalog/cache/chembl_activity/<release>); a refresh is a new cache directory.
  python3 activity_search.py --relations relations.tsv --out outdir [--types IC50,EC50,Ki,Kd,Potency] [--max-rows 5000] [--max-potency-rows 1000]"""
import argparse, csv, gzip, json, os, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(HERE.parents[4] / "framework")); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import measurement as ms  # noqa: E402  (HE43: a quantity keeps its original value, unit and relation; the nM conversion is labelled, flags are never silent)
from adapters import _http, chembl  # noqa: E402  (HE45: the one ChEMBL reader and its cache)
DOSE_TYPES = ("IC50", "EC50", "Ki", "Kd")
TYPES = DOSE_TYPES + ("Potency",)
UNKNOWN_FIELDS = "direction;site;target_composition_in_assay;transfer_to_WWOX_context"
ROWS_COMPLETE = ("COMPLETE", "COMPLETE_ASSAY_CONTEXT_MISSING", "COMPLETE_TARGET_GENES_MISSING")   # every row was read; the two others lack context fields, not rows
DEPOSIT = 200   # a document that measures more molecules than this on the relation's targets is a screening deposit: its molecules are pointers to the screen, not candidates

def cache_root():
    return Path(os.environ.get("LEGEND_ACTIVITY_CACHE", DR / "catalog/cache/chembl_activity"))

def release_dir(root, status_fetch=None):
    """(cache directory for the ChEMBL release in force, how the release was known). One directory per release: the adapter's cache key does not contain the release.
    Network unreachable: the newest existing release directory, declared as such in the manifest; with none, ('', 'UNKNOWN')."""
    url = chembl.BASE + "/status.json"
    status, payload = (status_fetch or _http.make_fetch())(url)   # bounded retry, no cache: the release must be read fresh
    if status == 200 and isinstance(payload, dict) and payload.get("chembl_db_version"):
        d = Path(root) / str(payload["chembl_db_version"]); d.mkdir(parents=True, exist_ok=True); return d, "status_endpoint"
    have = sorted(p for p in Path(root).glob("ChEMBL_*") if p.is_dir())
    return (have[-1], f"NETWORK_UNREACHABLE_newest_cached_release:{have[-1].name}") if have else (None, "UNKNOWN")

def target_index(cache_root_):
    """gene symbol -> [(target_chembl_id, target_type, organism, n_components)] from the cached ChEMBL target file (human only)."""
    idx = defaultdict(list)
    with gzip.open(Path(cache_root_) / "chembl/targets.jsonl.gz", "rt") as f:
        for line in f:
            t = json.loads(line)
            if t.get("organism") != "Homo sapiens": continue
            comps = t.get("target_components") or []
            for c in comps:
                for s in c.get("target_component_synonyms") or []:
                    if s.get("syn_type") == "GENE_SYMBOL": idx[s["component_synonym"].upper()].append((t["target_chembl_id"], t.get("target_type", ""), t.get("organism", ""), len(comps)))
    return {k: sorted(set(v)) for k, v in idx.items()}

def read_class(target, types, max_rows, fetch):
    """One read of one target under one set of types, through the adapter. Returns (hits, entry) with the coverage, counts, release and requests of this read."""
    ans = chembl.query({"target": target, "types": list(types), "max_rows": max_rows}, fetch=fetch)
    cov = ans.get("coverage") or ("READ_ERROR" if ans.get("status") == "QUERY_ERROR" else "NOT_READ")
    return [h for h in ans.get("hits") or [] if h.get("kind") == "activity"], {"types": list(types), "coverage": cov, "retrieved": ans.get("retrieved"), "total_count": ans.get("total_count"),
                                                                          "source_version": ans.get("source_version"), "requests": len(ans.get("requests_sent") or []), "error": ans.get("error", "")[:200]}

def catalogue_by_chembl():
    """ChEMBL id -> (catalogue name, status class, origin) from the tracked catalogue; the join is by id, never by name."""
    out = {}
    with gzip.open(DR / "catalog/catalog.jsonl.gz", "rt") as f:
        for line in f:
            r = json.loads(line)
            for sr in r.get("source_records", []):
                if sr.get("source") == "chembl": out[sr["id"]] = (r.get("name") or "", r.get("status_class") or "", r.get("origin") or "")
    return out

def make_resolver():
    """HE44's exact resolver (symbol -> the pinned GtoPdb accession -> ChEMBL targets by accession, with a state per symbol); None when it cannot be built (a test cache, no network) or LEGEND_ACTIVITY_RESOLVER=0."""
    if os.environ.get("LEGEND_ACTIVITY_RESOLVER", "1") == "0": return None
    try:
        import compound_catalog as cc, target_activity as ta
        path, _ = cc.cache_file("gtopdb/targets_and_families.csv"); acc = ta.load_gtopdb_targets(path); fetch = _http.make_fetch()
        return lambda sym: ta.resolve_targets(sym, lambda req: chembl.query(req, fetch=fetch), acc)
    except Exception:
        return None

def main(argv=None, fetch=None, release_fetch=None):
    ap = argparse.ArgumentParser(); ap.add_argument("--relations", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--types", default=",".join(TYPES)); ap.add_argument("--max-rows", type=int, default=5000); ap.add_argument("--max-potency-rows", type=int, default=1000)
    a = ap.parse_args(argv); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    croot = Path(os.environ.get("LEGEND_CATALOG_CACHE", DR / "catalog/cache"))
    if not (croot / "chembl/targets.jsonl.gz").is_file():     # the cache is gitignored, so a worktree has none: ADV-003 took this for a tool that cannot run
        print(f"no cached ChEMBL target file at {croot / 'chembl/targets.jsonl.gz'}: the catalogue cache exists per checkout (it is not in git). From a worktree, set "
              "LEGEND_CATALOG_CACHE to the primary checkout's disease-models/wwox/research/drug_repurposing/catalog/cache; nothing was read", file=sys.stderr); return 2
    idx = target_index(croot); types = tuple(a.types.split(","))
    dose, screen = tuple(t for t in types if t != "Potency"), tuple(t for t in types if t == "Potency")
    rdir, release_basis = release_dir(cache_root(), release_fetch) if fetch is None else (None, "INJECTED_FETCH")
    if fetch is None:
        if rdir is None: print("no ChEMBL release known and no cached release: nothing was read"); return 2
        fetch = _http.make_fetch(str(rdir))
    resolver = make_resolver()
    rels = list(csv.DictReader(open(a.relations, encoding="utf-8"), delimiter="\t")); act_rows, manifest, symbols, done = [], {"_release": {"directory": rdir.name if rdir else "", "basis": release_basis}}, {}, {}
    for r in rels:
        for sym in sorted({s.split(":")[0].strip().upper() for s in r["target_symbols"].replace(":down", "").replace(":up", "").split(";") if s.strip()}):
            tl = list(idx.get(sym, [])); state = "TARGETS_FOUND" if any(t[1] in ("SINGLE PROTEIN", "PROTEIN COMPLEX", "PROTEIN FAMILY") for t in tl) else "UNRESOLVED_IN_CACHED_INDEX"
            if resolver is not None:                       # the exact resolver adds the targets the cached index lacks and says why when it finds none
                rr = resolver(sym)
                for t in rr["targets"]:
                    if all(t["target_chembl_id"] != x[0] for x in tl): tl.append((t["target_chembl_id"], t.get("target_type", ""), t.get("organism", ""), len(t.get("accessions") or [1])))
                state = "TARGETS_FOUND" if tl else rr["state"]
            symbols[f"{r['relation_id']}:{sym}"] = state   # no row for a symbol means unread, never "no compounds"
            for tid, ttype, org, ncomp in sorted(set(tl)):
                if ttype not in ("SINGLE PROTEIN", "PROTEIN COMPLEX", "PROTEIN FAMILY"): continue
                gran = "single_protein" if ncomp == 1 and ttype == "SINGLE PROTEIN" else "complex_or_family_record"
                for cls, ts, cap in (("dose_response", dose, a.max_rows), ("potency_screen", screen, a.max_potency_rows)):
                    if not ts: continue
                    if (tid, cls) not in done:             # one read per target and class, shared by every relation that names the target
                        done[(tid, cls)] = read_class(tid, ts, cap, fetch); manifest.setdefault(tid, {})[cls] = done[(tid, cls)][1]
                    hits, entry = done[(tid, cls)]
                    for x in hits:
                        ctx = x.get("assay_context") or {}
                        q = ms.measure(x.get("standard_type") or "", x.get("standard_value"), x.get("standard_units"), x.get("standard_relation") or "=", target=sym, species=ctx.get("assay_organism") or "",
                                       system=ctx.get("assay_type") or "", source=f"activity_id={x.get('activity_id')}")
                        act_rows.append(dict(activity_id=x.get("activity_id") or "", converted_nM=("" if q["converted_nM"] is None else f"{q['converted_nM']:.6g}"), measurement_flags=";".join(q["flags"]), relation_id=r["relation_id"],
                            target_symbol=sym, target_chembl_id=tid, target_granularity=gran, read_class=cls, molecule_chembl_id=x.get("molecule_chembl_id") or "",
                            parent_chembl_id=x.get("parent_molecule_chembl_id") or x.get("molecule_chembl_id") or "", name=x.get("molecule_pref_name") or "", type=x.get("standard_type") or "", relation=x.get("standard_relation") or "",
                            value=x.get("standard_value") or "", units=x.get("standard_units") or "", assay_type=ctx.get("assay_type") or "", assay_organism=ctx.get("assay_organism") or "", validity=x.get("data_validity_comment") or "",
                            assay_description=(x.get("assay_description") or "")[:160].replace("\t", " ").replace("\n", " "), document=x.get("document_chembl_id") or "", coverage=entry["coverage"]))
    manifest["_symbols"] = symbols
    if not act_rows: json.dump(manifest, open(out / "activity_manifest.json", "w"), indent=1); print("no activity rows;", {k: v for k, v in symbols.items() if v != "TARGETS_FOUND"}); return 1
    with open(out / "activity_rows.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(act_rows[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(act_rows)
    cat = catalogue_by_chembl(); mol = defaultdict(list)
    for x in act_rows: mol[(x["relation_id"], x["parent_chembl_id"])].append(x)
    doc_mols = defaultdict(set)
    for (rid, par), xs in mol.items():
        for x in xs: doc_mols[(rid, x["document"])].add(par)
    mrows = []
    for (rid, par), xs in sorted(mol.items()):
        nm = sorted({x["name"] for x in xs if x["name"]}); fun = [x for x in xs if x["assay_type"] == "F"]
        cn, cs, co = cat.get(par, ("", "", ""))
        dose_rows = [x for x in xs if x["read_class"] == "dose_response"]
        summary = ms.summarise([ms.measure(x["type"], x["value"], x["units"], x["relation"] or "=", target=x["target_symbol"], species=x["assay_organism"], system=x["assay_type"], source=f"activity_id={x['activity_id']}") for x in xs])
        if any(x["coverage"] not in ROWS_COMPLETE for x in dose_rows): state = "TRUNCATED"      # the dose-response read stopped short: absence of other rows is unknown
        elif not dose_rows and any(x["coverage"] not in ROWS_COMPLETE for x in xs): state = "SCREEN_PARTIAL"   # only sampled screening rows: a pointer to the screen, not listed
        elif all(len(doc_mols[(rid, x["document"])]) > DEPOSIT for x in xs): state = "SCREEN_DEPOSIT"
        else: state = "OK"
        mrows.append(dict(relation_id=rid, parent_chembl_id=par, name=" | ".join(nm)[:80], catalogue_name=cn[:60], catalogue_status=cs or ("none" if not cn else "unstated"), catalogue_origin=co, n_documents=len({x["document"] for x in xs if x["document"]}), n_activities=len(xs), n_functional=len(fun), types=";".join(sorted({x["type"] for x in xs})), organisms=";".join(sorted({x["assay_organism"] for x in xs if x["assay_organism"]})),
            targets=";".join(sorted({x["target_symbol"] for x in xs})), n_flagged_validity=sum(1 for x in xs if x["validity"]), n_measurement_flags=sum(1 for x in xs if x["measurement_flags"]), n_measure_groups=len(summary), measure_summary=ms.render_summary(summary)[:600], unit_variants=";".join(sorted({x["units"] for x in xs if x["units"]})),
            coverage=";".join(sorted({f"{x['read_class']}:{x['coverage']}" for x in xs})), read_state=state, verdict="ACTIVITY_ONLY", unknown_fields=UNKNOWN_FIELDS))
    with open(out / "activity_molecules.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(mrows[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(mrows)
    json.dump(manifest, open(out / "activity_manifest.json", "w"), indent=1)
    print(len(act_rows), "activity rows;", len(mrows), "molecule x relation rows;", {f"{k}:{c}": v[c]["coverage"] for k, v in manifest.items() if not k.startswith("_") for c in v}, "unresolved symbols:", sorted(k for k, v in symbols.items() if v != "TARGETS_FOUND"))
    return 0
if __name__ == "__main__": sys.exit(main())
