#!/usr/bin/env python3
"""IT8 P3 pharmacological qualification: regenerates comparison.tsv and measures_detail.tsv.

  pharm_qualify.py --help            this text, no network, no work done
  pharm_qualify.py run [--out DIR]   live: ChEMBL (activity mode, molecule-first, retry with backoff), openFDA labels,
                                     GtoPdb / DGIdb cache; writes raw_store.json.gz and collected.json.gz (each only if < 1 MB), raw_hashes.tsv,
                                     service_log.tsv, measures_detail.tsv, comparison.tsv
  pharm_qualify.py rebuild [--out DIR]   offline: rebuilds both tables from collected.json.gz (or raw_store.json.gz) + cases.json (deterministic)
  pharm_qualify.py selftest          injected-fault tests of the retry layer and of the service-state classes

Cache: set LEGEND_CATALOG_CACHE to the catalogue cache (GtoPdb/DGIdb files). Standard library only.
A SERVICE_ERROR (HTTP 5xx or transport failure after retries) is never reported as 'no data' (NO_ROWS_UNDER_FILTERS) and never as a
negative result. UNKNOWN means the services queried hold no datum; it is not a zero. Nothing here is medical advice.
"""
import argparse, csv, gzip, hashlib, json, os, re, statistics, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BACKOFF = (0, 2, 6, 15, 30)  # seconds before attempt 1..5
RAW_LIMIT = 1_000_000
SECTIONS = ("pharmacokinetics", "clinical_pharmacology", "mechanism_of_action", "pediatric_use", "dosage_and_administration", "warnings_and_cautions", "warnings",
            "boxed_warning")   # the last one is read for presence only
TYPES = ["IC50", "Ki", "Kd", "EC50", "Kb", "Potency", "Inhibition"]
SIGN = {"INHIBITOR": "down", "ANTAGONIST": "down", "BLOCKER": "down", "NEGATIVE ALLOSTERIC MODULATOR": "down",
        "SEQUESTERING AGENT": "none (binds a metabolite)", "AGONIST": "up", "ACTIVATOR": "up", "OPENER": "up",
        "POSITIVE ALLOSTERIC MODULATOR": "up"}


class Net:
    """HTTP door with retry/backoff, an attempt log and a raw store (live) or a replay map (offline)."""
    def __init__(self, replay=None, sleep=time.sleep, get=None):
        self.replay, self.sleep, self.raw, self.log, self.case = replay, sleep, {}, [], ""
        if get is None:
            from framework.adapters import _http
            get = _http.get_json
        self._get = get

    @staticmethod
    def key(url, params):
        return url + ("?" + "&".join(f"{k}={params[k]}" for k in sorted(params)) if params else "")

    def get(self, url, params=None, body=None, timeout=40):
        k = self.key(url, params)
        if self.replay is not None:
            hit = self.replay.get(k)
            return (hit[0], hit[1]) if hit else (404, {"replay": "not in raw store"})
        status, payload = 0, ""
        for i, wait in enumerate(BACKOFF):
            if wait:
                self.sleep(wait)
            t0 = time.time()
            status, payload = self._get(url, params, body, timeout)
            self.log.append({"case": self.case, "attempt": i + 1, "status": status, "seconds": round(time.time() - t0, 2),
                             "url": k[:200], "error": "" if status == 200 else str(payload)[:120]})
            if status == 200 or status == 404:   # 404: a service answer (no match), not an error
                break
        self.raw[k] = [status, payload]
        return status, payload


def sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def state_of(result):
    """Distinct states: SERVICE_ERROR / NO_ROWS_UNDER_FILTERS / ROWS_RETRIEVED / ROWS_RETRIEVED_TRUNCATED."""
    if result.get("error"):
        return "SERVICE_ERROR"
    if not result.get("hits"):
        return "NO_ROWS_UNDER_FILTERS"
    return "ROWS_RETRIEVED_TRUNCATED" if result.get("truncated") else "ROWS_RETRIEVED"


