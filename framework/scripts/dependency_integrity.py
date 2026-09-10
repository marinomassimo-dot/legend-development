#!/usr/bin/env python3
"""Dependency-integrity propagation: screen what a paper DEPENDS ON, not just the paper.

WHY THIS EXISTS. A per-PMID retraction check (`retraction_check` in the deep-dive
manifests, NCBI ESummary underneath) asks one question: has THIS paper been retracted?
It is per-PMID by construction, so it cannot see the integrity status of the papers a
paper depends on. The 2026-09-09 sweep hit that gap concretely: four papers that read as
four independent bricks share an adenovirus and both antibodies, all descending from
PMID 16223882 (`10.1073/pnas.0505485102`), which carries a standing **expression of
concern whose scope is precisely the loading-control panel** that would license the
quantitative comparison. A per-PMID check over the corpus sees 1 flagged paper. Screening
the corpus's REFERENCE LISTS against the same dataset sees the descent.

The problem is recorded as S7 / H6 in
`disease-models/wwox/analysis/orchestration_reviews/2026-09-09_actor_retrospective.md`
and specified as P1 in
`governance/candidates/2026-09-09_sweep_capability_comparison.md`.

WHAT IT IS NOT. A flag is a **prompt to read**, never a claim about the citing paper.
This tool emits a report and a review queue. It does not annotate, qualify or touch any
claim, any registry, any dossier, or any of the four scientific current files, and it has
no code path that writes to them.

DATA. The Retraction Watch database as hosted by Crossref
(`https://api.labs.crossref.org/data/retractionwatch`), CC0, key-less, zero spend.
Reference lists come from `api.crossref.org/works/<doi>`, already used by
`oa_status_dissent.py`. Python stdlib only. The ~66 MB snapshot lives under `files/`,
which is gitignored; what is versioned is the PIN (sha256, bytes, rows, fetch date, URL)
at `framework/config/retraction_watch_pin.json`.

=============================== KNOWN FAILURE MODES ===============================
Declared up front because a screen that hides these is worse than no screen at all.

1. DOI-LESS REFERENCES ARE INVISIBLE. A reference deposited without a DOI cannot be
   screened by this method. It is reported `UNSCREENABLE_NO_DOI` and is NEVER counted
   as clean. `SCREENED_CLEAN` and `UNSCREENABLE_NO_DOI` are different verdicts and this
   tool will not collapse them: measured here, ~7% of corpus reference DOIs.

2. A PAPER WITH NO DEPOSITED REFERENCE LIST IS NOT A CLEAN PAPER. Crossref returns zero
   references for many deposits (publisher never deposited them). Such a paper gets
   `UNSCREENABLE_NO_REFERENCE_LIST`, not `SCREENED_CLEAN`. This is the same failure class
   as (1) one level up, and it is the larger of the two in this corpus. The neighbouring
   case is `UNSCREENABLE_NO_SCREENABLE_REFERENCES`: a paper that HAS references, none of
   which carries a DOI. Nothing about it was screened, so it is not clean. The first
   version of this file returned `SCREENED_CLEAN` there; its own regression suite caught
   it before the tool shipped, and that assertion is now
   `test_a_paper_whose_references_are_all_doi_less_is_not_clean`.

3. THE INTEGRITY CLASSES ARE NOT INTERCHANGEABLE. `RetractionNature` carries FIVE values
   in the pinned snapshot, not three: `Retraction`, `Expression of concern`, `Correction`,
   `Reinstatement`, and empty. A `Correction` is ordinary scientific housekeeping and is
   noise if treated as an integrity signal; a `Reinstatement` is the OPPOSITE of a flag.
   They are classified separately and never merged. Only `Retraction` and
   `Expression of concern` enter the review queue by default.

4. A DOI CAN CARRY SEVERAL ROWS. A paper may be flagged, then reinstated, or receive an
   expression of concern and later a retraction. Every row for a DOI is kept and the
   paper-level verdict takes the most severe live class, with the full row list retained
   so a reader adjudicates the sequence rather than a summary of it.

5. THE `Reason` FIELD'S SEMANTICS ARE NOT YET HONESTLY DESCRIBABLE. It is a
   semicolon-joined controlled-ish vocabulary of mixed granularity ("Concerns/Issues
   about Data" alongside "Error in Image"). It is passed through VERBATIM and never
   parsed, thresholded or scored. One adjudicated run is required before any claim is
   made about what a Reason means. `_external_repos/MANIFEST.md` records this as the
   open item on the entry.

6. THE SNAPSHOT GOES STALE. The dataset grows daily (72,450 rows on 2026-09-09;
   72,476 on 2026-09-10). `days_since_fetch` is emitted with EVERY verdict, and a screen
   run against a snapshot whose digest does not match the pin fails closed rather than
   reporting clean.

7. 218 ROWS OF THE DATASET ARE UNREACHABLE BY THIS METHOD. Every row whose
   `RetractionNature` is blank ALSO carries no `OriginalPaperDOI` (measured over the
   pinned snapshot, 218 of 218), so a DOI-keyed screen cannot see any of them. The
   `FLAGGED_NATURE_UNCLASSIFIED` branch is therefore live for a future snapshot and
   dead for this one, and the regression suite measures that rather than assuming it.

8. A MALFORMED DOI IS UNSCREENABLE, NOT CLEAN. A DOI prefix is `10.` plus 4-9 digits;
   anything else falls to `UNSCREENABLE_NO_DOI`. The direction of that failure is
   deliberate — a reference this tool cannot parse is one it did not screen.

9. FAIL-CLOSED. No snapshot, a digest mismatch, or a network failure fetching a
   reference list produces an UNSCREENABLE verdict and a non-zero exit — never a clean
   one. The failure this most guards against is the sweep's worst near-error: a screen
   that returned CLEAN without screening anything.
===================================================================================

VERDICT SHAPE. `framework/scripts/screen_verdict.py` did not exist when this was written
(`git log --oneline -- framework/scripts/screen_verdict.py` was empty on 2026-09-10), so
this module carries the same shape itself: an explicit `screened` boolean alongside the
verdict string, so that "not flagged" can never be read off a reference that was never
looked at. If that module lands later, `VERDICTS` here is the surface to reconcile.

MINIMUM REPRODUCIBLE INVOCATION
    python3 framework/scripts/dependency_integrity.py fetch      # ~66 MB, key-less, free
    python3 framework/scripts/dependency_integrity.py pin --write
    python3 framework/scripts/dependency_integrity.py control    # positive control
    python3 framework/scripts/dependency_integrity.py screen --doi 10.1093/brain/awab174
    python3 framework/scripts/dependency_integrity.py corpus --json out.json
    python3 framework/scripts/dependency_integrity.py selftest

CONTACT PARAMETER. The Crossref labs endpoint documents a `mailto` contact parameter.
This tool sends NO email address, ever: there is no code path that accepts one, and the
endpoint was measured on 2026-09-10 serving the complete CSV without it (HTTP 200,
`content-disposition: attachment; filename=retractions.csv`). Sending the operator's
personal address to an external service is out of scope by construction, not by default.
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import growth_anchors  # noqa: E402 - the single definition of a canonical record heading

csv.field_size_limit(10 ** 9)

RETRACTION_WATCH_URL = "https://api.labs.crossref.org/data/retractionwatch"
CROSSREF_WORKS = "https://api.crossref.org/works/"
USER_AGENT = "LEGEND/3.3.1 (dependency-integrity screen; stdlib urllib)"
TIMEOUT = 60

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PIN_PATH = os.path.join(REPO_ROOT, "framework", "config", "retraction_watch_pin.json")
SNAPSHOT_DIR = os.path.join(REPO_ROOT, "files", "retraction_watch")
REFS_CACHE = os.path.join(SNAPSHOT_DIR, "refs_cache")
MANIFEST_DIR = os.path.join(
    REPO_ROOT, "disease-models", "wwox", "research", "deepdive_manifests"
)
# READ-ONLY. These two are opened for reading only, to answer "which claims stand on a
# paper with a flagged dependency". This tool has no write path to either, and
# `test_no_canonical_surface_is_ever_opened_for_writing` asserts that mechanically.
_REG = os.path.join(REPO_ROOT, "disease-models", "wwox", "registries")
PAPER_REGISTRY_RO = os.path.join(_REG, "paper_registry_current.md")
CLAIM_REGISTRY_RO = os.path.join(_REG, "claim_registry_current.md")

# The record-heading matchers come from growth_anchors and are NEVER respelled here: a
# second copy is the 2026-08-08 defect. The paper registry carries CORPUS placeholders as
# well as PAPER records, so BOTH conventions are passed — a splitter given only `papers`
# does not merely miss the placeholders, their bodies join the PAPER record above them.
PAPER_HEADING = growth_anchors.heading_re("papers", "corpus")
CLAIM_HEADING = growth_anchors.heading_re("claims")

# --- verdicts -------------------------------------------------------------
# `screened` is part of the verdict, not a derived convenience: a caller must not be
# able to read "not flagged" off a reference that was never looked at.
V_CLEAN = "SCREENED_CLEAN"
V_NO_DOI = "UNSCREENABLE_NO_DOI"
V_NO_REFS = "UNSCREENABLE_NO_REFERENCE_LIST"
V_NO_SCREENABLE = "UNSCREENABLE_NO_SCREENABLE_REFERENCES"
V_NO_SNAPSHOT = "UNSCREENABLE_NO_SNAPSHOT"
V_FETCH_FAILED = "UNSCREENABLE_FETCH_FAILED"
V_RETRACTION = "FLAGGED_RETRACTION"
V_EOC = "FLAGGED_EXPRESSION_OF_CONCERN"
V_CORRECTION = "NOTED_CORRECTION"
V_REINSTATEMENT = "NOTED_REINSTATEMENT"
V_UNCLASSIFIED = "FLAGGED_NATURE_UNCLASSIFIED"

# Only these two are integrity flags. A Correction is housekeeping; a Reinstatement is
# the opposite of a flag. Kept as a frozenset so the distinction is one edit away from
# being audited, never one edit away from being lost.
INTEGRITY_FLAGS = frozenset({V_RETRACTION, V_EOC, V_UNCLASSIFIED})
UNSCREENABLE = frozenset(
    {V_NO_DOI, V_NO_REFS, V_NO_SCREENABLE, V_NO_SNAPSHOT, V_FETCH_FAILED}
)

# Severity order for picking a paper-level verdict; higher is more severe.
_SEVERITY = {
    V_REINSTATEMENT: 0,
    V_CLEAN: 1,
    V_CORRECTION: 2,
    V_UNCLASSIFIED: 3,
    V_EOC: 4,
    V_RETRACTION: 5,
}

_NATURE_MAP = {
    "retraction": V_RETRACTION,
    "expression of concern": V_EOC,
    "correction": V_CORRECTION,
    "reinstatement": V_REINSTATEMENT,
}

_DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>]+")


def normalise_doi(raw):
    """Return a lowercase bare DOI, or None if there is no DOI in `raw`.

    Returning None rather than "" matters: the caller must branch on absence, and an
    empty string compares equal to nothing while still being a str.
    """
    if not raw:
        return None
    text = str(raw).strip()
    if not text:
        return None
    text = text.replace("doi:", " ").replace("DOI:", " ")
    match = _DOI_RE.search(text)
    if not match:
        return None
    doi = match.group(0).rstrip(").,;'\"")
    return doi.lower()


def classify_nature(nature):
    """Map a RetractionNature cell onto a verdict. Never collapses the classes."""
    key = (nature or "").strip().lower()
    if not key:
        return V_UNCLASSIFIED
    return _NATURE_MAP.get(key, V_UNCLASSIFIED)


# --- snapshot and pin -----------------------------------------------------

def _digest_and_size(path):
    sha = hashlib.sha256()
    size = 0
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            sha.update(chunk)
            size += len(chunk)
    return sha.hexdigest(), size


def snapshot_path(pin=None):
    """The snapshot named by the pin, else the newest snapshot on disk."""
    if pin and pin.get("filename"):
        candidate = os.path.join(SNAPSHOT_DIR, pin["filename"])
        if os.path.exists(candidate):
            return candidate
    if not os.path.isdir(SNAPSHOT_DIR):
        return None
    found = sorted(
        f for f in os.listdir(SNAPSHOT_DIR)
        if f.startswith("retractionwatch_") and f.endswith(".csv")
    )
    return os.path.join(SNAPSHOT_DIR, found[-1]) if found else None


def read_pin(path=PIN_PATH):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def count_rows(path):
    n = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for _ in csv.DictReader(fh):
            n += 1
    return n


def fetch_snapshot(dest=None):
    """One key-less HTTP GET. No email is sent: the endpoint serves without one."""
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    stamp = _dt.date.today().strftime("%Y%m%d")
    dest = dest or os.path.join(SNAPSHOT_DIR, "retractionwatch_%s.csv" % stamp)
    req = urllib.request.Request(RETRACTION_WATCH_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=900) as resp, open(dest, "wb") as out:
        while True:
            chunk = resp.read(1 << 20)
            if not chunk:
                break
            out.write(chunk)
    return dest


def build_pin(path):
    sha, size = _digest_and_size(path)
    return {
        "resource": "Retraction Watch database, hosted by Crossref",
        "url": RETRACTION_WATCH_URL,
        "licence": "CC0",
        "filename": os.path.basename(path),
        "sha256": sha,
        "bytes": size,
        "rows": count_rows(path),
        "fetched": _dt.date.today().isoformat(),
        "note": (
            "The snapshot itself is ~66 MB and lives under files/, which is gitignored. "
            "This pin is what is versioned. Re-fetch with `dependency_integrity.py "
            "fetch`; a changed row count is a signal, not an error. No email address is "
            "sent to the endpoint."
        ),
    }


def verify_snapshot(pin=None):
    """Return (path, pin, problems). Fails closed: any problem means do not screen."""
    pin = pin or read_pin()
    problems = []
    if pin is None:
        return None, None, ["no pin at %s" % PIN_PATH]
    path = snapshot_path(pin)
    if path is None or not os.path.exists(path):
        return None, pin, [
            "snapshot %s absent under files/retraction_watch/ "
            "(run: dependency_integrity.py fetch)" % pin.get("filename")
        ]
    sha, size = _digest_and_size(path)
    if size != pin.get("bytes"):
        problems.append("byte count %d != pinned %s" % (size, pin.get("bytes")))
    if sha != pin.get("sha256"):
        problems.append("sha256 %s != pinned %s" % (sha[:16], str(pin.get("sha256"))[:16]))
    return path, pin, problems


def days_since_fetch(pin):
    try:
        fetched = _dt.date.fromisoformat(pin["fetched"])
    except (KeyError, TypeError, ValueError):
        return None
    return (_dt.date.today() - fetched).days


# --- the index ------------------------------------------------------------

def load_index(path):
    """doi -> list of row dicts. Every row is kept (failure mode 4)."""
    index = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            doi = normalise_doi(row.get("OriginalPaperDOI"))
            if not doi:
                continue
            index.setdefault(doi, []).append({
                "record_id": (row.get("Record ID") or "").strip(),
                "title": (row.get("Title") or "").strip(),
                "journal": (row.get("Journal") or "").strip(),
                "original_doi": doi,
                "original_pmid": (row.get("OriginalPaperPubMedID") or "").strip(),
                "nature": (row.get("RetractionNature") or "").strip(),
                "verdict": classify_nature(row.get("RetractionNature")),
                "retraction_pmid": (row.get("RetractionPubMedID") or "").strip(),
                "retraction_date": (row.get("RetractionDate") or "").strip(),
                # Reason is passed through verbatim and never parsed (failure mode 5).
                "reason": (row.get("Reason") or "").strip(),
            })
    return index


# --- screening ------------------------------------------------------------

def screen_reference(raw_doi, index, stale_days=None):
    """Screen ONE reference. The unit that must never report clean without looking."""
    doi = normalise_doi(raw_doi)
    if doi is None:
        return {
            "doi": None, "raw": raw_doi, "screened": False,
            "verdict": V_NO_DOI, "rows": [],
            "days_since_fetch": stale_days,
        }
    if index is None:
        return {
            "doi": doi, "raw": raw_doi, "screened": False,
            "verdict": V_NO_SNAPSHOT, "rows": [],
            "days_since_fetch": stale_days,
        }
    rows = index.get(doi, [])
    if not rows:
        verdict = V_CLEAN
    else:
        verdict = max((r["verdict"] for r in rows), key=lambda v: _SEVERITY.get(v, 3))
    return {
        "doi": doi, "raw": raw_doi, "screened": True,
        "verdict": verdict, "rows": rows,
        "days_since_fetch": stale_days,
    }


def _get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as fh:
        return json.loads(fh.read().decode("utf-8"))


def crossref_references(doi, cache_dir=REFS_CACHE, offline=False, sleep=0.0):
    """Reference list for a DOI. Cached under files/ so a corpus run is repeatable.

    Returns (references, source) where source is 'cache', 'network' or an error string.
    A reference entry is the raw Crossref dict; the DOI may be absent from it, and that
    absence is the point of failure mode 1 — it is preserved, not filtered away.
    """
    key = re.sub(r"[^a-z0-9]+", "_", (normalise_doi(doi) or "none"))
    cache_file = os.path.join(cache_dir, key + ".json")
    if os.path.exists(cache_file):
        with open(cache_file, encoding="utf-8") as fh:
            return json.load(fh), "cache"
    if offline:
        return None, "offline-not-cached"
    url = CROSSREF_WORKS + urllib.parse.quote(doi)
    try:
        data = _get_json(url)
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, ValueError) as exc:
        return None, "error:%s" % type(exc).__name__
    refs = (data.get("message") or {}).get("reference") or []
    os.makedirs(cache_dir, exist_ok=True)
    tmp = cache_file + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(refs, fh)
    os.replace(tmp, cache_file)
    if sleep:
        time.sleep(sleep)
    return refs, "network"


def screen_paper(doi, index, pmid=None, offline=False, stale_days=None, sleep=0.0):
    """Screen every reference of ONE paper. The entry point `selftest` exercises."""
    refs, source = crossref_references(doi, offline=offline, sleep=sleep)
    base = {
        "pmid": pmid, "doi": normalise_doi(doi), "reference_source": source,
        "days_since_fetch": stale_days,
    }
    if refs is None:
        base.update({
            "paper_verdict": V_FETCH_FAILED, "screened": False,
            "references_declared": 0, "references_with_doi": 0,
            "screened_count": 0, "unscreenable_no_doi": 0,
            "flagged": [], "counts": {},
        })
        return base
    results = [screen_reference(r.get("DOI"), index, stale_days) for r in refs]
    counts = {}
    for r in results:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    flagged = [r for r in results if r["verdict"] in INTEGRITY_FLAGS]
    with_doi = sum(1 for r in results if r["doi"])
    if not results:
        # A paper whose publisher deposited no reference list is NOT a clean paper.
        paper_verdict = V_NO_REFS
        screened = False
    elif flagged:
        paper_verdict = max(
            (r["verdict"] for r in flagged), key=lambda v: _SEVERITY.get(v, 3)
        )
        screened = True
    elif index is None:
        paper_verdict, screened = V_NO_SNAPSHOT, False
    elif counts.get(V_NO_DOI, 0) == len(results):
        # References exist but not one of them could be screened. Nothing was looked at,
        # so nothing is clean — the sweep's worst near-error, refused here by construction.
        paper_verdict, screened = V_NO_SCREENABLE, False
    else:
        paper_verdict, screened = V_CLEAN, True
    base.update({
        "paper_verdict": paper_verdict,
        "screened": screened,
        "references_declared": len(results),
        "references_with_doi": with_doi,
        "screened_count": counts.get(V_CLEAN, 0) + sum(
            counts.get(v, 0) for v in
            (V_RETRACTION, V_EOC, V_CORRECTION, V_REINSTATEMENT, V_UNCLASSIFIED)
        ),
        "unscreenable_no_doi": counts.get(V_NO_DOI, 0),
        "counts": counts,
        "flagged": [
            {"doi": r["doi"], "verdict": r["verdict"], "rows": r["rows"]}
            for r in flagged
        ],
        # Corrections and reinstatements are reported separately from flags, on purpose.
        "noted": [
            {"doi": r["doi"], "verdict": r["verdict"], "rows": r["rows"]}
            for r in results
            if r["verdict"] in (V_CORRECTION, V_REINSTATEMENT)
        ],
    })
    return base


def corpus_papers(manifest_dir=MANIFEST_DIR):
    """(pmid, doi) for every deep-dive manifest that carries a usable DOI."""
    out = []
    if not os.path.isdir(manifest_dir):
        return out
    for name in sorted(os.listdir(manifest_dir)):
        if not (name.startswith("PMID") and name.endswith(".json")):
            continue
        try:
            with open(os.path.join(manifest_dir, name), encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError):
            continue
        out.append((str(data.get("pmid") or name[4:-5]), normalise_doi(data.get("doi"))))
    return out


# --- claim chain (read-only) ----------------------------------------------

def paper_pmids(path=PAPER_REGISTRY_RO):
    """PAPER number -> PMID, read from the registry. Never written to."""
    out = {}
    if not os.path.exists(path):
        return out
    current = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            head = PAPER_HEADING.match(line.rstrip("\n"))
            if head:
                ident = head.group(1)
                current = (ident.split()[1].lstrip("0") or "0"
                           if ident.startswith("PAPER") else None)
                continue
            if current and line.startswith("**Identifier:**"):
                m = re.search(r"PMID\s*(\d{6,9})", line)
                if m:
                    out[current] = m.group(1)
                current = None
    return out


def claim_paper_links(path=CLAIM_REGISTRY_RO):
    """CLAIM number -> set of PAPER numbers it wikilinks. Never written to."""
    out = {}
    if not os.path.exists(path):
        return out
    current = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            head = CLAIM_HEADING.match(line.rstrip("\n"))
            if head:
                current = head.group(1).split()[1].lstrip("0") or "0"
                out.setdefault(current, set())
                continue
            if current:
                for m in re.finditer(r"paper_registry_current#PAPER\s+(\d+)", line):
                    out[current].add(m.group(1).lstrip("0") or "0")
    return out


def claims_touching(flagged_pmids, papers=None, claims=None):
    """Claims whose wikilinked papers include one carrying a flagged dependency."""
    papers = papers if papers is not None else paper_pmids()
    claims = claims if claims is not None else claim_paper_links()
    hits = {}
    for claim, paper_nums in claims.items():
        touched = {}
        for num in paper_nums:
            pmid = papers.get(num)
            if pmid and pmid in flagged_pmids:
                touched[pmid] = sorted(flagged_pmids[pmid])
        if touched:
            hits[claim] = touched
    return hits


# --- positive control -----------------------------------------------------

CONTROL_DOI = "10.1073/pnas.0505485102"
CONTROL_EXPECT = {
    "original_pmid": "16223882",
    "verdict": V_EOC,
    "retraction_pmid": "28373548",
}


def positive_control(index):
    """PMID 16223882 must reproduce, or the screen is not built."""
    rows = index.get(CONTROL_DOI, []) if index else []
    problems = []
    if not rows:
        return False, ["control DOI %s absent from the snapshot" % CONTROL_DOI], rows
    row = rows[0]
    for key, want in CONTROL_EXPECT.items():
        if row.get(key) != want:
            problems.append("%s = %r, expected %r" % (key, row.get(key), want))
    reason = (row.get("reason") or "").lower()
    if "image" not in reason:
        problems.append("Reason does not name image duplication/error: %r" % reason)
    return (not problems), problems, rows


# --- rendering ------------------------------------------------------------

def _stale_line(pin):
    d = days_since_fetch(pin) if pin else None
    if d is None:
        return "snapshot age: UNKNOWN (no usable pin date)"
    return "snapshot age: %d day(s) since fetch (%s)" % (d, pin.get("fetched"))


def render_paper(res):
    lines = []
    lines.append("PMID %s  DOI %s" % (res.get("pmid") or "-", res.get("doi") or "-"))
    lines.append("  paper verdict : %s (screened=%s)" % (res["paper_verdict"], res["screened"]))
    lines.append("  references    : %d declared, %d with DOI, %d screened, %d UNSCREENABLE_NO_DOI"
                 % (res["references_declared"], res["references_with_doi"],
                    res["screened_count"], res["unscreenable_no_doi"]))
    for f in res.get("flagged", []):
        for row in f["rows"]:
            lines.append("  FLAG %s  %s" % (f["verdict"], f["doi"]))
            lines.append("       nature=%s  retraction_pmid=%s  date=%s"
                         % (row["nature"], row["retraction_pmid"], row["retraction_date"]))
            lines.append("       reason(verbatim)=%s" % row["reason"])
            lines.append("       title=%s" % row["title"][:100])
    for f in res.get("noted", []):
        lines.append("  note %s  %s  (NOT an integrity flag)" % (f["verdict"], f["doi"]))
    return "\n".join(lines)


# --- commands -------------------------------------------------------------

def _load_or_fail(args):
    path, pin, problems = verify_snapshot()
    if problems:
        sys.stderr.write("SNAPSHOT UNUSABLE — failing closed, nothing is reported clean:\n")
        for p in problems:
            sys.stderr.write("  - %s\n" % p)
        return None, pin, 3
    return load_index(path), pin, 0


def cmd_fetch(args):
    dest = fetch_snapshot()
    sha, size = _digest_and_size(dest)
    print("fetched %s\n  bytes=%d\n  sha256=%s" % (dest, size, sha))
    print("  rows=%d" % count_rows(dest))
    print("no email address was sent to the endpoint")
    print("next: dependency_integrity.py pin --write")
    return 0


def cmd_pin(args):
    path = snapshot_path(read_pin())
    if path is None:
        sys.stderr.write("no snapshot under %s (run: fetch)\n" % SNAPSHOT_DIR)
        return 3
    pin = build_pin(path)
    if args.write:
        os.makedirs(os.path.dirname(PIN_PATH), exist_ok=True)
        with open(PIN_PATH, "w", encoding="utf-8") as fh:
            json.dump(pin, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print("wrote %s" % PIN_PATH)
    print(json.dumps(pin, indent=2, sort_keys=True))
    return 0


def cmd_verify(args):
    path, pin, problems = verify_snapshot()
    if pin is None:
        sys.stderr.write("no pin at %s\n" % PIN_PATH)
        return 3
    print(_stale_line(pin))
    if problems:
        for p in problems:
            print("PROBLEM: %s" % p)
        return 3
    print("VERIFIED %s" % path)
    print("  rows=%s bytes=%s sha256=%s" % (pin["rows"], pin["bytes"], pin["sha256"]))
    return 0


def cmd_control(args):
    index, pin, rc = _load_or_fail(args)
    if rc:
        return rc
    ok, problems, rows = positive_control(index)
    print(_stale_line(pin))
    for row in rows:
        print("Title:  %s" % row["title"])
        print("OriginalPaperDOI: %s   OriginalPaperPubMedID: %s"
              % (row["original_doi"], row["original_pmid"]))
        print("RetractionNature: %s     RetractionPubMedID: %s"
              % (row["nature"], row["retraction_pmid"]))
        print("Reason: %s" % row["reason"])
        print("verdict: %s" % row["verdict"])
    if ok:
        print("POSITIVE CONTROL: PASS")
        return 0
    for p in problems:
        print("POSITIVE CONTROL FAIL: %s" % p)
    return 1


def cmd_screen(args):
    index, pin, rc = _load_or_fail(args)
    if rc:
        return rc
    stale = days_since_fetch(pin)
    print(_stale_line(pin))
    worst = 0
    for doi in args.doi:
        res = screen_paper(doi, index, offline=args.offline, stale_days=stale)
        print(render_paper(res))
        if res["paper_verdict"] in INTEGRITY_FLAGS:
            worst = max(worst, 1)
        elif not res["screened"]:
            worst = max(worst, 2)
    return 0 if not args.strict else worst


def cmd_corpus(args):
    index, pin, rc = _load_or_fail(args)
    if rc:
        return rc
    stale = days_since_fetch(pin)
    papers = corpus_papers(args.manifest_dir)
    results, no_doi_papers = [], []
    for pmid, doi in papers:
        if not doi:
            no_doi_papers.append(pmid)
            continue
        if args.limit and len(results) >= args.limit:
            break
        res = screen_paper(doi, index, pmid=pmid, offline=args.offline,
                           stale_days=stale, sleep=args.sleep)
        results.append(res)
        if args.verbose:
            print(render_paper(res))

    refs_declared = sum(r["references_declared"] for r in results)
    refs_screened = sum(r["screened_count"] for r in results)
    refs_no_doi = sum(r["unscreenable_no_doi"] for r in results)
    flagged_papers = [r for r in results if r["paper_verdict"] in INTEGRITY_FLAGS]
    unscreenable_papers = [r for r in results if r["paper_verdict"] in UNSCREENABLE]
    clean_papers = [r for r in results if r["paper_verdict"] == V_CLEAN]

    dep_counter = {}
    for r in flagged_papers:
        for f in r["flagged"]:
            dep_counter.setdefault(f["doi"], {"verdict": f["verdict"], "citing": []})
            dep_counter[f["doi"]]["citing"].append(r["pmid"])

    print("")
    print("=== DEPENDENCY-INTEGRITY SCREEN — corpus ===")
    print(_stale_line(pin))
    print("manifests with a DOI screened     : %d" % len(results))
    print("manifests with no DOI (unscreened): %d  %s"
          % (len(no_doi_papers), ",".join(no_doi_papers) if no_doi_papers else ""))
    print("papers with >=1 flagged dependency: %d" % len(flagged_papers))
    print("papers SCREENED_CLEAN             : %d" % len(clean_papers))
    print("papers UNSCREENABLE               : %d" % len(unscreenable_papers))
    for v in sorted({r["paper_verdict"] for r in unscreenable_papers}):
        print("    %-34s %d" % (v, sum(1 for r in unscreenable_papers if r["paper_verdict"] == v)))
    print("reference DOIs screened / declared : %d / %d  (coverage %.1f%%)"
          % (refs_screened, refs_declared,
             100.0 * refs_screened / refs_declared if refs_declared else 0.0))
    print("references UNSCREENABLE_NO_DOI     : %d  (NOT counted clean)" % refs_no_doi)
    print("")
    print("--- review queue: flagged dependencies, most-cited first ---")
    for doi, info in sorted(dep_counter.items(), key=lambda kv: -len(kv[1]["citing"])):
        print("%s  %s  cited by %d corpus paper(s): %s"
              % (info["verdict"], doi, len(info["citing"]), ",".join(sorted(info["citing"]))))
    print("")
    print("A flag is a prompt to read. It is not a claim about the citing paper.")

    if args.json:
        payload = {
            "generated": _dt.datetime.now().isoformat(timespec="seconds"),
            "pin": pin, "days_since_fetch": stale,
            "papers": results, "no_doi_papers": no_doi_papers,
            "review_queue": dep_counter,
            "totals": {
                "papers_screened": len(results),
                "papers_flagged": len(flagged_papers),
                "papers_clean": len(clean_papers),
                "papers_unscreenable": len(unscreenable_papers),
                "refs_declared": refs_declared,
                "refs_screened": refs_screened,
                "refs_no_doi": refs_no_doi,
            },
        }
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=1, sort_keys=True)
        print("wrote %s" % args.json)
    return 0


def cmd_claims(args):
    """Join a corpus screen onto the claim registry. READ-ONLY, and emits no edit."""
    with open(args.from_json, encoding="utf-8") as fh:
        payload = json.load(fh)
    flagged = {}
    for paper in payload.get("papers", []):
        if paper.get("paper_verdict") in INTEGRITY_FLAGS:
            flagged[str(paper.get("pmid"))] = {
                f["doi"] for f in paper.get("flagged", [])
            }
    papers, claims = paper_pmids(), claim_paper_links()
    hits = claims_touching(flagged, papers, claims)
    print("=== CLAIMS WHOSE PRIMARY CHAIN TOUCHES A FLAGGED PAPER ===")
    print("snapshot age: %s day(s)" % payload.get("days_since_fetch"))
    print("claims in registry             : %d" % len(claims))
    print("papers resolved to a PMID      : %d" % len(papers))
    print("corpus papers flagged          : %d" % len(flagged))
    print("claims touching a flagged paper: %d" % len(hits))
    for claim in sorted(hits, key=lambda c: int(c)):
        for pmid, dois in sorted(hits[claim].items()):
            print("  CLAIM %s  via PMID %s  ->  %s" % (claim, pmid, ", ".join(dois)))
    print("")
    print("This is a READING DEBT, not a defect and not a claim about any claim.")
    print("Nothing here edits a registry; adjudication is the scientists'.")
    return 0


def cmd_selftest(args):
    """Self-test that CALLS THE ENTRY POINT on a real corpus artefact.

    Three tools shipped in one day whose self-tests were green while the tool crashed in
    production, one because its self-test never called the function it was testing. This
    one calls `screen_paper` — the function `corpus` calls — on a manifest from
    `deepdive_manifests/`, and asserts the positive control through the same index the
    screen uses.
    """
    failures = []
    path, pin, problems = verify_snapshot()
    if problems:
        for p in problems:
            failures.append("snapshot: %s" % p)
        print("SELFTEST: FAIL (snapshot unusable)")
        for f in failures:
            print("  - %s" % f)
        return 3
    index = load_index(path)

    ok, probs, _rows = positive_control(index)
    if not ok:
        failures.extend("positive control: %s" % p for p in probs)

    papers = corpus_papers()
    if not papers:
        failures.append("no corpus manifests found at %s" % MANIFEST_DIR)
    target = None
    for pmid, doi in papers:
        if doi and os.path.exists(os.path.join(
                REFS_CACHE, re.sub(r"[^a-z0-9]+", "_", doi) + ".json")):
            target = (pmid, doi)
            break
    if target is None:
        target = next(((p, d) for p, d in papers if d), (None, None))
    if target[1] is None:
        failures.append("no corpus manifest carries a usable DOI")
    else:
        res = screen_paper(target[1], index, pmid=target[0],
                           offline=args.offline, stale_days=days_since_fetch(pin))
        print("selftest called screen_paper() on PMID %s (%s)" % (target[0], target[1]))
        print(render_paper(res))
        for key in ("paper_verdict", "screened", "references_declared",
                    "references_with_doi", "unscreenable_no_doi", "counts"):
            if key not in res:
                failures.append("screen_paper() output missing %r" % key)
        if res.get("paper_verdict") == V_CLEAN and res.get("references_declared", 0) == 0:
            failures.append("a paper with 0 references was reported SCREENED_CLEAN")
        if res.get("screened") and res.get("paper_verdict") in UNSCREENABLE:
            failures.append("screened=True with an UNSCREENABLE verdict")

    # The invariant the whole tool exists to protect.
    probe = screen_reference(None, index)
    if probe["verdict"] != V_NO_DOI or probe["screened"]:
        failures.append("a DOI-less reference did not return UNSCREENABLE_NO_DOI")
    probe2 = screen_reference("10.1073/pnas.0505485102", index)
    if probe2["verdict"] != V_EOC:
        failures.append("control DOI screened as %s, expected %s" % (probe2["verdict"], V_EOC))

    print("")
    if failures:
        print("SELFTEST: FAIL")
        for f in failures:
            print("  - %s" % f)
        return 1
    print("SELFTEST: PASS")
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        description=__doc__.split("\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("fetch", help="download the CC0 snapshot (key-less, no email sent)")

    q = sub.add_parser("pin", help="compute the pin over the local snapshot")
    q.add_argument("--write", action="store_true", help="write %s" % PIN_PATH)

    sub.add_parser("verify", help="verify the local snapshot against the pin")
    sub.add_parser("control", help="run the positive control (PMID 16223882)")

    s = sub.add_parser("screen", help="screen one or more papers' reference lists")
    s.add_argument("--doi", action="append", required=True)
    s.add_argument("--offline", action="store_true", help="cached reference lists only")
    s.add_argument("--strict", action="store_true", help="non-zero exit on flag/unscreenable")

    c = sub.add_parser("corpus", help="screen every deep-dive manifest")
    c.add_argument("--manifest-dir", default=MANIFEST_DIR)
    c.add_argument("--offline", action="store_true")
    c.add_argument("--limit", type=int, default=0)
    c.add_argument("--sleep", type=float, default=0.0)
    c.add_argument("--json", default=None)
    c.add_argument("--verbose", action="store_true")

    cl = sub.add_parser("claims", help="join a corpus screen onto the claim registry")
    cl.add_argument("--from-json", required=True, help="output of `corpus --json`")

    t = sub.add_parser("selftest", help="call the entry point on a real corpus artefact")
    t.add_argument("--offline", action="store_true")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return {
        "fetch": cmd_fetch, "pin": cmd_pin, "verify": cmd_verify,
        "control": cmd_control, "screen": cmd_screen, "corpus": cmd_corpus,
        "claims": cmd_claims,
        "selftest": cmd_selftest,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
