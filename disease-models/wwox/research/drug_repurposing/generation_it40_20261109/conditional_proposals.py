"""IT40 P5: conditional pharmacological proposals from physiological-hypothesis packages, without a gene arc.

Reads each linked hypothesis in place through framework/scripts/hypothesis_package.py (Harness) and the by-action search of
mechsearch_it40_20261109/, and writes one row per hypothesis with the seven things a conditional proposal must keep:
starting observation and context; competing explanations; the premise that would justify the intervention; the pharmacological
action sought; source and limits of each step; the expected result under each explanation; the measure that would change the decision.
Nothing is invented: every cell is a verbatim cell of a package table or a catalogue row. A missing measure generates a question,
never an acquired datum. `--no-link` rebuilds the rows without the package reader (ablation: what the generator held before)."""
import csv, json, re, sys
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
          "compound_or_probe_named_by_package", "catalogue_by_action", "cell_context", "source_and_limits", "expected_result_by_explanation", "decision_measure", "experiments", "unresolved_refs", "nomination", "design_rows_same_investigation"]

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


def design_pointer(inv, pk):
    """HE51: where the design rows of this investigation are. The link is the manifest's `inv_id` and nothing else: the packages state no link from a hypothesis to a measurement, so none is made here.
    Keys only (the rows are in conditional_design_steps_it50.tsv, verbatim); a reachable table with no mapping is named as not in that file; absence is stated, not left empty."""
    rec = hp.design_for(pk, inv)
    mapped, unmapped = {}, {}
    for r in rec["rows"]:
        (mapped if DESIGN_MAP.get(r["package"], {}).get(r["table"]) else unmapped).setdefault((r["package"], r["table"]), []).append(r["key"])
    if not mapped and not unmapped:
        return f"none listed for {inv} ({rec['state']}): no design is registered for it, which does not say that none exists"
    # package-qualified ids, exactly the design_row_id of the file: a bare M16 here would read as the M16 of another package in the same row (IT51 residual)
    keys = lambda d: "; ".join(f"{pkg}::{tab}::{k.split(' ')[0]}" for (pkg, tab), ks in d.items() for k in ks)
    out = (f"{sum(map(len, mapped.values()))} design rows are in conditional_design_steps_it50.tsv for {inv}, read from the manifest's inv_id and not linked to this hypothesis by any package (a design is not an observation): " + keys(mapped)) if mapped else f"no mapped design rows for {inv}"
    return out + (f" || reachable and not mapped, so not in that file: {keys(unmapped)}" if unmapped else "")


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
                nomination="ABSTAIN" if nominated.lower().startswith(("none", "no ")) else "NAMED_BY_PACKAGE_ONLY (no ranking, no claim)", design_rows_same_investigation=design_pointer(inv, pk) if link else ""))
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
                                premise=["requires_first"], competing=["refuted_or_replaced_by"], expected=["benefit_if_true"], measure=["refuted_or_replaced_by"], title="statement_IPOTESI", sibling_cell="statement_IPOTESI"),
    "nrf2_inv08_20261107": dict(inv="INV-08", relation_ids=["S10"], observation=[], support=["what_supports"], relation=["hypothesis"], context=["transfer_note"], action=[], compound=[],
                                premise=["status", "what_refutes"], expected=[], measure=["what_separates"], title="hypothesis", sibling_cell="hypothesis", action_from_relation="S10"),
    # IT49: the two INV-18 packages IT47 reported as reachable and unmapped. The mapping was written from the column names and one full row of each package (the rows were read to fix it, so it is not
    # a pre-registered mapping). Discriminating outcomes (what would favour or weaken the row) go to `measure` and `reopen`; they are NOT the expected result: where a package has no stated
    # expectation, the slot says so. `symbols_by_key` joins each row to the channels it is about, because one package holds rows about different channels.
    "potassium_conductances_sci43_20261110": dict(inv="INV-18", relation_ids=[], symbols_by_key={"KH1": ["KCNJ2", "KCNK2", "KCNK3", "KCNK9"], "KH2": ["KCNQ2", "KCNQ3"], "KH3": ["HCN1", "HCN2"]},
                                                  observation=["observation"], relation=["relation_qualified"], context=["level"], action=["proposed_action_class"], compound=[],
                                                  premise=["premise"], competing=["opposite_context"], expected=["expected_functional_result"], measure=["refuting_measure", "favourable_context"], reopen=["opposite_context"],
                                                  title="relation_qualified", sibling_cell="relation_qualified"),
    "hcn_20261107": dict(inv="INV-18", relation_ids=[], symbols_by_key={"HY1": ["KCNQ2", "HCN1", "HCN2"], "HY2": ["HCN1", "HCN2"], "HY3": ["HCN1", "HCN2"]},
                         observation=["wwox_observation"], relation=["mechanism_and_missing_bridge"], context=["action_cell_context"], action=[], compound=["probe_or_qualified_compound"],
                         premise=["mechanism_and_missing_bridge"], competing=["competing_alternative"], expected=[], measure=["favourable_result"], reopen=["weakening_result", "next_decision"],
                         title="mechanism_and_missing_bridge", sibling_cell="mechanism_and_missing_bridge"),
    # IT50: the INV-02 ISR hypotheses written from the INV-02 row and the audited ISR package (layout like the HCN package). The package states no prediction, so the expected slot says so.
    "isr_inv02_it50_20261113": dict(inv="INV-02", relation_ids=[], symbols=["EIF2AK1", "EIF2AK2", "EIF2AK3", "EIF2AK4", "EIF2B1", "EIF2B2", "EIF2B3", "EIF2B4", "EIF2B5", "PPP1R15A", "PPP1R15B", "EIF2S1"],   # the twelve symbols of IT49-Q02 (the first staged list lacked PPP1R15B)
                                    observation=["wwox_observation"], relation=["explanation_and_rivals"], context=["preparation_context"], action=["hypothesised_action"], compound=["probe_or_compound"],
                                    premise=["unresolved_premise"], competing=["explanation_and_rivals"], expected=["prediction_stated"], measure=["discriminating_result"], reopen=["reopen_or_abandon"],
                                    title="hypothesised_action", sibling_cell="hypothesised_action"),
    # HE53 (ADV's assignment, 2026-11-14): the SCI47 levers of the inhibitory thread, INV-05. Mapping drafted from the column names and the rows, NOT yet confirmed by the package's owners (SCI): `status` carries the
    # lever's own condition (kept, conditional on ...; dropped) and is read as the unresolved premise, a dropped lever stays dropped in that cell; the package states no prediction, so the expected slot says so; the
    # comparators and the rejection result are the measure; no gene symbols are joined (the package names GAT-1, a transaminase and a receptor class, not symbols). `adv006` turns on the declared-key join below.
    "inhibitory_defect_sci47_20261112": dict(inv="INV-05", relation_ids=[], adv006=True, observation=["known_in_WWOX"], relation=["lever"], context=["transferred_from_other_systems_named"],
                                             action=["action_required_and_context"], compound=["compound_or_probe_sustained_by_a_document"], premise=["status"],
                                             competing=["risk_of_acting_on_a_compensation", "counter_evidence"], expected=[], measure=["result_that_would_reject_it", "functional_comparator", "mechanism_comparator"],
                                             support=["depth_of_support", "adds_over_general_anticonvulsant_action"], title="lever", sibling_cell="lever",
                                             mapping_unconfirmed=True, dropped=("status", "dropped"),
                                             rivals_note="other rows of the same package (this table does not classify them; the package relates its rows to explanations, with what each outcome would favour, in its matrix.tsv, which is not registered here)",
                                             expected_missing="not in levers.tsv, the table registered here; the package states compatible and weakened explanations and what each outcome would favour in its matrix.tsv (not registered): not stated here, not absent"),
}
PKG_FIELDS = FIELDS + ["package_ref", "direction_stated", "unmapped_cells", "package_title", "recorded_support", "reopen_or_abandon", "design_join"]


