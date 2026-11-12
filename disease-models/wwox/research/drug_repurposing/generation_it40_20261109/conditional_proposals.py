"""IT40 P5: conditional pharmacological proposals from physiological-hypothesis packages, without a gene arc.

Reads each linked hypothesis in place through framework/scripts/hypothesis_package.py (Harness) and the by-action search of
mechsearch_it40_20261109/, and writes one row per hypothesis with the seven things a conditional proposal must keep:
starting observation and context; competing explanations; the premise that would justify the intervention; the pharmacological
action sought; source and limits of each step; the expected result under each explanation; the measure that would change the decision.
Nothing is invented: every cell is a verbatim cell of a package table or a catalogue row. A missing measure generates a question,
never an acquired datum. `--no-link` rebuilds the rows without the package reader (ablation: what the generator held before)."""
import csv, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
DR = HERE.parent
sys.path.insert(0, str(ROOT / "framework/scripts"))
import hypothesis_package as hp  # noqa: E402
sys.path.insert(0, str(HERE.parent / "generation_it46_20261111"))
import cell_context as cc  # noqa: E402  IT46: relation targets joined to a held cell-class expression table

RELATIONS = {"MH1": ["R5"], "MH2": ["R4"], "MH3": [], "BH1": ["R3"], "BH2": ["R1", "R2"], "BH3": ["R6"]}
INVS = ("INV-05", "INV-18")
FIELDS = ["corrections_it40", "proposal_id", "kind", "need_id", "inv_id", "cards", "status", "starting_observation_and_chain", "context", "competing_explanations", "premise_and_action",
          "compound_or_probe_named_by_package", "catalogue_by_action", "cell_context", "source_and_limits", "expected_result_by_explanation", "decision_measure", "experiments", "unresolved_refs", "nomination"]

CORR_ALL = (" Predictions in the arms are INFERENZA from the hypothesis definitions; no cell is a measured result.")
CORRECTIONS = {
 "MH1": "Independent recomputation (IT40 verifier) gives standard-error multiples for the flat-tau argument of about 1.1 to 1.4, not the 3.9 and 2.9 quoted in the chain; read the chain's multiples as not reproduced. The argument also assumes a single compartment and a protocol that does not shorten the apparent tau.",
 "MH2": "The package describes the Ih blocker ivabradine as nonselective across HCN isoforms; the catalogue holds only an HCN4 mechanism row for it, which is a record granularity, not a selectivity.",
 "BH1": "Step 4 of the chain ('NMDAR current required, as d-APV shows') shows dependence of the burst on NMDA-receptor activity at one full block, not a gain.",
 "BH2": "The radiprodil selectivity sentence rests on an unread supplementary figure. Radiprodil washout data are from oocytes.",
 "BH3": "Step 4 ('sufficient to explain') is a possibility from a culture result, not a slice result; the package's own audit leaves no datum for the gap-junction half. The experiment BE4 line calling perampanel, radiprodil and carbenoxolone non-reversible is not supported: perampanel has a recovery time constant of about 3.3 s in culture, and the radiprodil washout datum is from oocytes.",
}
def by_action():
    out = {}
    for r in csv.DictReader(open(ROOT / "disease-models/wwox/research/drug_repurposing/mechsearch_it40_20261109/by_action.tsv"), delimiter="\t"):
        out.setdefault(r["relation"], []).append(r)
    return out

def catalogue_summary(rels, ba):
    parts = []
    for rid in rels:
        rows = [r for r in ba.get(rid, []) if r["catalogue_id"]]
        mol = lambda rs_: len({r["parent_molecule"] for r in rs_})
        down = [r for r in rows if r["direction"] == "down"]
        gran = {}
        for r in rows: gran.setdefault(r["target_record_granularity"], set()).add(r["parent_molecule"])
        parts.append(f"{rid}: {len(rows)} catalogue rows = {mol(rows)} distinct parent molecules on the target symbols (a record is repeated per gene symbol); {mol(down)} reduce activity, {mol(rows) - mol(down)} raise it or have no direction; "
                     + ", ".join(f"{k}: {len(v)}" for k, v in sorted(gran.items())) + ". A catalogue target record says where the mechanism was attached (one protein, a two-gene assembly or a family), not how selective the molecule is")
    return " | ".join(parts) if parts else "no relation searched (no pharmacological action proposed)"

def cell_context_text(rels):
    """IT46: where a held table says the relation's target genes are read (per table, unknown stays unknown); one sentence per relation."""
    rel = cc.relations()
    return " | ".join(f"{rid}: " + cc.context_for(rel[rid], rid)[1] for rid in rels if rid in rel) or "no relation searched (no target genes to place)"


