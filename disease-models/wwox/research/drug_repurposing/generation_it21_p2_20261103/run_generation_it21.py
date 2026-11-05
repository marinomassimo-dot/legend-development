#!/usr/bin/env python3
"""IT21 P2 steps B2 to B4: run the existing v4 generation engine on the REFRESHED action table, then attribute, select and hand over proposals.

  run_generation_it21.py engine     [--engine-dir DIR]     run_v4.py on results/actions (+ reach null), into DIR (default results/engine)
  run_generation_it21.py withdrawn  [--engine-dir DIR]     seed-specific rows of the IT10 v4 run that are no longer seed-specific, with the cause
  run_generation_it21.py control    --control-dir DIR      the unguarded engine run must reproduce the IT10 seed-specific list
  run_generation_it21.py anchors                           the compounds the guards were written for, before and after
  run_generation_it21.py direct     [--engine-dir DIR]     direct-search rows that lost their direction
  run_generation_it21.py propose    [--engine-dir DIR]     dispositions, proposals with attribution, handoff, clusters, carried decisions
  run_generation_it21.py all

Nothing here is a second engine. The compound side is `refresh_actions_it21.py` (the v3 builder plus the search-layer guards); the engine is
`generation_it10_p1_20261031/engine_v4/run_v4.py` (new options --actions and --reach, defaults unchanged); the role-aware dispositions are
`generation_it10_p1_20261031/dispose_it10.py` (imported, not copied). What this file adds is what no earlier file did: per-proposal attribution
(which seed row, origin, level and assumption generated it, which alternatives share its mechanism, which earlier decision or abstention
touches it), a written selection rule for the hand-over, and a status vocabulary in which no row can be called qualified.

A conditional hypothesis (H_HARM / H_PROTECT) is a research question with the measurement that resolves its role. This pipeline never writes
`QUALIFIED`: qualification is a separate record (a P4-type package) that this code cannot produce, and `check_status` refuses any row whose
status is outside the closed vocabulary below. Compatible action of a context-free regulatory network is not a predicted benefit; an RNA change
is never read as target activity. Not medical advice.
"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, glob, gzip, importlib.util, json, os, re, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = HERE.parents[4]
IT10 = DR / "generation_it10_p1_20261031"
sys.path.insert(0, str(REPO / "framework/scripts"))

# ---- the status vocabulary: closed, and QUALIFIED is not in it -------------------------------------------------------------------------------------
STATUS_VOCAB = ("CONDITIONAL_H_HARM", "CONDITIONAL_H_PROTECT", "HYPOTHESIS_ROLE_SOURCED_NOT_QUALIFIED", "HELD_UNCERTAIN_ACTIVE_MOIETY",
                "DIAGNOSTIC_ONLY", "NOT_APPLICABLE", "CLOSED_AS_WRITTEN")
# CLOSED_AS_WRITTEN (P8-fix, IT21 verifier B4): a qualification record rejected the proposal in the form it was written. It is a CLOSED status, not a
# promotion: it names no qualification, and nothing in this module can move a row out of it or into a qualified state. A reopening is a new record.
FORBIDDEN_STATUS_WORDS = ("QUALIFIED", "KEEP", "RECOMMEND", "CANDIDATE_FOR_USE", "VALIDATED")


def load_dispose():
    spec = importlib.util.spec_from_file_location("dispose_it10", IT10 / "dispose_it10.py")
    m = importlib.util.module_from_spec(spec)
    saved, sys.argv = sys.argv, ["dispose_it10.py", "run"]      # the module prints its help and exits at import when called without arguments
    try:
        spec.loader.exec_module(m)
    finally:
        sys.argv = saved
    return m


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


SALTS = re.compile(r"\b(hydrochloride|hcl|sodium|potassium|mesylate|maleate|tartrate|citrate|sulfate|sulphate|acetate|phosphate|besylate|fumarate|succinate|bromide|chloride|calcium|dihydrate|monohydrate)\b", re.I)


def base_name(s):
    """Name with salt words removed: the key under which catalogue twins of one compound are counted once."""
    return norm(SALTS.sub("", s or ""))


def check_status(status):
    """The writer calls this on every row. A status outside the closed vocabulary, or one that names qualification, is refused."""
    if status not in STATUS_VOCAB or any(w in status.upper().replace("NOT_QUALIFIED", "") for w in FORBIDDEN_STATUS_WORDS):
        raise ValueError(f"status {status!r} is not allowed: this pipeline produces conditional hypotheses, never qualified candidates")
    return status


def proposal_status(disp, arm):
    """Status of a candidate row from the dispositions of dispose_it10 (which already encode the role of the question). Pure.
    A sourced role raises the priority of an arm; it does not qualify it."""
    if arm.startswith("flagged_") or disp == "HELD_UNCERTAIN_ACTIVE_MOIETY":
        return check_status("HELD_UNCERTAIN_ACTIVE_MOIETY")
    if disp.startswith("CONDITIONAL_IF_HARMFUL"):
        return check_status("CONDITIONAL_H_HARM")
    if disp.startswith("CONDITIONAL_IF_PROTECTIVE"):
        return check_status("CONDITIONAL_H_PROTECT")
    if disp in ("PRIMARY_RELIEVE", "PRIMARY_SUPPORT"):
        return check_status("HYPOTHESIS_ROLE_SOURCED_NOT_QUALIFIED")
    if disp == "NOT_APPLICABLE":
        return check_status("NOT_APPLICABLE")
    return check_status("DIAGNOSTIC_ONLY")


NO_BENEFIT_HYPOTHESIS = re.compile(r"\bno (sourced|stated)\b", re.I)


def arm_has_stated_benefit(role, hypothesis):
    """False for an arm whose own question_roles text says no benefit hypothesis is stated for it (Q4/Q6/Q7 mimics): kept, never handed over."""
    txt = role["h_harm_action"] if hypothesis == "H_HARM" else role["h_protect_action"]
    return not NO_BENEFIT_HYPOTHESIS.search(txt or "")


def rd(p, gz=False):
    with (gzip.open(p, "rt", encoding="utf-8") if gz or str(p).endswith(".gz") else open(p, encoding="utf-8")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def write_tsv(path, rows, cols=None):
    cols = cols or (list(rows[0]) if rows else [])
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in cols})


# ---- engine ------------------------------------------------------------------------------------------------------------------------------------------
def cmd_engine(a):
    out = Path(a.engine_dir)
    env = dict(os.environ)
    env.setdefault("LEGEND_CATALOG_CACHE", str(DR / "catalog" / "cache"))
    cmd = [sys.executable, "-B", str(IT10 / "engine_v4" / "run_v4.py"), "--out", str(out), "--actions", str(HERE / "results" / "actions"), "--reach"]
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(r.stdout[-2500:])
    if r.returncode:
        raise SystemExit(r.stderr[-1500:])


# ---- seed-specific lists: before (IT10 v4) and now ------------------------------------------------------------------------------------------------
def spec_rows(d):
    p = Path(d) / "v3_seed_specific_all_nulls.tsv"
    return {(r["seed_set"], r["arm"], r["family_id"]): r for r in rd(p)} if p.exists() else {}


def lost_pairs(diff_path):
    """family -> list of (gene, status) from the actions diff (guards on versus guards off)."""
    out = collections.defaultdict(list)
    for r in rd(diff_path):
        out[r["family_id"]].append((r["target_symbol"], r["status"]))
    return out


def classify_withdrawn(old_row, family_diff, withheld_by_family):
    """Why a row seed-specific in IT10 is not seed-specific now. Pure on its inputs."""
    chain = (old_row.get("edge_chain_main_target_to_seed_1") or "")
    main = chain.split(" ")[0].upper() if chain and not chain.startswith("hop0") else ""
    lost = {g.upper() for g, s in family_diff.get(old_row["family_id"], []) if s in ("lost", "sign_changed")}
    wh = withheld_by_family.get(old_row["family_id"], [])
    if main and main in lost:
        return "DIRECTION_WITHDRAWN_AT_MAIN_TARGET"
    if lost:
        return "DIRECTION_WITHDRAWN_AT_OTHER_TARGET_OF_THE_FAMILY"
    if wh:
        return "FAMILY_HAS_WITHHELD_ROWS_BUT_NO_SIGNED_PAIR_CHANGED"
    return "NO_ACTION_CHANGE_NULL_OR_SCORE_SHIFT"


def withheld_by_family(fam=None):
    """family id -> withheld rows, through the catalogue's own record-to-family map (a record id is not always its family id)."""
    import compound_catalog as cc
    import repurposing_search as rs
    fam = fam or rs.families(cc.load(DR / "catalog" / "catalog.jsonl.gz"))
    out = collections.defaultdict(list)
    for r in rd(HERE / "results" / "actions" / "withheld_rows.tsv.gz"):
        out[fam.get(r["record"], "FAM:" + r["record"])].append(r)
    return out


