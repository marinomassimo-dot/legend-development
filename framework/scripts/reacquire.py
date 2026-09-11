#!/usr/bin/env python3
"""Replay an acquisition recipe and diff the digest — census P2, built 2026-09-10.

WHY THIS EXISTS. `files/` is gitignored for copyright reasons, so a fresh checkout holds
none of the bytes its deep-dive manifests fingerprint. Measured on this host on 2026-09-10,
the day after the repository changed hosts: 81 manifests, 616 declared artefacts, 0 of 616
versioned, 398 absent, 0 digests drifted. The digest half of the chain is in perfect health
and the transport half does not exist — every verification of a prior reading requires
re-acquisition, and re-acquisition is the fragile thing: a 19-tier cascade had to be
reconstructed by hand for one paper (2026-09-09.md § 6.1).

The repository already solved the identical constraint one layer down.
`regenerate_adjudications.py` publishes the RECIPE for a page crop — source digest, page,
rectangle, dpi, result digest — never the reproduction. Acquisitions carried a digest and no
recipe. This tool is the other half: it replays an `acquisition_recipe` (deep-dive manifest,
`source_artifacts[].acquisition_recipe`, validated by `deepdive_manifest.py`) and says, as a
RECORD and not as a boolean, what it did and what came back.

VERDICTS — records that say what they did (`screen_verdict.py`'s rule, applied to transport)

    RECOVERED                    the route replayed and the bytes hash to the declared digest
    EXTRACTOR_DRIFT              a DERIVED artefact regenerated to a different digest under a
                                 different extractor version; the record names BOTH versions
                                 (receipt-era vs this host). Not tampering: a MuPDF change.
    DIGEST_DIFFERS_SAME_ROUTE    a FETCHED binary came back from the same route with a different
                                 digest. A finding about the publisher — a re-typeset PDF, a
                                 changed deposit — and NOT `TAMPERED` by default. The record
                                 carries both digests and both sizes; a human decides.
    DIGEST_DIFFERS_SAME_EXTRACTOR  a derived artefact differs under the SAME extractor version:
                                 the recipe is underspecified (e.g. the page join), or the
                                 source is not the source. Named separately from drift.
    FAILED_<cause>               the route did not return the artefact, and the cause is named:
                                 HTTP_403_CLOUDFLARE (server: cloudflare / cf-ray present),
                                 HTTP_<code>, RECAPTCHA (a 200 that is a Google reCAPTCHA
                                 page), POW_UNSOLVED, NOT_THE_ARTEFACT (a 200 whose bytes are
                                 not the declared kind), NETWORK, TIMEOUT, SOURCE_ABSENT (a
                                 derived artefact whose source is not on this host),
                                 SOURCE_DIGEST_MISMATCH, EXTRACTOR_UNAVAILABLE, UNSUPPORTED,
                                 OFFLINE.
    NO_RECIPE                    nothing to replay. The reason travels with the verdict when a
                                 back-fill line states one.

THE VERSIONED HOME. `.gitignore` promised `files/fulltext/_retrieval_manifest.jsonl`, which
sits under `files/` and is therefore lost by construction — the census calls this the root
of the problem. The retrieval outcome now lives at a TRACKED path,
`disease-models/<disease>/research/retrieval_manifest.jsonl`, append-only, one JSON line per
event: a back-filled recipe, a stated NO_RECIPE, a replay, or a fresh acquisition. Nothing
copyrighted is in it — URLs, tiers, policies, digests, verdicts and dates.

THE BACK-FILL IS DECLAREDLY INCOMPLETE. `backfill` reads every manifest's artefact notes,
`route` and `extraction` fields and writes a recipe ONLY where the note shows the route:
an efetch call with its PMCID, a Europe PMC fullTextXML or pdf=render route with its PMCID, a
quoted URL, a `pmc_pow_fetch.py` retrieval from PMC (route shown; the URL form inferred and
labelled as such), or a derived extraction whose call AND join are stated. Everything else
gets a NO_RECIPE line with the reason class. A route the note does not show is not invented.

DETERMINISM, declared up front (census § 2 P2). Extraction receipts in this repository were
written under PyMuPDF 1.26.5; this host carries 1.28.2, pinned in `requirements-analysis.txt`
since this task. A derived recipe therefore carries the extractor version, and a mismatch on
replay resolves to EXTRACTOR_DRIFT naming the two versions compared, never to TAMPERED.

USER-AGENT POLICY IS PART OF THE ROUTE. The 2026-09-09 sweep measured PMC serving a
reCAPTCHA to browser-like User-Agents and nothing to NO User-Agent; on 2026-09-10 the
challenge covered `/bin/` asset and `/pdf/` paths under every policy. `none` sends no
User-Agent header at all; `identified` sends `pmc_pow_fetch.py`'s honest agent string;
`browser_like` is accepted only so a recipe can say that is what was done.

NO EMAIL ADDRESS OF ANY PERSON GOES TO ANY ENDPOINT. A recipe URL carrying `@` is refused
by the validator and by this tool; there is no code path that accepts a contact parameter.

MINIMUM REPRODUCIBLE INVOCATION
    python3 framework/scripts/reacquire.py status                      # the ratchet
    python3 framework/scripts/reacquire.py backfill --write            # declaredly incomplete
    python3 framework/scripts/reacquire.py replay --pmid 20146584      # replay one manifest
    python3 framework/scripts/reacquire.py replay --absent --limit 20  # the sample measurement
    python3 framework/scripts/reacquire.py selftest
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pmc_pow_fetch  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_DIR = "disease-models/{disease}/research/deepdive_manifests"
RETRIEVAL_MANIFEST = "disease-models/{disease}/research/retrieval_manifest.jsonl"
TIMEOUT = 60
# The receipt-era extractor version, so drift can be named even against a recipe that
# states none. Measured: PMID42397075/PMID42128308 partial locators, PMID38182577.json.
RECEIPT_ERA_PYMUPDF = "1.26.5"

# --- verdicts ---------------------------------------------------------------------------
RECOVERED = "RECOVERED"
EXTRACTOR_DRIFT = "EXTRACTOR_DRIFT"
DIGEST_DIFFERS_SAME_ROUTE = "DIGEST_DIFFERS_SAME_ROUTE"
DIGEST_DIFFERS_SAME_EXTRACTOR = "DIGEST_DIFFERS_SAME_EXTRACTOR"
NO_RECIPE = "NO_RECIPE"
FETCHED_NO_DECLARED_DIGEST = "FETCHED_NO_DECLARED_DIGEST"


def failed(cause: str) -> str:
    return "FAILED_" + cause


UA_IDENTIFIED = pmc_pow_fetch.USER_AGENT
UA_BROWSER_LIKE = "Mozilla/5.0"
UA_POLICIES = ("none", "identified", "browser_like")
# Back-fill recipes may not know which policy was used; replay then uses the one measured
# safe in the sweep and records the policy it actually sent.
UA_UNSTATED_REPLAY_POLICY = "none"

# Tiers the back-fill can show from a note. Free-form strings are accepted in recipes; these
# are the ones this file knows how to derive and how to replay.
TIER_EFETCH = "ncbi_efetch_pmc_xml"
TIER_EPMC_XML = "europepmc_fulltext_xml"
TIER_EPMC_RENDER = "europepmc_pdf_render"
TIER_PMC_POW = "pmc_pow"
TIER_PMC_HTML = "pmc_article_html"
TIER_PMC_BLOB = "pmc_blob_cdn"
TIER_PMC_BIN = "pmc_bin_asset"
TIER_URL_QUOTED = "url_quoted_in_note"
TIER_PUBLISHER_BRONZE = "publisher_bronze_oa"

RECIPE_URL_RE = re.compile(r"^https?://[^\s@]+$")


# --- small helpers ----------------------------------------------------------------------

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d")


def pymupdf_version() -> str | None:
    try:
        import fitz  # noqa: WPS433
    except ImportError:
        return None
    return str(getattr(fitz, "VersionBind", None) or getattr(fitz, "version", ["?"])[0])


def pdftotext_version() -> str | None:
    try:
        out = subprocess.run(["pdftotext", "-v"], capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    m = re.search(r"version\s+([\d.]+)", out.stderr + out.stdout)
    return m.group(1) if m else "unknown"


def host_environment() -> dict[str, Any]:
    return {"python": platform.python_version(), "pymupdf": pymupdf_version(),
            "pdftotext": pdftotext_version()}


def manifest_dir(root: Path, disease: str) -> Path:
    return root / MANIFEST_DIR.format(disease=disease)


def retrieval_manifest_path(root: Path, disease: str) -> Path:
    return root / RETRIEVAL_MANIFEST.format(disease=disease)


def load_manifests(root: Path, disease: str) -> list[dict]:
    out = []
    directory = manifest_dir(root, disease)
    if not directory.is_dir():
        return out
    for path in sorted(directory.glob("PMID*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(data, dict):
            data["_file"] = path.name
            out.append(data)
    return out


def read_ledger(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    lines = []
    with path.open(encoding="utf-8") as fh:
        for raw in fh:
            raw = raw.strip()
            if not raw:
                continue
            try:
                lines.append(json.loads(raw))
            except ValueError:
                continue
    return lines


def append_ledger(path: Path, record: dict) -> None:
    """Append-only, one line, sorted keys, flushed and fsynced — the receipt ledger's habit."""
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, sort_keys=True, ensure_ascii=False)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")
        fh.flush()
        os.fsync(fh.fileno())


