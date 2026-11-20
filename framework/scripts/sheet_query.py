#!/usr/bin/env python3
"""Ask the ADV-098 agent data sheets one question at a time: what do they say about an agent's potency, state dependence, exposure, harm or label, with the caveats beside it.

    python3 framework/scripts/sheet_query.py AGENT [--quantity potency|exposure|harm|label|comparable|all] [--alias NAME ...] [--json]
    python3 framework/scripts/sheet_query.py --list                      # the sheets read and the number of bullets indexed

WHY (ADV-103, 2026-11-20). Each compound-level comparison of the day re-read eleven sheets, and the one-origin flags were the main source of review corrections. The sheets stay the
source and are not edited; this is a DERIVED view, rebuilt on every call and never stored. It does NOT parse values out of prose (a regular expression over "IC50 18 nM at -80 mV, 2011" would be
a second reading with its own errors). It returns the sheet's own bullets VERBATIM with file and line, so every answer can be checked against the sheet by `grep -n`, and it keeps the three things
a number needs beside it: the batch's COMPARABLE? bullets that name the agent, the dated corrections that name it (a correction is never merged into the original wording), and, for the potency
question, the structured ChEMBL rows of `activities_expected_targets.tsv` grouped by ORIGIN (rows from one document are one origin; the same target, value and unit in two documents is flagged as
possibly one origin quoted twice).

What it cannot represent: a caveat that lives in the sentence of another agent's bullet, a condition stated in a table row of a different section, or a conclusion that needs two bullets read
together. It returns the bullets that name the agent; reading them together is still the reader's. An agent not named anywhere answers "not named in these sheets", which is not absence.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DIR = ROOT / "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/adv098_agent_sheets_he_20261119"

QUANTITY = {
    "potency": r"potency|target|selectiv|affinity|ic50|\bki\b|state dep|holding|voltage|kinase|binding|off-target",
    "exposure": r"exposure|brain|csf|cerebrospinal|pharmacokinetic|plasma|concentration|half-life|juvenile|pup",
    "harm": r"harm|tolerab|adverse|safety|sedat|toxic|signal|boxed|warning",
    "label": r"label|trial|registr|clinicaltrials|approved|indicat",
}
HEAD = re.compile(r"^(#{1,3})\s+(.*)$")
BULLET = re.compile(r"^-\s+(.*)$")
LABEL = re.compile(r"^\*\*(.+?)\*\*")


def parse_sheet(path: Path) -> list[dict]:
    """Every bullet of one sheet with its section heading, bold label, line number and verbatim text. A table row is indexed too, under the heading above it."""
    out, section = [], ""
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        h = HEAD.match(line)
        if h:
            section = h.group(2).strip()
            continue
        b = BULLET.match(line)
        row = line.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", line)
        para = bool(line.strip()) and not b and not row and re.match(r"what is not found|(second )?dated ", section.lower())     # the absence paragraphs and the dated lines of a batch are prose, not bullets, and are caveats too
        if not (b or row or para):
            continue
        text = b.group(1) if b else line
        lab = LABEL.match(text)
        out.append({"file": path.name, "line": n, "section": section, "label": (lab.group(1) if lab else ""), "text": text})
    return out


def load(sheets: Path) -> list[dict]:
    rows: list[dict] = []
    for p in sorted(sheets.glob("BATCH*.md")):
        rows += parse_sheet(p)
    return rows


def names(agent: str, aliases: list[str]) -> re.Pattern:
    words = [agent, *aliases]
    return re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(w) for w in words if w) + r")(?![\w])", re.I)


def tsv_rows(sheets: Path, agent: str, aliases: list[str]) -> list[dict]:
    path = sheets / "activities_expected_targets.tsv"
    if not path.is_file():
        return []
    want = {w.lower() for w in [agent, *aliases]}
    with path.open(newline="", encoding="utf-8") as fh:
        return [r for r in csv.DictReader(fh, delimiter="\t") if (r.get("agent") or "").lower() in want]


def origin_groups(rows: list[dict]) -> dict:
    """Rows from one document are ONE origin; a (target, value, unit) that appears in two or more documents is flagged as possibly one origin quoted twice."""
    by_doc: dict[str, list[dict]] = defaultdict(list)
    seen: dict[tuple, set] = defaultdict(set)
    for r in rows:
        by_doc[f"{r.get('document')} ({r.get('year')})"].append(r)
        seen[(r.get("target_genes"), r.get("value"), r.get("units"))].add(r.get("document"))
    repeated = [{"target": k[0], "value": k[1], "unit": k[2], "documents": sorted(v)} for k, v in seen.items() if len(v) > 1]
    return {"documents": {d: len(v) for d, v in sorted(by_doc.items())}, "same_value_in_several_documents": repeated}


def query(sheets: Path, agent: str, quantity: str = "all", aliases: list[str] | None = None) -> dict:
    aliases = aliases or []
    rx = names(agent, aliases)
    pattern = re.compile(QUANTITY[quantity], re.I) if quantity in QUANTITY else None
    answer: dict = {"agent": agent, "quantity": quantity, "bullets": [], "comparable": [], "corrections": [], "batch_caveats": [], "structured_rows": [], "origin": {}}
    for b in load(sheets):
        if not rx.search(b["text"]) and not rx.search(b["section"]):
            continue
        sec = b["section"].lower()
        if sec.startswith("comparable"):
            if quantity in ("all", "comparable", "potency", "exposure", "harm", "label"):
                answer["comparable"].append(b)
        elif re.match(r"(second )?dated (line|correction|addition)", sec):
            answer["corrections"].append(b)
        elif quantity == "comparable":
            continue
        elif sec.startswith("what changes") or sec.startswith("what is not found"):
            continue
        elif pattern is None or pattern.search(f"{b['section']} {b['label']} {b['text'][:160]}"):
            answer["bullets"].append(b)
    # Batch-level caveats: a sheet says "none of the five has ..." or "not found for any of the five" without naming each agent, and its absence paragraphs name none. For every sheet that names the
    # agent, those lines are returned apart, labelled as batch-level, so the group caveat is not lost when the question names one agent.
    named_in = {b["file"] for b in load(sheets) if rx.search(b["text"]) or rx.search(b["section"])}
    answer["batch_caveats"] = [b for b in load(sheets) if b["file"] in named_in and not rx.search(b["text"]) and
                               (b["section"].lower().startswith("what is not found") or re.match(r"\*\*(not found|none of|not measured|nothing)", b["text"], re.I))]
    if quantity in ("all", "potency"):
        answer["structured_rows"] = tsv_rows(sheets, agent, aliases)
        answer["origin"] = origin_groups(answer["structured_rows"])
    return answer


def render(a: dict, width: int = 600) -> str:
    out = [f"AGENT {a['agent']}  QUANTITY {a['quantity']}  (derived from the sheets; the sheets are the source: grep -n the file:line)"]
    for title, key in (("SHEET BULLETS", "bullets"), ("COMPARABLE? BULLETS THAT NAME IT", "comparable"), ("DATED CORRECTIONS THAT NAME IT (the original wording above is unchanged)", "corrections"),
                       ("BATCH-LEVEL CAVEATS (the sheet states them for a group or as absences; they may not name the agent)", "batch_caveats")):
        out.append(f"-- {title}: {len(a[key])}")
        for b in a[key]:
            out.append(f"  {b['file']}:{b['line']} [{b['section'][:60]}] {b['text'][:width]}")
    if a["structured_rows"]:
        o = a["origin"]
        out.append(f"-- STRUCTURED CHEMBL ROWS: {len(a['structured_rows'])} in {len(o['documents'])} document(s) (rows on the expected targets by gene symbol only: the sheet states the full count; one document = one origin): " + "; ".join(f"{d}: {n}" for d, n in o["documents"].items()))
        for r in o["same_value_in_several_documents"]:
            out.append(f"  SAME VALUE IN SEVERAL DOCUMENTS (possibly one origin quoted twice): {r['target']} {r['value']} {r['unit']} in {', '.join(r['documents'])}")
    if not (a["bullets"] or a["comparable"] or a["corrections"] or a["structured_rows"] or a["batch_caveats"]):
        out.append("not named in these sheets (not found here is not absence)")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("agent", nargs="?")
    ap.add_argument("--quantity", default="all", choices=["all", "comparable", *QUANTITY])
    ap.add_argument("--alias", action="append", default=[])
    ap.add_argument("--sheets", type=Path, default=DEFAULT_DIR)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args(argv)
    if a.list:
        for p in sorted(a.sheets.glob("BATCH*.md")):
            print(f"{p.name}: {len(parse_sheet(p))} bullets and rows")
        return 0
    if not a.agent:
        ap.error("an agent name is required (or --list)")
    res = query(a.sheets, a.agent, a.quantity, a.alias)
    print(json.dumps(res, indent=1, ensure_ascii=False) if a.json else render(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
