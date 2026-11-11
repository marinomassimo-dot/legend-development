#!/usr/bin/env python3
"""Assay conditions read from a free-text cell, and whether two sets of conditions agree — three answers, never two.

A comparison of two potency statements needs to know whether they were measured under conditions that can be set side by
side. The conditions of the packages live only in free text (`species_system_age_prep_exposure_readout`): there is no
structured conditions column. This module reads the few fields that decisions actually use, keeps the original text as the
provenance, and compares two readings:

  DOCUMENTED_AGREEMENT      every field stated on either side is stated on both and equal, the system is known on both,
                            and at least one parameter beyond the system is shared
  DOCUMENTED_INCOMPATIBILITY  a field stated on both sides differs (1 mM against 1 uM; core-free against core-bound)
  INSUFFICIENT              anything else: a field stated on one side only, a system not recognised, overlapping ranges,
                            nothing shared beyond the system. This is a premise to name, not a block.

A field that is not stated stays not stated: it never agrees with a stated value and never differs from one. An
unrecognised system is not a category: two unrecognised systems are not "the same".

Concentrations are converted with the unit table of measurement.py (mM, uM, µM, μM, nM...) and kept with their original
text. Ranges (`50-100 uM`, `-70 to +20 mV`) are intervals; two intervals agree only when equal, differ when disjoint, and are
INSUFFICIENT when they overlap without being equal. Fields are read from the cases present in the packages; this is not a
universal parser, and text it cannot place is listed under `unplaced` instead of being guessed.

  python3 framework/scripts/assay_conditions.py parse "Rat GluN1/GluN2B in oocytes, -40 mV, 100 uM glutamate plus 50 uM glycine"
  python3 framework/scripts/assay_conditions.py compare "oocytes, 1 mM ATP" "oocytes, 1000 uM ATP"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import measurement as ms  # noqa: E402

AGREEMENT, INCOMPATIBILITY, INSUFFICIENT = "DOCUMENTED_AGREEMENT", "DOCUMENTED_INCOMPATIBILITY", "INSUFFICIENT"

SYSTEMS = (  # ordered: the first pattern that matches names the system; a cell can name several (a contrast)
    ("oocyte", r"oocyte"),
    ("HEK", r"\bHEK"),
    ("slice", r"\bslices?\b"),
    ("neurons", r"(?<!no )\bneurons?\b|primary culture|cultured|\bDIV\b"),
    ("purified_protein", r"purified|crystal|cryo-EM|DELFIA|radiolabel|(?:kinase|enzyme|activity|coupled) assay|in vitro enzyme|circular dichroism|recombinant (?:human |rat |mouse )?(?:SUMO-)?PDK\d|recombinant [\w-]+ (?:kinase|enzyme)"),
)
SOLUTES = (  # canonical name, pattern of how it is written
    ("glycine", r"glycine|\bGly\b"),
    ("glutamate", r"glutamate|\bGlu\b"),
    ("NMDA", r"\bNMDA\b"),
    ("ATP", r"\bATP\b"),
    ("Mg", r"\bMg(?:Cl2)?(?:2\+)?"),
    ("Ca", r"\bCa(?:Cl2)?(?:2\+)?"),
    ("Zn", r"\bZn(?:2\+)?"),
    ("EDTA", r"\bEDTA\b"),
)
NUM = r"[-+−–]?\d+(?:[.,]\d+)?"
UNIT = r"[pnuµμm]?M"
_CONC = re.compile(rf"(?P<lo>{NUM})(?:\s*(?:to|-|–)\s*(?P<hi>{NUM}))?\s*(?P<unit>{UNIT})(?![A-Za-z])")
_MV = re.compile(rf"(?P<lo>{NUM})(?:\s*(?:to|–)\s*(?P<hi>[-+−]?\d+))?\s*mV\b")
_NOT_STATED = re.compile(r"not (?:stated|named|reported|given|read)|unread|unknown", re.I)
_OPEN_POTENTIALS = re.compile(r"other potentials|various potentials", re.I)
_SUBUNIT = re.compile(r"\b(?:GluN2[A-D]|NR2[A-D]|GluN3[AB]|GluA[1-4]|GluR[1-4]|GluK[1-5])\b")
_STOP = {"and", "plus", "with", "for", "at", "in", "from", "each", "or", "then"}
_FREE = re.compile(r"\b(Mg|Ca|Zn)(?:2\+)?(?:/(Mg|Ca|Zn)(?:2\+)?)?[- ]free\b", re.I)


def _f(text: str) -> float:
    t = text.replace("−", "-").replace("–", "-")
    if re.fullmatch(r"[-+]?\d{1,3}(,\d{3})+", t):
        t = t.replace(",", "")
    return float(t.replace(",", "."))


def _interval(lo: float, hi: float | None) -> tuple[float, float]:
    return (lo, lo) if hi is None else (min(lo, hi), max(lo, hi))


_INHERIT = re.compile(r"^\s*As (D\d+)\b|[Cc]onditions as (D\d+)\b")


def parse(text: str, cells: dict[str, str] | None = None, _seen: tuple = ()) -> dict:
    """Fields read from one cell. `cells` (prop_id -> cell text) resolves "As D01; glycine 3 uM": the referenced reading is the base, the system stays the base's, and what the cell states itself overrides. Each field: {'state': 'STATED'|'NOT_STATED', 'values': [...], 'text': [...]} (system and scaffold carry labels)."""
    s = (text or "").replace("µ", "u").replace("μ", "u")
    fields: dict[str, dict] = {}
    placed: list[tuple[int, int]] = []

    labels = [name for name, pat in SYSTEMS if re.search(pat, s, re.I)]
    if labels:
        fields["system"] = {"state": "STATED", "values": labels, "text": labels}

    subunits = sorted(set(re.sub(r"^NR2", "GluN2", m.group(0)).replace("GluR", "GluA") for m in _SUBUNIT.finditer(s)))
    if subunits:
        fields["composition"] = {"state": "STATED", "values": subunits, "text": []}
    if re.search(r"triheteromer", s, re.I):
        fields.setdefault("composition", {"state": "STATED", "values": [], "text": []})["values"].append("triheteromer")

    free = bool(re.search(r"core[- ]free|without (?:the )?(?:E2|E3BP)|E1-only", s, re.I))
    bound = bool(re.search(r"core[- ]bound|(?:with|on) (?:the )?(?:E2|E3BP)", s, re.I))
    if free or bound:
        fields["scaffold"] = {"state": "STATED", "values": (["core_free"] if free else []) + (["core_bound"] if bound else []), "text": []}

    for m in _MV.finditer(s):
        lo, hi = _interval(_f(m.group("lo")), _f(m.group("hi")) if m.group("hi") else None)
        v = fields.setdefault("holding_potential_mV", {"state": "STATED", "values": [], "text": []})
        if (lo, hi) not in v["values"]:
            v["values"].append((lo, hi))
            v["text"].append(m.group(0))
        placed.append(m.span())
    if "holding_potential_mV" in fields and _OPEN_POTENTIALS.search(s):
        fields["holding_potential_mV"]["open"] = True
    if re.search(r"no voltage clamp|no holding potential", s, re.I) and "holding_potential_mV" not in fields:
        fields["holding_potential_mV"] = {"state": "STATED", "values": ["none"], "text": ["no voltage clamp"]}

    # concentrations: a token belongs to the solute written right after it ("5 uM ATP") or right before it ("glycine 10 uM")
    solute_spans = [(name, m.start(), m.end()) for name, pat in SOLUTES for m in re.finditer(pat, s)]
    unplaced: list[str] = []
    for m in _CONC.finditer(s):
        if any(a <= m.start() < b for a, b in placed):
            continue
        after = [x for x in solute_spans if 0 <= x[1] - m.end() <= 3 or (x[1] >= m.end() and not s[m.end():x[1]].strip(" of"))]
        following = re.match(r"\s*([A-Za-z][\w+]*)", s[m.end():])
        other_noun = bool(following) and following.group(1).lower() not in _STOP and not any(x[1] == m.end() + following.start(1) for x in solute_spans)
        before = [x for x in solute_spans if 0 <= m.start() - x[2] <= 4 and re.fullmatch(r"[\s(:=]*(?:at )?", s[x[2]:m.start()]) and not other_noun]
        nxt_solute_close = [x for x in after if x[1] - m.end() <= 3]
        if nxt_solute_close and before:
            unplaced.append(m.group(0) + " (between two solutes)")
            continue
        pick = nxt_solute_close or before
        if not pick:
            continue  # a drug or other concentration that is not an assay condition
        name = pick[0][0]
        factor = ms.TO_NM.get(m.group("unit"))
        if factor is None:
            unplaced.append(m.group(0))
            continue
        lo, hi = _interval(_f(m.group("lo")) * factor, _f(m.group("hi")) * factor if m.group("hi") else None)
        v = fields.setdefault(name, {"state": "STATED", "values": [], "text": []})
        if (lo, hi) not in v["values"]:
            v["values"].append((lo, hi))
            v["text"].append(f"{m.group(0)} {name}")
    for m in _FREE.finditer(s):
        for name in filter(None, (m.group(1), m.group(2))):
            fields.setdefault(name.capitalize(), {"state": "STATED", "values": [(0.0, 0.0)], "text": [m.group(0)]})

    # a clause that says a condition is not stated keeps it explicitly unknown
    for clause in re.split(r"[;.]", s):
        if _NOT_STATED.search(clause):
            for name, pat in SOLUTES:
                if name not in fields and re.search(pat, clause):
                    fields[name] = {"state": "NOT_STATED", "values": [], "text": []}
            if "holding_potential_mV" not in fields and re.search(r"holding potential", clause, re.I):
                fields["holding_potential_mV"] = {"state": "NOT_STATED", "values": [], "text": []}
    ref = _INHERIT.search(text or "")
    inherited = ""
    if ref and cells is not None:
        inherited = ref.group(1) or ref.group(2)
        if inherited in cells and inherited not in _seen:
            base = parse(cells[inherited], cells, _seen + (inherited,))["fields"]
            own = {k: v for k, v in fields.items() if k not in ("system", "scaffold")}
            fields = {**base, **own}
        else:
            inherited = ""   # reference not resolvable here: the cell keeps only what it states
    return {"source_text": text or "", "fields": fields, "unplaced": unplaced, "inherits": inherited}


