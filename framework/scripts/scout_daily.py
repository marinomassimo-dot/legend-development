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
The questions are not a fixed list: `resolve_plan` DERIVES them (deterministic text rules, no model call) from the
current priority surfaces read at the remote-main SHA (diagnosis, roadmap work order, work_order.json, the open task
record, the CURRENT iteration section, WATCH rows with a reopen condition), reuses unchanged blobs, and flags the plan
provisional when the SHA or a surface cannot be verified. Each question carries priority -> source (path, blob, SHA) ->
decision; a step marked DONE or a resolved condition stops generating. `--plan` prints it. One level of public team
exploration (the owner's other repositories, term-matched, 3 per team, 1 team a day, 14-day cooldown) follows discovery.
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
    # openFDA-NDC removed 2026-10-29 (iteration 6, triage of the 05:20 selection): `meta.last_updated` is the refresh date of
    # a product catalogue and moves on nearly every refresh, so the probe selected itself day after day without ever bearing
    # on a drug, an approval or evidence. The adapter (framework/adapters/openfda.py) still reads NDC on demand.
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
          "follow": {"max_teams": 6, "max_repos": 18, "max_per_team": 3, "deep_check_days": 7, "deep_per_run": 3},
          "explore": {"teams_per_run": 1, "repos_per_team": 3, "cooldown_days": 14, "max_per_owner": 2}}


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
        done = subprocess.run(["git", *args], cwd=cwd, capture_output=True, timeout=timeout, env=env)
        return done.returncode, done.stdout.decode("utf-8", "replace")  # a stray byte must not end the daily run
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
# PRIORITY PLAN: the questions the search asks are DERIVED, by a deterministic function and without any model call,
# from the surfaces that hold the current priorities, read at the remote-main SHA. Nothing here is a register: the
# plan is recomputed whenever a surface blob changes and is never edited by hand. Each question carries its origin
# (surface, locator, path, blob, SHA) so that "priority -> source -> decision" is readable from the report.
MODULE = "disease-models/wwox/research/drug_repurposing"
TASK_DIR = "ledger/tasks/orchestrator"
SURFACE_PATHS = {"roadmap": f"{MODULE}/roadmap_current.md", "readme": f"{MODULE}/README.md",
                 "work_order": f"{MODULE}/view/work_order.json"}
DONE_STATES = {"DONE", "COMPLETE", "COMPLETED", "CLOSED"}
WEIGHT = {"task_step": 4, "diagnosis": 3, "work_order": 3, "open_item": 3, "reopen": 2, "roadmap_first": 2, "roadmap": 1}
STOP = frozenset("""about above after again against also among another because been before being below between both
but can could did does done during each either else every first from further had has have having here how into its just
less like may might more most much must new next not now off once one only other our out over own same should since some
such than that the their them then there these they this those through too under until upon use used using very was were
what when where whether which while who will with within without would yet iteration package record task step steps
owner status todo wwox module roadmap current work orchestrator scientist verifier output outputs state states
result results change changes position give gives read differences difference several systematically explicit online cases
attempts failed produce resume behaviour visibility reuse regenerated operational comparison documented bottleneck principal called itself""".split())
# Translation of priority text into a search category (and a Hugging Face search word). First match wins. These are
# vocabulary, not priorities: a priority that matches nothing is skipped when it is task text, kept otherwise.
HOOKS = [(re.compile(r"evaluat|benchmark|gold set|outcome|prospective|predict", re.I), "prediction/evaluation", "benchmark", "drug repurposing"),
         (re.compile(r"leakage|confound|negative result|counter-?evidence", re.I), "negative results", None, "drug repurposing"),
         (re.compile(r"pharmacolog|potency|selectiv|ic50|\bki\b|assay condition", re.I), "matching/pharmacology", "bioactivity", "pharmacology"),
         (re.compile(r"licen[cs]e|redistribut|terms of|notice|attribution", re.I), "databases", "dataset", "compound database"),
         (re.compile(r"signature|perturb|lincs|transcriptom", re.I), "databases", "perturbation", "perturbation signature"),
         (re.compile(r"cache|retry|rest api|retriev|endpoint|extract|fragil", re.I), "tools/capabilities", None, "biomedical"),
         (re.compile(r"continuity|handoff|autonom|mandate|checkpoint|agent|resum", re.I), "Scientist/Orchestrator patterns", "agent", "agent"),
         (re.compile(r"compound|catalogue|identity|drug", re.I), "databases", "compound", "compound database"),
         (re.compile(r"network|pathway|context|tissue|species|assay|biolog", re.I), "scientific inputs", None, "biomedical")]
DEFAULT_HOOK = ("scientific inputs", None, "")
NEURO = re.compile(r"neuron|neural|seizure|epilep|glia|brain|synap|cortex|slice|wwox|myelin|excitab", re.I)
# Purely internal process (how we work, not what exists outside) is not an external search question unless the
# same text carries an explicit external hook.
INTERNAL = re.compile(r"presentation|shareable|dashboard|continuity|autonom|agent|report|checkpoint|handoff|mandate|resum|"
                      r"verification|battery|cleanup|reconcil|canonical|fresh actor|scouting|radar|follow cycle|traced|channels", re.I)
EXTERNAL = re.compile(r"benchmark|evaluat|licen[cs]e|dataset|database|repurpos|pharmacolog|signature|perturb|compound|assay|"
                      r"predict|leakage|retriev|cache|rest api", re.I)
# Words too generic to prove that another repository is about the same subject.
GENERIC = frozenset("""agent agents neuronal evaluation independent predictive benchmark data model models method methods tool tools
source sources system systems analysis dataset database open public research tests test validation framework pipeline
workflow platform network networks outcome outcomes""".split())


def _words(text: str) -> list[str]:
    out = []
    for w in re.findall(r"[a-z][a-z0-9-]{3,}", re.sub(r"[`*_\[\]()|]", " ", text.lower())):
        w = w.strip("-")
        if len(w) >= 4 and w not in STOP and not re.fullmatch(r"(it|p|r)\d+\w*", w):
            out.append(w)
    return out


