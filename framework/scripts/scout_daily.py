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

Each probe observes the resource whose change would matter, not a proxy: a licence of DATA is read
from the dataset card (Hugging Face API), an explorer's accessibility from the explorer URL (status
only, one attempt), a repository without releases from its latest default-branch commit. An
availability or ETag change is reported as an AVAILABILITY SIGNAL, never as a capability.

Context first: each run resolves the current remote `main` SHA (`git ls-remote development main`, read-only), reads
the roadmap, README and capability log AT THAT REVISION (`git show`; no checkout is touched), reuses its cache while
the SHA or a blob is unchanged, and states a FRESHNESS LIMIT when it cannot verify. An old CURRENT/Updated heading
never outranks later dated evidence.

A small external SEARCH (two questions a day plus one open slot, from a rotation of priority questions each tied to
the decision it would change) goes through explicit channels reported separately with outcome error | no_news | delta:
GitHub (default-branch head and latest release kept apart), Hugging Face (models, datasets, Spaces: revision, card
licence, files), Nature portfolio (Crossref metadata of Nature-portfolio journals); Europe PMC complements. Probing
a known resource is not a discovery on the channel. Hits are de-duplicated (DOI, title, repo name), licences are kept
per part (code / data / weights / service / article) and every claim carries labels (declared ... transferable_to_wwox,
all `unknown` until someone does the work). Stars and downloads are popularity, never quality. "No useful
opportunity" is a valid result.
A followed teams/repos list (max 6 teams, 18 repos, 3 per team; scout_daily_config.json) is deep-checked weekly and
never limits the daily search; no collaborator expansion, no contact, public projects only.
Signal -> examination -> trial -> decision -> integration is a state record (`--trace`); a log line is not an
examination, and adoption in a plan is not a verified implementation. The radar researches and plans; it installs
nothing. Every run ends with a briefing (material deltas only, ONE next step first; a save is claimed only after
read-back).
`--discover-only [--theme N|all]` runs just the search (not a second scheduler: the cron line is the
only one). `--status` prints the compact line that `harness_session_start.py` shows at session start.

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
import fcntl
import hashlib
import html
import json
import os
import pwd
import re
import subprocess
import sys
import time
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
# kind: gh (GitHub repo), hf (dataset card + commit sha), url (status+ETag+Last-Modified), json (a version string, or
# with digest=True the hash of a record list), regex (file names in a plain listing), avail (reachability).
# `vs` points at the measuring tool or the dated record; it never restates an inventory (that goes stale).
# `signal`: "availability" = a change in reachability/ETag, reported as such and never as a capability.
# `reopen`: the condition whose observation this probe stands for (one line, from the dated outcome).
WATCH = [
    {"id": "ToolUniverse", "kind": "gh", "repo": "mims-harvard/ToolUniverse",
     "q": "Can one live-lookup layer (MCP) answer gene-level WWOX queries?",
     "vs": "optional isolated tool; see tooluniverse_capability_test_20261026.md (work saved) and tool_survey row 12"},
    {"id": "TxGNN-code", "kind": "gh", "repo": "mims-harvard/TxGNN",
     "q": "Did the code or a deployable (full_graph) checkpoint change?",
     "vs": "p3b1/txgnn_matrix_outcomes_20261026.md (REASONED WAIT); no release exists, so the latest commit is the signal"},
    {"id": "TxGNN-explorer", "kind": "avail", "url": "https://txgnn.org", "signal": "availability",
     "q": "Is the explorer (the only carrier of per-disease predictions) reachable again?",
     "vs": "p3b1/txgnn_matrix_outcomes_20261026.md section 1.4 reopening condition; a reachable site is not yet a retrievable prediction"},
    {"id": "EveryCure-MATRIX-code", "kind": "gh", "repo": "everycure-org/matrix",
     "q": "Open drug-disease score matrix: code release (says nothing about the licence of the DATA)",
     "vs": "p3b1/txgnn_matrix_outcomes_20261026.md; the data licence is watched by EveryCure-MATRIX-scores"},
    {"id": "EveryCure-MATRIX-scores", "kind": "hf", "repo": "everycure/matrix-scores",
     "q": "Has a licence for the scores table been stated (the stated reopening condition)?",
     "vs": "p3b1/txgnn_matrix_outcomes_20261026.md: scores table declared no licence on 2026-10-26"},
    {"id": "DGIdb", "kind": "gh", "repo": "dgidb/dgidb-v5",
     "q": "Drug-gene interaction source/licence changes", "vs": "framework/adapters + kg_thin_slice.py use it"},
    {"id": "Monarch-app", "kind": "gh", "repo": "monarch-initiative/monarch-app",
     "q": "Phenotype/disease KG API changes", "vs": "kg_thin_slice.py uses it"},
    {"id": "SigCom-LINCS", "kind": "json", "signal": "content",
     "url": "https://maayanlab.cloud/sigcom-lincs/metadata-api/libraries/count", "path": ["count"],
     "q": "Did the number of signature libraries change (a landing-page ETag only says the site was redeployed)?",
     "vs": "reversal route measured in gse156243/; `repurposing_adapter.py list` shows the adapters"},
    {"id": "iLINCS", "kind": "url", "url": "https://www.ilincs.org/", "signal": "availability",
     "q": "Reachability of the iLINCS portal", "vs": "`repurposing_adapter.py list` shows the iLINCS adapter"},
    {"id": "OpenTargets", "kind": "json", "method": "POST",
     "url": "https://api.platform.opentargets.org/api/v4/graphql",
     "body": '{"query":"{meta{dataVersion{year month iteration}}}"}',
     "path": ["data", "meta", "dataVersion"],
     "q": "New data release for WWOX target/association lookups", "vs": "framework/adapters/opentargets.py"},
    {"id": "ChEMBL", "kind": "json", "url": "https://www.ebi.ac.uk/chembl/api/data/status.json",
     "path": ["chembl_db_version"],
     "q": "New ChEMBL release (bioactivity for candidate drugs)", "vs": "framework/adapters/chembl.py"},
    {"id": "ChEMBL-FTP", "kind": "regex", "url": "https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/",
     "pattern": r'href="(chembl_\d+_sqlite\.tar\.gz)"',
     "q": "Which release file does the FTP `latest/` directory carry (cross-check of the API status version)?",
     "vs": "framework/adapters/chembl.py reads the API; a disagreement between the two probes is itself a finding"},
    {"id": "DGIdb-data", "kind": "json", "method": "POST", "digest": True, "url": "https://dgidb.org/api/graphql",
     "body": '{"query":"{sources{nodes{sourceDbName sourceDbVersion}}}"}', "path": ["data", "sources", "nodes"],
     "q": "Did any DGIdb source database change version (the repository probe above sees only code)?",
     "vs": "framework/adapters + kg_thin_slice.py read DGIdb; fingerprint = count + hash of the (source, version) records"},
    {"id": "openFDA-NDC", "kind": "json", "url": "https://api.fda.gov/drug/ndc.json?limit=1", "path": ["meta", "last_updated"],
     "q": "Date of the last openFDA NDC refresh (drug product / marketed-status catalogue)",
     "vs": "access-category and product lookups; one call, key-less, far below the 1,000/day limit"},
    {"id": "EveryCure-drug-list", "kind": "hf", "repo": "everycure/drug-list",
     "q": "Did the MATRIX drug list (CC BY 4.0 on its card) change content or terms? Lists are judged apart from scores, graph and code",
     "vs": "p3b1/txgnn_matrix_outcomes_20261026.md section 2.1 (1 935 rows, commit dc75f85 at 2026-10-13)"},
    {"id": "EveryCure-kg-nodes", "kind": "hf", "repo": "everycure/kg-nodes",
     "q": "Did the MATRIX knowledge-graph nodes change content or terms (graph terms are separate; upstream licences stay in force)?",
     "vs": "p3b1/txgnn_matrix_outcomes_20261026.md section 2.1"},
    {"id": "EveryCure-kg-edges", "kind": "hf", "repo": "everycure/kg-edges",
     "q": "Did the MATRIX knowledge-graph edges change content or terms (separate from nodes, scores, code)?",
     "vs": "p3b1/txgnn_matrix_outcomes_20261026.md section 2.1"},
    {"id": "GEO-LINCS-L1000", "kind": "json", "signal": "content",
     "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&retmode=json&retmax=0&term="
            "LINCS%5BAll+Fields%5D+AND+L1000%5BAll+Fields%5D",
     "path": ["esearchresult", "count"],
     "q": "New GEO records mentioning LINCS L1000 (count of matching GEO DataSets records; a count is not a signature)",
     "vs": "complements the SigCom library count: raw deposits versus processed libraries"},
    {"id": "MTBLS12344", "kind": "url", "signal": "availability",
     "url": "https://www.ebi.ac.uk/metabolights/ws/studies/public/study/MTBLS12344",
     "q": "Is the metabolomics dataset openly accessible (metabolic-signature question)?",
     "vs": "dated accessibility record: tool_survey_20261022.md; a status change is a reachability signal only"},
    {"id": "E-MTAB-14792", "kind": "url", "url": "https://www.ebi.ac.uk/biostudies/api/v1/studies/E-MTAB-14792",
     "signal": "availability", "q": "Is the E-MTAB-14792 dataset accessible?",
     "vs": "ebi_access_request_E-MTAB-14792_draft.md (not sent: no contact with curators); status change is a reachability signal only"},
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
        if tag is None:  # no releases: a light signal of real change is the default branch's latest commit
            branch = info.get("default_branch") or "HEAD"
            code3, _, body3 = opener(f"{base}/commits?per_page=1&sha={urllib.parse.quote(branch)}")
            if code3 == 200:
                commits = json.loads(body3 or b"[]")
                fp["last_commit"] = (commits[0]["commit"]["committer"]["date"] if commits else None)
            else:
                fp["last_commit"] = previous.get("fp", {}).get("last_commit")
        return {"fp": fp, "etag": hdr.get("ETag") or hdr.get("Etag")}
    if kind == "hf":  # a dataset's licence lives on its card, not in the code repository that built it
        base = f"https://huggingface.co/api/datasets/{entry['repo']}"
        code, _, body = opener(base)
        if code != 200:
            return {"error": f"dataset API HTTP {code}"}
        info = json.loads(body)
        card = info.get("cardData") or {}
        tags = [t for t in info.get("tags", []) if t.startswith("license:")]
        code2, _, body2 = opener(base + "/tree/main?limit=100")
        files = json.loads(body2) if code2 == 200 else []
        by_path = {f.get("path"): f.get("oid") for f in files if isinstance(f, dict)}
        fp = {"license": card.get("license") or (tags[0][8:] if tags else None), "gated": info.get("gated"),
              "licence_file": any(str(n).upper().startswith(("LICENSE", "LICENCE")) for n in by_path),
              "card_oid": by_path.get("README.md"), "sha": info.get("sha")}
        return {"fp": fp}
    if kind == "avail":  # reachability of one URL: one attempt, status only, an outage is not a change
        code, _, _ = opener(entry["url"], "GET", None)
        return {"fp": {"reachable": 0 < code < 400}}
    if kind == "json":
        code, hdr, body = opener(entry["url"], entry.get("method", "GET"), entry.get("body"))
        if code != 200:
            return {"error": f"HTTP {code}"}
        value = json.loads(body)
        for key in entry["path"]:
            value = value[key]
        if entry.get("digest"):  # a record list: fingerprint = count + hash of its canonical form
            return {"fp": {"n": len(value), "digest": digest(json.dumps(value, sort_keys=True))}}
        return {"fp": {"version": value}}
    if kind == "regex":  # names found in a plain listing; no match is an error (page changed), never "unchanged"
        code, _, body = opener(entry["url"], "GET", None)
        if code != 200:
            return {"error": f"HTTP {code}"}
        found = sorted(set(re.findall(entry["pattern"], body.decode("utf-8", "replace"))))
        if not found:
            return {"error": "pattern matched nothing (listing format changed?)"}
        return {"fp": {"match": ",".join(found)}}
    code, hdr, body = opener(entry["url"], "GET", None)
    if code == 0 or code >= 500:  # an outage is not a change
        return {"error": f"HTTP {code}"}
    low = {k.lower(): v for k, v in hdr.items()}
    fp = {"status": code}
    if code == 200 and entry.get("signal") != "availability":
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
        common = set(old.get("fp") or {}) & set(res["fp"])
        if old.get("fp") is None or not common:  # first sight, or the fingerprint was redefined: re-baseline
            rows.append({"id": entry["id"], "result": "BASELINE", "fp": res["fp"]})
        elif any(old["fp"][k] != res["fp"][k] for k in common):
            old_fp = {k: old["fp"][k] for k in common}
            detail = describe_change(old_fp, {k: res["fp"][k] for k in common})
            rows.append({"id": entry["id"], "result": "CHANGED", "detail": detail})
            avail = entry.get("signal") == "availability"
            selected.append({"id": entry["id"], "wwox_question": entry["q"], "contribution_vs_existing": entry["vs"],
                             "estimated_cost": "reading the change: minutes; any adoption: unestimated until triaged",
                             "licence": res["fp"].get("license") or "see source",
                             "proof": entry.get("repo") and f"https://github.com/{entry['repo']}/releases"
                                      or entry.get("url") or "", "detail": detail,
                             "outcome": ("AVAILABILITY SIGNAL (reachability changed; not a capability: check the "
                                         "reopening condition named above, then decide)" if avail else
                                         "TO_TRIAGE (a detected change is not a reading)")})
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


# ---------------------------------------------------------------------------------------------
# Configuration (overridable in <state dir>/scout_daily_config.json; unknown keys are ignored).
CONFIG = {"questions_per_run": 2, "open_slot": True, "version_checks": 3,
          "follow": {"max_teams": 6, "max_repos": 18, "max_per_team": 3, "deep_check_days": 7, "deep_per_run": 3}}


def load_config(directory: Path | None = None) -> dict:
    cfg = json.loads(json.dumps(CONFIG))
    try:
        user = json.loads(((directory or state_dir()) / "scout_daily_config.json").read_text())
    except (OSError, ValueError):
        return cfg
    for key, value in (user.items() if isinstance(user, dict) else []):
        if isinstance(value, dict) and isinstance(cfg.get(key), dict):
            cfg[key].update({a: b for a, b in value.items() if a in cfg[key] and type(b) is type(cfg[key][a])})
        elif key in cfg and type(value) is type(cfg[key]):
            cfg[key] = value
    return cfg


# ---------------------------------------------------------------------------------------------
# Context: the radar reads the REMOTE main, not whatever a checkout happens to hold.
REMOTE, BRANCH = "development", "main"
CONTEXT_FILES = ("disease-models/wwox/research/drug_repurposing/roadmap_current.md",
                 "disease-models/wwox/research/drug_repurposing/README.md",
                 "disease-models/wwox/research/capability_scout_log.md")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
REPO_RE = re.compile(r"(?:github\.com|huggingface\.co(?:/datasets|/spaces)?)/([\w.-]+/[\w.-]+)")


def git(args: list[str], cwd: Path = ROOT, timeout: int = 40):
    """(returncode, stdout). Read-only use only: ls-remote, rev-parse, cat-file, show, and an object-only fetch."""
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_SSH_COMMAND="ssh -o BatchMode=yes -o ConnectTimeout=10")
    try:
        done = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, timeout=timeout, env=env)
        return done.returncode, done.stdout
    except (OSError, subprocess.SubprocessError):
        return 127, ""


