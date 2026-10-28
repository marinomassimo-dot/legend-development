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

A small external SEARCH (one rotating theme a day, two public key-less calls: Europe PMC and the GitHub
repository search) looks for repositories, tools, datasets and methods tied to concrete WWOX gaps.
It de-duplicates against the cache, caps what it shows, and "no useful opportunity" is a valid result.
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
import hashlib
import html
import json
import os
import pwd
import re
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
# External discovery: one rotating theme a day, tied to a concrete WWOX gap (a handful of themes, not
# an inventory of resources). Gap sources: module_blindspots_20261023.md, the batch-selection hand-off,
# the iteration-1 README "Next step" column. Edit a theme when its gap closes; delete it when answered.
THEMES = [
    {"id": "sdr-enzyme-assay", "gap": "WWOX SDR domain: no activity assay or substrate known",
     "epmc": '(TITLE_ABS:WWOX OR TITLE_ABS:SDR16C5 OR TITLE_ABS:"short-chain dehydrogenase") AND '
             '(TITLE_ABS:"substrate screening" OR TITLE_ABS:"activity assay" OR TITLE_ABS:"orphan" OR '
             'TITLE_ABS:"catalytic activity") AND TITLE_ABS:(WWOX OR SDR)',
     "gh": "orphan oxidoreductase substrate prediction"},
    {"id": "isr-atf4-epilepsy", "gap": "ISR/ATF4 modulators in epilepsy or DEE (candidate-class evidence is thin)",
     "epmc": '(TITLE_ABS:"integrated stress response" OR TITLE_ABS:ISRIB OR TITLE_ABS:ATF4 OR TITLE_ABS:GCN2) AND '
             '(TITLE_ABS:epilepsy OR TITLE_ABS:seizure OR TITLE_ABS:"epileptic encephalopathy")',
     "gh": None},
    {"id": "residual-function-chaperone", "gap": "residual-function / chaperone rescue of missense alleles",
     "epmc": '(TITLE_ABS:"pharmacological chaperone" OR TITLE_ABS:"residual function") AND '
             '(TITLE_ABS:"epileptic encephalopathy" OR TITLE_ABS:"neurodevelopmental") AND TITLE_ABS:missense',
     "gh": "variant protein stability ddg"},
    {"id": "dee-drug-response-data", "gap": "paediatric DEE drug-response datasets (a gold set does not exist)",
     "epmc": 'TITLE_ABS:"developmental and epileptic encephalopathy" AND (TITLE_ABS:"treatment response" OR '
             'TITLE_ABS:"drug response" OR TITLE_ABS:"antiseizure") AND (TITLE_ABS:dataset OR TITLE_ABS:registry '
             'OR TITLE_ABS:database)',
     "gh": "epilepsy antiseizure dataset"},
    {"id": "pdh-assay", "gap": "a PDH-specific measure (activity, phosphorylation or flux) is missing",
     "epmc": 'TITLE_ABS:"pyruvate dehydrogenase" AND (TITLE_ABS:"activity assay" OR TITLE_ABS:phosphorylation OR '
             'TITLE_ABS:flux OR TITLE_ABS:biosensor) AND (TITLE_ABS:neuron* OR TITLE_ABS:epilep* OR TITLE_ABS:fibroblast*)',
     "gh": None},
    {"id": "assertion-extraction", "gap": "module blind spot: typed drug assertions from papers and name-to-compound linking",
     "epmc": None, "gh": "drug entity linking"},
    {"id": "neuron-perturbation-signatures", "gap": "context-matched neuronal perturbation signatures for reversal queries",
     "epmc": '(TITLE_ABS:"perturbation signature*" OR TITLE_ABS:L1000 OR TITLE_ABS:"connectivity map") AND '
             '(TITLE_ABS:neuron* OR TITLE_ABS:iPSC) AND (TITLE_ABS:reversal OR TITLE_ABS:repurposing)',
     "gh": "lincs signature reversal"},
]
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
GH_SEARCH = "https://api.github.com/search/repositories"
SHOW = 3  # per source per run; only what is shown is marked seen, the rest waits for the next rotation
NEW_WINDOW_DAYS = 730


def _years_ago(now: dt.datetime, days: int) -> str:
    return (now - dt.timedelta(days=days)).date().isoformat()