def rows(link=True):
    ba = by_action(); pk = hp.load_all(); out = []
    for inv in INVS:
        rec = hp.record_for(pk, inv)
        for h in rec["hypotheses"]:
            hyp = h["hypothesis"]; hid = h["hyp_id"]
            alts = hyp["competing_explanation"] + (" || linked alternatives: " + "; ".join(f"{a['alt_id']}: {a['explanation']} (matrix {a.get('matrix_column') or 'none'})" for a in h["alternatives"]) if link and h["alternatives"] else "")
            exps, expected = [], []
            for e in (h["experiments"] if link else []):
                exps.append(f"{e['row']['exp_id']}: {e['row']['comparison_arms']}")
                for a in e["arms"]:
                    cols = {k: v for k, v in a.items() if k.startswith("H") and k[1:2].isdigit()}
                    if cols: expected.append(f"{a['arm_id']}: " + " | ".join(f"{k.split('_')[0]}={v}" for k, v in cols.items()) + " | arms do not separate: " + a.get("same_prediction_note_arm_does_not_separate", "") + " | label: " + a.get("prediction_label", ""))
                if not e["arms"]: expected.append(f"{e['row']['exp_id']}: " + e["row"]["what_each_outcome_would_mean"])
            nominated = hyp.get("compound_or_probe", "")
            out.append(dict(corrections_it40=CORRECTIONS.get(hid, "") + CORR_ALL, proposal_id="CP-" + hid, kind="conditional_physiological_hypothesis", need_id=h["need_id"], inv_id=inv, cards=";".join(h["card_ids"]) if isinstance(h["card_ids"], list) else h["card_ids"],
                status=hyp["status"], starting_observation_and_chain=hyp["chain"], context=hyp["context"], competing_explanations=alts or hyp["competing_explanation"],
                premise_and_action=hyp["pharmacological_action"], compound_or_probe_named_by_package=nominated, catalogue_by_action=catalogue_summary(RELATIONS[hid], ba), cell_context=cell_context_text(RELATIONS[hid]),
                source_and_limits=hyp["counter_evidence"] + " || weakening: " + hyp["weakening_result"], expected_result_by_explanation=" ;; ".join(expected) if link else "",
                decision_measure=hyp["what_would_change_the_decision"], experiments=" ;; ".join(exps), unresolved_refs=",".join(h["unresolved_refs"]),
                nomination="ABSTAIN" if nominated.lower().startswith(("none", "no ")) else "NAMED_BY_PACKAGE_ONLY (no ranking, no claim)"))
    return out


# IT47 P1: the hypotheses HE46 made reachable (manifest role `hypotheses_only`, own layout per package) are read through hp.hypotheses_for and mapped, cell by cell, onto the seven things a
# conditional proposal keeps. The mapping is the reviewable part (which cell answers which question); the loader maps nothing. A slot with no cell says so; no direction is invented.
# slot -> package cells (joined in order, each labelled with its own column name). `action_from_relation` names a relation of the IT41/IT43 tables to take the action from when the package has none.
PKG_MAP = {
    "ph_k2p_sci45_20261111": dict(inv="INV-18", relation_ids=[], symbols=["KCNK2", "KCNK3", "KCNK9"],  # the channels the package names (TREK-1, TASK-1, TASK-3)
                                   observation=["initial_observation"], relation=["mechanistic_relation"], context=["context"], action=["action"], compound=["compound_or_class"],
                                  premise=["counter_evidence"], expected=["possible_functional_outcome"], measure=["experiment_that_rejects_it"], title="hypothesis", sibling_cell="hypothesis"),
    # IT47 P4 (new case; mapping fixed from the column names before any row was read, see generation_it47_20261112/p4_gsk3/prereg_it47.md). Post-case correction found by the blind reader (R0):
    # `requires_first` names a prerequisite (premise), not the discriminating measure; the discriminating outcomes are in `refuted_or_replaced_by`. The preregistered run read the measure from `requires_first` (rows kept in p4_gsk3/rows_preregistered_mapping.tsv).
    "gsk3_eif2b_20261107": dict(inv="INV-09", relation_ids=[], symbols=["GSK3B", "GSK3A", "EIF2B5"],  # symbols added after the case: the preregistered run left them empty, so the context join was not tried (prediction c was untested, then wrong)
                                 observation=[], relation=["statement_IPOTESI"], context=["context"], action=["documented_action_on_the_node"], compound=["compound_or_tool", "tool_or_candidate"],
                                premise=["requires_first"], competing=[], expected=["benefit_if_true"], measure=["refuted_or_replaced_by"], title="statement_IPOTESI", sibling_cell="statement_IPOTESI"),
    "nrf2_inv08_20261107": dict(inv="INV-08", relation_ids=["S10"], observation=["what_supports"], relation=["hypothesis"], context=["transfer_note"], action=[], compound=[],
                                premise=["status", "what_refutes"], expected=["what_supports"], measure=["what_separates"], title="hypothesis", sibling_cell="hypothesis", action_from_relation="S10"),
}
PKG_FIELDS = FIELDS + ["package_ref", "direction_stated", "unmapped_cells", "package_title"]


