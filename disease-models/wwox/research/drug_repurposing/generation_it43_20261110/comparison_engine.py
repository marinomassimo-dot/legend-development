#!/usr/bin/env python3
"""IT43 P1: the comparison rows of a package decide a compound's role, premise, experiment and relaunched question.

Reads, through Harness's hypothesis_package, the explicit fields of a pharmacological_comparison package
(decisive.tsv depth/class/system, new_measurements.tsv blocks_which_comparison_row, comparison.tsv needs_new_experiment) and
ties them to a compound by a whole-word name match in the proposition statement or the row's compound cell. No prose is
interpreted beyond that match, no score or probability is produced.

Evidence tier of a compound for the comparison (lowest rung that is true, stated with its props):
  PRIMARY   a proposition naming it with depth partial/full text read and class 'compound/class read'
  TRANSFER  only propositions read in another system, or derived by arithmetic
  ABSTRACT  only abstract-level propositions
  NONE      no proposition names it (not stated here, never 'tested and absent')
Role ceiling: only PRIMARY may be a probe or comparator; every other tier is 'unresolved' with the missing datum named.
A reference control is assigned by the comparison design (the row's action cell calls it the reference), not by tier.
Two potency propositions of one compound are NOT_COMPARABLE when their recording conditions (holding potential, glycine, system) differ.
A premise that no source resolves keeps the role conditional: the engine never writes 'weakened' without an explicit ABSENCE or measured-negative row."""
from __future__ import annotations
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import hypothesis_package as hp  # noqa: E402

ALIASES = {"d-apv": ["d-apv", "d-ap5", "apv"], "ro 25-6981": ["ro 25-6981", "ro25-6981", "ro 25 6981"]}
OUT_FIELDS = ["item_id", "name", "evidence_tier", "tier_props", "role_derived", "role_reason", "comparison_state", "premise_needed", "discriminating_measure", "public_source_work", "relaunch_question"]

def names_of(name_full: str) -> list[str]:
    return [re.sub(r"\s*\(.*?\)", "", n).strip() for n in name_full.split(";") if n.strip() and "different structure" not in n and "tool arm" not in n or n.strip().startswith("GYKI")]

def pattern(name: str):
    forms = ALIASES.get(name.lower(), [name.lower()])
    return re.compile(r"(?<![\w-])(" + "|".join(re.escape(f) for f in forms) + r")(?![\w-])", re.I)

def tier_of(props: list[dict]) -> str:
    """props already carry `shared` (names another compound: a class statement, never a per-molecule measurement)."""
    if any(not p.get("shared") and p["depth"].startswith(("partial_fulltext_read", "fulltext_read")) and p["class"].startswith("compound") for p in props): return "PRIMARY"
    if any(p["class"].startswith(("transfer", "derived")) or p["depth"].startswith("partial_fulltext_read") for p in props): return "TRANSFER"
    if props: return "ABSTRACT"
    return "NONE"

def conditions(p: dict) -> tuple:
    s = p.get("species_system_age_prep_exposure_readout", "")
    mv = re.findall(r"(-\d+) ?mV", s); gly = re.findall(r"(\d+) uM glycine|glycine (\d+) uM", s)
    system = "oocyte" if re.search(r"oocyte", s, re.I) else "HEK" if "HEK" in s else "slice" if re.search(r"slice", s, re.I) else "other"
    free = bool(re.search(r"core[- ]free|without (?:the )?(?:E2|E3BP)|E1-only", s, re.I)); bound = bool(re.search(r"core[- ]bound|(?:with|on) (?:the )?(?:E2|E3BP|E2p/E3BP)", s, re.I))
    scaffold = "core_both" if free and bound else "core_free" if free else "core_bound" if bound else ""
    atp = tuple(re.findall(r"(\d+(?:\.\d+)?) ?[um]M ATP", s))
    return (system, tuple(mv), tuple(g for pair in gly for g in pair if g), scaffold, atp)

def comparable(a: dict, b: dict) -> tuple[bool, str]:
    ca, cb = conditions(a), conditions(b)
    if ca[0] != cb[0]: return False, f"{a['prop_id']} and {b['prop_id']} differ in system ({ca[0]} / {cb[0]})"
    if ca[1] and cb[1] and ca[1] != cb[1]: return False, f"{a['prop_id']} and {b['prop_id']} differ in holding potential ({ca[1]} / {cb[1]})"
    if ca[2] and cb[2] and ca[2] != cb[2]: return False, f"{a['prop_id']} and {b['prop_id']} differ in co-agonist ({ca[2]} / {cb[2]})"
    if ca[3] and cb[3] and ca[3] != cb[3]: return False, f"{a['prop_id']} and {b['prop_id']} differ in assay scaffold ({ca[3]} / {cb[3]}): lipoamide-site compounds change sign with the core"
    if ca[4] and cb[4] and ca[4] != cb[4]: return False, f"{a['prop_id']} and {b['prop_id']} differ in ATP ({ca[4]} / {cb[4]})"
    return True, ""

