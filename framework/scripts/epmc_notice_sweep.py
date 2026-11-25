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

A bot-challenge, an HTTP refusal or a non-JSON answer stops the run (exit 2); an HTTP 429 or 5xx (Retry-After, at least 60 s)
or a request with no answer (30 s) is tried once more and stops the run if it fails again. The table is written to `--out`.

`--catalogue` (ADV-258, 2026-11-25; method of SCI's ADV-256) asks the same question over every catalogued PMID (corpus
seed, paper registry, batch queue, tracking log), reports `pmid, kind, notice_pmid, notice_date` for retractions,
expressions of concern and corrections, the rows that are new since the previous run, and prints a proposed flag line for
each retraction or concern the repository does not already mention. It edits no registry. `scout_daily.py` runs it once
a week; its state is under ~/.local/state/legend/notice_sweep (LEGEND_NOTICE_STATE overrides), and the advisor's tick says
`NEW NOTICE` once for a retraction or concern that appeared since the previous run.

    python3 framework/scripts/epmc_notice_sweep.py --out /tmp/notice_sweep
    python3 framework/scripts/epmc_notice_sweep.py --catalogue
    python3 framework/scripts/epmc_notice_sweep.py --self-check
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
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


class SweepStopped(Exception):
    """The service did not answer with data. The run stops: an unanswered PMID is never read as clean."""


def get(query: str, page_size: int = 1000, opener=urllib.request.urlopen, sleep=time.sleep) -> list[dict]:
    url = API + urllib.parse.urlencode({"query": query, "resultType": "core", "format": "json",
                                        "pageSize": page_size})
    for attempt in (1, 2):
        try:
            body = opener(urllib.request.Request(url), timeout=120).read()
            return json.loads(body)["resultList"]["result"]
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise SweepStopped(f"HTTP {exc.code}") from exc
            after = str((exc.headers or {}).get("Retry-After") or "")
            sleep(min(max(int(after) if after.isdigit() else 60, 60), 300))
        except (TimeoutError, ConnectionError, urllib.error.URLError) as exc:   # no answer at all is not a refusal: one more try
            if attempt == 2:
                raise SweepStopped(repr(exc)) from exc
            sleep(30)
        except Exception as exc:  # challenge page, network error or non-JSON body
            raise SweepStopped(repr(exc)) from exc
    raise SweepStopped("no answer")


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


# ---- the catalogue pass (ADV-258) --------------------------------------------------------------------------------

REGISTRIES = ROOT / "disease-models/wwox/registries"
SEED = "corpus_seed_pubmed_20260806.tsv"
QUEUE = "batch_queue.md"
RECORD_FILES = ("paper_registry_current.md", "literature_tracking_log_current.md")
PMID_IN_TEXT = re.compile(r"(?:PMID\W{0,4}|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{6,8})")
NOTICE_COLUMNS = ("pmid", "kind", "notice_pmid", "notice_date")
FLAGGED_KINDS = ("retraction", "concern")
KIND_WORDS = {"retraction": re.compile(r"retract|ritrat|ritirat", re.I), "concern": re.compile(r"concern", re.I)}
WEEK_DAYS = 7


def read_text(folder: Path, name: str) -> str:
    path = folder / name
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def catalogue_pmids(folder: Path = REGISTRIES) -> list[str]:
    """Every PMID the repository catalogues: the PubMed corpus seed, identifier lines of the paper registry and the tracking log, and the rows of the batch queue."""
    found: set[str] = set()
    if (folder / SEED).exists():
        with (folder / SEED).open(encoding="utf-8", newline="") as handle:
            found |= {row["pmid"] for row in csv.DictReader(handle, delimiter="\t") if row.get("pmid")}
    found |= set(re.findall(r"(?m)^\| \[(\d{6,8})\]\(", read_text(folder, QUEUE)))
    for name in RECORD_FILES:
        found |= {p for line in read_text(folder, name).split("\n") if "Identifier" in line for p in PMID_IN_TEXT.findall(line)}
    return sorted(found, key=int)


def notice_kind(link_type: str) -> str:
    t = link_type.lower()
    if t in ("retraction in", "partial retraction in"):
        return "retraction"
    if t == "expression of concern in":
        return "concern"
    if t in ("erratum in", "corrected and republished in", "retracted and republished in") or ("correct" in t and t.endswith(" in")):
        return "correction"
    return ""


def catalogue_notices(pmids: list[str], batch: int = 40, pause: float = 2.0, fetch=get) -> tuple[list[tuple[str, str, str, str]], list[str]]:
    """(rows of NOTICE_COLUMNS, PMIDs the source does not hold). One batched request at a time, spaced."""
    def in_batches(ids):
        for i in range(0, len(ids), batch):
            yield from fetch("SRC:MED AND EXT_ID:(" + " OR ".join(ids[i:i + batch]) + ")")
            time.sleep(pause)

    core = {rec["id"]: rec for rec in in_batches(pmids)}
    hits: list[tuple[str, str, str, str]] = []
    for pmid, rec in core.items():
        marked = False
        for link in (rec.get("commentCorrectionList") or {}).get("commentCorrection", []):
            kind = notice_kind(link.get("type", ""))
            if kind:
                hits.append((pmid, kind, link.get("id") or "", link.get("reference", "")))
                marked = marked or kind == "retraction"
        if not marked and "Retracted Publication" in (rec.get("pubTypeList") or {}).get("pubType", []):
            hits.append((pmid, "retraction", "", ""))
    notices = {rec["id"]: rec for rec in in_batches(sorted({h[2] for h in hits if h[2]}))}
    rows = [(p, k, n or "-", notices.get(n, {}).get("firstPublicationDate") or reference_date(ref) or "-") for p, k, n, ref in hits]
    order = {"retraction": 0, "concern": 1, "correction": 2}
    return sorted(set(rows), key=lambda r: (order[r[1]], int(r[0]), r[2])), [p for p in pmids if p not in core]


