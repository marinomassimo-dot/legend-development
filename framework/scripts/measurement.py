#!/usr/bin/env python3
"""A potency or affinity value, kept as it was reported, converted openly, and compared only when it can be.

WHY THIS EXISTS (2026-11-10, HE43)
----------------------------------
A registry row filed under a target can be wrong by unit as well as by subunit. In the GtoPdb snapshot the DQP-1105 rows for
GluN2B and GluN2C carry micromolar IC50 values from the primary paper as 113 and 7 in the nanomolar column. The existing search
path reduced each registry row to one string ("6.95 pIC50 (=)"): the original type, the nanomolar column, the range and the
relation were gone, so nothing downstream could notice a disagreement, and "113 nM" looked like any other number.
Measured on the snapshot in the catalogue cache: of 24,968 rows, 13,737 carry a pIC50-type value and a nanomolar value that
agree, and 7 of the others disagree by exactly 1000 (Cs+ on HCN1, HCN2 and HCN4, decavanadate on TRPM4, DkTx on TRPV1 and two
farnesyl diphosphate synthase rows): the same class of slip, found without opening a paper. DQP-1105 itself is NOT found by that
check, because its pIC50 and nanomolar columns agree with each other; only the primary table shows the slip. Both checks are
here, and the second one needs a second measurement row.

What a measurement keeps: the kind (IC50, EC50, Ki, Kd, KB or a p-form), the original value, unit and relation (=, <, >, ~, or a
low-high range), the transformation applied, the converted nanomolar value (labelled `converted_nM`: a conversion is not new
evidence), target, species, system, the conditions that decide comparability, and the source. A missing piece is a statement in
`flags`, never a silent default and never a reason to drop the row.

  python3 framework/scripts/measurement.py scan-gtopdb      # rows whose pIC50-type and nanomolar columns disagree (pinned cache)
  python3 framework/scripts/measurement.py convert 6.95 pIC50
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

KINDS = ("IC50", "EC50", "Ki", "Kd", "KB", "pA2")
TO_NM = {"M": 1e9, "mM": 1e6, "uM": 1e3, "µM": 1e3, "μM": 1e3, "nM": 1.0, "pM": 1e-3, "fM": 1e-6}
RELATIONS = ("=", "<", ">", "<=", ">=", "~")
SCALE_TOL = 0.05  # a ratio within 5% of a power of 1000 reads as a unit slip, not a real difference


def _num(x):
    if x in (None, "", "-"):
        return None
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def measure(kind: str, value=None, unit: str | None = None, relation: str = "=", *, low=None, high=None,
            target: str = "", species: str = "", system: str = "", conditions: str = "", source: str = "") -> dict:
    """One reported measurement. `kind` is IC50/EC50/Ki/Kd/KB or its p-form (pIC50...); `unit` is a concentration unit, or None for a p-form."""
    flags: list[str] = []
    is_log = kind.startswith("p") and kind[1:] in KINDS
    base = kind[1:] if is_log else kind
    if base not in KINDS:
        flags.append("KIND_UNRECOGNISED")
    if relation not in RELATIONS:
        flags.append("RELATION_UNRECOGNISED")
    v, lo, hi = _num(value), _num(low), _num(high)
    converted, transform = None, None
    if v is None and lo is None and hi is None:
        flags.append("VALUE_MISSING")
    elif is_log:
        if v is not None:
            converted, transform = 10 ** (9 - v), "nM = 10^(9 - p)"
    elif unit is None or unit == "":
        flags.append("UNIT_MISSING")
    elif unit not in TO_NM:
        flags.append("UNIT_UNRECOGNISED")
    elif v is not None:
        converted, transform = v * TO_NM[unit], f"nM = value x {TO_NM[unit]:g} ({unit})"
    if relation in ("<", ">", "<=", ">="):
        flags.append("CENSORED")      # `converted_nM` is a bound, not a value
    if relation == "~":
        flags.append("APPROXIMATE")
    if lo is not None or hi is not None:
        flags.append("RANGE")
    return {"kind": base, "is_log": is_log, "original": {"value": value, "unit": unit if not is_log else "p-scale", "relation": relation, "low": low, "high": high},
            "transform": transform, "converted_nM": converted, "target": target, "species": species, "system": system, "conditions": conditions,
            "source": source, "flags": flags}


def compare(a: dict, b: dict) -> dict:
    """Are two measurements comparable, and if both are plain values do they differ by a scale that is a unit slip? Never decides which is right."""
    reasons, unknown = [], []
    if a["kind"] != b["kind"]:
        reasons.append(f"different quantity: {a['kind']} vs {b['kind']}")
    for field in ("target", "species", "system", "conditions"):
        x, y = (a[field] or "").strip().lower(), (b[field] or "").strip().lower()
        if x and y and x != y:
            reasons.append(f"{field} differs: {a[field]!r} vs {b[field]!r}")
        elif not x or not y:
            unknown.append(field)
    na, nb = a["converted_nM"], b["converted_nM"]
    plain = na is not None and nb is not None and not ({"CENSORED", "APPROXIMATE", "RANGE"} & (set(a["flags"]) | set(b["flags"])))
    ratio = (nb / na) if plain and na else None
    slip = False
    if ratio and ratio > 0:
        k = math.log10(ratio) / 3
        slip = abs(k) >= 0.9 and abs(k - round(k)) * 3 <= math.log10(1 + SCALE_TOL) and round(k) != 0
    if na is None or nb is None:
        unknown.append("converted value (unit or value missing)")
    elif not plain:
        unknown.append("censored, approximate or range value: bounds only")
    verdict = "NO" if reasons else "UNKNOWN" if unknown else "YES"
    return {"comparable": verdict, "not_equivalent": reasons, "unstated": unknown, "ratio_b_over_a": ratio,
            "unit_conflict_suspect": slip,
            "note": "UNIT_CONFLICT_SUSPECT means open the source; it does not say which value is right" if slip else
                    "a conversion to nM makes values commensurable in scale only, not the same measurement"}


def summarise(measures: list[dict]) -> list[dict]:
    """Descriptive range of many measurements of one molecule, per comparable group — never one minimum across groups.

    A group is (kind, target, species, system): an IC50 and a Ki, two targets, two species or a binding and a functional assay are different groups, and the lowest
    value of the union is not a potency. Inside a group the lowest and highest plain value are given with the row they come from (`source` of that measurement,
    which the caller sets to the original row's id); censored, approximate and range values are counted, never taken as an extreme. Whether the values of a group
    are comparable with each other (conditions) is `compare()`'s question: a group's range is a description of what was reported, not a ranking."""
    groups: dict[tuple, list[tuple[int, dict]]] = {}
    for i, m in enumerate(measures):
        key = (m["kind"], (m["target"] or "").strip(), (m["species"] or "").strip(), (m["system"] or "").strip())
        groups.setdefault(key, []).append((i, m))
    out = []
    for (kind, target, species, system), items in groups.items():
        plain = [(i, m) for i, m in items if m["converted_nM"] is not None and not ({"CENSORED", "APPROXIMATE", "RANGE"} & set(m["flags"]))]
        lo = min(plain, key=lambda t: t[1]["converted_nM"], default=None)
        hi = max(plain, key=lambda t: t[1]["converted_nM"], default=None)
        out.append({"kind": kind, "target": target, "species": species, "system": system, "n": len(items), "n_plain": len(plain),
                    "n_bounds_or_ranges": sum(1 for _, m in items if {"CENSORED", "APPROXIMATE", "RANGE"} & set(m["flags"])),
                    "n_unusable": sum(1 for _, m in items if m["converted_nM"] is None),
                    "lowest_nM": lo[1]["converted_nM"] if lo else None, "lowest_ref": lo[1]["source"] if lo else "",
                    "highest_nM": hi[1]["converted_nM"] if hi else None, "highest_ref": hi[1]["source"] if hi else ""})
    return sorted(out, key=lambda g: (g["kind"], g["target"], g["species"], g["system"]))


def render_summary(groups: list[dict]) -> str:
    """One cell for a table: each group on its own, with the row of its lowest value. Values stay nM as converted; the original rows hold value and unit."""
    parts = []
    for g in groups:
        span = "no plain value" if g["lowest_nM"] is None else (f"{g['lowest_nM']:.4g} nM" if g["n_plain"] == 1 or g["lowest_nM"] == g["highest_nM"] else f"{g['lowest_nM']:.4g}-{g['highest_nM']:.4g} nM")
        extra = (f", {g['n_bounds_or_ranges']} bound/range" if g["n_bounds_or_ranges"] else "") + (f", {g['n_unusable']} without a usable value" if g["n_unusable"] else "")
        where = " ".join(x for x in (g["target"], g["species"], g["system"]) if x)
        parts.append(f"{g['kind']} [{where}] n={g['n']}: {span}{extra} (lowest at {g['lowest_ref'] or 'row not named'})")
    return " | ".join(parts)


def from_gtopdb(row: dict) -> dict:
    """The two quantitative views of one GtoPdb interactions.csv row, side by side: the log value and the original nanomolar column."""
    kind = (row.get("Original Affinity Units") or "").strip()
    common = dict(target=row.get("Target", ""), species=row.get("Target Species", ""), source="GtoPdb interactions row (original reference in its PubMed ID column)")
    rel = (row.get("Original Affinity Relation") or "=") or "="
    unit = (row.get("Affinity Units") or "").strip()
    logv = measure(unit, row.get("Affinity Median"), None, rel, low=row.get("Affinity Low"), high=row.get("Affinity High"), **common) if unit.startswith("p") else None
    nm = measure(kind, row.get("Original Affinity Median nm"), "nM", rel, low=row.get("Original Affinity Low nm"), high=row.get("Original Affinity High nm"), **common) if kind in KINDS else None
    return {"log": logv, "nm_column": nm, "internal": internal_check(logv, nm)}


def internal_check(logv: dict | None, nm: dict | None, tol: float = 0.5) -> dict:
    """Do the log value and the nanomolar column of one row say the same thing? tol is in log10 units (0.5 leaves room for rounding of p-values)."""
    if not logv or not nm or logv["converted_nM"] is None or nm["converted_nM"] is None or nm["converted_nM"] <= 0:
        return {"state": "NOT_CHECKABLE", "log10_ratio": None}
    lr = math.log10(nm["converted_nM"] / logv["converted_nM"])
    if abs(lr) < tol:
        return {"state": "AGREE", "log10_ratio": round(lr, 2)}
    return {"state": "UNIT_CONFLICT_SUSPECT" if abs(abs(lr) - round(abs(lr / 3)) * 3) < 0.1 and abs(lr) > 2.5 else "DISAGREE", "log10_ratio": round(lr, 2)}


def scan_gtopdb(path: Path):
    with open(path, encoding="utf-8", newline="") as f:
        if not f.readline().lstrip('"').startswith("#"):   # the registry file opens with a quoted version comment line
            f.seek(0)
        for r in csv.DictReader(f):
            v = from_gtopdb(r)
            if v["internal"]["state"] in ("UNIT_CONFLICT_SUSPECT", "DISAGREE"):
                yield r, v["internal"]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sc = sub.add_parser("scan-gtopdb", help="list rows whose log value and nanomolar column disagree (reads the pinned cache file)")
    sc.add_argument("--tsv", type=Path, default=None, help="also write the rows, with the input digest and registry version, as a TSV")
    c = sub.add_parser("convert", help="print one conversion with its transformation")
    c.add_argument("value")
    c.add_argument("unit", help="pIC50, pKi... or nM, uM, mM, M, pM")
    a = ap.parse_args(argv)
    if a.cmd == "convert":
        m = measure(a.unit, a.value, None) if a.unit.startswith("p") else measure("IC50", a.value, a.unit)
        print(m["original"], "->", m["converted_nM"], "nM via", m["transform"], m["flags"])
        return 0
    import compound_catalog as cc
    path, digest = cc.cache_file("gtopdb/interactions.csv")
    print(f"input {path} sha256 {digest}")
    n = 0
    flagged = []
    for r, i in scan_gtopdb(path):
        n += 1
        flagged.append((r, i))
        print(f"{i['state']:22s} log10(nM column / from p-value) {i['log10_ratio']:+.2f}  {r['Ligand'][:30]} | {r['Target'][:24]} | {r['Target Species'][:10]} | {r['Affinity Units']} {r['Affinity Median'][:5]} | nM column {r['Original Affinity Median nm']}")
    if a.tsv:
        with open(path, encoding="utf-8") as f:
            version = f.readline().strip().strip('"')
        with open(a.tsv, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["state", "log10_nM_column_over_p_value", "ligand", "target", "species", "affinity_units", "affinity_median", "original_affinity_units", "nM_column", "relation", "pubmed_id", "registry_version", "input_sha256"])
            for r, i in flagged:
                w.writerow([i["state"], i["log10_ratio"], r["Ligand"], r["Target"], r["Target Species"], r["Affinity Units"], r["Affinity Median"], r["Original Affinity Units"],
                            r["Original Affinity Median nm"], r["Original Affinity Relation"], r["PubMed ID"], version, digest])
    print(f"{n} rows; a factor of about 1000 is a unit slip candidate (open the source; the check does not say which column is wrong); the other disagreements are not a power of 1000 and are left unexplained")
    return 0


if __name__ == "__main__":
    sys.exit(main())
