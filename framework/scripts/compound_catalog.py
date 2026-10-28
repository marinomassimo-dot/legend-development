#!/usr/bin/env python3
"""Read-only lookup over a compound catalogue (JSONL, optionally gzipped) built by a disease model.

Generic engine code: it knows the entry shape, not the disease. The WWOX catalogue is built by
`disease-models/wwox/research/drug_repurposing/catalog/catalog_build.py` (network `fetch`, offline
`build`); this module never touches the network and never writes.

  compound_catalog.py lookup [--catalog PATH] [--id X] [--name X] [--target X] [--access X] [--status X] [--limit N] [--full]
  compound_catalog.py card CARD_ID [--catalog PATH] [--links PATH]     # entries linked to a curated card

Importable: `load(path)`, `find(entries, id=, name=, target=, access=, status=)`, `for_card(card_id, ...)`.
An empty result means "no entry matched in this catalogue", never "not a drug"; unknown access is
`unknown/unverified`, not a negative.
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_DIR = REPO / "disease-models/wwox/research/drug_repurposing/catalog"
DEFAULT_CATALOG = DEFAULT_DIR / "catalog.jsonl.gz"
DEFAULT_LINKS = DEFAULT_DIR / "card_links.json"


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def load(path: Path = DEFAULT_CATALOG) -> list[dict]:
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def find(entries, id=None, name=None, target=None, access=None, status=None) -> list[dict]:
    out = []
    for e in entries:
        if id:
            q = id.upper()
            vals = {e["id"].upper()} | {str(x).upper() for v in e["ids"].values() for x in (v if isinstance(v, list) else [v]) if x}
            if q not in vals and "CAT:" + q not in vals:
                continue
        if name:
            q = _norm(name)
            if q not in _norm(e.get("name") or "") and not any(q in _norm(s) for s in e.get("synonyms", [])):
                continue
        if target:
            q = target.lower()
            if not any(q in (t.get("gene") or "").lower() or q in " ".join(t.get("gene_symbols") or []).lower()
                       or q in (t.get("target_name") or "").lower() or q == (t.get("target_id") or "").lower() for t in e.get("targets", [])):
                continue
        if access and access not in e.get("access_categories", []):
            continue
        if status and e.get("status_class") != status:
            continue
        out.append(e)
    return out


def for_card(card_id: str, catalog: Path = DEFAULT_CATALOG, links: Path = DEFAULT_LINKS) -> dict:
    """{'card_id', 'links': [{catalogue_id, rule,...}], 'entries': [...], 'status': MATCHED|UNMATCHED|CARD_UNKNOWN}"""
    lk = json.loads(Path(links).read_text())["cards"].get(card_id)
    if lk is None:
        return {"card_id": card_id, "status": "CARD_UNKNOWN", "links": [], "entries": []}
    ids = {l["catalogue_id"] for l in lk["links"]}
    ents = [e for e in load(catalog) if e["id"] in ids]
    return {"card_id": card_id, "status": "MATCHED" if ents else "UNMATCHED", "links": lk["links"], "entries": ents,
            "unmatched_reason": lk.get("unmatched_reason")}


def _row(e: dict) -> str:
    return "\t".join([e["id"], e.get("name") or "-", e.get("modality", ""), e.get("status_class", ""), ",".join(e.get("access_categories", [])),
                      f"targets={len(e.get('targets', []))}", e.get("origin", "")])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd")
    lo = sub.add_parser("lookup")
    for k in ("id", "name", "target", "access", "status"):
        lo.add_argument("--" + k)
    lo.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    lo.add_argument("--limit", type=int, default=20)
    lo.add_argument("--full", action="store_true")
    cd = sub.add_parser("card")
    cd.add_argument("card_id")
    cd.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    cd.add_argument("--links", type=Path, default=DEFAULT_LINKS)
    a = ap.parse_args(argv)
    if a.cmd == "lookup":
        hits = find(load(a.catalog), a.id, a.name, a.target, a.access, a.status)
        print(f"{len(hits)} match(es)", file=sys.stderr)
        for e in hits[: a.limit]:
            print(json.dumps(e, ensure_ascii=False, indent=1) if a.full else _row(e))
        return 0 if hits else 1
    if a.cmd == "card":
        r = for_card(a.card_id, a.catalog, a.links)
        print(json.dumps({k: v for k, v in r.items() if k != "entries"}, indent=1, ensure_ascii=False))
        for e in r["entries"]:
            print(_row(e))
        return 0 if r["status"] == "MATCHED" else 1
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