def _relation_action(rid):
    import csv as _csv
    for f in sorted(DR.glob("generation_it4[1-9]_*/relations*.tsv")):
        for r in _csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            if r.get("relation_id") == rid and r.get("action_label"):
                return r["action_label"]
    return ""


ADV006 = "measurement_reconciliation_adv006_20261114"
TOKEN_ALIASES = {"inhibitory_defect_sci47_20261112": "sci47_inhibitory"}   # the alias ADV-006's `requests_merged` writes for a source package: a reviewable declaration, not a guess
LEADING_IDS = re.compile(r"^\s*(M\d{2}(?:\s*,\s*M\d{2})*)\s*(?:\(|$)")   # only a list that STARTS the cell is a declared pointer; an id inside a quotation (SCI42's own M01, say) is not


def ids_declared(row, gating):
    """The ids a cell declares as pointers: the list that starts `interpretable_after` (already read as `gating`) and nothing else."""
    return list(gating)


def design_join(pkg, key, design_rows_all):
    """HE53: join a package row to the ADV-006 design rows through the keys the packages DECLARE, one hop, nothing inferred from prose:
    (1) the measurement rows whose `requests_merged` list holds the token `<alias>#levers:<id>`; (2) the rows named by the list that starts the `interpretable_after` cell of those rows (the sources' conditional
    reading, quoted, never an observation, and an order of cost or priority is not a dependency); (3) the rows whose `lever_or_comparison_gated` cell names the row's id as a whole token (the comparator
    co-requirement); (4) the conflicts whose own `m_id` list holds any of those ids, with their type. Second-hop ids named by the gating rows are listed and NOT followed. The SCI42/SCI47 local ids (L1, O01, SCI42's M01)
    and ADV-006's M-ids are two id spaces: only ADV-006 ids are read, and only from ADV-006 rows."""
    alias = TOKEN_ALIASES.get(pkg)
    if not alias:
        return ""
    meas = {x["key"]: x["row"] for x in design_rows_all if x["package"] == ADV006 and x["table"] == "measurements.tsv"}
    conf = {x["key"]: x["row"] for x in design_rows_all if x["package"] == ADV006 and x["table"] == "conflicts.tsv"}
    if not meas:
        return "ADV-006 design rows are not registered for this investigation: not joined"
    token = f"{alias}#levers:{key}"
    hit = [m for m, r in meas.items() if token in [t.strip() for t in r["requests_merged"].split(";")]]
    if not hit:
        return f"no ADV-006 measurement row declares {token} in requests_merged: not joined (not stated is not tested and absent)"
    parts = []
    for m in hit:
        r = meas[m]
        lead = LEADING_IDS.match(r["interpretable_after"])
        gating = [g.strip() for g in lead.group(1).split(",") if g.strip() in meas] if lead else []
        coreq = [m2 for m2, r2 in meas.items() if m2 != m and re.search(rf"\b{m}\b", r2["lever_or_comparison_gated"])]
        second = []
        for g in gating:
            lead2 = LEADING_IDS.match(meas[g]["interpretable_after"])
            second += [i.strip() for i in (lead2.group(1).split(",") if lead2 else []) if i.strip() in meas and i.strip() not in gating + [m] + coreq]
        second = sorted(set(second))
        ids = [m] + gating + coreq
        cf = [c for c, cr in conf.items() if set(i.strip() for i in cr["m_id"].split(";")) & set(ids)]
        genuine = [c for c in cf if conf[c]["type"] == "genuine"]
        others = [f"{c} ({conf[c]['type']})" for c in cf if conf[c]["type"] != "genuine"]
        cell = r["interpretable_after"]                                    # the quotation part of this cell cites the SOURCES' own ids (SCI42's M01 inside M05's cell); `lever_or_comparison_gated` is ADV-006's own text, its ids are its own
        quoted = sorted(set(re.findall(r"\bM\d{2}\b", cell.split("(", 1)[1] if "(" in cell else "")) - set(ids_declared(r, gating)))
        parts.append(f"{ADV006}::measurements.tsv::{m} (declared by {token}; preparation: {r['preparation']!r}; age_bin: {r['age_bin']!r}; cohort_and_genotype_arms: {r['cohort_and_genotype_arms']!r}; "
                     f"its `interpretable_after`, quoted, is the sources' conditional reading and not an observation: {r['interpretable_after']!r}; its `lever_or_comparison_gated`: {r['lever_or_comparison_gated']!r}"
                     + (f"; ids inside the quotation of `interpretable_after`, a source's own id space (SCI42's or SCI47's, not ADV-006 rows): {', '.join(quoted)}" if quoted else "")
                     + f") | rows named at the start of that cell: {', '.join(gating) or 'none (no leading list in the cell)'} | "
                     f"rows whose `lever_or_comparison_gated` names {m} as a whole token (their own cell, quoted, says what the relation is): "
                     + ("; ".join(f"{c2} {meas[c2]['lever_or_comparison_gated']!r}" for c2 in coreq) or "none") + " | "
                     f"conflicts of type genuine whose m_id names any of {', '.join(ids)}: "
                     + ("; ".join(f"{c} [type: {conf[c]['type']}; cell_type: {conf[c]['cell_type']}; {conf[c]['source_A']}: {conf[c]['quote_A']!r}; {conf[c]['source_B']}: {conf[c]['quote_B']!r}; adjudicable_from_the_packages: {conf[c]['adjudicable_from_the_packages']}]" for c in genuine) or "none")
                     + f"; rows of other types (gap or synonym: not conflicts), same rule: {', '.join(others) or 'none'}"
                     + (f" | second-hop rows named by the gating rows, listed and NOT followed (an order of cost or priority may sit there): {', '.join(second)}; genuine conflicts on them, for the reader to weigh: "
                        + (", ".join(c for c, cr in conf.items() if cr["type"] == "genuine" and set(i.strip() for i in cr["m_id"].split(";")) & set(second) and c not in genuine) or "none beyond those above") if second else ""))
    return " || ".join(parts) + " || no side is chosen on any conflict; no order here is a result"