def chembl_molecule(net, mid):
    s, m = net.get(f"https://www.ebi.ac.uk/chembl/api/data/molecule/{mid}.json")
    if s != 200 or not isinstance(m, dict):
        return {"id": mid, "state": "SERVICE_ERROR" if s != 404 else "NO_RECORD", "http": s}
    h = m.get("molecule_hierarchy") or {}
    st = m.get("molecule_structures") or {}
    s2, c = net.get(f"https://www.ebi.ac.uk/chembl/api/data/molecule.json?molecule_hierarchy__parent_chembl_id={h.get('parent_chembl_id') or mid}&limit=50")
    kids = sorted((x["molecule_chembl_id"], x.get("pref_name")) for x in (c.get("molecules") or [])) if s2 == 200 and isinstance(c, dict) else []
    chir = {0: "racemic mixture", 1: "single stereoisomer", 2: "achiral", -1: "unknown"}.get(m.get("chirality"), str(m.get("chirality")))
    return {"id": mid, "state": "OK", "pref_name": m.get("pref_name"), "parent": h.get("parent_chembl_id"), "is_parent": h.get("parent_chembl_id") == mid,
            "family": kids, "chirality": chir, "max_phase": m.get("max_phase"), "type": m.get("molecule_type"), "smiles": st.get("canonical_smiles"),
            "inchikey": st.get("standard_inchi_key"), "oral": m.get("oral"), "black_box_warning": m.get("black_box_warning")}


def rel(r):
    return {"=": "=", ">": ">", ">=": ">", "<": "<", "<=": "<"}.get(r or "=", r or "=")


def groups(rows, target_rx, assay_rx):
    """Group rows by (target, organism, type, relation, units, assay type); never aggregate across groups."""
    out = {}
    for r in rows:
        c = r.get("assay_context") or {}
        text = f"{r.get('target_pref_name') or ''} {r.get('assay_description') or ''}"
        if not (re.search(target_rx, r.get("target_pref_name") or "") or (assay_rx and re.search(assay_rx, r.get("assay_description") or "", re.I))):
            continue
        key = (r.get("target_pref_name") or "NA", r.get("target_organism") or "NA", r.get("standard_type"), rel(r.get("standard_relation")),
               r.get("standard_units") or "NA", c.get("assay_type") or "NA", r.get("molecule_chembl_id"))
        out.setdefault(key, []).append(r)
    return out


def num(r):
    try:
        return float(r["standard_value"])
    except (TypeError, ValueError, KeyError):
        return None


def fmt(v):
    return f"{v:g}"


