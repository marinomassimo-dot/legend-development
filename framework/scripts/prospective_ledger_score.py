#!/usr/bin/env python3
"""Mechanical log score for a prospective prediction ledger: a binned sidecar with its own digest, an observed-value table, and a refusal for any value without a locator.

A prospective ledger is a register of predictions made BEFORE the data exist (SCI's `PROSPECTIVE_LEDGER_SCI_20261116.md` is the first). Its markdown table is the human text; the
SIDECAR is the machine text: a TSV with one row per probability bin, hashed and frozen before any datum arrives, so the score cannot depend on how a range is read afterwards.

  python3 prospective_ledger_score.py check SIDECAR.tsv                      validate and print the sha256 to freeze and send
  python3 prospective_ledger_score.py score SIDECAR.tsv OBSERVED.tsv [--expect-sha256 HEX] [--floor 0.001]

SIDECAR.tsv columns (tab separated, header required): id, who, bin_low, bin_high, probability.
  `who` names the forecaster (ledger, naive, delegate ...); for each (id, who) the bins must not overlap and the probabilities must sum to 1 within 1e-6. A bin is [low, high):
  inclusive low, exclusive high, `-inf` and `inf` allowed; bins need not cover the whole line, but an observed value outside every bin of a forecaster is scored with the floor.
  Probability 0 is allowed. A point forecast (a naive rule) is written as a narrow bin carrying most of the probability, the rest spread over the other bins; the convention is yours
  and is part of the digest.
OBSERVED.tsv columns: id, value, locator, and an OPTIONAL note.  `locator` is required and must say where the value was read (file, table row, figure panel, page): an empty value, `-`, `?`, `tbd`,
  `todo` or `n/a` is refused. An id absent from the sidecar is refused. No value is ever read from a chat message or from the sidecar itself.
The note (a limit such as 'below the readability threshold' or 'interval touches 0') is printed beside the score and NEVER excludes a line: a line is scored by its registered bin (ADV's rule of 2026-11-16);
  'not scorable' only for the reasons registered with the ledger (below the stated minimum n, no locator, no observed value), which are refusals here.
Score: the natural log of the probability the forecaster put on the bin that contains the observed value (the floor replaces a probability below it, so a bin with 0 costs ln(floor));
  per id and forecaster, then the sum per forecaster over the ids observed. A higher (less negative) total is better; the ledger 'improves' only if it beats both baselines on a second
  ledger of this kind (SCI's rule); this tool only computes the numbers. Nothing here is evidence about biology; it scores the forecasters. Not medical advice.
Refusals (exit 1, nothing printed as a score): sidecar digest differs from --expect-sha256; a malformed bin; overlapping bins; probabilities not summing to 1; an observed id not in the sidecar; a missing or placeholder locator; a non-numeric value.
"""
from __future__ import annotations
import csv, hashlib, math, sys
from collections import defaultdict
from pathlib import Path

PLACEHOLDERS = {"", "-", "?", "tbd", "todo", "n/a", "na", "none", "unknown"}


def die(msg: str) -> "None":
    sys.stderr.write("REFUSED: " + msg + "\n")
    raise SystemExit(1)


def num(s: str, what: str) -> float:
    s = s.strip().lower()
    if s in ("inf", "+inf"):
        return math.inf
    if s == "-inf":
        return -math.inf
    try:
        return float(s)
    except ValueError:
        die(f"{what}: {s!r} is not a number")


def read_tsv(path: str, cols: list[str]) -> list[dict]:
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8"), delimiter="\t"))
    if not rows:
        die(f"{path}: no rows")
    for c in cols:
        if c not in rows[0]:
            die(f"{path}: missing column {c!r} (needs {cols})")
    return rows


