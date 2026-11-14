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
                                             competing=["risk_of_acting_on_a_compensation"], limits=["counter_evidence"], expected=["adds_over_general_anticonvulsant_action"],
                                             measure=["result_that_would_reject_it"], controls=["functional_comparator", "mechanism_comparator"], support=["depth_of_support"],
                                             title="lever", sibling_cell="lever", mapping_unconfirmed=True, nomination_from_status=True, dropped=("status", "dropped"),
                                             attach=dict(matrix="matrix.tsv", notes="levers_notes.md"),
                                             owner_stated={"L2": {"CF03": "attached by the owners' reading (SCI, PRESIDIO-001, unverified when built): the E5 stratification side; no declared key of this row reaches it"}},
                                             unattached={"CF01": "SCI47 is not consistent on the sIPSC configuration (its Phase 0 item (i) asks a pipette-set chloride, its cohort sentence names perforated native chloride): stating the conflict for a lever needs a choice that is the owners'"},
                                             rivals_note="other rows of the same package (their relations are stated in this table's own cells: L3's status says it gates L1 and L2, L4's functional_comparator names L5 and the GABA arms, L4 and L5 are labelled alternative levers; the explanation-to-lever table is levers_notes.md, rows E1-E6; matrix.tsv relates observations to explanations and some of its rows carry no lever id)",
                                             expected_missing="this row's own cells in levers.tsv (status, adds_over_general_anticonvulsant_action, risk_of_acting_on_a_compensation) state by-explanation conditions; the explanation-to-lever table is levers_notes.md and the observation-to-explanation table is matrix.tsv: read them there, none is attached here beyond the ids this row names",
                                             conflict_notes={"CF23": "owner note (SCI, PRESIDIO-001 blind reader): SCI47 design_review (b) reviews the IT46 p9 design and gives a reason against matching a reuptake arm on membrane potential and input resistance (the matched measure there is tonic current or sIPSC decay); it says nothing about SCI42's variable. A tension inside SCI47, incomplete, not wrong: the line above is printed as ADV-006 wrote it and no side is taken"},
                                             owner_refs={"L1": ["levers_notes.md#Already-used antiseizure drugs", "design_review.md#(d)", "README.md#3", "matrix#O12"], "L2": ["levers_notes.md#Already-used antiseizure drugs", "design_review.md#(d)", "README.md#3", "matrix#O12"]},
                                             owner_rows={"L2": {"M01": "owners' reading: first hop for the lever; no declared key of this row reaches it", "M03": "first hop through O01/O05 in ADV-006's M03; no declared key of this row reaches it"}}),
    # Owner reading (SCI, PRESIDIO-001, 2026-11-14; unverified until its blind reader reports): all cells faithful, with the slot corrections applied here: counter_evidence is evidence (limits), the 'adds over general anticonvulsant
    # action' cell is an outcome-to-lever condition (expected slot), only the rejection cell decides (measure), comparators are controls, the nomination follows the package's own status.
}
PKG_FIELDS = FIELDS + ["package_ref", "direction_stated", "unmapped_cells", "package_title", "recorded_support", "reopen_or_abandon", "design_join", "lever_attachments"]


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
    notes = PKG_MAP.get(pkg, {}).get("conflict_notes", {})
    shown = " ".join(parts)
    extra = "".join(f" || {c}: {note}" for c, note in notes.items() if f"{c} [type:" in shown)
    return " || ".join(parts) + extra + " || no side is chosen on any conflict; no order here is a result"


def _section(path: Path, heading_start: str) -> tuple[str, int]:
    """The text under a markdown heading that starts with `heading_start`, until the next heading of the same or a higher level, with the line it starts on."""
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if re.match(r"#+\s", line) and line.lstrip("# ").startswith(heading_start):
            level = len(line) - len(line.lstrip("#"))
            body = []
            for l2 in lines[i + 1:]:
                if re.match(r"#+\s", l2) and len(l2) - len(l2.lstrip("#")) <= level:
                    break
                body.append(l2)
            return "\n".join(body).strip(), i + 1
    return "", 0


def _owner_ref_text(ref, m):
    out_dir = DR / "inhibitory_defect_sci47_20261112"
    f, _, anchor = ref.partition("#")
    if f == "matrix":
        mr, loc = _matrix_rows(m).get(anchor, (None, ""))
        return f"{loc}: matrix {anchor}: " + " | ".join(f"{c}: {mr[c]}" for c in ("observation", "what_each_outcome_would_favour", "pharmacological_decision_it_would_change")) if mr else f"matrix {anchor}: not found"
    path = out_dir / "README.md" if f == "README.md" else out_dir / "output" / f
    if f == "README.md":
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if line.startswith(f"{anchor}. "):
                return f"{path.relative_to(ROOT)}:{n}: {line}"
        return f"{ref}: not found"
    text, n = _section(path, anchor if f != "design_review.md" else "(d)")
    return f"{path.relative_to(ROOT)}:{n}: {text}" if text else f"{ref}: not found"