def discover_theme(theme: dict, seen: dict, opener=http, now: dt.datetime | None = None) -> dict:
    """Run one theme: at most one Europe PMC call and one GitHub call. Returns {items, errors}; `seen` is updated."""
    now = now or dt.datetime.now(dt.timezone.utc)
    items, errors = [], []
    if theme.get("epmc"):
        query = f"({theme['epmc']}) AND FIRST_PDATE:[{_years_ago(now, NEW_WINDOW_DAYS)} TO {now.date().isoformat()}]"
        url = (f"{EPMC}?format=json&resultType=lite&pageSize=25&query="
               + urllib.parse.quote(query))
        code, _, body = opener(url)
        if code != 200:
            errors.append(f"{theme['id']} europepmc HTTP {code}")
        else:
            fresh = []
            for rec in json.loads(body).get("resultList", {}).get("result", []):
                key = f"epmc:{rec.get('source')}:{rec.get('id')}"
                if key in seen:
                    continue
                fresh.append({"key": key, "kind": "paper" if rec.get("source") != "PPR" else "preprint",
                              "title": re.sub(r"<[^>]+>", "", html.unescape(rec.get("title") or ""))[:140], "when": rec.get("firstPublicationDate"),
                              "venue": rec.get("journalTitle") or rec.get("source"),
                              "open": rec.get("isOpenAccess"), "doi": rec.get("doi"),
                              "url": f"https://europepmc.org/article/{rec.get('source')}/{rec.get('id')}"})
            items += fresh[:SHOW]
            seen.update({i["key"]: now.date().isoformat() for i in fresh[:SHOW]})
    if theme.get("gh"):
        query = f"{theme['gh']} pushed:>{_years_ago(now, NEW_WINDOW_DAYS)} archived:false fork:false"
        url = f"{GH_SEARCH}?per_page=15&sort=updated&q=" + urllib.parse.quote(query)
        code, _, body = opener(url)
        if code != 200:
            errors.append(f"{theme['id']} github HTTP {code}")
        else:
            fresh = []
            for repo in json.loads(body).get("items", []):
                key = f"gh:{repo.get('full_name')}"
                if key in seen:
                    continue
                fresh.append({"key": key, "kind": "repository", "title": repo.get("full_name"),
                              "description": (repo.get("description") or "")[:140],
                              "licence": (repo.get("license") or {}).get("spdx_id") or "none stated",
                              "stars": repo.get("stargazers_count"), "when": repo.get("pushed_at", "")[:10],
                              "url": repo.get("html_url")})
            fresh.sort(key=lambda r: -(r["stars"] or 0))
            items += fresh[:SHOW]
            seen.update({i["key"]: now.date().isoformat() for i in fresh[:SHOW]})
    if len(seen) > 3000:  # bounded cache: keep the newest 2000 keys
        for key in sorted(seen, key=seen.get)[:len(seen) - 2000]:
            del seen[key]
    return {"theme": theme["id"], "gap": theme["gap"], "items": items, "errors": errors}


def discover(dstate: dict, themes=THEMES, opener=http, now: dt.datetime | None = None, only: str | None = None, pause: float = 0):
    """The daily search: the next theme in rotation, once per calendar day (`only`: one theme id or 'all').
    Returns (result | None, new_discovery_state)."""
    now = now or dt.datetime.now(dt.timezone.utc)
    today = now.date().isoformat()
    state = {"cursor": dstate.get("cursor", 0), "last_day": dstate.get("last_day"), "seen": dict(dstate.get("seen", {}))}
    if only is None:
        if state["last_day"] == today:
            return None, state
        chosen = [themes[state["cursor"] % len(themes)]]
        state["cursor"] = (state["cursor"] + 1) % len(themes)
        state["last_day"] = today
    else:
        chosen = [t for t in themes if only == "all" or t["id"] == only]
    results = []
    for number, t in enumerate(chosen):
        if number and pause:
            time.sleep(pause)  # the unauthenticated GitHub search allows about 10 calls a minute
        results.append(discover_theme(t, state["seen"], opener, now))
    return {"themes": results, "new_items": sum(len(r["items"]) for r in results)}, state


def discovery_entries(result: dict, when: str) -> list[dict]:
    out = []
    for res in result["themes"]:
        if not res["items"]:
            continue
        detail = "; ".join(f"[{i['kind']}] {i['title']} ({i.get('when') or '?'}"
                           f"{', ' + i['licence'] if i.get('licence') else ''}) {i['url']}" for i in res["items"])
        out.append({"id": f"Discovery:{res['theme']}", "wwox_question": res["gap"],
                    "contribution_vs_existing": "unchecked: a search hit is the first look (no relevance scoring)",
                    "estimated_cost": "screening: minutes; adoption: unestimated until read (licence, version, provenance)",
                    "licence": "per item (shown where a repository states one)", "detail": detail,
                    "proof": "Europe PMC / GitHub search, public endpoints, no key",
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
    parser.add_argument("--status", action="store_true", help="print the last run's one-line status and exit")
    parser.add_argument("--discover-only", action="store_true",
                        help="run only the external search (no watch probes, no PubMed)")
    parser.add_argument("--theme", help="with --discover-only: one theme id or 'all' (default: next in rotation)")
    parser.add_argument("--dry-run", action="store_true", help="with --discover-only: print, write nothing")
    args = parser.parse_args(argv)
    directory = state_dir()
    if args.append_log:
        return append_log(directory)
    if args.status:
        print(status_line(radar_status(directory)))
        return 0
    state_path = directory / "scout_daily_state.json"
    try:
        state = json.loads(state_path.read_text())
    except (OSError, ValueError):
        state = {}
    now = dt.datetime.now(dt.timezone.utc)
    if args.discover_only:
        result, dstate = discover(state.get("discovery", {}), now=now, only=args.theme, pause=7)
        print(json.dumps(result, indent=1, ensure_ascii=False) if result else "already searched today")
        if result and not args.dry_run:
            state["discovery"] = dstate
            atomic_write(state_path, json.dumps(state, indent=1))
            entries = discovery_entries(result, now.isoformat())
            if entries:
                with open(directory / "scout_daily_pending_log.md", "a") as handle:
                    for item in entries:
                        handle.write(entry_markdown(item, now.isoformat(timespec="seconds")))
        return 0
    report, new_state = run(state)
    try:  # the search is additive: its failure must never hide the probes
        result, new_state["discovery"] = discover(state.get("discovery", {}), now=now)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        result, new_state["discovery"] = None, state.get("discovery", {})
        report["errors"].append(f"discovery: {exc}")
    if result:
        report["discovery"] = {"themes": [r["theme"] for r in result["themes"]], "new_items": result["new_items"],
                               "items": [i for r in result["themes"] for i in r["items"]]}
        report["errors"] += [e for r in result["themes"] for e in r["errors"]]
        if not report["baseline"]:
            report["selected"] += discovery_entries(result, report["run_at"])
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