def parse_context_file(text: str) -> dict:
    heads = [line for line in text.splitlines() if line.startswith("#")]
    dates = sorted({d for line in heads for d in DATE_RE.findall(line)})
    updated = re.search(r"Updated\s+(\d{4}-\d{2}-\d{2})", text[:2000])
    repos = sorted({r.lower().rstrip(".") for r in REPO_RE.findall(text)})
    return {"updated": updated.group(1) if updated else None,
            "latest_heading_date": dates[-1] if dates else None, "repos": repos}


def resolve_context(cached: dict | None, runner=git, now: dt.datetime | None = None) -> dict:
    """Resolve the current remote main SHA and read the context files AT THAT REVISION (git show; no checkout is
    touched). Unchanged blobs and an unchanged SHA reuse the cache. If the SHA cannot be verified the result says
    so in `freshness_limit`. An old CURRENT/Updated heading never outranks later dated evidence (`outranked_by`)."""
    cached = cached or {}
    now = now or dt.datetime.now(dt.timezone.utc)
    ctx = {"checked_at": now.isoformat(timespec="seconds"), "remote_ref": f"{REMOTE}/{BRANCH}", "files": {},
           "freshness_limit": None, "cache": "refreshed", "main_sha": None}
    code, out = runner(["ls-remote", REMOTE, f"refs/heads/{BRANCH}"])
    sha = out.split()[0] if code == 0 and out.strip() else None
    old_files = cached.get("files") or {}
    if not sha:
        local_code, local = runner(["rev-parse", f"{REMOTE}/{BRANCH}"])
        if cached.get("main_sha"):
            ctx.update(main_sha=cached["main_sha"], files=old_files, cache="stale_reused")
            ctx["freshness_limit"] = (f"remote main NOT verified (git ls-remote failed); context is the cached read of "
                                      f"{cached['main_sha'][:12]} from {cached.get('checked_at')}")
            return _outrank(ctx)
        if local_code != 0 or not local.strip():
            ctx["freshness_limit"] = "remote main NOT verified and no local remote-tracking ref: context unavailable"
            return ctx
        sha = local.strip()
        ctx["freshness_limit"] = (f"remote main NOT verified (git ls-remote failed); read the local "
                                  f"{REMOTE}/{BRANCH} ref {sha[:12]}, which may lag the true remote")
    ctx["main_sha"] = sha
    if cached.get("main_sha") == sha and old_files:
        ctx.update(files=old_files, cache="hit")
        return _outrank(ctx)
    if runner(["cat-file", "-e", f"{sha}^{{commit}}"])[0] != 0:
        runner(["fetch", "--quiet", "--no-write-fetch-head", REMOTE, BRANCH])  # objects only: no ref, no worktree change
    if runner(["cat-file", "-e", f"{sha}^{{commit}}"])[0] != 0:
        ctx.update(files=old_files, cache="stale_reused")
        extra = f"; context is the cached read of {cached['main_sha'][:12]}" if cached.get("main_sha") else ""
        ctx["freshness_limit"] = f"remote main is {sha[:12]} but its objects are not available locally{extra}"
        return _outrank(ctx)
    reused = 0
    for path in CONTEXT_FILES:
        code, blob = runner(["rev-parse", f"{sha}:{path}"])
        blob = blob.strip()
        if code != 0 or not blob:
            ctx["files"][path] = {"error": "absent at this revision"}
        elif (old_files.get(path) or {}).get("blob") == blob:
            ctx["files"][path] = old_files[path]
            reused += 1
        else:
            code, text = runner(["show", f"{sha}:{path}"])
            ctx["files"][path] = ({"blob": blob, **parse_context_file(text)} if code == 0
                                  else {"error": "git show failed"})
    ctx["blobs_reused"] = reused
    return _outrank(ctx)