def load_sidecar(path: str) -> dict:
    by: dict = defaultdict(list)
    for i, r in enumerate(read_tsv(path, ["id", "who", "bin_low", "bin_high", "probability"]), 2):
        lo, hi, p = num(r["bin_low"], f"row {i} bin_low"), num(r["bin_high"], f"row {i} bin_high"), num(r["probability"], f"row {i} probability")
        if not lo < hi:
            die(f"row {i} ({r['id']}/{r['who']}): bin_low {lo} is not below bin_high {hi}")
        if not 0.0 <= p <= 1.0:
            die(f"row {i} ({r['id']}/{r['who']}): probability {p} outside [0, 1]")
        by[(r["id"].strip(), r["who"].strip())].append((lo, hi, p))
    for (i, w), bins in by.items():
        bins.sort()
        for a, b in zip(bins, bins[1:]):
            if b[0] < a[1]:
                die(f"{i}/{w}: bins [{a[0]}, {a[1]}) and [{b[0]}, {b[1]}) overlap")
        if abs(sum(p for *_, p in bins) - 1.0) > 1e-6:
            die(f"{i}/{w}: probabilities sum to {sum(p for *_, p in bins):.6f}, not 1")
    return by


def sha(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prob_of(bins: list, x: float) -> float | None:
    for lo, hi, p in bins:
        if lo <= x < hi:
            return p
    return None


def cmd_check(a: list[str]) -> int:
    by = load_sidecar(a[0])
    ids = sorted({i for i, _ in by}); who = sorted({w for _, w in by})
    print(f"OK sidecar: {len(ids)} ids, forecasters {who}, {sum(len(v) for v in by.values())} bins")
    print(f"sha256 {sha(a[0])}  {Path(a[0]).name}")
    return 0


def cmd_score(a: list[str]) -> int:
    args = [x for x in a]; expect = None; floor = 0.001
    if "--expect-sha256" in args:
        k = args.index("--expect-sha256"); expect = args[k + 1]; del args[k:k + 2]
    if "--floor" in args:
        k = args.index("--floor"); floor = float(args[k + 1]); del args[k:k + 2]
    if len(args) != 2:
        die("usage: score SIDECAR.tsv OBSERVED.tsv [--expect-sha256 HEX] [--floor F]")
    if expect and sha(args[0]) != expect:
        die(f"the sidecar hashes to {sha(args[0])}, not the digest frozen before the data ({expect})")
    by = load_sidecar(args[0]); obs = read_tsv(args[1], ["id", "value", "locator"])
    totals: dict = defaultdict(float); lines = []
    seen = set()
    for r in obs:
        i = r["id"].strip()
        if i in seen:
            die(f"observed id {i} appears twice")
        seen.add(i)
        if r["locator"].strip().lower() in PLACEHOLDERS:
            die(f"observed id {i} has no locator (where was the value read?): refused")
        if not any(k[0] == i for k in by):
            die(f"observed id {i} is not in the sidecar")
        x = num(r["value"], f"observed {i} value"); note = (r.get("note") or "").strip()
        for (sid, w), bins in sorted(by.items()):
            if sid != i:
                continue
            p = prob_of(bins, x); eff = max(p if p is not None else 0.0, floor)
            totals[w] += math.log(eff)
            lines.append((i, w, x, "outside every bin" if p is None else f"p={p:g}", math.log(eff), note))
    print("id\twho\tvalue\tbin\tlog_score\tnote")
    for i, w, x, b, s, nt in lines:
        print(f"{i}\t{w}\t{x:g}\t{b}\t{s:.4f}\t{nt}")
    print("TOTAL\t" + "\t".join(f"{w}={t:.4f}" for w, t in sorted(totals.items())) + f"\t(ids observed: {len(seen)}; floor {floor})")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help", "help"):
        print(__doc__)
        return 0
    if argv[1] == "check" and len(argv) == 3:
        return cmd_check(argv[2:])
    if argv[1] == "score":
        return cmd_score(argv[2:])
    die("usage: prospective_ledger_score.py check SIDECAR.tsv | score SIDECAR.tsv OBSERVED.tsv [--expect-sha256 HEX] [--floor F]")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
