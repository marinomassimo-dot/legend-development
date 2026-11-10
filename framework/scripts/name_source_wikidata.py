#!/usr/bin/env python3
"""English labels of compounds from Wikidata, joined to a compound ONLY through its ChEMBL identifier, as a class-A name source for the shareable view.

WHY THIS EXISTS (2026-11-10, HE43 H5)
-------------------------------------
The shareable page withholds compound names whose only provenance is a ChEMBL (CC BY-SA 3.0) or GtoPdb (ODbL / CC BY-SA 4.0) record. A name is allowed
when an independent class-A source states it (MATRIX list, openFDA NDC), and none of the twelve compound_view entries had one. Wikidata states that its
structured data (the item namespace) "is released into the public domain" (CC0; https://www.wikidata.org/wiki/Wikidata:Licensing, read 2026-11-10; the
page does not mention labels by name). An item that carries a ChEMBL id (property P592) can therefore give an attributed name, joined by identifier and
never by name.

Uncertainty kept (not a legal clearance): the licensing page is silent on labels as such, and it cannot say where one label's wording came from, so a label
is shown with its Wikidata item number and the credit line, and a label that differs from the compound's usual name (for example a code name) is shown as
Wikidata states it, never replaced.

  python3 framework/scripts/name_source_wikidata.py CHEMBL305187 CHEMBL471737 --out view/name_source_wikidata.tsv

Fails closed: any HTTP error, a malformed answer or an item without a label is reported and nothing is written; an id without an item is a row with
state NO_WIKIDATA_ITEM, which says nothing about the compound. Keyless, no contact address, one request.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://www.wikidata.org/w/api.php"
LICENCE_URL = "https://www.wikidata.org/wiki/Wikidata:Licensing"
FIELDS = ("chembl_id", "state", "qid", "label", "retrieved_utc", "source", "licence_url")
CHEMBL_ID = re.compile(r"CHEMBL\d+")
QID = re.compile(r"Q\d+")


def search_url(chembl_id: str) -> str:
    return API + "?" + urllib.parse.urlencode({"action": "query", "list": "search", "srsearch": f"haswbstatement:P592={chembl_id}", "srlimit": 5, "format": "json"})


def labels_url(qids) -> str:
    return API + "?" + urllib.parse.urlencode({"action": "wbgetentities", "ids": "|".join(sorted(qids)), "props": "labels", "languages": "en", "format": "json"})


def http_fetch(url: str, retries: int = 3) -> dict:
    """GET one JSON answer. A 429 is retried up to `retries` times after the server's Retry-After (at most 60 s each); any other error, or a 429 that persists, raises."""
    req = urllib.request.Request(url, headers={"User-Agent": "legend-name-source/1.0 (research tool; no contact)", "Accept": "application/json"})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == retries:
                raise
            time.sleep(min(60.0, float(e.headers.get("Retry-After") or 30)))
    raise OSError("unreachable")


def fetch(ids, fetcher=None, now=None, pause: float = 2.0) -> list[dict]:
    """One search per id (items carrying that ChEMBL id in property P592), then one label request for the items found. Ambiguity, a missing label or a malformed answer raises."""
    bad = [i for i in ids if not CHEMBL_ID.fullmatch(i)]
    if bad:
        raise ValueError(f"not ChEMBL ids: {bad}")
    get = fetcher or http_fetch
    stamp = (now or datetime.datetime.now(datetime.timezone.utc)).strftime("%Y-%m-%dT%H:%MZ")
    found: dict[str, str] = {}
    for i in sorted(set(ids)):
        try:
            hits = get(search_url(i))["query"]["search"]
        except (KeyError, TypeError) as e:
            raise ValueError(f"{i}: answer without query.search: {e!r}")
        qids = [h["title"] for h in hits if QID.fullmatch(h.get("title", ""))]
        if len(qids) > 1:
            raise ValueError(f"{i}: {len(qids)} Wikidata items carry this ChEMBL id ({', '.join(qids)}); not chosen automatically")
        if qids:
            found[i] = qids[0]
        if pause and not fetcher:
            time.sleep(pause)
    labels: dict[str, str] = {}
    if found:
        try:
            ents = get(labels_url(set(found.values())))["entities"]
        except (KeyError, TypeError) as e:
            raise ValueError(f"label answer without entities: {e!r}")
        for q in found.values():
            lab = ((ents.get(q) or {}).get("labels") or {}).get("en", {}).get("value")
            if not lab:
                raise ValueError(f"item {q} has no English label")
            labels[q] = lab
    return [({"chembl_id": i, "state": "LABEL", "qid": found[i], "label": labels[found[i]]} if i in found else
             {"chembl_id": i, "state": "NO_WIKIDATA_ITEM", "qid": "", "label": ""}) | {"retrieved_utc": stamp, "source": "Wikidata P592 search", "licence_url": LICENCE_URL}
            for i in sorted(set(ids))]


def write(rows: list[dict], path: Path) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def read(path: Path) -> list[dict]:
    if not Path(path).exists():
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("ids", nargs="+", help="ChEMBL ids")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args(argv)
    try:
        rows = fetch(a.ids)
    except (ValueError, OSError) as e:
        print(f"NOT WRITTEN: {e}", file=sys.stderr)
        return 3
    write(rows, a.out)
    print(f"{sum(r['state'] == 'LABEL' for r in rows)} labels, {sum(r['state'] != 'LABEL' for r in rows)} without item; wrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
