#!/usr/bin/env python3
"""Which of a paper's citations can this checkout adjudicate — and what did the reader find?

## Where this comes from

`CC-20260826-UPSTREAM-CITATION-FAILURE-01` §6. Three groups assert that `Wwox`-null mice have
seizures; of the eight citations they offer, ONE is a primary measurement of that fact in that
animal, and one says the opposite of the sentence it supports. The defect is upstream of LEGEND
and invisible from inside any one paper. It is caught by asking, for a load-bearing assertion
that cites prior work: **does the cited paper contain the asserted fact?** Three outcomes —
`SUPPORTED`, `NOT_CONTAINED`, `CONTRADICTED`.

## What this tool does, and the half it refuses

The question itself is a judgement made by a reader with both texts open. **No string match
approaches it, so this tool never answers it.** What is mechanical, and what the proposal made
mandatory, is the **denominator**: of the m citations in play, how many n point at a paper this
checkout has read in full, and can therefore be adjudicated here at all.

    upstream_citation_census.py --cited 19366774,21447726       # citations named by the reader
    upstream_citation_census.py --from-jats files/fulltext/PMID42422765_x.xml   # a whole ref-list
    upstream_citation_census.py --cited ... --adjudications verdicts.json       # tally a reading

`--adjudications` is a JSON object `{"<cited pmid>": "SUPPORTED" | "NOT_CONTAINED" |
"CONTRADICTED"}` written by the reader. The tool tallies it against the denominator and
**refuses** a verdict on a citation this checkout has not read in full: a verdict with no read
behind it is the very defect being measured.

## 🔴 Bounds the proposal set, kept here on purpose

- **The denominator is printed every time**, and a run with nothing to count exits 3 (void), not
  0 (clean). A check that silently skips what it cannot reach reads as coverage it does not have.
- **A reference without a PMID counts in m and never in n.** Dropping it would make the
  resolvable share look larger than it is.
- **No source genre is taken or reported.** The proposal forbids an automatic distrust of
  reviews: the defect is a review standing where a primary measurement is claimed, and whether
  the asserted fact needs a primary is the reader's call, not a column.
- **It is not a LINT rule.** LINT runs over canonical state and cannot see whether a sentence
  in a paper is carried by its citation; a WARN it could raise would carry no evidence. The
  census runs when a reader is reading, and its output is a worksheet, not a verdict.
- **True of this checkout only.** "Read in full" means a standing `complete_fulltext_read`
  receipt in this tree's ledger; a reading on an unmerged branch is not here.

Exit codes: 0 census printed · 2 invalid invocation or refused adjudication · 3 nothing to count.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import fulltext_receipts as receipts  # noqa: E402

ROOT = HERE.parents[1]
VERDICTS = ("SUPPORTED", "NOT_CONTAINED", "CONTRADICTED")
PMID = re.compile(r"^\d{1,9}$")
REF = re.compile(r"<ref(?=[\s>])[^>]*>(.*?)</ref>", re.S)
REF_PMID = re.compile(r"<pub-id[^>]*pub-id-type=[\"']pmid[\"'][^>]*>\s*(\d{1,9})\s*</pub-id>")


def jats_references(text: str) -> list[str | None]:
    """One entry per `<ref>` in the document: its PMID, or None when it declares none."""
    found: list[str | None] = []
    for body in REF.findall(text):
        match = REF_PMID.search(body)
        found.append(match.group(1) if match else None)
    return found


def complete_reads(root: Path, disease: str) -> dict[str, str]:
    """PMID -> event id of the deepest standing receipt, for complete reads only."""
    index = receipts.receipt_depth_index(receipts.default_ledger_path(root, disease))
    return {key.removeprefix("pmid:"): receipt["event_id"]
            for key, receipt in index.items()
            if key.startswith("pmid:")
            and receipt.get("evidence_depth") == "complete_fulltext_read"}


def census(cited: list[str | None], read: dict[str, str],
           adjudications: dict[str, str]) -> dict:
    """The worksheet. Raises ValueError on a verdict this checkout cannot stand behind."""
    rows = []
    for position, pmid in enumerate(cited, 1):
        receipt = read.get(pmid) if pmid else None
        rows.append({"position": position, "pmid": pmid, "resolvable": bool(receipt),
                     "receipt": receipt, "verdict": adjudications.get(pmid) if pmid else None})
    listed = {row["pmid"] for row in rows if row["pmid"]}
    for pmid, verdict in adjudications.items():
        if verdict not in VERDICTS:
            raise ValueError(f"PMID {pmid}: verdict {verdict!r} is not one of {', '.join(VERDICTS)}")
        if pmid not in listed:
            raise ValueError(f"PMID {pmid}: adjudicated but not among the citations counted")
        if pmid not in read:
            raise ValueError(f"PMID {pmid}: adjudicated as {verdict} but this checkout holds no "
                             f"complete read of it — a verdict with no read behind it is the "
                             f"defect this census exists to find")
    resolvable = [row for row in rows if row["resolvable"]]
    tally = {verdict: sum(row["verdict"] == verdict for row in rows) for verdict in VERDICTS}
    return {"cited": len(rows), "without_pmid": sum(row["pmid"] is None for row in rows),
            "resolvable": len(resolvable),
            "adjudicated": sum(row["verdict"] is not None for row in rows),
            "tally": tally, "rows": rows}


def denominator_line(result: dict) -> str:
    return (f"DENOMINATOR: {result['resolvable']} of {result['cited']} citation(s) resolvable "
            f"against a complete read in this checkout ({result['without_pmid']} without a "
            f"PMID). The other {result['cited'] - result['resolvable']} cannot be adjudicated "
            f"here, and their absence from the tally is not evidence of support.")


def render(result: dict) -> str:
    lines = ["| # | cited PMID | complete read here | verdict (reader) |", "|---|---|---|---|"]
    for row in result["rows"]:
        lines.append(f"| {row['position']} | {row['pmid'] or '— (no PMID)'} | "
                     f"{row['receipt'] or 'no'} | "
                     f"{row['verdict'] or ('____' if row['resolvable'] else 'not adjudicable here')} |")
    lines.append("")
    lines.append(denominator_line(result))
    tally = result["tally"]
    lines.append(f"ADJUDICATED: {result['adjudicated']} of {result['resolvable']} resolvable — "
                 + " · ".join(f"{verdict} {tally[verdict]}" for verdict in VERDICTS))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--cited", help="comma-separated PMIDs of the citations in play")
    source.add_argument("--from-jats", help="a JATS XML full text; every <ref> is counted")
    parser.add_argument("--adjudications", help="JSON object {cited PMID: verdict}")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if args.cited is not None:
        cited: list[str | None] = [item.strip() for item in args.cited.split(",") if item.strip()]
        bad = [item for item in cited if not PMID.match(item)]
        if bad:
            print(f"not a PMID: {', '.join(bad)}", file=sys.stderr)
            return 2
    else:
        path = Path(args.from_jats)
        if not path.is_file():
            print(f"no such file: {path} — files/ is gitignored; pass the checkout that holds it",
                  file=sys.stderr)
            return 2
        cited = jats_references(path.read_text(encoding="utf-8", errors="replace"))

    adjudications: dict[str, str] = {}
    if args.adjudications:
        adjudications = {str(k): str(v) for k, v in
                         json.loads(Path(args.adjudications).read_text(encoding="utf-8")).items()}

    if not cited:
        print("NOTHING TO COUNT — no citation was supplied or found; this is void, not clean")
        return 3
    try:
        result = census(cited, complete_reads(Path(args.root).resolve(), args.disease),
                        adjudications)
    except ValueError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({**result, "denominator": denominator_line(result)}, indent=2))
    else:
        print(render(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
