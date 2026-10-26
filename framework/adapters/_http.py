"""One small door to HTTP for the repurposing adapters: standard library, no key, no retry
policy to configure. Not an adapter (the leading underscore keeps it out of discovery).

`get_json(url, params=None, body=None, timeout=20)` returns `(http_status, parsed_json_or_text)`
and never raises on an HTTP error: a 404 is an answer (NO_MATCH on most services), a 5xx is a
QUERY_ERROR, and the adapter decides which. A transport failure (DNS, timeout) returns
`(0, "<exception text>")` so the adapter can report it as QUERY_ERROR with the text kept.
"""
from __future__ import annotations

import json
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
