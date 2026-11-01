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
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

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


# --- Keeping a fetched document: original local, extract public -------------------------
#
# A third-party README, release body or tool source is fetched to be READ, not republished.
# Two IT15 incidents came from saving such bodies verbatim inside a tracked package: contributor
# e-mail addresses reached the release gate, and README copies whose relative links pointed at
# files the copy did not contain broke the link test. The rule is the one the corpus already
# follows: the ORIGINAL stays byte-identical in the local ignored corpus (`files/<package>/`)
# with its SHA-256, origin and revision; the repository gets an extract that is safe to publish.

EMAIL_REPLACEMENT = "[address withheld]"
_EMAIL = re.compile(r"(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9_%+-])")
_MD_LINK = re.compile(r"(?<!!)(\[[^\]]*\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")


def keep_original(corpus_dir, name: str, data: bytes, origin: str, revision: str) -> dict:
    """Write `data` unchanged under `corpus_dir/name` and return its manifest record.

    Never silently alters an original: if `name` exists with different bytes it raises. The
    record (`sha256`, `bytes`, `origin`, `revision`) is what the tracked package keeps, as a
    digest line, in place of the third-party bytes.
    """
    path = Path(corpus_dir) / name
    if path.exists() and path.read_bytes() != data:
        raise FileExistsError(f"{path} exists with different bytes; keep the old original and name the new one")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(data)
    return {"name": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
            "origin": origin, "revision": revision}


def public_extract(text: str, origin_url: str) -> str:
    """The publishable form of a fetched Markdown text.

    E-mail addresses are withheld (personal data in third-party text). Licence and attribution
    wording is NOT touched: a text that cannot be redistributed is kept local and not extracted.
    Relative links and bare anchors are resolved against `origin_url`, the place they were
    written for, so no link points at content the extract does not contain.
    """
    def resolve(match: "re.Match[str]") -> str:
        target = match.group(2)
        if re.match(r"(?i)[a-z][a-z0-9+.-]*:", target):
            return match.group(0)
        return match.group(1) + urljoin(origin_url, target) + match.group(3)

    return _MD_LINK.sub(resolve, _EMAIL.sub(EMAIL_REPLACEMENT, text))