def _fmt(field: str, values) -> str:
    if field in ("system", "scaffold", "composition"):
        return "/".join(values)
    out = []
    for v in values:
        if v == "none":
            out.append("none")
            continue
        lo, hi = v
        unit = "mV" if field == "holding_potential_mV" else "nM"
        out.append(f"{lo:g} {unit}" if lo == hi else f"{lo:g} to {hi:g} {unit}")
    return "; ".join(out)


def _show(field: str, f: dict) -> str:
    """The original wording when the field has one (it is the provenance), the normalised value otherwise."""
    return "; ".join(f["text"]) if f["text"] and field not in ("system", "scaffold", "composition") else _fmt(field, f["values"])


def _same(field: str, a: list, b: list) -> str:
    """'equal' | 'disjoint' | 'overlap' for two lists of values of one field."""
    if field in ("system", "scaffold", "composition") or "none" in a or "none" in b:
        sa, sb = set(a), set(b)
        return "equal" if sa == sb else "disjoint" if not sa & sb else "overlap"
    def eq(x, y): return abs(x - y) <= 1e-9 * max(1.0, abs(x), abs(y))
    if len(a) == len(b) and all(eq(x[0], y[0]) and eq(x[1], y[1]) for x, y in zip(sorted(a), sorted(b))):
        return "equal"
    touch = any(x[0] <= y[1] + 1e-9 and y[0] <= x[1] + 1e-9 for x in a for y in b)
    return "overlap" if touch else "disjoint"


