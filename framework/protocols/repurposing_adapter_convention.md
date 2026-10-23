# Repurposing adapter convention — one page, no contract

Written by Harness Engineering (`plan`) on 2026-10-23 under
`PLAN-DRUGREPURPOSING-MODULE-20261022`, on the operator's instruction of 2026-10-22: lean,
flexible, modular; easy to implement, easy to remove; **no rigid contracts**. This page is a
convention a reader follows, not a schema a validator enforces. Not medical advice.

## Where

`framework/adapters/<name>.py` — one file per external source. The directory is under
`framework/` because an adapter is generic engine (it knows a service, not a disease); it is
**not** under `framework/scripts/` because every tool there must be routed in the scripts README
(`scripts/test_tool_routing.py`), and an adapter must be added or deleted with nothing else to
edit. The CLI `framework/scripts/repurposing_adapter.py` is routed once and discovers the
adapters by listing the directory. A file whose name starts with `_` is not an adapter (`_http.py`
is the shared four-line HTTP door).

## What a file holds

```python
INFO = {"name": "<file stem>", "gives": "...", "network": "GET https://...", "licence": "...; key-less, no payment",
        "inputs": "...", "outputs": "...",
        "licence_url": "<the terms page you read>", "licence_read_on": "<YYYY-MM-DD>",
        "licence_terms": "<what it says: attribution, share-alike, rate limit, user-agent>",
        "citation": "<the citation the source asks for, with DOI>", "attribution": "<credit line printed with the data>"}

def query(request: dict, fetch=_http.get_json) -> dict: ...   # dict in, dict out
SAMPLE = {"request": {...}, "response": (200, {...})}          # one canned exchange
def selftest(fetch=None) -> dict: ...                           # offline with SAMPLE; live when fetch is given
```

`fetch(url, params=None, body=None, timeout=20) -> (http_status, parsed_json_or_text)` is the
only seam: tests inject canned responses, `selftest --live` injects the real door.

## What `query` returns

A plain dict with these keys, nothing enforced beyond `check_output()` in the CLI reporting a
missing one:

| key | value |
|---|---|
| `adapter` | `INFO["name"]` |
| `retrieved_at` | UTC timestamp of this call (every external statement carries its date) |
| `request`, `requests_sent` | what was asked, and the URLs actually hit (the query is reproducible) |
| `status` | `MATCH_FOUND` · `NO_MATCH_FOUND` · `QUERY_ERROR` — the bridge's own words (`repurposing_bridge.py`), so a card can carry them unchanged |
| `hits` | a list of dicts with the source's fields verbatim; **no `score`, `rank`, `probability`, `belief` key** — a scalar from a source is dropped at the adapter |
| `source_version` | the version the service states for itself (`ChEMBL_37`, `api 26.9.0 data 26.09`, a payload date) or `UNKNOWN` — a value, not a schema field |
| `evidence_label` | always `NOT WWOX EVIDENCE` |
| `licence`, `citation` | copied from `INFO`, so every output names its source, its licence and the citation the source asks for, beside `retrieved_at` |
| `note` | says that `NO_MATCH_FOUND` is an answer about this query on this date, never absence |
| `error` | the text returned, when `QUERY_ERROR` |

Three states, three different facts: an empty answer is `NO_MATCH_FOUND`; a transport failure,
an HTTP 5xx or a malformed payload is `QUERY_ERROR` with the text kept; HTTP 404 is whatever the
service means by it (openFDA: no match). An empty `request` is a `QUERY_ERROR`, not a search.

## Adding, removing, checking

```
python3 framework/scripts/repurposing_adapter.py add <name>        # writes the template; fill it in
python3 framework/scripts/repurposing_adapter.py selftest [name]   # offline; add --live to call the service
python3 framework/scripts/repurposing_adapter.py remove <name>     # deletes the file; nothing else changes
python3 framework/scripts/repurposing_adapter.py query <name> '{"...": "..."}'
```

`framework/scripts/test_repurposing_adapter.py` (in the release battery) removes every adapter in
turn in a temporary copy and asserts the rest stay green and byte-identical, so the one-file
promise is measured, not stated.

## Licences, read not remembered (operator instruction, 2026-10-23)

Before an adapter is written, its source's licence or terms page is **read** and quoted in
`INFO["licence_terms"]` with the URL and the date; what the licence asks for (attribution text,
the paper to cite, share-alike, rate limits, user-agent or contact) is complied with inside the
adapter; a source whose terms need a key, a payment, a signed agreement or are unclear is a
recorded block and is not used. `disease-models/wwox/research/drug_repurposing/ACKNOWLEDGEMENTS.md`
is rendered from these fields (`acknowledgements --write`; `add` and `remove` re-render it) and
thanks the maintainers; the test fails if it is stale. No e-mail address appears in any record.

## What was deliberately not built

No abstract base class, no registry file, no schema or validator layer, no version field, no
plugin framework, no dependency injection, no configuration language, no retry policy, no cache.
An adapter that needs any of these is the wrong adapter. Licence, retrieval date and query travel
as values in the output, which is where a reader of a card finds them.
