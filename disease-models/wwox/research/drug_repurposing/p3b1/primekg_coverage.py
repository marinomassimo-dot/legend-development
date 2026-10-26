#!/usr/bin/env python3
"""Entity coverage of PrimeKG (the knowledge graph TxGNN is trained on) for NAMED genes and disease nodes.

Standard library only. Streams PrimeKG `kg.csv` (about 1 GB) once, keeps only the rows that touch the requested nodes,
and never stores the file. The md5 of the stream is compared with the md5 Harvard Dataverse publishes, so a truncated or
changed file is reported rather than silently used. Nothing here trains, scores or ranks anything: it answers "is this
entity a node, what is it merged into, and which relation types touch it".

Usage: primekg_coverage.py <outfile.json> --genes WWOX PDK1 ... --diseases "developmental and epileptic encephalopathy" ...
Disease names are the PrimeKG node names AFTER its disease grouping (a grouped node holds many MONDO ids joined by `_`).
Data: PrimeKG, Harvard Dataverse doi:10.7910/DVN/IXA7BM version 2.1, CC0 1.0 as declared on the dataset record
(upstream sources of PrimeKG keep their own terms).
"""
import argparse
import collections
import csv
import hashlib
import io
import json
import urllib.request

DV = "https://dataverse.harvard.edu/api/access/datafile/"
NODES, KG = DV + "6180617", DV + "6180620"          # nodes.tab, kg.csv of version 2.1
KG_MD5 = "aac8191d4fbc5bf09cdf8c3c78b4e75f"         # md5 published on the Dataverse record for kg.csv


def opener(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "legend-repurposing"}), timeout=180)


class Hashing(io.RawIOBase):
    def __init__(self, resp):
        self.r, self.md5 = resp, hashlib.md5()

    def readable(self):
        return True

    def readinto(self, b):
        d = self.r.read(len(b))
        self.md5.update(d)
        b[:len(d)] = d
        return len(d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--genes", nargs="*", default=[])
    ap.add_argument("--diseases", nargs="*", default=[])
    a = ap.parse_args()
    nodes = list(csv.reader(io.TextIOWrapper(opener(NODES), encoding="utf-8"), delimiter="\t"))[1:]
    want, report = {}, {"genes": {}, "diseases": {}}
    for idx, nid, ntype, name, src in nodes:
        if ntype == "gene/protein" and name in a.genes:
            want[idx] = ("gene", name)
            report["genes"][name] = {"node_index": idx, "ncbi_gene_id": nid}
        elif ntype == "disease" and name in a.diseases:
            want[idx] = ("disease", name)
            report["diseases"][name] = {"node_index": idx, "member_ids": nid.split("_"), "n_members": len(nid.split("_"))}
    report["genes_absent"] = [g for g in a.genes if g not in report["genes"]]
    report["diseases_absent"] = [d for d in a.diseases if d not in report["diseases"]]
    hasher = Hashing(opener(KG))
    rd = csv.reader(io.TextIOWrapper(io.BufferedReader(hasher, 1 << 20), encoding="utf-8", newline=""))
    next(rd)
    rel = collections.defaultdict(collections.Counter)
    partners = collections.defaultdict(lambda: collections.defaultdict(set))
    for row in rd:
        r, xi, xt, xn, yi, yt, yn = row[0], row[2], row[4], row[5], row[7], row[9], row[10]
        for here, other_t, other_n in ((xi, yt, yn), (yi, xt, xn)):
            if here in want:
                name = want[here][1]
                rel[name][r] += 1
                if r in ("drug_protein", "indication", "contraindication", "off-label use"):
                    partners[name][r].add(other_n)
    for kind in ("genes", "diseases"):
        for name, rec in report[kind].items():
            rec["edges_by_relation_directed_rows"] = dict(rel[name])
            rec["drug_partners"] = {k: sorted(v) for k, v in partners[name].items()}
    report["kg_md5_computed"] = hasher.md5.hexdigest()
    report["kg_md5_published"] = KG_MD5
    report["kg_md5_match"] = report["kg_md5_computed"] == KG_MD5
    json.dump(report, open(a.out, "w"), indent=1, sort_keys=True)
    print(json.dumps({k: report[k] for k in ("genes_absent", "diseases_absent", "kg_md5_match")}))


if __name__ == "__main__":
    main()
