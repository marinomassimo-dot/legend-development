#!/usr/bin/env python3
"""Has any paper behind a read receipt gained a correction, expression of concern or retraction notice, and did the notice come after the reading?

Read-only on the receipt ledger. For every distinct PMID in it, asks Europe PMC (REST, no key,
no contact parameter, one request at a time) for the record's comment/correction links and keeps
three link types: `Erratum in`, `Expression of concern in`, `Retraction in`. The notice's own
date comes from the notice record (or, for an old erratum listed only by citation, from the year
in the citation). The table says per hit whether the notice is dated after the last receipt event
for that paper (`POST`), before the first (`PRE`), between the two (`BETWEEN`) or not comparable
(`UNKNOWN`).

What it does not see: a PMID absent from the `MED` source (a PMC-hosted preprint) is listed under
`not_indexed`, not as clean; a notice that PubMed never linked to the paper is invisible here (the
Retraction Watch route in `dependency_integrity.py` is a second, DOI-keyed route); a notice date
is the notice's first publication date, not the day Europe PMC linked it.

A bot-challenge or non-JSON answer stops the run (exit 2). The table is written to `--out`.

    python3 framework/scripts/epmc_notice_sweep.py --out /tmp/notice_sweep
    python3 framework/scripts/epmc_notice_sweep.py --self-check
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
NOTICE_TYPES = ("Erratum in", "Expression of concern in", "Retraction in")
COLUMNS = ("pmid", "receipt_events", "first_event", "last_event", "depths", "notice_type",
           "notice_id", "notice_date", "vs_receipt", "notice_doi", "title")


def receipt_index(path: Path) -> dict[str, list[tuple[str, str, str]]]:
    """PMID -> [(event_at, event_id, evidence_depth)] over every row that names a PMID."""
    out: dict[str, list[tuple[str, str, str]]] = collections.defaultdict(list)
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        pmid = (row.get("study_id") or {}).get("pmid")
        if pmid:
            out[str(pmid)].append((row["event_at"], row["event_id"], row["evidence_depth"]))
    return out


def date_key(text: str) -> tuple[int, ...] | None:
    """'2025-06-13' -> (2025, 6, 13); '2012 May' -> (2012, 5); '2013' -> (2013,); else None."""
    m = re.match(r"\s*((?:19|20)\d\d)(?:[-\s]+(\d\d|[A-Z][a-z]{2}))?(?:[-\s]+(\d{1,2}))?", text or "")
    if not m:
        return None
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    key = [int(m.group(1))]
    if m.group(2):
        key.append(int(m.group(2)) if m.group(2).isdigit() else months.index(m.group(2)) + 1)
        if m.group(3):
            key.append(int(m.group(3)))
    return tuple(key)


def reference_date(reference: str) -> str:
    """The date part of a citation-only notice ('Oncogene. 2006 Dec 7;25(58):7662' -> '2006 Dec 7')."""
    m = re.search(r"(?:19|20)\d\d(?:\s+[A-Z][a-z]{2}(?:\s+\d{1,2})?)?", reference or "")
    return m.group(0) if m else ""


def compare(notice: str, first_event: str, last_event: str) -> str:
    """POST / PRE / BETWEEN / UNKNOWN, comparing at the precision the notice date has."""
    nk = date_key(notice)
    if nk is None:
        return "UNKNOWN"
    n = len(nk)
    first, last = date_key(first_event)[:n], date_key(last_event)[:n]
    if nk > last:
        return "POST"
    if nk < first:
        return "PRE"
    if nk == first == last:
        return "SAME_DAY_OR_PERIOD"
    return "BETWEEN"


def get(query: str, page_size: int = 1000) -> list[dict]:
    url = API + urllib.parse.urlencode({"query": query, "resultType": "core", "format": "json",
                                        "pageSize": page_size})
    try:
        body = urllib.request.urlopen(urllib.request.Request(url), timeout=60).read()
        return json.loads(body)["resultList"]["result"]
    except Exception as exc:  # challenge page, HTTP error or non-JSON body: stop, never read as clean
        print(f"STOP: {exc!r}", file=sys.stderr)
        sys.exit(2)


def sweep(index: dict, batch: int, pause: float) -> tuple[list[list], list[str]]:
    pmids = sorted(index)
    core: dict[str, dict] = {}
    for i in range(0, len(pmids), batch):
        for rec in get("SRC:MED AND EXT_ID:(" + " OR ".join(pmids[i:i + batch]) + ")"):
            core[rec["id"]] = rec
        time.sleep(pause)
    not_indexed = [p for p in pmids if p not in core]
    hits = [(p, c) for p, rec in core.items()
            for c in (rec.get("commentCorrectionList") or {}).get("commentCorrection", [])
            if c.get("type") in NOTICE_TYPES]
    ids = sorted({c["id"] for _, c in hits if c.get("id")})
    notices: dict[str, dict] = {}
    for i in range(0, len(ids), batch):
        for rec in get("SRC:MED AND EXT_ID:(" + " OR ".join(ids[i:i + batch]) + ")"):
            notices[rec["id"]] = rec
        time.sleep(pause)
    rows = []
    for p, c in hits:
        events = sorted(index[p])
        note = notices.get(c.get("id", ""), {})
        date = note.get("firstPublicationDate") or reference_date(c.get("reference", ""))
        rows.append([p, len(events), events[0][0][:10], events[-1][0][:10],
                     "|".join(sorted({e[2] for e in events})), c["type"],
                     c.get("id") or "(no id; " + c.get("reference", "") + ")", date,
                     compare(date, events[0][0][:10], events[-1][0][:10]), note.get("doi", ""),
                     (core[p].get("title") or "")[:80]])
    rows.sort(key=lambda r: (r[8] != "POST", r[5], r[0]))
    return rows, not_indexed


def self_check() -> int:
    assert date_key("2025-06-13") == (2025, 6, 13) and date_key("2012 May") == (2012, 5)
    assert date_key("Oncogene. 2006 Dec 7;25(58):7662") is None
    assert reference_date("Oncogene. 2006 Dec 7;25(58):7662") == "2006 Dec 7"
    assert reference_date("Nature.2014 Jul 17;511(7509):370") == "2014 Jul 17"
    assert reference_date("PLoS One. 2013;8(8). doi:10.1371/annotation/x") == "2013"
    assert compare("2026-11-20", "2026-07-26", "2026-08-06") == "POST"
    assert compare("2026-07-17", "2026-07-26", "2026-08-06") == "PRE"
    assert compare("2026-08-01", "2026-07-26", "2026-08-06") == "BETWEEN"
    assert compare("2026 Nov", "2026-11-04", "2026-11-04") == "SAME_DAY_OR_PERIOD"
    assert compare("2012 May", "2026-11-07", "2026-11-07") == "PRE"
    assert compare("", "2026-11-07", "2026-11-07") == "UNKNOWN"
    print("self-check OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--ledger", type=Path, default=LEDGER)
    ap.add_argument("--out", type=Path, help="folder for notice_sweep.tsv and not_indexed.txt")
    ap.add_argument("--batch", type=int, default=40)
    ap.add_argument("--pause", type=float, default=1.0, help="seconds between requests")
    ap.add_argument("--self-check", action="store_true", help="run the offline date checks and exit")
    args = ap.parse_args()
    if args.self_check:
        return self_check()
    index = receipt_index(args.ledger)
    rows, not_indexed = sweep(index, args.batch, args.pause)
    tally = collections.Counter((r[5], r[8]) for r in rows)
    print(f"{len(index)} distinct PMIDs; {len(rows)} notice links; not indexed: {len(not_indexed)}")
    for key, n in sorted(tally.items()):
        print(f"  {key[0]} / {key[1]}: {n}")
    post = [r for r in rows if r[8] == "POST"]
    print(f"POST-DATING: {len(post)}" + ("" if post else " (none)"))
    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "notice_sweep.tsv").write_text(
            "\t".join(COLUMNS) + "\n" + "\n".join("\t".join(str(x) for x in r) for r in rows) + "\n",
            encoding="utf-8")
        (args.out / "not_indexed.txt").write_text("\n".join(not_indexed) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