def _matrix_rows(m):
    path = DR / "inhibitory_defect_sci47_20261112" / "output" / m["attach"]["matrix"]
    with open(path, encoding="utf-8", newline="") as f:
        return {r["obs_id"]: (r, f"{path.relative_to(ROOT)}:{n}") for n, r in enumerate(csv.DictReader(f, delimiter="\t"), start=2)}


def _notes_rows(m):
    """Rows of the explanation-to-lever table of levers_notes.md, verbatim, keyed by the explanation id that starts their second cell."""
    path = DR / "inhibitory_defect_sci47_20261112" / "output" / m["attach"]["notes"]
    out = {}
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) == 4 and re.match(r"E\d\b", cells[1]):
            out[re.match(r"E\d", cells[1]).group(0)] = (cells, f"{path.relative_to(ROOT)}:{n}")
    return out


def lever_attachments(pkg, key, row, m, design_all):
    """HE54 (SCI's owner reading, PRESIDIO-001): what a lever row DECLARES it relates to, attached verbatim and never widened. (1) O-ids and E-ids named in the lever's own cells: the matrix rows and the
    explanation-to-lever rows of levers_notes.md. (2) The matrix tokens (`sci47_inhibitory#matrix:<O>`) of the ADV-006 rows declared for this lever. (3) The ADV-006 rows whose requests_merged names an attached matrix row,
    and the genuine conflicts on them, except the ones the mapping records as the owners' unattached choice. The E-id route alone cannot separate one lever from another (the same matrix rows name E1-E3 for L1 and L2),
    so the rows named only through an E-id are listed by id and not attached. A word in a cell is not a link."""
    matrix, notes = _matrix_rows(m), _notes_rows(m)
    alias = TOKEN_ALIASES.get(pkg, "")
    meas = {x["key"]: x["row"] for x in design_all if x["package"] == ADV006 and x["table"] == "measurements.tsv"}
    conf = {x["key"]: x["row"] for x in design_all if x["package"] == ADV006 and x["table"] == "conflicts.tsv"}
    text = " ".join(str(v) for k, v in row.items() if k != "lever")
    own_o = sorted(set(re.findall(r"\bO\d{2}\b", text)) & set(matrix))
    own_e = sorted(set(re.findall(r"\bE\d\b", text)))
    declared = [mid for mid, r in meas.items() if f"{alias}#levers:{key}" in [t.strip() for t in r["requests_merged"].split(";")]]
    token_o = sorted({t.strip().split(":", 1)[1] for mid in declared for t in meas[mid]["requests_merged"].split(";") if t.strip().startswith(f"{alias}#matrix:")} & set(matrix) - set(own_o))
    attached = own_o + token_o
    fan = sorted({o for e in own_e for o, (mr, _) in matrix.items() if re.search(rf"\b{e}\b", mr["what_each_outcome_would_favour"])} - set(attached))
    cols = ("observation", "compatible_explanations", "weakened_explanations", "discriminating_measure", "what_each_outcome_would_favour", "pharmacological_decision_it_would_change")
    parts = []
    for o in attached:
        mr, ref = matrix[o]
        via = "named in this lever's own cells" if o in own_o else f"named in requests_merged of {', '.join(declared)} (declared for this lever)"
        parts.append(f"matrix {o} [{ref}; {via}]: " + " | ".join(f"{c}: {mr[c]}" for c in cols))
    for e in own_e:
        if e in notes:
            cells, ref = notes[e]
            parts.append(f"levers_notes {e} [{ref}; the explanation-to-lever table]: if the recordings show: {cells[0]} | explanation: {cells[1]} | lever that becomes interpretable: {cells[2]} | lever that does not: {cells[3]}")
    if fan:
        parts.append(f"matrix rows that name {', '.join(own_e)} in their outcome cell, listed and NOT attached (the E-id route cannot separate this lever from the others): {', '.join(fan)}")
    reach = [mid for mid, r in meas.items() if any(f"{alias}#matrix:{o}" in [t.strip() for t in r["requests_merged"].split(";")] for o in attached)]
    if reach:
        gen = [c for c, cr in conf.items() if cr["type"] == "genuine" and set(i.strip() for i in cr["m_id"].split(";")) & set(reach)]
        held = {c: m["unattached"][c] for c in gen if c in m.get("unattached", {})}
        parts.append(f"ADV-006 rows whose requests_merged names an attached matrix row: {', '.join(reach)}; genuine conflicts on them: "
                     + ("; ".join(f"{c} [cell_type: {conf[c]['cell_type']}; {conf[c]['source_A']}: {conf[c]['quote_A']!r}; {conf[c]['source_B']}: {conf[c]['quote_B']!r}]" for c in gen if c not in held) or "none")
                     + "".join(f"; {c} NOT attached: {why}" for c, why in held.items()))
    bullet = next((l for l in (DR / "inhibitory_defect_sci47_20261112" / "output" / m["attach"]["notes"]).read_text(encoding="utf-8").splitlines() if re.match(rf"\* \*\*{key}\b", l)), "")
    if bullet:
        parts.append(f"levers_notes bullet for {key} (this lever's id starts it; the 'Kept, with the reason' or 'Dropped' list): {bullet}")
    for mid, why in (m.get("owner_rows") or {}).get(key, {}).items():
        if mid in meas:
            parts.append(f"ADV-006 row {mid} ({meas[mid]['name']}): {why} (owner-stated, SCI PRESIDIO-001)")
    for ref in (m.get("owner_refs") or {}).get(key, []):
        parts.append(f"owner-stated attachment (SCI, PRESIDIO-001; not reached by a declared key of this row) {ref}: {_owner_ref_text(ref, m)}")
    for c, why in (m.get("owner_stated") or {}).get(key, {}).items():
        if c in conf:
            parts.append(f"{c} [cell_type: {conf[c]['cell_type']}; {conf[c]['source_A']}: {conf[c]['quote_A']!r}; {conf[c]['source_B']}: {conf[c]['quote_B']!r}] {why}")
    shown = " ".join(parts)
    for c, note in (m.get("conflict_notes") or {}).items():
        if c + " [" in shown:
            parts.append(f"{c}: {note}")
    return " || ".join(parts) if parts else "no id named by this lever's cells, and no matrix token declared for it by ADV-006: nothing attached (a word-only link is not a link)"


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
                used = set(m["observation"] + m.get("support", []) + m["relation"] + m["context"] + m["action"] + m["compound"] + m["premise"] + m.get("competing", []) + m.get("limits", []) + m.get("controls", []) + m["expected"] + m["measure"] + m.get("reopen", []) + [m["title"]])
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
                                source_and_limits="package row, verbatim cells; no direction asserted; labels of the package kept: " + cells(r, [c for c in ("class", "status", "label") if r.get(c)]) + (" || counter-evidence as documented by the package (evidence, not an explanation): " + cells(r, m["limits"]) if m.get("limits") and cells(r, m["limits"]) else ""),
                                expected_result_by_explanation=cells(r, m["expected"]) or m.get("expected_missing", "not stated by the package (missing): its recorded support and counter-evidence are not a falsifiable prediction"), decision_measure=cells(r, m["measure"]) or "not stated by the package: a question, not an experiment",
                                experiments=("controls as documented by the package (controls, not outcomes): " + cells(r, m["controls"]) if m.get("controls") and cells(r, m["controls"]) else ""), unresolved_refs="", nomination=(f"NOT PROPOSED: the package drops this row (its own status label: {r.get(dcol)!r}); kept so the drop is visible" if dropped else (f"the package's own status: {r.get(dcol)!r}; named compounds are the package's, not ranked; no therapeutic direction asserted" if m.get("nomination_from_status") else "CONDITIONAL; named compounds are the package's, not ranked; no therapeutic direction asserted"))
                                + ("; mapping drafted by HE and read by the owners (SCI, PRESIDIO-001, 2026-11-14), whose own blind reader had not reported when this was built" if m.get("mapping_unconfirmed") else ""),
                                design_rows_same_investigation=("dropped by the package: the investigation-level list of design rows is not repeated for a row nobody proposes" if dropped else design_pointer(inv, pk)),
                                package_ref=x["id"] + " @ " + x["source_ref"], direction_stated="none (the package states no therapeutic direction)", unmapped_cells=",".join(unmapped), package_title=r.get(m["title"], ""), reopen_or_abandon=cells(r, m.get("reopen", [])) or "not stated by the package", recorded_support=cells(r, m.get("support", [])),
                                design_join=design_join(pkg, x["key"], design_all) if m.get("adv006") else "",
                                lever_attachments=lever_attachments(pkg, x["key"], r, m, design_all) if m.get("attach") else ""))
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