def _outrank(ctx: dict) -> dict:
    road = ctx["files"].get(CONTEXT_FILES[0]) or {}
    dated = road.get("updated") or road.get("latest_heading_date")
    later = sorted((f.get("latest_heading_date"), p.rsplit("/", 1)[-1]) for p, f in ctx["files"].items()
                   if p != CONTEXT_FILES[0] and f.get("latest_heading_date") and dated
                   and f["latest_heading_date"] > dated)
    ctx["roadmap_dated"] = dated
    ctx["outranked_by"] = [f"{name} ({date})" for date, name in later]
    return ctx


def known_idents(watch, follow: dict | None, ctx: dict | None) -> set:
    """Resources the repository already probes, follows or records: a hit on one is not a new discovery."""
    ids = {w["repo"].lower() for w in watch if w.get("repo")}
    ids |= {e["repo"].lower() for e in (follow or {}).get("entries", [])}
    for f in ((ctx or {}).get("files") or {}).values():
        ids.update(f.get("repos", []))
    return ids


# ---------------------------------------------------------------------------------------------
# Followed teams/repos: internal monitoring of PUBLIC projects only (no contact, no social action, no
# collaborator expansion). Limits are configuration; slots are never filled to reach a number.
FOLLOW_SEED = [
    {"team": "mims-harvard", "repo": "mims-harvard/ToolUniverse", "relevance": 3,
     "source": "WATCH ToolUniverse; tooluniverse_capability_test_20261026.md",
     "reason": "live-lookup layer tried on a capability the adapters lack",
     "reopen": "a capability the adapters lack becomes available, or terms change"},
    {"team": "mims-harvard", "repo": "mims-harvard/TxGNN", "relevance": 3,
     "source": "WATCH TxGNN-code; p3b1/txgnn_matrix_outcomes_20261026.md",
     "reason": "REASONED WAIT on a deployable checkpoint",
     "reopen": "a deployable full_graph checkpoint or per-disease predictions are retrievable"},
    {"team": "everycure-org", "repo": "everycure-org/matrix", "relevance": 3,
     "source": "WATCH EveryCure-MATRIX-code; p3b1/txgnn_matrix_outcomes_20261026.md",
     "reason": "open drug-disease score matrix, inconclusive trial",
     "reopen": "a stated licence for the scores table, or a code/data release"},
]


def follow_seed(today: str = "2026-11-01") -> dict:
    return {"entries": [dict(e, status="active", added=today, last_deep=None, fp=None) for e in FOLLOW_SEED]}


def _rank(entry: dict):
    return (entry.get("relevance", 0), entry.get("added", ""))  # the least relevant, then the oldest, is replaced first


def follow_add(follow: dict, new: dict, limits: dict, today: str) -> tuple[str, str]:
    """Add a followed repo under the limits. Returns (added|replaced|refused, detail). When full, the least relevant
    entry is SUSPENDED (source, reason and reopen condition kept) only if the newcomer is more relevant."""
    for key in ("team", "repo", "source", "reason", "reopen"):
        if not str(new.get(key, "")).strip():
            return "refused", f"missing {key}"
    new = dict(new, status="active", added=today, last_deep=None, fp=None)
    new["relevance"] = int(new.get("relevance", 1))
    active = [e for e in follow["entries"] if e["status"] == "active"]
    if any(e["repo"].lower() == new["repo"].lower() for e in active):
        return "refused", "already followed"
    victims: list[dict] = []

    def pick(pool: list[dict]):
        victim = min(pool, key=_rank)
        return victim if victim["relevance"] < new["relevance"] else None

    same_team = [e for e in active if e["team"] == new["team"]]
    if len(same_team) >= limits["max_per_team"]:
        victim = pick(same_team)
        if victim is None:
            return "refused", f"team {new['team']} is at {limits['max_per_team']} repos and none is less relevant"
        victims.append(victim)
    rest = [e for e in active if e not in victims]
    teams = {e["team"] for e in rest}
    if new["team"] not in teams and len(teams) >= limits["max_teams"]:
        weakest = min(teams, key=lambda t: (max(e["relevance"] for e in rest if e["team"] == t), t))
        if max(e["relevance"] for e in rest if e["team"] == weakest) >= new["relevance"]:
            return "refused", f"{limits['max_teams']} teams followed and none is less relevant"
        victims += [e for e in rest if e["team"] == weakest]
    rest = [e for e in active if e not in victims]
    if len(rest) + 1 > limits["max_repos"]:
        victim = pick(rest)
        if victim is None:
            return "refused", f"{limits['max_repos']} repos followed and none is less relevant"
        victims.append(victim)
    for victim in victims:
        victim.update(status="suspended", suspended_at=today, suspended_for=new["repo"])
    follow["entries"].append(new)
    suspended = [e for e in follow["entries"] if e["status"] == "suspended"]
    for old in suspended[:-30]:  # bounded history; the newest 30 suspensions keep source/reason/reopen
        follow["entries"].remove(old)
    return ("replaced" if victims else "added"), (
        "suspended " + ", ".join(v["repo"] for v in victims) if victims else "slot free")


def follow_due(follow: dict, now: dt.datetime, days: int, limit: int) -> list[dict]:
    """Active repos not deep-checked for `days`, never-checked first, then oldest; at most `limit` per run."""
    cutoff = (now - dt.timedelta(days=days)).isoformat()
    due = [e for e in follow["entries"] if e["status"] == "active" and (e.get("last_deep") or "") < cutoff]
    return sorted(due, key=lambda e: e.get("last_deep") or "")[:limit]


# ---------------------------------------------------------------------------------------------
# Signal -> examination -> trial -> decision -> integration. A log line is not an examination; adoption in a plan
# is not a verified implementation.
STAGES = {"signal": {"signalled"}, "examination": {"examined"}, "trial": {"not_needed", "trialled"},
          "decision": {"adopt", "defer", "reject", "reopen_later"},
          "integration": {"adopted_in_plan", "implemented_unverified", "verified"}}
EVIDENCE = {"source_read", "test_run", "record_file", "session_check"}  # "log_line" is deliberately absent


def trace_event(trace: dict, key: str, stage: str, state: str, kind: str | None = None, ref: str | None = None,
                at: str = "") -> tuple[bool, str]:
    if stage not in STAGES or state not in STAGES[stage]:
        return False, f"unknown stage/state {stage}/{state}"
    rec = trace.setdefault(key, {"history": []})
    done = {h["stage"]: h["state"] for h in rec["history"]}
    if stage != "signal" and "signal" not in done:
        return False, "no signal recorded for this key"
    needs_evidence = (stage == "examination" or (stage == "trial" and state == "trialled")
                      or (stage == "integration" and state in ("implemented_unverified", "verified")))
    if needs_evidence and (kind not in EVIDENCE or not ref):
        return False, ("a log line alone does not prove evaluation" if kind == "log_line"
                       else "an evidence kind (source_read|test_run|record_file|session_check) and a ref are required")
    if stage == "trial" and state == "trialled" and kind != "test_run":
        return False, "a trial needs a test_run"
    if stage == "integration" and state == "verified" and kind not in ("test_run", "record_file"):
        return False, "verified needs a test_run or record_file"
    if stage == "decision" and "examination" not in done:
        return False, "no examination recorded"
    if stage == "integration" and done.get("decision") != "adopt":
        return False, "integration needs decision adopt"
    rec["history"].append({"stage": stage, "state": state, "kind": kind, "ref": ref, "at": at})
    return True, "recorded"