def package_rows():
    """One conditional proposal per hypothesis row of the mapped packages. Returns (rows, report) where report lists packages reachable but not mapped."""
    pk = hp.load_all(); out = []; seen_unmapped = {}
    rel = cc.relations()
    design_all = [x for inv_ in sorted({p["inv_id"] for p in pk if p.get("role") == "design_only"}) for x in hp.design_for(pk, inv_)["rows"]]
    # IT50: the investigations are read from the manifest (every INV with a hypotheses_only package), not from a fixed list; the three earlier ones keep their order so existing rows stay byte-identical.
    order = ["INV-18", "INV-08", "INV-09"]
    for p in pk:
        if p.get("role") == "hypotheses_only" and p.get("inv_id") and p["inv_id"] not in order:
            order.append(p["inv_id"])
    for inv in order:
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
                used = set(m["observation"] + m.get("support", []) + m["relation"] + m["context"] + m["action"] + m["compound"] + m["premise"] + m.get("competing", []) + m["expected"] + m["measure"] + m.get("reopen", []) + [m["title"]])
                action = cells(r, m["action"])
                if not action and m.get("action_from_relation"):
                    action = "not stated by the package; taken from relation " + m["action_from_relation"] + " (" + _relation_action(m["action_from_relation"]) + ")"
                if not action:
                    action = "not stated by the package"
                prem = cells(r, m["premise"])
                dcol, dpre = m.get("dropped", (None, None))
                dropped = bool(dcol and str(r.get(dcol, "")).strip().lower().startswith(dpre))        # the package's own label, read at the start of its own status cell and declared in the mapping; no other word is read
                unmapped = [c for c in x["columns"] if c not in used and c not in ("id", "hyp_id", "hypothesis_id", m["title"]) and r.get(c)]
                symbols = (m.get("symbols_by_key") or {}).get(x["key"]) or m.get("symbols") or (rel.get(m["relation_ids"][0], []) if m["relation_ids"] else [])
                out.append(dict(corrections_it40="", proposal_id="CP-" + x["id"], kind="package_row_dropped_by_the_package" if dropped else "conditional_hypothesis_from_package", need_id="", inv_id=inv, cards="", status="exploratory (IPOTESI); the package row is not an approval",
                                starting_observation_and_chain=(cells(r, m["observation"]) or "not stated by the package as an observation") + " [source: " + x["source_ref"] + "]", context=cells(r, m["context"]) or "not stated by the package",
                                competing_explanations=cells(r, m.get("competing", [])) + (" || " + m.get("rivals_note", "other rows of the same package (the package does not classify them as rivals, complementary or compatible)") + ": " + rivals if rivals else ""),
                                premise_and_action="relation: " + cells(r, m["relation"]) + " || action: " + action + " || unresolved premise: " + prem,
                                compound_or_probe_named_by_package=cells(r, m["compound"]) or "none named", catalogue_by_action="", cell_context=(cc.context_for(symbols, (m["relation_ids"] or [pkg])[0])[1] if symbols else "not joined (no relation symbols for this package)"),
                                source_and_limits="package row, verbatim cells; no direction asserted; labels of the package kept: " + cells(r, [c for c in ("class", "status", "label") if r.get(c)]),
                                expected_result_by_explanation=cells(r, m["expected"]) or m.get("expected_missing", "not stated by the package (missing): its recorded support and counter-evidence are not a falsifiable prediction"), decision_measure=cells(r, m["measure"]) or "not stated by the package: a question, not an experiment",
                                experiments="", unresolved_refs="", nomination=(f"NOT PROPOSED: the package drops this row (its own status label: {r.get(dcol)!r}); kept so the drop is visible" if dropped else "CONDITIONAL; named compounds are the package's, not ranked; no therapeutic direction asserted")
                                + ("; mapping drafted by HE from the column names and rows, not confirmed by the package's owners" if m.get("mapping_unconfirmed") else ""),
                                design_rows_same_investigation=("dropped by the package: the investigation-level list of design rows is not repeated for a row nobody proposes" if dropped else design_pointer(inv, pk)),
                                package_ref=x["id"] + " @ " + x["source_ref"], direction_stated="none (the package states no therapeutic direction)", unmapped_cells=",".join(unmapped), package_title=r.get(m["title"], ""), reopen_or_abandon=cells(r, m.get("reopen", [])) or "not stated by the package", recorded_support=cells(r, m.get("support", [])),
                                design_join=design_join(pkg, x["key"], design_all) if m.get("adv006") else ""))
    return out, seen_unmapped


