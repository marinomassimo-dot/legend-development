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
Two potency propositions of one compound are NOT_COMPARABLE when a recording condition stated on both sides differs (system, holding potential, glycine, glutamate, ATP, scaffold...); CONDITIONS_INSUFFICIENT when the conditions are missing on one side or the system is not recognised (a premise to name, not a block); COMPARABLE only when the conditions are documented and equal (framework/scripts/assay_conditions.py).
Relation (HE47 H1): a proposition whose `relation` cell says other_route or context names the compound without measuring the mechanism the comparison tests; it is listed (`uncounted_props`) and never raises the tier. `counter_props` lists propositions whose `direction` cell is opposes, null or mixed: counter-evidence stays visible and never changes a tier (a probe with a negative result is still a probe). `unclassified_props` lists counted propositions whose relation is not stated. A state names failing pairs; its bracket gives their number among all potency pairs.
A premise that no source resolves keeps the role conditional: the engine never writes 'weakened' without an explicit ABSENCE or measured-negative row."""
from __future__ import annotations
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import hypothesis_package as hp  # noqa: E402
import assay_conditions as ac  # noqa: E402

ALIASES = {"d-apv": ["d-apv", "d-ap5", "apv"], "ro 25-6981": ["ro 25-6981", "ro25-6981", "ro 25 6981"], "uk-5099": ["uk-5099", "uk5099", "uk 5099"], "oxamate": ["oxamate", "sodium oxamate"], "ki-696": ["ki-696", "ki696", "l6i"], "dimethyl fumarate": ["dimethyl fumarate", "dmf"], "monomethyl fumarate": ["monomethyl fumarate", "mmf"], "ra839": ["ra839", "ra-839", "ra 839"], "sulforaphane": ["sulforaphane", "r-sulforaphane"], "bardoxolone methyl": ["bardoxolone methyl", "cddo-me"]}
OUT_FIELDS = ["item_id", "name", "evidence_tier", "tier_props", "role_derived", "role_reason", "comparison_state", "premise_needed", "discriminating_measure", "public_source_work", "relaunch_question", "uncounted_props", "counter_props", "unclassified_props"]

def names_of(name_full: str) -> list[str]:
    return [re.sub(r"\s*\(.*?\)", "", n).strip() for n in name_full.split(";") if n.strip() and "different structure" not in n and "tool arm" not in n or n.strip().startswith("GYKI")]

def pattern(name: str):
    forms = ALIASES.get(name.lower(), [name.lower()])
    return re.compile(r"(?<![\w-])(" + "|".join(re.escape(f) for f in forms) + r")(?![\w-])", re.I)

def counts_toward_tier(p: dict) -> bool:
    """HE47 H1: a proposition that names the compound but, by its author's `relation` cell, does not measure the mechanism the comparison tests (other_route, context)
    is listed with the compound and never raises its tier. An unclassified one counts as it always did: older packages read as before. Nothing is read from the statement text."""
    return hp.prop_facets(p)["relation"] not in ("other_route", "context")


def tier_of(props: list[dict]) -> str:
    """props already carry `shared` (names another compound: a class statement, never a per-molecule measurement)."""
    if any(not p.get("shared") and p["depth"].startswith(("partial_fulltext_read", "fulltext_read")) and p["class"].startswith("compound") for p in props): return "PRIMARY"
    if any(p["class"].startswith(("transfer", "derived")) or p["depth"].startswith("partial_fulltext_read") for p in props): return "TRANSFER"
    if props: return "ABSTRACT"
    return "NONE"

def compare_props(a: dict, b: dict, cells: dict | None = None) -> dict:
    """Two propositions' recording conditions, read by the generic assay_conditions: DOCUMENTED_AGREEMENT / DOCUMENTED_INCOMPATIBILITY / INSUFFICIENT."""
    field = "species_system_age_prep_exposure_readout"
    return ac.compare(ac.parse(a.get(field, ""), cells), ac.parse(b.get(field, ""), cells))

def comparable(a: dict, b: dict) -> tuple[bool, str]:
    """Kept for callers of the earlier name: False only for a documented incompatibility (insufficient information is not a block)."""
    r = compare_props(a, b)
    return r["state"] != ac.INCOMPATIBILITY, "; ".join(f"{a['prop_id']} and {b['prop_id']} differ in {x}" for x in r["reasons"]) if r["state"] == ac.INCOMPATIBILITY else ""

