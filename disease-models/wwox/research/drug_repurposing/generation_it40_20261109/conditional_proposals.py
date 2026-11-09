#!/usr/bin/env python3
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
sys.path.insert(0, str(ROOT / "framework/scripts"))
import hypothesis_package as hp  # noqa: E402

RELATIONS = {"MH1": ["R5"], "MH2": ["R4"], "MH3": [], "BH1": ["R3"], "BH2": ["R1", "R2"], "BH3": ["R6"]}
INVS = ("INV-05", "INV-18")
FIELDS = ["corrections_it40", "proposal_id", "kind", "need_id", "inv_id", "cards", "status", "starting_observation_and_chain", "context", "competing_explanations", "premise_and_action",
          "compound_or_probe_named_by_package", "catalogue_by_action", "source_and_limits", "expected_result_by_explanation", "decision_measure", "experiments", "unresolved_refs", "nomination"]

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
                premise_and_action=hyp["pharmacological_action"], compound_or_probe_named_by_package=nominated, catalogue_by_action=catalogue_summary(RELATIONS[hid], ba),
                source_and_limits=hyp["counter_evidence"] + " || weakening: " + hyp["weakening_result"], expected_result_by_explanation=" ;; ".join(expected) if link else "",
                decision_measure=hyp["what_would_change_the_decision"], experiments=" ;; ".join(exps), unresolved_refs=",".join(h["unresolved_refs"]),
                nomination="ABSTAIN" if nominated.lower().startswith(("none", "no ")) else "NAMED_BY_PACKAGE_ONLY (no ranking, no claim)"))
    return out

if __name__ == "__main__":
    link = "--no-link" not in sys.argv
    r = rows(link)
    name = "conditional_proposals_it40.tsv" if link else "conditional_proposals_nolink.tsv"
    with open(HERE / name, "w", newline="") as f:
        w = csv.DictWriter(f, FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(r)
    print(len(r), "rows ->", name)
