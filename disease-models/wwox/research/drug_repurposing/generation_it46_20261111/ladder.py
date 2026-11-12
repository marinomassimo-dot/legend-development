"""IT46 P2: one row per molecule that any relation reached, with the six things that must stay apart (reached / identity /
action / transfer to the context / possible benefit / what verification is next) and where, downstream, it is mentioned.
Built only from held tables; a field that no table carries says so. Nothing here ranks and nothing is an exclusion:
`unqualified_entity` is a role, not a filter, and every role keeps its row.

  ladder.py   -> ladder_it46.tsv and a printed measure (rows, situations, rows with no downstream mention)"""
import csv, re, sys
from pathlib import Path
import cell_context as cc

HERE = Path(__file__).resolve().parent; DR = HERE.parent
csv.field_size_limit(10**9)
R = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
F = ["relation_id", "molecule", "name", "molecule_group", "situation", "reached_by", "identity", "action", "transfer_to_context", "possible_benefit", "next_verification", "role", "role_basis", "engine_verdicts", "downstream_mentions"]
DOWN = [DR / "generation_it41_20261109/compound_view.tsv", DR / "ranking_it8_p9_20261029/investigations_it20.tsv", DR / "batch_sci_20261105/map/open_questions_map.tsv",
        DR / "generation_it40_20261109/conditional_proposals_it40.tsv", DR / "view/index.en.html"]


def relation_rows():
    out = {}
    for f in sorted(DR.glob("generation_it4[3-9]_*/relations*.tsv")):
        for r in R(f):
            if r.get("relation_id"):
                out[r["relation_id"]] = r
    return out


def situation(role, status, verdicts, pointer, in_mech):
    if role in ("probe", "control_or_reagent") or status == "tool_probe":
        return "C_probe_or_reagent"
    if pointer and in_mech == "no" and not verdicts:
        return "B_reached_by_activity_only"
    if "CANDIDATE" in verdicts:
        return "A_engine_candidate"          # known action in the tables; identity and role may still be unqualified
    if "UNKNOWN" in verdicts:
        return "U_verdict_unknown"
    return "E_excluded_and_kept"            # the engine says opposite or unsupported action; the row stays, with its reason in the engine columns


SALTS = r"\b(hydrochloride|hydrobromide|sodium|calcium|potassium|mesylate|maleate|tartrate|sulfate|acetate|citrate)\b"


def group_key(name):
    """one key per molecule family inside a relation: case, a radiolabel bracket and a salt word do not make a new molecule (two structures that differ otherwise stay two)"""
    n = re.sub(r"\[[0-9]*h\]", "", name.lower()); n = re.sub(SALTS, "", n)
    return re.sub(r"[^a-z0-9]+", " ", n).strip()


PANEL = re.compile(r"selectivity (interaction|assay)|\bpanel\b|\bPDSP\b|\bscreen(ed|ing)?\b", re.I)


def assay_descriptions():
    """(relation, parent chembl id) -> assay descriptions of the activity rows kept in a case folder (the IT44 activity tables are not committed: only the cases with a committed row file can be checked)"""
    out = {}
    files = [(DR / "generation_it45_20261111/s10_dose/activity_rows.tsv", None), (DR / "generation_it45_20261111/s2_dose/activity_rows.tsv", None), (HERE / "s7_case/s7_activity_rows.tsv", "S7")]
    for f, fixed in files:
        if not f.exists():
            continue
        for r in R(f):
            rid = fixed or r.get("relation_id")
            mol = r.get("parent_chembl_id") or r.get("molecule_chembl_id")
            out.setdefault((rid, mol), []).append(r.get("assay_description", ""))
    return out


def panel_only(descs):
    return bool(descs) and all(PANEL.search(d or "") for d in descs)


def mentions(names, txt):
    """substring first (fast), word boundary only on a hit"""
    return sum(1 for n in names if n and n in txt and re.search(r"\b" + re.escape(n) + r"\b", txt))


