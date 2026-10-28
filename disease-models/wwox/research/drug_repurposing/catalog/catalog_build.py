#!/usr/bin/env python3
"""Compound catalogue for the drug-repurposing module: fetch (cached, incremental), build, stats,
link existing cards, query.  Standard library only, no key, no e-mail/contact string sent anywhere,
no LLM call.  Non-canonical research material: a catalogue says what exists and under which source
and scope; it never says a compound is suitable, safe, effective or obtainable by anyone.

  catalog_build.py fetch  [--refresh] [--only SRC[,SRC]]   download into cache/ (skips fresh sources)
  catalog_build.py probe-dsld [--limit N] [--refresh]       supplement-label probe (name-only; see README)
  catalog_build.py build                                    cache -> catalog.jsonl.gz + stats + links
  catalog_build.py all [--refresh]                          fetch + build
  catalog_build.py query (--id X | --name X | --target X | --access X | --status X) [--limit N]
  catalog_build.py verify                                   reconcile counts of the written outputs

Honesty rules enforced in code: a source that failed or came back short is recorded as
INCOMPLETE/FAILED in cache_manifest.json and shown as NOT AVAILABLE in the stats (never as 0);
UNKNOWN is never a negative; entries are merged only on declared identifier keys (README).
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import hashlib
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get("LEGEND_CATALOG_CACHE", HERE / "cache"))
MANIFEST = HERE / "cache_manifest.json"
OUT_CATALOG = HERE / "catalog.jsonl.gz"
OUT_STATS = HERE / "catalog_stats.json"
OUT_LINKS = HERE / "card_links.json"
OUT_MODALITIES = HERE / "non_molecule_modalities.tsv"
DECLARATIONS = HERE / "card_identity_declarations.tsv"
MODULE = HERE.parent
UA = "LEGEND-compound-catalog/1 (research; key-less; no contact string)"
SCHEMA = 1
TTL_DAYS = 30
GTOPDB_FILES = ("interactions.csv", "targets_and_families.csv")

CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"
UNICHEM = "https://ftp.ebi.ac.uk/pub/databases/chembl/UniChem/data/wholeSourceMapping/src_id1/src1src{n}.txt.gz"
SOURCES = {
    "chembl": dict(
        name="ChEMBL", licence="CC BY-SA 3.0 (verified 2026-10-28, chembl.gitbook.io About: 'made available on a Creative Commons Attribution-Share Alike 3.0 Unported License'); web access under EBI Terms of Use",
        terms="https://www.ebi.ac.uk/about/terms-of-use",
        note="share-alike: an adaptation (the ChEMBL-derived rows of catalog.jsonl.gz and anything built from them) must carry CC BY-SA 3.0 and attribution; mixing with differently licensed rows makes the file a composite whose ChEMBL-derived part keeps that licence"),
    "unichem": dict(
        name="UniChem (EMBL-EBI) whole-source mappings ChEMBL<->DrugBank/ChEBI/UNII", licence="EMBL-EBI Terms of Use (UniChem docs, read 2026-10-28, point to them; no CC0 statement found, so none is claimed)",
        terms="https://www.ebi.ac.uk/about/terms-of-use", note="identifier cross-references only; EBI expects attribution"),
    "dgidb": dict(
        name="DGIdb (drugs.tsv, interactions.tsv)", licence="NOT CLEARED FOR PUBLIC RELEASE as a whole. DGIdb applies no data licence of its own (its software is MIT; the dgidb-data README of 2026-10-14 states that the claims of each source remain subject to that source's licence and that DGIdb applies no additional terms); the export of 2024-06-10 therefore carries 21 source databases with different terms (see catalog/README.md, section 'Licence reconciliation'). The repository is public, so rows from non-commercial, share-alike or unclear sources (for example DTC, CKB-CORE, CGI, TTD, ChEMBL, GuideToPharmacology, PharmGKB) are an exposure to be decided by the operator, not a held-back item",
        terms="https://dgidb.org/downloads", note="the TSV release of 2024-06-10 is the newest the site serves at /data/latest"),
    "gtopdb": dict(
        name="IUPHAR/BPS Guide to PHARMACOLOGY (GtoPdb) interactions.csv + targets_and_families.csv", licence="database under ODbL; contents under CC BY-SA 4.0 (guidetopharmacology.org/about.jsp and /download.jsp, read 2026-10-28); public download, no registration",
        terms="https://www.guidetopharmacology.org/download.jsp", note="used ONLY to verify and correct the identity of the DGIdb Guide-to-Pharmacology rows (see README, 'Target identity'); share-alike: the GtoPdb-derived fields (target ids, names, types) of catalog.jsonl.gz must carry CC BY-SA 4.0 and attribution"),
    "matrix": dict(
        name="Every Cure MATRIX drug list", licence="CC BY 4.0 (dataset-card metadata of everycure/drug-list, read 2026-10-27, HF API)",
        terms="https://huggingface.co/datasets/everycure/drug-list", note="applies to the drug list only; the knowledge graph and the scores table are separate artefacts with their own (or no declared) terms and nothing is transferred to them; the scores table is not used"),
    "openfda_ndc": dict(
        name="openFDA drug/ndc bulk download", licence="CC0 1.0 / US public domain (verified 2026-10-28 at open.fda.gov/license: 'public domain ... CC0 1.0 Universal dedication', third-party content on the site such as GMDN is excluded; not present in the NDC fields used)",
        terms="https://open.fda.gov/terms/", note="openFDA disclaimer: do not rely on it for decisions about medical care"),
    "dsld": dict(
        name="NIH ODS Dietary Supplement Label Database API v9", licence="CC0 1.0 (API documentation licence block, read 2026-10-27; the documentation page also lists a contact address, which this tool never uses)",
        terms="https://dsld.od.nih.gov/", note="per-query API; no bulk file was fetched; labels carry no UNII, so matching is by name only"),
}


# ----------------------------------------------------------------------------- utilities
def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def http(url: str, timeout: float = 90.0, tries: int = 3, want_headers: bool = False):
    """(status, bytes[, headers]).  status 0 = transport failure; never raises."""
    last = (0, f"no attempt".encode(), {})
    for i in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, */*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read()
                last = (r.status, body, dict(r.headers))
        except urllib.error.HTTPError as e:
            last = (e.code, (e.read() if e.fp else b""), dict(e.headers or {}))
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            last = (0, f"{type(e).__name__}: {e}".encode(), {})
        if last[0] == 200 or last[0] in (400, 404):
            break
        time.sleep(1.5 * (i + 1))
    return last if want_headers else last[:2]


def jget(url: str, **kw):
    st, body = http(url, **kw)[:2]
    if st != 200:
        return st, body.decode("utf-8", "replace")[:300]
    try:
        return 200, json.loads(body)
    except ValueError as e:
        return -1, f"unparseable JSON: {e}"


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"schema_version": SCHEMA, "sources": {}}


def save_manifest(m: dict) -> None:
    for k, e in m["sources"].items():  # terms text always follows the code's verified statement
        if k in SOURCES:
            e.update({x: SOURCES[k][x] for x in ("name", "licence", "terms")})
    MANIFEST.write_text(json.dumps(m, indent=1, sort_keys=True) + "\n")


def fresh(m: dict, src: str, ttl: int = TTL_DAYS) -> bool:
    d = m["sources"].get(src, {}).get("data")
    if not d or d.get("status") != "OK":
        return False
    files_ok = all((CACHE / f["path"]).exists() for f in d.get("files", []))
    age = (datetime.now(timezone.utc) - datetime.strptime(d["retrieved_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)).days
    return files_ok and age < ttl


def record(m: dict, src: str, status: str, detail: str, data: dict | None = None) -> None:
    """`data` = last complete retrieval (kept when a refresh fails); `last_attempt` = what just happened."""
    e = m["sources"].setdefault(src, {})
    e.update({k: SOURCES[src][k] for k in ("name", "licence", "terms")})
    e["last_attempt"] = {"utc": now(), "status": status, "detail": detail}
    if data is not None and status == "OK":
        e["data"] = data


def write_gz_jsonl(path: Path, rows) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with gzip.GzipFile(tmp, "wb", mtime=0) as fh:
        for r in rows:
            fh.write((json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n").encode())
    tmp.replace(path)
    return sha256_file(path)


def read_gz_jsonl(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)


# ----------------------------------------------------------------------------- fetchers
MOL_ONLY = ("molecule_chembl_id,pref_name,max_phase,first_approval,molecule_type,molecule_hierarchy,"
            "molecule_structures,molecule_synonyms,atc_classifications,withdrawn_flag,therapeutic_flag,"
            "natural_product,prodrug,black_box_warning,chemical_probe,first_in_class,dosed_ingredient,"
            "availability_type,structure_type,chirality,oral,parenteral,topical,biotherapeutic,"
            "usan_stem,inorganic_flag")
MOL_QUERIES = {"phase_ge_0_5": "max_phase__gte=0.5", "phase_unknown": "max_phase=-1", "chemical_probe": "chemical_probe=1"}


def page_all(base: str, key: str, query: str, limit: int = 1000, sleep: float = 0.15):
    """Walk a ChEMBL list endpoint.  Returns (rows, expected_total, error)."""
    rows, total, off = [], None, 0
    while True:
        st, js = jget(f"{base}?{query}&limit={limit}&offset={off}")
        if st != 200 or not isinstance(js, dict) or key not in js:
            return rows, total, f"HTTP {st}: {str(js)[:160]}"
        total = js["page_meta"]["total_count"]
        rows.extend(js[key])
        if not js["page_meta"].get("next"):
            return rows, total, ""
        off += limit
        time.sleep(sleep)


def fetch_chembl(m: dict, refresh: bool) -> None:
    if not refresh and fresh(m, "chembl"):
        return
    st, status = jget(f"{CHEMBL}/status.json")
    if st != 200 or not isinstance(status, dict):
        record(m, "chembl", "FAILED", f"status endpoint: HTTP {st}")
        return
    version = f"{status.get('chembl_db_version')} {status.get('chembl_release_date')}"
    files, counts, problems = [], {}, []
    mols: dict[str, dict] = {}
    for name, q in MOL_QUERIES.items():
        rows, total, err = page_all(f"{CHEMBL}/molecule.json", "molecules", f"{q}&only={MOL_ONLY}")
        counts[name] = {"expected": total, "received": len(rows)}
        if err or total != len(rows):
            problems.append(f"molecule {name}: expected {total}, received {len(rows)} {err}")
        for r in rows:
            mols[r["molecule_chembl_id"]] = r
    # parents of selected children that the filters did not select (kept so a salt never loses its parent)
    want = sorted({r["molecule_hierarchy"]["parent_chembl_id"] for r in mols.values() if r.get("molecule_hierarchy")} - set(mols))
    extra = {}
    for i in range(0, len(want), 40):
        rows, total, err = page_all(f"{CHEMBL}/molecule.json", "molecules", f"molecule_chembl_id__in={','.join(want[i:i+40])}&only={MOL_ONLY}")
        if err or total != len(rows):
            problems.append(f"parent batch {i}: expected {total}, received {len(rows)} {err}")
        for r in rows:
            extra[r["molecule_chembl_id"]] = r
    counts["parents_added"] = {"expected": len(want), "received": len(extra)}
    if len(extra) != len(want):
        problems.append(f"parents: asked {len(want)}, received {len(extra)} (missing ones stay unresolved, listed in stats)")
    selected = set(mols)
    out = [dict(r, _selection="selected") for r in mols.values()] + [dict(r, _selection="parent_added") for r in extra.values()]
    out.sort(key=lambda r: r["molecule_chembl_id"])
    sha = write_gz_jsonl(CACHE / "chembl/molecules.jsonl.gz", out)
    files.append({"path": "chembl/molecules.jsonl.gz", "sha256": sha, "rows": len(out)})
    mechs, total, err = page_all(f"{CHEMBL}/mechanism.json", "mechanisms", "")
    counts["mechanisms"] = {"expected": total, "received": len(mechs)}
    if err or total != len(mechs):
        problems.append(f"mechanisms: expected {total}, received {len(mechs)} {err}")
    sha = write_gz_jsonl(CACHE / "chembl/mechanisms.jsonl.gz", sorted(mechs, key=lambda r: r["mec_id"]))
    files.append({"path": "chembl/mechanisms.jsonl.gz", "sha256": sha, "rows": len(mechs)})
    tids = sorted({x["target_chembl_id"] for x in mechs if x.get("target_chembl_id")})
    tg = []
    for i in range(0, len(tids), 40):
        rows, total, err = page_all(f"{CHEMBL}/target.json", "targets",
                                    f"target_chembl_id__in={','.join(tids[i:i+40])}&only=target_chembl_id,pref_name,target_type,organism,target_components")
        if err or total != len(rows):
            problems.append(f"targets batch {i}: expected {total}, received {len(rows)} {err}")
        tg.extend(rows)
    counts["targets"] = {"expected": len(tids), "received": len(tg)}
    sha = write_gz_jsonl(CACHE / "chembl/targets.jsonl.gz", sorted(tg, key=lambda r: r["target_chembl_id"]))
    files.append({"path": "chembl/targets.jsonl.gz", "sha256": sha, "rows": len(tg)})
    data = {"status": "OK" if not problems else "INCOMPLETE", "retrieved_utc": now(), "version": version,
            "url": CHEMBL, "files": files, "counts": counts, "problems": problems,
            "chembl_status": {k: status.get(k) for k in ("disinct_compounds", "compound_records", "activities", "targets")}}
    record(m, "chembl", data["status"], "; ".join(problems) or "complete", data if data["status"] == "OK" else None)
    if problems:
        m["sources"]["chembl"]["incomplete_attempt"] = data


def fetch_file(m: dict, src: str, jobs: list[tuple[str, str]], version_fn, refresh: bool) -> None:
    """jobs = [(url, cache-relative path)].  Whole-file sources."""
    if not refresh and fresh(m, src):
        return
    files, problems, versions = [], [], {}
    for url, rel in jobs:
        st, body, hdr = http(url, timeout=300, want_headers=True)
        if st != 200 or not body:
            problems.append(f"{url}: HTTP {st}")
            continue
        cl = hdr.get("Content-Length") or hdr.get("content-length")
        if cl and int(cl) != len(body):
            problems.append(f"{url}: truncated ({len(body)} of {cl} bytes)")
            continue
        p = CACHE / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(p.suffix + ".tmp")
        tmp.write_bytes(body)
        tmp.replace(p)
        files.append({"path": rel, "url": url, "bytes": len(body), "sha256": sha256_file(p)})
        versions[rel] = hdr.get("Last-Modified") or hdr.get("last-modified") or "none stated"
    data = {"status": "OK" if not problems else "INCOMPLETE", "retrieved_utc": now(), "files": files,
            "version": version_fn(versions), "problems": problems}
    record(m, src, data["status"], "; ".join(problems) or "complete", data if not problems else None)
    if problems:
        m["sources"][src]["incomplete_attempt"] = data


def fetch_unichem(m, refresh):
    jobs = [(UNICHEM.format(n=n), f"unichem/src1src{n}.txt.gz") for n in (2, 7, 14)]
    fetch_file(m, "unichem", jobs, lambda v: "Last-Modified " + "; ".join(f"{k.split('/')[-1]}={x}" for k, x in sorted(v.items())), refresh)


def fetch_dgidb(m, refresh):
    was_fresh = (not refresh) and fresh(m, "dgidb")
    jobs = [("https://dgidb.org/data/latest/drugs.tsv", "dgidb/drugs.tsv"), ("https://dgidb.org/data/latest/interactions.tsv", "dgidb/interactions.tsv")]
    fetch_file(m, "dgidb", jobs, lambda v: "latest as served; Last-Modified " + "; ".join(sorted(set(v.values()))), refresh)
    if was_fresh and (CACHE / "dgidb/live_sources.json").exists():
        return
    # current SERVICE coverage (source database versions the live API reports), kept apart from the TSV export
    req = urllib.request.Request("https://dgidb.org/api/graphql", data=json.dumps({"query": "{ sources { nodes { sourceDbName sourceDbVersion } } }"}).encode(),
                                 headers={"User-Agent": UA, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            nodes = json.loads(r.read())["data"]["sources"]["nodes"]
        (CACHE / "dgidb").mkdir(parents=True, exist_ok=True)
        (CACHE / "dgidb/live_sources.json").write_text(json.dumps({"retrieved_utc": now(), "nodes": nodes}, sort_keys=True, indent=0))
        m["sources"]["dgidb"]["live_service_sources"] = {"retrieved_utc": now(), "n_sources": len(nodes), "status": "OK"}
    except Exception as e:  # noqa: BLE001 - recorded, not hidden
        m["sources"]["dgidb"]["live_service_sources"] = {"retrieved_utc": now(), "status": "FAILED", "detail": f"{type(e).__name__}: {e}"}


def fetch_gtopdb(m, refresh):
    base = "https://www.guidetopharmacology.org/DATA/"
    jobs = [(base + f, "gtopdb/" + f) for f in GTOPDB_FILES]
    fetch_file(m, "gtopdb", jobs, lambda v: "latest download as served", refresh)
    d = m["sources"].get("gtopdb", {}).get("data")
    if d and (CACHE / "gtopdb/interactions.csv").exists():
        with open(CACHE / "gtopdb/interactions.csv", encoding="utf-8") as fh:
            d["version"] = fh.readline().strip().strip('"').lstrip("# ").strip()


def fetch_ndc(m, refresh):
    if not refresh and fresh(m, "openfda_ndc"):
        return
    st, dl = jget("https://api.fda.gov/download.json")
    if st != 200:
        record(m, "openfda_ndc", "FAILED", f"download.json HTTP {st}")
        return
    ndc = dl["results"]["drug"]["ndc"]
    parts = ndc["partitions"]
    jobs = [(p["file"], "openfda/" + p["file"].rsplit("/", 1)[-1]) for p in parts]
    fetch_file(m, "openfda_ndc", jobs, lambda v: f"export_date {ndc['export_date']}", refresh)
    e = m["sources"]["openfda_ndc"].get("data")
    if e and e["retrieved_utc"].startswith(now()[:10]):
        e["declared_records"] = ndc["total_records"]
        n = 0
        for f in e["files"]:
            with zipfile.ZipFile(CACHE / f["path"]) as z:
                n += len(json.load(z.open(z.namelist()[0]))["results"])
        e["parsed_records"] = n
        if n != ndc["total_records"]:
            e["status"] = "INCOMPLETE"
            e["problems"] = [f"parsed {n} of declared {ndc['total_records']}"]
            m["sources"]["openfda_ndc"]["incomplete_attempt"] = e
            del m["sources"]["openfda_ndc"]["data"]
            m["sources"]["openfda_ndc"]["last_attempt"]["status"] = "INCOMPLETE"


def fetch_matrix(m, refresh):
    if not refresh and fresh(m, "matrix"):
        return
    st, meta = jget("https://huggingface.co/api/datasets/everycure/drug-list")
    if st != 200:
        record(m, "matrix", "FAILED", f"HF api HTTP {st}")
        return
    rows, total, off = [], None, 0
    while True:
        st, js = jget(f"https://datasets-server.huggingface.co/rows?dataset=everycure/drug-list&config=default&split=train&offset={off}&length=100")
        if st != 200 or "rows" not in js:
            record(m, "matrix", "FAILED", f"rows offset {off}: HTTP {st}")
            return
        total = js["num_rows_total"]
        rows.extend(r["row"] for r in js["rows"])
        off += 100
        if off >= total:
            break
    ok = len(rows) == total
    sha = write_gz_jsonl(CACHE / "matrix/drug_list.jsonl.gz", rows)
    data = {"status": "OK" if ok else "INCOMPLETE", "retrieved_utc": now(), "version": f"HF commit {meta.get('sha')}",
            "licence_declared": (meta.get("cardData") or {}).get("license"), "url": "https://huggingface.co/datasets/everycure/drug-list",
            "files": [{"path": "matrix/drug_list.jsonl.gz", "sha256": sha, "rows": len(rows)}], "declared_rows": total,
            "problems": [] if ok else [f"received {len(rows)} of {total}"]}
    record(m, "matrix", data["status"], "; ".join(data["problems"]) or "complete", data if ok else None)


def fetch_chembl_lookup(m, ids: set[str]) -> None:
    """entity type of each CHEMBL id mentioned in cards (compound/target/document share one prefix)."""
    p = CACHE / "chembl/id_lookup.json"
    have = json.loads(p.read_text()) if p.exists() else {}
    for i in sorted(ids - set(have)):
        st, js = jget(f"{CHEMBL}/chembl_id_lookup/{i}.json")
        have[i] = {"entity_type": js.get("entity_type")} if st == 200 and isinstance(js, dict) else {"entity_type": None, "error": f"HTTP {st}"}
        time.sleep(0.1)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(have, sort_keys=True, indent=0))


FETCHERS = {"chembl": fetch_chembl, "unichem": fetch_unichem, "dgidb": fetch_dgidb, "gtopdb": fetch_gtopdb,
            "openfda_ndc": fetch_ndc, "matrix": fetch_matrix}


def card_chembl_ids() -> set[str]:
    out = set()
    for f in card_files():
        for _cid, text in card_key(f, json.loads(f.read_text())):
            out |= set(ID_RE.findall(text))
    return out


def cmd_fetch(args) -> int:
    """NETWORK step.  `build` never touches the network."""
    m = load_manifest()
    only = set(args.only.split(",")) if args.only else set(FETCHERS)
    for src in FETCHERS:
        if src in only:
            before = m["sources"].get(src, {}).get("last_attempt", {}).get("utc")
            FETCHERS[src](m, args.refresh)
            a = m["sources"].get(src, {}).get("last_attempt", {})
            print(f"{src}: " + ("SKIPPED_FRESH (cache newer than %d days; use --refresh)" % TTL_DAYS if a.get("utc") == before and before else f"{a.get('status')} {a.get('detail', '')}".rstrip()))
            save_manifest(m)
    if not args.only or "chembl" in args.only:
        ids = card_chembl_ids()
        fetch_chembl_lookup(m, ids)
        m["sources"].setdefault("chembl", {})["id_lookup"] = {"utc": now(), "ids_looked_up": len(ids), "file": "chembl/id_lookup.json",
                                                              "purpose": "entity type (COMPOUND/TARGET/DOCUMENT) of CHEMBL ids mentioned in cards"}
        save_manifest(m)
    return 0


# ----------------------------------------------------------------------------- DSLD probe (name-only)
def dsld_probe_one(name: str) -> dict:
    q = urllib.parse.quote(f'"{name}"')
    st, js = jget(f"https://api.ods.od.nih.gov/dsld/v9/search-filter?q={q}&size=50", timeout=60)
    base = {"query": name, "retrieved_utc": now()}
    if st != 200 or not isinstance(js, dict) or "hits" not in js:
        return dict(base, status="ERROR", detail=f"HTTP {st} {str(js)[:100]}")
    n = norm(name)
    exact, ids = 0, []
    for h in js["hits"]:
        s = h.get("_source", {})
        if any(norm(i.get("ingredientGroup", "")) == n or norm(i.get("name", "")) == n for i in s.get("allIngredients", [])):
            exact += 1
            if len(ids) < 3:
                ids.append(h.get("_id"))
    return dict(base, status="OK", total_fulltext_hits=js.get("stats", {}).get("count"), sample_size=len(js["hits"]),
                exact_ingredient_in_sample=exact, example_label_ids=ids)


def cmd_probe(args) -> int:
    p = CACHE / "dsld/probes.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    done = {}
    if p.exists():
        for line in p.read_text().splitlines():
            r = json.loads(line)
            done[r["query"]] = r
    if args.retry_errors:
        names, tag = sorted(k for k, r in done.items() if r["status"] != "OK"), "bulk"
    elif args.names:
        names = [x.strip() for x in args.names.split(",") if x.strip()]
        tag = "targeted"
    else:
        names, tag = probe_names(), "bulk"
    todo = [n for n in names if args.refresh or n not in done or done[n]["status"] != "OK"]
    if args.limit:
        todo = todo[: args.limit]
    print(f"probe: {len(names)} names, {len(todo)} to query")
    with ThreadPoolExecutor(max_workers=3) as ex, open(p, "a") as fh:
        for r in ex.map(dsld_probe_one, todo):
            r["set"] = tag
            fh.write(json.dumps(r, sort_keys=True) + "\n")
            fh.flush()
    m = load_manifest()
    rows = {}
    for line in p.read_text().splitlines():
        r = json.loads(line)
        rows[r["query"]] = r
    ok = sum(1 for r in rows.values() if r["status"] == "OK")
    record(m, "dsld", "OK" if ok else "FAILED", f"{'PARTIAL: ' if ok != len(rows) else ''}{ok} probes OK, {len(rows) - ok} errors",
           {"status": "OK", "retrieved_utc": now(), "version": "API v9.4.0",
            "url": "https://api.ods.od.nih.gov/dsld/v9/search-filter", "files": [{"path": "dsld/probes.jsonl", "rows": len(rows)}], "problems": []})
    save_manifest(m)
    return 0


def probe_names() -> list[str]:
    """Which names get a supplement probe: approved-by-ChEMBL (phase 4) pref_names + MATRIX names, sorted."""
    names = set()
    mp = CACHE / "chembl/molecules.jsonl.gz"
    if mp.exists():
        for r in read_gz_jsonl(mp):
            if r.get("pref_name") and str(r.get("max_phase")) in ("4.0", "4") and r["_selection"] == "selected":
                names.add(r["pref_name"].title())
    xp = CACHE / "matrix/drug_list.jsonl.gz"
    if xp.exists():
        for r in read_gz_jsonl(xp):
            if not r.get("deleted") and r.get("name"):
                names.add(r["name"])
    return sorted(names, key=lambda x: (x.lower(), x))


# ----------------------------------------------------------------------------- build
def read_unichem(n: int) -> list[tuple[str, str]]:
    out = []
    with gzip.open(CACHE / f"unichem/src1src{n}.txt.gz", "rt") as fh:
        next(fh)
        for line in fh:
            a = line.rstrip("\n").split("\t")
            if len(a) == 2:
                out.append((a[0], a[1]))
    return out


def read_tsv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def inchikey_skeleton(k: str | None) -> str | None:
    return k.split("-")[0] if k and "-" in k else None


def classify_modality(molecule_type: str | None, biotherapeutic) -> str:
    t = (molecule_type or "").lower()
    return {"small molecule": "small_molecule", "protein": "protein_or_peptide", "antibody": "antibody",
            "oligonucleotide": "oligonucleotide", "oligosaccharide": "oligosaccharide", "enzyme": "enzyme",
            "cell": "cell_product", "gene": "gene_product", "unknown": "unknown"}.get(t, "unknown" if not t else "other:" + t)


def new_entry(cid: str, origin: str, name: str | None, name_source: str) -> dict:
    return {"id": cid, "origin": origin, "name": name, "name_source": name_source, "synonyms": [], "n_synonyms_total": 0,
            "ids": {}, "relations": {}, "molecule_type": None, "modality": "unknown", "status_records": [], "status_class": None,
            "access": [], "access_categories": [], "targets": [], "source_records": [], "provenance": [],
            "accessibility_is_not": "approval, appropriateness or safety (separate fields; the last two are NOT_ASSESSED)",
            "appropriateness": "NOT_ASSESSED", "safety_assessment": "NOT_ASSESSED"}


STATUS_ORDER = ["approved_any_source", "marketed_otc_monograph", "marketed_unapproved_us", "clinical_candidate",
                "phase_unknown", "tool_probe", "no_status_statement"]
NDA_LIKE = {"NDA", "ANDA", "BLA", "NDA AUTHORIZED GENERIC"}


# ----------------------------------------------------------------------------- target identity (GtoPdb rows of DGIdb)
# DGIdb's Guide-to-Pharmacology rows carry gene_claim_name "NCBIGENE:<n>" where <n> is the GtoPdb TARGET ID (an internal
# number), not an NCBI Gene id; DGIdb then resolved the number to a gene (a different gene for most rows).  The stable
# identifiers survive in the claim (drug_claim_name IUPHAR.LIGAND:<id>, gene_claim_name number = GtoPdb target id), so the
# link is verified through them against the GtoPdb release, never by symbol.
GTOPDB_TYPE_TO_DGIDB = {"Inhibitor": "inhibitor", "Antagonist": "inhibitor", "Gating inhibitor": "inhibitor", "Agonist": "agonist",
                        "Activator": "activator", "Channel blocker": "blocker", "Allosteric modulator": "modulator", "Antibody": "antibody"}


def load_gtopdb(cache: Path):
    """None when the release is not in the cache.  Otherwise a dict of plain lookups (a pure function of two CSV files)."""
    di, dt = cache / "gtopdb/interactions.csv", cache / "gtopdb/targets_and_families.csv"
    if not (di.exists() and dt.exists()):
        return None

    def rd(path):
        with open(path, encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh))
        return rows[0][0].lstrip("# ").strip(), [dict(zip(rows[1], r)) for r in rows[2:]]
    release, inter = rd(di)
    _, tgt = rd(dt)
    T: dict[str, dict] = {}
    for t in tgt:
        tid = t["Target id"]
        if not tid:
            continue
        e = T.setdefault(tid, {"name": t["Target name"], "type": t["Type"], "families": set(), "hgnc": "", "symbol": "", "subunits": []})
        e["families"].add(t["Family id"])
        if t["HGNC id"]:
            e["hgnc"], e["symbol"] = "hgnc:" + t["HGNC id"], t["HGNC symbol"]
        if t["Subunit id"]:
            e["subunits"] = t["Subunit id"].split("|")
    pairs = collections.defaultdict(list)
    lig_targets = collections.defaultdict(set)
    for r in inter:
        if r["Ligand ID"] and r["Target ID"]:
            pairs[(r["Ligand ID"], r["Target ID"])].append(r)
            if r["Target Species"] == "Human":
                lig_targets[r["Ligand ID"]].add(r["Target ID"])
    return {"release": release, "targets": T, "pairs": pairs, "ligand_human_targets": lig_targets}


def gtopdb_genes(gt: dict, tid: str) -> list[tuple[str, str]]:
    """[(hgnc concept id, symbol)] of a GtoPdb target: its own gene, or the genes of its subunits (a complex)."""
    t = gt["targets"].get(tid)
    if not t:
        return []
    if t["hgnc"]:
        return [(t["hgnc"], t["symbol"])]
    return [(gt["targets"][u]["hgnc"], gt["targets"][u]["symbol"]) for u in t["subunits"] if u in gt["targets"] and gt["targets"][u]["hgnc"]]


def identity_gtopdb(gt: dict | None, ir: dict) -> list[dict]:
    """Rows replacing one DGIdb Guide-to-Pharmacology interaction row: [{identity..., gene, gene_concept_id, ...}].
    states: confirmed (served gene is a gene of the GtoPdb target), corrected (served gene is not; the GtoPdb target's genes
    replace it, the served gene is kept as `dgidb_served_gene`), unverified (pair or gene not recoverable: the relation stays visible
    but is not counted)."""
    lig = ir["drug_claim_name"].split(":", 1)[-1]
    tid = ir["gene_claim_name"].split(":", 1)[-1]
    served = {"gene": ir["gene_name"], "gene_concept_id": ir["gene_concept_id"]}
    base = {"gene_claim_name": ir["gene_claim_name"], "iuphar_ligand_id": lig, "iuphar_target_id": tid}
    if gt is None:
        return [dict(served, **base, identity={"state": "unverified", "method": "none",
                                                "note": "the GtoPdb release is not in the cache: the DGIdb gene could not be verified through the GtoPdb target id"})]
    rows = gt["pairs"].get((lig, tid), [])
    genes = gtopdb_genes(gt, tid)
    t = gt["targets"].get(tid, {})
    if not rows or not genes:
        why = ("this (ligand, target id) pair is not in the GtoPdb release " + gt["release"] + " (DGIdb used 2024.1)") if not rows else \
              f"GtoPdb target {tid} ({t.get('name')}) has no human gene in the release"
        return [dict(served, **base, identity={"state": "unverified", "method": "gtopdb_pair_lookup", "note": why})]
    species = sorted({r["Target Species"] for r in rows})
    stated = sorted({GTOPDB_TYPE_TO_DGIDB.get(r["Type"], r["Type"]) for r in rows if r["Type"] and r["Type"] != "None"})
    served_type = None if ir["interaction_type"] in ("NULL", "") else ir["interaction_type"]
    if len(stated) == 1 and served_type in (None, stated[0]):
        itype, tstate = served_type, "agrees_with_source" if served_type else "UNKNOWN"
    elif not stated:
        itype, tstate = served_type, "UNKNOWN" if served_type is None else "source_states_no_type"
    else:
        itype, tstate = None, f"CONFLICT_WITH_SOURCE: DGIdb '{served_type}' vs GtoPdb {sorted({r['Type'] for r in rows})}"
    sibs = {x for x in gt["ligand_human_targets"].get(lig, ()) if x != tid and (gt["targets"].get(x, {}).get("families", set()) & t.get("families", set()))}
    complex_ = len(genes) > 1 or (not t.get("hgnc") and bool(t.get("subunits")))
    extra = {"iuphar_target_name": t.get("name"), "iuphar_target_class": t.get("type"), "target_level": "complex" if complex_ else "single_protein",
             "species_of_evidence": species, "selectivity_stated": sorted({r["Selectivity"] for r in rows if r["Selectivity"]}),
             "primary_target_stated": sorted({r["Primary Target"] for r in rows if r["Primary Target"]}),
             "same_family_targets_of_this_ligand": len(sibs), "gtopdb_types": sorted({r["Type"] for r in rows}),
             "gtopdb_release": gt["release"]}
    out = []
    for hg, sym in genes:
        state = "confirmed" if hg == served["gene_concept_id"] else "corrected"
        row = dict(base, gene=sym, gene_concept_id=hg, interaction_type=itype, interaction_type_state=tstate, **extra,
                   identity={"state": state, "method": "gtopdb_target_id",
                             "note": ("served gene is a gene of the GtoPdb target" if state == "confirmed" else
                                      f"DGIdb served {served['gene']} ({served['gene_concept_id']}) for GtoPdb target id {tid} = {t.get('name')}: the number was read as an NCBI Gene id")})
        if state == "corrected":
            row["dgidb_served_gene"] = served
        out.append(row)
    if not any(r["identity"]["state"] == "confirmed" for r in out):
        for r in out:
            r["dgidb_served_gene"] = served
    return out


PSEUDO_RE = re.compile(r"^(?P<root>.+?)(P\d*|-AS\d+|-IT\d+|-OT\d+)$")
# loci that are not protein-coding genes a drug could act on: antisense / lncRNA / intronic-overlapping, and endogenous-retrovirus loci
NONCODING_RE = re.compile(r"-AS\d+$|^LINC\d+|-IT\d+$|-OT\d+$")
RETROELEMENT_RE = re.compile(r"^(HERV|ERV)[A-Z0-9]*-\d+$|^HERV")
# a UniProt accession (optionally with the 'UNIPROT:' prefix) names a protein, not a gene symbol
UNIPROT_ACC_RE = re.compile(r"^(?:UNIPROT:)?(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})$")


def claim_symbol_anomaly(ir: dict) -> str | None:
    """A heuristic FLAG (not proof, never an identity statement): a claim that is not the served gene's own symbol but DGIdb
    resolved to a pseudogene, an antisense/lncRNA locus or an endogenous-retrovirus locus.  Drugs act on proteins, so the resolved
    gene is not trusted.  Covers symbol claims (MCL1 -> ADAMTSL4-AS1, HSP90AA2 -> HSP90AA2P), claims that are a UniProt accession
    (UNIPROT:Q07820 -> ADAMTSL4-AS1, UNIPROT:Q9Y233 -> LINC00473) and claims that are a protein/target name rather than a gene
    symbol (ChEMBL POL/ENV/PROTEASE -> ERVW-4/ERVK-20/ERVK-10).  A claim that is itself retroelement-named is left alone."""
    claim, gene = ir["gene_claim_name"].upper(), ir["gene_name"].upper()
    if ir["interaction_source_db_name"] == "GuideToPharmacology" or claim == gene:
        return None
    if ":" in claim and not UNIPROT_ACC_RE.match(claim):
        return None
    bare = claim.split(":", 1)[1] if claim.startswith("UNIPROT:") else claim
    m = PSEUDO_RE.match(gene)
    if m and m.group("root") == bare:
        return f"symbol claim {ir['gene_claim_name']} resolved to {ir['gene_name']}, a pseudogene/antisense locus built on that symbol"
    if NONCODING_RE.search(gene) and not NONCODING_RE.search(bare):
        what = "a UniProt accession" if UNIPROT_ACC_RE.match(claim) else "a symbol claim"
        return f"{what} {ir['gene_claim_name']} resolved to {ir['gene_name']}, a non-coding/pseudogene locus"
    if RETROELEMENT_RE.search(gene) and not RETROELEMENT_RE.search(bare):
        what = "a UniProt accession" if UNIPROT_ACC_RE.match(claim) else "claim"
        return f"{what} {ir['gene_claim_name']} resolved to {ir['gene_name']}, an endogenous-retrovirus locus; the claim is not retrovirus-named (a viral protein name is not a human gene symbol)"
    return None


def build_catalog(cache: Path | None = None) -> tuple[list[dict], dict]:
    """Pure function of the cache and manifest.  Returns (entries, stats)."""
    cache = cache or CACHE
    manifest = load_manifest()
    src_status = {}
    for s in ("chembl", "unichem", "dgidb", "gtopdb", "matrix", "openfda_ndc", "dsld"):
        e = manifest["sources"].get(s)
        if not e:
            src_status[s] = {"state": "NOT_FETCHED"}
        elif "data" in e:
            d = e["data"]
            src_status[s] = {"state": "OK" if e["last_attempt"]["status"] == "OK" else "STALE_AFTER_FAILED_REFRESH",
                             "version": d.get("version"), "retrieved_utc": d["retrieved_utc"], "licence": SOURCES[s]["licence"]}
        else:
            src_status[s] = {"state": e["last_attempt"]["status"], "detail": e["last_attempt"]["detail"]}
    avail = {s: v["state"] in ("OK", "STALE_AFTER_FAILED_REFRESH") for s, v in src_status.items()}
    if not avail["chembl"]:
        raise SystemExit("ChEMBL cache is not complete: refusing to build a catalogue without its backbone (run fetch)")

    E: dict[str, dict] = {}
    # ---- ChEMBL backbone
    chembl_v = src_status["chembl"]["version"]
    for r in read_gz_jsonl(cache / "chembl/molecules.jsonl.gz"):
        cid = "CAT:" + r["molecule_chembl_id"]
        e = new_entry(cid, "chembl_selected" if r["_selection"] == "selected" else "chembl_parent_added", r.get("pref_name"),
                      "ChEMBL pref_name" if r.get("pref_name") else "none (ChEMBL has no preferred name)")
        syn = {}
        for s in r.get("molecule_synonyms") or []:
            v = (s.get("molecule_synonym") or "").strip()
            if v and v.lower() not in syn and v.lower() != (e["name"] or "").lower():
                syn[v.lower()] = v
        e["synonyms"] = sorted(syn.values(), key=lambda x: (x.lower(), x))[:40]
        e["n_synonyms_total"] = len(syn)
        st = r.get("molecule_structures") or {}
        h = r.get("molecule_hierarchy") or {}
        e["ids"] = {"chembl": r["molecule_chembl_id"], "inchikey": st.get("standard_inchi_key"), "unii": [], "drugbank": [], "chebi": []}
        e["ids"]["skeleton_key"] = inchikey_skeleton(st.get("standard_inchi_key"))
        e["relations"] = {"parent": ("CAT:" + h["parent_chembl_id"]) if h.get("parent_chembl_id") else None,
                          "is_parent": bool(h) and h.get("parent_chembl_id") == r["molecule_chembl_id"], "children": []}
        e["molecule_type"] = r.get("molecule_type")
        e["modality"] = classify_modality(r.get("molecule_type"), r.get("biotherapeutic"))
        e["chemistry"] = {"chirality_code_chembl": r.get("chirality"), "structure_type": r.get("structure_type"),
                          "natural_product": r.get("natural_product"), "prodrug": r.get("prodrug"), "inorganic": r.get("inorganic_flag")}
        e["atc"] = sorted(r.get("atc_classifications") or [])
        mp = r.get("max_phase")
        e["status_records"].append({
            "source": "ChEMBL", "version": chembl_v,
            "scope": "highest clinical phase curated by ChEMBL for any indication (max_phase; -1 = unknown phase); not an agency approval statement for any country",
            "max_phase": None if mp is None else float(mp), "first_approval_year": r.get("first_approval"),
            "withdrawn_flag": r.get("withdrawn_flag"), "chemical_probe": r.get("chemical_probe"), "black_box_warning_in_source": r.get("black_box_warning")})
        e["provenance"].append({"source": "ChEMBL", "version": chembl_v})
        e["source_records"].append({"source": "chembl", "id": r["molecule_chembl_id"]})
        E[cid] = e
    for e in E.values():
        p = e["relations"]["parent"]
        if p and p != e["id"] and p in E:
            E[p]["relations"]["children"].append(e["id"])
    unresolved_parents = sorted(e["id"] for e in E.values() if e["relations"]["parent"] and e["relations"]["parent"] not in E)

    # ---- UniChem cross-references (identifier keys)
    xr = {"unii": collections.defaultdict(set), "drugbank": collections.defaultdict(set), "chebi": collections.defaultdict(set)}
    rev = {"unii": collections.defaultdict(set), "drugbank": collections.defaultdict(set), "chebi": collections.defaultdict(set)}
    if avail["unichem"]:
        for key, n in (("drugbank", 2), ("chebi", 7), ("unii", 14)):
            for chembl_id, other in read_unichem(n):
                c = "CAT:" + chembl_id
                if c in E:
                    xr[key][c].add(other)
                    E[c]["ids"][key].append(other)
                rev[key][other].add(chembl_id)
        for e in E.values():
            for k in ("unii", "drugbank", "chebi"):
                e["ids"][k] = sorted(set(e["ids"][k]))

    def link(entry_ids: set[str], source: str, record_: dict) -> None:
        for c in sorted(entry_ids):
            E[c]["source_records"].append(dict(record_, source=source, multiplicity=len(entry_ids)))

    # ---- mechanisms (ChEMBL curated) -> targets with action direction and reference ids
    targets = {t["target_chembl_id"]: t for t in read_gz_jsonl(cache / "chembl/targets.jsonl.gz")}
    mech_by_mol = collections.defaultdict(list)
    for mm in read_gz_jsonl(cache / "chembl/mechanisms.jsonl.gz"):
        mech_by_mol[mm["molecule_chembl_id"]].append(mm)

    def tgt_record(mm: dict, inherited_from: str | None) -> dict:
        t = targets.get(mm.get("target_chembl_id"), {})
        genes, accs = set(), set()
        for comp in t.get("target_components") or []:
            if comp.get("accession"):
                accs.add(comp["accession"])
            for sy in comp.get("target_component_synonyms") or []:
                if sy.get("syn_type") == "GENE_SYMBOL":
                    genes.add(sy["component_synonym"])
        return {"source": "ChEMBL curated mechanism", "target_id": mm.get("target_chembl_id"), "target_name": t.get("pref_name"),
                "target_type": t.get("target_type"), "organism": t.get("organism"), "gene_symbols": sorted(genes), "uniprot": sorted(accs),
                "action_type": mm.get("action_type"), "mechanism_of_action": mm.get("mechanism_of_action"),
                "direct_interaction": mm.get("direct_interaction"), "molecular_mechanism": mm.get("molecular_mechanism"),
                "reference_ids": sorted({f"{x.get('ref_type')}:{x.get('ref_id')}" for x in mm.get("mechanism_refs") or []}),
                "inherited_from_parent": inherited_from,
                "potency": "NOT_CARRIED (ids and direction only; no activity value is copied)"}

    for cid, e in E.items():
        mid = e["ids"]["chembl"]
        for mm in mech_by_mol.get(mid, []):
            e["targets"].append(tgt_record(mm, None))
        if not e["targets"] and e["relations"]["parent"] and e["relations"]["parent"] != cid:
            pid = e["relations"]["parent"].replace("CAT:", "")
            for mm in mech_by_mol.get(pid, []):
                e["targets"].append(tgt_record(mm, pid))

    # ---- DGIdb: groups by DGIdb's own drug_name; identifier links only through chembl:ID concepts
    dg_stats = {}
    gt = load_gtopdb(cache) if avail["gtopdb"] else None
    if avail["dgidb"]:
        rows = read_tsv(cache / "dgidb/drugs.tsv")
        groups = collections.defaultdict(list)
        for r in rows:
            groups[r["drug_name"]].append(r)
        inter = collections.defaultdict(list)
        for r in read_tsv(cache / "dgidb/interactions.tsv"):
            inter[r["drug_name"]].append(r)
        dgv = sorted({r["source_db_version"] for r in rows if r["source_db_name"] == "ChEMBL"})
        linked_groups = only_groups = multi = 0
        interactions_attached = 0
        id_counts = collections.Counter()
        exact_symbol = collections.defaultdict(set)    # claim symbol -> {(concept id, symbol)} where DGIdb resolved it to the identical symbol
        for rows_ in inter.values():
            for ir in rows_:
                if ir["interaction_source_db_name"] != "GuideToPharmacology" and ir["gene_claim_name"].upper() == ir["gene_name"].upper() and ir["gene_concept_id"] != "NULL":
                    exact_symbol[ir["gene_claim_name"].upper()].add((ir["gene_concept_id"], ir["gene_name"]))
        for gname in sorted(groups):
            g = groups[gname]
            flags = collections.Counter(r["approved"] for r in g)
            appr = "TRUE" if flags.get("TRUE") and not flags.get("FALSE") else "FALSE" if flags.get("FALSE") and not flags.get("TRUE") else "MIXED" if flags.get("TRUE") else "UNKNOWN"
            chembl_ids = {"CAT:" + r["concept_id"].split(":", 1)[1].upper() for r in g if r["concept_id"].lower().startswith("chembl:")}
            chembl_ids = {c for c in chembl_ids if c in E}
            rec = {"dgidb_drug_name": gname, "claims": len(g), "approved_flag_counts": dict(flags), "claim_sources": sorted({r["source_db_name"] for r in g})}
            status_rec = {"source": "DGIdb", "version": "drugs.tsv release as served " + str(src_status["dgidb"].get("version")),
                          "scope": "claim-level approved flag aggregated over the DGIdb claims of this drug_name; the underlying source database differs per claim (see claim_sources); not a statement about one country",
                          "approved_aggregate": appr, "approved_flag_counts": dict(flags)}
            if chembl_ids:
                linked_groups += 1
                multi += len(chembl_ids) > 1
                for c in chembl_ids:
                    E[c]["status_records"].append(status_rec)
                    E[c]["provenance"].append({"source": "DGIdb", "version": src_status["dgidb"].get("version")})
                    E[c]["ids"]["dgidb_drug_name"] = gname
                link(chembl_ids, "dgidb", rec)
                owners = chembl_ids
            else:
                only_groups += 1
                cid = "CAT:DGIDB:" + hashlib.sha1(gname.encode()).hexdigest()[:12]
                e = new_entry(cid, "dgidb_only", gname.title(), "DGIdb drug_name")
                e["synonyms"] = sorted({r["drug_claim_name"] for r in g if r["drug_claim_name"].lower() != gname.lower()}, key=lambda x: (x.lower(), x))[:40]
                e["n_synonyms_total"] = len({r["drug_claim_name"] for r in g})
                e["ids"] = {"dgidb_drug_name": gname, "concept_ids": sorted({r["concept_id"] for r in g if r["concept_id"] != "NULL"})[:20],
                            "unii": [], "drugbank": [], "chebi": [], "chembl": None, "inchikey": None,
                            "chembl_from_dgidb_concept_not_enumerated": sorted({r["concept_id"].split(":", 1)[1].upper() for r in g if r["concept_id"].lower().startswith("chembl:")})}
                for r in g:
                    cc = r["concept_id"]
                    if cc.startswith("drugbank:"):
                        e["ids"]["drugbank"].append(cc.split(":", 1)[1])
                e["ids"]["drugbank"] = sorted(set(e["ids"]["drugbank"]))
                e["status_records"].append(status_rec)
                e["provenance"].append({"source": "DGIdb", "version": src_status["dgidb"].get("version")})
                e["source_records"].append(dict(rec, source="dgidb"))
                E[cid] = e
                owners = {cid}
            for ir in inter.get(gname, []):
                if ir["interaction_source_db_name"] == "GuideToPharmacology":
                    variants = identity_gtopdb(gt, ir)
                else:
                    flag = claim_symbol_anomaly(ir)
                    exact = exact_symbol.get(ir["gene_claim_name"].upper())
                    if flag and exact and len(exact) == 1:
                        (hg, sym), = exact
                        variants = [{"gene": sym, "gene_concept_id": hg, "gene_claim_name": ir["gene_claim_name"],
                                     "dgidb_served_gene": {"gene": ir["gene_name"], "gene_concept_id": ir["gene_concept_id"]},
                                     "identity": {"state": "corrected", "method": "claim_symbol_equals_an_exactly_resolved_symbol_in_the_same_export",
                                                  "note": flag + f"; the identical claim symbol resolves exactly to {sym} ({hg}) on other rows of the same export"}}]
                    else:
                        variants = [{"gene": ir["gene_name"], "gene_concept_id": ir["gene_concept_id"], "gene_claim_name": ir["gene_claim_name"],
                                     "identity": {"state": "unverified", "method": "claim_symbol_heuristic", "note": flag} if flag else
                                                 {"state": "as_served", "method": "none", "note": "claim symbol/id as DGIdb served it; no independent id check available for this source"}}]
                for v in variants:
                    id_counts[(ir["interaction_source_db_name"], v["identity"]["state"])] += 1
                    itype = v.pop("interaction_type") if "interaction_type" in v else (None if ir["interaction_type"] in ("NULL", "") else ir["interaction_type"])
                    ist = v.pop("interaction_type_state") if "interaction_type_state" in v else ("UNKNOWN" if ir["interaction_type"] in ("NULL", "") else "stated")
                    tr = dict(v, **{"source": "DGIdb interaction", "interaction_type": itype, "interaction_type_state": ist,
                                    "claim_source": ir["interaction_source_db_name"], "action_direction": "see interaction_type; DGIdb carries no potency here",
                                    "multiplicity": len(owners)})
                    for c in owners:
                        E[c]["targets"].append(tr)
                        interactions_attached += 1
        dg_stats = {"drug_names": len(groups), "claims": len(rows), "groups_linked_to_chembl_by_identifier": linked_groups,
                    "groups_linked_to_more_than_one_chembl_entry": multi, "groups_without_enumerated_chembl_entry_became_entries": only_groups,
                    "of_which_carry_a_chembl_concept_id_outside_the_enumerated_set": sum(1 for g in groups.values() if any(r["concept_id"].lower().startswith("chembl:") for r in g)) - linked_groups,
                    "interaction_rows": sum(len(v) for v in inter.values()), "interaction_rows_attached_to_entries": interactions_attached,
                    "claim_chembl_versions": dgv,
                    "target_identity_by_claim_source_and_state": {f"{a}|{b}": n for (a, b), n in sorted(id_counts.items()) if a == "GuideToPharmacology" or b != "as_served"},
                    "gtopdb_release_used_to_verify": None if gt is None else gt["release"]}

    # ---- MATRIX drug list
    mx_stats = {}
    if avail["matrix"]:
        n_linked = n_new = n_deleted = n_multi = 0
        for r in read_gz_jsonl(cache / "matrix/drug_list.jsonl.gz"):
            if r.get("deleted"):
                n_deleted += 1
                continue
            hits = set()
            if r.get("drugbank_id"):
                hits |= {"CAT:" + c for c in rev["drugbank"].get(r["drugbank_id"], ())}
            tid = r.get("translator_id") or ""
            if tid.startswith("CHEBI:"):
                hits |= {"CAT:" + c for c in rev["chebi"].get(tid.split(":", 1)[1], ())}
            hits = {h for h in hits if h in E}
            rec = {"matrix_id": r["id"], "name": r.get("name"), "drugbank_id": r.get("drugbank_id"), "translator_id": r.get("translator_id"),
                   "approved_usa": r.get("approved_usa"), "gras_usa": r.get("gras_usa"), "atc_main": r.get("atc_main"),
                   "is_cell_therapy": r.get("is_cell_therapy"), "match_rule": "identifier: drugbank_id or ChEBI id via UniChem" if hits else "none"}
            sr = {"source": "Every Cure MATRIX drug list", "version": src_status["matrix"].get("version"),
                  "scope": "approved_usa as stated by the list (US); gras_usa is a food-additive status and is NOT a supplement or OTC statement",
                  "approved_usa": r.get("approved_usa"), "gras_usa": r.get("gras_usa")}
            if hits:
                n_linked += 1
                n_multi += len(hits) > 1
                for c in hits:
                    E[c]["status_records"].append(sr)
                    E[c]["provenance"].append({"source": "Every Cure MATRIX drug list", "version": src_status["matrix"].get("version")})
                    E[c]["ids"].setdefault("matrix_id", [])
                    E[c]["ids"]["matrix_id"] = sorted(set(E[c]["ids"].get("matrix_id", [])) | {r["id"]})
                link(hits, "matrix", rec)
            else:
                n_new += 1
                cid = "CAT:" + r["id"]
                e = new_entry(cid, "matrix_only", r.get("name"), "MATRIX list name")
                e["synonyms"] = sorted(set(r.get("synonyms") or []), key=lambda x: (x.lower(), x))[:40]
                e["n_synonyms_total"] = len(set(r.get("synonyms") or []))
                e["ids"] = {"matrix_id": [r["id"]], "drugbank": [r["drugbank_id"]] if r.get("drugbank_id") else [], "chebi": [tid.split(":", 1)[1]] if tid.startswith("CHEBI:") else [],
                            "unii": [], "chembl": None, "inchikey": None, "translator_id": tid or None}
                e["modality"] = "cell_product" if r.get("is_cell_therapy") else "unknown"
                e["atc"] = [r["atc_main"]] if r.get("atc_main") else []
                e["status_records"].append(sr)
                e["provenance"].append({"source": "Every Cure MATRIX drug list", "version": src_status["matrix"].get("version")})
                e["source_records"].append(dict(rec, source="matrix"))
                E[cid] = e
        mx_stats = {"rows_not_deleted": n_linked + n_new, "rows_deleted_skipped": n_deleted, "linked_to_chembl_entries": n_linked,
                    "linked_to_more_than_one_chembl_entry": n_multi, "became_entries": n_new}

    # ---- openFDA NDC: access evidence keyed by UNII
    ndc_stats = {}
    unii_acc = {}
    if avail["openfda_ndc"]:
        d = manifest["sources"]["openfda_ndc"]["data"]
        counters = collections.defaultdict(lambda: collections.Counter())
        names = collections.defaultdict(collections.Counter)
        examples = collections.defaultdict(list)
        total = rx_otc_fin = no_unii = excluded_types = 0
        homeo_only = set()
        for f in d["files"]:
            with zipfile.ZipFile(cache / f["path"]) as z:
                res = json.load(z.open(z.namelist()[0]))["results"]
            for p in res:
                total += 1
                pt = p.get("product_type")
                if pt not in ("HUMAN PRESCRIPTION DRUG", "HUMAN OTC DRUG") or not p.get("finished"):
                    excluded_types += 1
                    continue
                rx_otc_fin += 1
                unii = (p.get("openfda") or {}).get("unii") or []
                if not unii:
                    no_unii += 1
                    continue
                single = len(p.get("active_ingredients") or []) == 1
                mc = p.get("marketing_category") or "UNSTATED"
                for u in unii:
                    counters[u][(pt, mc, "single" if single else "combination")] += 1
                    if single and p["active_ingredients"][0].get("name"):
                        names[u][p["active_ingredients"][0]["name"]] += 1
                    if len(examples[u]) < 3:
                        examples[u].append(p["product_ndc"])
        ndc_ver = d["version"]
        for u, c in counters.items():
            unii_acc[u] = {"counts": {"|".join(k): v for k, v in sorted(c.items())}, "examples": examples[u], "name": names[u].most_common(1)[0][0] if names[u] else None}
        ndc_stats = {"products_total": total, "products_not_finished_human_rx_otc_excluded": excluded_types, "finished_human_rx_otc_products": rx_otc_fin,
                     "finished_human_rx_otc_products_without_unii_cannot_be_linked": no_unii, "distinct_uniis_in_finished_rx_otc": len(unii_acc)}
        # create entries for UNIIs that no ChEMBL id carries, except homeopathic-only
        ndc_only = homeo_skipped = 0
        for u in sorted(unii_acc):
            if rev["unii"].get(u) and any(("CAT:" + c) in E for c in rev["unii"][u]):
                continue
            cats = {k.split("|")[1] for k in unii_acc[u]["counts"]}
            if cats <= {"UNAPPROVED HOMEOPATHIC"}:
                homeo_skipped += 1
                continue
            cid = "CAT:UNII:" + u
            e = new_entry(cid, "openfda_unii_only", unii_acc[u]["name"] or f"UNII {u}", "openFDA NDC single-ingredient active_ingredient name" if unii_acc[u]["name"] else "identifier only (appears only in combination products)")
            e["ids"] = {"unii": [u], "chembl": None, "inchikey": None, "drugbank": [], "chebi": []}
            e["source_records"].append({"source": "openfda_ndc", "id": u})
            e["provenance"].append({"source": "openFDA NDC", "version": ndc_ver})
            E[cid] = e
            ndc_only += 1
        ndc_stats.update({"uniis_without_chembl_entry_that_became_entries": ndc_only, "homeopathic_only_uniis_not_made_entries": homeo_skipped})
    # attach NDC to every entry that carries the UNII
    ndc_links = 0
    for cid, e in E.items():
        for u in e["ids"].get("unii") or []:
            a = unii_acc.get(u)
            if not a:
                continue
            ndc_links += 1
            for k, v in a["counts"].items():
                pt, mc, kind = k.split("|")
                e.setdefault("_ndc", []).append((u, pt, mc, kind, v))
            e["status_records"].append({"source": "openFDA NDC", "version": src_status["openfda_ndc"].get("version"),
                                        "scope": "US NDC directory listing, marketing category per product; matched by UNII (UniChem or the entry's own UNII); several products and salt forms may share one UNII",
                                        "unii": u, "marketing_category_counts": {k: v for k, v in a["counts"].items()}, "example_product_ndc": a["examples"]})
    ndc_stats["entries_with_ndc_evidence"] = sum(1 for e in E.values() if "_ndc" in e)
    ndc_stats["unii_to_entry_links"] = ndc_links

    # ---- DSLD probes (name-only evidence; read, not made)
    probes = {}
    pp = cache / "dsld/probes.jsonl"
    if avail["dsld"] and pp.exists():
        for line in pp.read_text().splitlines():
            r = json.loads(line)
            probes[norm(r["query"])] = r
    bulk_planned = len(probe_names())
    dsld_stats = {"probes_ok": sum(1 for r in probes.values() if r["status"] == "OK"), "probes_error": sum(1 for r in probes.values() if r["status"] != "OK"),
                  "probes_by_set": dict(collections.Counter(r.get("set", "bulk") for r in probes.values())),
                  "bulk_list_planned_names": bulk_planned,
                  "bulk_list_probed": sum(1 for r in probes.values() if r.get("set", "bulk") == "bulk"),
                  "bulk_list_coverage_note": "the bulk probe was interrupted; names not probed have NO supplement evidence either way (unknown, not negative)",
                  "queries_with_exact_name_in_sample": sum(1 for r in probes.values() if r["status"] == "OK" and r["exact_ingredient_in_sample"] > 0),
                  "match_strength": "name_only: DSLD labels carry no identifier; US labels only (not an Italian or EU classification)"}

    # ---- derived fields: status class, access
    for e in E.values():
        ndc = e.pop("_ndc", [])
        phases = [s["max_phase"] for s in e["status_records"] if s["source"] == "ChEMBL" and s.get("max_phase") is not None]
        chem = [s for s in e["status_records"] if s["source"] == "ChEMBL"]
        approved = any(p == 4 for p in phases) or any(s.get("approved_aggregate") in ("TRUE", "MIXED") for s in e["status_records"]) \
            or any(s.get("approved_usa") == "APPROVED" for s in e["status_records"]) \
            or any(mc in NDA_LIKE for (_, _, mc, _, _) in ndc)
        monograph = any(mc.startswith("OTC MONOGRAPH") for (_, _, mc, _, _) in ndc)
        unappr = any(mc.startswith("UNAPPROVED") and mc != "UNAPPROVED HOMEOPATHIC" for (_, _, mc, _, _) in ndc)
        if approved:
            cls = "approved_any_source"
        elif monograph:
            cls = "marketed_otc_monograph"
        elif unappr:
            cls = "marketed_unapproved_us"
        elif any(p in (0.5, 1.0, 2.0, 3.0) for p in phases):
            cls = "clinical_candidate"
        elif any(p == -1.0 for p in phases):
            cls = "phase_unknown"
        elif any(s.get("chemical_probe") for s in chem):
            cls = "tool_probe"
        else:
            cls = "no_status_statement"
        e["status_class"] = cls
        acc = []
        rx = [(u, mc, n) for (u, pt, mc, kind, n) in ndc if pt == "HUMAN PRESCRIPTION DRUG" and mc != "UNAPPROVED HOMEOPATHIC"]
        otc = [(u, mc, n) for (u, pt, mc, kind, n) in ndc if pt == "HUMAN OTC DRUG" and mc != "UNAPPROVED HOMEOPATHIC"]
        if rx:
            acc.append({"category": "prescription", "scope": f"US, openFDA NDC {src_status['openfda_ndc'].get('version')}: finished human prescription products (any marketing category) carrying this UNII", "strength": "identifier_match", "products": sum(n for _, _, n in rx)})
        if otc:
            acc.append({"category": "OTC", "scope": f"US, openFDA NDC {src_status['openfda_ndc'].get('version')}: finished human OTC products (non-homeopathic) carrying this UNII; may be a combination product", "strength": "identifier_match", "products": sum(n for _, _, n in otc)})
        probe = None
        matched_on = None
        for nm in [e["name"]] + e["synonyms"]:
            pr = probes.get(norm(nm)) if nm else None
            if pr and (nm == e["name"] or pr.get("set") == "targeted"):
                probe, matched_on = pr, nm
                if pr["status"] == "OK" and pr["exact_ingredient_in_sample"] > 0:
                    break
        if probe and probe["status"] == "OK" and probe["exact_ingredient_in_sample"] > 0:
            acc.append({"category": "supplement", "scope": "US, NIH ODS DSLD v9: a label lists an ingredient whose name equals this entry's name (normalised); DSLD has no identifiers, so this is NAME-ONLY evidence",
                        "strength": "name_only", "matched_on": matched_on, "label_ids_example": probe["example_label_ids"], "retrieved_utc": probe["retrieved_utc"]})
        if not (rx or otc) and not approved and (any(p in (0.5, 1.0, 2.0, 3.0) for p in phases) or any(s.get("chemical_probe") for s in chem)):
            acc.append({"category": "experimental", "scope": f"ChEMBL {chembl_v}: clinical-candidate or chemical-probe statement and no approval statement in any source used; says nothing about whether anyone can obtain it",
                        "strength": "source_statement"})
        if not acc:
            why = "approval stated by a source but no US NDC listing matched by identifier" if approved else "no source used states how it is obtained"
            acc.append({"category": "unknown/unverified", "scope": f"{why}; absence from the sources used is not a negative (country, product and date dependent)", "strength": "none"})
        if (rx or otc) and ndc and all(mc == "UNAPPROVED HOMEOPATHIC" for (_, _, mc, _, _) in ndc):
            pass
        e["access"] = acc
        e["access_categories"] = sorted({a["category"] for a in acc})
        e["synonyms_note"] = "capped at 40 per entry; n_synonyms_total is the real count"

    entries = [E[k] for k in sorted(E)]
    stats = compute_stats(entries, src_status, unresolved_parents, dg_stats, mx_stats, ndc_stats, dsld_stats, manifest)
    return entries, stats


def compute_stats(entries, src_status, unresolved_parents, dg, mx, ndc, dsld, manifest) -> dict:
    n = len(entries)
    by = lambda f: dict(sorted(collections.Counter(f(e) for e in entries).items(), key=lambda kv: (-kv[1], str(kv[0]))))
    cat_overlap = collections.Counter(c for e in entries for c in e["access_categories"])
    sig = by(lambda e: "+".join(e["access_categories"]))
    by_origin = by(lambda e: e["origin"])
    by_status = by(lambda e: e["status_class"])
    by_mod = by(lambda e: e["modality"])
    # stereo / salt families kept, not merged
    skel = collections.defaultdict(list)
    for e in entries:
        if e["ids"].get("skeleton_key"):
            skel[e["ids"]["skeleton_key"]].append(e["id"])
    parents = sum(1 for e in entries if e["relations"].get("is_parent"))
    children = sum(1 for e in entries if e["relations"].get("parent") and not e["relations"].get("is_parent"))
    ch = manifest["sources"].get("chembl", {}).get("data", {})
    ch_total = (ch.get("chembl_status") or {}).get("disinct_compounds")
    ch_in = sum(1 for e in entries if e["origin"].startswith("chembl"))
    usable = [e for e in entries if {"prescription", "OTC", "supplement"} & set(e["access_categories"])]
    stats = {
        "schema_version": SCHEMA, "generated_utc": now(), "unit": "one catalogue entry = one source-level substance record (ChEMBL molecule record incl. salts and stereoisomers; or one source-only substance); NOT a unique chemical entity",
        "sources": src_status,
        "entries_total": n,
        "by_origin": by_origin,
        "by_status_class": by_status,
        "by_modality": by_mod,
        "access_signature_sums_to_total": sig,
        "access_category_overlapping_counts": dict(sorted(cat_overlap.items())),
        "access_unknown_unverified_entries": cat_overlap.get("unknown/unverified", 0),
        "universe": {
            "chembl_distinct_compounds_in_release": ch_total,
            "chembl_entries_enumerated_in_catalogue": ch_in,
            "chembl_compounds_not_enumerated_bioactive_only": None if ch_total is None else ch_total - ch_in,
            "meaning": "the bioactive-molecule universe is the ChEMBL total; the catalogue enumerates only compounds with a clinical-phase statement, a probe flag, or a source row; the rest is counted here and not listed",
            "entries_with_access_evidence_prescription_or_OTC_or_supplement": len(usable),
            "meaning_of_the_previous": "evidence of access in at least one US listing on a date, scoped per entry; not approval, appropriateness or safety, and not access for a given person or country",
        },
        "relations_kept": {"chembl_parent_entries": parents, "chembl_child_entries_salts_or_forms": children,
                           "skeleton_keys_shared_by_more_than_one_entry": sum(1 for v in skel.values() if len(v) > 1),
                           "entries_in_shared_skeleton_groups": sum(len(v) for v in skel.values() if len(v) > 1),
                           "child_entries_whose_parent_is_missing_from_catalogue": len(unresolved_parents)},
        "merge_report": {
            "rule": "entries are never merged on name; evidence from another source is attached to an entry only by a declared identifier key (ChEMBL id; UniChem ChEMBL<->DrugBank/ChEBI/UNII; DGIdb chembl: concept ids; MATRIX drugbank_id/ChEBI)",
            "entries_merged_away": 0,
            "evidence_attached_by_identifier": {"dgidb_groups_linked_to_chembl": dg.get("groups_linked_to_chembl_by_identifier"), "matrix_rows_linked_to_chembl": mx.get("linked_to_chembl_entries"),
                                                "ndc_unii_to_entry_links": ndc.get("unii_to_entry_links")},
            "one_to_many_links_note": "a DGIdb drug group, a MATRIX row or a UNII that matches several salt/stereoisomer entries is attached to each of them and flagged multiplicity>1; it is not collapsed",
            "possible_cross_source_duplicates": "source-only entries (DGIdb, MATRIX, openFDA) that no identifier connects to a ChEMBL entry may describe the same substance as a ChEMBL entry; the entry count is an upper bound for distinct substances",
        },
        "dgidb": dg, "matrix": mx, "openfda_ndc": ndc, "dsld": dsld,
        "entries_with_targets": sum(1 for e in entries if e["targets"]),
        "entries_with_chembl_curated_mechanism": sum(1 for e in entries if any(t["source"] == "ChEMBL curated mechanism" for t in e["targets"])),
        "not_obtained": [
            "dietary-supplement status for any compound that was not probed in DSLD, and for all probed ones except by normalised-name match (DSLD labels carry no identifiers)",
            "non-US access (EMA, MHRA, PMDA, national lists): no open bulk source was found",
            "US NDC products without a UNII (cannot be linked by identifier)",
            "DGIdb newer than the 2024-06-10 TSV release",
        ],
    }
    stats["unresolved_parent_ids"] = unresolved_parents[:50]
    stats["units"] = units_block(entries, ch_total)
    stats["source_verification"] = verify_sources(manifest)
    stats["dgidb_age"] = dgidb_age(manifest, src_status)
    return stats


def units_block(entries: list[dict], ch_total) -> dict:
    """What the counts count.  Records, families, duplicates, pharmacology and WWOX evaluation are different units."""
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    chem = [e for e in entries if e["origin"].startswith("chembl")]
    first = {}
    for e in chem:
        find(e["id"])
        if e["relations"].get("parent") and e["relations"]["parent"] != e["id"]:
            union(e["id"], e["relations"]["parent"])
        sk = e["ids"].get("skeleton_key")
        if sk:
            if sk in first:
                union(e["id"], first[sk])
            else:
                first[sk] = e["id"]
    fam = collections.Counter(find(e["id"]) for e in chem)
    names = collections.defaultdict(set)
    for e in chem:
        for nm in [e["name"]] + e["synonyms"]:
            if nm:
                names[norm(nm)].add(e["id"])
    src_only = [e for e in entries if not e["origin"].startswith("chembl")]
    coincide = [e for e in src_only if e["name"] and norm(e["name"]) in names]
    genes, tids = set(), set()
    for e in entries:
        for t in e["targets"]:
            if t.get("gene"):
                genes.add(t["gene"])
            genes.update(t.get("gene_symbols") or [])
            if t.get("target_id"):
                tids.add(t["target_id"])
    return {
        "records_enumerated": len(entries),
        "records_are": "source-level substance records (a salt, a stereoisomer, a formulation record and a source-only row each count once); NOT distinct drugs and NOT distinct chemical entities",
        "external_declared_total_chembl_distinct_compounds": ch_total,
        "external_total_vs_acquired": "the ChEMBL figure is the database's own declared total; it is not the number of records acquired, and the two are never added",
        "chembl_records_acquired": len(chem),
        "chemical_families_reconciled": {
            "rule": "ChEMBL records joined by parent/child hierarchy or by identical InChIKey first block (connectivity layer); reconciliation shown, nothing merged",
            "families": len(fam), "records_in_families_of_size_gt_1": sum(v for v in fam.values() if v > 1),
            "families_of_size_gt_1": sum(1 for v in fam.values() if v > 1), "largest_family": max(fam.values()) if fam else 0,
            "not_demonstrable_for": "source-only records (no structure, no identifier tying them to a ChEMBL record); they are listed under possible_duplicates"},
        "possible_duplicates_and_unresolved_identities": {
            "source_only_records_without_identifier_link_to_chembl": len(src_only),
            "of_which_normalised_name_equals_a_chembl_name_or_synonym_NOT_MERGED": len(coincide),
            "meaning": "the name coincidence is a flag for human review; identity is unresolved until an identifier says so",
            "chembl_child_records_with_missing_parent": len([e for e in chem if e["relations"].get("parent") and e["relations"]["parent"] not in {x["id"] for x in chem}])},
        "modalities": dict(collections.Counter(e["modality"] for e in entries).most_common()),
        "modality_unknown_meaning": "source-only rows carry no molecule type; unknown is not small molecule",
        "pharmacological_data": {
            "records_with_chembl_curated_mechanism": sum(1 for e in entries if any(t["source"] == "ChEMBL curated mechanism" for t in e["targets"])),
            "records_with_dgidb_interaction": sum(1 for e in entries if any(t["source"] == "DGIdb interaction" for t in e["targets"])),
            "records_with_any_target_link": sum(1 for e in entries if e["targets"]),
            "distinct_target_ids_chembl": len(tids), "distinct_gene_symbols": len(genes),
            "meaning": "a target link is a source statement with action type and reference ids; it is not potency and not relevance to WWOX"},
        "compounds_evaluated_against_WWOX_needs": 0,
        "evaluated_meaning": "0 until the WWOX needs matrix exists; no record in this catalogue has been scored or ranked for the disease",
    }


def verify_sources(manifest: dict) -> dict:
    out = {}
    for s, e in sorted(manifest["sources"].items()):
        d = e.get("data")
        if not d:
            out[s] = {"complete": False, "last_attempt": e.get("last_attempt")}
            continue
        checks, ok = [], True
        for f in d.get("files", []):
            p = CACHE / f["path"]
            if not p.exists():
                checks.append(f"{f['path']}: MISSING in cache")
                ok = False
            elif f.get("sha256") and sha256_file(p) != f["sha256"]:
                checks.append(f"{f['path']}: sha256 differs from manifest")
                ok = False
        for k, c in (d.get("counts") or {}).items():
            if c.get("expected") != c.get("received"):
                checks.append(f"count {k}: expected {c.get('expected')} received {c.get('received')}")
                ok = False
        if "declared_records" in d and d.get("parsed_records") != d["declared_records"]:
            checks.append("NDC parsed != declared")
            ok = False
        if "declared_rows" in d:
            n = sum(f.get("rows", 0) for f in d["files"])
            if n != d["declared_rows"]:
                checks.append(f"rows {n} != declared {d['declared_rows']}")
                ok = False
        out[s] = {"complete_and_coherent": ok, "version": d.get("version"), "retrieved_utc": d.get("retrieved_utc"),
                  "counts_checked": {k: [c["expected"], c["received"]] for k, c in (d.get("counts") or {}).items()},
                  "files_hash_checked": sum(1 for f in d.get("files", []) if f.get("sha256")), "problems": checks,
                  "last_attempt_status": e.get("last_attempt", {}).get("status")}
    return out


def dgidb_age(manifest: dict, src_status: dict) -> dict:
    d = manifest["sources"].get("dgidb", {}).get("data")
    if not d:
        return {"state": "NOT_AVAILABLE"}
    lm = re.search(r"Last-Modified ([^;]+)", d.get("version", ""))
    chembl_date = (manifest["sources"].get("chembl", {}).get("data", {}).get("version") or "").split(" ")[-1]
    out = {"export_in_use": {"file": "drugs.tsv/interactions.tsv served at /data/latest", "last_modified": lm.group(1) if lm else None,
                             "its_ChEMBL_claims_version": "33"},
           "chembl_in_use": manifest["sources"].get("chembl", {}).get("data", {}).get("version"),
           "reading": "the TSV export is an OLD export (June 2024, claims from ChEMBL 33) next to ChEMBL_37 (2026-05-01); it is not the current service",
           "current_service_coverage": "not ingested: the live GraphQL API reports newer source versions (listed below when fetched), but its drug/interaction rows were not downloaded"}
    lp = CACHE / "dgidb/live_sources.json"
    if lp.exists():
        live = json.loads(lp.read_text())
        rows = read_tsv(CACHE / "dgidb/drugs.tsv")
        tsv_v = {}
        for r in rows:
            tsv_v[r["source_db_name"]] = r["source_db_version"]
        cmp_ = [{"source": n["sourceDbName"], "export_version": tsv_v.get(n["sourceDbName"]), "live_service_version": n["sourceDbVersion"]}
                for n in live["nodes"] if tsv_v.get(n["sourceDbName"]) not in (None, n["sourceDbVersion"])]
        out["live_service_checked_utc"] = live["retrieved_utc"]
        out["sources_where_live_service_differs_from_export"] = len(cmp_)
        out["examples"] = cmp_[:8]
    else:
        out["live_service_checked_utc"] = None
    return out


# ----------------------------------------------------------------------------- cards
ID_RE = re.compile(r"\bCHEMBL\d+\b")
DB_RE = re.compile(r"\bDB\d{5}\b")


def card_files() -> list[Path]:
    fs = sorted((MODULE / "cards").glob("*.json")) + sorted((MODULE / "cards_early").glob("*.json")) + [MODULE / "join/cards.json"]
    return [f for f in fs if f.exists()]


def card_key(path: Path, js) -> list[tuple[str, str]]:
    """(card id, text) pairs: one per card file, or one per derived card in join/cards.json."""
    if path.name == "cards.json":
        return [(c.get("query_id", f"join[{i}]"), json.dumps(c, ensure_ascii=False)) for i, c in enumerate(js)]
    stem = path.name.split(".")[0]
    return [(stem, json.dumps(js, ensure_ascii=False))]


def cmd_cards(entries: list[dict]) -> dict:
    by_chembl = {e["ids"]["chembl"]: e["id"] for e in entries if e["ids"].get("chembl")}
    by_db = collections.defaultdict(list)
    for e in entries:
        for d in e["ids"].get("drugbank") or []:
            by_db[d].append(e["id"])
    mentions = collections.defaultdict(lambda: {"chembl": set(), "drugbank": set(), "files": set()})
    for f in card_files():
        for cid, text in card_key(f, json.loads(f.read_text())):
            mentions[cid]["chembl"] |= set(ID_RE.findall(text))
            mentions[cid]["drugbank"] |= set(DB_RE.findall(text))
            mentions[cid]["files"].add(str(f.relative_to(MODULE)))
    lkp = CACHE / "chembl/id_lookup.json"
    lk = json.loads(lkp.read_text()) if lkp.exists() else {}  # offline: written by `fetch`; an id absent here stays UNRESOLVED, not "not a compound"
    decls = {}
    if DECLARATIONS.exists():
        for r in read_tsv(DECLARATIONS):
            decls.setdefault(r["card_id"], []).append(r)
    out, matched, unmatched = {}, 0, []
    for cid in sorted(set(mentions) | set(decls)):
        mm = mentions.get(cid, {"chembl": set(), "drugbank": set(), "files": set()})
        links = []
        for i in sorted(mm["chembl"]):
            t = (lk.get(i) or {}).get("entity_type")
            if t == "COMPOUND" and i in by_chembl:
                links.append({"catalogue_id": by_chembl[i], "rule": "chembl_id_mentioned_in_card_text; entity_type COMPOUND per ChEMBL id lookup; a mention, not an identity declaration"})
            elif t is None:
                links.append({"catalogue_id": None, "rule": "id type UNRESOLVED (no lookup in cache; run fetch); not used", "chembl_id": i})
            elif t == "COMPOUND":
                links.append({"catalogue_id": None, "rule": "compound id mentioned but not in catalogue (max_phase 0 or no phase statement)", "chembl_id": i})
        for d in sorted(mm["drugbank"]):
            for c in by_db.get(d, []):
                links.append({"catalogue_id": c, "rule": "drugbank_id_mentioned_in_card_text via UniChem"})
        for r in decls.get(cid, []):
            c = by_chembl.get(r["chembl_id"])
            links.append({"catalogue_id": c, "rule": "curator_declared_identifier (card_identity_declarations.tsv); " + r["basis"], "chembl_id": r["chembl_id"], "role": r["role"]})
        ok = [l for l in links if l["catalogue_id"]]
        entry = {"links": ok, "card_files": sorted(mm["files"]),
                 "non_compound_ids_ignored": sorted(i for i in mm["chembl"] if (lk.get(i) or {}).get("entity_type") not in ("COMPOUND",)),
                 "compound_ids_outside_catalogue": sorted({l["chembl_id"] for l in links if not l["catalogue_id"] and l.get("chembl_id")})}
        if ok:
            matched += 1
        else:
            entry["unmatched_reason"] = "no compound identifier in the card text and no curator declaration; name similarity is not used"
            unmatched.append(cid)
        out[cid] = entry
    return {"generated_utc": now(), "cards_considered": len(out), "cards_with_at_least_one_link": matched, "unmatched_cards": unmatched, "cards": out}


# ----------------------------------------------------------------------------- modalities
def write_modalities() -> int:
    rows = [("card_id", "modality", "why_not_a_molecule_entry", "source")]
    spec = {"C01_aav9_wwox": ("gene_replacement_vector", "viral-vector gene therapy"),
            "C04_aav9_endpoint_families": ("gene_replacement_vector", "viral-vector gene therapy"),
            "C03_crispra_boost": ("gene_regulation_editing_system", "CRISPR-based system, delivery-dependent"),
            "C02_splice_aso": ("oligonucleotide_therapy_or_editing", "sequence-specific oligonucleotide or editing; a molecule class but no single compound"),
            "EB-KD-01": ("dietary_intervention", "diet, composition and course not a compound"),
            "E04_ketogenic_lactate_axis": ("dietary_intervention_plus_transport_blockade", "contains a diet; the MCT1 blockade control is a separate compound class")}
    for k, (m, why) in spec.items():
        rows.append((k, m, why, "card names (cards/*.packet.json candidate.name), curator classification of this task"))
    with open(OUT_MODALITIES, "w") as fh:
        for r in rows:
            fh.write("\t".join(r) + "\n")
    return len(rows) - 1


# ----------------------------------------------------------------------------- outputs, verify, query
def write_outputs(entries, stats, links) -> None:
    write_gz_jsonl(OUT_CATALOG, entries)
    stats["catalog_file"] = {"path": "catalog.jsonl.gz", "sha256": sha256_file(OUT_CATALOG), "bytes": OUT_CATALOG.stat().st_size}
    stats["card_links"] = {k: links[k] for k in ("cards_considered", "cards_with_at_least_one_link")} | {"unmatched": len(links["unmatched_cards"])}
    stats["non_molecule_modalities_listed_separately"] = write_modalities()
    OUT_STATS.write_text(json.dumps(stats, indent=1, ensure_ascii=False) + "\n")
    OUT_LINKS.write_text(json.dumps(links, indent=1, ensure_ascii=False, sort_keys=True) + "\n")


def reconcile(entries: list[dict], stats: dict) -> list[str]:
    bad = []
    n = len(entries)
    for k in ("by_origin", "by_status_class", "by_modality", "access_signature_sums_to_total"):
        if sum(stats[k].values()) != n:
            bad.append(f"{k} sums to {sum(stats[k].values())} != {n}")
    if stats["entries_total"] != n:
        bad.append("entries_total mismatch")
    if len({e["id"] for e in entries}) != n:
        bad.append("duplicate catalogue ids")
    return bad


def cmd_build(args) -> int:
    entries, stats = build_catalog()
    links = cmd_cards(entries)
    bad = reconcile(entries, stats)
    write_outputs(entries, stats, links)
    print(json.dumps({k: stats[k] for k in ("entries_total", "by_origin", "by_status_class", "access_signature_sums_to_total")}, indent=1))
    if bad:
        print("RECONCILIATION FAILED:", bad, file=sys.stderr)
        return 2
    return 0


def cmd_verify(_a) -> int:
    entries = list(read_gz_jsonl(OUT_CATALOG))
    stats = json.loads(OUT_STATS.read_text())
    bad = reconcile(entries, stats)
    print("OK: counts reconcile" if not bad else "FAILED: " + "; ".join(bad))
    return 1 if bad else 0


def cmd_query(a) -> int:
    """Delegates to the generic engine module (framework/scripts/compound_catalog.py); read-only, offline."""
    sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
    import compound_catalog as cc  # noqa: PLC0415
    hits = cc.find(cc.load(OUT_CATALOG), a.id, a.name, a.target, a.access, a.status)
    print(f"{len(hits)} match(es)", file=sys.stderr)
    for e in hits[: a.limit]:
        print(json.dumps(e, ensure_ascii=False, indent=1) if a.full else cc._row(e))
    return 0 if hits else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    f = sub.add_parser("fetch")
    f.add_argument("--refresh", action="store_true")
    f.add_argument("--only")
    p = sub.add_parser("probe-dsld")
    p.add_argument("--names", help="comma-separated names (targeted probe); default = the bulk list (phase-4 ChEMBL names + MATRIX names)")
    p.add_argument("--limit", type=int)
    p.add_argument("--refresh", action="store_true")
    p.add_argument("--retry-errors", action="store_true", help="re-query only the names whose latest probe errored")
    sub.add_parser("build")
    al = sub.add_parser("all")
    al.add_argument("--refresh", action="store_true")
    sub.add_parser("verify")
    q = sub.add_parser("query")
    for k in ("id", "name", "target", "access", "status"):
        q.add_argument("--" + k)
    q.add_argument("--limit", type=int, default=20)
    q.add_argument("--full", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "fetch":
        return cmd_fetch(a)
    if a.cmd == "probe-dsld":
        return cmd_probe(a)
    if a.cmd == "build":
        return cmd_build(a)
    if a.cmd == "all":
        a.only = None
        cmd_fetch(a)
        return cmd_build(a)
    if a.cmd == "verify":
        return cmd_verify(a)
    if a.cmd == "query":
        return cmd_query(a)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
