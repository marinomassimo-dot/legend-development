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
import os
import time
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
# Third-party text is never "cleaned" into a different text: licence wording and notices are not
# altered automatically, and a modified text is not called licence-intact. When a document carries
# an e-mail address (typically in a copyright or contact notice) `public_extract` REFUSES it; the
# asset stays local and the repository gets `reference_record` (own structured data plus origin,
# digest and licence identifier) instead of the third-party bytes.


class NoticeContainsAddress(ValueError):
    """The text holds e-mail addresses (count and line numbers are reported, never the addresses)."""

_EMAIL = re.compile(r"(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9_%+-])")
_INLINE_LINK = re.compile(r"(!?\[[^\]]*\]\()(<[^>\n]*>|[^)\s]+)((?:\s+(?:\"[^\"]*\"|'[^']*'))?\))")
_REF_DEF = re.compile(r"(?m)^(\s{0,3}\[[^\]\n]+\]:[ \t]*)(<[^>\n]*>|\S+)")
_HTML_ATTR = re.compile(r"(?i)(\b(?:href|src)\s*=\s*)([\"'])(.*?)\2")


def keep_original(corpus_dir, name: str, data: bytes, origin: str, revision: str) -> dict:
    """Write `data` unchanged under `corpus_dir/name` and return its manifest record.

    Never silently alters an original: if `name` exists with different bytes it raises, and a
    `name` that resolves outside `corpus_dir` raises ValueError. The record (`sha256`, `bytes`,
    `origin`, `revision`) is what the tracked package keeps, as a digest line, in place of the
    third-party bytes.
    """
    root = Path(corpus_dir).resolve()
    path = (root / name).resolve()
    if path == root or root not in path.parents:
        raise ValueError(f"{name!r} resolves outside the corpus directory {root}")
    if path.exists() and path.read_bytes() != data:
        raise FileExistsError(f"{path} exists with different bytes; keep the old original and name the new one")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(data)
    return {"name": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
            "origin": origin, "revision": revision}


def _unobfuscated(line: str) -> str:
    """Fold the common ways an address is written to dodge a scanner (percent- or entity-encoded at sign, full-width at sign, '[at]'/'(at)') so that they are refused like a plain one."""
    out = line.replace("%40", "@").replace("&#64;", "@").replace("&#x40;", "@").replace("\uff20", "@")
    return re.sub(r"\s*[\[(]\s*at\s*[\])]\s*", "@", out, flags=re.I)


def addresses_in(text: str) -> list[int]:
    """Line numbers (1-based) of the lines that contain an e-mail address, including `mailto:` targets."""
    return [n for n, line in enumerate(text.splitlines(), 1) if _EMAIL.search(_unobfuscated(line))]


def reference_record(record: dict, licence_id: str, own_notes: str = "") -> str:
    """The publishable stand-in for a third-party document that cannot be extracted: a reference by origin, revision, SHA-256 and licence
    identifier (SPDX or the name the source gives), plus what WE concluded from it. `record` is what `keep_original` returned."""
    lines = [f"- document: {record['name']}", f"- origin: {record['origin']}", f"- revision: {record['revision']}",
             f"- sha256: {record['sha256']} ({record['bytes']} bytes, original kept in the local corpus)", f"- licence: {licence_id}"]
    if own_notes:
        lines.append(f"- our notes: {own_notes}")
    return "\n".join(lines) + "\n"


def public_extract(text: str, origin_url: str) -> str:
    """The publishable form of a fetched Markdown/HTML text: THE TEXT UNCHANGED except that relative links are made absolute.

    Licence wording, copyright lines and notices are never rewritten. If the text contains an e-mail address (including a `mailto:` target)
    it raises `NoticeContainsAddress` with the line numbers: the address would enter the repository, and masking it would alter a notice the
    licence may require. The caller then keeps the document local (`keep_original`) and tracks `reference_record(...)` instead, or extracts
    only its own structured information. A text that cannot be redistributed is likewise kept local and not extracted.
    Relative link targets (inline links, images, reference definitions, `<angle>` targets, HTML href/src) and bare anchors are resolved
    against `origin_url`, the place they were written for, so no link points at content the extract does not contain. Absolute URLs and other
    schemes are left alone.
    """
    lines = addresses_in(text)
    if lines:
        raise NoticeContainsAddress(f"{len(lines)} line(s) contain an e-mail address (lines {lines[:10]}); keep the document local and track reference_record() instead of rewriting it")

    def absolute(target: str) -> str:
        if not target or re.match(r"(?i)[a-z][a-z0-9+.-]*:", target):
            return target
        return urljoin(origin_url, target)

    def angle(target: str) -> str:
        return "<" + absolute(target[1:-1]) + ">" if target.startswith("<") else absolute(target)

    text = _INLINE_LINK.sub(lambda m: m.group(1) + angle(m.group(2)) + m.group(3), text)
    text = _REF_DEF.sub(lambda m: m.group(1) + angle(m.group(2)), text)
    return _HTML_ATTR.sub(lambda m: m.group(1) + m.group(2) + absolute(m.group(3)) + m.group(2), text)