# --- recipe resolution ------------------------------------------------------------------

def artifacts_of(manifest: dict) -> list[dict]:
    return [a for a in manifest.get("source_artifacts") or [] if isinstance(a, dict)
            and str(a.get("path", "")).strip()]


def latest_ledger_recipe(ledger: list[dict], pmid: str, path: str) -> dict | None:
    """The most recent back-fill or acquisition line carrying a recipe for this artefact."""
    hit = None
    for line in ledger:
        if str(line.get("pmid")) != str(pmid) or line.get("artifact_path") != path:
            continue
        if line.get("record_kind") in ("backfill_recipe", "acquisition") and line.get("recipe"):
            hit = line
    return hit


def latest_ledger_no_recipe(ledger: list[dict], pmid: str, path: str) -> dict | None:
    hit = None
    for line in ledger:
        if str(line.get("pmid")) != str(pmid) or line.get("artifact_path") != path:
            continue
        if line.get("record_kind") == "backfill_no_recipe":
            hit = line
    return hit


def resolve_recipe(manifest: dict, artifact: dict, ledger: list[dict]) -> tuple[dict | None, str, str | None]:
    """(recipe, source, no_recipe_reason). The manifest wins; the ledger is the back-fill."""
    recipe = artifact.get("acquisition_recipe")
    if isinstance(recipe, dict) and "no_recipe" in recipe:
        return None, "manifest", str(recipe["no_recipe"])
    if isinstance(recipe, dict):
        return recipe, "manifest", None
    line = latest_ledger_recipe(ledger, manifest.get("pmid"), artifact["path"])
    if line:
        return line["recipe"], "retrieval_manifest:%s" % line.get("recorded_at"), None
    line = latest_ledger_no_recipe(ledger, manifest.get("pmid"), artifact["path"])
    if line:
        return None, "retrieval_manifest:%s" % line.get("recorded_at"), line.get("no_recipe_reason")
    return None, "none", None


# --- transport --------------------------------------------------------------------------

