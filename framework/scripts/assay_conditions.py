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

pH and temperature are their own fields, not concentrations: pH is dimensionless and never goes through the nM table. A pH
value keeps its side when the text gives one (`pH_extracellular`, `pH_intracellular`, otherwise `pH`); a step ("pH 7.4 to
7.2", "pHo step") is `pH_step` and a difference ("0.2 pH unit fall") is `pH_delta`, so none of the three agrees with, or
differs from, another. "Room temperature" is read as 18-26 C and says so. A clause that describes another preparation or an
untested transfer ("transfer to a slice at 35 C is untested") and a loading or incubation temperature never become the assay
condition; they are listed under `contrast`. "not stated" and "not applicable" stay apart, and a reference to another
proposition ("As D01") that is missing or circular is named in the reasons, not dropped.

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
    ("cultured_cells", r"\bLUHMES\b|\bmicroglia\b|\bastrocytes?\b|\bNHBE\b|BEAS-?2B|\bA549\b|\bH460\b|\bH1299\b|SH-SY5Y|HaCaT|\bmacrophages?\b|\bcell lines?\b|\bU2OS\b|\bTHP-1\b|\bHUVEC\b"),
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
_NUMPH = r"\d{1,2}(?:[.,]\d+)?"
_PH_STEP = re.compile(rf"\s*(?:step\b\W{{0,8}}|from\s+(?:pH\s*)?)(?P<a>{_NUMPH})\s*(?:to|→|->)\s*(?P<b>{_NUMPH})", re.I)
_PH_SERIES = re.compile(rf"\s*(?:of |=|:|at |\()?\s*(?P<a>{_NUMPH})(?!\d|[.,]\d)(?:\s*(?P<sep>to|-|–)\s*(?P<b>{_NUMPH})(?!\d|[.,]\d)|(?P<more>(?:\s*(?:,|or|and)\s*{_NUMPH}(?!\d|[.,]\d)(?!\s*(?:[pnuµμm]M\b|mV\b|C\b)))+))?")
_PH_NUMBER_NEAR = re.compile(r"(?<![\w.])\d{1,2}(?:[.,]\d+)?(?!\d)(?!\s*(?:[pnuµμm]M\b|mV\b|°?\s*C\b|%|min\b|h\b|s\b))")
_PH_DELTA = re.compile(r"(?P<lo>\d+(?:\.\d+)?)(?:\s*(?:to|-|–)\s*(?P<hi>\d+(?:\.\d+)?))?\s*(?:pH\s*)?units?\b", re.I)
_TEMP = re.compile(rf"(?<![\w.])(?P<lo>{NUM})(?:\s*(?:to|-|–)\s*(?P<hi>{NUM}))?\s*(?:°\s*C|º\s*C|˚\s*C|C)(?![\w+/-])")
_ROOM = re.compile(r"\broom temperature\b|\bambient temperature\b|\bRT\b(?![-/\w])", re.I)   # "RT-qPCR" and "RT/PCR" are assays, not a temperature
ROOM_C = (18.0, 26.0)
_CONTRAST = re.compile(r"\btransfer\b|\buntested\b|\bnot tested\b|\bnot measured\b|\bunlike\b|\bwhereas\b|\bin contrast\b|\bversus\b|\bcompared with\b|\bas opposed to\b", re.I)
_NOT_ASSAY_TEMP = re.compile(r"loading|incubat|slicing|\bsliced\b|storage|stored|recover|housed|housing|rearing|reared|culture medium", re.I)
_SIDE_IN = re.compile(r"pipette|internal|intracellular|cytosol|patch solution", re.I)
_SIDE_EX = re.compile(r"extracellular|external|\bbath|aCSF|recording solution|perfus|medium|buffer|bicarbonate|Ringer", re.I)
_NS = r"(?:not (?:stated|named|reported|given|read|measured)|unread|unknown|not in (?:the |any )?(?:abstract|text|file))"
PH_FIELDS = ("pH", "pH_extracellular", "pH_intracellular")
LABEL_FIELDS = ("system", "scaffold", "composition", "readout_class", "nrf2_loss_arm", "nrf2_loss_verified", "cell")   # values are labels, compared as sets
NON_CONC = LABEL_FIELDS + ("holding_potential_mV", "temperature_C", "pH_step", "pH_delta") + PH_FIELDS
_FREE = re.compile(r"\b(Mg|Ca|Zn)(?:2\+)?(?:/(Mg|Ca|Zn)(?:2\+)?)?[- ]free\b", re.I)


def _f(text: str) -> float:
    t = text.replace("−", "-").replace("–", "-")
    if re.fullmatch(r"[-+]?\d{1,3}(,\d{3})+", t):
        t = t.replace(",", "")
    return float(t.replace(",", "."))


def _interval(lo: float, hi: float | None) -> tuple[float, float]:
    return (lo, lo) if hi is None else (min(lo, hi), max(lo, hi))


def _clauses(s: str):
    """(start, end) of the clauses of a cell: split on ';' and on a full stop that is not a decimal point."""
    start = 0
    for m in re.finditer(r";|(?<!\d)\.(?=\s|$)", s):
        yield start, m.start()
        start = m.end()
    yield start, len(s)


def _side(clause: str, at: int, token: str | None) -> str | None:
    """'extracellular' | 'intracellular' | None for the pH written at `at` in `clause`: its own suffix (pHo, pHi) first, otherwise the nearest side word."""
    if token:
        return "extracellular" if token == "o" else "intracellular"
    best = None
    for side, rx in (("intracellular", _SIDE_IN), ("extracellular", _SIDE_EX)):
        for m in rx.finditer(clause):
            d = min(abs(m.start() - at), abs(m.end() - at))
            if d <= 45 and (best is None or d < best[0]):
                best = (d, side)
    return best[1] if best else None


def _add(fields: dict, name: str, value, text: str) -> None:
    v = fields.setdefault(name, {"state": "STATED", "values": [], "text": []})
    if v["state"] != "STATED":
        return
    if value not in v["values"]:
        v["values"].append(value)
        v["text"].append(text)


def _read_ph_temperature(s: str, fields: dict, unplaced: list, contrast: list) -> None:
    """pH (side, absolute values, step, difference) and assay temperature, clause by clause."""
    for a, b in _clauses(s):
        clause = s[a:b]
        has_ph = re.search(r"\bpH", clause)
        temps = list(_TEMP.finditer(clause))
        room = _ROOM.search(clause)
        if _CONTRAST.search(clause):
            if (has_ph and re.search(r"\bpH[io]?\b\W{0,3}" + _NUMPH, clause)) or temps or room:
                contrast.append(clause.strip())
            continue
        for m in re.finditer(r"\bpH([io])?\b", clause):
            after = clause[m.end():m.end() + 70]
            st = _PH_STEP.match(after)
            if st:
                _add(fields, "pH_step", (_f(st.group("a")), _f(st.group("b"))), f"pH{m.group(1) or ''} {after.strip()[:st.end()].strip()}")
                continue
            sv = _PH_SERIES.match(after)
            if not sv:
                if _PH_NUMBER_NEAR.search(after[:30]):
                    unplaced.append(f"pH{m.group(1) or ''} {after.strip()[:40]} (pH wording not recognised: not read as a value, a step or a series)")
                continue
            lo = _f(sv.group("a"))
            name = {"extracellular": "pH_extracellular", "intracellular": "pH_intracellular"}.get(_side(clause, m.start(), m.group(1)), "pH")
            quote = f"pH{m.group(1) or ''} {after[:sv.end()].strip()}"
            if sv.group("sep"):
                hi = _f(sv.group("b"))
                if hi < lo:
                    unplaced.append(f"{quote} (a range or a step: not stated)")
                    continue
                vals = [(lo, hi)]
            else:
                vals = [(lo, lo)] + [(_f(x), _f(x)) for x in re.findall(_NUMPH, sv.group("more") or "")]
            if any(v[1] > 14 or v[0] < 0 for v in vals):
                unplaced.append(quote)
                continue
            for v in vals:
                _add(fields, name, v, quote)
        if has_ph or re.search(r"acid|alkal", clause, re.I):
            for m in _PH_DELTA.finditer(clause):
                lo = float(m.group("lo")); hi = float(m.group("hi")) if m.group("hi") else lo
                _add(fields, "pH_delta", (min(lo, hi), max(lo, hi)), m.group(0))
        for m in temps:
            if _NOT_ASSAY_TEMP.search(clause[max(0, m.start() - 25):m.end() + 25]):
                unplaced.append(f"{m.group(0)} (not an assay temperature)")
                continue
            lo, hi = _interval(_f(m.group("lo")), _f(m.group("hi")) if m.group("hi") else None)
            if -5 <= lo and hi <= 100:
                _add(fields, "temperature_C", (lo, hi), m.group(0))
        if room and not temps:
            _add(fields, "temperature_C", ROOM_C, f"{room.group(0)} (read as {ROOM_C[0]:g}-{ROOM_C[1]:g} C)")
            if fields.get("temperature_C", {}).get("state") == "STATED" and ROOM_C in fields["temperature_C"]["values"]:
                fields["temperature_C"]["convention"] = [ROOM_C]      # an interval the reader supplied, not one the source gave
    for name, key in (("pH", r"\bpH\b"), ("temperature_C", r"\btemperature\b")):
        if name in fields or (name == "pH" and any(f in fields for f in PH_FIELDS)):
            continue
        if re.search(key + r"[^;.)]{0," + ("30" if name == "pH" else "70") + r"}?" + _NS, s, re.I) or (name == "pH" and re.search(r"\bno\b[^;.]{0,40}\bpH\b[^;.]{0,10}\bstated", s, re.I)):
            fields[name] = {"state": "NOT_STATED", "values": [], "text": []}
        elif re.search(key + r"[^;.)]{0,25}?not applicable", s, re.I):
            fields[name] = {"state": "NOT_APPLICABLE", "values": [], "text": []}


_KEY = re.compile(r"(?:^|;\s+)([a-z][a-z ]*?)=")
READOUTS = (   # ordered; a readout cell can name several classes ("mRNA and enzyme activity")
    ("binding", r"\bbinding\b|\bKd\b|\bITC\b|\bSPR\b|\bfluorescence polarization\b|\bFP\b"),
    ("translocation", r"translocation|nuclear (?:NRF2|Nrf2)"),
    ("reporter", r"reporter|\bARE\b|luciferase"),
    ("enzyme_activity", r"enzyme activity|NQO1 activity|activity \(NQO1\)"),
    ("mRNA", r"mRNA|RT-?PCR|qPCR|microarray"),
    ("protein", r"western|immunoblot|(?<!nuclear )(?<!nuclear NRF2 )\bprotein level|\bHO-1 protein"),
    ("viability", r"viability|CCK-8|\bMTT\b|calcein|TUNEL|apoptosis|cell death|cytotox|GSH depletion"),
    ("function", r"clinical score|histolog|neurite|morphology|behaviou?r|survival score"),
)
LOSS_ARMS = (("siRNA", r"\bsiRNA\b"), ("shRNA", r"\bshRNA\b"), ("knockout", r"knock-?out|\bKO\b|CRISPR|germline [A-Za-z0-9]+ deficiency|\bdeficien"), ("dominant_negative", r"dominant[- ]negative"), ("inhibitor", r"pharmacological|\binhibitor\b"))


def _read_structured(s: str, fields: dict, unplaced: list) -> None:
    """Cells written as `key=value; key=value` (the SCI46 decisive tables): the readout class, the loss arm and whether the loss was verified, and the cell type."""
    keys = list(_KEY.finditer(s))
    if len(keys) < 2:
        return
    parts = {}
    for i, m in enumerate(keys):
        end = keys[i + 1].start() if i + 1 < len(keys) else len(s)
        parts[m.group(1).strip()] = s[m.end():end].strip().rstrip(";")
    if "readout" in parts and not _NOT_STATED.search(parts["readout"]):
        found = [name for name, pat in READOUTS if re.search(pat, parts["readout"], re.I)]
        if found:
            fields["readout_class"] = {"state": "STATED", "values": found, "text": [parts["readout"]]}
        else:
            unplaced.append(f"readout {parts['readout'][:60]!r} names no readout class")
    kd = parts.get("knockdown")
    if kd is not None:
        if re.fullmatch(r"n/a|na|", kd.strip(), re.I):
            fields["nrf2_loss_arm"] = {"state": "NOT_APPLICABLE", "values": [], "text": []}
        else:
            arms = [name for name, pat in LOSS_ARMS if re.search(pat, kd, re.I)]
            if not arms and re.match(r"none\b", kd.strip(), re.I):
                arms = ["none"]
            if arms:
                fields["nrf2_loss_arm"] = {"state": "STATED", "values": arms, "text": [kd]}
                if arms != ["none"]:
                    efficiency = re.search(r"about \d+(?:\.\d+)?|over \d+ ?%|\d+ ?% knockdown", kd, re.I)
                    if re.search(r"incomplete|inadequate|insufficient|partial", kd, re.I):
                        v = "no"
                    elif re.search(r"unverified|not stated|unstated|verification not", kd, re.I):
                        v = "unstated"
                    elif efficiency or re.search(r"(?<!un)verified", kd, re.I):
                        v = "yes"
                    else:
                        v = "unstated"
                    fields["nrf2_loss_verified"] = {"state": "STATED", "values": [v], "text": [kd]}
            else:
                unplaced.append(f"knockdown {kd[:60]!r} names no loss arm")
    cell = parts.get("cell")
    if cell and not re.fullmatch(r"n/a|na|whole animal", cell.strip(), re.I):
        names = sorted({c.strip().lower() for c in re.split(r",|/|\band\b|\bor\b|;", cell) if c.strip() and c.strip().lower() not in ("others", "n/a")})
        if names:
            fields["cell"] = {"state": "STATED", "values": names, "text": [cell]}


_INHERIT = re.compile(r"^\s*As (D\d+)\b|[Cc]onditions as (D\d+)\b")


def parse(text: str, cells: dict[str, str] | None = None, _seen: tuple = ()) -> dict:
    """Fields read from one cell. `cells` (prop_id -> cell text) resolves "As D01; glycine 3 uM": the referenced reading is the base, the system stays the base's, and what the cell states itself overrides. Each field: {'state': 'STATED'|'NOT_STATED', 'values': [...], 'text': [...]} (system and scaffold carry labels)."""
    s = (text or "").replace("µ", "u").replace("μ", "u")
    fields: dict[str, dict] = {}
    placed: list[tuple[int, int]] = []
    contrast: list[str] = []

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
    _read_ph_temperature(s, fields, unplaced, contrast)
    _read_structured(s, fields, unplaced)
    ref = _INHERIT.search(text or "")
    inherited, ref_state = "", "NONE"
    if ref and cells is not None:
        target = ref.group(1) or ref.group(2)
        if target in _seen:
            ref_state, unplaced = "CIRCULAR", unplaced + [f"reference {target} is circular"]
        elif target not in cells:
            ref_state, unplaced = "MISSING", unplaced + [f"reference {target} not found among the propositions of this package"]
        else:
            inherited, ref_state = target, "RESOLVED"
            base_read = parse(cells[target], cells, _seen + (target,))
            base = base_read["fields"]
            if base_read["inherit_state"] in ("MISSING", "CIRCULAR"):
                ref_state = base_read["inherit_state"]
                unplaced = unplaced + [f"reference {target} itself has an unresolved reference ({ref_state.lower()})"]
            own = {k: v for k, v in fields.items() if k not in ("system", "scaffold")}
            if any(k in own for k in ("pH", "pH_extracellular")):      # a pH the cell states itself replaces the inherited bath pH, whatever the side wording
                base = {k: v for k, v in base.items() if k not in ("pH", "pH_extracellular")}
            fields = {**base, **own}
    return {"source_text": text or "", "fields": fields, "unplaced": unplaced, "inherits": inherited, "inherit_state": ref_state, "contrast": contrast}


def _fmt(field: str, values) -> str:
    if field in LABEL_FIELDS:
        return "/".join(values)
    out = []
    for v in values:
        if v == "none":
            out.append("none")
            continue
        lo, hi = v
        if field == "pH_step":
            out.append(f"pH {lo:g} to {hi:g}")
            continue
        unit = {"holding_potential_mV": "mV", "temperature_C": "C", "pH_delta": "pH units"}.get(field, "" if field in PH_FIELDS else "nM")
        out.append((f"{lo:g}" if lo == hi else f"{lo:g} to {hi:g}") + (f" {unit}" if unit else ""))
    return "; ".join(out)


def _show(field: str, f: dict) -> str:
    """The original wording when the field has one (it is the provenance), the normalised value otherwise."""
    return "; ".join(f["text"]) if f["text"] and field not in LABEL_FIELDS else _fmt(field, f["values"])


def _same(field: str, a: list, b: list) -> str:
    """'equal' | 'disjoint' | 'overlap' for two lists of values of one field."""
    if field == "pH_step":
        return "equal" if set(a) == set(b) else "disjoint"
    if field in LABEL_FIELDS or "none" in a or "none" in b:
        sa, sb = set(a), set(b)
        if sa == sb:
            return "equal"
        if field == "cell":          # cell-type wording varies ("LUHMES differentiated", "differentiated neuron-like"): different words are not a documented difference
            return "overlap"
        return "disjoint" if not sa & sb else "overlap"
    def eq(x, y): return abs(x - y) <= 1e-9 * max(1.0, abs(x), abs(y))
    if len(a) == len(b) and all(eq(x[0], y[0]) and eq(x[1], y[1]) for x, y in zip(sorted(a), sorted(b))):
        return "equal"
    touch = any(x[0] <= y[1] + 1e-9 and y[0] <= x[1] + 1e-9 for x in a for y in b)
    return "overlap" if touch else "disjoint"


def compare(a: dict, b: dict) -> dict:
    """a, b: parse() results (or strings). Returns the state, with what agreed, what differs, what is stated on one side only."""
    a = parse(a) if isinstance(a, str) else a
    b = parse(b) if isinstance(b, str) else b
    fa, fb = dict(a["fields"]), dict(b["fields"])
    agreed, differ, one_sided, partial, notes = [], [], [], [], []
    for x, y in ((fa, fb), (fb, fa)):     # a pH with no side on one side meets the extracellular pH of the other: same bath, side not documented
        if "pH" in x and "pH_extracellular" in y and "pH_extracellular" not in x and "pH" not in y:
            x["pH_extracellular"] = {**x.pop("pH"), "side_not_stated": True}

    for field in sorted(set(fa) | set(fb)):
        x, y = fa.get(field), fb.get(field)
        sx, sy = bool(x and x["state"] == "STATED"), bool(y and y["state"] == "STATED")
        if sx and sy:
            rel = _same(field, x["values"], y["values"])
            if rel == "equal":
                agreed.append(field)
                if x.get("side_not_stated") or y.get("side_not_stated"):
                    notes.append(f"{field}: side stated on one side only")
            elif rel == "disjoint" and (x.get("side_not_stated") or y.get("side_not_stated")):
                partial.append({"field": field, "a": _show(field, x), "b": _show(field, y), "why": "differ, and the side (bath or pipette) is not stated on one side"})
            elif rel == "disjoint" and not (x.get("open") or y.get("open")):
                note = ""
                if field not in NON_CONC and x["values"] != ["none"] and y["values"] != ["none"]:
                    px, py = x["values"][0][0], y["values"][0][0]
                    if px and py and any(abs(px / py - r) <= 0.05 * r or abs(py / px - r) <= 0.05 * r for r in (1e3, 1e6)):
                        note = " (ratio is a power of 1000: read both originals for a unit slip)"
                differ.append({"field": field, "a": _show(field, x), "b": _show(field, y) + note, **({"by_convention": True} if x.get("convention") or y.get("convention") else {})})
            else:
                partial.append({"field": field, "a": _show(field, x), "b": _show(field, y), **({"by_convention": True} if x.get("convention") or y.get("convention") else {})})
        elif sx or sy:
            side, f = ("a", x) if sx else ("b", y)
            other = x if sy else y
            declared = ("declared " + other["state"].lower().replace("_", " ") + " on the other side") if other else "absent on the other side"
            one_sided.append({"field": field, "stated_in": side, "value": _show(field, f), "other": declared})
    system_known = "system" in agreed
    unresolved = [f"reference to another proposition unresolved ({r.lower()})" for r in {a.get("inherit_state"), b.get("inherit_state")} if r in ("MISSING", "CIRCULAR")]
    if differ:
        state = INCOMPATIBILITY
    elif not system_known or partial or one_sided or unresolved or not [f for f in agreed if f != "system"]:
        state = INSUFFICIENT
    else:
        state = AGREEMENT
    reasons = [f"{d['field']}: {d['a']} / {d['b']}" for d in differ]
    reasons += [f"{p['field']}: {p.get('why', 'values overlap without being equal')} ({p['a']} / {p['b']})" for p in partial]
    reasons += [f"{o['field']} stated only in {o['stated_in']} ({o['value']})" for o in one_sided]
    reasons += unresolved
    if not system_known:
        reasons.append("system not recognised or not the same on both sides")
    elif not [f for f in agreed if f != "system"]:
        reasons.append("no condition shared beyond the system")
    return {"state": state, "agreed": agreed, "differ": differ, "partial": partial, "one_sided": one_sided, "notes": notes,
            "reasons": reasons, "unplaced": a["unplaced"] + b["unplaced"], "contrast": a.get("contrast", []) + b.get("contrast", [])}


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