def withheld_reasons_at(family_rows, main):
    """Reason classes of the withheld rows of a family that name the main target gene (what withdrew the direction there)."""
    return ";".join(sorted({r["reason_class"] + "/" + r["target_level"] for r in family_rows if main and main.upper() in {g.upper() for g in r["genes"].split(";")}}))


def cmd_control(a):
    """Control: an engine run on the UNGUARDED rebuild (refresh_actions_it21.py run --guards off) must reproduce the IT10 seed-specific list; if it does not, the
    differences of the guarded run cannot be attributed to the guards. Writes results/control_reproduction.json."""
    old, ctl, new = spec_rows(IT10 / "results_v4"), spec_rows(a.control_dir), spec_rows(a.engine_dir)
    out = dict(it10_seed_specific=len(old), control_seed_specific=len(ctl), control_only=len(set(ctl) - set(old)), it10_only=len(set(old) - set(ctl)),
               identical_keys=set(old) == set(ctl), guarded_seed_specific=len(new), guarded_vs_control_lost=len(set(ctl) - set(new)), guarded_vs_control_gained=len(set(new) - set(ctl)))
    (HERE / "results" / "control_reproduction.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1, sort_keys=True))


def cmd_withdrawn(a):
    old = spec_rows(IT10 / "results_v4")
    new = spec_rows(a.engine_dir)
    diff = lost_pairs(HERE / "results" / "actions_diff_guards_on_vs_off.tsv")
    whf = withheld_by_family()
    new_names = {(k[0], k[1], base_name(r["name"])) for k, r in new.items()}
    lost, kept, gained = [], 0, []
    for k, r in old.items():
        if k in new:
            kept += 1
        else:
            lost.append(dict(question=r["question"], seed_set=r["seed_set"], arm=r["arm"], family_id=r["family_id"], name=r["name"],
                             z_total=r["Z_ind_robust_total_null"], z_indeg=r["Z_ind_robust_indeg_null"], z_adm=r["Z_ind_robust_adm_null"],
                             chain=(r["edge_chain_main_target_to_seed_1"] or "")[:80], cause=classify_withdrawn(r, diff, whf),
                             withheld_reasons_at_main_target=withheld_reasons_at(whf.get(r["family_id"], []), (r["edge_chain_main_target_to_seed_1"] or "").split(" ")[0]),
                             same_compound_still_seed_specific_in_a_twin_family="yes" if (k[0], k[1], base_name(r["name"])) in new_names else "no"))
    for k, r in new.items():
        if k not in old:
            gained.append(dict(question=r["question"], seed_set=r["seed_set"], arm=r["arm"], family_id=r["family_id"], name=r["name"],
                               z_total=r["Z_ind_robust_total_null"], chain=(r["edge_chain_main_target_to_seed_1"] or "")[:80],
                               cause="GAINED_BY_RERUN_NULL_OR_SIGN_CHANGE_NOT_A_FINDING"))
    write_tsv(HERE / "results" / "withdrawn_vs_it10.tsv", lost, ["question", "seed_set", "arm", "family_id", "name", "z_total", "z_indeg", "z_adm", "chain", "cause", "withheld_reasons_at_main_target", "same_compound_still_seed_specific_in_a_twin_family"])
    write_tsv(HERE / "results" / "gained_vs_it10.tsv", gained, ["question", "seed_set", "arm", "family_id", "name", "z_total", "chain", "cause"])
    by = collections.Counter((r["seed_set"], r["arm"], r["cause"]) for r in lost)
    summ = dict(it10_seed_specific=len(old), still_seed_specific=kept, withdrawn=len(lost), gained=len(gained),
                withdrawn_by_cause=dict(collections.Counter(r["cause"] for r in lost)),
                withdrawn_compounds_with_no_surviving_twin=sum(1 for r in lost if r["same_compound_still_seed_specific_in_a_twin_family"] == "no"),
                withdrawn_by_withheld_reason=dict(collections.Counter(r["withheld_reasons_at_main_target"] or "none" for r in lost)),
                withdrawn_by_set={f"{s}|{arm}": n for (s, arm), n in sorted(collections.Counter((r["seed_set"], r["arm"]) for r in lost).items())})
    (HERE / "results" / "withdrawn_summary.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summ, indent=1, sort_keys=True))



# ---- anchors: compounds the guards were written for and the phenotype-first interventions, before and after ----------------------------------------------
ANCHORS = ("bepridil", "terodiline", "suloctidil", "phloroglucinol", "ethosuximide", "vigabatrin", "lithium", "memantine", "roxadustat", "dichloroacetate")


def cmd_anchors(a):
    old_dir = DR / "generation_it9_p2_20261030" / "v3" / "results" / "actions"
    new_dir = HERE / "results" / "actions"
    rows = []
    def signed(d):
        out = collections.defaultdict(dict)
        for r in rd(d / "family_actions.tsv.gz"):
            out[r["family_id"]][r["target_symbol"]] = r["mean_sign"]
        return out
    so, sn = signed(old_dir), signed(new_dir)
    names = {r["family_id"]: r["name"] for r in rd(new_dir / "family_meta.tsv.gz")}
    anyt = collections.defaultdict(set)
    for r in rd(new_dir / "family_targets_any.tsv.gz"):
        anyt[r["family_id"]].add(r["target_symbol"])
    for f, nm in sorted(names.items(), key=lambda x: x[1].lower()):
        if any(base_name(nm).startswith(base_name(an)) for an in ANCHORS):
            o, n = so.get(f, {}), sn.get(f, {})
            if not o and not n and not anyt.get(f):
                continue
            rows.append(dict(family_id=f, name=nm, signed_targets_it9=len(o), signed_targets_now=len(n), any_action_targets=len(anyt.get(f, ())),
                             lost=";".join(sorted(set(o) - set(n)))[:120], kept_or_added=";".join(f"{g}({v})" for g, v in sorted(n.items()))[:120]))
    write_tsv(HERE / "results" / "anchors_it21.tsv", rows)
    print(len(rows), "anchor families")


def cmd_direct(a):
    """Direct-search rows (the compound's own target is a seed gene) that carried a direction in IT10 and carry none now: abstentions at the seed gene itself."""
    old = {}
    for f in glob.glob(str(IT10 / "results_v4" / "candidates_Q*.tsv")):
        for r in rd(f):
            if r["arm"] == "direct_search":
                old[(r["seed_set"], r["family_id"])] = r
    rows = []
    for f in sorted(glob.glob(str(Path(a.engine_dir) / "candidates_Q*.tsv"))):
        for r in rd(f):
            if r["arm"] != "direct_search":
                continue
            o = old.get((r["seed_set"], r["family_id"]))
            unsigned_now = r["compatible_action"].startswith("unsigned")
            signed_then = bool(o) and not o["compatible_action"].startswith("unsigned")
            if unsigned_now and signed_then:
                rows.append(dict(question=r["question"], seed_set=r["seed_set"], family_id=r["family_id"], name=r["name"], seed_gene_targets=r["contributing_seed_1"],
                                 action_it10=o["compatible_action"], action_now=r["compatible_action"], reading="direction withdrawn by the current guards; the association stays (unknown is not negative)"))
    write_tsv(HERE / "results" / "direct_search_direction_withdrawn_it21.tsv", rows, ["question", "seed_set", "family_id", "name", "seed_gene_targets", "action_it10", "action_now", "reading"])
    print(len(rows), "direct-search rows lost their direction")


# ---- novelty / earlier decisions --------------------------------------------------------------------------------------------------------------------
def earlier_decisions(include_p4a=False):
    """name -> (state, source file, label) from the IT9/IT10/IT11 qualification records and the ranking proposal maps.
    include_p4a (IT21 V1): also the IT21 P4a qualification records, a produced output that the hand-over did not consume (a rejected chain re-emitted under another member name
    of the same mechanism cluster was handed over as new)."""
    out = []
    rk = DR / "ranking_it8_p9_20261029"
    labels = {}
    for f in ("proposals_map.tsv", "proposals_map_it10.tsv", "proposals_map_it11.tsv"):
        for r in rd(rk / f):
            labels[r["cand_id"]] = r.get("label", "")
    for f in ("it9_records.tsv", "it10_records.tsv", "it11_records.tsv"):
        for r in rd(rk / f):
            out.append((r["compound"], r["state"], f"ranking_it8_p9_20261029/{f}#{r['cand_id']}", labels.get(r["cand_id"], "")))
    p4a = DR / "qualification_it21_p4a_20261103" / "qualification_it21_p4a.tsv"
    if include_p4a and p4a.exists():
        for r in rd(p4a):
            out.append((r["compound"], r["disposition"], f"qualification_it21_p4a_20261103/qualification_it21_p4a.tsv#{r['proposal_id']}", r.get("classification", "")[:60]))
    return out


def earlier_state(name, decisions):
    n = base_name(name)
    if len(n) < 4:
        return None
    for comp, state, src, label in decisions:
        c = base_name(comp)
        first = base_name(re.split(r"[ (]", comp.strip())[0]) if comp.strip() else ""
        if n == c or (len(n) >= 6 and n in c) or (len(first) >= 4 and first == n):      # V1: exact first-token match from 4 characters (IOX1 was missed at 6)
            return state, src, label
    return None


# ---- earlier threads: LEGEND's own earlier exclusion and candidate tables (P8-fix, IT21 verifier C4) --------------------------------------------------
# (relative path under DR, name column, id column, reason columns). Listed from the most to the least informative; the first thread found for a compound carries its reason.
EARLIER_THREAD_SOURCES = (
    ("exploration_it9_p3_20261030/excluded.tsv", "name", "parent", ("disposition", "selection_reason")),
    ("qualification_it9_p4c_d_20261030/excluded_selection_p4c_d.tsv", "name", "parent", ("disposition",)),
    ("exploration_it9_p3_20261030/selected.tsv", "name", "parent_chembl_id", ("legend_status",)),
    ("exploration_it9_p3_20261030/candidates_consolidated.tsv", "name", "parent", ("disposition", "selection_reason")),
    ("generation_it10_p1_20261031/results/deepening_candidates.tsv", "name", "", ("disposition", "rule")),
)


def thread_keys(name, ident=""):
    """Every key under which one compound can be found again: the hyphen/space/case-free name, the salt-free name, and the ChEMBL id."""
    ks = {norm(name), base_name(name)}
    m = re.search(r"CHEMBL\d+", (ident or "").upper())
    if m:
        ks.add(m.group(0).lower())
    return {k for k in ks if len(k) >= 4}


def load_earlier_threads(sources=EARLIER_THREAD_SOURCES, root=None):
    """key -> (source file, reason). First source wins. A missing file is skipped (the perimeter is then smaller, never invented)."""
    root = Path(root) if root else DR
    out = {}
    for rel, ncol, icol, rcols in sources:
        p = root / rel
        if not p.exists():
            continue
        for r in rd(p):
            reason = "; ".join(x for x in (r.get(c, "") for c in rcols) if x)
            for k in thread_keys(r.get(ncol, ""), r.get(icol, "") if icol else ""):
                out.setdefault(k, (rel, reason))
    return out


def earlier_thread(name, family_id, threads):
    """'source: reason' of an earlier LEGEND thread on this compound, or ''. Matches by name (hyphen variants, salts) and by the ChEMBL id of the family."""
    for k in sorted(thread_keys(name, family_id)):
        if k in threads:
            src, why = threads[k]
            return f"{src}: {why or 'listed'}"
    return ""


def intended_effect(hyp, seed_direction):
    """What the arm wants the compound to do to the seed readout, from the seed's OWN direction. H_HARM (arm 'opposes'): move the readout against the observed
    change; H_PROTECT (arm 'mimics'): move it with the observed change, a probe of the role question. Pure."""
    d = (seed_direction or "").lower()
    if d not in ("up", "down"):
        return "direction of the seed readout not stated in the row: the intended effect cannot be written"
    if hyp == "H_HARM":
        eff = "lowers" if d == "up" else "raises"
        return f"{eff} the seed-gene readout (the seed is {d} in the WWOX-deficient system and that change is assumed harmful)"
    eff = "raises or sustains" if d == "up" else "lowers"
    return (f"{eff} the seed-gene readout (the seed is {d}): a probe of the role question, a risk and not a benefit unless step 0 shows the seed change is protective")


def corpus_text():
    """Lower-cased text of the cards, packets, unit tables and proposal maps: a name found here is 'named in LEGEND material' (a perimeter, not a literature claim)."""
    parts = []
    for p in list((DR / "cards").glob("*.json")) + [DR / "ranking_it8_p9_20261029" / n for n in ("unit_members.tsv", "unit_inputs.tsv", "member_evidence.tsv", "proposals_map.tsv", "proposals_map_it10.tsv", "proposals_map_it11.tsv", "investigations_it20.tsv")]:
        if p.exists():
            parts.append(p.read_text(encoding="utf-8", errors="replace").lower())
    return "\n".join(parts)


def named_in_corpus(name, text):
    n = SALTS.sub("", (name or "").lower()).strip()
    return len(n) >= 4 and re.search(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])", text) is not None


# ---- selection rule for the hand-over (written here before the table is read) ------------------------------------------------------------------------
H5_NEW = "H5 one proposal per mechanism cluster = (question, hypothesis, main target), chosen by the order key (in this order: no cluster work already done, no limited seed support, main target not UNMEASURED, then more evidence origins, then the shorter admissible chain (fewer edges), then the LARGER smallest-|z|); an exact tie on the whole key is not broken by any science, the first row in table order is kept and the cluster export says how many eligible rows tied (tie_size); salt twins count once; "
H5_LEGACY = "H5 one proposal per mechanism cluster = (question, hypothesis, main target), chosen by number of evidence origins, then the shorter admissible chain (fewer edges), then the smallest |z|; salt twins count once; "   # the committed no-v1 (P2) tables keep this wording byte for byte
HANDOFF_RULE = (
    "H1 arm opposes or mimics, unflagged for active moiety, seed-specific under the three IT10 nulls AND the reach-matched null (same sign, |z| > 3 in all four); "
    "H2 identity resolved in the catalogue (ChEMBL id) and modality small_molecule; "
    "H3 the arm has a stated benefit hypothesis in question_roles.tsv (arms whose own text says 'no sourced/stated' benefit hypothesis are kept in proposals, never handed over); "
    "H4 not decided in an IT9/IT10/IT11 qualification record (those are carried with their state, not re-proposed); "
    "{H5}"
    "H6 at most 3 per (question, hypothesis); "
    "H7 a proposal whose only signed support at the main target is not a resolved assertion is not handed over (the signed pair must survive the refreshed guards, which is the case for every row of the refreshed table); "
    "H8 (IT22 P1: scoped; before, ANY member's decision vetoed the whole cluster) a decision about one member reaches another member only inside the scope its own reason supports "
    "(decision_scope_it22.tsv): a reason about the molecule (potency profile, label, artefact) stays with the molecule; a premise REFUTED for the arc (an edge or a target-in-context) "
    "blocks the members whose chain or main target carries that premise ('shared_premise_refuted'); an UNRESOLVED premise travels as a carried limit, never a veto; work already done "
    "demotes the cluster behind unworked ones and the hand-over says 'not a discovery'; a decision with no scope row keeps the old veto under its own label ('decision_scope_untagged')."
)
H8_NEW = (
    "H8 (IT22 P1: scoped; before, ANY member's decision vetoed the whole cluster) a decision about one member reaches another member only inside the scope its own reason supports "
    "(decision_scope_it22.tsv): a reason about the molecule (potency profile, label, artefact) stays with the molecule; a premise REFUTED for the arc (an edge or a target-in-context) "
    "blocks the members whose chain or main target carries that premise ('shared_premise_refuted'); an UNRESOLVED premise travels as a carried limit, never a veto; work already done "
    "demotes the cluster behind unworked ones and the hand-over says 'not a discovery'; a decision with no scope row keeps the old veto under its own label ('decision_scope_untagged')."
)
H8_LEGACY = (
    "H8 a mechanism cluster in which ANY member (eligible or not) has an IT9/IT10/IT11 qualification record is not handed over as new: it is listed in mechanism_clusters_it21.tsv with that record, "
    "because the earlier reason may have been about the compound and only the qualification can say so (unknown is not negative)."
)
REASON_LABELS = {"mechanism_cluster_selection": "H5/H6 diversification of the selection (one per cluster, three per question and hypothesis)",
                 "work_already_done": "an earlier qualification already worked this cluster: priority only, never a scientific verdict",
                 "shared_premise_refuted": "the premise that sank an earlier member is refuted for this arc and applies to this member",
                 "decision_scope_untagged": "an earlier decision with no recorded scope: the old cluster veto, kept until its reason is read"}
DECISION_SCOPE_TABLE = DR / "generation_it22_p1_20261103" / "decision_scope_it22.tsv"


def load_decision_scopes(path=None):
    """source id (the `#cand_id` pointer earlier_decisions() carries) -> [component dicts]."""
    out = collections.defaultdict(list)
    path = Path(path or DECISION_SCOPE_TABLE)
    if path.exists():
        for r in rd(path):
            out[r["decision_source"]].append(dict(scope=r["scope"], premise_key=r["premise_key"], note=r["basis"], questions=[q for q in (r.get("questions") or "").split(",") if q]))
    return out


def _premise_applies(key, p):
    """edge:A>B -> both genes appear in the chain in that order; target:GENE@Q -> same main target and question."""
    kind, _, val = key.partition(":")
    if kind == "edge":
        a, _, b = val.partition(">")
        return re.search(rf"\b{re.escape(a)}\b[^;]*?-> *{re.escape(b)}\b", p.get("chain", "") or "") is not None
    if kind == "target":
        g, _, q = val.partition("@")
        return p.get("main_target") == g and (not q or p.get("question") == q)
    return False


SUPPORT_LIMITING_GUARDS = {"NPY_SIGN_CONTESTED": "the NPY direction is contested by the mouse bulk and pooled-nuclei contrasts and by the neuron loss in the knockout organoid (cell-population sensitive)",
                           "SECOND_SYSTEM_PROGENITOR_GATE_FAILED": "the shWWOX hNPC (progenitor) library did not show WWOX lower (gate 1 failed; the neuron arm is lower but one noisy library), so it is not an independent second system for this seed",
                           "ADJUSTED_P_ABOVE_ALPHA": "the seed transcript change has an adjusted p above the deposit's own alpha (4 v 2 libraries)"}


def seed_guard_limits(p, sidx, ann=None):
    """IT22 P3: the guard tags of the P1 rows behind a proposal's two contributing seeds, and the support limits among them. Pure given sidx."""
    tags = set()
    for k in ("contributing_seed_1", "contributing_seed_2"):
        f = (p.get(k) or "").split("|")[0]
        if not f:
            continue
        for r in sidx.get((p["seed_set"], f"{p['seed_set']}:{f}"), []) or sidx.get((p["seed_set"], f), []):
            tags |= {t for t in (r.get("guard_tag") or "").split(";") if t}
            tags |= set((ann or {}).get(r["seed_id"], ()))
    return sorted(tags), [f"{t}: {SUPPORT_LIMITING_GUARDS[t]}" for t in sorted(tags) if t in SUPPORT_LIMITING_GUARDS]


def decision_effect(p, cluster_decisions, global_decisions=()):
    """What earlier decisions mean for p. Pure. cluster_decisions: decisions on OTHER members of p's mechanism cluster (compound/state/source/components); global_decisions: every decision with a
    scope, whatever its cluster (IT22 P8-fix F01: a premise or class limit about an EDGE or a TARGET applies wherever that edge or target is in a chain, not only inside one cluster).
    Scopes: molecule (stays with the molecule), premise_refuted / premise_contradicted (block), premise_unresolved / class_limit (carried limit), work_done (priority only, and only for the
    questions the decided record concerned; F03). Returns block (reason or ''), work_done, carried_limits."""
    block, work, limits = "", False, []
    for d in cluster_decisions:
        comps = d.get("components") or []
        if not comps:
            block = block or "decision_scope_untagged"
            continue
        for c in comps:
            if c["scope"] == "work_done" and (not c.get("questions") or p.get("question") in c["questions"]):
                work = True
    for d in list(cluster_decisions) + list(global_decisions):
        if base_name(d.get("compound", "")) == base_name(p.get("compound", "")):
            continue
        for c in d.get("components") or []:
            sc = c["scope"]
            if not _premise_applies(c.get("premise_key", ""), p):
                continue
            if sc in ("premise_refuted", "premise_contradicted"):
                block = f"shared_premise_{'refuted' if sc == 'premise_refuted' else 'contradicted'}: {c['premise_key']} ({d['compound']})"
            elif sc in ("premise_unresolved", "class_limit"):
                msg = f"{d['compound']} {d['state']}: {c['note']}"
                if msg not in limits:
                    limits.append(msg)
    return dict(block=block, work_done=work, carried_limits=limits)


MODALITY_DECL_FILE = Path(__file__).resolve().parent / "modality_declarations_it27.tsv"


def load_modality_declarations(path=None):
    """{family id: (from_modality, to_modality)} declared at structure level by a second actor (IT27: PX-478, a single amino acid that ChEMBL types 'Protein'). The modality filter is not loosened:
    a declaration applies only while the computed modality still equals its `from_modality`, so a stale or wrong row does nothing."""
    path = Path(path) if path else MODALITY_DECL_FILE
    if not path.exists():
        return {}
    with open(path, encoding="utf-8", newline="") as fh:
        return {r["family_id"]: (r["from_modality"], r["to_modality"]) for r in csv.DictReader(fh, delimiter="\t")}


R4_FILE = DR / "identity_gsrs_it26_a1_20261104" / "identity_r4_it26.tsv"


def load_identity_r4(path=None):
    """{family id: ChEMBL id} of the identity route R4 (G-SRS name -> UNII -> structure). Only rows a second actor confirmed at structure level are in the file;
    a weak (name-only) trial row is not. The route gives the generator an identity (has_chembl), never a merge of two families."""
    path = Path(path) if path else R4_FILE
    if not path.exists():
        return {}
    with open(path, encoding="utf-8", newline="") as fh:
        return {r["family_id"]: r["chembl_id"] for r in csv.DictReader(fh, delimiter="\t")}


def eligible(row, role, fam_meta, decisions):
    """(ok, reason). Pure given its inputs; the tests call it."""
    if row["arm"] not in ("opposes", "mimics"):
        return False, "arm_not_opposes_or_mimics"
    if str(row.get("seed_specific_all_three_nulls")) != "1":
        return False, "not_seed_specific_in_three_nulls"
    z = row.get("reach_z")
    sgn = 1 if row["arm"] == "opposes" else -1
    if z in (None, "") or float(z) * sgn <= 3:
        return False, "reach_null_not_confirming"
    m = fam_meta.get(row["family_id"], {})
    if m.get("has_chembl") != "1":
        return False, "identity_not_resolved"
    if m.get("modality") != "small_molecule":
        return False, f"modality_{m.get('modality') or 'unknown'}_not_small_molecule"
    if row.get("attribution_state") == "WEAK_ATTRIBUTION":      # IT21 V1: the listed main target is not where the compound acts (attribution_screen_it21.py)
        return False, "main_target_weak_attribution"
    hyp = "H_HARM" if row["arm"] == "opposes" else "H_PROTECT"
    if not arm_has_stated_benefit(role, hyp):
        return False, "arm_has_no_stated_benefit_hypothesis"
    if earlier_state(row["name"], decisions):
        return False, "decided_in_earlier_qualification_record"
    return True, ""


ROUTE_ATC = {"D": "dermatological (topical use is the usual route)", "S": "sensory organs (ophthalmic or otic use is the usual route)"}


def route_class_note(atc_codes):
    """IT22 reverse test G4: the ATC class names the usual route; a topical or local class says nothing about systemic or brain exposure. Empty when no ATC code or a systemic class."""
    classes = sorted({c[0] for c in atc_codes if c and c[0] in ROUTE_ATC})
    return "; ".join(f"ATC {c}: {ROUTE_ATC[c]}: systemic and brain exposure not established by the class" for c in classes)


def attribution_note(p):
    """One sentence for the qualifier: what the local Guide to Pharmacology release says about the main target of this compound (IT21 V1). Affinity, not occupancy or exposure."""
    st = p.get("attribution_state", "")
    via = (" Identity joined to its ChEMBL record through the ligand id in the claim name (" + p["identity_via"] + ")." if p.get("identity_via") else "")
    mixed = (f" Basis: {p['attribution_comparison_basis']}." if p.get("attribution_comparison_basis") else "") + (f" Note: {p['attribution_context_note']}." if p.get("attribution_context_note") else "")
    co = f" {p['attribution_copotent']} other target(s) measured within 10-fold of it in the same measure type: attribution is to a set of co-targets, not to one." if str(p.get("attribution_copotent") or "0") not in ("", "0") else ""
    mixed = mixed + co
    if st == "ATTRIBUTABLE":
        return f"main target {p['main_target']} measured at {p['attribution_main_nm']} nM; best measured target {p['attribution_best_target']} at {p['attribution_best_nm']} nM ({p['attribution_fold']}-fold).{via}{mixed}"
    if st == "SINGLE_MEASURED_TARGET":
        return f"main target {p['main_target']} measured at {p['attribution_main_nm']} nM and it is the only measured target: no comparison is possible (not attributable by comparison; unknown, not negative).{via}{mixed}"
    if st == "BORDERLINE_POTENT_MAIN_TARGET":
        return (f"BORDERLINE: main target {p['main_target']} measured at {p['attribution_main_nm']} nM (potent, at or below {AS_POTENT_NM:g} nM) although {p['attribution_fold']}-fold weaker than the best "
                f"measured target {p['attribution_best_target']} ({p['attribution_best_nm']} nM): relative weakness only, not blocked; check that the chain's cell type expresses {p['main_target']}.{via}{mixed}")
    if st == "UNMEASURED_AT_MAIN_TARGET":
        return (f"UNMEASURED AT MAIN TARGET (ranked after measured rows in the cap): no measured affinity for {p['main_target']}; the compound is measured on other targets, best "
                f"{p['attribution_best_target']} at {p['attribution_best_nm']} nM: the listed target may not be the main action (annotation only).{via}{mixed}")
    if st == "SECONDARY_ACTIVITY_MEASURED":
        return (f"SECONDARY ACTIVITY: main target {p['main_target']} measured at {p['attribution_main_nm']} nM, {p['attribution_fold']}-fold weaker than {p['attribution_best_target']} "
                f"({p['attribution_best_nm']} nM) in the same measure type: a measured secondary action, kept; the experiment needs an on-target control because the more potent target co-acts (potency in vitro, not exposure).{via}{mixed}")
    if st == "NOT_COMPARABLE_MEASURES":
        return (f"NOT COMPARABLE: the local release has values for this compound but none of the same measure type at {p['main_target']} and at another target, so no ratio is formed and no quantitative exclusion follows "
                f"(values: {p.get('attribution_values_kept', '')[:200]}).{via}{mixed}")
    if st == "NOT_ASSESSABLE":
        return "no ligand or no affinity in the local Guide to Pharmacology release: attribution not assessed (unknown, not negative)." + via
    return (f"WEAK: main target {p['main_target']} at {p['attribution_main_nm']} nM (above {AS_SECONDARY_NM:g} nM), {p['attribution_fold']}-fold weaker than {p['attribution_best_target']} in the same measure type: "
            f"potency alone does not support attributing the effect to the listed target; not a statement that the compound is inactive there.{via}{mixed}")


AS_SECONDARY_NM = 1000.0   # mirrors attribution_screen_it21.SECONDARY_MAIN_NM
AS_POTENT_NM = 100.0     # mirrors attribution_screen_it21.POTENT_MAIN_NM (a unit test asserts they agree)


def order_key(r):
    """IT21 V1-fix: a row whose main target is UNMEASURED (measured elsewhere) ranks after every other row; then more independent origins first, then the shorter admissible chain, then the larger smallest-|z| (a null-relative score, last on purpose)."""
    return (1 if r.get("cluster_work_done") == "yes" else 0, 1 if r.get("seed_support_limited") == "yes" else 0, 1 if r.get("attribution_state") == "UNMEASURED_AT_MAIN_TARGET" else 0, -int(r["n_origins"] or 0), int(r.get("chain_edges") or 99), -float(r["zmin"]))


def select_handoff(rows, per_group=3):
    """rows: eligible rows with keys question, hypothesis, main_target, n_origins, zmin, name. One per mechanism cluster, <= per_group per (question, hypothesis)."""
    best = {}
    for r in rows:
        k = (r["question"], r["hypothesis"], r["main_target"])
        if k not in best or order_key(r) < order_key(best[k]):
            best[k] = r
    out, count = [], collections.Counter()
    for r in sorted(best.values(), key=lambda r: (r["question"], r["hypothesis"]) + order_key(r)):
        g = (r["question"], r["hypothesis"])
        if count[g] < per_group:
            out.append(r)
            count[g] += 1
    return out


def tie_size(members):
    """Eligible rows of a cluster that share the best order_key with the representative (1 = no tie; 0 = nothing eligible). Informational: the rule is unchanged."""
    keys = [order_key(x) for x in members if x["handoff_eligible"] == "yes"]
    return keys.count(min(keys)) if keys else 0


def assertion_counts(entries_idx, family, gene, rs):
    """Distinct underlying assertions (one origin counts once) behind the signed support of a family at a gene: (n_rows, n_assertions, sources)."""
    idx, fam = entries_idx
    rows, keys, srcs = 0, set(), set()
    for e in idx.members.get(family, []):
        for t in e["targets"]:
            src = t["source"]
            genes = [g.upper() for g in (t.get("gene_symbols") or [])] if src.startswith("ChEMBL") else [(t.get("gene") or "").upper()]
            if gene.upper() not in genes:
                continue
            raw = t.get("action_type") if src.startswith("ChEMBL") else t.get("interaction_type")
            if rs.action_direction(raw) not in ("up", "down"):
                continue
            prov = rs.claim_provenance(e, t, idx.artefacts)
            rows += 1
            keys.add(rs.assertion_key(e, src, t, prov))
            srcs.add(("ChEMBL" if src.startswith("ChEMBL") else "DGIdb/" + (t.get("claim_source") or "?")))
    return rows, len(keys), ";".join(sorted(srcs))


def assign_ids(proposals, previous_path):
    """Proposal ids are stable across a re-run (P8-fix): a row already numbered in the previous table keeps its id (qualification records cite them); a new row takes the
    next free number, in the order of the original rule; a row that disappeared leaves a gap. On a first run this is the original contiguous numbering."""
    keyed = lambda p: (p["seed_set"], p["hypothesis"], p["family_id"])
    prev = {}
    if Path(previous_path).exists():
        prev = {keyed(r): r["proposal_id"] for r in rd(previous_path)}
    order = sorted(proposals, key=lambda p: (p["question"], p["hypothesis"], -float(p["zmin"])))
    used = {prev[keyed(p)] for p in proposals if keyed(p) in prev}
    nxt = max([int(i.split("-")[1]) for i in prev.values()] + [0]) + 1 if prev else 1
    for p in order:
        if keyed(p) in prev:
            p["proposal_id"] = prev[keyed(p)]
        else:
            p["proposal_id"] = f"IT21P2-{nxt:04d}"
            nxt += 1
    assert len({p["proposal_id"] for p in proposals}) == len(proposals)


def cmd_propose(a):
    D = load_dispose()
    import compound_catalog as cc
    import repurposing_search as rs
    R = HERE / "results"
    OUT = Path(a.out_dir) if a.out_dir else R          # reads stay on R (actions, previous ids); writes go to OUT
    OUT.mkdir(parents=True, exist_ok=True)
    eng = Path(a.engine_dir)
    # dispositions through the existing function; reach z replaced by the reach run of THIS engine directory
    P1D = Path(a.p1_inputs) if getattr(a, "p1_inputs", "") else None       # IT22: an amended seed/question/role set (seeds.tsv, questions.tsv, question_roles.tsv, seeds_p1/)
    rows_out, n_by, it9 = D.build(eng, DR, P1D)
    cols = D.COLS
    ix = {c: cols.index(c) for c in cols}
    reach, reach_act = {}, {}
    for pr in glob.glob(str(eng / "proposals_p1_*_reach.tsv.gz")):
        sn = os.path.basename(pr)[len("proposals_p1_"):-len(".tsv.gz")][:-len("_reach")]
        reach[sn] = {r["family_id"]: float(r["Z_ind_robust"]) for r in rd(pr)}
        reach_act[sn] = {r["family_id"]: r["compatible_action"] for r in rd(pr)}
    disp = {}
    for q, rws in rows_out.items():
        for r in rws:
            d = {c: r[ix[c]] for c in cols}
            d["reach_z"] = reach.get(d["seed_set"], {}).get(d["family_id"], "")
            disp[(d["seed_set"], d["arm"], d["family_id"])] = d
    roles = D.load_roles((P1D / "question_roles.tsv") if P1D else IT10 / "question_roles.tsv")
    meta = {r["family_id"]: r for r in rd(R / "actions" / "family_meta.tsv.gz")}
    entries = cc.load(DR / "catalog" / "catalog.jsonl.gz")
    fam = rs.families(entries)
    idx = rs.Index(entries, rs.load_artefacts(), rs.module_intervention_symbols(rs.load_needs()["needs"]))
    modality = {}
    status_of, phase_of = {}, {}
    atc_of = collections.defaultdict(set)
    for e in entries:
        f = fam[e["id"]]
        atc_of[f] |= set(e.get("atc") or [])
        if (e.get("ids") or {}).get("chembl") or f not in modality:
            modality[f] = e.get("modality")
        sc = e.get("status_class")
        if f not in status_of or sc in ("approved_any_source", "clinical_candidate"):
            status_of[f] = sc
        for s in e.get("status_records") or []:
            if s.get("source") == "ChEMBL" and s.get("max_phase") is not None:
                phase_of[f] = max(phase_of.get(f, -1), s["max_phase"])
    v1 = not a.no_v1
    fb, fl, aff, kinds_ = {}, {}, {}, {}
    if v1:      # IT21 V1: identity bridge (claim-name ligand id) and attribution screen; both read data the repository already holds
        import attribution_screen_it21 as AS
        lig_, aff, kinds_ = AS.load_gtopdb_affinities()
        bridges = AS.bridge_claim_name_ligands(entries)
        fb = AS.family_bridge(bridges, fam)
        fl = AS.family_ligands(entries, fam, bridges, lig_)
        for f, tgt in fb.items():
            if f in meta:
                modality[f] = modality.get(tgt) or modality.get(f)       # the substance is the ChEMBL record's: its modality is that record's
    r4 = load_identity_r4() if v1 else {}
    modality_decl = load_modality_declarations() if v1 else {}
    for f_, c_ in r4.items():       # IT28: an R4 identity (structure-level, second actor) also carries the measures of the ChEMBL record's family, as the claim-name bridge already does
        if f_ in meta and f_ not in fb:
            fl[f_] = set(fl.get(f_, set())) | set(fl.get("FAM:CAT:" + c_, set()))
    for f, m in meta.items():
        if f in r4 and f not in fb and m.get("has_chembl") != "1":      # IT26: route R4 (G-SRS name -> UNII -> structure, verified by a second actor), the family's own record has no ChEMBL id
            modality[f] = modality.get("FAM:CAT:" + r4[f]) or modality.get(f)
        decl = modality_decl.get(f)
        if decl and modality.get(f) == decl[0]:
            modality[f] = decl[1]
        m["modality"] = modality.get(f)
        if v1 and f in fb and m.get("has_chembl") != "1":
            m["has_chembl"], m["identity_via"] = "1", "gtopdb_ligand_claim_name->" + fb[f]
        elif f in r4 and m.get("has_chembl") != "1":
            m["has_chembl"], m["identity_via"] = "1", "gsrs_unii_structure->" + r4[f]
    decisions = earlier_decisions(include_p4a=v1)
    text = corpus_text()
    threads = load_earlier_threads()
    signed = collections.defaultdict(dict)
    for r in rd(R / "actions" / "family_actions.tsv.gz"):
        signed[r["family_id"]][r["target_symbol"].upper()] = r
    withheld = withheld_by_family(fam)
    p1 = rd((P1D or DR / "generation_it9_p1_20261030") / "seeds.tsv")
    sidx = D.load_seed_index(str((P1D / "seeds_p1") if P1D else DR / "generation_it9_p2_20261030" / "seeds_p1"), p1)
    questions = {r["question_id"]: r for r in rd((P1D or DR / "generation_it9_p1_20261030") / "questions.tsv")}
    spec = rd(eng / "v3_seed_specific_all_nulls.tsv")
    contrib = {}

    def contribs(sn, fid):
        if sn not in contrib:
            cc_ = collections.defaultdict(list)
            for c in rd(eng / f"contributions_p1_{sn}.tsv.gz"):
                cc_[c["family_id"]].append(c)
            contrib[sn] = cc_
        return sorted(contrib[sn].get(fid, []), key=lambda c: -abs(float(c["contrib_total"])))

    proposals, elig_rows = [], []
    for s in spec:
        key = (s["seed_set"], s["arm"], s["family_id"])
        d = disp.get(key)
        if d is None:                         # seed-specific but outside the top-N disposition tables: disposition computed here by the same function
            role = roles[s["question"]]
            hyp, dis = D.disposition(s["arm"], role)
            d = dict(question=s["question"], seed_set=s["seed_set"], arm=s["arm"], family_id=s["family_id"], name=s["name"], hypothesis=hyp, disposition=dis,
                     role_status=role["role_status"], resolving_measure=role["resolving_measure"], n_origins="", n_seed_rows="", origin_note="", chain_status=s["edge_chain_main_target_to_seed_1"],
                     chain_note="", top_seed_share="", contrary_seed_share="", reach_z=reach.get(s["seed_set"], {}).get(s["family_id"], ""), it9_state="", reconcile="", use_scope="", evaluation_forbidden_on=s["evaluation_forbidden_on"])
            cs = contribs(s["seed_set"], s["family_id"])
            mx = max((abs(float(c["contrib_total"])) for c in cs), default=0) or 1.0
            keep = [c for c in cs if abs(float(c["contrib_total"])) >= 0.1 * mx]
            nrows, norig, note = D.contributing_origins(keep, sidx, s["seed_set"], frac=0.0) if keep else (0, 0, "")
            d.update(n_seed_rows=nrows, n_origins=norig, origin_note=note)
        role = roles[s["question"]]
        zs = [float(s["Z_ind_robust_total_null"]), float(s["Z_ind_robust_indeg_null"] or 0), float(s["Z_ind_robust_adm_null"] or 0)]
        sgn = 1 if s["arm"] == "opposes" else -1
        rz = d["reach_z"]
        zmin = min([sgn * z for z in zs] + ([sgn * float(rz)] if rz != "" else []))
        chain = s["edge_chain_main_target_to_seed_1"] or ""
        main = s["contributing_seed_1"].split("|")[4] if s["contributing_seed_1"] and len(s["contributing_seed_1"].split("|")) > 4 else (chain.split(" ")[0] if chain else "")
        att = None
        if v1:
            import attribution_screen_it21 as AS
            att = AS.attribution(fl.get(s["family_id"], set()), main, aff, kinds_)
        d2 = dict(d, seed_specific_all_three_nulls=s["seed_specific_all_three_nulls"], attribution_state=(att or {}).get("state", ""))
        ok, why = eligible(d2, role, meta, decisions)
        hyp = "H_HARM" if s["arm"] == "opposes" else "H_PROTECT"
        status = proposal_status(d["disposition"], s["arm"])
        dec = earlier_state(s["name"], decisions)
        proposals.append(dict(
            proposal_id="", question=s["question"], seed_set=s["seed_set"], hypothesis=hyp, status=status, qualified="no",
            compound=s["name"], family_id=s["family_id"], base_name=base_name(s["name"]), main_target=main,
            z_total=zs[0], z_indeg=zs[1], z_adm=zs[2], z_reach=rz, zmin=round(zmin, 2), n_origins=d["n_origins"], n_seed_rows=d["n_seed_rows"], origin_note=d["origin_note"],
            chain=chain[:140], chain_status=d.get("chain_note", ""), top_seed_share=d.get("top_seed_share", ""), contrary_seed_share=d.get("contrary_seed_share", ""),
            contributing_seed_1=s["contributing_seed_1"], contributing_seed_2=s["contributing_seed_2"],
            readout_level="expression" if "expression" in s["seed_set"] else s["seed_set"].split("_")[1],
            has_chembl=meta.get(s["family_id"], {}).get("has_chembl", ""), modality=meta.get(s["family_id"], {}).get("modality") or "",
            status_class=status_of.get(s["family_id"], ""), max_phase=phase_of.get(s["family_id"], ""),
            chain_edges=chain.count("->"), earlier_decision=(f"{dec[0]} ({dec[1]})" if dec else ""), earlier_thread=earlier_thread(s["name"], s["family_id"], threads),
            named_in_legend_material="yes" if (named_in_corpus(s["name"], text) or earlier_thread(s["name"], s["family_id"], threads)) else "no",
            target_named_in_legend_material="yes" if named_in_corpus(main, text) else "no",
            handoff_eligible="yes" if ok else "no", handoff_blocker=why, evaluation_forbidden_on=s["evaluation_forbidden_on"]))
        if v1:
            sib = fb.get(s["family_id"]) or next((t for t, c_ in fb.items() if c_ == s["family_id"]), "")
            proposals[-1].update(identity_via=meta.get(s["family_id"], {}).get("identity_via", ""), attribution_state=att["state"], attribution_fold=att["fold"],
                                 attribution_best_target=att["best_target"], attribution_best_nm=att["best_nm"], attribution_main_nm=att["main_nm"],
                                 attribution_main_measure=att["main_measure"], attribution_best_measure=att["best_measure"], attribution_mixed_measure=att["mixed_measure"], attribution_comparison_basis=att["comparison_basis"], attribution_context_note=att["context_note"], attribution_copotent=att.get("n_copotent", ""), attribution_values_kept=att["values_kept"][:400],
                                 max_phase_source="own" if proposals[-1]["max_phase"] != "" else ("sibling_family" if sib and phase_of.get(sib, "") != "" else ""),
                                 sibling_family=sib, sibling_z_reach=reach.get(s["seed_set"], {}).get(sib, "") if sib else "",
                                 sibling_compatible_action=reach_act.get(s["seed_set"], {}).get(sib, "") if sib else "")
        if v1 and proposals[-1].get("max_phase_source") == "sibling_family":      # IT25 (IT24 reverse-test F2): a blank phase is read from the sibling family the identity bridge names, and says so
            proposals[-1]["max_phase"] = phase_of[sib]
        if ok:
            elig_rows.append(proposals[-1])
    assign_ids(proposals, R / "proposals_it21.tsv")
    # H8 (IT22 P1): an earlier decision on a cluster member reaches another member only inside its own scope
    scopes = load_decision_scopes() if v1 else {}
    global_dec, seen_src = [], set()
    for comp_, st_, src_, lab_ in decisions:
        if src_ in scopes and src_ not in seen_src:
            seen_src.add(src_)
            global_dec.append(dict(compound=comp_, state=st_, source=src_, components=scopes[src_]))
    conflicts = rd(DR / "generation_it22_p1_20261103" / "data_conflicts_it22.tsv") if (DR / "generation_it22_p1_20261103" / "data_conflicts_it22.tsv").exists() and v1 else []
    harm_f = DR / "relations_it23_p2_20261103" / "harm_signals_it23.tsv"          # IT23 P2: FAERS seizure-related reports from EC-KG (id join), carried as a limit
    harm = {}
    if v1 and harm_f.exists():
        for r_ in rd(harm_f):
            harm.setdefault(r_["family_id"], r_)
    seed_ann = collections.defaultdict(set)
    if P1D and (P1D / "seed_annotations.tsv").exists():
        for r_ in rd(P1D / "seed_annotations.tsv"):
            seed_ann[r_["seed_id"]].add(r_["annotation"])
    cl_dec, cl_str = collections.defaultdict(list), collections.defaultdict(list)
    for p in proposals:
        dec = earlier_state(p["compound"], decisions)
        if dec:
            k = (p["question"], p["hypothesis"], p["main_target"])
            cl_str[k].append(f"{p['compound']}: {p['earlier_decision']}")
            cl_dec[k].append(dict(compound=p["compound"], state=dec[0], source=dec[1], components=scopes.get(dec[1], [])))
    for p in proposals:
        k = (p["question"], p["hypothesis"], p["main_target"])
        p["cluster_earlier_decisions"] = " | ".join(sorted(set(cl_str.get(k, []))))[:300]
        p["cluster_work_done"], p["carried_limits"], p["blocker_detail"] = "", "", ""
        sg, sl = seed_guard_limits(p, sidx, seed_ann) if v1 else ([], [])
        p["seed_guards"], p["seed_support_limited"] = ";".join(sg), "yes" if sl else ""
        if sl:
            p["carried_limits"] = " | ".join(sl)
        hs = harm.get(p["family_id"])
        p["harm_signal_faers_seizure"] = "yes" if hs else ""
        if hs:                                       # a counter-evidence limit for a seizure disorder, never a verdict: reports are associations and may reflect the indication
            p["carried_limits"] = " | ".join(([p["carried_limits"]] if p["carried_limits"] else []) + [f"FAERS_SEIZURE_REPORTS: spontaneous reports of {hs['events']} (association, not causation; " + ("an antiseizure drug (ATC N03): the reports mainly reflect its indication; " if any(c_.startswith("N03") for c_ in atc_of.get(p["family_id"], ())) else "confounded by indication; ") + f"{hs['completeness']}; absence would not mean safety)"])
        cf = [r_["note"] for r_ in conflicts if base_name(r_["compound"]) == base_name(p["compound"]) and (not r_["main_target"] or r_["main_target"] == p["main_target"])]
        if cf:                                       # IT22 P8-fix F07: two sources disagree about a measured value; the disagreement stays visible
            p["carried_limits"] = " | ".join(([p["carried_limits"]] if p["carried_limits"] else []) + ["SOURCE_CONFLICT: " + x for x in cf])
        if not p["cluster_earlier_decisions"] and not (v1 and global_dec):
            continue
        if not v1:                                    # legacy P2 behaviour, kept so --no-v1 reproduces the committed P2 byte for byte
            if p["handoff_eligible"] == "yes":
                p["handoff_eligible"], p["handoff_blocker"] = "no", "mechanism_cluster_examined_earlier"
            continue
        others = [d for d in cl_dec.get(k, []) if base_name(d["compound"]) != base_name(p["compound"])]
        eff = decision_effect(p, others, global_dec)
        p["cluster_work_done"] = "yes" if eff["work_done"] else ""
        p["carried_limits"] = " | ".join(([p["carried_limits"]] if p["carried_limits"] else []) + eff["carried_limits"])[:1600]
        if p["handoff_eligible"] == "yes" and eff["block"]:
            p["handoff_eligible"], p["handoff_blocker"] = "no", eff["block"].split(":")[0] if eff["block"].startswith("shared") else eff["block"]
            p["blocker_detail"] = eff["block"]
    elig_rows = [p for p in proposals if p["handoff_eligible"] == "yes"]
    handed = select_handoff(elig_rows)
    hid = {p["proposal_id"] for p in handed}
    # attribution for the handed-over proposals
    direct_hits = {}                                            # IT22 reverse test G1: signed hits ON the seed gene itself are executed (diagnostic arm) and were never shown beside the hand-over
    for (sset, arm_, fid_), d_ in disp.items():
        if arm_ == "direct_search" and meta.get(fid_, {}).get("modality") == "small_molecule" and (phase_of.get(fid_, -1) >= 3 or earlier_state(d_["name"], decisions)):
            direct_hits.setdefault(sset, []).append((d_["name"], phase_of.get(fid_, -1)))
    direct_hits = {k: "; ".join(f"{n} (phase {ph:g})" for n, ph in sorted(set(v), key=lambda x: (-x[1], x[0]))[:6]) + " - diagnostic only: acts on the seed gene itself, not through the chain" for k, v in direct_hits.items()}
    handoff = []
    for p in sorted(handed, key=lambda p: (p["question"], p["hypothesis"], -float(p["zmin"]))):
        q, hyp, role = p["question"], p["hypothesis"], roles[p["question"]]
        cs = contribs(p["seed_set"], p["family_id"])[:2]
        seeds_txt = []
        for c in cs:
            for sr in sidx.get((p["seed_set"], c["seed_id"]), []):
                seeds_txt.append(f"{sr['seed_id']} {sr['entity_symbol'] or sr['process_id']} {sr['direction']} ({sr['level']}, {sr['species_observed']}, tier {sr['context_tier']}; {sr['source_locator'][:60]})")
        act = signed[p["family_id"]].get(p["main_target"].upper())
        n_rows, n_assert, srcs = assertion_counts((idx, fam), p["family_id"], p["main_target"], rs) if act else (0, 0, "")
        alts = [x for x in proposals if x["question"] == q and x["hypothesis"] == hyp and x["main_target"] == p["main_target"] and x["base_name"] != p["base_name"]]
        alt_names = sorted({x["base_name"].lower(): x["compound"] for x in alts}.values()) if v1 else sorted({x["compound"] for x in alts})
        rivals = [x for x in proposals if x["question"] == q and x["hypothesis"] == hyp and x["main_target"] != p["main_target"] and x["handoff_eligible"] == "yes" and x["proposal_id"] not in hid]
        wh = withheld.get(p["family_id"], [])
        benefit = role["h_harm_action"] if hyp == "H_HARM" else role["h_protect_action"]
        action = ("inhibits/lowers" if act and float(act["mean_sign"]) < 0 else "activates/raises" if act else "unresolved")
        experiment = (f"Step 0 (resolves the role; no compound): {role['resolving_measure'][:200]}. Step 1 (only if step 0 supports the role assumed here): {p['compound']} versus vehicle in the "
                      f"WWOX-deficient neural system and its corrected/control counterpart, with a genetic perturbation of {p['main_target']} as the on-target control; readout: "
                      f"{', '.join(sorted({c['gene'] for c in cs}))} at the same level as the seed ({p['readout_level']}) plus the question's functional endpoint. "
                      f"Discriminates: the effect must track {p['main_target']} and must go in the direction the role assumes; no change, or a change toward the disease direction, falsifies this arm.")
        handoff.append(dict(
            proposal_id=p["proposal_id"], status=p["status"], qualified="no (needs a P4-type qualification record)", question=q, hypothesis=hyp, compound=p["compound"], family_id=p["family_id"],
            action_on_main_target=f"{action} {p['main_target']} (mean sign {act['mean_sign'] if act else 'n/a'}; {n_rows} signed row(s) = {n_assert} distinct assertion(s); sources {srcs or 'n/a'}; flags {(act or {}).get('flags') or 'none'})",
            mechanism_path=p["chain"], seed_generated_by="; ".join(seeds_txt) or p["contributing_seed_1"], seed_level=p["readout_level"],
            origins=f"{p['n_origins']} origin(s): {p['origin_note']}", assumption=f"role of the observed change = {role['role_status']} (no source: {role['role_basis']}); {benefit[:230]}",
            hypothesised_benefit=benefit[:260], discriminating_experiment=experiment,
            alternatives_same_mechanism=("; ".join(alt_names[:6]) + (f" (+{len(alt_names) - 6})" if len(alt_names) > 6 else "")) or "none seed-specific at this main target",
            rival_mechanism_clusters_not_handed_over=len({x["main_target"] for x in rivals}),
            rival_explanations=(questions[q]["falsifiers_or_irrelevance_conditions"] or "")[:260],
            negatives_and_limits=f"contrary seed share {p['contrary_seed_share'] or 'n/a'}; z total/indeg/adm/reach {p['z_total']}/{p['z_indeg']}/{p['z_adm']}/{p['z_reach']}; chain of {p['chain_edges']} edge(s); modality {p['modality']}; phase {p['max_phase']}; status {p['status_class']}"
                               + ("; TOOL COMPOUND: selectivity and exposure not assessed here, the single listed target may not be the only action" if p["status_class"] == "tool_probe" else "")
                               + f"; dev limits: {D.dev_scope(p['compound'], rd(IT10 / 'dev_constraints.tsv'))}; the seed is {p['readout_level']}-level, so a change there is not a change in target activity or function",
            intended_effect_on_seed_readout=intended_effect(hyp, (p["contributing_seed_1"].split("|") + ["", "", ""])[2]),
            target_axis_named_in_legend_material=p["target_named_in_legend_material"],
            abstentions=(f"{len(wh)} withheld row(s) on this record ({collections.Counter(r['reason_class'] for r in wh).most_common(1)[0][0]})" if wh else "none on this record"),
            earlier_thread=p["earlier_thread"],
            carried_limits_from_cluster=p.get("carried_limits", ""), seed_guards=p.get("seed_guards", ""),
            route_class_note=route_class_note(atc_of.get(p["family_id"], ())),
            direct_acting_hits_same_set=direct_hits.get(p["seed_set"], ""),
            cluster_work_done=("an earlier qualification already worked this cluster (" + p["cluster_earlier_decisions"][:120] + "); this molecule was not assessed there: priority was lowered, and it is not a discovery") if p.get("cluster_work_done") else "",
            **({"attribution_state": p["attribution_state"], "attribution_note": attribution_note(p)} if "attribution_state" in p else {}),
            novelty_perimeter=(("earlier LEGEND thread (" + p["earlier_thread"] + ")") if p["earlier_thread"] else "named in LEGEND cards/units" if p["named_in_legend_material"] == "yes" else
                               "not named in LEGEND cards, units, earlier exclusion lists or IT9/IT10 candidate lists (perimeter of this module only, not a literature claim)"),
            evaluation_forbidden_on=p["evaluation_forbidden_on"]))
    for h in handoff:
        check_status(h["status"])
    for p in proposals:
        check_status(p["status"])
    if not v1:                       # --no-v1 must reproduce the committed P2 tables byte for byte: the IT22 columns exist only on the production path
        it22_cols = ("harm_signal_faers_seizure", "cluster_work_done", "carried_limits", "blocker_detail", "seed_guards", "seed_support_limited", "carried_limits_from_cluster", "route_class_note", "direct_acting_hits_same_set")
        for row_ in proposals + handoff:
            for k_ in it22_cols:
                row_.pop(k_, None)
    write_tsv(OUT / "proposals_it21.tsv", sorted(proposals, key=lambda p: p["proposal_id"]))
    write_tsv(OUT / "handoff_it21.tsv", handoff)
    carried = [p for p in proposals if p["earlier_decision"]]
    write_tsv(OUT / "carried_prior_decisions.tsv", carried, ["proposal_id", "question", "hypothesis", "compound", "earlier_decision", "main_target", "zmin", "n_origins"])
    # cluster map: every mechanism cluster with its members (alternatives), handed or not
    cl = collections.defaultdict(list)
    for p in proposals:
        cl[(p["question"], p["hypothesis"], p["main_target"])].append(p)
    write_tsv(OUT / "mechanism_clusters_it21.tsv", [dict(question=k[0], hypothesis=k[1], main_target=k[2], n_families=len(v), n_base_names=len({x["base_name"] for x in v}),
                                                         n_eligible=sum(1 for x in v if x["handoff_eligible"] == "yes"), **({"tie_size": tie_size(v)} if v1 else {}), handed_over=sum(1 for x in v if x["proposal_id"] in hid),
                                                         target_named_in_legend_material=v[0]["target_named_in_legend_material"], earlier_decisions_in_cluster=v[0]["cluster_earlier_decisions"],
                                                         examples="; ".join(sorted({x["compound"] for x in v})[:6])) for k, v in sorted(cl.items())])
    blockers = collections.Counter(p["handoff_blocker"] or "ELIGIBLE" for p in proposals)
    summ = dict(seed_specific_rows=len(proposals), by_status=dict(collections.Counter(p["status"] for p in proposals)), eligible=len(elig_rows), handed_over=len(handoff),
                blockers=dict(blockers), mechanism_clusters=len(cl), carried_prior_decisions=len(carried),
                handed_over_ids=[h["proposal_id"] for h in handoff], dispositions={f"{q}|{arm}|{d}": n for (q, arm, d), n in sorted(n_by.items())},
                selection_rule=(HANDOFF_RULE.replace("{H5}", H5_NEW) if v1 else HANDOFF_RULE.replace("{H5}", H5_LEGACY).replace(H8_NEW, H8_LEGACY)))
    (OUT / "summary_it21.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in summ.items() if k != "selection_rule"}, indent=1, sort_keys=True))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["engine", "withdrawn", "propose", "anchors", "direct", "control", "all"])
    ap.add_argument("--control-dir", default="")
    ap.add_argument("--engine-dir", default=str(HERE / "results" / "engine"))
    ap.add_argument("--out-dir", default="", help="propose: write the tables here instead of results/ (default unchanged)")
    ap.add_argument("--p1-inputs", default="", help="propose: read seeds/questions/roles/seed sets from this amended input folder (IT22) instead of the IT9 P1 + IT10 ones")
    ap.add_argument("--no-v1", action="store_true", help="propose: switch the IT21 V1 identity bridge and attribution screen off (the control: reproduces the committed tables)")
    a = ap.parse_args()
    if a.cmd in ("engine", "all"):
        cmd_engine(a)
    if a.cmd in ("withdrawn", "all"):
        cmd_withdrawn(a)
    if a.cmd == "control":
        cmd_control(a)
    if a.cmd in ("anchors", "all"):
        cmd_anchors(a)
    if a.cmd in ("direct", "all"):
        cmd_direct(a)
    if a.cmd in ("propose", "all"):
        cmd_propose(a)