def _opener_for(policy: str) -> tuple[urllib.request.OpenerDirector, str]:
    opener = urllib.request.build_opener()
    if policy == "none":
        opener.addheaders = []            # urllib would otherwise send Python-urllib/x.y
    elif policy == "identified":
        opener.addheaders = [("User-Agent", UA_IDENTIFIED)]
    elif policy == "browser_like":
        opener.addheaders = [("User-Agent", UA_BROWSER_LIKE)]
    else:
        raise ValueError("unknown user_agent_policy %r" % policy)
    return opener, policy


def http_get(url: str, policy: str, timeout: int = TIMEOUT) -> dict[str, Any]:
    """One GET. Returns a transport record; never raises on an HTTP status."""
    if not RECIPE_URL_RE.fullmatch(url):
        return {"status": None, "error": "URL_REFUSED", "detail": "not http(s), or carries an address"}
    opener, sent_policy = _opener_for(policy)
    started = time.time()
    try:
        with opener.open(url, timeout=timeout) as response:
            data = response.read()
            headers = {k.lower(): v for k, v in response.headers.items()}
            return {"status": response.status, "bytes": len(data), "data": data,
                    "headers": headers, "final_url": response.geturl(),
                    "user_agent_policy_sent": sent_policy,
                    "seconds": round(time.time() - started, 2)}
    except urllib.error.HTTPError as exc:
        data = exc.read() if hasattr(exc, "read") else b""
        headers = {k.lower(): v for k, v in (exc.headers.items() if exc.headers else [])}
        return {"status": exc.code, "bytes": len(data), "data": data, "headers": headers,
                "final_url": url, "user_agent_policy_sent": sent_policy,
                "seconds": round(time.time() - started, 2)}
    except TimeoutError:
        return {"status": None, "error": "TIMEOUT", "user_agent_policy_sent": sent_policy}
    except (urllib.error.URLError, OSError, ValueError) as exc:
        if "timed out" in str(exc).lower():
            return {"status": None, "error": "TIMEOUT", "user_agent_policy_sent": sent_policy}
        return {"status": None, "error": "NETWORK", "detail": type(exc).__name__,
                "user_agent_policy_sent": sent_policy}


def looks_like_recaptcha(data: bytes) -> bool:
    head = data[:65536].lower()
    return b"recaptcha" in head or b"g-recaptcha" in head


def looks_like_cloudflare(headers: dict[str, str]) -> bool:
    return "cf-ray" in headers or headers.get("server", "").lower().startswith("cloudflare")


