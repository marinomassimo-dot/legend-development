"""One small door to HTTP for the repurposing adapters: standard library, no key, no retry
policy to configure. Not an adapter (the leading underscore keeps it out of discovery).

`get_json(url, params=None, body=None, timeout=20)` returns `(http_status, parsed_json_or_text)`
and never raises on an HTTP error: a 404 is an answer (NO_MATCH on most services), a 5xx is a
QUERY_ERROR, and the adapter decides which. A transport failure (DNS, timeout) returns
`(0, "<exception text>")` so the adapter can report it as QUERY_ERROR with the text kept.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

USER_AGENT = "LEGEND-repurposing-adapter/1 (research; no key; contact via repository)"


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get_json(url: str, params: dict | None = None, body: dict | None = None,
             timeout: float = 20.0) -> tuple[int, object]:
    if params:
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    data = None
    headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = response.status
            text = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        status = exc.code
        text = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:  # ValueError covers http.client.InvalidURL
        return 0, f"{type(exc).__name__}: {exc}"
    try:
        return status, json.loads(text) if text.strip() else {}
    except ValueError:
        return status, text


def make_fetch(cache_dir: str | None = None, retries: int = 2, pause: float = 6.0, get=None, sleep=time.sleep):
    """A `fetch` for the adapters with a bounded retry and an optional response cache; the adapters take it through `query(request, fetch=...)`.

    * Retry: a transport failure (status 0) or an HTTP 5xx is tried again at most `retries` times (`pause` seconds apart); a 4xx is an answer and is not
      retried. Every failed attempt is appended to `fetch.failures` ({url, http, attempt, text}); nothing is retried silently and nothing loops.
    * Cache (only when `cache_dir` is given, an explicit path; nothing is written otherwise): only a successful (HTTP 200) response is stored, one JSON file
      per request keyed by SHA-256 of the full URL, body and parameters, with its own `retrieved_at`. An error, a 404 or an empty 'no result' answer for a
      query that failed is never stored, so a cache hit can never turn an error into 'no result'. The key does not contain the database release: use one
      directory per release, or delete it, to refresh. Rerunning a query after a failure fetches only the requests (pages, batches) that are not yet cached.
    * `fetch.stats` counts cache hits, network requests, failed attempts and requests that ended in an error."""
    inner = get or get_json
    stats = {"cache_hits": 0, "network_requests": 0, "failed_attempts": 0, "requests_ended_in_error": 0}
    failures: list = []

    def key(url, params, body):
        return hashlib.sha256(json.dumps([url, params, body], sort_keys=True, default=str).encode("utf-8")).hexdigest()

    def fetch(url, params=None, body=None, timeout=20.0):
        path = os.path.join(cache_dir, key(url, params, body) + ".json") if cache_dir else None
        if path and os.path.isfile(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    stored = json.load(fh)
                if stored.get("http") == 200 and stored.get("url") == url:
                    stats["cache_hits"] += 1
                    return 200, stored["payload"]
            except (OSError, ValueError):
                pass  # a damaged cache file is a miss, never an answer
        status, payload = 0, ""
        for attempt in range(retries + 1):
            stats["network_requests"] += 1
            status, payload = inner(url, params, body, timeout)
            if status == 200 or (status and status < 500):
                break
            stats["failed_attempts"] += 1
            failures.append({"url": url, "http": status, "attempt": attempt + 1, "text": str(payload)[:120]})
            if attempt < retries:
                sleep(pause)
        else:
            stats["requests_ended_in_error"] += 1
        if status == 200 and path and isinstance(payload, (dict, list)):
            os.makedirs(cache_dir, exist_ok=True)
            tmp = path + ".part"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump({"url": url, "http": 200, "retrieved_at": now_utc(), "payload": payload}, fh)
            os.replace(tmp, path)
        return status, payload

    fetch.stats, fetch.failures = stats, failures
    return fetch
