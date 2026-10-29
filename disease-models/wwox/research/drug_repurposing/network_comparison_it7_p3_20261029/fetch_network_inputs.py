#!/usr/bin/env python3
"""Re-derive the two external network edge tables of IT7 P3 from the public OmniPath web service (stdlib only; no key, no registration).

Usage: fetch_network_inputs.py run --out DIR      downloads the raw exports and the OmniPath resource/licence list into DIR, filters, writes
                                                    DIR/signor_omnipath_edges.tsv.gz, DIR/collectri_omnipath_edges.tsv.gz, DIR/fetch_log.json (urls, hashes, counts)
       fetch_network_inputs.py --help             this text; no network access, no work

Queries (exact, human, as used on 2026-10-29):
  A  https://omnipathdb.org/interactions?resources=SIGNOR&datasets=omnipath,pathwayextra,kinaseextra,tf_target&genesymbols=1&fields=sources,type,references&organisms=9606&format=tsv&license=commercial
  B  https://omnipathdb.org/interactions?datasets=collectri&genesymbols=1&fields=sources,type,references&organisms=9606&format=tsv&license=commercial
  C  https://omnipathdb.org/resources?format=json            (licence of every resource)
Filter: a row is kept only if EVERY resource in its `sources` column has OmniPath licence purpose 'commercial'; for B (CollecTRI) named composites (purpose 'composite':
CollecTRI, CollecTRI2, DoRothEA) are also accepted; for A the row must also list SIGNOR and composites are NOT accepted (as in the committed table). Edge sign: consensus_stimulation XOR consensus_inhibition (ambiguous rows dropped). Output columns: source_symbol, target_symbol, sign, type, sources.
The service is live: the exports change over time, so a re-run on another date differs from the committed tables (see README, section 7a for the measured difference).
The committed tables inputs/*.tsv.gz are the ones used for every reported number."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help") or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, hashlib, io, json, os, urllib.request
out = sys.argv[sys.argv.index("--out") + 1]; os.makedirs(out, exist_ok=True)
BASE = "https://omnipathdb.org/"
Q = {"A": BASE + "interactions?resources=SIGNOR&datasets=omnipath,pathwayextra,kinaseextra,tf_target&genesymbols=1&fields=sources,type,references&organisms=9606&format=tsv&license=commercial",
     "B": BASE + "interactions?datasets=collectri&genesymbols=1&fields=sources,type,references&organisms=9606&format=tsv&license=commercial",
     "C": BASE + "resources?format=json"}
log = {"queries": Q, "files": {}}
raw = {}
for k, u in Q.items():
    data = urllib.request.urlopen(u, timeout=300).read(); raw[k] = data
    open(os.path.join(out, f"omnipath_{k}.raw"), "wb").write(data); log["files"][k] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
res = json.loads(raw["C"]); ok = {n for n, v in res.items() if v["license"]["purpose"] == "commercial"}; okc = ok | {n for n, v in res.items() if v["license"]["purpose"] == "composite"}
def sign(r):
    s, i = r["consensus_stimulation"] == "True", r["consensus_inhibition"] == "True"
    return 1 if s and not i else -1 if i and not s else 0
for key, name, need in (("A", "signor", "SIGNOR"), ("B", "collectri", None)):
    rows = list(csv.DictReader(io.StringIO(raw[key].decode()), delimiter="\t")); n = kept = 0
    with gzip.open(os.path.join(out, f"{name}_omnipath_edges.tsv.gz"), "wt", compresslevel=9) as o:
        o.write("source_symbol\ttarget_symbol\tsign\ttype\tsources\n")
        for r in rows:
            srcs = r["sources"].split(";")
            if not all(s in (ok if need else okc) for s in srcs) or (need and need not in srcs): continue
            kept += 1; sg = sign(r)
            if sg == 0: continue
            n += 1; o.write(f"{r['source_genesymbol']}\t{r['target_genesymbol']}\t{sg}\t{r['type']}\t{r['sources']}\n")
    log["files"][name] = {"rows_raw": len(rows), "rows_licence_ok": kept, "signed_edges_written": n}
json.dump(log, open(os.path.join(out, "fetch_log.json"), "w"), indent=1); print(json.dumps(log["files"], indent=1))