def repository_mentions(pmid: str, kind: str, folder: Path = REGISTRIES) -> bool:
    """Does a queue line, or a registry or log record naming this PMID, already say this kind of notice? A word match, so a place to look, not a verdict."""
    words = KIND_WORDS[kind]
    if any(pmid in line and words.search(line) for line in read_text(folder, QUEUE).split("\n")):
        return True
    named = re.compile(r"(?:PMID\W{0,4}|pubmed\.ncbi\.nlm\.nih\.gov/)%s\b" % pmid)
    return any(named.search(unit) and words.search(unit) for name in RECORD_FILES for unit in re.split(r"(?m)^(?=## )", read_text(folder, name)))


def proposed_flags(rows: list[tuple[str, str, str, str]], folder: Path = REGISTRIES) -> list[str]:
    """Lines to propose to the owner of the state files, for retractions and concerns the repository does not mention. Printed, never written."""
    label = {"retraction": "retracted", "concern": "expression of concern"}
    return [f"PROPOSED FLAG (not applied): PMID {pmid} {label[kind]}; notice {notice}, {date}; it may not support or promote a claim until read"
            for pmid, kind, notice, date in rows if kind in FLAGGED_KINDS and not repository_mentions(pmid, kind, folder)]


def state_folder() -> Path:
    return Path(os.environ.get("LEGEND_NOTICE_STATE") or Path.home() / ".local/state/legend/notice_sweep")


def read_summary(folder: Path | None = None) -> dict:
    try:
        return json.loads(((folder or state_folder()) / "summary.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def due(folder: Path | None = None, now: dt.datetime | None = None, days: int = WEEK_DAYS) -> bool:
    last = read_summary(folder).get("run_at", "")
    now = now or dt.datetime.now(dt.timezone.utc)
    try:
        return now - dt.datetime.fromisoformat(last.replace("Z", "+00:00")) >= dt.timedelta(days=days) - dt.timedelta(hours=1)
    except ValueError:
        return True


def run_catalogue(folder: Path | None = None, registries: Path = REGISTRIES, fetch=get, pause: float = 2.0, now: dt.datetime | None = None) -> dict:
    """One pass: ask, compare with the previous run, write `notices.tsv` and `summary.json` in the state folder. The first run is a baseline: nothing is 'new' in it.
    A stopped sweep raises and writes nothing, so the previous run stays the comparison."""
    folder = folder or state_folder()
    pmids = catalogue_pmids(registries)
    if not pmids:
        raise SweepStopped(f"no catalogued PMID found under {registries}")
    rows, not_indexed = catalogue_notices(pmids, pause=pause, fetch=fetch)
    table = folder / "notices.tsv"
    before = read_summary(folder)
    held = set()
    if table.exists():
        held = {tuple(line.split("\t")[:3]) for line in table.read_text(encoding="utf-8").splitlines()[1:] if line}
    new = [r for r in rows if before and r[:3] not in held]
    # flags accumulate until a reader has seen them: a second run must not erase what the tick never read
    waiting = [tuple(x) for x in before.get("new_flagged", [])]
    waiting += [r for r in new if r[1] in FLAGGED_KINDS and r not in waiting]
    summary = {"run_at": (now or dt.datetime.now(dt.timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ"), "pmids": len(pmids), "not_indexed": len(not_indexed),
               "counts": {k: len({r[0] for r in rows if r[1] == k}) for k in ("retraction", "concern", "correction")},
               "baseline": not before, "new": [list(r) for r in new], "new_flagged": [list(r) for r in waiting], "proposed": proposed_flags(rows, registries)}
    folder.mkdir(parents=True, exist_ok=True)
    table.write_text("\t".join(NOTICE_COLUMNS) + "\n" + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    (folder / "summary.json").write_text(json.dumps(summary, indent=1) + "\n", encoding="utf-8")
    return summary


def summary_text(summary: dict, folder: Path | None = None) -> str:
    c = summary["counts"]
    lines = [f"NOTICE SWEEP {summary['run_at']}: {summary['pmids']} catalogued PMIDs ({summary['not_indexed']} not indexed, never read as clean); "
             f"retracted {c['retraction']}, concern {c['concern']}, corrected {c['correction']}; " + ("baseline run" if summary["baseline"] else f"new since the previous run: {len(summary['new'])}")]
    lines += [f"  new {' '.join(r)}" for r in summary["new"]]
    lines += ["  " + line for line in summary["proposed"]]
    lines.append(f"  table: {(folder or state_folder()) / 'notices.tsv'}")
    return "\n".join(lines)


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
    ap.add_argument("--catalogue", action="store_true", help="sweep every catalogued PMID, compare with the previous run, print proposed flag lines (writes only in the state folder)")
    args = ap.parse_args()
    if args.self_check:
        return self_check()
    try:
        if args.catalogue:
            folder = args.out or state_folder()
            print(summary_text(run_catalogue(folder, pause=max(args.pause, 2.0)), folder))
            return 0
        index = receipt_index(args.ledger)
        rows, not_indexed = sweep(index, args.batch, args.pause)
    except SweepStopped as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        return 2
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