def _relation_action(rid):
    import csv as _csv
    for f in sorted(DR.glob("generation_it4[1-9]_*/relations*.tsv")):
        for r in _csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            if r.get("relation_id") == rid and r.get("action_label"):
                return r["action_label"]
    return ""


def package_rows():
    """One conditional proposal per hypothesis row of the mapped packages. Returns (rows, report) where report lists packages reachable but not mapped."""
    pk = hp.load_all(); out = []; seen_unmapped = {}
    rel = cc.relations()
    for inv in ("INV-18", "INV-08", "INV-09"):
        res = hp.hypotheses_for(pk, inv)
        by_pkg = {}
        for x in res["rows"]:
            by_pkg.setdefault(x["package"], []).append(x)
        for pkg, rws in by_pkg.items():
            m = PKG_MAP.get(pkg)
            if not m:
                seen_unmapped[(inv, pkg)] = len(rws); continue
            def cells(row, names):
                return " | ".join(f"{n}: {row[n]}" for n in names if row.get(n)) or ""
            for x in rws:
                r = x["row"]; sib = [y for y in rws if y is not x]
                rivals = " || ".join(f"{y['key']}: {y['row'].get(m['sibling_cell'], '')}" for y in sib)
                used = set(m["observation"] + m["relation"] + m["context"] + m["action"] + m["compound"] + m["premise"] + m.get("competing", []) + m["expected"] + m["measure"] + [m["title"]])
                action = cells(r, m["action"])
                if not action and m.get("action_from_relation"):
                    action = "not stated by the package; taken from relation " + m["action_from_relation"] + " (" + _relation_action(m["action_from_relation"]) + ")"
                if not action:
                    action = "not stated by the package"
                prem = cells(r, m["premise"])
                unmapped = [c for c in x["columns"] if c not in used and c not in ("id", "hyp_id", "hypothesis_id", m["title"]) and r.get(c)]
                symbols = m.get("symbols") or (rel.get(m["relation_ids"][0], []) if m["relation_ids"] else [])
                out.append(dict(corrections_it40="", proposal_id="CP-" + x["id"], kind="conditional_hypothesis_from_package", need_id="", inv_id=inv, cards="", status="exploratory (IPOTESI); the package row is not an approval",
                                starting_observation_and_chain=(cells(r, m["observation"]) or "not stated by the package") + " [source: " + x["source_ref"] + "]", context=cells(r, m["context"]) or "not stated by the package",
                                competing_explanations=cells(r, m.get("competing", [])) + (" || rival rows of the same package: " + rivals if rivals else ""),
                                premise_and_action="relation: " + cells(r, m["relation"]) + " || action: " + action + " || unresolved premise: " + prem,
                                compound_or_probe_named_by_package=cells(r, m["compound"]) or "none named", catalogue_by_action="", cell_context=(cc.context_for(symbols, (m["relation_ids"] or [pkg])[0])[1] if symbols else "not joined (no relation symbols for this package)"),
                                source_and_limits="package row, verbatim cells; no direction asserted; labels of the package kept: " + cells(r, [c for c in ("class", "status", "label") if r.get(c)]),
                                expected_result_by_explanation=cells(r, m["expected"]), decision_measure=cells(r, m["measure"]) or "not stated by the package: a question, not an experiment",
                                experiments="", unresolved_refs="", nomination="CONDITIONAL; named compounds are the package's, not ranked; no therapeutic direction asserted",
                                package_ref=x["id"] + " @ " + x["source_ref"], direction_stated="none (the package states no therapeutic direction)", unmapped_cells=",".join(unmapped), package_title=r.get(m["title"], "")))
    return out, seen_unmapped


if __name__ == "__main__":
    link = "--no-link" not in sys.argv
    r = rows(link)
    name = "conditional_proposals_it40.tsv" if link else "conditional_proposals_nolink.tsv"
    with open(HERE / name, "w", newline="") as f:
        w = csv.DictWriter(f, FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(r)
    print(len(r), "rows ->", name)
    if link:
        pr, unm = package_rows()
        with open(HERE / "conditional_proposals_packages_it47.tsv", "w", newline="") as f:
            w = csv.DictWriter(f, PKG_FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(pr)
        print(len(pr), "package rows -> conditional_proposals_packages_it47.tsv; reachable but not mapped:", {f"{i}:{p}": n for (i, p), n in unm.items()})
