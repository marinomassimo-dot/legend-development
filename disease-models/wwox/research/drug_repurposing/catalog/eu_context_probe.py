#!/usr/bin/env python3
"""European context probe (IT5 P10): the EU register of nutrition and health claims and the EU Novel Food
status catalogue, as published on the EU Open Data Portal (DG SANTE data lake download URLs, no key, no
registration, no contact string sent).  Name-based, counts only; it says how a NAME appears in two EU
registers, never that a product is available, authorised for a use, effective or safe.

  eu_context_probe.py fetch                 download both JSON files into $LEGEND_CATALOG_CACHE/eu/ (skips files already there)
  eu_context_probe.py run                   offline: write eu_context_probe.tsv for the names in dsld_probe_annotations.tsv families
  eu_context_probe.py --help
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get("LEGEND_CATALOG_CACHE", HERE / "cache")) / "eu"
URLS = {
    "novel_food.ndjson": "https://api.datalake.sante.service.ec.europa.eu/novel-food-catalog/novel-food-catalog/download?format=json&api-version=v2.0",
    "health_claims.ndjson": "https://api.datalake.sante.service.ec.europa.eu/health-claims/download-eu-register?format=json&api-version=v2.0",
}
UA = "legend-repurposing-research/1.0 (public data download; no contact string)"


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", re.sub(r"<[^>]+>", " ", s or "").lower()).strip()


def fetch() -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    for name, url in URLS.items():
        p = CACHE / name
        if p.exists():
            print(f"present: {p.name}")
            continue
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as r:
            p.write_bytes(r.read())
        print(f"fetched {p.name}: {p.stat().st_size} bytes sha256 {hashlib.sha256(p.read_bytes()).hexdigest()}")
        time.sleep(2)
    return 0


def rows(name: str):
    return [json.loads(line) for line in (CACHE / name).read_text().splitlines() if line.strip()]


def has(term: str, text: str) -> bool:
    return f" {term} " in f" {text} "


def run() -> int:
    nf, hc = rows("novel_food.ndjson"), rows("health_claims.ndjson")
    names = []
    for r in csv.DictReader((HERE / "dsld_probe_annotations.tsv").open(), delimiter="\t"):
        if r["family"] != "control" and r["query"] not in names:
            names.append(r["query"])
    nf_text = [(norm(" ; ".join(str(x.get(k) or "") for k in ("novel_food_name", "novel_food_display_name", "common_name", "synonyms"))), x) for x in nf]
    hc_text = [(norm(x.get("nutrient_subst_food_no_html") or x.get("nutrient_subst_food")), x) for x in hc]
    out = HERE / "eu_context_probe.tsv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["query", "novel_food_catalogue_entries", "novel_food_status_values", "novel_food_example_names", "health_claim_entries",
                    "health_claim_status_counts", "health_claim_example_substances", "note"])
        for q in names:
            t = norm(q)
            nfm = [x for s, x in nf_text if has(t, s)]
            hcm = [x for s, x in hc_text if has(t, s)]
            st = sorted({str(x.get("novel_food_status")) for x in nfm})
            cs: dict = {}
            for x in hcm:
                cs[x.get("claim_status")] = cs.get(x.get("claim_status"), 0) + 1
            w.writerow([q, len(nfm), ";".join(st), ";".join(sorted({re.sub(r"<[^>]+>", "", x["novel_food_display_name"] or "").strip() for x in nfm})[:3]), len(hcm),
                        ";".join(f"{k}={v}" for k, v in sorted(cs.items())), ";".join(sorted({norm(x.get("nutrient_subst_food_no_html"))[:60] for x in hcm})[:3]),
                        "name match (whole words, normalised) in the EU register text; not a product, a dose, a use or a safety statement; EU-level, not Italian national"])
    print(f"wrote {out.name}: {len(names)} rows")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("cmd", nargs="?", choices=("fetch", "run"), default="run")
    a = ap.parse_args(argv)
    return fetch() if a.cmd == "fetch" else run()


if __name__ == "__main__":
    sys.exit(main())