def collect(net, case, cache):
    from framework.adapters import chembl
    net.case = case["id"]
    res = {"id": case["id"], "compounds": [], "target_first": [], "fda": [], "gtopdb": [], "dgidb": []}
    for comp in case["compounds"]:
        e = {"label": comp["label"], "resolution": [], "mechanisms": [], "molecules": [], "rows": [], "status": {}}
        for nm in comp["names"]:
            r = chembl.query({"drug": nm}, fetch=net.get)
            e["resolution"].append({"name": nm, "status": r["status"], "error": r["error"], "nearest": [n.get("molecule_chembl_id") for n in r.get("nearest") or []],
                                    "version": r["source_version"]})
            for h in r["hits"]:
                if h.get("kind") == "mechanism":
                    e["mechanisms"].append((h.get("molecule_chembl_id"), h.get("action_type"), h.get("mechanism_of_action"), h.get("target_chembl_id")))
        seen = []
        for mid in comp["ids"]:
            mol = chembl_molecule(net, mid)
            e["molecules"].append(mol)
            fam = [mid] + ([mol["parent"]] if mol.get("parent") else []) + [k for k, _ in mol.get("family", [])]
            for fid in fam:
                if fid in seen:
                    continue
                seen.append(fid)
                a = chembl.query({"molecule": fid, "types": TYPES, "max_rows": 2000}, fetch=net.get)
                e["status"][fid] = {"state": state_of(a), "total": a.get("total_count"), "retrieved": a.get("retrieved"),
                                    "truncated": a.get("truncated"), "error": a["error"], "version": a["source_version"], "note": a.get("note", "")[:200]}
                e["rows"] += a["hits"]
        res["compounds"].append(e)
    for tf in case.get("target_first", []):
        a = chembl.query({"target": tf["target"], "types": tf["types"], "max_rows": tf["max_rows"]}, fetch=net.get)
        res["target_first"].append({"spec": tf, "state": state_of(a), "total": a.get("total_count"), "retrieved": a.get("retrieved"),
                                    "truncated": a.get("truncated"), "error": a["error"], "rows": a["hits"]})
    for f in case.get("fda", []):
        s, p = net.get("https://api.fda.gov/drug/label.json", params={"search": f'openfda.generic_name:"{f["generic"]}"', "limit": 10})
        ent = {"generic": f["generic"], "http": s, "state": "SERVICE_ERROR" if s not in (200, 404) else ("NO_MATCH" if s == 404 else "OK")}
        if s == 200 and isinstance(p, dict):
            labs = p.get("results") or []
            pick = next((x for x in labs if f["prefer"] and re.search(f["prefer"], json.dumps(x.get("openfda", {})), re.I)), None) or labs[0]
            texts = {k: " ".join(pick.get(k, [])) for k in SECTIONS}
            sents = []
            for k in SECTIONS[:-1]:
                for sn in re.split(r"(?<=[.;])\s+", texts[k]):
                    if re.search(f["pattern"], sn, re.I) and sn[:300] not in sents:
                        sents.append(sn[:300])
            ent.update({"brand": (pick.get("openfda", {}).get("brand_name") or ["UNKNOWN"])[0], "manufacturer": (pick.get("openfda", {}).get("manufacturer_name") or ["UNKNOWN"])[0],
                        "product_type": (pick.get("openfda", {}).get("product_type") or ["UNKNOWN"])[0], "effective_time": pick.get("effective_time"),
                        "set_id": pick.get("set_id"), "n_labels": len(labs), "boxed_warning": bool(texts["boxed_warning"]), "snippets": sents[:4],
                        "full_hash": sha(pick), "last_updated": (p.get("meta") or {}).get("last_updated")})
        res["fda"].append(ent)
    res["gtopdb"] = gtopdb_rows(cache, case.get("gtopdb", []))
    res["dgidb"] = dgidb_rows(cache, case.get("dgidb", []))
    return res


def gtopdb_rows(cache, names):
    p = Path(cache) / "gtopdb" / "interactions.csv"
    out, want = [], {n.casefold() for n in names}
    if not p.exists():
        return [{"state": "CACHE_ABSENT"}]
    with open(p, newline="", encoding="utf-8") as f:
        f.readline()
        for r in csv.DictReader(f):
            if r["Ligand"].casefold() in want:
                out.append({"ligand": r["Ligand"], "target": r["Target"], "species": r["Target Species"], "action": r["Action"], "units": r["Affinity Units"],
                            "median": r["Affinity Median"][:6], "nM": r["Original Affinity Median nm"], "relation": r["Original Affinity Relation"], "pmid": r["PubMed ID"]})
    return out