def trace_summary(trace: dict) -> dict:
    out = {}
    for key, rec in trace.items():
        done = {h["stage"]: h["state"] for h in rec["history"]}
        out[key] = {"furthest": next((s for s in reversed(list(STAGES)) if s in done), None), "states": done,
                    "verified_implementation": done.get("integration") == "verified"}
    return out


# ---------------------------------------------------------------------------------------------
# External discovery: rotating priority questions, each tied to a decision. Capability / benchmark questions do not
# require the word WWOX. `kw` is the plain keyword query used for GitHub, Hugging Face and the Nature portfolio
# (it defaults to the gap text); `epmc` is an optional Europe PMC complement. Edit a question when its gap closes.
THEMES = [
    {"id": "sdr-enzyme-assay", "category": "scientific inputs", "gap": "WWOX SDR domain: no activity assay or substrate known",
     "decision": "whether an assay/substrate route can replace the current inference-only SDR statement",
     "hf": "oxidoreductase", "kw": "short-chain dehydrogenase orphan substrate assay",
     "epmc": '(TITLE_ABS:WWOX OR TITLE_ABS:SDR16C5 OR TITLE_ABS:"short-chain dehydrogenase") AND '
             '(TITLE_ABS:"substrate screening" OR TITLE_ABS:"activity assay" OR TITLE_ABS:"orphan" OR '
             'TITLE_ABS:"catalytic activity") AND TITLE_ABS:(WWOX OR SDR)',
     "gh": "orphan oxidoreductase substrate prediction"},
    {"id": "isr-atf4-epilepsy", "category": "matching/pharmacology",
     "gap": "ISR/ATF4 modulators in epilepsy or DEE (candidate-class evidence is thin)",
     "decision": "whether the ISR candidate class moves in the pharmacology comparison (R5)",
     "hf": "epilepsy", "kw": "integrated stress response epilepsy",
     "epmc": '(TITLE_ABS:"integrated stress response" OR TITLE_ABS:ISRIB OR TITLE_ABS:ATF4 OR TITLE_ABS:GCN2) AND '
             '(TITLE_ABS:epilepsy OR TITLE_ABS:seizure OR TITLE_ABS:"epileptic encephalopathy")',
     "gh": None},
    {"id": "residual-function-chaperone", "category": "experiments",
     "gap": "residual-function / chaperone rescue of missense alleles",
     "decision": "whether a residual-function experiment enters the experiment ledger",
     "hf": "chaperone", "kw": "pharmacological chaperone missense stability",
     "epmc": '(TITLE_ABS:"pharmacological chaperone" OR TITLE_ABS:"residual function") AND '
             '(TITLE_ABS:"epileptic encephalopathy" OR TITLE_ABS:"neurodevelopmental") AND TITLE_ABS:missense',
     "gh": "variant protein stability ddg"},
    {"id": "dee-drug-response-data", "category": "databases",
     "gap": "paediatric DEE drug-response datasets (a gold set does not exist)",
     "decision": "whether an evaluation set for R3 exists or must be assembled",
     "hf": "epilepsy", "kw": "epilepsy antiseizure drug response dataset",
     "epmc": 'TITLE_ABS:"developmental and epileptic encephalopathy" AND (TITLE_ABS:"treatment response" OR '
             'TITLE_ABS:"drug response" OR TITLE_ABS:"antiseizure") AND (TITLE_ABS:dataset OR TITLE_ABS:registry '
             'OR TITLE_ABS:database)',
     "gh": "epilepsy antiseizure dataset"},
    {"id": "pdh-assay", "category": "scientific inputs", "gap": "a PDH-specific measure (activity, phosphorylation or flux) is missing",
     "decision": "whether the PDH question gets a measurable endpoint",
     "hf": "pyruvate", "kw": "pyruvate dehydrogenase activity phosphorylation biosensor",
     "epmc": 'TITLE_ABS:"pyruvate dehydrogenase" AND (TITLE_ABS:"activity assay" OR TITLE_ABS:phosphorylation OR '
             'TITLE_ABS:flux OR TITLE_ABS:biosensor) AND (TITLE_ABS:neuron* OR TITLE_ABS:epilep* OR TITLE_ABS:fibroblast*)',
     "gh": None},
    {"id": "assertion-extraction", "category": "tools/capabilities",
     "gap": "module blind spot: typed drug assertions from papers and name-to-compound linking",
     "decision": "whether an existing extractor replaces a hand-built step", "hf": "relation-extraction", "kw": "drug entity linking relation extraction",
     "epmc": None, "gh": "drug entity linking"},
    {"id": "neuron-perturbation-signatures", "category": "databases",
     "gap": "context-matched neuronal perturbation signatures for reversal queries",
     "decision": "whether R3 can use a neuron-matched signature set instead of a generic one",
     "hf": "perturbation", "kw": "perturbation signature neuron reversal",
     "epmc": '(TITLE_ABS:"perturbation signature*" OR TITLE_ABS:L1000 OR TITLE_ABS:"connectivity map") AND '
             '(TITLE_ABS:neuron* OR TITLE_ABS:iPSC) AND (TITLE_ABS:reversal OR TITLE_ABS:repurposing)',
     "gh": "lincs signature reversal"},
    {"id": "repurposing-benchmarks", "category": "prediction/evaluation",
     "gap": "independent evaluations of drug-repurposing and signature-reversal methods (no WWOX needed)",
     "decision": "whether the R3 reference comparison keeps its method set",
     "hf": "repurposing", "kw": "drug repurposing benchmark evaluation",
     "epmc": 'TITLE_ABS:"drug repurposing" AND TITLE_ABS:(benchmark OR "independent evaluation" OR "prospective validation")',
     "gh": "drug repurposing benchmark"},
    {"id": "repurposing-negative-results", "category": "negative results",
     "gap": "reported failures or leakage in repurposing predictions (counter-evidence to our own methods)",
     "decision": "whether a method in use needs a leakage/confound check before its output is trusted",
     "hf": "repurposing", "kw": "drug repurposing data leakage failure",
     "epmc": 'TITLE_ABS:"drug repurposing" AND TITLE_ABS:(leakage OR "negative results" OR "failed to replicate" OR confound*)',
     "gh": None},
    {"id": "agent-research-patterns", "category": "Scientist/Orchestrator patterns",
     "gap": "agentic research workflows with audit trails and evaluation of their own errors",
     "decision": "whether a handoff/record pattern replaces an existing LEGEND step",
     "hf": "agent", "kw": "agent scientific workflow provenance evaluation", "epmc": None, "gh": "agentic research workflow provenance"},
    {"id": "open-compound-resources", "category": "databases",
     "gap": "open compound-target-effect resources beyond ChEMBL and DGIdb with stated terms",
     "decision": "whether the R2 catalogue gains or drops a source", "hf": "bioactivity", "kw": "compound target bioactivity open database",
     "epmc": None, "gh": "compound target interaction database"},
]
OPEN_QUERIES = ["rare disease drug repurposing", "neurodevelopmental disorder compound screening",
                "biomedical agent benchmark", "knowledge graph drug disease prediction"]  # the room for unexpected finds
CATEGORY_ROADMAP = {"errors/gaps": "R12", "tools/capabilities": "R9", "databases": "R2", "matching/pharmacology": "R5",
                    "prediction/evaluation": "R3", "scientific inputs": "R1/R8", "negative results": "R4",
                    "experiments": "R6/R7", "Scientist/Orchestrator patterns": "R9/R12", "unexpected": "R9"}
NATURE_PREFIXES = ("nature", "npj", "scientific", "communications")  # Nature portfolio container titles
CHANNELS = ("github", "huggingface", "nature", "europepmc")  # the first three are mandatory; europepmc complements
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
GH_API = "https://api.github.com"
GH_SEARCH = GH_API + "/search/repositories"
HF_API = "https://huggingface.co/api"
CROSSREF = "https://api.crossref.org/works"
SHOW = 3  # per source per run; only what is shown is marked seen, the rest waits for the next rotation
NEW_WINDOW_DAYS = 730
CLAIM_LABELS = ("declared", "implemented", "tested_by_authors", "independently_reproduced",
                "verified_by_this_session", "transferable_to_wwox")