def expected_class(path: str, kind: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix == ".pdf":
        return "pdf"
    if suffix in (".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff"):
        return "image"
    if suffix == ".xml":
        return "xml"
    if suffix in (".html", ".htm"):
        return "html"
    if suffix in (".docx", ".pptx", ".xlsx", ".doc", ".ppt", ".xls", ".zip"):
        return "office"
    if kind in ("article_binary", "supplement_binary"):
        return "binary"
    return "text"


def bytes_match_class(data: bytes, klass: str, content_type: str) -> bool:
    if klass == "pdf":
        return data.startswith(b"%PDF")
    if klass == "image":
        return data.startswith((b"\xff\xd8\xff", b"\x89PNG\r\n\x1a\n", b"GII", b"II*\x00", b"MM\x00*"))
    if klass == "xml":
        head = data[:512].lstrip()
        return head.startswith(b"<?xml") or head.startswith(b"<!DOCTYPE") or head.startswith(b"<")
    if klass == "office":
        return data.startswith((b"PK\x03\x04", b"\xd0\xcf\x11\xe0"))
    if klass == "html":
        return b"<html" in data[:4096].lower() or "html" in content_type
    return len(data) > 0


def classify_failure(transport: dict, klass: str) -> str | None:
    """Name the cause, or None when the transport returned something worth hashing."""
    if transport.get("error"):
        return failed(transport["error"])
    status = transport.get("status")
    headers = transport.get("headers") or {}
    data = transport.get("data") or b""
    if status == 403 and looks_like_cloudflare(headers):
        return failed("HTTP_403_CLOUDFLARE")
    if status is not None and status >= 400:
        return failed("HTTP_%d" % status)
    if klass != "html" and looks_like_recaptcha(data) and not bytes_match_class(
            data, klass, headers.get("content-type", "")):
        return failed("RECAPTCHA")
    if not bytes_match_class(data, klass, headers.get("content-type", "")):
        return failed("NOT_THE_ARTEFACT")
    return None


def fetch_by_recipe(recipe: dict, path: str, kind: str) -> tuple[bytes | None, dict[str, Any]]:
    """Replay a fetch recipe. Returns (bytes-or-None, transport record with a `cause` when None)."""
    url = str(recipe.get("resolved_url", "")).strip()
    tier = str(recipe.get("tier", "")).strip()
    policy = str(recipe.get("user_agent_policy", "")).strip() or "unstated"
    if policy not in UA_POLICIES:
        policy = UA_UNSTATED_REPLAY_POLICY
    klass = expected_class(path, kind)
    if not RECIPE_URL_RE.fullmatch(url):
        return None, {"cause": failed("UNSUPPORTED"), "detail": "recipe URL refused", "url": url}
    if tier == TIER_PMC_POW:
        try:
            data, meta = pmc_pow_fetch.fetch(url)
        except urllib.error.HTTPError as exc:
            headers = {k.lower(): v for k, v in (exc.headers.items() if exc.headers else [])}
            cause = failed("HTTP_403_CLOUDFLARE") if exc.code == 403 and looks_like_cloudflare(
                headers) else failed("HTTP_%d" % exc.code)
            return None, {"cause": cause, "status": exc.code, "url": url,
                          "user_agent_policy_sent": "identified"}
        except ValueError as exc:
            # pmc_pow_fetch raises on a page that is neither the binary nor a POW page —
            # since the sweep, that page is a reCAPTCHA. Look, and name it.
            probe = http_get(url, "none")
            data = probe.get("data") or b""
            cause = failed("RECAPTCHA") if looks_like_recaptcha(data) else failed("POW_UNSOLVED")
            return None, {"cause": cause, "status": probe.get("status"), "url": url,
                          "detail": str(exc)[:200], "user_agent_policy_sent": "identified",
                          "bytes": len(data)}
        except (urllib.error.URLError, OSError) as exc:
            return None, {"cause": failed("NETWORK"), "detail": type(exc).__name__, "url": url}
        return data, {"status": meta.get("retry_status") or meta.get("first_status"),
                      "pow_used": meta.get("pow_used"), "url": url, "bytes": len(data),
                      "content_type": meta.get("content_type"),
                      "user_agent_policy_sent": "identified"}
    transport = http_get(url, policy)
    cause = classify_failure(transport, klass)
    record = {k: v for k, v in transport.items() if k != "data"}
    record["url"] = url
    record["content_type"] = (transport.get("headers") or {}).get("content-type")
    record.pop("headers", None)
    if cause:
        record["cause"] = cause
        if looks_like_recaptcha(transport.get("data") or b""):
            record["challenge"] = "recaptcha"
        return None, record
    return transport["data"], record


# --- derivation -------------------------------------------------------------------------

def derive_by_recipe(recipe: dict, source: Path) -> tuple[bytes | None, dict[str, Any]]:
    """Regenerate a derived artefact from its source with the named extractor."""
    extractor = recipe.get("extractor") or {}
    name = str(extractor.get("name", "")).strip().lower()
    call = str(extractor.get("call", "")).strip()
    record: dict[str, Any] = {"extractor": name, "call": call,
                              "version_recipe": str(extractor.get("version", "")).strip() or "unstated"}
    if name in ("pymupdf", "fitz"):
        version = pymupdf_version()
        record["version_host"] = version
        if version is None:
            return None, dict(record, cause=failed("EXTRACTOR_UNAVAILABLE"))
        import fitz
        try:
            doc = fitz.open(str(source))
        except Exception as exc:  # noqa: BLE001 — a verdict, never a traceback
            return None, dict(record, cause=failed("SOURCE_UNREADABLE"), detail=str(exc)[:200])
        if "get_text" in call:
            join = extractor.get("join", "")
            if not isinstance(join, str):
                return None, dict(record, cause=failed("UNSUPPORTED"), detail="join must be a string")
            pages = [page.get_text() for page in doc]
            return join.join(pages).encode("utf-8"), record
        m = re.search(r"get_pixmap\(dpi=(\d+)\)", call)
        if m and isinstance(recipe.get("page"), int):
            pix = doc[recipe["page"] - 1].get_pixmap(dpi=int(m.group(1)))
            return pix.tobytes("png"), record
        if "extract_image" in call and isinstance(recipe.get("xref"), int):
            info = doc.extract_image(recipe["xref"])
            return info["image"], dict(record, ext=info.get("ext"))
        return None, dict(record, cause=failed("UNSUPPORTED"), detail="call not replayable: %s" % call)
    if name == "pdftotext":
        version = pdftotext_version()
        record["version_host"] = version
        if version is None:
            return None, dict(record, cause=failed("EXTRACTOR_UNAVAILABLE"))
        args = extractor.get("args") or []
        if not isinstance(args, list) or not all(isinstance(a, str) for a in args):
            return None, dict(record, cause=failed("UNSUPPORTED"), detail="args must be strings")
        try:
            out = subprocess.run(["pdftotext", *args, str(source), "-"], capture_output=True,
                                 timeout=120)
        except (OSError, subprocess.SubprocessError) as exc:
            return None, dict(record, cause=failed("EXTRACTOR_UNAVAILABLE"), detail=str(exc)[:200])
        if out.returncode != 0:
            return None, dict(record, cause=failed("EXTRACTOR_ERROR"), detail=out.stderr[:200].decode(errors="replace"))
        return out.stdout, record
    return None, dict(record, cause=failed("UNSUPPORTED"), detail="unknown extractor %r" % name)


# --- the replay of one artefact ---------------------------------------------------------

def replay_artifact(root: Path, manifest: dict, artifact: dict, ledger: list[dict], *,
                    offline: bool = False, write: bool = True,
                    recovered_this_run: dict[str, Path] | None = None) -> dict[str, Any]:
    """Replay one declared artefact. Returns the verdict record — what it did, what came back."""
    path = str(artifact["path"]).strip()
    kind = str(artifact.get("kind", "")).strip()
    declared = str(artifact.get("sha256", "")).strip() or None
    local = root / path
    recipe, source, no_reason = resolve_recipe(manifest, artifact, ledger)
    record: dict[str, Any] = {
        "record_kind": "replay", "recorded_at": now_iso(), "pmid": str(manifest.get("pmid")),
        "artifact_path": path, "kind": kind, "declared_sha256": declared,
        "recipe_source": source, "present_before": local.is_file(),
        "host_environment": host_environment(),
    }
    if recipe is None:
        record.update(verdict=NO_RECIPE, no_recipe_reason=no_reason)
        return record
    record["recipe"] = recipe
    if recipe.get("derived") is True:
        src_rel = str(recipe.get("derived_from", "")).strip()
        src = (recovered_this_run or {}).get(src_rel) or (root / src_rel)
        if not src.is_file():
            record.update(verdict=failed("SOURCE_ABSENT"), source=src_rel)
            return record
        src_declared = next((str(a.get("sha256", "")) for a in artifacts_of(manifest)
                             if str(a.get("path")) == src_rel), None)
        actual_src = sha256_file(src)
        if src_declared and actual_src != src_declared:
            record.update(verdict=failed("SOURCE_DIGEST_MISMATCH"), source=src_rel,
                          source_declared_sha256=src_declared, source_observed_sha256=actual_src)
            return record
        data, detail = derive_by_recipe(recipe, src)
        record["derivation"] = detail
        if data is None:
            record["verdict"] = detail.get("cause", failed("UNSUPPORTED"))
            return record
        observed = sha256_bytes(data)
        record.update(observed_sha256=observed, observed_bytes=len(data))
        if declared is None:
            record["verdict"] = FETCHED_NO_DECLARED_DIGEST
        elif observed == declared:
            record["verdict"] = RECOVERED
        else:
            v_recipe = detail.get("version_recipe") or "unstated"
            v_host = detail.get("version_host")
            if v_recipe != v_host:
                record["verdict"] = EXTRACTOR_DRIFT
                record["drift"] = {"extractor": detail.get("extractor"),
                                   "version_recipe": v_recipe, "version_host": v_host,
                                   "receipt_era_pymupdf": RECEIPT_ERA_PYMUPDF}
            else:
                record["verdict"] = DIGEST_DIFFERS_SAME_EXTRACTOR
        _maybe_write(root, path, data, declared, record, write, recovered_this_run)
        return record
    if offline:
        record["verdict"] = failed("OFFLINE")
        return record
    data, transport = fetch_by_recipe(recipe, path, kind)
    record["transport"] = transport
    if data is None:
        record["verdict"] = transport.get("cause", failed("UNSUPPORTED"))
        return record
    observed = sha256_bytes(data)
    record.update(observed_sha256=observed, observed_bytes=len(data))
    if declared is None:
        record["verdict"] = FETCHED_NO_DECLARED_DIGEST
    elif observed == declared:
        record["verdict"] = RECOVERED
    else:
        record["verdict"] = DIGEST_DIFFERS_SAME_ROUTE
        record["finding"] = ("the same route returned different bytes: a finding about the "
                             "publisher or the deposit, not TAMPERED by default — compare "
                             "declared and observed sizes and read both before deciding")
    _maybe_write(root, path, data, declared, record, write, recovered_this_run)
    return record


def _maybe_write(root: Path, path: str, data: bytes, declared: str | None, record: dict,
                 write: bool, recovered_this_run: dict[str, Path] | None) -> None:
    """Write RECOVERED bytes to their declared path; never overwrite a file with other bytes."""
    if not write or record.get("verdict") != RECOVERED:
        return
    local = root / path
    if local.is_file():
        if sha256_file(local) == declared:
            record["written"] = "already_present"
            return
        record["written"] = "refused: a file with a different digest already sits at the path"
        return
    local.parent.mkdir(parents=True, exist_ok=True)
    local.write_bytes(data)
    record["written"] = "written"
    if recovered_this_run is not None:
        recovered_this_run[path] = local


# --- back-fill ---------------------------------------------------------------------------

PMCID_RE = re.compile(r"\bPMC(\d{5,9})\b")
URL_RE = re.compile(r"https?://[^\s'\")\]>]+")
CDN_RE = re.compile(r"\bcdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^\s'\")\]>]+")


def _note_blob(artifact: dict, manifest: dict) -> str:
    parts = [str(artifact.get(k, "")) for k in ("note", "route", "extraction", "surface_note")]
    return " ".join(parts)


def infer_recipe(manifest: dict, artifact: dict, acquired_on: str = "2026-09-09") -> tuple[dict | None, str, str]:
    """(recipe | None, reason_class, evidence) — a recipe ONLY where the note shows the route.

    `evidence` is the quoted span of the note the recipe rests on, so every back-fill line
    is auditable against the manifest it came from.
    """
    path = str(artifact["path"])
    kind = str(artifact.get("kind", ""))
    blob = _note_blob(artifact, manifest)
    suffix = Path(path).suffix.lower()
    declared_paths = {str(a.get("path")) for a in artifacts_of(manifest)}
    manifest_pmcid = PMCID_RE.search(str(manifest.get("pmcid") or ""))
    note_pmcid = PMCID_RE.search(blob)
    pmcid = (note_pmcid or manifest_pmcid)
    pmc_num = pmcid.group(1) if pmcid else None
    date_m = re.search(r"\b(20\d\d-\d\d-\d\d)\b", blob)
    when = date_m.group(1) if date_m else acquired_on

    def fetch(tier, url, policy="none", confidence="url_quoted", evidence=""):
        return ({"resolved_url": url, "http_method": "GET", "tier": tier,
                 "user_agent_policy": policy, "acquired_on": when, "derived": False,
                 "recipe_confidence": confidence, "evidence": evidence[:300]},
                "route_shown", evidence[:300])

    # 1. a quoted CDN blob route (figures; `route` field)
    cdn = CDN_RE.search(blob)
    if cdn:
        return fetch(TIER_PMC_BLOB, "https://" + cdn.group(0), "unstated", "url_quoted", cdn.group(0))
    # 2. a quoted URL anywhere in the note
    url = URL_RE.search(blob)
    if url and "@" not in url.group(0):
        u = url.group(0).rstrip(".,;")
        tier = TIER_PMC_HTML if "pmc.ncbi.nlm.nih.gov/articles/" in u and suffix in (".html", ".htm") else TIER_URL_QUOTED
        return fetch(tier, u, "unstated", "url_quoted", u)
    # 3. efetch db=pmc with a PMCID, for an XML text surface
    if re.search(r"efetch", blob, re.I) and re.search(r"db\s*=\s*pmc", blob, re.I) and pmc_num \
            and suffix == ".xml":
        ev = re.search(r"[^.]*efetch[^.]*\.", blob)
        return fetch(TIER_EFETCH,
                     "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=%s" % pmc_num,
                     "none", "route_named_url_form_determined", ev.group(0) if ev else blob[:200])
    # 4. Europe PMC fullTextXML for PMCxxx (success phrasing), XML surface
    m = re.search(r"Europe PMC(?: REST)? fullTextXML for (PMC\d+)[^.]*", blob)
    if m and suffix == ".xml" and "404" not in m.group(0):
        num = m.group(1)[3:]
        return fetch(TIER_EPMC_XML,
                     "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC%s/fullTextXML" % num,
                     "unstated", "route_named_url_form_determined", m.group(0))
    # 5. Europe PMC pdf=render with a PMCID, PDF surface
    if re.search(r"pdf=render", blob) and suffix == ".pdf" and pmc_num:
        ev = re.search(r"[^.]*pdf=render[^.]*\.", blob)
        return fetch(TIER_EPMC_RENDER, "https://europepmc.org/articles/PMC%s?pdf=render" % pmc_num,
                     "unstated", "route_named_url_form_determined", ev.group(0) if ev else blob[:200])
    # 6. pmc_pow_fetch.py from PMC: route shown, URL form inferred
    if "pmc_pow_fetch" in blob and pmc_num and suffix == ".pdf" and "supplement" not in path.lower() \
            and not re.search(r"supplement|SI Appendix|Supplementary", blob[:200], re.I):
        ev = re.search(r"[^.]*pmc_pow_fetch[^.]*\.", blob)
        return fetch(TIER_PMC_POW, "https://pmc.ncbi.nlm.nih.gov/articles/PMC%s/pdf/" % pmc_num,
                     "identified", "route_named_url_form_inferred", ev.group(0) if ev else blob[:200])
    if "pmc_pow_fetch" in blob:
        return None, "pow_route_named_url_not_recorded", blob[:200]
    # 7. derived text with a stated call AND join
    if kind in ("article_text", "supplement_text") and suffix == ".txt":
        sources = [p for p in declared_paths if p.lower().endswith(".pdf")]
        stem_src = [p for p in sources if Path(p).stem.split("_fitz")[0] in Path(path).stem]
        src = stem_src[0] if stem_src else (sources[0] if len(sources) == 1 else None)
        m_ver = re.search(r"PyMuPDF\s+([\d.]+)", blob)
        if "pdftotext" in blob and src:
            args = re.findall(r"(-[a-zA-Z]+)", blob.split("pdftotext", 1)[1][:60])
            return ({"derived": True, "derived_from": src, "acquired_on": when,
                     "extractor": {"name": "pdftotext", "version": "unstated", "args": args,
                                   "call": "pdftotext %s <pdf> -" % " ".join(args)},
                     "recipe_confidence": "call_stated", "evidence": blob[:300]},
                    "route_shown", blob[:300])
        if "get_text" in blob and src:
            join = None
            if re.search(r"''\.join|no separator", blob):
                join = ""
            elif re.search(r"'\\n'\.join|newline-joined", blob):
                join = "\n"
            if join is None:
                return None, "derived_join_unstated", blob[:200]
            return ({"derived": True, "derived_from": src, "acquired_on": when,
                     "extractor": {"name": "PyMuPDF", "version": m_ver.group(1) if m_ver else "unstated",
                                   "call": "page.get_text() default mode", "join": join},
                     "recipe_confidence": "call_and_join_stated", "evidence": blob[:300]},
                    "route_shown", blob[:300])
        if src:
            return None, "derived_extractor_unstated", blob[:200]
        return None, "derived_source_undeclared", blob[:200]
    if kind == "figure":
        if re.search(r"rendered|get_pixmap|dpi", blob, re.I):
            return None, "figure_render_parameters_not_on_the_entry", blob[:200]
        if pmc_num:
            return None, "figure_pmcid_only_asset_url_unrecorded", blob[:200]
        return None, "figure_note_names_no_route", blob[:200]
    if pmc_num:
        return None, "pmcid_only_route_unstated", blob[:200]
    if not blob.strip():
        return None, "no_note", ""
    return None, "note_names_no_route", blob[:200]


# --- commands ---------------------------------------------------------------------------

def _actor(args) -> str:
    return args.actor or os.environ.get("ACTOR_ID") or "unknown"


def cmd_status(args) -> int:
    root = Path(args.workspace).resolve()
    manifests = load_manifests(root, args.disease)
    ledger = read_ledger(retrieval_manifest_path(root, args.disease))
    total = in_manifest = via_backfill = stated_none = none = present = 0
    for manifest in manifests:
        for artifact in artifacts_of(manifest):
            total += 1
            if (root / artifact["path"]).is_file():
                present += 1
            recipe, source, reason = resolve_recipe(manifest, artifact, ledger)
            if recipe is not None and source == "manifest":
                in_manifest += 1
            elif recipe is not None:
                via_backfill += 1
            elif reason:
                stated_none += 1
            else:
                none += 1
    replays = [l for l in ledger if l.get("record_kind") == "replay"]
    verdicts: dict[str, int] = {}
    for line in replays:
        verdicts[line.get("verdict", "?")] = verdicts.get(line.get("verdict", "?"), 0) + 1
    print("=== ACQUISITION RECIPES — the ratchet ===")
    print("manifests                         : %d" % len(manifests))
    print("declared artefacts                : %d  (%d present on this host)" % (total, present))
    print("recipe in the manifest            : %d" % in_manifest)
    print("recipe via back-fill (ledger)     : %d" % via_backfill)
    print("NO_RECIPE, reason stated          : %d" % stated_none)
    print("no recipe, nothing stated         : %d" % none)
    print("replayable                        : %d / %d" % (in_manifest + via_backfill, total))
    print("retrieval manifest                : %s (%d line(s))"
          % (retrieval_manifest_path(root, args.disease).relative_to(root), len(ledger)))
    if replays:
        print("replay verdicts recorded          : " + ", ".join(
            "%s=%d" % (k, v) for k, v in sorted(verdicts.items())))
    return 0


def cmd_backfill(args) -> int:
    root = Path(args.workspace).resolve()
    manifests = load_manifests(root, args.disease)
    ledger_path = retrieval_manifest_path(root, args.disease)
    ledger = read_ledger(ledger_path)
    counts: dict[str, int] = {}
    written = skipped = 0
    for manifest in manifests:
        for artifact in artifacts_of(manifest):
            recipe_here, source, _ = resolve_recipe(manifest, artifact, ledger)
            if source != "none":
                skipped += 1        # already has a recipe or a stated reason
                continue
            recipe, reason, evidence = infer_recipe(manifest, artifact)
            counts[reason] = counts.get(reason, 0) + 1
            record = {"record_kind": "backfill_recipe" if recipe else "backfill_no_recipe",
                      "recorded_at": now_iso(), "actor": _actor(args), "task": args.task,
                      "pmid": str(manifest.get("pmid")), "artifact_path": artifact["path"],
                      "kind": artifact.get("kind"), "declared_sha256": artifact.get("sha256"),
                      "recipe": recipe, "no_recipe_reason": None if recipe else reason,
                      "evidence": evidence,
                      "basis": "%s source_artifacts note/route/extraction" % manifest["_file"]}
            if args.write:
                append_ledger(ledger_path, record)
                written += 1
            elif args.verbose:
                print(json.dumps(record, sort_keys=True)[:300])
    shown = sum(v for k, v in counts.items() if k == "route_shown")
    total = sum(counts.values())
    print("=== BACK-FILL — declaredly incomplete ===")
    print("artefacts considered              : %d  (%d already covered, skipped)" % (total, skipped))
    print("recipe written (route shown)      : %d / %d  (%.1f%%)"
          % (shown, total, 100.0 * shown / total if total else 0.0))
    print("NO_RECIPE by reason class:")
    for reason, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        if reason != "route_shown":
            print("    %-46s %d" % (reason, n))
    print("lines %s: %d -> %s" % ("appended" if args.write else "that would be appended",
                                 written if args.write else total, ledger_path.relative_to(root)))
    print("A route the note does not show is not invented; it is a NO_RECIPE with its reason.")
    return 0


def _targets(root: Path, manifests: list[dict], ledger: list[dict], args) -> list[tuple[dict, dict]]:
    targets = []
    for manifest in manifests:
        if args.pmid and str(manifest.get("pmid")) not in args.pmid:
            continue
        for artifact in artifacts_of(manifest):
            if args.path and artifact["path"] not in args.path:
                continue
            if args.absent and (root / artifact["path"]).is_file():
                continue
            if args.with_recipe:
                recipe, _s, _r = resolve_recipe(manifest, artifact, ledger)
                if recipe is None:
                    continue
            targets.append((manifest, artifact))
    return targets


def cmd_replay(args) -> int:
    root = Path(args.workspace).resolve()
    manifests = load_manifests(root, args.disease)
    ledger_path = retrieval_manifest_path(root, args.disease)
    ledger = read_ledger(ledger_path)
    targets = _targets(root, manifests, ledger, args)
    # Extra ledger-only targets: artefacts recorded in the retrieval manifest for a PMID that
    # has no deep-dive manifest (the 33914858 case) or that a manifest does not declare.
    known = {(str(m.get("pmid")), a["path"]) for m, a in targets}
    if args.ledger_only:
        for line in ledger:
            if line.get("record_kind") == "backfill_recipe" and line.get("recipe") and \
                    (str(line.get("pmid")), line.get("artifact_path")) not in known and \
                    (not args.pmid or str(line.get("pmid")) in args.pmid):
                pseudo = {"pmid": line.get("pmid"), "source_artifacts": [
                    {"path": line["artifact_path"], "kind": line.get("kind") or "article_binary",
                     "sha256": line.get("declared_sha256") or ""}], "_file": "retrieval_manifest"}
                targets.append((pseudo, pseudo["source_artifacts"][0]))
                known.add((str(line.get("pmid")), line["artifact_path"]))
    if args.limit:
        targets = targets[: args.limit]
    recovered_this_run: dict[str, Path] = {}
    verdicts: dict[str, int] = {}
    for manifest, artifact in targets:
        record = replay_artifact(root, manifest, artifact, ledger, offline=args.offline,
                                 write=not args.no_write, recovered_this_run=recovered_this_run)
        record["actor"] = _actor(args)
        record["task"] = args.task
        verdicts[record["verdict"]] = verdicts.get(record["verdict"], 0) + 1
        line = "%-30s PMID %-9s %s" % (record["verdict"], record["pmid"], record["artifact_path"])
        extra = record.get("transport") or record.get("derivation") or {}
        if record["verdict"].startswith("FAILED_") and extra:
            line += "  [status=%s%s]" % (extra.get("status"),
                                        ", " + extra["detail"][:60] if extra.get("detail") else "")
        if record["verdict"] == EXTRACTOR_DRIFT:
            line += "  [%s %s -> %s]" % (record["drift"]["extractor"],
                                         record["drift"]["version_recipe"], record["drift"]["version_host"])
        if record["verdict"] == NO_RECIPE and record.get("no_recipe_reason"):
            line += "  [%s]" % record["no_recipe_reason"][:60]
        print(line)
        if not args.no_record:
            append_ledger(ledger_path, record)
        if args.sleep and not record["verdict"] == NO_RECIPE:
            time.sleep(args.sleep)
    total = sum(verdicts.values())
    print("")
    print("=== REPLAY — %d artefact(s) on this host, %s ===" % (total, today()))
    for verdict, n in sorted(verdicts.items(), key=lambda kv: (-kv[1], kv[0])):
        print("  %-32s %d" % (verdict, n))
    grouped = {"RECOVERED": verdicts.get(RECOVERED, 0),
               "FAILED": sum(v for k, v in verdicts.items() if k.startswith("FAILED_")),
               "NO_RECIPE": verdicts.get(NO_RECIPE, 0),
               "DRIFT_OR_DIFFERS": sum(v for k, v in verdicts.items() if k in (
                   EXTRACTOR_DRIFT, DIGEST_DIFFERS_SAME_ROUTE, DIGEST_DIFFERS_SAME_EXTRACTOR))}
    print("RECOVERED / FAILED / NO_RECIPE / DRIFT_OR_DIFFERS = %d / %d / %d / %d" % (
        grouped["RECOVERED"], grouped["FAILED"], grouped["NO_RECIPE"], grouped["DRIFT_OR_DIFFERS"]))
    print("A digest mismatch on a binary fetched by the same route is a finding about the "
          "publisher, not TAMPERED; a mismatch under a different extractor is EXTRACTOR_DRIFT.")
    return 0


def cmd_record(args) -> int:
    """Append one acquisition line from a JSON file — for `find-fulltext` and the readers."""
    root = Path(args.workspace).resolve()
    payload = json.loads(Path(args.json).read_text(encoding="utf-8"))
    for key in ("pmid", "artifact_path", "recipe"):
        if key not in payload:
            sys.stderr.write("record: payload lacks %r\n" % key)
            return 2
    url = str((payload.get("recipe") or {}).get("resolved_url", ""))
    if url and not RECIPE_URL_RE.fullmatch(url):
        sys.stderr.write("record: recipe URL refused (not http(s), or carries an address)\n")
        return 2
    record = dict(payload, record_kind="acquisition", recorded_at=now_iso(),
                  actor=_actor(args), task=args.task)
    append_ledger(retrieval_manifest_path(root, args.disease), record)
    print("appended acquisition for PMID %s %s" % (payload["pmid"], payload["artifact_path"]))
    return 0


def cmd_selftest(args) -> int:
    """Calls the entry points on real corpus artefacts, offline, and says what it skipped."""
    root = Path(args.workspace).resolve()
    failures = []
    manifests = load_manifests(root, args.disease)
    if not manifests:
        failures.append("no manifests under %s" % manifest_dir(root, args.disease))
    ledger = read_ledger(retrieval_manifest_path(root, args.disease))
    # 1. status on the real corpus, through main()
    rc = main(["--workspace", str(root), "--disease", args.disease, "status"])
    if rc != 0:
        failures.append("status exited %d" % rc)
    # 2. a derived replay on a real present source, if any; declared skip otherwise
    replayed = False
    for manifest in manifests:
        for artifact in artifacts_of(manifest):
            recipe, _s, _r = resolve_recipe(manifest, artifact, ledger)
            if recipe and recipe.get("derived") and (root / str(recipe.get("derived_from", ""))).is_file():
                record = replay_artifact(root, manifest, artifact, ledger, offline=True, write=False)
                print("selftest replayed derived %s -> %s" % (artifact["path"], record["verdict"]))
                if record["verdict"] not in (RECOVERED, EXTRACTOR_DRIFT, DIGEST_DIFFERS_SAME_EXTRACTOR) \
                        and not record["verdict"].startswith("FAILED_"):
                    failures.append("unexpected verdict %s" % record["verdict"])
                replayed = True
                break
        if replayed:
            break
    if not replayed:
        print("selftest: SKIPPED derived replay — no derived recipe with its source present on this host")
    # 3. a fetch recipe replays OFFLINE to FAILED_OFFLINE, never to RECOVERED
    for manifest in manifests:
        for artifact in artifacts_of(manifest):
            recipe, _s, _r = resolve_recipe(manifest, artifact, ledger)
            if recipe and not recipe.get("derived"):
                record = replay_artifact(root, manifest, artifact, ledger, offline=True, write=False)
                if record["verdict"] != failed("OFFLINE"):
                    failures.append("offline fetch replay gave %s" % record["verdict"])
                else:
                    print("selftest: offline fetch replay of %s -> %s" % (artifact["path"], record["verdict"]))
                replayed = True
                break
        else:
            continue
        break
    # 4. NO_RECIPE is a verdict, not an exception
    probe = replay_artifact(root, {"pmid": "0", "source_artifacts": []},
                            {"path": "files/none.pdf", "kind": "article_binary", "sha256": "0" * 64},
                            [], offline=True, write=False)
    if probe["verdict"] != NO_RECIPE:
        failures.append("an artefact with no recipe did not yield NO_RECIPE")
    print("")
    if failures:
        print("SELFTEST: FAIL")
        for f in failures:
            print("  - %s" % f)
        return 1
    print("SELFTEST: PASS")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--workspace", default=str(REPO_ROOT))
    p.add_argument("--disease", default="wwox")
    p.add_argument("--actor", default=None, help="ACTOR_ID recorded on every line (or $ACTOR_ID)")
    p.add_argument("--task", default=None, help="TASK_ID recorded on every line")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="the ratchet: recipes in manifests, via back-fill, NO_RECIPE")
    b = sub.add_parser("backfill", help="write recipes where a note shows the route; NO_RECIPE elsewhere")
    b.add_argument("--write", action="store_true", help="append to the retrieval manifest")
    b.add_argument("--verbose", action="store_true")
    r = sub.add_parser("replay", help="replay recipes and diff the digest")
    r.add_argument("--pmid", action="append")
    r.add_argument("--path", action="append", help="repository-relative artefact path")
    r.add_argument("--absent", action="store_true", help="only artefacts absent on this host")
    r.add_argument("--with-recipe", action="store_true", help="skip artefacts that have no recipe")
    r.add_argument("--ledger-only", action="store_true",
                   help="also replay back-filled recipes for artefacts no manifest declares")
    r.add_argument("--limit", type=int, default=0)
    r.add_argument("--sleep", type=float, default=0.0)
    r.add_argument("--offline", action="store_true")
    r.add_argument("--no-write", action="store_true", help="do not write RECOVERED bytes to files/")
    r.add_argument("--no-record", action="store_true", help="do not append to the retrieval manifest")
    c = sub.add_parser("record", help="append one acquisition line from a JSON payload")
    c.add_argument("--json", required=True)
    sub.add_parser("selftest", help="call the entry points on real corpus artefacts, offline")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return {"status": cmd_status, "backfill": cmd_backfill, "replay": cmd_replay,
            "record": cmd_record, "selftest": cmd_selftest}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