def compare(a: dict, b: dict) -> dict:
    """a, b: parse() results (or strings). Returns the state, with what agreed, what differs, what is stated on one side only."""
    a = parse(a) if isinstance(a, str) else a
    b = parse(b) if isinstance(b, str) else b
    fa, fb = a["fields"], b["fields"]
    agreed, differ, one_sided, partial = [], [], [], []
    for field in sorted(set(fa) | set(fb)):
        x, y = fa.get(field), fb.get(field)
        sx, sy = bool(x and x["state"] == "STATED"), bool(y and y["state"] == "STATED")
        if sx and sy:
            rel = _same(field, x["values"], y["values"])
            if rel == "equal":
                agreed.append(field)
            elif rel == "disjoint" and not (x.get("open") or y.get("open")):
                note = ""
                if field not in ("system", "scaffold", "composition") and x["values"] != ["none"] and y["values"] != ["none"]:
                    px, py = x["values"][0][0], y["values"][0][0]
                    if px and py and any(abs(px / py - r) <= 0.05 * r or abs(py / px - r) <= 0.05 * r for r in (1e3, 1e6)):
                        note = " (ratio is a power of 1000: read both originals for a unit slip)"
                differ.append({"field": field, "a": _show(field, x), "b": _show(field, y) + note})
            else:
                partial.append({"field": field, "a": _show(field, x), "b": _show(field, y)})
        elif sx or sy:
            side, f = ("a", x) if sx else ("b", y)
            declared = "declared not stated on the other side" if (x if sy else y) else "absent on the other side"
            one_sided.append({"field": field, "stated_in": side, "value": _show(field, f), "other": declared})
    system_known = "system" in agreed
    if differ:
        state = INCOMPATIBILITY
    elif not system_known or partial or one_sided or not [f for f in agreed if f != "system"]:
        state = INSUFFICIENT
    else:
        state = AGREEMENT
    reasons = [f"{d['field']}: {d['a']} / {d['b']}" for d in differ]
    reasons += [f"{p['field']}: values overlap without being equal ({p['a']} / {p['b']})" for p in partial]
    reasons += [f"{o['field']} stated only in {o['stated_in']} ({o['value']})" for o in one_sided]
    if not system_known:
        reasons.append("system not recognised or not the same on both sides")
    elif not [f for f in agreed if f != "system"]:
        reasons.append("no condition shared beyond the system")
    return {"state": state, "agreed": agreed, "differ": differ, "partial": partial, "one_sided": one_sided,
            "reasons": reasons, "unplaced": a["unplaced"] + b["unplaced"]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("parse")
    p.add_argument("text")
    c = sub.add_parser("compare")
    c.add_argument("a")
    c.add_argument("b")
    args = ap.parse_args(argv)
    print(json.dumps(parse(args.text) if args.cmd == "parse" else compare(args.a, args.b), indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