def _years_ago(now: dt.datetime, days: int) -> str:
    return (now - dt.timedelta(days=days)).date().isoformat()


def _clean(text: str | None, limit: int = 140) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(text or ""))[:limit]


def claim_labels(item: dict) -> dict:
    """Everything a search hit supports is `declared`; the rest stays `unknown` until someone does the work."""
    labels = {name: "unknown" for name in CLAIM_LABELS}
    labels["declared"] = "yes: by the title/description/metadata only"
    labels["verified_by_this_session"] = "metadata retrieved (existence, dates, licence field); nothing run or read"
    if (item.get("versions") or {}).get("last_commit"):
        labels["implemented"] = "code exists (a commit was seen); behaviour not run"
    return labels


def repo_versions(full_name: str, opener=http) -> dict:
    """Last commit of the DEFAULT branch and the latest release, kept apart. 404 on releases = none published."""
    out = {"last_commit": None, "latest_release": None, "errors": []}
    code, _, body = opener(f"{GH_API}/repos/{full_name}/commits?per_page=1")
    try:
        first = json.loads(body)[0] if code == 200 else None
        if first:
            out["last_commit"] = {"sha": first["sha"][:12], "date": first["commit"]["committer"]["date"]}
        elif code != 200:
            out["errors"].append(f"{full_name} commits HTTP {code}")
    except (ValueError, KeyError, IndexError, TypeError):
        out["errors"].append(f"{full_name} commits unparseable")
    code, _, body = opener(f"{GH_API}/repos/{full_name}/releases/latest")
    if code == 404:
        out["latest_release"] = "none published"
    elif code != 200:
        out["errors"].append(f"{full_name} releases HTTP {code}")
    else:
        try:
            rel = json.loads(body)
            out["latest_release"] = {"tag": rel.get("tag_name"), "date": (rel.get("published_at") or "")[:10]}
        except ValueError:
            out["errors"].append(f"{full_name} releases unparseable")
    return out


def hf_versions(kind: str, ident: str, opener=http) -> dict:
    code, _, body = opener(f"{HF_API}/{kind}/{ident}")
    if code != 200:
        return {"errors": [f"{ident} card HTTP {code}"]}
    try:
        data = json.loads(body)
        files = [s.get("rfilename") for s in data.get("siblings", [])]
        return {"revision": (data.get("sha") or "")[:12], "modified": (data.get("lastModified") or "")[:10],
                "card_licence": (data.get("cardData") or {}).get("license"), "gated": data.get("gated"),
                "files": {"count": len(files), "first": files[:5]}, "errors": []}
    except (ValueError, AttributeError, TypeError):
        return {"errors": [f"{ident} card unparseable"]}


def discover_theme(theme: dict, seen: dict, opener=http, now: dt.datetime | None = None,
                   known=frozenset(), budget: dict | None = None) -> dict:
    """One question across the channels: GitHub, Hugging Face (models, datasets, Spaces), Nature portfolio (Crossref
    metadata) and, as a complement, Europe PMC. Returns items plus a per-channel record; `seen` is updated.
    Items that are known resources (probed, followed or already in the log) are counted apart and never shown."""
    now = now or dt.datetime.now(dt.timezone.utc)
    budget = budget if budget is not None else {"n": 0}
    kw = theme.get("kw") or theme["gap"]
    chans = {c: {"calls": 0, "errors": [], "new": 0, "known": 0, "known_names": []} for c in CHANNELS}
    items: list[dict] = []
    since = _years_ago(now, NEW_WINDOW_DAYS)

    def fetch(chan: str, label: str, url: str):
        chans[chan]["calls"] += 1
        code, _, body = opener(url)
        if code != 200:
            chans[chan]["errors"].append(f"{theme['id']} {label} HTTP {code}")
            return None
        try:
            return json.loads(body)
        except ValueError:
            chans[chan]["errors"].append(f"{theme['id']} {label} unparseable answer")
            return None

    def take(chan: str, fresh: list[dict]) -> None:
        keep = []
        for it in fresh:
            if it["key"] in seen:
                continue
            if it.get("ident") and it["ident"] in known:
                chans[chan]["known"] += 1
                chans[chan]["known_names"].append(it["ident"])
                continue
            keep.append(it)
        keep = keep[:SHOW]
        seen.update({i["key"]: now.date().isoformat() for i in keep})
        for it in keep:
            it["channel"] = chan
        chans[chan]["new"] = len(keep)
        items.extend(keep)

    def guarded(chan: str, label: str, url: str, build) -> list[dict]:
        data = fetch(chan, label, url)
        if data is None:
            return []
        try:
            return build(data)
        except (KeyError, AttributeError, TypeError, ValueError):
            chans[chan]["errors"].append(f"{theme['id']} {label} unexpected answer shape")
            return []

    if theme.get("epmc"):
        query = f"({theme['epmc']}) AND FIRST_PDATE:[{since} TO {now.date().isoformat()}]"

        def epmc_items(data):
            out = []
            for rec in data["resultList"]["result"]:
                preprint = rec.get("source") == "PPR"
                out.append({"key": f"epmc:{rec.get('source')}:{rec.get('id')}", "kind": "preprint" if preprint else "paper",
                            "title": _clean(rec.get("title")), "when": rec.get("firstPublicationDate"),
                            "venue": rec.get("journalTitle") or rec.get("source"), "open": rec.get("isOpenAccess"),
                            "doi": (rec.get("doi") or "").lower() or None,
                            "versions": {"published": rec.get("firstPublicationDate"),
                                         "editorial_status": "preprint (not peer reviewed)" if preprint else "published record",
                                         "corrections": "not checked", "supplements": "not checked"},
                            "licences": {"article": "unknown (not read)"},
                            "url": f"https://europepmc.org/article/{rec.get('source')}/{rec.get('id')}"})
            return out
        take("europepmc", guarded("europepmc", "europepmc",
                                  f"{EPMC}?format=json&resultType=lite&pageSize=25&query=" + urllib.parse.quote(query),
                                  epmc_items))

    gh_terms = " ".join((theme.get("gh") or kw).split()[:3])  # repository search ANDs every word: keep it short
    gh_query = f"{gh_terms} pushed:>{since} archived:false fork:false"

    def gh_items(data):
        out = []
        for repo in data["items"]:
            lic = (repo.get("license") or {}).get("spdx_id") or "none stated"
            out.append({"key": f"gh:{repo['full_name']}", "ident": repo["full_name"].lower(), "kind": "repository",
                        "title": repo["full_name"], "description": _clean(repo.get("description")),
                        "licences": {"code": lic}, "licence": lic, "when": (repo.get("pushed_at") or "")[:10],
                        "default_branch": repo.get("default_branch"), "popularity": {"stars": repo.get("stargazers_count")},
                        "url": repo.get("html_url")})
        out.sort(key=lambda r: r["when"], reverse=True)  # recency, not stars: popularity is not quality
        return out
    take("github", guarded("github", "github", f"{GH_SEARCH}?per_page=15&sort=updated&q=" + urllib.parse.quote(gh_query),
                           gh_items))

    hf_term = theme.get("hf") or max(kw.split(), key=len)  # Hugging Face search matches names/tags: one short term
    scope = {"models": ("model", "weights"), "datasets": ("dataset", "data"), "spaces": ("space", "service")}
    hf_all: list[dict] = []
    for kind, (word, lic_scope) in scope.items():
        def hf_items(data, kind=kind, word=word, lic_scope=lic_scope):
            if not isinstance(data, list):
                raise TypeError("not a list")
            out = []
            for rec in data:
                lic = next((t.split(":", 1)[1] for t in rec.get("tags", []) if t.startswith("license:")), None)
                modified = (rec.get("lastModified") or "")[:10]
                if modified and modified < since:
                    continue
                path = {"models": "", "datasets": "datasets/", "spaces": "spaces/"}[kind]
                out.append({"key": f"hf:{kind}:{rec['id']}", "ident": rec["id"].lower(), "kind": word, "hf_kind": kind,
                            "title": rec["id"], "licences": {lic_scope: lic or "none stated"}, "licence": lic or "none stated",
                            "when": modified, "popularity": {"downloads": rec.get("downloads"), "likes": rec.get("likes")},
                            "versions": {"modified": modified}, "url": f"https://huggingface.co/{path}{rec['id']}"})
            return out
        hf_all += guarded("huggingface", f"huggingface {kind}",
                          f"{HF_API}/{kind}?search={urllib.parse.quote(hf_term)}&sort=lastModified&direction=-1&limit=10", hf_items)
    hf_all.sort(key=lambda r: r["when"], reverse=True)
    take("huggingface", hf_all)

    def nature_items(data):
        out = []
        for rec in data["message"]["items"]:
            venue = (rec.get("container-title") or [""])[0]
            if not venue.lower().startswith(NATURE_PREFIXES):
                continue
            title = _clean((rec.get("title") or [""])[0])
            parts = (rec.get("issued") or {}).get("date-parts", [[None]])[0]
            when = "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts) if p)
            lic = sorted({(x.get("URL") or "")[:80] for x in rec.get("license", [])})
            out.append({"key": f"nature:{rec['DOI'].lower()}", "ident": rec["DOI"].lower(), "kind": "paper", "title": title,
                        "doi": rec["DOI"].lower(), "venue": venue, "when": when,
                        "versions": {"published": when, "editorial_status": rec.get("type"),
                                     "corrections": "correction notice" if re.search(
                                         r"correction|retraction|expression of concern", title, re.I) else "none seen in metadata",
                                     "supplements": "not checked",
                                     "preprint_relation": bool((rec.get("relation") or {}).get("has-preprint"))},
                        "licences": {"article": ", ".join(lic) or "unknown"}, "url": "https://doi.org/" + rec["DOI"]})
        out.sort(key=lambda r: r["when"], reverse=True)
        return out
    nature_url = (f"{CROSSREF}?query.bibliographic={urllib.parse.quote(kw)}&rows=40&select=DOI,title,container-title,issued,"
                  f"type,license,relation&filter=prefix:10.1038,from-pub-date:{since},type:journal-article")
    take("nature", guarded("nature", "nature (Crossref)", nature_url, nature_items))

    for it in items:  # version / card detail for a small budget of shown items (read-only public endpoints)
        if budget["n"] <= 0:
            break
        if it["channel"] == "github":
            budget["n"] -= 1
            res = repo_versions(it["title"], opener)
            chans["github"]["calls"] += 2
            chans["github"]["errors"] += res.pop("errors")
            it["versions"] = dict(res, default_branch=it.get("default_branch"))
        elif it["channel"] == "huggingface":
            budget["n"] -= 1
            res = hf_versions(it["hf_kind"], it["title"], opener)
            chans["huggingface"]["calls"] += 1
            chans["huggingface"]["errors"] += res.pop("errors")
            it["versions"] = dict(it.get("versions") or {}, **res)
    for it in items:
        it["claims"] = claim_labels(it)
        it["checks"] = {"counter_evidence": "not searched", "leakage": "not assessed", "shared_origin": "not assessed",
                        "context_mismatch": "not assessed (a search hit says nothing about WWOX context)"}
    return {"theme": theme["id"], "gap": theme["gap"], "category": theme.get("category", "unexpected"),
            "decision": theme.get("decision", "unstated"), "items": items, "channels": chans,
            "errors": [e for c in chans.values() for e in c["errors"]]}


