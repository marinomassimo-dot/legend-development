#!/usr/bin/env python3
"""Reproduce the WWOX-neighbourhood extract of the Every Cure knowledge graph (EC-KG).

Source: Zenodo record 10.5281/zenodo.20815442 (EC-KG v0.15.19, CC BY 4.0 for the
integration layer, upstream licences continue to apply). Key-less, zero spend.

The edge file is one 1.23 GB parquet with no column statistics, and Zenodo answers
more than 133 requests per minute with HTTP 429.  So the script reads it row group by
row group with a throttled HTTP Range reader, and never stores the raw file.

Stages (run in order; every stage is restartable and writes under --work):
  nodes    slim node table (id, name, category, upstream, equivalent ids)  [DuckDB range reads]
  so       slim edge table: subject, object, row-group, row-in-group        [~0.5 GB streamed]
  select   compound match, WWOX 1-hop / 2-hop sets, target row list         [local]
  fetch    full rows for the target rows, hit row groups only               [<= 1.23 GB streamed]
  build    extract_ecKG_wwox.tsv, novelty tables, digest                    [local]

Usage:  PYTHONPATH=<dir with duckdb+pyarrow> python3 reproduce_ecKG_wwox.py all \
            --work <scratch dir> --repo <repo drug_repurposing dir> --out <output dir>
No e-mail address, account or token is sent anywhere.
"""
import argparse, csv, gzip, io, json, os, re, sys, time, urllib.request, urllib.error
from collections import defaultdict, Counter

REC = "https://zenodo.org/api/records/20815442/files/%s/content"
EDGES, NODES = REC % "kg-edges.parquet", REC % "kg-nodes.parquet"
WWOX = "NCBIGene:51741"            # EC-KG node for WWOX (HGNC:12799 is in its equivalent ids)
WWOX_HGNC = "HGNC:12799"
CHEM_CATS = {"biolink:SmallMolecule", "biolink:Drug", "biolink:ChemicalEntity",
             "biolink:MolecularMixture", "biolink:MolecularEntity", "biolink:Polypeptide"}
NEIGH_CATS = CHEM_CATS | {"biolink:Gene", "biolink:Protein", "biolink:Disease",
                          "biolink:PhenotypicFeature", "biolink:DiseaseOrPhenotypicFeature",
                          "biolink:Cell", "biolink:CellularComponent_NOT"}
GENE_CATS = {"biolink:Gene", "biolink:Protein"}
DIS_CATS = {"biolink:Disease", "biolink:PhenotypicFeature", "biolink:DiseaseOrPhenotypicFeature"}
MIN_INTERVAL = 0.55                 # seconds between requests: ~109/min < 133/min limit


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


class Throttled:
    last = 0.0

    @classmethod
    def get(cls, url, start, end, tries=8):
        for k in range(tries):
            dt = time.time() - cls.last
            if dt < MIN_INTERVAL:
                time.sleep(MIN_INTERVAL - dt)
            cls.last = time.time()
            req = urllib.request.Request(url, headers={"Range": "bytes=%d-%d" % (start, end)})
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    return r.read()
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(20 * (k + 1)); continue
                raise
            except Exception:
                time.sleep(5 * (k + 1))
        raise RuntimeError("range fetch failed %s %d-%d" % (url, start, end))


class SparseFile(io.RawIOBase):
    """Seekable file view that only holds pre-fetched byte ranges."""
    def __init__(self, size, footer_start, footer):
        self.size, self.pos, self.parts = size, 0, [(footer_start, footer)]
    def add(self, start, data): self.parts.append((start, data))
    def clear(self): self.parts = self.parts[:1]
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.pos
    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else (self.pos + off if whence == 1 else self.size + off)
        return self.pos
    def readinto(self, b):
        n = len(b)
        for s, d in self.parts:
            if s <= self.pos and self.pos + n <= s + len(d):
                b[:n] = d[self.pos - s:self.pos - s + n]; self.pos += n; return n
        raise IOError("range %d+%d not prefetched" % (self.pos, n))