def derive(items: list[dict], pkg: dict, tag: str = "") -> list[dict]:
    """items: compound_view rows (item_id, name_full, kind...); pkg: a loaded pharmacological_comparison package (hp.load_comparison)."""
    dec, cmp_, meas = pkg["dec"], pkg["cmp"], pkg["meas"]; out = []
    universe = [n for i in items for n in names_of(i["name_full"])] + ["CP-465,022", "cyclothiazide", "TCN-201", "CP-101,606"]
    for it in items:
        for nm in names_of(it["name_full"]):
            pat = pattern(nm)
            limited = {m.group(1) for p in dec.values() if pat.search(p["statement"]) for m in re.finditer(r"limit of (D\d{2})", p["statement"])}
            props = [dict(p, shared=any(o != nm and pattern(o).search(p["statement"]) for o in universe)) for p in dec.values()
                     if pat.search(p["statement"]) and not p["class"].startswith("absence") and p["prop_id"] not in limited and "limit of D" not in p["statement"][:40]]
            rows = {k: r for k, r in cmp_.items() if pat.search(next((v for c, v in r.items() if c.startswith("compound_or_probe")), ""))}
            ref = any(re.search(re.escape(nm) + r"[^.]*\bis the reference\b", next((v for c, v in r.items() if c.startswith(("pharmacological_action", "action_context"))), ""), re.I) for r in cmp_.values()) or any(re.search(r"\bd-apv\b", nm, re.I) and "reference" in v for r in cmp_.values() for c, v in r.items() if c.startswith("pharmacological_action"))
            tier = tier_of(props)
            nc = [(a, b, comparable(a, b)) for i, a in enumerate(props) for b in props[i + 1:] if all(x["class"].startswith("compound") and not x["shared"] and re.search(r"IC50|\bKi\b|\bKd\b|percent|%|fold|kcat|maxim", x["statement"]) for x in (a, b))]
            bad = [r for _, _, (ok, r) in nc if not ok]
            blocking = [m for m in meas.values() if any(k in hp._blocked_keys(m["blocks_which_comparison_row"], cmp_) for k in rows)]
            if ref: role, why = "control", "named the reference in the comparison design; tier does not apply"
            elif tier == "PRIMARY": role, why = it["kind"] if it["kind"] in ("probe", "known_requalified") else "probe", f"mechanism read in a primary source ({', '.join(p['prop_id'] for p in props)})"
            else:
                miss = {"TRANSFER": "propositions only from another system or by arithmetic", "ABSTRACT": "abstract-level values only, primary text not reached", "NONE": "no proposition in the package names it"}[tier]
                role, why = "unresolved", miss
            first = min(blocking, key=lambda m: -len([k for k in hp._blocked_keys(m["blocks_which_comparison_row"], cmp_)])) if blocking else None
            out.append({"item_id": it["item_id"], "name": nm, "evidence_tier": tier, "tier_props": ",".join(f"{tag}:{p['prop_id']}" for p in props), "role_derived": role, "role_reason": why,
                        "comparison_state": ("NOT_COMPARABLE: " + "; ".join(bad)) if bad else ("COMPARABLE" if len(props) > 1 else "SINGLE_OR_NONE"),
                        "premise_needed": ",".join(m["meas_id"] for m in blocking), "discriminating_measure": first["measurement"] if first else "",
                        "public_source_work": "read the primary source for the named propositions" if tier in ("ABSTRACT", "TRANSFER", "NONE") and not ref else "",
                        "relaunch_question": first["why_no_literature_can_substitute"] if first else ""})
    return out

RANK = {"PRIMARY": 3, "TRANSFER": 2, "ABSTRACT": 1, "NONE": 0}

def merge(rows: list[dict]) -> list[dict]:
    """One row per (item, name) across packages: the strongest tier wins, every package's props, premises and states are kept."""
    by: dict = {}
    for r in rows:
        k = (r["item_id"], r["name"])
        if k not in by: by[k] = dict(r); continue
        m = by[k]
        best = r if RANK[r["evidence_tier"]] > RANK[m["evidence_tier"]] else m
        for f in ("tier_props", "premise_needed"): m[f] = ",".join(x for x in dict.fromkeys((m[f] + "," + r[f]).split(",")) if x)
        if "control" in (m["role_derived"], r["role_derived"]): best = m if m["role_derived"] == "control" else r
        for f in ("evidence_tier", "role_derived", "role_reason", "public_source_work"): m[f] = best[f]
        for f in ("discriminating_measure", "relaunch_question"): m[f] = m[f] or r[f]
        m["comparison_state"] = m["comparison_state"] if m["comparison_state"].startswith("NOT") else r["comparison_state"]
    return list(by.values())

def main():
    inv = (sys.argv[sys.argv.index("--inv") + 1] if "--inv" in sys.argv else "INV-05")
    items = [r for r in csv.DictReader(open(DR / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["inv_id"] == inv]
    pkgs = [p for p in hp.load_all() if p.get("role") == "pharmacological_comparison" and p.get("inv_id") == inv]
    res = merge([r for p in pkgs for r in derive(items, p, p["dir"].parent.name.split("_")[0])])
    out = HERE / ("compound_decisions_it43.tsv" if inv == "INV-05" else f"compound_decisions_{inv.lower().replace('-', '')}_it44.tsv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, OUT_FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(res)
    for r in res: print(r["item_id"], r["name"], r["evidence_tier"], r["role_derived"], "|", r["comparison_state"][:70], "|", r["premise_needed"])

if __name__ == "__main__": main()