def _norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (title or "").lower())


def dedup(items: list[dict]) -> list[dict]:
    """Collapse papers/code/datasets/mirrors: same DOI, same normalised title, or same repo name (code, data, model or
    Space sharing the last path segment, 6+ chars) count ONCE; the others are kept as `mirrors`."""
    kept: list[dict] = []
    index: dict[tuple, dict] = {}
    for it in items:
        keys = []
        if it.get("doi"):
            keys.append(("doi", it["doi"]))
        if it["kind"] in ("paper", "preprint") and len(_norm_title(it["title"])) > 20:
            keys.append(("title", _norm_title(it["title"])))
        if it["kind"] in ("repository", "model", "dataset", "space"):
            tail = it["title"].rsplit("/", 1)[-1].lower()
            if len(tail) >= 6:
                keys.append(("name", tail))
        hit = next((k for k in keys if k in index), None)
        if hit:
            first = index[hit]
            first.setdefault("mirrors", []).append({"url": it["url"], "channel": it["channel"], "kind": it["kind"],
                                                    "basis": hit[0]})
            first["checks"]["shared_origin"] = "possible shared origin: mirrors merged and counted once (a name match is a hint)"
            continue
        kept.append(it)
        for k in keys:
            index.setdefault(k, it)
    return kept


def discover(dstate: dict, themes=THEMES, opener=http, now: dt.datetime | None = None, only: str | None = None,
             pause: float = 0, per_run: int = 1, open_slot: bool = False, known=frozenset(), deep: int = 0):
    """The daily search: the next `per_run` questions in rotation (plus an open slot), once per calendar day (`only`:
    one theme id or 'all'). The followed-repo watchlist never limits it. Returns (result | None, new_state)."""
    now = now or dt.datetime.now(dt.timezone.utc)
    today = now.date().isoformat()
    state = {"cursor": dstate.get("cursor", 0), "last_day": dstate.get("last_day"), "seen": dict(dstate.get("seen", {}))}
    if only is None:
        if state["last_day"] == today:
            return None, state
        n = max(1, min(per_run, len(themes)))
        chosen = [themes[(state["cursor"] + i) % len(themes)] for i in range(n)]
        state["cursor"] = (state["cursor"] + n) % len(themes)
        state["last_day"] = today
        if open_slot:
            chosen.append({"id": "open-slot", "category": "unexpected", "gap": "unplanned find: no gap assumed",
                           "decision": "whether it reveals a question we did not know to ask",
                           "kw": OPEN_QUERIES[now.toordinal() % len(OPEN_QUERIES)], "epmc": None, "gh": None})
    else:
        chosen = [t for t in themes if only == "all" or t["id"] == only]
    budget = {"n": deep}
    results = []
    for number, t in enumerate(chosen):
        if number and pause:
            time.sleep(pause)  # the unauthenticated GitHub search allows about 10 calls a minute
        results.append(discover_theme(t, state["seen"], opener, now, known, budget))
    kept = dedup([i for r in results for i in r["items"]])
    kept_ids = {id(i) for i in kept}
    duplicates = {c: 0 for c in CHANNELS}
    for r in results:
        for i in r["items"]:
            if id(i) not in kept_ids:
                duplicates[i["channel"]] += 1
        r["items"] = [i for i in r["items"] if id(i) in kept_ids]
    if len(state["seen"]) > 3000:  # bounded cache: keep the newest 2000 keys
        for key in sorted(state["seen"], key=state["seen"].get)[:len(state["seen"]) - 2000]:
            del state["seen"][key]
    return {"themes": results, "new_items": len(kept), "channels": channel_summary(results, duplicates),
            "questions": [{"id": r["theme"], "category": r["category"], "question": r["gap"], "decision": r["decision"]}
                          for r in results]}, state


def channel_summary(results: list[dict], duplicates: dict | None = None) -> dict:
    """Per channel: outcome in {error, no_news, delta} (europepmc may also be not_queried). An error is never
    reported as 'no news'; partial errors stay listed next to a delta. Known resources are not news."""
    summary = {}
    for chan in CHANNELS:
        calls = sum(r["channels"][chan]["calls"] for r in results)
        errors = [e for r in results for e in r["channels"][chan]["errors"]]
        new = sum(sum(1 for i in r["items"] if i["channel"] == chan) for r in results)
        known = sorted({n for r in results for n in r["channels"][chan]["known_names"]})
        if calls == 0:
            outcome = "not_queried"
        elif len(errors) >= calls:
            outcome = "error"
        else:
            outcome = "delta" if new else "no_news"
        summary[chan] = {"outcome": outcome, "calls": calls, "new": new, "errors": errors, "known_resources": known[:10],
                         "duplicates": (duplicates or {}).get(chan, 0)}
    return summary


def item_line(i: dict) -> str:
    v = i.get("versions") or {}
    bits = [f"{i['when'] or '?'}"]
    if i.get("licence"):
        bits.append(i["licence"])
    if v.get("last_commit"):
        bits.append(f"default-branch head {v['last_commit']['sha']} {v['last_commit']['date'][:10]}")
        rel = v.get("latest_release")
        bits.append("release " + (f"{rel['tag']} {rel['date']}" if isinstance(rel, dict) else str(rel)))
    if v.get("revision"):
        bits.append(f"revision {v['revision']}, {v['files']['count']} files")
    if i["kind"] in ("paper", "preprint") and v.get("editorial_status"):
        bits.append(str(v["editorial_status"]))
    mirrors = f" [+{len(i['mirrors'])} mirror(s) merged]" if i.get("mirrors") else ""
    return f"[{i['kind']}/{i['channel']}] {i['title']} ({', '.join(bits)}){mirrors} {i['url']}"