def key_terms(text: str, n: int = 4) -> list[str]:
    """Distinctive words of ONE text: most frequent, then longest, then alphabetical. A pure function of the text
    (deterministic, no model, no network, and independent of every other priority)."""
    counts: dict[str, int] = {}
    for w in _words(text):
        counts[w] = counts.get(w, 0) + 1
    return sorted(counts, key=lambda w: (-counts[w], -len(w), w))[:n]


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[`*]", "", text)).strip()


def parse_roadmap(text: str, path: str) -> list[dict]:
    out = []
    for line in text.splitlines():
        m = re.match(r"\|\s*(R\d+)\s*/\s*([\w ]+?)\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(3).split("|")]
        if len(cells) < 3:
            continue
        rid, prio = m.group(1), m.group(2).strip()
        out.append({"surface": "roadmap", "lid": rid, "locator": f"{rid} ({prio})", "weight": WEIGHT["roadmap_first" if prio == "first" else "roadmap"],
                    "text": _plain(f"{cells[0]} {cells[1]}"), "decision": f"{rid} completion: {_plain(cells[2])[:140]}"})
    return out


def parse_diagnosis(text: str, path: str) -> list[dict]:
    out = []
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] in ("Stage", "") or set(cells[0]) <= set("-: "):
            continue
        missing = _plain(cells[5])
        if missing in ("-", "") or missing.lower().startswith("not diagnosed"):
            continue
        out.append({"surface": "diagnosis", "lid": _plain(cells[0]).lower().replace(" ", "-"),
                    "locator": f"row '{_plain(cells[0])}' ({_plain(cells[1])})",
                    "weight": WEIGHT["diagnosis"] + ("principal bottleneck" in cells[5].lower()),
                    "text": f"{_plain(cells[0])} {missing}", "decision": f"{_plain(cells[0])}: closing '{missing[:130]}'"})
    return out


def parse_work_order(text: str, path: str) -> list[dict]:
    out = []
    for entry in json.loads(text).get("entries", []):
        need = str(entry.get("need"))
        out.append({"surface": "work_order", "lid": need, "locator": f"entry {need}", "weight": WEIGHT["work_order"],
                    "text": _plain(f"{entry.get('question', '')} {entry.get('would_change', '')}"),
                    "decision": _plain(str(entry.get("would_change") or entry.get("question") or ""))[:160]})
    return out


def parse_task(text: str, path: str) -> list[dict]:
    """Open steps of the mandate record. A step whose status is DONE generates nothing; a step is search-relevant only
    when its text matches a hook (most steps are internal work that no external search can inform)."""
    rec = json.loads(text)
    out = []
    for key, queue in rec.items():
        if not (key.startswith("AUTHORISED_QUEUE") and isinstance(queue, dict)):
            continue
        for okey, obj in queue.items():
            for st in (obj.get("steps", []) if okey.startswith("OBJ_") and isinstance(obj, dict) else []):
                if str(st.get("status", "")).upper() in DONE_STATES:
                    continue
                body = _plain(str(st.get("step", "")))
                sid = body.split(" ", 1)[0]
                out.append({"surface": "task_step", "lid": f"{okey}/{sid}", "locator": f"{rec.get('TASK_ID')} {okey} step {sid} [{st.get('status')}]",
                            "weight": WEIGHT["task_step"], "text": body, "hook_required": True,
                            "decision": f"step {sid} ({st.get('owner')}): whether a found method/resource changes how it is done"})
    return out


def current_section(text: str):
    """(section text, note). The LAST heading marked CURRENT wins; two marked headings are flagged as ambiguous."""
    lines = text.splitlines()
    marked = [i for i, line in enumerate(lines) if re.match(r"#{2,4} .*\bCURRENT\b", line)]
    if not marked:
        return "", "no heading marked CURRENT in the module README"
    i = marked[-1]
    j = next((k for k in range(i + 1, len(lines)) if re.match(r"#{2,4} Roadmap iteration", lines[k])), len(lines))
    note = f"{len(marked)} headings are marked CURRENT; the last one is used" if len(marked) > 1 else ""
    return "\n".join(lines[i:j]), note


def parse_readme(text: str, path: str):
    """Open items the CURRENT iteration section declares (`Only planned:` / `Next:` sentences), the package READMEs it
    links, and a note when the section is missing or ambiguous."""
    section, note = current_section(text)
    out = []
    for m in re.finditer(r"(?:Only planned|Next step|Next|Remaining|Not yet)\s*:\s*([^\n]+?)(?:\.\s|\.$|\n|$)", section):
        sentence = _plain(m.group(1))
        out.append({"surface": "open_item", "lid": digest(sentence), "locator": f"CURRENT section: '{sentence[:60]}'",
                    "weight": WEIGHT["open_item"], "text": sentence, "decision": f"still open per the CURRENT section: {sentence[:130]}"})
    links = sorted({m for m in re.findall(r"\]\(([\w./-]+/README\.md)\)", section)})[:8]
    return out, [f"{MODULE}/{p}" for p in links], ([note] if note else [])


def parse_reopen(text: str, path: str) -> list[dict]:
    """Reopen conditions of a package README: WATCH table rows that state `reopen if/when ...`, and, when the README
    names a WATCH decision anywhere, prose or heading lines such as `Reopen if ...` / `Reopens when ...` (the name is the
    nearest heading above). A row no longer WATCH, or a line that lost its condition, generates nothing."""
    out = []
    pkg = path.rsplit("/", 2)[-2]
    cond_re = re.compile(r"\breopens?(?:ed)?\s+(?:if|when|on|once)\s+(.+?)(?:[;]|\.\s|\.$|$)", re.I)
    has_watch = bool(re.search(r"\bWATCH\b", text))
    heading = pkg
    for line in text.splitlines():
        if line.startswith("#"):
            heading = _plain(line.lstrip("# "))[:40]
            continue
        cells = [_plain(c) for c in line.strip().strip("|").split("|")]
        if line.lstrip().startswith("|"):
            if len(cells) >= 3 and any(c.upper() == "WATCH" for c in cells[1:3]):
                m = cond_re.search(cells[-1])
                if m:
                    out.append({"surface": "reopen", "lid": f"{pkg}/{cells[0][:40]}", "locator": f"{pkg} row '{cells[0][:40]}'",
                                "weight": WEIGHT["reopen"], "text": f"{cells[0]} {m.group(1)}",
                                "decision": f"reopen condition met? {m.group(1)[:140]}"})
            continue
        m = cond_re.search(_plain(line)) if has_watch else None
        if m:
            out.append({"surface": "reopen", "lid": f"{pkg}/{heading}/{digest(m.group(1))}",
                        "locator": f"{pkg} '{heading}' line 'reopen {m.group(1)[:40]}'", "weight": WEIGHT["reopen"],
                        "text": f"{heading} {m.group(1)}", "decision": f"reopen condition met? {m.group(1)[:140]}"})
    return out


OPEN_VERDICT = re.compile(r"^(NEEDS-DATUM|PARTIAL|PARTLY|WATCH)", re.I)
TABLE_NAME = re.compile(r"/(reopen_searches[^/]*|decisions)\.tsv$")
TABLE_LIMIT = 12  # newest package tables read; each is blob-cached, so an unchanged table costs no read


def parse_reopen_table(text: str, path: str) -> list[dict]:
    """Reopen conditions kept as a TABLE: `reopen_searches*.tsv` (id, item, verdict, trigger_to_reopen) or `decisions.tsv`
    (name, verdict, reopen_condition). A row is open only while its verdict is still NEEDS-DATUM, PARTIAL(LY) or WATCH;
    an answered, discarded or condition-less row generates nothing. Read as columns, not matched as prose."""
    rows = [line.split("\t") for line in text.splitlines() if line.strip()]
    if len(rows) < 2:
        return []
    head = [c.strip().lower() for c in rows[0]]
    col = {name: head.index(name) for name in ("id", "name", "item", "verdict", "trigger_to_reopen", "reopen_condition") if name in head}
    cond_col = col.get("trigger_to_reopen", col.get("reopen_condition"))
    label_col = col.get("item", col.get("name"))
    if "verdict" not in col or cond_col is None or label_col is None:
        return []
    pkg = path.rsplit("/", 2)[-2]
    out = []
    for n, row in enumerate(rows[1:]):
        if len(row) <= max(col["verdict"], cond_col, label_col):
            continue
        verdict, cond, label = _plain(row[col["verdict"]]), _plain(row[cond_col]), _plain(row[label_col])
        if not OPEN_VERDICT.match(verdict) or not cond:
            continue
        rid = _plain(row[col["id"]]) if "id" in col and len(row) > col["id"] else str(n)
        out.append({"surface": "reopen", "lid": f"{pkg}/{rid or n}", "locator": f"{pkg} table row {rid or n} [{verdict[:24]}]",
                    "weight": WEIGHT["reopen"], "text": f"{label[:160]} {cond[:200]}", "external": True,
                    "decision": f"reopen condition met? {cond[:140]}"})
    return out


def hook(text: str):
    """(category, hf word, anchor) of the first matching hook, or (None, None, anchor of the default)."""
    for pattern, category, hf, anchor in HOOKS:
        if pattern.search(text):
            return category, hf, anchor
    return None, None, "epilepsy" if NEURO.search(text) else "biomedical"


# Technical objects of a priority: what a search should be about. Symbols and acronyms (GSK3, GluN2B, PDHA1, NMDAR),
# drug names by their international stems, and a short list of assay/method words. Read from the text of ONE item.
ENTITY = re.compile(r"\b(?:[A-Z][A-Za-z]*\d[A-Za-z0-9]*|[A-Z]{3,6}[a-z]?)\b")
# Our own labels (P10, C2, H02, A05, IT12, PPR..., E-MTAB..., Ca2) and ions are not searchable objects.
LOCAL_ID = re.compile(r"[A-Za-z]{1,2}\d{1,2}[A-Za-z]?|IT\d+|PPR\d+|MTAB\d*|Ca2|Mg2|Na1|I{2,3}|IV|VI{0,3}", re.I)
NOT_ENTITY = frozenset("WWOX WOREE SCAR DEE WATCH NEEDS DATUM PARTIAL PARTLY DONE TODO PMID DOI UMI CPP NAM HIF NOT ONLY AND THE FOR ATP ROS CNS SRA DNA RNA REST EMBL EBI".split())
DRUG = re.compile(r"\b[a-z]{2,}(?:prodil|mide|pril|tinib|ciclib|setron|zolam|barbital|oxetine|vastatin|gliptin|parib|olol|dipine|azole|"
                  r"idone|triptan|caine|profen|gabatrin|zepam|sartan|lukast|mab)\b", re.I)
METHODS = re.compile(r"\b(patch[- ]clamp|perforated patch|gramicidin|sIPSC|mIPSC|snRNA-?seq|single[- ]nucle\w+|western blot|SPR|DepMap|"
                     r"electrophysiolog\w+|phosphorylation|knockout|isogenic|organoid|proteomic\w*|crystal structure)\b", re.I)


def entities(text: str, n: int = 3) -> tuple[list[str], list[str]]:
    """(objects, methods) named in one text, in order of first appearance, lower-case, no duplicates."""
    seen: dict[str, None] = {}
    for m in ENTITY.finditer(text):
        if m.group(0) not in NOT_ENTITY and not LOCAL_ID.fullmatch(m.group(0)):
            seen.setdefault(m.group(0).lower(), None)
    for m in DRUG.finditer(text):
        seen.setdefault(m.group(0).lower(), None)
    methods: dict[str, None] = {}
    for m in METHODS.finditer(text):
        methods.setdefault(re.sub(r"\s+", " ", m.group(0).lower().replace("-", " ")).strip(), None)
    return list(seen)[:n], list(methods)[:1]


def build_questions(items: list[dict]) -> tuple[list[dict], int]:
    """Items -> search questions in the shape of THEMES, each with its origin. Returns (questions, skipped)."""
    best: dict[str, dict] = {}
    skipped = 0
    for it in items:
        category, hf, anchor = hook(it["text"])
        if INTERNAL.search(it["text"]) and not EXTERNAL.search(it["text"]) and not it.get("external"):
            skipped += 1  # process about our own work: nothing outside can answer it
            continue
        if category == "scientific inputs":
            anchor = "epilepsy" if NEURO.search(it["text"]) else "biomedical"
        terms = key_terms(it["text"])  # local to the item: editing one priority never moves another question
        if len(terms) < 2 or (it.get("hook_required") and category is None):
            skipped += 1
            continue
        plain = [t for t in terms if re.fullmatch(r"[a-z]{4,14}", t)]  # no hyphenated or rare tokens in a search string
        objs, methods = entities(it["text"])
        if objs and not hf:
            hf = objs[0]
        if objs or methods:  # named objects lead; frequency words only fill what the text did not name
            plain = list(dict.fromkeys(objs + methods + [t for t in plain if t not in GENERIC]))[:3]
            # a category word ("compound database", "epilepsy") drowned the object; only a lone short acronym keeps a context word
            if objs:
                anchor = "neuron" if len(objs) == 1 and len(objs[0]) <= 4 and NEURO.search(it["text"]) else ""
        kw = " ".join(([anchor] if anchor else []) + (plain or terms))
        q = {"id": f"{it['surface']}:{it['lid']}", "category": category or "scientific inputs",
             "gap": it["text"][:140], "decision": it["decision"], "weight": it["weight"], "kw": kw,
             "gh": " ".join(((anchor + " " if anchor else "") + (plain or terms)[0]).split()[:3]), "hf": hf or max(plain or terms, key=len),
             "epmc": " AND ".join(f'TITLE_ABS:"{w}"' if " " in w else f"TITLE_ABS:{w}"
                                  for w in (([anchor] if anchor else []) + plain)[:2]) if plain else None,
             "terms": terms, "plain": plain, "anchor": anchor,
             "domain": [t for t in plain if t not in GENERIC][:3],
             "origin": {k: it[k] for k in ("surface", "locator", "path", "blob", "sha")} | {"priority": it["text"][:200]}}
        if kw not in best or q["weight"] > best[kw]["weight"]:
            best[kw] = q
    return sorted(best.values(), key=lambda q: (-q["weight"], q["id"])), skipped


def _extract(path: str, text: str):
    """(items, links, notes) of one surface, by file kind."""
    name = path.rsplit("/", 1)[-1]
    if name == "roadmap_current.md":
        return parse_roadmap(text, path), [], []
    if name == "work_order.json":
        return parse_work_order(text, path), [], []
    if name.startswith("ORCH-ROADMAP"):
        return parse_task(text, path), [], []
    if path == SURFACE_PATHS["readme"]:
        return parse_readme(text, path)
    if path.startswith(f"{MODULE}/diagnosis_it"):
        return parse_diagnosis(text, path), [], []
    if path.endswith(".tsv"):
        return parse_reopen_table(text, path), [], []
    return parse_reopen(text, path), [], []


def _tables(runner, sha: str) -> list[str]:
    """Reopen/decision tables of the module at `sha`: one listing call, newest packages first, bounded."""
    code, out = runner(["ls-tree", "-r", "--name-only", sha, MODULE + "/"])
    if code != 0:
        return []
    names = [p for p in out.split("\n") if TABLE_NAME.search(p)]
    return sorted(names, key=lambda p: (-int(m.group(1)) if (m := re.search(r"_it(\d+)", p)) else 0, p))[:TABLE_LIMIT]


def _latest(runner, sha: str, directory: str, pattern: str):
    code, out = runner(["ls-tree", "--name-only", sha, directory + "/"])
    hits = [(int(m.group(1)), p) for p in out.split() for m in [re.search(pattern, p)] if m]
    return max(hits)[1].rstrip("/") if code == 0 and hits else None


def resolve_plan(cached: dict | None, extracts: dict | None, ctx: dict, runner=git, now: dt.datetime | None = None):
    """Derive the plan at ctx['main_sha'] -> (plan, extracts). Surfaces whose blob is unchanged are not re-read or re-parsed.
    Without a verified SHA the cached plan is returned marked provisional (never silently current)."""
    now = now or dt.datetime.now(dt.timezone.utc)
    cached = cached if isinstance(cached, dict) and isinstance(cached.get("questions", []), list) else {}
    extracts = {k: v for k, v in (extracts if isinstance(extracts, dict) else {}).items()
                if isinstance(v, dict) and isinstance(v.get("items"), list) and isinstance(v.get("blob"), str)}
    sha = ctx.get("main_sha")
    if not sha or ctx.get("cache") == "stale_reused":
        if cached.get("questions"):
            return dict(cached, provisional=(cached.get("provisional") or []) + [
                f"STALE: remote main not resolved or its objects unavailable; plan is the one derived at {str(cached.get('sha'))[:12]}"]), extracts
        return {"sha": sha, "questions": [], "inputs": {}, "provisional": ["no plan: remote main unavailable and no cached plan"]}, extracts
    reasons = [ctx["freshness_limit"]] if ctx.get("freshness_limit") else []
    paths = dict(SURFACE_PATHS)
    task = _latest(runner, sha, TASK_DIR, r"ORCH-ROADMAP-IT(\d+)-")
    diag = _latest(runner, sha, MODULE, r"diagnosis_it(\d+)_")
    if task:
        paths["task"] = task
    else:
        reasons.append("no ORCH-ROADMAP task record at this revision")
    if diag:
        paths["diagnosis"] = f"{diag}/README.md"
    else:
        reasons.append("no diagnosis_it* directory at this revision")
    inputs, items, reread = {}, [], 0
    todo = list(paths.items()) + [("reopen", t) for t in _tables(runner, sha)]
    seen_paths = set()
    while todo:
        kind, path = todo.pop(0)
        if path in seen_paths:
            continue
        seen_paths.add(path)
        code, blob = runner(["rev-parse", f"{sha}:{path}"])
        blob = blob.strip()
        if code != 0 or not blob:
            reasons.append(f"surface {path} absent at this revision")
            continue
        old = extracts.get(path) or {}
        if old.get("blob") != blob:
            code, text = runner(["show", f"{sha}:{path}"])
            try:
                if code != 0:
                    raise ValueError("git show failed")
                found, links, notes = _extract(path, text)
                notes = [f"{path}: {n}" for n in notes]
                if "\ufffd" in text:
                    notes.append(f"surface {path} held undecodable bytes (replaced): unreadable parts may be missing")
                if not found and kind in ("roadmap", "work_order", "diagnosis"):
                    notes.append(f"surface {path} parsed 0 items (format changed or table emptied?)")
            except (ValueError, KeyError, TypeError, AttributeError) as exc:
                reasons.append(f"surface {path} unreadable: {exc}")
                continue
            extracts[path] = old = {"blob": blob, "items": found, "links": links, "notes": notes}
            reread += 1
        inputs[path] = {"surface": kind, "blob": blob}
        reasons += old.get("notes", [])  # stored with the blob, so a cached surface keeps its warnings
        for it in old["items"]:
            items.append(dict(it, path=path, blob=blob, sha=sha))
        todo += [("reopen", link) for link in old.get("links", [])]
    extracts = {p: v for p, v in extracts.items() if p in inputs}
    questions, skipped = build_questions(items)
    plan = {"sha": sha, "derived_at": now.isoformat(timespec="seconds"), "inputs": inputs, "questions": questions,
            "skipped": skipped, "provisional": reasons, "reread": reread,
            "cache": "hit" if reread == 0 else "re-derived"}
    plan["digest"] = digest(json.dumps([[q["id"], q["kw"], q["weight"]] for q in questions]))
    return plan, extracts


NEVER_ASKED_DAYS = 90   # IT19 P7: above the 30-day cap of a repeat (3 x 30), so no question starves behind recurring ones


def pick_questions(questions: list[dict], asked: dict, now: dt.datetime, n: int) -> list[dict]:
    """Higher weight and longer since asked go first. A repeat counts at most 30 days; a never-asked question counts as 90, so every
    question is asked once before any heavier one is asked again (measured on the real plan in IT19: with 30 for both, 11 roadmap rows were never
    asked in 90 days and 2 reopen rows waited past 60). A question whose terms changed is a new question (the key includes the terms)."""
    today = now.date()

    def score(q):
        last = asked.get(f"{q['id']}|{digest(q['kw'])}")
        try:
            age = min(30, (today - dt.date.fromisoformat(last)).days) if isinstance(last, str) else NEVER_ASKED_DAYS
        except ValueError:
            age = NEVER_ASKED_DAYS  # a damaged date counts as never asked
        return q["weight"] * age
    return sorted(questions, key=lambda q: (-score(q), q["id"]))[:n]


def origin_line(origin: dict | None) -> str:
    if not origin:
        return "open slot: no priority assumed"
    return (f"{origin['surface']} {origin['locator']} [{origin['path']} @ blob {origin['blob'][:10]}, main {origin['sha'][:12]}]: "
            f"\"{origin['priority'][:110]}\"")


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
        if not new.get(key) or not str(new[key]).strip():  # falsy BEFORE str(): None must not become "None"
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


def _ref_exists(kind: str | None, ref: str | None, root: Path) -> bool:
    """record_file / test_run refs name a file under the repository root (`path[::test id]`); other kinds are not files."""
    if kind in ("source_read", "session_check"):  # not a file kind, but it must still name something checkable
        text = ref or ""
        if re.search(r"https?://\S+", text):
            return True
        token = text.split()[0] if text.split() else ""
        try:
            return bool(token) and (root / token).resolve().is_file() and root.resolve() in (root / token).resolve().parents
        except (OSError, ValueError):
            return False
    if kind not in ("record_file", "test_run"):
        return True
    path = (ref or "").split("::")[0].strip()
    try:
        target = (root / path).resolve()
        return bool(path) and target.is_file() and root.resolve() in target.parents
    except (OSError, ValueError):
        return False


def _done(rec: dict) -> dict:
    return {h["stage"]: h["state"] for h in rec["history"] if h["state"] != "claimed"}


def trace_event(trace: dict, key: str, stage: str, state: str, kind: str | None = None, ref: str | None = None,
                at: str = "", root: Path = ROOT, via: str = "") -> tuple[bool, str]:
    if stage not in STAGES or state not in STAGES[stage]:
        return False, f"unknown stage/state {stage}/{state}"
    rec = trace.setdefault(key, {"history": []})
    done = _done(rec)
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
    if needs_evidence and not _ref_exists(kind, ref, root):
        rec["history"].append({"stage": stage, "state": "claimed", "claimed": state, "kind": kind, "ref": ref, "at": at})
        return False, f"evidence ref not found under the repository root: {ref}; stays 'claimed', not {state}"
    rec["history"].append(dict({"stage": stage, "state": state, "kind": kind, "ref": ref, "at": at},
                               **({"via": via} if via else {})))
    return True, "recorded"


def trace_summary(trace: dict) -> dict:
    out = {}
    for key, rec in trace.items():
        done = _done(rec)
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
     "gap": "context-matched neuronal perturbation signatures for reversal queries (compound signatures: LINCS phase I used; phase II not)",
     "decision": "whether R3 can use a neuron-matched signature set instead of a generic one",
     "hf": "perturbation", "kw": "perturbation signature neuron reversal",
     "epmc": '(TITLE_ABS:"perturbation signature*" OR TITLE_ABS:L1000 OR TITLE_ABS:"connectivity map") AND '
             '(TITLE_ABS:neuron* OR TITLE_ABS:iPSC) AND (TITLE_ABS:reversal OR TITLE_ABS:repurposing)',
     "gh": "lincs signature reversal"},
    {"id": "gene-knockdown-neural", "category": "databases",
     "gap": "what a single-gene knockdown shifts in human neural cells (LINCS shRNA covers 4 of 23 panel genes in NPC; WWOX itself is not a measured landmark)",
     "decision": "whether a gene-knockdown readout can test a module direction without a WWOX-deficient neural line",
     "hf": "perturb-seq", "kw": "Perturb-seq CRISPRi human neurons iPSC dataset",
     "epmc": '(TITLE_ABS:"Perturb-seq" OR TITLE_ABS:"CRISPRi screen") AND (TITLE_ABS:neuron* OR TITLE_ABS:iPSC) AND '
             '(TITLE_ABS:"single-cell" OR TITLE_ABS:transcriptom*)',
     "gh": "perturb-seq neurons"},
    {"id": "genetic-suppression-rescue", "category": "scientific inputs",
     "gap": "genetic suppressors / synthetic rescue of loss-of-function neurodevelopmental genes (curated human table has 1 of 25 panel genes, none WWOX)",
     "decision": "whether a rescue route (not a drug) is added to the experiment ledger",
     "hf": None, "kw": "genetic suppressor synthetic rescue human genes database",
     "epmc": '(TITLE_ABS:"genetic suppression" OR TITLE_ABS:"suppressor mutation*" OR TITLE_ABS:"synthetic rescue") AND '
             '(TITLE_ABS:human OR TITLE_ABS:patient*) AND (TITLE_ABS:screen OR TITLE_ABS:network OR TITLE_ABS:database)',
     "gh": "genetic suppression interactions human"},
    {"id": "repurposing-benchmarks", "category": "prediction/evaluation",
     "gap": "independent evaluations of drug-repurposing and signature-reversal methods (no WWOX needed)",
     "decision": "whether the R3 reference comparison keeps its method set",
     "hf": "repurposing", "kw": "knowledge graph link prediction benchmark data leakage negative sampling",
     "epmc": 'TITLE_ABS:"drug repurposing" AND TITLE_ABS:(benchmark OR "independent evaluation" OR "prospective validation")',
     "gh": "biomedical knowledge graph link prediction evaluation"},
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
MAX_PER_OWNER = 2  # items one team/owner may contribute to a run
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


def _tokens(text: str) -> set:
    return set(re.findall(r"[a-z][a-z0-9]{3,}", (text or "").lower().replace("-", " ").replace("_", " ")))


def item_owner(item: dict):
    """(channel, owner) of a discovered GitHub repository or Hub asset; None for a paper or an owner-less asset."""
    ident = (item.get("ident") or "")
    if item.get("channel") in ("github", "huggingface") and "/" in ident:
        return item["channel"], ident.split("/")[0]
    return None


def explore_team(channel: str, owner: str, terms: list[str], known, listed=(), opener=http, limit: int = 3,
                 now: dt.datetime | None = None) -> dict:
    """ONE level of bounded exploration: the owner's other public repositories (GitHub) or models/datasets (Hugging Face),
    kept only when their name, description or tags share a term with a current priority question. No collaborator,
    follower or contributor is ever requested, and nothing found here is explored in turn."""
    now = now or dt.datetime.now(dt.timezone.utc)
    since = _years_ago(now, NEW_WINDOW_DAYS)
    out = {"owner": owner, "channel": channel, "calls": 0, "errors": [], "candidates": [], "scanned": 0, "no_match": 0}
    q = urllib.parse.quote(owner)
    urls = ([f"{GH_API}/users/{q}/repos?sort=pushed&per_page=30&type=owner"] if channel == "github" else
            [f"{HF_API}/{k}?author={q}&sort=lastModified&direction=-1&limit=30" for k in ("models", "datasets")])
    pool = []
    for url in urls:
        out["calls"] += 1
        code, _, body = opener(url)
        try:
            if code != 200:
                raise ValueError(f"HTTP {code}")
            data = json.loads(body)
            if not isinstance(data, list):
                raise TypeError("not a list")
        except (ValueError, TypeError) as exc:
            out["errors"].append(f"explore {owner} {url.split('?')[0].rsplit('/', 1)[-1]}: {exc}")
            continue
        for rec in data:
            if channel == "github":
                if rec.get("fork") or rec.get("archived") or (rec.get("pushed_at") or "")[:10] < since:
                    continue
                pool.append({"ident": rec["full_name"].lower(), "title": rec["full_name"],
                             "when": (rec.get("pushed_at") or "")[:10],
                             "text": " ".join([rec["full_name"], rec.get("description") or "", " ".join(rec.get("topics") or [])]),
                             "licence": (rec.get("license") or {}).get("spdx_id") or "none stated", "url": rec.get("html_url")})
            else:
                modified = (rec.get("lastModified") or "")[:10]
                if modified and modified < since:
                    continue
                kind = "datasets/" if "/datasets?" in url else ""
                lic = next((t.split(":", 1)[1] for t in rec.get("tags", []) if t.startswith("license:")), None)
                pool.append({"ident": rec["id"].lower(), "title": rec["id"], "when": modified,
                             "text": rec["id"] + " " + " ".join(rec.get("tags") or []), "licence": lic or "none stated",
                             "url": f"https://huggingface.co/{kind}{rec['id']}"})
    wanted = set(terms)
    scored = []
    for it in pool:
        out["scanned"] += 1
        if it["ident"] in known or it["ident"] in listed:
            continue
        matched = sorted(wanted & _tokens(it["text"]))
        if not matched:
            out["no_match"] += 1
            continue
        scored.append((-len(matched), it["when"], it["ident"], matched, it))
    scored.sort(key=lambda t: (t[0], [-ord(c) for c in t[1]], t[2]))  # most matched terms, then most recent
    for _, _, _, matched, it in scored[:limit]:
        out["candidates"].append(dict(it, matched=matched, text=None))
    return out


def pick_owners(items: list[dict], follow: dict | None, explored: dict, now: dt.datetime, days: int, n: int) -> list[tuple]:
    """Owners worth one exploration today: those of today's discovered items plus followed teams, never one explored
    within `days`, the longest-unexplored first (so a prolific team cannot take every day), at most `n`."""
    cand: dict[tuple, str] = {}
    for it in items:
        who = item_owner(it)
        if who:
            cand.setdefault((who[0], who[1].lower()), f"owner of discovered {it['title']}")
    for e in (follow or {}).get("entries", []):
        if e.get("status") == "active" and "/" in e["repo"]:
            cand.setdefault(("github", e["team"].lower()), f"followed team (repo {e['repo']})")
    cutoff = (now - dt.timedelta(days=days)).isoformat()
    ok = [(k, why) for k, why in cand.items() if (explored.get(k[1]) or {}).get("last", "") < cutoff]
    ok.sort(key=lambda kw: ((explored.get(kw[0][1]) or {}).get("last", ""), kw[0][1]))
    return [(k[0], k[1], why) for k, why in ok[:n]]


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

    owners = budget.setdefault("owners", {})
    cap = budget.get("cap", MAX_PER_OWNER)

    def owner_of(it):
        return it["ident"].split("/")[0] if it.get("ident") and "/" in it["ident"] else None

    def take(chan: str, fresh: list[dict]) -> None:
        keep, local = [], {}
        for it in fresh:
            if it["key"] in seen:
                continue
            if it.get("ident") and it["ident"] in known:
                chans[chan]["known"] += 1
                chans[chan]["known_names"].append(it["ident"])
                continue
            who = owner_of(it)  # a prolific team may show at most `cap` items per run; the rest stays unseen
            if who and owners.get(who, 0) + local.get(who, 0) >= cap:
                chans[chan]["capped"] = chans[chan].get("capped", 0) + 1
                continue
            if who:
                local[who] = local.get(who, 0) + 1
            keep.append(it)
        keep = keep[:SHOW]
        for it in keep:
            if owner_of(it):
                owners[owner_of(it)] = owners.get(owner_of(it), 0) + 1
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
            "decision": theme.get("decision", "unstated"), "origin": theme.get("origin"), "items": items, "channels": chans,
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
             pause: float = 0, per_run: int = 1, open_slot: bool = False, known=frozenset(), deep: int = 0,
             owner_cap: int = MAX_PER_OWNER):
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
    budget = {"n": deep, "cap": owner_cap}
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
    summary = channel_summary(results, duplicates)
    held = only is None and any(v["errors"] for v in summary.values()) and all(
        v["outcome"] in ("error", "not_queried") for v in summary.values())
    if held:  # every channel failed: the same questions and the same day stay open for the next run
        state["cursor"], state["last_day"] = dstate.get("cursor", 0), dstate.get("last_day")
    return {"themes": results, "new_items": len(kept), "channels": summary, "rotation_held": held,
            "questions": [{"id": r["theme"], "category": r["category"], "question": r["gap"], "decision": r["decision"],
                           "origin": r.get("origin")}
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
                         "duplicates": (duplicates or {}).get(chan, 0),
                         "owner_capped": sum(r["channels"][chan].get("capped", 0) for r in results)}
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
                    "question_category": res.get("category"), "decision": res.get("decision"), "origin": res.get("origin"),
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
            current = load_state_file(path)
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
    pl = report.get("plan")
    if pl:
        lines.append(f"PLAN derived at main {(pl.get('sha') or 'UNRESOLVED')[:12]} from {len(pl['inputs'])} surfaces "
                     f"({pl.get('cache')}, {pl.get('reread')} re-read), {pl['questions']} priority question(s), digest {pl.get('digest')}"
                     + ("; FALLBACK to the fixed theme list (no plan)" if pl.get("fallback") else ""))
        for why in pl.get("provisional", []):
            lines.append(f"PLAN PROVISIONAL: {why}")
    teams = report.get("teams") or {}
    for t in teams.get("explored", []):
        lines.append(f"Team explored: {t['owner']} ({t['channel']}; {t['why']}): {len(t['found'])} lead(s) of {t['scanned']} scanned")
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
            lines.append(f"    because: {origin_line(q.get('origin'))}")
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
    if "origin" in item:
        extra = f"**Why asked.** {origin_line(item['origin'])}\n\n" + extra
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


def final_verdict(report: dict) -> str:
    """Computed AFTER discovery and follow entries are appended, so a verdict never contradicts `selected`."""
    return "SELECTED" if report["selected"] else ("BASELINE" if report["baseline"] else "NO_USEFUL_CHANGE")


STATE_NOTES: list[str] = []  # what read_state/save_state had to do to a damaged state file; shown in the briefing


def _aside(path: Path, why: str) -> None:
    bad = path.with_name(path.name + ".bad")
    try:
        os.replace(path, bad)
        STATE_NOTES.append(f"state file {path.name} was {why}; moved aside to {bad.name}, run continues from an empty state")
    except OSError as exc:
        STATE_NOTES.append(f"state file {path.name} was {why} and could not be moved aside ({exc})")


def load_state_file(path: Path) -> dict:
    """The stored state, or {} when absent. Unparseable or non-object content is moved to <name>.bad, never overwritten
    silently; sub-keys of the wrong type are dropped (and noted)."""
    try:
        text = path.read_text()
    except OSError:
        return {}
    try:
        data = json.loads(text)
    except ValueError:
        _aside(path, "not valid JSON (truncated?)")
        return {}
    if not isinstance(data, dict):
        _aside(path, "valid JSON but not an object")
        return {}
    for key in ("watch", "pubmed", "discovery", "context", "follow", "trace", "plan", "extracts", "plan_asked", "explored"):
        bad = key in data and (not isinstance(data[key], dict)
                               or (key == "follow" and not isinstance(data[key].get("entries"), list)))
        if bad:
            STATE_NOTES.append(f"state key {key!r} had the wrong shape and was dropped (file kept as {path.name}.bad)")
            try:
                (path.with_name(path.name + ".bad")).write_text(text)
            except OSError:
                pass
            del data[key]
    return data


def read_state(path: Path) -> dict:
    return load_state_file(path)


def plan_step(state: dict, ctx: dict, cfg: dict, now: dt.datetime, runner=git):
    """The questions for today: from the derived plan when it has any, else the fixed theme list (said so in the report).
    Returns (plan, extracts, themes, dstate, per_run)."""
    plan, extracts = resolve_plan(state.get("plan"), state.get("extracts"), ctx, runner, now)
    dstate = state.get("discovery", {})
    if not isinstance(state.get("plan_asked"), dict):
        state = dict(state, plan_asked={})
    if plan.get("questions"):
        picked = pick_questions(plan["questions"], state.get("plan_asked") or {}, now, cfg["questions_per_run"])
        return plan, extracts, picked, dict(dstate, cursor=0), len(picked)
    return plan, extracts, THEMES, dstate, cfg["questions_per_run"]


def record_asked(asked: dict, result: dict | None, themes: list[dict], today: str) -> dict:
    """Mark the questions actually searched today (a held rotation marks nothing). Keys carry the terms digest."""
    asked = {k: v for k, v in (asked if isinstance(asked, dict) else {}).items() if isinstance(v, str) and DATE_RE.fullmatch(v)}
    if result and not result.get("rotation_held"):
        ran = {r["theme"] for r in result["themes"]}
        for q in themes:
            if q["id"] in ran and q.get("kw") is not None and q.get("origin"):
                asked[f"{q['id']}|{digest(q['kw'])}"] = today
    if len(asked) > 300:
        for key in sorted(asked, key=asked.get)[:len(asked) - 200]:
            del asked[key]
    return asked


def team_step(result: dict | None, follow: dict, explored: dict, themes: list[dict], known, cfg: dict, opener, now: dt.datetime):
    """One level of public exploration for at most `teams_per_run` owners (see explore_team). Returns
    (summary, selected items, new explored map, trace events)."""
    ecfg = cfg["explore"]
    items = [i for r in (result or {"themes": []})["themes"] for i in r["items"]]
    terms_by_q = {q["id"]: q.get("domain", []) for q in themes if q.get("origin")}
    ran = [r for r in (result or {"themes": []})["themes"] if r.get("origin")]
    terms = sorted({t for r in ran for t in terms_by_q.get(r["theme"], [])})  # DOMAIN terms only: generic words prove nothing
    known = set(known) | {i["ident"] for i in items if i.get("ident")}  # what this very run already shows is not "other work"
    summary = {"explored": [], "calls": 0, "errors": [], "candidates": 0}
    selected, events = [], []
    explored = {k: v for k, v in explored.items() if isinstance(v, dict) and isinstance(v.get("last", ""), str)}
    new = {k: dict(v) for k, v in explored.items()}
    if not terms:
        return summary, selected, new, events
    for channel, owner, why in pick_owners(items, follow, explored, now, ecfg["cooldown_days"], ecfg["teams_per_run"]):
        prior = (explored.get(owner) or {}).get("listed", [])
        res = explore_team(channel, owner, terms, known, prior, opener, ecfg["repos_per_team"], now)
        summary["calls"] += res["calls"]
        summary["errors"] += res["errors"]
        summary["candidates"] += len(res["candidates"])
        summary["explored"].append({"owner": owner, "channel": channel, "why": why, "scanned": res["scanned"],
                                    "no_match": res["no_match"], "found": [c["title"] for c in res["candidates"]]})
        if res["errors"] and not res["calls"] - len(res["errors"]):
            continue  # nothing answered: not explored, retried next run
        new[owner] = {"last": now.isoformat(timespec="seconds"),
                      "listed": (prior + [c["ident"] for c in res["candidates"]])[-30:]}
        if res["candidates"]:
            q = next((r for r in ran if set(terms_by_q[r["theme"]]) & {m for c in res["candidates"] for m in c["matched"]}), ran[0])
            selected.append({
                "id": f"Team:{owner}", "wwox_question": q["gap"], "decision": q["decision"], "origin": q["origin"],
                "roadmap": CATEGORY_ROADMAP.get(q["category"], "R9"), "keys": [f"team:{c['ident']}" for c in res["candidates"]],
                "detail": f"{why}; other public work matching {sorted({m for c in res['candidates'] for m in c['matched']})}: " + "; ".join(
                    f"[{channel}] {c['title']} ({c['when']}, {c['licence']}, matched {c['matched']}) {c['url']}" for c in res["candidates"]),
                "contribution_vs_existing": f"one-level exploration of {owner}'s public listing ({res['scanned']} scanned, "
                                            f"{res['no_match']} without a shared term); not recursive",
                "estimated_cost": "reading the listing entries: minutes", "licence": "per item, shown where stated",
                "proof": f"public {channel} listing of {owner}, no key", "use": "none proposed until examined",
                "test": "read the repository's README and latest default-branch commit; record the SHA and release apart",
                "outcome": "TO_TRIAGE (a listing match is a lead, not a reading)"})
            events += [(f"team:{c['ident']}", "signal", "signalled", f"team-explore:{owner}") for c in res["candidates"]]
    if len(new) > 200:
        for key in sorted(new, key=lambda k: new[k].get("last", ""))[:len(new) - 150]:
            del new[key]
    return summary, selected, new, events


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--append-log", action="store_true", help="move pending entries into the scout log")
    parser.add_argument("--status", action="store_true", help="print the last run's one-line status and exit")
    parser.add_argument("--discover-only", action="store_true",
                        help="run only the external search (no watch probes, no PubMed)")
    parser.add_argument("--theme", help="with --discover-only: one theme id or 'all' (default: next in rotation)")
    parser.add_argument("--dry-run", action="store_true", help="with --discover-only: print, write nothing")
    parser.add_argument("--briefing", action="store_true", help="always print the briefing (default: only if non-empty)")
    parser.add_argument("--plan", action="store_true", help="print today's derived plan (questions with origin) and exit")
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
        result = outcome.get("r") or outcome.get("t")
        accepted = bool(result) and (result[0] in ("added", "replaced") if args.follow_add else result[0] is True)
        for note in STATE_NOTES:
            print("NOTE:", note)
        if not accepted:
            print("REFUSED (nothing recorded as accepted):", result)
        elif not ok:
            print("SAVE FAILED:", why, result)
        else:
            print("saved:", result)
        return 0 if (ok and accepted) else 1
    state = read_state(state_path)
    follow = state.get("follow") or follow_seed()
    ctx = resolve_context(state.get("context"), now=now)
    known = known_idents(WATCH, follow, ctx)
    counter = CountingOpener(http)
    plan, extracts, themes, din, per_run = plan_step(state, ctx, cfg, now)
    if args.plan:
        print(f"plan at main {str(plan.get('sha'))[:12]} digest {plan.get('digest')} cache {plan.get('cache')} "
              f"provisional: {plan.get('provisional') or 'no'}")
        for q in plan.get("questions", []):
            print(f"  w{q['weight']} {q['id']} [{q['category']}] terms {q['terms']}\n      because {origin_line(q['origin'])}"
                  f"\n      decision: {q['decision']}")
        return 0
    if args.discover_only:
        result, dstate = discover(din, themes, now=now, only=args.theme, pause=7, opener=counter, known=known,
                                  per_run=per_run, open_slot=cfg["open_slot"] and not args.theme,
                                  deep=cfg["version_checks"], owner_cap=cfg["explore"]["max_per_owner"])
        print(json.dumps(result, indent=1, ensure_ascii=False) if result else "already searched today")
        if result and not args.dry_run:
            entries = discovery_entries(result, now.isoformat())
            asked = state.get("plan_asked") or {}
            if args.theme is None:
                asked = record_asked(asked, result, themes, today)
            ok, why = save_state(state_path, {"discovery": dstate, "context": ctx, "plan": plan, "extracts": extracts,
                                              "plan_asked": asked})
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
        result, new_state["discovery"] = discover(din, themes, now=now, opener=counter, known=known, pause=7,
                                                  per_run=per_run, open_slot=cfg["open_slot"],
                                                  deep=cfg["version_checks"], owner_cap=cfg["explore"]["max_per_owner"])
    except (ValueError, KeyError, TypeError, OSError) as exc:
        result, new_state["discovery"] = None, state.get("discovery", {})
        report["errors"].append(f"discovery: {exc}")
    if result:
        report["discovery"] = {"themes": [r["theme"] for r in result["themes"]], "new_items": result["new_items"],
                               "channels": result["channels"], "questions": result["questions"],
                               "items": [i for r in result["themes"] for i in r["items"]]}
        report["errors"] += [f"{c}: {e}" for c, v in result["channels"].items() for e in v["errors"]]
        report["selected"] += discovery_entries(result, report["run_at"])  # the search keeps its own seen-cache: no baseline
        trace_events += [(i["key"], "signal", "signalled", f"question:{r['theme']}") for r in result["themes"] for i in r["items"]]
    asked = record_asked(state.get("plan_asked") or {}, result, themes, today)
    tsum, tsel, explored, tev = team_step(result, follow, state.get("explored") or {}, themes, known, cfg, counter, now)
    report["teams"] = tsum
    report["errors"] += [f"teams: {e}" for e in tsum["errors"]]
    report["selected"] += tsel  # like the search, exploration keeps its own cache: no baseline gate
    trace_events += tev
    report["plan"] = {"sha": plan.get("sha"), "digest": plan.get("digest"), "cache": plan.get("cache"), "reread": plan.get("reread"),
                      "questions": len(plan.get("questions", [])), "skipped": plan.get("skipped"),
                      "provisional": plan.get("provisional") or [],
                      "inputs": {p: v["blob"][:10] for p, v in plan.get("inputs", {}).items()},
                      "fallback": not plan.get("questions")}
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
            trace_events.append((f"follow:{entry['repo']}:{fp['commit']}", "signal", "signalled", f"follow:{entry['repo']}"))
    report["verdict"] = final_verdict(report)
    report["follow"] = {"active": sum(e["status"] == "active" for e in follow["entries"]), "deep_checked": deep_rows}
    report["http"] = counter.summary()

    def follow_fn(cur):
        for repo, fp in deep_updates:
            for e in cur["entries"]:
                if e["repo"] == repo:
                    e["fp"], e["last_deep"] = fp, now.isoformat(timespec="seconds")
        return cur

    def trace_fn(cur):
        for key, stage, st, via in trace_events:
            trace_event(cur, key, stage, st, at=now.isoformat(timespec="seconds"), via=via)
        return cur
    persisted = {}
    ok, why = save_state(state_path, {"watch": new_state["watch"], "pubmed": new_state["pubmed"],
                                      "discovery": new_state["discovery"], "context": ctx, "plan": plan, "extracts": extracts,
                                      "plan_asked": asked, "explored": explored}, follow_fn, trace_fn)
    persisted["state"] = "ok" if ok else why or "failed"
    report["errors"] += STATE_NOTES
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