def open_remote(url):
    import pyarrow.parquet as pq
    head = Throttled.get(url, 0, 0)
    req = urllib.request.Request(url, headers={"Range": "bytes=0-0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        size = int(r.headers["Content-Range"].split("/")[1])
    tail = Throttled.get(url, size - 4_000_000, size - 1)
    sf = SparseFile(size, size - 4_000_000, tail)
    pf = pq.ParquetFile(sf)
    return pf, sf


def chunk_range(md_col):
    s = md_col.dictionary_page_offset if md_col.has_dictionary_page and md_col.dictionary_page_offset else md_col.data_page_offset
    return s, s + md_col.total_compressed_size - 1


def stage_nodes(a):
    import duckdb
    out = os.path.join(a.work, "nodes_slim.parquet")
    if os.path.exists(out): return
    con = duckdb.connect(); con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute("COPY (SELECT id,name,category,upstream_data_source,equivalent_identifiers "
                "FROM read_parquet('%s')) TO '%s' (FORMAT parquet, COMPRESSION zstd)" % (NODES, out))


def stage_so(a):
    import pyarrow as pa, pyarrow.parquet as pq
    out = os.path.join(a.work, "edges_so.parquet")
    if os.path.exists(out): return
    pf, sf = open_remote(EDGES)
    names = [pf.schema_arrow.field(i).name for i in range(len(pf.schema_arrow))]
    ci = {n: i for i, n in enumerate(names)}
    writer = None
    for rg in range(pf.num_row_groups):
        md = pf.metadata.row_group(rg)
        sf.clear()
        for c in ("subject", "object"):
            s, e = chunk_range(md.column(ci[c])); sf.add(s, Throttled.get(EDGES, s, e))
        t = pf.read_row_group(rg, columns=["subject", "object"])
        t = t.append_column("rg", pa.array([rg] * t.num_rows, pa.int16()))
        t = t.append_column("ri", pa.array(range(t.num_rows), pa.int32()))
        if writer is None: writer = pq.ParquetWriter(out + ".part", t.schema, compression="zstd")
        writer.write_table(t)
        if rg % 50 == 0: print("so rg", rg, flush=True)
    writer.close(); os.replace(out + ".part", out)


def legend_compounds(repo):
    p = os.path.join(repo, "generation_it22_p1_20261103/results_p4/proposals_it21.tsv")
    rows = list(csv.DictReader(open(p), delimiter="\t"))
    fam_name = {}
    with gzip.open(os.path.join(repo, "generation_it21_p2_20261103/results/actions/family_meta.tsv.gz"), "rt") as f:
        for r in csv.DictReader(f, delimiter="\t"): fam_name[r["family_id"]] = r["name"]
    comps = {}
    for r in rows:
        comps.setdefault(r["family_id"], set()).add(r["base_name"])
    return rows, comps, fam_name


def stage_select(a):
    import duckdb
    con = duckdb.connect()
    nodes = os.path.join(a.work, "nodes_slim.parquet"); so = os.path.join(a.work, "edges_so.parquet")
    rows, comps, fam_name = legend_compounds(a.repo)
    base_names = {norm(b) for s in comps.values() for b in s} | {norm(fam_name.get(f, "")) for f in comps}
    base_names.discard("")
    chembl = {"CHEMBL.COMPOUND:" + f.split(":")[-1]: f for f in comps if f.startswith("FAM:CAT:CHEMBL")}
    con.execute("CREATE TABLE bn(n VARCHAR)")
    con.executemany("INSERT INTO bn VALUES (?)", [(x,) for x in base_names])
    con.execute("CREATE TABLE cb(c VARCHAR)")
    con.executemany("INSERT INTO cb VALUES (?)", [(x,) for x in chembl])
    cats = ",".join("'%s'" % c for c in CHEM_CATS)
    cbl = "[" + ",".join("'%s'" % c for c in chembl) + "]::VARCHAR[]"
    con.execute(f"""CREATE TABLE comp AS
        SELECT DISTINCT n.id, n.name, n.category, n.upstream_data_source,
          (regexp_replace(lower(n.name),'[^a-z0-9]','','g') IN (SELECT n FROM bn)) AS by_name,
          list_has_any(n.equivalent_identifiers, {cbl}) AS by_chembl
        FROM '{nodes}' n WHERE n.category IN ({cats})
          AND (regexp_replace(lower(n.name),'[^a-z0-9]','','g') IN (SELECT n FROM bn)
               OR list_has_any(n.equivalent_identifiers, {cbl}))""")
    con.execute(f"COPY comp TO '{a.work}/matched_compounds.tsv' (DELIMITER '\t', HEADER)")
    con.execute(f"CREATE VIEW so AS SELECT * FROM '{so}'")
    con.execute(f"CREATE VIEW nd AS SELECT id,name,category FROM '{nodes}'")
    allowed = ",".join("'%s'" % c for c in NEIGH_CATS)
    con.execute(f"""CREATE TABLE n1 AS SELECT DISTINCT x.o AS id FROM
        (SELECT CASE WHEN subject='{WWOX}' THEN object ELSE subject END AS o FROM so
         WHERE subject='{WWOX}' OR object='{WWOX}') x JOIN nd ON nd.id=x.o
        WHERE nd.category IN ({allowed}) AND x.o<>'{WWOX}'""")
    con.execute(f"""CREATE TABLE n2 AS SELECT DISTINCT x.o AS id FROM
        (SELECT CASE WHEN s.subject IN (SELECT id FROM n1) THEN s.object ELSE s.subject END AS o
         FROM so s WHERE s.subject IN (SELECT id FROM n1) OR s.object IN (SELECT id FROM n1)) x
        JOIN nd ON nd.id=x.o WHERE nd.category IN ({allowed})
          AND x.o NOT IN (SELECT id FROM n1) AND x.o<>'{WWOX}'""")
    print("matched compound nodes", con.execute("SELECT count(*) FROM comp").fetchone(),
          "N1", con.execute("SELECT count(*) FROM n1").fetchone(),
          "N2", con.execute("SELECT count(*) FROM n2").fetchone())
    # target rows: (a) every edge incident to WWOX, (b) every edge incident to a matched compound
    # (c) tagging which of (b) fall inside the WWOX 1-/2-hop neighbourhood is done in `build`.
    con.execute(f"""CREATE TABLE tgt AS SELECT rg,ri,subject,object,
        CASE WHEN subject='{WWOX}' OR object='{WWOX}' THEN 'W' ELSE 'C' END AS why
        FROM so WHERE subject='{WWOX}' OR object='{WWOX}'
           OR subject IN (SELECT id FROM comp) OR object IN (SELECT id FROM comp)""")
    con.execute(f"COPY tgt TO '{a.work}/target_rows.parquet' (FORMAT parquet)")
    con.execute(f"COPY n1 TO '{a.work}/n1.parquet' (FORMAT parquet)")
    con.execute(f"COPY n2 TO '{a.work}/n2.parquet' (FORMAT parquet)")
    print("target rows", con.execute("SELECT why,count(*),count(DISTINCT rg) FROM tgt GROUP BY why").fetchall())


def stage_fetch(a):
    import duckdb, pyarrow as pa, pyarrow.parquet as pq
    out = os.path.join(a.work, "edges_full_target.parquet")
    if os.path.exists(out): return
    con = duckdb.connect()
    hits = con.execute(f"SELECT rg, list(ri ORDER BY ri) FROM '{a.work}/target_rows.parquet' GROUP BY rg ORDER BY rg").fetchall()
    pf, sf = open_remote(EDGES)
    writer = None
    for k, (rg, ris) in enumerate(hits):
        md = pf.metadata.row_group(rg)
        s = min(chunk_range(md.column(i))[0] for i in range(md.num_columns))
        e = max(chunk_range(md.column(i))[1] for i in range(md.num_columns))
        sf.clear(); sf.add(s, Throttled.get(EDGES, s, e))
        t = pf.read_row_group(rg).take(pa.array(ris, pa.int32()))
        t = t.append_column("rg", pa.array([rg] * t.num_rows, pa.int16()))
        t = t.append_column("ri", pa.array(ris, pa.int32()))
        if writer is None: writer = pq.ParquetWriter(out + ".part", t.schema, compression="zstd")
        writer.write_table(t)
        if k % 50 == 0: print("fetch", k, "/", len(hits), flush=True)
    writer.close(); os.replace(out + ".part", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["nodes", "so", "select", "fetch", "build", "all"])
    ap.add_argument("--work", required=True); ap.add_argument("--repo", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.work, exist_ok=True); os.makedirs(a.out, exist_ok=True)
    st = ["nodes", "so", "select", "fetch", "build"] if a.stage == "all" else [a.stage]
    for s in st:
        if s == "build":
            import importlib.util
            sp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_ecKG_tables.py")
            spec = importlib.util.spec_from_file_location("build", sp); m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m); m.run(a)
        else:
            globals()["stage_" + s](a)