def discovery_entries(result: dict, when: str) -> list[dict]:
    out = []
    for res in result["themes"]:
        if not res["items"]:
            continue
        out.append({"id": f"Discovery:{res['theme']}", "wwox_question": res["gap"],
                    "question_category": res.get("category"), "decision": res.get("decision"),
                    "roadmap": CATEGORY_ROADMAP.get(res.get("category"), "R9"),
                    "contribution_vs_existing": "unchecked: a search hit is the first look (no relevance scoring)",
                    "estimated_cost": "screening: minutes; adoption: unestimated until read (licence, version, provenance)",
                    "licence": "per item and per part (code / data / weights / service / article), shown where stated",
                    "detail": "; ".join(item_line(i) for i in res["items"]),
                    "keys": [i["key"] for i in res["items"]],
                    "proof": "GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key",
                    "use": "none proposed until a claim is examined",
                    "test": "read the source; reproduce one stated result on public inputs before any adoption",
                    "outcome": "TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)"})
    return out



def radar_status(directory: Path | None = None, now: dt.datetime | None = None) -> dict:
    """Non-blocking summary of the last run for session start; never raises."""
    directory = directory or state_dir()
    now = now or dt.datetime.now(dt.timezone.utc)
    out = {"state_dir": str(directory), "status": "NO_REPORT"}
    try:
        report = json.loads((directory / "scout_daily.json").read_text())
        ran = dt.datetime.fromisoformat(report["run_at"])
        age = (now - ran).total_seconds() / 3600
        out.update({"status": "STALE" if age > 36 else "OK", "last_run": report["run_at"], "age_hours": round(age, 1),
                    "verdict": report.get("verdict"), "errors": report.get("errors", []),
                    "to_examine": [s["id"] for s in report.get("selected", [])],
                    "discovery_new": (report.get("discovery") or {}).get("new_items", 0)})
    except (OSError, ValueError, KeyError, TypeError):
        pass
    try:
        text = (directory / "scout_daily_pending_log.md").read_text()
        out["pending_log_entries"] = sum(1 for line in text.splitlines() if line.startswith("## "))
    except OSError:
        out["pending_log_entries"] = 0
    return out


def status_line(info: dict) -> str:
    if info["status"] == "NO_REPORT":
        return "RADAR no report yet (cron 05:20 UTC; first run records a baseline)"
    bits = [f"RADAR {info['status']} last run {info['last_run']} ({info['age_hours']} h ago), verdict {info['verdict']}",
            f"{len(info['errors'])} probe error(s)", f"{info['pending_log_entries']} pending log entr(ies) "
            "(`scout_daily.py --append-log` on a task branch)"]
    if info["to_examine"]:
        bits.append("to examine: " + ", ".join(info["to_examine"]))
    return "; ".join(bits)


class CountingOpener:
    """Wraps an opener and records every call (host, status, seconds) so a run can document what it did."""

    def __init__(self, inner=http):
        self.inner, self.calls = inner, []

    def __call__(self, url, *args, **kwargs):
        started = time.monotonic()
        result = self.inner(url, *args, **kwargs)
        self.calls.append({"host": urllib.parse.urlsplit(url).netloc, "status": result[0],
                           "seconds": round(time.monotonic() - started, 2)})
        return result

    def summary(self) -> dict:
        hosts: dict[str, dict] = {}
        for c in self.calls:
            h = hosts.setdefault(c["host"], {"calls": 0, "non_200": 0, "seconds": 0.0})
            h["calls"] += 1
            h["non_200"] += c["status"] != 200
            h["seconds"] = round(h["seconds"] + c["seconds"], 2)
        return {"calls": len(self.calls), "by_host": hosts}


def save_text(path: Path, text: str, append: bool = False) -> tuple[bool, str]:
    """Write, then read back. A persistence claim is only ever made from ok=True."""
    try:
        if append:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "a") as handle:  # append: concurrent entries written meanwhile are preserved
                handle.write(text)
            ok = path.read_text().endswith(text)
        else:
            atomic_write(path, text)
            ok = path.read_text() == text
        return ok, "" if ok else "read-back differs from what was written"
    except OSError as exc:
        return False, str(exc)


