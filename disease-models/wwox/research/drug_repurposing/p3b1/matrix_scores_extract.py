#!/usr/bin/env python3
"""Read the MATRIX scores for NAMED disease nodes through the Hugging Face datasets-server `filter` endpoint.

No bulk download, no token, no account: one filtered, paged GET per disease. The ORIGINAL response bytes of every page
are digested (sha256) and the digests recorded next to the rows, so a rerun can be compared byte for byte.
Rows are predictions of a computational pipeline. This script emits no score of its own, ranks nothing and converts
nothing into a probability of efficacy; it only fetches what the publisher computed, with the publisher's column names.

Usage: matrix_scores_extract.py <outdir> <MONDO:id> [<MONDO:id> ...]
Writes <outdir>/matrix_scores_raw.json  {"meta": {...}, "rows": {MONDO: [row, ...]}}
Dataset terms: the dataset card declares NO licence (see ../tool_survey_20261022.md, MATRIX row); keep what you
commit to a handful of rows and never redistribute the table.
"""
import datetime
import hashlib
import json
import sys
import time
import urllib.parse
import urllib.request

DATASET = "everycure/matrix-scores"
ENDPOINT = "https://datasets-server.huggingface.co/filter"


def page(target, offset, length=100, tries=30):
    q = urllib.parse.urlencode({"dataset": DATASET, "config": "default", "split": "train",
                                "where": f"\"target\"='{target}'", "offset": offset, "length": length})
    req = urllib.request.Request(ENDPOINT + "?" + q, headers={"User-Agent": "legend-repurposing"})
    for attempt in range(tries):
        try:
            return urllib.request.urlopen(req, timeout=180).read()
        except Exception as exc:  # 5xx while the server rebuilds its index; 429 rate limit
            print(f"retry {target} offset {offset}: {exc}", file=sys.stderr, flush=True)
            time.sleep(min(10 * (attempt + 1), 30))
    raise SystemExit(f"giving up on {target} offset {offset}")


def main(outdir, targets):
    rows, digests, totals = {}, {}, {}
    for t in targets:
        rows[t], digests[t], off = [], [], 0
        while True:
            raw = page(t, off)
            d = json.loads(raw)
            digests[t].append(hashlib.sha256(raw).hexdigest())
            totals[t] = d["num_rows_total"]
            rows[t] += [r["row"] for r in d["rows"]]
            off += 100
            if off >= totals[t]:
                break
        print(t, totals[t], len(rows[t]), flush=True)
    meta = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "dataset": DATASET, "endpoint": ENDPOINT,
            "num_rows_total": totals, "page_sha256": digests}
    json.dump({"meta": meta, "rows": rows}, open(f"{outdir}/matrix_scores_raw.json", "w"))


if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        raise SystemExit(0)
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2:])