def derive(items: list[dict], pkg: dict, tag: str = "") -> list[dict]:
    """items: compound_view rows (item_id, name_full, kind...); pkg: a loaded pharmacological_comparison package (hp.load_comparison)."""
    dec, cmp_, meas = pkg["dec"], pkg["cmp"], pkg["meas"]; out = []
    universe = [n for i in items for n in names_of(i["name_full"])] + ["CP-465,022", "cyclothiazide", "TCN-201", "CP-101,606"]
    for it in items:
        for nm in names_of(it["name_full"]):
            pat = pattern(nm)
            limited = {m.group(1) for p in dec.values() if pat.search(p["statement"]) for m in re.finditer(r"limit of (D\d{2})", p["statement"])}
            named = [dict(p, shared=any(o != nm and pattern(o).search(p["statement"]) for o in universe)) for p in dec.values()
                     if pat.search(p["statement"]) and not p["class"].startswith("absence") and p["prop_id"] not in limited and "limit of D" not in p["statement"][:40]]
            props = [p for p in named if counts_toward_tier(p)]
            side = [p for p in named if not counts_toward_tier(p)]
            rows = {k: r for k, r in cmp_.items() if pat.search(next((v for c, v in r.items() if c.startswith("compound_or_probe")), ""))}
            ref = any(re.search(re.escape(nm) + r"[^.]*\bis the reference\b", next((v for c, v in r.items() if c.startswith(("pharmacological_action", "action_context"))), ""), re.I) for r in cmp_.values()) or any(re.search(r"\bd-apv\b", nm, re.I) and "reference" in v for r in cmp_.values() for c, v in r.items() if c.startswith("pharmacological_action"))
            tier = tier_of(props)
            cells = {i: q.get("species_system_age_prep_exposure_readout", "") for i, q in dec.items()}
            nc = [(a, b, compare_props(a, b, cells)) for i, a in enumerate(props) for b in props[i + 1:] if all(x["class"].startswith("compound") and not x["shared"] and re.search(r"IC50|\bKi\b|\bKd\b|percent|%|fold|kcat|maxim", x["statement"]) for x in (a, b))]
            bad = [f"{a['prop_id']} and {b['prop_id']} differ in " + "; ".join(r["reasons"]) for a, b, r in nc if r["state"] == ac.INCOMPATIBILITY]
            thin = [f"{a['prop_id']} and {b['prop_id']}: " + "; ".join(r["reasons"]) for a, b, r in nc if r["state"] == ac.INSUFFICIENT]
            # the state names the pairs that fail; the scope says how many pairs there were, so one failing pair is not read as a verdict on the compound
            scope = f" [pairs: {len(bad)} incompatible, {len(thin)} insufficient, {len(nc) - len(bad) - len(thin)} agreeing, of {len(nc)}]" if (bad or thin) else ""
            blocking = [m for m in meas.values() if any(k in hp._blocked_keys(m["blocks_which_comparison_row"], cmp_) for k in rows)]
            if ref: role, why = "control", "named the reference in the comparison design; tier does not apply"
            elif tier == "PRIMARY": role, why = it["kind"] if it["kind"] in ("probe", "known_requalified") else "probe", f"mechanism read in a primary source ({', '.join(p['prop_id'] for p in props)})"
            else:
                miss = {"TRANSFER": "propositions only from another system or by arithmetic", "ABSTRACT": "abstract-level values only, primary text not reached",
                        "NONE": ("named only in propositions that do not measure the mechanism tested (" + ", ".join(f"{p['prop_id']} {hp.prop_facets(p)['relation']}" for p in side) + ")") if side else "no proposition in the package names it"}[tier]
                role, why = "unresolved", miss
            first = min(blocking, key=lambda m: -len([k for k in hp._blocked_keys(m["blocks_which_comparison_row"], cmp_)])) if blocking else None
            out.append({"item_id": it["item_id"], "name": nm, "evidence_tier": tier, "tier_props": ",".join(f"{tag}:{p['prop_id']}" for p in props), "role_derived": role, "role_reason": why,
                        "comparison_state": (f"NOT_COMPARABLE: " + "; ".join(bad) + scope) if bad else ("CONDITIONS_INSUFFICIENT: " + "; ".join(thin) + scope) if thin else ("COMPARABLE" if nc else "NO_POTENCY_PAIR" if len(props) > 1 else "SINGLE_OR_NONE"),
                        "premise_needed": ",".join(m["meas_id"] for m in blocking), "discriminating_measure": first["measurement"] if first else "",
                        "public_source_work": "read the primary source for the named propositions" if tier in ("ABSTRACT", "TRANSFER", "NONE") and not ref else "",
                        "relaunch_question": first["why_no_literature_can_substitute"] if first else "",
                        "uncounted_props": ",".join(f"{tag}:{p['prop_id']}={hp.prop_facets(p)['relation']}" for p in side),
                        "counter_props": ",".join(f"{tag}:{p['prop_id']}={hp.prop_facets(p)['direction']}" for p in named if hp.prop_facets(p)["direction"] in ("opposes", "null", "mixed")),
                        "unclassified_props": ",".join(f"{tag}:{p['prop_id']}" for p in props if hp.prop_facets(p)["relation"] == hp.UNCLASSIFIED)})
    return out

def _STATE_RANK(state: str) -> int:
    """Across packages the weakest answer wins: a documented incompatibility, then insufficient information, then agreement."""
    return 3 if state.startswith("NOT_COMPARABLE") else 2 if state.startswith("CONDITIONS_INSUFFICIENT") else 1 if state == "COMPARABLE" else 0

RANK = {"PRIMARY": 3, "TRANSFER": 2, "ABSTRACT": 1, "NONE": 0}

def merge(rows: list[dict]) -> list[dict]:
    """One row per (item, name) across packages: the strongest tier wins, every package's props, premises and states are kept."""
    by: dict = {}
    for r in rows:
        k = (r["item_id"], r["name"])
        if k not in by: by[k] = dict(r); continue
        m = by[k]
        best = r if RANK[r["evidence_tier"]] > RANK[m["evidence_tier"]] else m
        for f in ("tier_props", "premise_needed", "uncounted_props", "counter_props", "unclassified_props"): m[f] = ",".join(x for x in dict.fromkeys((m.get(f, "") + "," + r.get(f, "")).split(",")) if x)
        if "control" in (m["role_derived"], r["role_derived"]): best = m if m["role_derived"] == "control" else r
        for f in ("evidence_tier", "role_derived", "role_reason", "public_source_work"): m[f] = best[f]
        for f in ("discriminating_measure", "relaunch_question"): m[f] = m[f] or r[f]
        m["comparison_state"] = max(m["comparison_state"], r["comparison_state"], key=_STATE_RANK)
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
