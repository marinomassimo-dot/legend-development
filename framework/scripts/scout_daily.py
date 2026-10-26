#!/usr/bin/env python3
"""Daily radar: cheap diffs on a small watchlist plus new WWOX papers; silent unless something changed.

Reuses, does not replace: the weekly harness scout (`governance/candidates/HARNESS-SCOUT-*.md`,
`harness_session_start.py`), the capability-scout log, the throttled PubMed door `eutils.py`
(no contact e-mail, no `tool=` parameter) and the cron-probe pattern of `daily_push_check.py`.

What it does, per run (stdlib only, zero spend, no key, no install, no repo write):
  * for each WATCH entry fetches ONE small answer (GitHub release tag + licence, a database's
    version string, or status/ETag/Last-Modified of a landing page or accession) and compares a
    short fingerprint with the cache;
  * runs two PubMed esearch queries for WWOX and lists PMIDs not seen on the previous run;
  * writes ~/.local/state/legend/scout_daily.json (cache: scout_daily_state.json beside it).

A first run records a BASELINE and selects nothing. "No useful change" is the normal outcome and
prints nothing. A detection is a trigger to look, never a reading and never a scientific claim.

When something is selected the brief entry (WWOX question, contribution vs existing, cost,
licence, proof, outcome) goes to ~/.local/state/legend/scout_daily_pending_log.md, so cron never
dirties the repository. A session lands it with `--append-log` on a task branch (the log is
append-only: `disease-models/wwox/research/capability_scout_log.md`).

    python3 framework/scripts/scout_daily.py                # the cron command
    python3 framework/scripts/scout_daily.py --append-log   # move pending entries into the log
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import pwd
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import eutils  # noqa: E402

ROOT = HERE.parents[1]
LOG = ROOT / "disease-models/wwox/research/capability_scout_log.md"
TIMEOUT = 25
UA = "legend-scout-daily"  # no contact address, by rule

# Static context per entry: why it matters for WWOX and what it adds over what the repo has.
# kind: gh (GitHub repo), url (status+ETag+Last-Modified), json (a version string out of a JSON answer).
WATCH = [
    {"id": "ToolUniverse", "kind": "gh", "repo": "mims-harvard/ToolUniverse",
     "q": "Can one live-lookup layer (MCP) answer gene-level WWOX queries?",
     "vs": "_external_repos/MANIFEST.md lists it DESCRIBED only; tool_survey_20261022 says WATCH/TRY"},
    {"id": "TxGNN", "kind": "gh", "repo": "mims-harvard/TxGNN",
     "q": "Zero-shot repurposing scores for a rare, unlabelled disease",
     "vs": "no executed repurposing-score source today"},
    {"id": "EveryCure-MATRIX", "kind": "gh", "repo": "everycure-org/matrix",
     "q": "Open drug-disease score matrix usable as a seed list",
     "vs": "MATRIX is DESCRIBED in the manifest"},
    {"id": "DGIdb", "kind": "gh", "repo": "dgidb/dgidb-v5",
     "q": "Drug-gene interaction source/licence changes", "vs": "framework/adapters + kg_thin_slice.py use DGIdb"},
    {"id": "Monarch-app", "kind": "gh", "repo": "monarch-initiative/monarch-app",
     "q": "Phenotype/disease KG API changes", "vs": "kg_thin_slice.py uses Monarch"},
    {"id": "SigCom-LINCS", "kind": "url", "url": "https://maayanlab.cloud/sigcom-lincs/",
     "q": "Transcriptional-reversal signatures for a WWOX-loss signature",
     "vs": "LINCS/CLUE declined on terms (module_proof_20261023); SigCom/iLINCS not yet reached"},
    {"id": "iLINCS", "kind": "url", "url": "https://www.ilincs.org/",
     "q": "Same as SigCom-LINCS", "vs": "not yet reached"},
    {"id": "OpenTargets", "kind": "json", "method": "POST",
     "url": "https://api.platform.opentargets.org/api/v4/graphql",
     "body": '{"query":"{meta{dataVersion{year month iteration}}}"}',
     "path": ["data", "meta", "dataVersion"],
     "q": "New data release for WWOX target/association lookups", "vs": "adapter set has no Open Targets row"},
    {"id": "ChEMBL", "kind": "json", "url": "https://www.ebi.ac.uk/chembl/api/data/status.json",
     "path": ["chembl_db_version"],
     "q": "New ChEMBL release (bioactivity for candidate drugs)", "vs": "no ChEMBL adapter today"},
    {"id": "MTBLS12344", "kind": "url",
     "url": "https://www.ebi.ac.uk/metabolights/ws/studies/public/study/MTBLS12344",
     "q": "Is the metabolomics dataset openly accessible (metabolic-signature question)?",
     "vs": "accessibility previously unverified"},
    {"id": "E-MTAB-14792", "kind": "url", "url": "https://www.ebi.ac.uk/biostudies/api/v1/studies/E-MTAB-14792",
     "q": "Is the E-MTAB-14792 dataset accessible?", "vs": "accessibility previously unverified"},
]
PUBMED = [
    ("wwox_any", "WWOX[Title/Abstract] OR \"WW domain-containing oxidoreductase\"[Title/Abstract]"),
    ("wwox_dee", "(WWOX OR \"WW domain-containing oxidoreductase\") AND (epileptic encephalopathy OR "
                 "SCAR12 OR WOREE OR \"drug repurposing\" OR \"antisense\" OR \"gene therapy\")"),
]


def state_dir() -> Path:
    base = os.environ.get("LEGEND_SCOUT_DIR")
    if base:
        return Path(base)
    home = os.environ.get("HOME") or pwd.getpwuid(os.getuid()).pw_dir
    return Path(home) / ".local/state/legend"


def http(url: str, method: str = "GET", body: str | None = None, etag: str | None = None):
    """(status, headers, bytes); status 0 = no answer. Sends If-None-Match when an ETag is known."""
    headers = {"User-Agent": UA, "Accept": "application/json, text/html;q=0.8"}
    if body:
        headers["Content-Type"] = "application/json"
    if etag:
        headers["If-None-Match"] = etag
    request = urllib.request.Request(url, data=body.encode() if body else None, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.status, dict(response.headers), response.read(2_000_000)
    except urllib.error.HTTPError as error:
        return error.code, dict(error.headers or {}), error.read(200_000) or b""
    except (OSError, ValueError):
        return 0, {}, b""


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def probe(entry: dict, previous: dict, opener=http) -> dict:
    """Fingerprint of one entry: {fp: {...}, etag?}. A fingerprint holds only fields that mean a change."""
    kind = entry["kind"]
    if kind == "gh":
        base = f"https://api.github.com/repos/{entry['repo']}"
        code, hdr, body = opener(base + "/releases?per_page=1", etag=previous.get("etag"))
        if code == 304:
            return {"fp": previous["fp"], "etag": previous.get("etag"), "note": "304"}
        if code != 200:
            return {"error": f"releases HTTP {code}"}
        tags = json.loads(body or b"[]")
        tag = tags[0].get("tag_name") if tags else None
        code2, _, body2 = opener(base)
        info = json.loads(body2) if code2 == 200 else {}
        lic = (info.get("license") or {}).get("spdx_id")
        fp = {"release": tag, "license": lic if code2 == 200 else previous.get("fp", {}).get("license"),
              "archived": info.get("archived") if code2 == 200 else previous.get("fp", {}).get("archived")}
        return {"fp": fp, "etag": hdr.get("ETag") or hdr.get("Etag")}
    if kind == "json":
        code, hdr, body = opener(entry["url"], entry.get("method", "GET"), entry.get("body"))
        if code != 200:
            return {"error": f"HTTP {code}"}
        value = json.loads(body)
        for key in entry["path"]:
            value = value[key]
        return {"fp": {"version": value}}
    code, hdr, body = opener(entry["url"], "GET", None)
    if code == 0 or code >= 500:  # an outage is not a change
        return {"error": f"HTTP {code}"}
    low = {k.lower(): v for k, v in hdr.items()}
    fp = {"status": code}
    if code == 200:
        # ETag/Last-Modified when the server gives them; otherwise a hash of the first 2 kB is too
        # noisy for dynamic pages, so status alone then.
        for name in ("etag", "last-modified"):
            if low.get(name):
                fp[name] = low[name]
        if "last-modified" not in low and "etag" not in low and entry["url"].endswith(("MTBLS12344", "E-MTAB-14792")):
            fp["body"] = digest(body.decode("utf-8", "replace"))
    return {"fp": fp}


def pubmed_ids(term: str, opener=None) -> list[str]:
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&sort=pub_date"
           "&retmax=30&term=" + urllib.parse.quote(term))
    code, body = (opener or (lambda u: eutils.fetch(u, use_cache=False, retries=3, user_agent=UA)))(url)
    if code != 200:
        raise RuntimeError(f"esearch HTTP {code}")
    return list(json.loads(body)["esearchresult"]["idlist"])


def titles(ids: list[str], opener=None) -> dict[str, str]:
    if not ids:
        return {}
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids))
    code, body = (opener or (lambda u: eutils.fetch(u, use_cache=False, retries=3, user_agent=UA)))(url)
    if code != 200:
        return {}
    result = json.loads(body).get("result", {})
    return {i: result.get(i, {}).get("title", "") for i in ids}


def describe_change(old: dict, new: dict) -> str:
    keys = sorted(set(old) | set(new))
    return "; ".join(f"{k}: {old.get(k)!r} -> {new.get(k)!r}" for k in keys if old.get(k) != new.get(k))


def run(state: dict, watch=WATCH, queries=PUBMED, opener=http, pm_opener=None, now: dt.datetime | None = None):
    """Compare against `state`; return (report, new_state). Pure given its openers."""
    now = now or dt.datetime.now(dt.timezone.utc)
    baseline = not state.get("watch") and not state.get("pubmed")
    new_state = {"watch": {}, "pubmed": {}}
    selected, rows, errors = [], [], []
    for entry in watch:
        old = state.get("watch", {}).get(entry["id"], {})
        try:
            res = probe(entry, old, opener)
        except (ValueError, KeyError, TypeError) as exc:
            res = {"error": f"unparseable answer: {exc}"}
        if "error" in res:
            errors.append(f"{entry['id']}: {res['error']}")
            new_state["watch"][entry["id"]] = old  # keep the last good fingerprint
            rows.append({"id": entry["id"], "result": "ERROR", "detail": res["error"]})
            continue
        new_state["watch"][entry["id"]] = {k: v for k, v in res.items() if k in ("fp", "etag")}
        if old.get("fp") is None:
            rows.append({"id": entry["id"], "result": "BASELINE", "fp": res["fp"]})
        elif old["fp"] != res["fp"]:
            detail = describe_change(old["fp"], res["fp"])
            rows.append({"id": entry["id"], "result": "CHANGED", "detail": detail})
            selected.append({"id": entry["id"], "wwox_question": entry["q"], "contribution_vs_existing": entry["vs"],
                             "estimated_cost": "reading the change: minutes; any adoption: unestimated until triaged",
                             "licence": res["fp"].get("license") or "see source",
                             "proof": entry.get("repo") and f"https://github.com/{entry['repo']}/releases"
                                      or entry.get("url") or "", "detail": detail,
                             "outcome": "TO_TRIAGE (a detected change is not a reading)"})
        else:
            rows.append({"id": entry["id"], "result": "UNCHANGED"})
    papers = {}
    for name, term in queries:
        try:
            ids = pubmed_ids(term, pm_opener)
        except (RuntimeError, ValueError, KeyError, OSError) as exc:
            errors.append(f"pubmed {name}: {exc}")
            new_state["pubmed"][name] = state.get("pubmed", {}).get(name, [])
            continue
        seen = state.get("pubmed", {}).get(name)
        new_state["pubmed"][name] = ids
        fresh = [] if seen is None else [i for i in ids if i not in seen]
        papers[name] = {"count_returned": len(ids), "new_pmids": fresh, "baseline": seen is None}
        if fresh:
            tt = titles(fresh, pm_opener)
            papers[name]["titles"] = tt
            selected.append({"id": f"PubMed:{name}", "wwox_question": "New WWOX paper or external precedent that could "
                             "reopen a research question", "contribution_vs_existing": "not checked against the registry "
                             "(never grepped); intake triage decides new vs already read",
                             "estimated_cost": "abstract screen: minutes; a full read needs its receipt",
                             "licence": "PubMed metadata; full text per paper", "detail": "; ".join(
                                 f"{i} {tt.get(i, '')[:90]}" for i in fresh),
                             "proof": "https://pubmed.ncbi.nlm.nih.gov/?term=" + "+".join(fresh[:5]),
                             "outcome": "TO_TRIAGE (abstract = discovery, not a reading)"})
    report = {"run_at": now.isoformat(timespec="seconds"), "baseline": baseline,
              "verdict": "BASELINE" if baseline else ("SELECTED" if selected else "NO_USEFUL_CHANGE"),
              "selected": [] if baseline else selected, "watch": rows, "pubmed": papers, "errors": errors}
    return report, new_state


def entry_markdown(item: dict, when: str) -> str:
    return (f"\n## {when[:10]} · scout_daily · {item['id']}\n\n"
            f"**WWOX question.** {item['wwox_question']}\n\n"
            f"**Contribution vs existing.** {item['contribution_vs_existing']}\n\n"
            f"**Detected.** {item['detail']}\n\n"
            f"**Cost / licence.** {item['estimated_cost']}; {item['licence']}.\n\n"
            f"**Proof.** {item['proof']}\n\n**Outcome.** {item['outcome']}\n")


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f".{os.getpid()}.tmp")
    temporary.write_text(text)
    os.replace(temporary, path)


def append_log(directory: Path, log: Path = LOG) -> int:
    pending = directory / "scout_daily_pending_log.md"
    if not pending.is_file() or not pending.read_text().strip():
        print("no pending scout_daily entries")
        return 0
    with open(log, "a") as handle:
        handle.write(pending.read_text())
    pending.unlink()
    print(f"appended pending entries to {log}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--append-log", action="store_true", help="move pending entries into the scout log")
    args = parser.parse_args(argv)
    directory = state_dir()
    if args.append_log:
        return append_log(directory)
    state_path = directory / "scout_daily_state.json"
    try:
        state = json.loads(state_path.read_text())
    except (OSError, ValueError):
        state = {}
    report, new_state = run(state)
    atomic_write(directory / "scout_daily.json", json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    atomic_write(state_path, json.dumps(new_state, indent=1))
    if report["selected"]:
        with open(directory / "scout_daily_pending_log.md", "a") as handle:
            for item in report["selected"]:
                handle.write(entry_markdown(item, report["run_at"]))
        for item in report["selected"]:
            print(f"SCOUT_DAILY {item['id']}: {item['detail'][:200]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