def build():
    ad = assay_descriptions()
    rels = relation_rows(); txt = " ".join(open(f, encoding="utf-8").read().lower() for f in DOWN)
    ptr = {(r["relation_id"], r["parent_chembl_id"]): r for r in R(DR / "generation_it44_20261110/pointers_it44.tsv")}
    ctx = {}
    out = []
    for r in R(DR / "generation_it44_20261110/entity_roles_it44.tsv"):
        rid, mol = r["relation_id"], r["molecule"].replace("CAT:", "")
        p = ptr.get((rid, mol)); rel = rels.get(rid, {})
        if rid not in ctx and rel.get("target_symbols"):
            ctx[rid] = cc.context_for([s for s in re.split(r"[;,]", rel["target_symbols"]) if s], rid)[1]
        v = r["engine_verdicts"]
        reached = "mechanism table" + (" + activity read" if p else "") if v else ("activity read" if p else "role table only")
        action = ("activity only, direction not read (ACTIVITY_ONLY)" if (p and p["in_mechanism_path"] == "no" and not v) else
                  "engine: CANDIDATE" if v == "CANDIDATE" else "engine: EXCLUDED (opposite or unsupported action; kept)" if v.startswith("EXCLUDED") else
                  "engine: UNKNOWN" if "UNKNOWN" in v else "engine verdict: " + (v or "none"))
        sit = situation(r["role"], r["catalogue_status"], v, p, p["in_mechanism_path"] if p else "")
        ident = r["catalogue_status"] or "not in catalogue"
        nxt = ("qualify as a tool: identity, selectivity, system" if sit == "C_probe_or_reagent" else
               "qualify identity first (not in catalogue)" if not r["catalogue_status"] and sit == "A_engine_candidate" else
               "qualify role and status first (no rule classified it)" if r["role"] == "unqualified_entity" and sit == "A_engine_candidate" else
               "measure in the context; premise first" if sit == "A_engine_candidate" else
               "read what the verdict lacks" if sit == "U_verdict_unknown" else
               "none unless the exclusion premise changes (see the engine columns)")
        names = {r["name"].lower(), mol.lower()}
        hits = mentions(names, txt)
        out.append(dict(relation_id=rid, molecule=r["molecule"], name=r["name"], molecule_group=group_key(r["name"]), situation=sit, reached_by=reached, identity=ident, action=action,
                        transfer_to_context=ctx.get(rid, "no target symbols for this relation"), possible_benefit="IPOTESI: " + (rel.get("hypothesised_benefit") or "not stated"),
                        next_verification=nxt, role=r["role"], role_basis=r["role_basis"], engine_verdicts=v, downstream_mentions=hits))
    # activity-only pointers have no row in the role table: give them one, with the same six fields (situation B)
    have = {(r["relation_id"], r["molecule"].replace("CAT:", "")) for r in R(DR / "generation_it44_20261110/entity_roles_it44.tsv")}
    seen = set(have)
    srcs = [DR / "generation_it44_20261110/pointers_it44.tsv"] + [DR / d / "activity_molecules.tsv" for d in ("generation_it45_20261111/s10_dose", "generation_it45_20261111/s2_dose", "generation_it45_20261111/s12_reopen")]
    for f in srcs:
        if not f.exists():
            continue
        for p in R(f):
            key = (p["relation_id"], p["parent_chembl_id"])
            if key in seen or p.get("catalogue_status", "none") == "none" or p.get("read_state") != "OK":
                continue
            seen.add(key); rid = p["relation_id"]; rel = rels.get(rid, {})
            if rid not in ctx and rel.get("target_symbols"):
                ctx[rid] = cc.context_for([s for s in re.split(r"[;,]", rel["target_symbols"]) if s], rid)[1]
            nm = p.get("catalogue_name") or p.get("name") or p["parent_chembl_id"]
            sit = "C_probe_or_reagent" if p["catalogue_status"] == "tool_probe" else "B_reached_by_activity_only"
            pan = panel_only(ad.get((rid, p["parent_chembl_id"])))
            hits = mentions({nm.lower(), p["parent_chembl_id"].lower()}, txt)
            out.append(dict(relation_id=rid, molecule="CAT:" + p["parent_chembl_id"], name=nm, molecule_group=group_key(nm), situation=sit, reached_by="activity read", identity=p["catalogue_status"],
                            action="activity only, direction not read (ACTIVITY_ONLY)" + ("; every committed row is a selectivity-panel or screening row" if pan else ""), transfer_to_context=ctx.get(rid, "no target symbols for this relation"),
                            possible_benefit="IPOTESI: " + (rel.get("hypothesised_benefit") or "not stated"),
                            next_verification=("likely an off-target panel entry, not a measurement on this target: confirm the target mapping before any use" if pan else "qualify as a tool: identity, selectivity, system" if sit == "C_probe_or_reagent" else "read the primary documents (activity only)"),
                            role="(no role row)", role_basis="activity pointer not in the role table", engine_verdicts="", downstream_mentions=hits))
    # a row with no catalogue entry of its own that is the same family (same name once case, radiolabel and salt are removed) as a catalogue row of the same relation inherits that identity
    cat_of = {}
    for r in out:
        if r["identity"] not in ("not in catalogue", ""):
            cat_of.setdefault((r["relation_id"], r["molecule_group"]), r["identity"])
    for r in out:
        if r["identity"] == "not in catalogue" and (r["relation_id"], r["molecule_group"]) in cat_of:
            r["identity"] = cat_of[(r["relation_id"], r["molecule_group"])] + " (same family as a catalogue entry of this relation)"
            if r["next_verification"] == "qualify identity first (not in catalogue)":
                r["next_verification"] = "qualify role and status first (no rule classified it)" if r["role"] == "unqualified_entity" else "measure in the context; premise first"
    return out


if __name__ == "__main__":
    rows = build()
    with open(HERE / "ladder_it46.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, F, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print(len(rows), "rows;", len({(r["relation_id"], r["molecule_group"]) for r in rows}), "distinct molecule groups;", dict(Counter(r["situation"] for r in rows)))
    for s in sorted({r["situation"] for r in rows}):
        sub = [r for r in rows if r["situation"] == s]
        print(f"  {s}: {len(sub)} rows, {sum(1 for r in sub if r['downstream_mentions'] == 0)} with no downstream mention")