# HE50: design-only packages (manifest role `design_only`): steps, controls and decision branches, returned verbatim by hp.design_for and mapped here, cell by cell, onto what a design keeps apart.
# The mapping is the reviewable part and is confirmed by the package's scientific owners; the reader maps nothing and no word of a cell is interpreted. A slot with no column, or an empty cell, says so.
# What each slot is NOT (owners' wording, 2026-11-13): `precondition` stays unmet until the step before it has been run, never assumed true; `controls` are the controls the package documents, some entries say a control is
# NOT qualified, and ids in them refer to module evidence, not to observations of this design; `outcomes` hold possible outcomes together with the conditions and cautions written beside them, never data;
# `decision` is written for several outcomes in one cell and is not collapsed to a favourable branch; an observation does not exist in a design.
DESIGN_MAP = {
    "isrib_discrim_20261108": {"design.tsv": dict(step=["question", "arms", "readouts"], precondition=["condition_on"], controls=["controls_already_qualified_in_module"],
                                                  outcomes=["if_result_X_then"], decision=["decision_it_changes"], scope=[], link=[])},
    "myelin_generative_it36_20261108/levers_bc": {"experiments.tsv": dict(step=["question", "design", "endpoint"], precondition=[], controls=["comparator", "mechanism_control", "engagement_check"],
                                           outcomes=["weakened_by"], decision=["decision_it_changes"], scope=["endpoint_scope", "not_a_substitute_for"], link=["hyp_id"])},
    # HE51: the ADV-006 reconciliation of the inhibitory thread (INV-05 as registered; the SCI42/SCI47 source tables are deliberately NOT registered: one measurement, one row). `m_id` is package-local and the row id is
    # package-qualified, so the pH M01 of another package and this package's chloride rows never meet. No column holds an outcome, a control or a hypothesis link, so those slots say so. `gloss` is appended to a column's own
    # label where the label alone would mislead (the cell is kept verbatim): `open_questions_closed` is not a resolved state, `interpretable_after` quotes both dependencies and priority orders of the sources.
    "measurement_reconciliation_adv006_20261114": {
        "measurements.tsv": dict(step=["name", "source_names", "requests_merged", "preparation", "mode_and_configuration", "quantity_read", "conditions", "unit_of_analysis", "age_bin", "cohort_and_genotype_arms", "endpoint"],
                                 precondition=["interpretable_after"], controls=[], outcomes=[], decision=["lever_or_comparison_gated", "open_questions_closed"],
                                 scope=["not_decided_by_it"], link=[],
                                 gloss={"open_questions_closed": "questions this measurement would inform if it were performed; no measurement exists and no question is closed by this row",
                                        "interpretable_after": "as the sources state it, quoted; an order of cost or priority inside it is not a dependency"}),
        "conflicts.tsv": dict(step=["type", "cell_type", "source_A", "quote_A", "source_B", "quote_B"], precondition=[], controls=[], outcomes=[],
                              decision=["which_would_change_the_interpretation"], scope=["why_both_cannot_be_met_in_one_recording", "adjudicable_from_the_packages"], link=["m_id"],
                              gloss={"adjudicable_from_the_packages": "whether the two source texts alone settle it; no side is chosen by this row"}),
    },
}
DESIGN_FIELDS = ["design_row_id", "package", "table", "inv_id", "source_ref", "step", "precondition_unmet_until_the_step_before_is_run", "controls_as_documented_by_the_package",
                 "possible_outcomes_conditions_and_cautions_not_observed", "conditioned_decision", "scope_and_what_the_result_is_not", "hypothesis_link", "observation", "unmapped_cells"]
