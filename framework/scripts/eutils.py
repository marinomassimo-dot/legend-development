"""One polite door to NCBI E-utilities for every LEGEND tool: a cross-process throttle, back-off
on 429/5xx, and a short-lived response cache. A library, not a command.

WHY. In the metabolic batch of 2026-10-19 four Scientists queried PubMed in parallel from one
host. NCBI's limit (3 requests/s without an API key, 10 with one) is per client, not per
process, so each tool's private `sleep` did not add up: HTTP 429s, and identity checks that
failed only when run in parallel ("sequential with a one-second pause is clean",
capability_scout_log 2026-10-20). N8 of PLAN-HARNESS-FROM-METABOLIC-BATCH-20261020.

HOW.
* Throttle: one lock file per user, shared by every process, worktree and clone on the host
  (`~/.cache/legend/eutils/`, or `$LEGEND_EUTILS_DIR`). Under an exclusive lock a request
  waits until the previous one is `interval` old, stamps the time, releases, then fetches.
* Back-off: 429 honours `Retry-After`; 429/5xx/network errors retry with exponential back-off
  and jitter; any other HTTP error is returned to the caller at once (it will not improve).
* Cache: a 200 response is kept for `LEGEND_EUTILS_CACHE_TTL` seconds (default one day; 0
  disables). Two Scientists asking for the same PMID's summary cost NCBI one request.
  The cache is a convenience for identity look-ups, never evidence: a receipt names the
  artefact it read, not this cache.
* User-Agent: empty by default — the measured policy that PMC and E-utilities serve cleanly.

    import eutils
    body = eutils.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?...")
    code, body = eutils.fetch(url)          # never raises on HTTP errors; code 0 = no answer
"""
from __future__ import annotations

import fcntl
import hashlib
import os
import random
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable

HOST = "eutils.ncbi.nlm.nih.gov"
RETRY_CEILING_SECONDS = 30.0


def state_dir() -> Path:
    base = os.environ.get("LEGEND_EUTILS_DIR")
    if base:
        return Path(base)
    cache = os.environ.get("XDG_CACHE_HOME") or str(Path.home() / ".cache")
    return Path(cache) / "legend" / "eutils"


def interval() -> float:
    return 0.12 if os.environ.get("NCBI_API_KEY") else 0.4


def ttl() -> float:
    try:
        return float(os.environ.get("LEGEND_EUTILS_CACHE_TTL", "86400"))
    except ValueError:
        return 86400.0


def wait_turn(directory: Path | None = None, gap: float | None = None) -> float:
    """Block until this process may send the next request; return the seconds waited."""
    directory = directory or state_dir()
    directory.mkdir(parents=True, exist_ok=True)
    gap = interval() if gap is None else gap
    with open(directory / "throttle.lock", "a+") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            handle.seek(0)
            try:
                last = float(handle.read().strip() or 0)
            except ValueError:
                last = 0.0
            waited = max(0.0, last + gap - time.time())
            if waited:
                time.sleep(waited)
            handle.seek(0)
            handle.truncate()
            handle.write(f"{time.time():.6f}")
            handle.flush()
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    return waited


def _cache_path(url: str) -> Path:
    return state_dir() / "cache" / hashlib.sha256(url.encode("utf-8")).hexdigest()


def _urlopen(url: str, timeout: float, user_agent: str) -> tuple[int, bytes, dict]:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read(), dict(response.headers)
    except urllib.error.HTTPError as error:
        return error.code, error.read() or b"", dict(error.headers or {})


def fetch(url: str, *, timeout: float = 40, retries: int = 5, user_agent: str = "",
          opener: Callable[[str, float, str], tuple[int, bytes, dict]] | None = None,
          use_cache: bool = True) -> tuple[int, bytes]:
    """(HTTP status, body). Status 0 means no answer after every retry. Never raises on HTTP."""
    opener = opener or _urlopen
    cache = _cache_path(url) if use_cache and ttl() > 0 else None
    if cache is not None and cache.is_file() and time.time() - cache.stat().st_mtime < ttl():
        return 200, cache.read_bytes()
    code, body = 0, b""
    for attempt in range(retries):
        wait_turn()
        try:
            code, body, headers = opener(url, timeout, user_agent)
        except OSError:
            code, body, headers = 0, b"", {}
        if code == 200:
            if cache is not None and body:
                cache.parent.mkdir(parents=True, exist_ok=True)
                temporary = cache.with_suffix(f".{os.getpid()}.tmp")
                temporary.write_bytes(body)
                os.replace(temporary, cache)
            return code, body
        if code and code != 429 and not 500 <= code < 600:
            return code, body
        delay = min(2 ** attempt, RETRY_CEILING_SECONDS)
        if code == 429:
            try:
                delay = max(delay, float(headers.get("Retry-After", 0)))
            except (TypeError, ValueError):
                pass
        if attempt + 1 < retries:
            time.sleep(delay + random.uniform(0, 0.5))
    return code, body


def get(url: str, **kwargs) -> bytes:
    """The body of a 200 answer, or RuntimeError naming the last status."""
    code, body = fetch(url, **kwargs)
    if code != 200:
        raise RuntimeError(f"E-utilities returned HTTP {code or 'no answer'} for {url}")
    return body