ERROR_KEYS = {"error", "errors", "detail", "message"}


def payload_problem(payload, expect: str | None = None) -> str | None:
    """Why a 200 answer is not worth keeping, or None. ONE test, used when an entry is written and when it is read.

    Not worth keeping: not JSON-structured, empty, a bare error envelope (only error/errors/detail/message keys), or, when the caller says
    which key a good answer carries (`expect`), an object without it. An answer that has the expected key but an empty list (a ChEMBL page of
    zero rows with its normal `page_meta`) is a legitimate empty answer and passes."""
    if not isinstance(payload, (dict, list)) or not payload:
        return "empty or not structured"
    if isinstance(payload, dict) and set(payload) <= ERROR_KEYS:
        return "bare error envelope"
    if expect and not (isinstance(payload, dict) and expect in payload):
        return f"expected key {expect!r} absent"
    return None


def make_fetch(cache_dir: str | None = None, retries: int = 2, pause: float = 6.0, get=None, sleep=time.sleep):
    """A `fetch` for the adapters with a bounded retry and an optional response cache; the adapters take it through `query(request, fetch=...)`.

    * Retry: a transport failure (status 0) or an HTTP 5xx is tried again at most `retries` times (`pause` seconds apart); a 4xx is an answer and is not
      retried. Every failed attempt is appended to `fetch.failures` ({url, http, attempt, text}); nothing is retried silently and nothing loops.
    * Cache (only when `cache_dir` is given, an explicit path; nothing is written otherwise): only a successful (HTTP 200) response that passes `payload_problem` is stored, one JSON file
      per request keyed by SHA-256 of the full URL, body and parameters, with its own `retrieved_at`. An error, a 404 or an empty 'no result' answer for a
      query that failed is never stored, so a cache hit can never turn an error into 'no result'. The key does not contain the database release: use one
      directory per release, or delete it, to refresh. Rerunning a query after a failure fetches only the requests (pages, batches) that are not yet cached.
    * The same `payload_problem` test runs on READ: an older, damaged or semantically invalid entry (error-only body, missing the key the caller
      passes as `expect=`) is a miss, is renamed to `<key>.json.discarded` (kept, not deleted; one per key), counted in `stats["cache_discarded"]` and listed in `fetch.discarded`,
      and the answer is fetched again under the same bounded retry. `fetch.validates` is True so an adapter may pass `expect=`.
    * `fetch.stats` counts cache hits, discarded entries, network requests, failed attempts and requests that ended in an error."""
    inner = get or get_json
    stats = {"cache_hits": 0, "cache_discarded": 0, "network_requests": 0, "failed_attempts": 0, "requests_ended_in_error": 0}
    failures: list = []
    discarded: list = []

    def key(url, params, body):
        return hashlib.sha256(json.dumps([url, params, body], sort_keys=True, default=str).encode("utf-8")).hexdigest()

    def fetch(url, params=None, body=None, timeout=20.0, expect=None):
        path = os.path.join(cache_dir, key(url, params, body) + ".json") if cache_dir else None
        if path and os.path.isfile(path):
            reason, stored = None, None
            try:
                with open(path, encoding="utf-8") as fh:
                    stored = json.load(fh)
                if not (isinstance(stored, dict) and stored.get("http") == 200 and stored.get("url") == url):
                    reason = "entry header does not match the request"
                else:
                    reason = payload_problem(stored.get("payload"), expect)
            except OSError:
                reason = "unreadable"
            except ValueError:
                reason = "damaged JSON"
            if reason is None:
                stats["cache_hits"] += 1
                return 200, stored["payload"]
            stats["cache_discarded"] += 1  # a bad entry is a miss, never an answer; kept aside, not deleted
            kept = path + ".discarded"
            n = 1
            while os.path.exists(kept):  # an earlier discarded entry is evidence too: never overwrite it
                n += 1
                kept = f"{path}.discarded.{n}"
            try:
                os.replace(path, kept)
            except OSError:
                kept = None
            discarded.append({"url": url, "reason": reason, "kept_as": kept})
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
        if status == 200 and path and payload_problem(payload, expect) is None:
            os.makedirs(cache_dir, exist_ok=True)
            tmp = path + ".part"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump({"url": url, "http": 200, "retrieved_at": now_utc(), "payload": payload}, fh)
            os.replace(tmp, path)
        return status, payload

    fetch.stats, fetch.failures, fetch.discarded, fetch.validates = stats, failures, discarded, True
    return fetch