ABSENT = "not stated by the package (no such column)"
EMPTY = "not stated by the package (empty cell)"


def design_rows():
    """One row per design row of the mapped `design_only` packages. Returns (rows, unmapped) where unmapped lists reachable tables with no mapping."""
    pk = hp.load_all(); out = []; unmapped = {}
    for inv in sorted({p["inv_id"] for p in pk if p.get("role") == "design_only"}):
        for x in hp.design_for(pk, inv)["rows"]:
            m = (DESIGN_MAP.get(x["package"]) or {}).get(x["table"])
            if not m:
                unmapped[(inv, x["package"], x["table"])] = unmapped.get((inv, x["package"], x["table"]), 0) + 1
                continue
            r, cols = x["row"], x["columns"]

            gloss = m.get("gloss", {})

            def slot(names):
                if not names:
                    return ABSENT
                lab = lambda n: f"{n} [{gloss[n]}]" if n in gloss else n
                return " | ".join(f"{lab(n)}: {r[n]}" if n in cols and r.get(n) else f"{lab(n)}: {EMPTY if n in cols else ABSENT}" for n in names)
            used = {c for k, names in m.items() if k != "gloss" for c in names} | {x["key_column"]}
            out.append(dict(design_row_id=x["id"], package=x["package"], table=x["table"], inv_id=inv, source_ref=x["source_ref"],
                            step=f"{x['key_column']}: {x['key']} | " + slot(m["step"]), precondition_unmet_until_the_step_before_is_run=slot(m["precondition"]),
                            controls_as_documented_by_the_package=slot(m["controls"]), possible_outcomes_conditions_and_cautions_not_observed=slot(m["outcomes"]),
                            conditioned_decision=slot(m["decision"]), scope_and_what_the_result_is_not=slot(m["scope"]), hypothesis_link=slot(m["link"]),
                            observation="absent: a design states no observation; its outcome cells are possible results, not data", unmapped_cells=",".join(c for c in cols if c not in used and r.get(c))))
    return out, unmapped


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
        dr_, dunm = design_rows()
        with open(HERE / "conditional_design_steps_it50.tsv", "w", newline="") as f:
            w = csv.DictWriter(f, DESIGN_FIELDS, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(dr_)
        print(len(dr_), "design rows -> conditional_design_steps_it50.tsv; reachable but not mapped:", {f"{i}:{p}:{t}": n for (i, p, t), n in dunm.items()})
