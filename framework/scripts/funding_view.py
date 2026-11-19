#!/usr/bin/env python3
"""Read-only ORDINAL funding view: which costly study could change which decision (ADV-092).

It renders one self-contained HTML page from two tables in a package folder:

  opportunities.tsv   one row per candidate: the four chain links (L1 target engaged, L2 direction,
                      L3 phenotype relevance, L4 transfer to variant and age) each with an evidence
                      class, the decision the study would change, the null-control status, the shared
                      assay, the blind-check status and what was read.
  cost_ranges.tsv     OPERATOR-SUPPLIED ranges (item, low, high, currency, source, date); header only
                      by default, so every cost prints "not supplied".

What it deliberately does not do:
  * no score and no probability; components stay separate columns and are never summed;
  * 'unknown' is printed as unknown and counts as the lowest class, never as a missing cell;
  * the three sensitivity orderings are LEXICOGRAPHIC (key tuples), not weighted sums, and ties are
    shown as ties;
  * cost is a separate column and a flag, never a sort key, never inside any ordering, and an agent
    never writes it: this tool has no write path to cost_ranges.tsv;
  * it reads no ranking and changes no ranking digest (the repository's next_priority stays
    cost-blind); funding order is not research order, and the page says so first.

Usage:
  python3 framework/scripts/funding_view.py run   [--dir DIR] [--out FILE]
  python3 framework/scripts/funding_view.py check [--dir DIR] [--out FILE]   # exit 1 when FILE is stale
Hypothesis level; reference genotype class only; not medical advice.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DIR = (ROOT / "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/"
               "brainstorm_20261116/generative_engine_funding_adv_20261119/it_adv092_20261119")
DEFAULT_OUT = "FUNDING_VIEW_PREVIEW_IT_ADV092.html"

LINKS = ("L1", "L2", "L3", "L4")
LINK_NAMES = {"L1": "Target engaged", "L2": "Direction", "L3": "Phenotype relevance",
              "L4": "Transfer (variant, age)"}
# Ordinal, low to high. 'n/a' (an assay, not a candidate) is outside the scale.
CLASS_RANK = {"unknown": 0, "ESPANSIONE": 1, "IPOTESI": 2, "INFERENZA": 3,
              "DATO-adjacent": 4, "DATO-matching": 5}
OPP_COLS = ["opp_id", "portfolio", "name", "study_class", "resolves_links", *LINKS, "chain_notes",
            "decision_named", "decision_text", "null_control", "safety_cell", "rows_that_change_decision", "assay_id",
            "ordering_page_row", "blind_check", "read_state", "cost_item", "sources"]
COST_COLS = ["item", "low", "high", "currency", "source", "date"]
NS = "not supplied"


class ViewError(Exception):
    pass


def read_tsv(path: Path, cols: list[str]) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        if rd.fieldnames != cols:
            raise ViewError(f"{path.name}: header {rd.fieldnames} is not {cols}")
        return [dict(r) for r in rd]


def load(d: Path) -> tuple[list[dict], dict[str, dict]]:
    opps = read_tsv(d / "opportunities.tsv", OPP_COLS)
    ids = [o["opp_id"] for o in opps]
    if len(set(ids)) != len(ids):
        raise ViewError("duplicate opp_id")
    for o in opps:
        if o["portfolio"] not in ("ambitious", "conservative"):
            raise ViewError(f"{o['opp_id']}: portfolio must be ambitious or conservative")
        for k in LINKS:
            if o[k] not in CLASS_RANK and o[k] != "n/a":
                raise ViewError(f"{o['opp_id']}: {k}={o[k]!r} is not an evidence class")
        if o["decision_named"] not in ("yes", "no", "unknown"):
            raise ViewError(f"{o['opp_id']}: decision_named")
        if o["null_control"] not in ("named", "partly", "none", "unknown"):
            raise ViewError(f"{o['opp_id']}: null_control")
    costs: dict[str, dict] = {}
    for r in read_tsv(d / "cost_ranges.tsv", COST_COLS):
        try:
            lo, hi = float(r["low"]), float(r["high"])
        except ValueError:
            raise ViewError(f"cost_ranges.tsv: {r['item']}: low and high must be numbers") from None
        if not (0 <= lo <= hi) or not r["currency"] or not r["source"] or not r["date"]:
            raise ViewError(f"cost_ranges.tsv: {r['item']}: need 0 <= low <= high, currency, source, date")
        costs[r["item"]] = {**r, "lo": lo, "hi": hi}
    return opps, costs


def weakest(o: dict) -> list[str]:
    scored = [(CLASS_RANK[o[k]], k) for k in LINKS if o[k] != "n/a"]
    if not scored:
        return []
    low = min(s for s, _ in scored)
    return [k for s, k in scored if s == low]


def resolved(o: dict) -> str:
    wk = weakest(o)
    if not wk:
        return "n/a"
    res = {x.strip() for x in o["resolves_links"].split(",")}
    if res <= {"unknown", ""}:
        return "unknown"
    return "yes" if set(wk) & res else "no"


def sharers(opps: list[dict]) -> dict[str, list[str]]:
    by: dict[str, list[str]] = {}
    for o in opps:
        by.setdefault(o["assay_id"], []).append(o["opp_id"])
    return {o["opp_id"]: [x for x in by[o["assay_id"]] if x != o["opp_id"]] for o in opps}


def keys(opps: list[dict]) -> dict[str, dict[str, tuple]]:
    sh = sharers(opps)
    dec = {"yes": 2, "unknown": 1, "no": 0}
    nul = {"named": 2, "partly": 1, "unknown": 0, "none": 0}
    res = {"yes": 2, "unknown": 1, "n/a": 1, "no": 0}
    out: dict[str, dict[str, tuple]] = {"A": {}, "B": {}, "C": {}}
    for o in opps:
        d, n, r, s = dec[o["decision_named"]], nul[o["null_control"]], res[resolved(o)], len(sh[o["opp_id"]])
        out["A"][o["opp_id"]] = (d, n, r, s)
        out["B"][o["opp_id"]] = (r, d, n, s)
        out["C"][o["opp_id"]] = (s, d, r, n)
    return out


def dense_rank(key: dict[str, tuple]) -> dict[str, int]:
    order = sorted(set(key.values()), reverse=True)
    return {i: order.index(k) + 1 for i, k in key.items()}


def info_ranks(opps: list[dict]) -> dict[str, int] | None:
    vals = {o["opp_id"]: int(o["rows_that_change_decision"]) for o in opps
            if o["rows_that_change_decision"].isdigit()}
    if len(vals) < 2:
        return None
    return dense_rank({i: (v,) for i, v in vals.items()})


def cost_of(o: dict, costs: dict) -> dict | None:
    return costs.get(o["cost_item"])


def fmt_cost(c: dict | None) -> str:
    if not c:
        return NS
    return f"{c['low']} to {c['high']} {c['currency']} ({c['source']}, {c['date']})"


def pair_cost(a: dict, b: dict, costs: dict) -> str:
    ca, cb = cost_of(a, costs), cost_of(b, costs)
    n = (ca is not None) + (cb is not None)
    if n < 2:
        return f"{NS} ({n} of 2)"
    if ca["currency"] != cb["currency"]:
        return "two ranges in different currencies (not added)"
    return f"{ca['lo'] + cb['lo']:g} to {ca['hi'] + cb['hi']:g} {ca['currency']} (sum of two supplied ranges)"


E = html.escape
CSS = """:root{--bg:#fbfbf8;--fg:#1d2321;--mut:#58625d;--line:#d6dad4;--card:#fff;--hd:#eef1ec;--warn:#8a4b00}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#15191a;--fg:#e6e9e4;--mut:#a3aea8;--line:#334039;--card:#1c2223;--hd:#232b2c;--warn:#e0a45a}}
body{background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif;margin:0;padding:0 16px 48px}
main{max-width:1180px;margin:0 auto}h1{font-size:1.35rem;margin:20px 0 6px}h2{font-size:1.05rem;margin:28px 0 6px}
.first{border:2px solid var(--warn);padding:10px 12px;border-radius:6px;font-weight:600;margin:14px 0}
.note{color:var(--mut);font-size:.88rem;margin:4px 0 10px}.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:6px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:.84rem}th,td{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}
th{background:var(--hd);position:sticky;top:0}td.u{font-style:italic;color:var(--mut)}code{font-size:.82rem}
details{margin:6px 0}summary{cursor:pointer}"""


def cell(v: str) -> str:
    cls = ' class="u"' if v in ("unknown", NS, "n/a") else ""
    return f"<td{cls}>{E(v)}</td>"


def table(head: list[str], rows: list[list[str]], tag: str) -> str:
    h = "".join(f"<th>{E(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(cell(c) for c in r) + "</tr>" for r in rows)
    return f'<div class="scroll"><table data-table="{tag}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def render(d: Path) -> str:
    opps, costs = load(d)
    sh = sharers(opps)
    wk = {o["opp_id"]: weakest(o) for o in opps}
    K = keys(opps)
    R = {n: dense_rank(K[n]) for n in K}
    info = info_ranks(opps)
    digest = hashlib.sha256((d / "opportunities.tsv").read_bytes() + (d / "cost_ranges.tsv").read_bytes()).hexdigest()[:16]
    p: list[str] = []
    p.append("<h1>Which study could change which decision: an ordinal view</h1>")
    p.append('<p class="first">Funding order is not research order. Nothing on this page is a score, a probability of benefit '
             'or a recommendation; the orderings below are declared, ordinal, and shown beside the evidence they rest on.</p>')
    p.append('<p class="note">Hypothesis level. Reference genotype class only. Not medical advice. Costs appear only as ranges the '
             f'operator supplies ({sum(1 for _ in costs)} supplied; default "{NS}"). Input digest {digest}.</p>')
    # Table A
    head = ["Candidate", "Portfolio", "Study class", *[f"{k} {LINK_NAMES[k]}" for k in LINKS],
            "Weakest link(s)", "Study resolves the weakest?", "Decision named", "Null control", "Safety (per agent and age; never in an ordering)", "Shared assay",
            "Blind check", "Cost range", "Cost flag"]
    rows = []
    for o in opps:
        c = cost_of(o, costs)
        share = f"{o['assay_id']} (with {', '.join(sh[o['opp_id']])})" if sh[o["opp_id"]] else f"{o['assay_id']} (alone)"
        rows.append([f"{o['opp_id']} {o['name']}", o["portfolio"], o["study_class"], *[o[k] for k in LINKS],
                     ", ".join(wk[o["opp_id"]]) or "n/a", resolved(o), f"{o['decision_named']}: {o['decision_text']}",
                     o["null_control"], o["safety_cell"], share, o["blind_check"], fmt_cost(c), "supplied" if c else NS])
    p.append("<h2>1. Candidates: components as separate columns</h2>")
    p.append('<p class="note">Evidence classes, low to high: unknown, ESPANSIONE, IPOTESI, INFERENZA, DATO-adjacent (a datum in another '
             'system, stage or only at abstract level), DATO-matching (a datum in the system the study would use). The weakest link is '
             'the lowest class; unknown is the lowest and is printed as unknown. A mid-chain study resolves L1 and L2, not L3 or L4.</p>')
    p.append(table(head, rows, "components"))
    # strip
    p.append("<h2>2. Sensitivity strip: rank under three declared orderings</h2>")
    p.append('<p class="note">Each ordering is a lexicographic key (no weights, no sums): '
             'A = decision named, null control, weakest link resolved, assay sharing; '
             'B = weakest link resolved, decision named, null control, assay sharing; '
             'C = assay sharing, decision named, weakest link resolved, null control. '
             'Rank 1 is first; equal keys share a rank. A wide range means the position depends on the ordering chosen, not on the evidence. '
             'The keys measure how ready a study is to be judged (a decision named, a null that can be read, the weakest link reachable, a preparation already shared); they contain no benefit, no safety and no cost, so rank 1 is not a verdict on a candidate. '
             'Assay sharing counts candidates tagged to one preparation, which may be several stages of one programme rather than one study.</p>')
    srows = []
    for o in opps:
        i = o["opp_id"]
        rs = [R["A"][i], R["B"][i], R["C"][i]]
        srows.append([f"{i} {o['name']}", str(rs[0]), str(rs[1]), str(rs[2]), f"{min(rs)} to {max(rs)}"])
    p.append(table(["Candidate", "Ordering A", "Ordering B", "Ordering C", "Range"], srows, "strip"))
    if info:
        irows = [[f"{o['opp_id']} {o['name']}", str(info.get(o["opp_id"], "unknown")),
                  o["rows_that_change_decision"] or "unknown"] for o in opps]
        p.append('<p class="note">Information-value sensitivity (not an ordering of merit; counts the outcome rows of a dossier that '
                 'would change a decision and claims no probability):</p>')
        p.append(table(["Candidate", "Rank", "Outcome rows that change a decision (of 3)"], irows, "info"))
    else:
        n = sum(1 for o in opps if o["rows_that_change_decision"].isdigit())
        p.append(f'<p class="note">Information-value sensitivity: not available; {n} of {len(opps)} candidates have a dossier '
                 "stating which outcome rows change a decision.</p>")
    # assays
    p.append("<h2>3. Shared assays</h2>")
    by: dict[str, list[str]] = {}
    for o in opps:
        by.setdefault(o["assay_id"], []).append(f"{o['opp_id']} ({o['portfolio']})")
    p.append(table(["Assay or preparation", "Candidates it serves", "Count"],
                   [[a, ", ".join(v), str(len(v))] for a, v in sorted(by.items())], "assays"))
    # pairs
    p.append("<h2>4. Pairs: one ambitious and one conservative candidate (listed by id, not ordered)</h2>")
    p.append('<p class="note">The pair, not the top two names. "Shares an assay" is a design fact, not a merit. A pair cost is shown only '
             "when both ranges are supplied in one currency, and is never a sort key.</p>")
    amb = [o for o in opps if o["portfolio"] == "ambitious"]
    con = [o for o in opps if o["portfolio"] == "conservative"]
    prow = []
    for a, b in product(amb, con):
        same = a["assay_id"] == b["assay_id"]
        both = a["decision_named"] == "yes" and b["decision_named"] == "yes"
        prow.append([f"{a['opp_id']} + {b['opp_id']}", f"yes: {a['assay_id']}" if same else "no",
                     "both yes" if both else "not both", f"{resolved(a)} / {resolved(b)}", pair_cost(a, b, costs)])
    p.append(table(["Pair", "Shares an assay", "Decision named", "Weakest resolved (ambitious / conservative)", "Pair cost"], prow, "pairs"))
    # details
    p.append("<h2>5. What was read for each row</h2>")
    for o in opps:
        p.append(f"<details><summary>{E(o['opp_id'])} {E(o['name'])}</summary><p><b>Chain notes.</b> {E(o['chain_notes'])}</p>"
                 f"<p><b>Read in this window.</b> {E(o['read_state'])}</p><p><b>Ordering page row.</b> {E(o['ordering_page_row'])}. "
                 f"<b>Sources.</b> <code>{E(o['sources'])}</code></p></details>")
    p.append('<p class="note">Limits: the classes are the row author\'s reading of the cited sources, not a re-audit; a blank or unread '
             "link is printed as unknown. Source tables: opportunities.tsv and cost_ranges.tsv (operator-supplied only).</p>")
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>Funding view</title><style>{CSS}</style></head><body><main>{''.join(p)}</main></body></html>\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["run", "check"])
    ap.add_argument("--dir", type=Path, default=DEFAULT_DIR)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args(argv)
    out = a.out or a.dir / DEFAULT_OUT
    try:
        text = render(a.dir)
    except (ViewError, OSError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    if a.cmd == "run":
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out} ({len(text)} bytes)")
        return 0
    if not out.exists() or out.read_text(encoding="utf-8") != text:
        print(f"STALE: {out} differs from a fresh render (run `funding_view.py run`)")
        return 1
    print("OK: preview is current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