def save_state(path: Path, own: dict, follow_fn=None, trace_fn=None) -> tuple[bool, str]:
    """Locked read-modify-write: keys this run owns replace the stored ones; follow/trace are updated by a function
    applied to the CURRENT stored value, so a concurrent `--follow-add` / `--trace` edit is not overwritten."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path.with_suffix(".lock"), "w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                current = json.loads(path.read_text())
            except (OSError, ValueError):
                current = {}
            current.update(own)
            if follow_fn:
                current["follow"] = follow_fn(current.get("follow") or follow_seed())
            if trace_fn:
                current["trace"] = trace_fn(current.get("trace") or {})
            text = json.dumps(current, indent=1)
            atomic_write(path, text)
            return path.read_text() == text, ""
    except (OSError, ValueError, TypeError) as exc:
        return False, str(exc)


def briefing(report: dict, persisted: dict | None = None) -> str:
    """Material deltas only, ONE next step first. 'Nothing useful' is a valid briefing; errors and failed saves are
    never hidden; 'saved' is stated only for files whose write was read back."""
    ctx = report.get("context") or {}
    deltas = report.get("selected", [])
    channels = (report.get("discovery") or {}).get("channels") or {}
    bad = [f"{c} ({v['outcome']})" for c, v in channels.items() if v["outcome"] == "error"]
    failed = [n for n, s in (persisted or {}).items() if s != "ok"]
    if deltas:
        top = deltas[0]
        nxt = f"examine {top['id']}: {top.get('wwox_question', '')[:110]}. Minimal test: {top.get('test', 'read the source first')}"
    elif bad or report["errors"] or failed:
        nxt = "inspect the errors below; nothing else is pending"
    else:
        nxt = "none; nothing useful today"
    lines = [f"RADAR BRIEFING {report['run_at']} | remote main {(ctx.get('main_sha') or 'UNRESOLVED')[:12]} "
             f"(context {ctx.get('cache', '?')})", f"NEXT STEP: {nxt}"]
    if ctx.get("freshness_limit"):
        lines.append(f"FRESHNESS LIMIT: {ctx['freshness_limit']}")
    if ctx.get("outranked_by"):
        lines.append(f"CONTEXT: roadmap_current is dated {ctx.get('roadmap_dated')}; later dated evidence in "
                     f"{', '.join(ctx['outranked_by'])} outranks its CURRENT heading: read that first.")
    if channels:
        lines.append("Channels: " + " | ".join(
            f"{c} {v['outcome']}" + (f" ({v['new']} new)" if v["outcome"] == "delta" else "")
            + (f" [{len(v['errors'])} error(s)]" if v["errors"] and v["outcome"] != "error" else "")
            for c, v in channels.items()))
        for q in (report.get("discovery") or {}).get("questions", []):
            lines.append(f"  question [{q['category']}] {q['question']} -> if confirmed: {q['decision']}")
    for n, item in enumerate(deltas, 1):
        lines += [f"Delta {n}: {item['id']}",
                  f"  source / version+date / fact+limit: {item['detail'][:600]}",
                  f"  question + decision: {item.get('wwox_question', '')} -> {item.get('decision', 'decide whether to examine')}",
                  f"  roadmap placement: {item.get('roadmap', 'R9/R12')}; proposed use: {item.get('use', 'none until examined')}",
                  f"  minimal test: {item.get('test', 'read the change at its source')}",
                  f"  cost + terms: {item.get('estimated_cost', '?')}; {item.get('licence', '?')}",
                  f"  outcome / reopen: {item.get('outcome', '?')}"]
    if not deltas:
        lines.append("No material delta.")
    known = sorted({n for v in channels.values() for n in v["known_resources"]})
    if known:
        lines.append("Known resources seen again (not news): " + ", ".join(known[:8]))
    for e in report["errors"][:12]:
        lines.append(f"ERROR: {e}")
    if len(report["errors"]) > 12:
        lines.append(f"ERROR: ... {len(report['errors']) - 12} more in scout_daily.json")
    for name, status in (persisted or {}).items():
        lines.append(f"{'Saved' if status == 'ok' else 'SAVE FAILED'}: {name}" + ("" if status == "ok" else f" ({status})"))
    return "\n".join(lines) + "\n"


def entry_markdown(item: dict, when: str) -> str:
    extra = ""
    if item.get("decision"):
        extra += f"**If confirmed (decision).** {item['decision']} Roadmap: {item.get('roadmap', 'R9')}.\n\n"
    if item.get("test"):
        extra += f"**Minimal test.** {item['test']}\n\n"
    return (f"\n## {when[:10]} · scout_daily · {item['id']}\n\n"
            f"**WWOX question.** {item['wwox_question']}\n\n"
            f"**Contribution vs existing.** {item['contribution_vs_existing']}\n\n"
            f"**Detected.** {item['detail']}\n\n{extra}"
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
    text = pending.read_text()
    ok, why = save_text(log, text, append=True)
    if not ok:
        print(f"APPEND FAILED, pending entries kept: {why}")
        return 1
    pending.unlink()
    print(f"appended pending entries to {log}")
    return 0


def read_state(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return {}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--append-log", action="store_true", help="move pending entries into the scout log")
    parser.add_argument("--status", action="store_true", help="print the last run's one-line status and exit")
    parser.add_argument("--discover-only", action="store_true",
                        help="run only the external search (no watch probes, no PubMed)")
    parser.add_argument("--theme", help="with --discover-only: one theme id or 'all' (default: next in rotation)")
    parser.add_argument("--dry-run", action="store_true", help="with --discover-only: print, write nothing")
    parser.add_argument("--briefing", action="store_true", help="always print the briefing (default: only if non-empty)")
    parser.add_argument("--follow-list", action="store_true", help="print the followed teams/repos and exit")
    parser.add_argument("--follow-add", metavar="TEAM/REPO", help="follow a public repo (needs --source --reason --reopen)")
    parser.add_argument("--source"), parser.add_argument("--reason"), parser.add_argument("--reopen")
    parser.add_argument("--relevance", type=int, default=1)
    parser.add_argument("--trace", metavar="KEY", help="record a traceability event (needs --stage --state)")
    parser.add_argument("--stage"), parser.add_argument("--state")
    parser.add_argument("--evidence-kind"), parser.add_argument("--evidence-ref")
    args = parser.parse_args(argv)
    directory = state_dir()
    cfg = load_config(directory)
    state_path = directory / "scout_daily_state.json"
    if args.append_log:
        return append_log(directory)
    if args.status:
        print(status_line(radar_status(directory)))
        return 0
    now = dt.datetime.now(dt.timezone.utc)
    today = now.date().isoformat()
    if args.follow_list:
        for e in (read_state(state_path).get("follow") or follow_seed())["entries"]:
            print(f"{e['status']:9} {e['repo']} relevance {e['relevance']} | {e['source']} | {e['reason']} | reopen: {e['reopen']}")
        return 0
    if args.follow_add or args.trace:
        outcome = {}

        def follow_fn(follow):
            if args.follow_add:
                team, _, repo = args.follow_add.partition("/")
                outcome["r"] = follow_add(follow, {"team": team, "repo": args.follow_add, "source": args.source,
                                                   "reason": args.reason, "reopen": args.reopen,
                                                   "relevance": args.relevance}, cfg["follow"], today)
            return follow

        def trace_fn(trace):
            if args.trace:
                outcome["t"] = trace_event(trace, args.trace, args.stage, args.state, args.evidence_kind,
                                           args.evidence_ref, now.isoformat(timespec="seconds"))
            return trace
        ok, why = save_state(state_path, {}, follow_fn, trace_fn)
        print(outcome.get("r") or outcome.get("t"), "saved" if ok else f"SAVE FAILED {why}")
        return 0 if ok else 1
    state = read_state(state_path)
    follow = state.get("follow") or follow_seed()
    ctx = resolve_context(state.get("context"), now=now)
    known = known_idents(WATCH, follow, ctx)
    counter = CountingOpener(http)
    if args.discover_only:
        result, dstate = discover(state.get("discovery", {}), now=now, only=args.theme, pause=7, opener=counter, known=known,
                                  per_run=cfg["questions_per_run"], open_slot=cfg["open_slot"] and not args.theme,
                                  deep=cfg["version_checks"])
        print(json.dumps(result, indent=1, ensure_ascii=False) if result else "already searched today")
        if result and not args.dry_run:
            entries = discovery_entries(result, now.isoformat())
            ok, why = save_state(state_path, {"discovery": dstate, "context": ctx})
            print("state saved" if ok else f"STATE SAVE FAILED: {why}")
            if ok and entries:
                ok, why = save_text(directory / "scout_daily_pending_log.md",
                                    "".join(entry_markdown(i, now.isoformat(timespec="seconds")) for i in entries), append=True)
                print("pending log saved" if ok else f"PENDING LOG SAVE FAILED: {why}")
        return 0
    report, new_state = run(state, opener=counter)
    report["context"] = {k: v for k, v in ctx.items() if k != "files"}
    report["context"]["files"] = {p.rsplit("/", 1)[-1]: {k: v for k, v in f.items() if k != "repos"}
                                  for p, f in ctx["files"].items()}
    trace_events: list[tuple] = []
    try:  # the search is additive: its failure must never hide the probes
        result, new_state["discovery"] = discover(state.get("discovery", {}), now=now, opener=counter, known=known, pause=7,
                                                  per_run=cfg["questions_per_run"], open_slot=cfg["open_slot"],
                                                  deep=cfg["version_checks"])
    except (ValueError, KeyError, TypeError, OSError) as exc:
        result, new_state["discovery"] = None, state.get("discovery", {})
        report["errors"].append(f"discovery: {exc}")
    if result:
        report["discovery"] = {"themes": [r["theme"] for r in result["themes"]], "new_items": result["new_items"],
                               "channels": result["channels"], "questions": result["questions"],
                               "items": [i for r in result["themes"] for i in r["items"]]}
        report["errors"] += [f"{c}: {e}" for c, v in result["channels"].items() for e in v["errors"]]
        report["selected"] += discovery_entries(result, report["run_at"])  # the search keeps its own seen-cache: no baseline
        trace_events += [(k, "signal", "signalled") for r in result["themes"] for k in (i["key"] for i in r["items"])]
    deep_updates, deep_rows = [], []
    fcfg = cfg["follow"]
    for entry in follow_due(follow, now, fcfg["deep_check_days"], fcfg["deep_per_run"]):  # known projects: weekly
        res = repo_versions(entry["repo"], counter)
        fp = {"commit": (res["last_commit"] or {}).get("sha"), "release": json.dumps(res["latest_release"], sort_keys=True)}
        deep_rows.append({"repo": entry["repo"], "versions": {k: res[k] for k in ("last_commit", "latest_release")},
                          "errors": res["errors"]})
        report["errors"] += [f"follow: {e}" for e in res["errors"]]
        if res["last_commit"] is None:
            continue  # an error is not a check: last_deep stays, the repo is retried next run
        deep_updates.append((entry["repo"], fp))
        if entry.get("fp") and entry["fp"] != fp and not report["baseline"]:
            item = {"id": f"Follow:{entry['repo']}", "wwox_question": entry["reason"], "decision": f"reopen condition: {entry['reopen']}",
                    "contribution_vs_existing": f"followed since {entry['added']} ({entry['source']})",
                    "detail": f"default-branch head {entry['fp'].get('commit')} -> {fp['commit']}; latest release "
                              f"{entry['fp'].get('release')} -> {fp['release']}",
                    "estimated_cost": "reading the change: minutes", "licence": "see source", "roadmap": "R9",
                    "proof": f"https://github.com/{entry['repo']}", "outcome": "TO_TRIAGE (a detected change is not a reading)"}
            report["selected"].append(item)
            trace_events.append((f"follow:{entry['repo']}:{fp['commit']}", "signal", "signalled"))
    report["follow"] = {"active": sum(e["status"] == "active" for e in follow["entries"]), "deep_checked": deep_rows}
    report["http"] = counter.summary()

    def follow_fn(cur):
        for repo, fp in deep_updates:
            for e in cur["entries"]:
                if e["repo"] == repo:
                    e["fp"], e["last_deep"] = fp, now.isoformat(timespec="seconds")
        return cur

    def trace_fn(cur):
        for key, stage, st in trace_events:
            trace_event(cur, key, stage, st, at=now.isoformat(timespec="seconds"))
        return cur
    persisted = {}
    ok, why = save_state(state_path, {"watch": new_state["watch"], "pubmed": new_state["pubmed"],
                                      "discovery": new_state["discovery"], "context": ctx}, follow_fn, trace_fn)
    persisted["state"] = "ok" if ok else why or "failed"
    ok, why = save_text(directory / "scout_daily.json", json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    persisted["report"] = "ok" if ok else why or "failed"
    if report["selected"]:
        ok, why = save_text(directory / "scout_daily_pending_log.md",
                            "".join(entry_markdown(i, report["run_at"]) for i in report["selected"]), append=True)
        persisted["pending log"] = "ok" if ok else why or "failed"
    text = briefing(report, persisted)
    ok, why = save_text(directory / "scout_daily_briefing.md", text)
    if not ok:
        text += f"SAVE FAILED: briefing file ({why})\n"
    if args.briefing or report["selected"] or report["errors"] or persisted.get("state") != "ok":
        print(text, end="")
    return 0 if all(s == "ok" for s in persisted.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