def dgidb_rows(cache, names):
    p = Path(cache) / "dgidb" / "interactions.tsv"
    if not p.exists():
        return [{"state": "CACHE_ABSENT"}]
    want, out = {n.upper() for n in names}, {}
    with open(p, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["drug_name"].upper() in want:
                out.setdefault((r["drug_name"], r["gene_name"], r["interaction_type"]), set()).add(r["interaction_source_db_name"])
    return [{"drug": k[0], "gene": k[1], "interaction": k[2], "sources": ",".join(sorted(v))} for k, v in sorted(out.items())]


def detail_rows(res, case):
    rows = []
    for ce in res["compounds"]:
        for key, rs in sorted(groups(ce["rows"], case["target_pattern"], case.get("assay_pattern")).items(), key=lambda kv: str(kv[0])):
            vals = [num(r) for r in rs if num(r) is not None]
            docs = sorted({r.get("document_chembl_id") for r in rs if r.get("document_chembl_id")})
            descs = sorted({(r.get("assay_description") or "")[:140] for r in rs})
            orgs = sorted({(r.get("assay_context") or {}).get("assay_organism") or "NA" for r in rs})
            cells = sorted({(r.get("assay_context") or {}).get("assay_cell_type") or "NA" for r in rs})
            pch = [r["pchembl_value"] for r in rs if r.get("pchembl_value")]
            rows.append([case["id"], ce["label"], key[6], rs[0].get("molecule_pref_name") or "", key[0], key[1], key[2], key[3], key[4], key[5], len(rs), len(docs),
                         fmt(min(vals)) if vals else "", fmt(statistics.median(vals)) if vals else "", fmt(max(vals)) if vals else "",
                         ",".join(pch[:3]), ";".join(orgs), ";".join(cells), ",".join(docs), " || ".join(descs[:2]),
                         ";".join(sorted({str(r.get("data_validity_comment")) for r in rs if r.get("data_validity_comment")}))])
    for tf in res["target_first"]:
        sp = tf["spec"]
        rs = [r for r in tf["rows"] if r.get("standard_units") == "nM" and rel(r.get("standard_relation")) == "=" and num(r) is not None]
        pot = sorted(rs, key=num)
        best = [r for r in pot if num(r) <= sp["potent_nM"]]
        mols = sorted({r["molecule_chembl_id"] for r in best})
        for mid in mols[:12]:
            rr = [r for r in best if r["molecule_chembl_id"] == mid]
            docs = sorted({r["document_chembl_id"] for r in rr})
            rows.append([case["id"], f"TARGET-FIRST {sp['label']} [{tf['state']}; {tf['retrieved']} of {tf['total']} rows]", mid, rr[0].get("molecule_pref_name") or "", rr[0].get("target_pref_name"),
                         rr[0].get("target_organism"), rr[0]["standard_type"], "=", "nM", (rr[0].get("assay_context") or {}).get("assay_type") or "NA", len(rr), len(docs),
                         fmt(min(num(r) for r in rr)), "", fmt(max(num(r) for r in rr)), "", (rr[0].get("assay_context") or {}).get("assay_organism") or "NA", "",
                         ",".join(docs), (rr[0].get("assay_description") or "")[:140], ""])
        if not mols:
            rows.append([case["id"], f"TARGET-FIRST {sp['label']} [{tf['state']}; {tf['retrieved']} of {tf['total']} rows]", "", "", "none at or below %d nM" % sp["potent_nM"],
                         "", "", "", "", "", 0, 0, "", "", "", "", "", "", "", "", ""])
    return rows


DETAIL_HEAD = ["case", "compound_or_query", "molecule_chembl_id", "molecule_pref_name", "target", "target_organism", "standard_type", "relation", "units", "assay_type", "n_rows",
               "n_documents", "min", "median", "max", "pchembl_first3", "assay_organism", "assay_cell_type", "documents", "assay_description_first2", "data_validity"]


def measures_summary(res, case):
    parts = []
    for ce in res["compounds"]:
        gs = groups(ce["rows"], case["target_pattern"], case.get("assay_pattern"))
        chunks = []
        for key, rs in sorted(gs.items(), key=lambda kv: (kv[0][0], kv[0][2], kv[0][3])):
            vals = [num(r) for r in rs if num(r) is not None]
            tgt = key[0][:38]
            if key[4] in ("nM", "uM", "mM") and vals:
                v = fmt(min(vals)) if len(vals) == 1 or min(vals) == max(vals) else f"{fmt(min(vals))}-{fmt(max(vals))}"
                chunks.append(f"{tgt} [{key[1][:12]}; assay type {key[5]}; {key[6]}] {key[2]} {key[3]} {v} {key[4]} (n={len(rs)})")
            elif key[2] == "Inhibition":
                chunks.append(f"{tgt} [{key[1][:12]}; assay type {key[5]}; {key[6]}] % inhibition at stated conc. (n={len(rs)}; see assay text in detail)")
        if len(chunks) > 14:
            chunks = chunks[:14] + [f"... {len(gs) - 14} more groups in measures_detail.tsv"]
        parts.append(f"{ce['label']}: " + (" | ".join(chunks) if chunks else "no row matching the case target/assay filter"))
    for tf in res["target_first"]:
        rs = [r for r in tf["rows"] if r.get("standard_units") == "nM" and rel(r.get("standard_relation")) == "=" and num(r) is not None]
        n_pot = len({r["molecule_chembl_id"] for r in rs if num(r) <= tf["spec"]["potent_nM"]})
        parts.append(f"target-first {tf['spec']['label']}: {tf['state']}, {tf['retrieved']} of {tf['total']} rows, {n_pot} molecules with an '=' value at or below {tf['spec']['potent_nM']} nM")
    return " ## ".join(parts)


def status_summary(res):
    parts = []
    for ce in res["compounds"]:
        st = ", ".join(f"{k}:{v['state']}({v['retrieved']}/{v['total']})" for k, v in ce["status"].items())
        parts.append(f"{ce['label']}: {st}")
    for tf in res["target_first"]:
        parts.append(f"{tf['spec']['target']}:{tf['state']}({tf['retrieved']}/{tf['total']}{', TRUNCATED' if tf['truncated'] else ''})")
    for f in res["fda"]:
        parts.append(f"openFDA {f['generic']}:{f['state']}")
    return "; ".join(parts)


def identity_summary(res):
    out = []
    for ce in res["compounds"]:
        for m in ce["molecules"]:
            if m["state"] != "OK":
                out.append(f"{m['id']}:{m['state']}")
                continue
            role = "parent" if m["is_parent"] else f"salt/child of {m['parent']}"
            out.append(f"{m['id']} {m['pref_name']} ({role}; {m['chirality']}; max_phase {m['max_phase']})")
        mech = sorted({(a, b) for _, a, b, _ in ce["mechanisms"]})
        out.append("mechanism: " + ("; ".join(f"{a} / {b} -> sign {SIGN.get(a or '', 'not stated')}" for a, b in mech) if mech else "none curated"))
    return " | ".join(out)


def fda_summary(res):
    out = []
    for f in res["fda"]:
        if f["state"] != "OK":
            out.append(f"openFDA {f['generic']}: {f['state']} (HTTP {f['http']}) - not absence of a label")
            continue
        out.append(f"US label {f['brand']} ({f['product_type']}; {f['manufacturer']}; effective {f['effective_time']}; set {f['set_id']}; boxed warning {'yes' if f['boxed_warning'] else 'no'}): "
                   + (" // ".join(f["snippets"]) if f["snippets"] else "no sentence matching the case pattern"))
    return " || ".join(out)


def gd_summary(res):
    g = res["gtopdb"]
    d = res["dgidb"]
    gs = "GtoPdb: " + ("; ".join(f"{x['ligand']} -> {x['target']} ({x['species']}) {x['action']} {x['units']} {x['median']} (PMID {x['pmid']})" for x in g if "ligand" in x) or "no row for the names queried")
    ds = "DGIdb: " + (f"{len(d)} drug-gene-type rows (" + "; ".join(f"{x['drug']}/{x['gene']}/{x['interaction']}" for x in d[:5]) + ")" if d and "drug" in d[0] else "no row for the names queried")
    return gs + " | " + ds


HEAD = ["case_id", "research_purpose", "cards_and_needs", "compound_identity_and_action_sign", "quantitative_measures_by_assay_type_not_aggregated",
        "selectivity", "assay_concentration_and_duration", "human_exposure", "nervous_system_data", "favourable_signals", "contrary_signals", "unknown_signals",
        "experimental_context", "gtopdb_dgidb", "service_status", "old_decision", "new_decision", "decision_status", "datum_that_changed_it", "literature_abstract_level", "retrieved_on"]


def comparison_rows(results, cases, stamp):
    rows = []
    for case in cases:
        res = results[case["id"]]
        lit = " ; ".join(f"PMID {l['pmid']} (DOI {l['doi']}; {l['level']}): {l['point']}" for l in case.get("literature", [])) or "none used"
        fdatxt = fda_summary(res)
        rows.append([case["id"], case["purpose"], "; ".join(case["cards"]) + " -> " + "; ".join(case["needs"]), identity_summary(res), measures_summary(res, case),
                     case["selectivity"], case["assay_conditions"], case["exposure"] + " || " + fdatxt, case["nervous_system"], case["favourable"], case["contrary"],
                     case["unknown"], case["context"], gd_summary(res), status_summary(res), case["old_decision"], case["new_decision"], case["decision_status"],
                     case["changed_datum"], lit, stamp])
    return rows


def write_tsv(path, head, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        for r in rows:
            w.writerow([re.sub(r"[\t\r\n]+", " ", str(c)) for c in r])


def build(results, cases, out, stamp):
    det = []
    for c in cases:
        det += detail_rows(results[c["id"]], c)
    write_tsv(out / "measures_detail.tsv", DETAIL_HEAD, det)
    write_tsv(out / "comparison.tsv", HEAD, comparison_rows(results, cases, stamp))
    return len(det)


def cmd_run(out):
    cases = json.load(open(HERE / "cases.json"))["cases"]
    cache = os.environ.get("LEGEND_CATALOG_CACHE", "")
    if not cache:
        sys.exit("set LEGEND_CATALOG_CACHE to the catalogue cache directory")
    net = Net()
    results = {}
    for c in cases:
        results[c["id"]] = collect(net, c, cache)
        print(f"{c['id']}: {status_summary(results[c['id']])[:200]}", file=sys.stderr)
    stamp = time.strftime("%Y-%m-%d", time.gmtime())
    blob = json.dumps({"retrieved_on": stamp, "results": results}, sort_keys=True).encode()
    raw_gz = gzip.compress(json.dumps({"retrieved_on": stamp, "responses": net.raw, "collected": results}, sort_keys=True).encode(), mtime=0)
    hashes = [["item", "sha256", "bytes"]]
    for k in sorted(net.raw):
        hashes.append([k[:160], sha(net.raw[k]), len(json.dumps(net.raw[k]))])
    for rel_path in ("gtopdb/interactions.csv", "dgidb/interactions.tsv"):
        p = Path(cache) / rel_path
        if p.exists():
            hashes.append([f"cache:{rel_path}", hashlib.sha256(p.read_bytes()).hexdigest(), p.stat().st_size])
    write_tsv(out / "raw_hashes.tsv", hashes[0], hashes[1:])
    if len(raw_gz) < RAW_LIMIT:
        (out / "raw_store.json.gz").write_bytes(raw_gz)
        print(f"raw store kept ({len(raw_gz)} bytes gz)")
    else:
        (out / "raw_store.json.gz").unlink(missing_ok=True)
        print(f"raw responses NOT kept ({len(raw_gz)} bytes gz >= {RAW_LIMIT}); hashes listed in raw_hashes.tsv")
    col_gz = gzip.compress(json.dumps({"retrieved_on": stamp, "collected": results}, sort_keys=True).encode(), mtime=0)
    if len(col_gz) < RAW_LIMIT:   # DERIVED (adapter-normalised rows), not raw; lets 'rebuild' work offline
        (out / "collected.json.gz").write_bytes(col_gz)
        print(f"collected (derived) rows kept ({len(col_gz)} bytes gz)")
    else:
        (out / "collected.json.gz").unlink(missing_ok=True)
        print(f"collected rows NOT kept ({len(col_gz)} bytes gz)")
    write_tsv(out / "service_log.tsv", ["case", "attempt", "status", "seconds", "url", "error"], [[l["case"], l["attempt"], l["status"], l["seconds"], l["url"], l["error"]] for l in net.log])
    n = build(results, cases, out, stamp)
    print(f"comparison.tsv {len(cases)} cases; measures_detail.tsv {n} rows; attempts logged {len(net.log)}; non-200 attempts {sum(1 for l in net.log if l['status'] not in (200, 404))}")


def cmd_rebuild(out):
    p = out / "collected.json.gz"
    if not p.exists():
        p = out / "raw_store.json.gz"
    if not p.exists():
        sys.exit("no stored rows (>= 1 MB): rebuild needs a live run; compare raw_hashes.tsv instead")
    d = json.loads(gzip.decompress(p.read_bytes()))
    cases = json.load(open(HERE / "cases.json"))["cases"]
    n = build(d["collected"], cases, out, d["retrieved_on"])
    print(f"rebuilt comparison.tsv ({len(cases)} cases) and measures_detail.tsv ({n} rows) from the stored responses")


def selftest():
    from framework.adapters import chembl
    # 1: two 500s then success -> retried, logged, result is data
    calls = {"n": 0}
    def flaky(url, params=None, body=None, timeout=40):
        calls["n"] += 1
        if "status.json" in url:
            return 200, {"chembl_db_version": "T", "chembl_release_date": "x"}
        if calls["n"] <= 3:
            return 500, "boom"
        return 200, {"activities": [], "page_meta": {"total_count": 0, "next": None}}
    sleeps = []
    net = Net(sleep=sleeps.append, get=flaky)
    r = chembl.query({"molecule": "CHEMBL1", "types": ["IC50"]}, fetch=net.get)
    assert state_of(r) == "NO_ROWS_UNDER_FILTERS", state_of(r)
    assert [l["status"] for l in net.log if "activity" in l["url"]] == [500, 500, 200] or len(net.log) >= 4, net.log
    assert sleeps and sleeps[0] == 2, sleeps
    # 2: permanent 500 -> SERVICE_ERROR, never NO_ROWS
    net2 = Net(sleep=lambda s: None, get=lambda u, p=None, b=None, t=40: (200, {"chembl_db_version": "T", "chembl_release_date": "x"}) if "status.json" in u else (500, "down"))
    r2 = chembl.query({"molecule": "CHEMBL1", "types": ["IC50"]}, fetch=net2.get)
    assert state_of(r2) == "SERVICE_ERROR", state_of(r2)
    assert sum(1 for l in net2.log if l["status"] == 500) == len(BACKOFF), net2.log
    # 3: transport failure (status 0) is retried too
    net3 = Net(sleep=lambda s: None, get=lambda u, p=None, b=None, t=40: (0, "URLError: x") if "activity" in u else (200, {}))
    r3 = chembl.query({"molecule": "CHEMBL1", "types": ["IC50"]}, fetch=net3.get)
    assert state_of(r3) == "SERVICE_ERROR"
    # 4: a 404 is an answer, not an error
    net4 = Net(sleep=lambda s: None, get=lambda u, p=None, b=None, t=40: (404, {}))
    assert net4.get("https://x/y")[0] == 404 and len(net4.log) == 1
    # 5: grouping never merges different units or relations
    rows = [{"target_pref_name": "T", "target_organism": "H", "standard_type": "IC50", "standard_relation": "=", "standard_units": "nM", "standard_value": "5", "molecule_chembl_id": "M", "assay_context": {"assay_type": "B"}},
            {"target_pref_name": "T", "target_organism": "H", "standard_type": "IC50", "standard_relation": ">", "standard_units": "nM", "standard_value": "9", "molecule_chembl_id": "M", "assay_context": {"assay_type": "B"}},
            {"target_pref_name": "T", "target_organism": "H", "standard_type": "IC50", "standard_relation": "=", "standard_units": "nM", "standard_value": "7", "molecule_chembl_id": "M", "assay_context": {"assay_type": "F"}}]
    assert len(groups(rows, "T", None)) == 3
    print("selftest OK (5 checks)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run", "rebuild", "selftest"])
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    out = Path(a.out)
    {"run": lambda: cmd_run(out), "rebuild": lambda: cmd_rebuild(out), "selftest": selftest}[a.cmd]()


if __name__ == "__main__":
    main()
