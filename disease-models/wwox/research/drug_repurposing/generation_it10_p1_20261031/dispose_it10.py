#!/usr/bin/env python3
"""IT10 P1: role-aware dispositions of the IT9 v3 candidate tables (matching_guidance_v3.md sections 1.2, 5, 6, 7, 8).

The v3 engine (generation_it9_p2_20261030/v3) returns a compatible action (opposes / mimics) per family. It never says what the
observed change MEANS (harmful, protective, mixed, composition, unknown): in IT9 every 'opposes' row was read as the goal and every
'mimics' row as a direction control, i.e. the role was silently assumed harmful for all 65 usable seeds, none of which states a role
(seeds.tsv carries no role column and no usable seed's text states one). This script makes the role an explicit, sourced input and
changes four decisions that were implicit:

  1. Which arm is a lever.  role unknown/mixed -> BOTH arms are kept as separate conditional hypotheses (H_HARM from 'opposes',
     H_PROTECT from 'mimics'), each with the measurement that resolves the role.  An arm is WITHDRAWN only when the role is
     SOURCE_STATED; a curator leaning orders the arms but never withdraws one.
  2. Which candidates enter at all.  A phenotype-first arm admits an intervention with a signed functional result in a WWOX system whether
     or not the graph returns it (graph_status is reported, not required).
  3. How much convergence is real.  Contributing seeds are collapsed to evidence ORIGINS where the origin is reconstructable (accession
     or system id in the locator; PMID + readout level otherwise); an unreconstructable origin stays its own origin and is flagged.
  4. What a limit removes.  A systemic-development constraint (dev_constraints.tsv) does not cancel ex vivo probe utility.

Usage:
  dispose_it10.py run [--v3 DIR] [--baseline DIR] [--out DIR]
  dispose_it10.py --help
Inputs are read-only: v3 results, P1 seeds, ranking member evidence, question_roles.tsv, dev_constraints.tsv, phenotype_first_extra.tsv (optional).
A compatible action is not a predicted benefit; a conditional hypothesis is not a recommendation; not medical advice.
"""
import sys

if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import argparse, collections, csv, glob, gzip, importlib.util, json, os, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
ROLE_VOCAB = {"harmful", "protective", "mixed", "composition", "unknown", "not_applicable"}
BASIS_VOCAB = {"SOURCE_STATED", "NONE"}
COLS = ["question", "seed_set", "arm", "rank", "family_id", "name", "hypothesis", "disposition", "role_status", "resolving_measure",
        "n_seed_rows", "n_origins", "origin_note", "chain_status", "chain_note", "top_seed_share", "contrary_seed_share", "chain_pair_walks", "chain_pair_share", "chain_contrary_walks", "reach_null_z", "use_scope", "it9_state", "reconcile", "evaluation_forbidden_on", "v3_row_ref"]


def rd(p, gz=False):
    with (gzip.open(p, "rt", encoding="utf-8") if gz else open(p, encoding="utf-8")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_roles(path):
    out = {}
    for r in rd(path):
        if r["role_status"] not in ROLE_VOCAB or r["role_basis"] not in BASIS_VOCAB:
            raise SystemExit(f"{path}: closed vocabulary violated for {r['question_id']}: {r['role_status']}/{r['role_basis']}")
        if r["role_status"] not in ("unknown", "not_applicable") and r["role_basis"] != "SOURCE_STATED":
            raise SystemExit(f"{r['question_id']}: a {r['role_status']} role needs role_basis SOURCE_STATED (a leaning orders arms, it does not set a role)")
        if r["role_status"] != "unknown" and r["role_status"] != "not_applicable" and not r.get("role_source", "").strip():
            raise SystemExit(f"{r['question_id']}: role_source (a locator) is required when the role is stated")
        out[r["question_id"]] = r
    return out


def disposition(arm, role):
    """(hypothesis, disposition) for an opposes/mimics row under the question's role. Pure function; the tests call it."""
    st = role["role_status"]
    if arm not in ("opposes", "mimics"):
        return "NONE", "DIAGNOSTIC_ONLY"
    if st == "not_applicable":
        return "NONE", "NOT_APPLICABLE"
    if st == "harmful":
        return ("H_HARM", "PRIMARY_RELIEVE") if arm == "opposes" else ("H_HARM", "WITHDRAWN_DISEASE_DIRECTION_CONTROL")
    if st == "protective":
        return ("H_PROTECT", "PRIMARY_SUPPORT") if arm == "mimics" else ("H_PROTECT", "WITHDRAWN_OPPOSES_PROTECTIVE_RISK")
    if st == "composition":
        return ("H_COMPOSITION", "HELD_UNTIL_COMPOSITION_RESOLVED")
    lead = role.get("leaning", "none")
    first = (arm == "opposes" and lead == "harmful") or (arm == "mimics" and lead == "protective")
    tag = "(leaning-first)" if first else ""
    return ("H_HARM", f"CONDITIONAL_IF_HARMFUL{tag}") if arm == "opposes" else ("H_PROTECT", f"CONDITIONAL_IF_PROTECTIVE{tag}")


ACC = re.compile(r"\b(GSE\d+|E-MTAB-\d+|PMID\s*\d+|system_id=[A-Za-z0-9_,]+)")


def origin_keys(seed):
    """Reconstructable evidence origins of one P1 seed row (a list: a seed that cites two articles carries two origins), each (key, reconstructable).
    Same accession/system id, or same PMID at the same readout level, is ONE origin. Different levels of one article are different origins (complementary
    measures). Not deduplicated by PMID alone. An unreconstructable origin stays its own and is flagged."""
    loc = seed["source_locator"]
    txt = loc + " " + seed["context"]
    m = re.search(r"system_id=([A-Za-z0-9_,]+)", loc)
    if m:
        return [("SYS:" + ",".join(sorted(m.group(1).split(","))), True)]
    g = sorted({x.upper() for x in re.findall(r"gse\d+", txt, flags=re.I)})
    if g:
        return [("ACC:" + ",".join(g) + "|" + seed["level"], True)]
    p = set()
    for mm in re.finditer(r"PMIDs?\s*", loc):
        seg = re.split(r"[;)]", loc[mm.end():mm.end() + 80])[0]
        p |= set(re.findall(r"(?<![-\d])(\d{7,8})(?![-\d])", seg))
    p = sorted(p)
    if p:
        return [(f"PMID:{x}|{seed['level']}", True) for x in p]
    if "CM-IT7P4:" in loc or "SN-IT7P1:" in loc:
        sysm = re.findall(r"(ORG_KO|HNPC_KD|NEUR_KD|MS_HIP|MN_HIP|MNULL_HIP|MS_CTX|organoid_ko_w15|hnpc_shwwox)", loc)
        if sysm:
            return [("SYS:" + ",".join(sorted(set(x.lower() for x in sysm))), True)]
    return [("SEED:" + seed["seed_id"], False)]


def canonical_origins(seed):
    """Fold the IT7 derived tables of the two human deposits (GSE156243 organoid, GSE126075 hNPC, neurons) to one origin. This is a judgement: two deposits read
    with one method and one derivation count once, which makes 'no change' true for Q2 by construction; the fold is declared in the README and tested as intended."""
    out = []
    for k, ok in origin_keys(seed):
        if re.search(r"organoid_ko_w15|hnpc_shwwox|org_ko|hnpc_kd|neur_kd|gse156243|gse126075", k.lower()):
            k, ok = "DEPOSITS:GSE156243+GSE126075(+neurons)", True
        out.append((k, ok))
    return out


_OVR = None


def canonical_origins_checked(seed):
    """canonical_origins minus the origins an override row removes (an observation that is not significant at its source does not count as an origin)."""
    global _OVR
    if _OVR is None:
        _OVR = collections.defaultdict(set)
        for r in rd(HERE / "origin_overrides.tsv"):
            _OVR[r["seed_id"]].add(r["drop_origin"])
    keep = [(k, ok) for k, ok in canonical_origins(seed) if k not in _OVR.get(seed["seed_id"], ())]
    return keep or canonical_origins(seed)


def canonical_origin(seed):
    """first origin only (kept for callers that need one key)"""
    return canonical_origins(seed)[0]


def load_seed_index(seeds_dir_p1, p1_seeds):
    """seed_set name + P1 seed id -> P1 seed row, from the engine seed files (source_ref carries the P1 ids)."""
    by_p1 = {r["seed_id"]: r for r in p1_seeds}
    idx = {}
    for f in glob.glob(os.path.join(seeds_dir_p1, "*.tsv")):
        if f.endswith("manifest.tsv"):
            continue
        sn = os.path.basename(f)[:-4]
        for r in rd(f):
            ids = [x for x in re.split(r"[;,\s]+", r["source_ref"]) if x in by_p1]
            idx[(sn, r["seed_id"])] = [by_p1[i] for i in ids]
    return idx


def contributing_origins(contrib_rows, seed_index, set_name, frac=0.10):
    """Seed rows that carry at least frac of the strongest contribution to the family, folded to origins."""
    if not contrib_rows:
        return 0, 0, ""
    mx = max(abs(float(c["contrib_total"])) for c in contrib_rows) or 1.0
    keep = [c for c in contrib_rows if abs(float(c["contrib_total"])) >= frac * mx]
    origins = {}
    unrec = 0
    for c in keep:
        for s in seed_index.get((set_name, c["seed_id"]), []) or [None]:
            if s is None:
                k, ok = "SEED:" + c["seed_id"], False
            else:
                for k, ok in canonical_origins_checked(s):
                    origins.setdefault(k, ok)
                continue
            origins.setdefault(k, ok)
    unrec = sum(1 for ok in origins.values() if not ok)
    note = ("origins: " + "; ".join(sorted(origins))[:160]) + (f"; {unrec} origin(s) not reconstructable" if unrec else "")
    return len(keep), len(origins), note


def dev_scope(name, dev):
    """Systemic-development limits and probe-level limits are reported side by side. ex_vivo_probe_eligible means no probe-scope row says it affects the probe;
    a probe_specificity / probe_precondition row that affects the probe (affects_ex_vivo_probe = yes) adds a visible qualifier instead of hiding it."""
    hits = [d for d in dev if d["compound"].lower() in name.lower()]
    if not hits:
        return "unspecified"
    parts = []
    if any(d["scope"] == "systemic_development" for d in hits):
        parts.append("systemic_development_limited")
    probe = [d for d in hits if d["scope"].startswith("probe")]
    parts.append("ex_vivo_probe_with_confound(" + ",".join(sorted({d["scope"] for d in probe if d["affects_ex_vivo_probe"] == "yes"})) + ")"
                 if any(d["affects_ex_vivo_probe"] == "yes" for d in probe) else "ex_vivo_probe_eligible")
    if any(d["scope"] == "probe_precondition" for d in hits):
        parts.append("probe_precondition_open")
    return ";".join(parts)


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


PHENO_ALIASES = {"d-apv": ["d-ap5", "apv", "aminophosphonovalerate", "aminophosphonovaleric"]}


def member_tokens(member):
    t = re.split(r"[ ,(]", member.strip().lower())[0]
    return [t] + PHENO_ALIASES.get(t, [])


def phenotype_first(v3_dir, dr, extra_path):
    """Interventions with a recorded WWOX-system result (ranking member_evidence.tsv, tested_in_wwox_system = yes; the admission rule is that, not a requirement that the
    result be signed or fully read: depth and signs are carried as columns) plus curated extras. graph_status is computed per MEMBER by name, never per unit, and is
    reported, not required: a salt or name twin that has a row is labelled NAME_TWIN_*, because twins are not merged."""
    me = rd(dr / "ranking_it8_p9_20261029" / "member_evidence.tsv")
    specific = {}
    # IT11 P2.1: read the FULL seed-specific list; the candidate tables keep only the top 50 opposes / 25 mimics per set (lithium sat at mimics rank 67 to 70 of 232 in Q6)
    for r in rd(v3_dir / "v3_seed_specific_all_nulls.tsv"):
        specific.setdefault(norm(r["name"]), []).append((r["question"], r["arm"]))
    rows = collections.defaultdict(list)       # token-matchable proposal rows: (question, name, nonzero Q, direct hit)
    for f in glob.glob(str(v3_dir / "proposals_p1_*tiers*.tsv.gz")):
        if f.endswith(("_indeg.tsv.gz", "_adm.tsv.gz")):
            continue
        q = os.path.basename(f).split("_")[2]
        for r in rd(f, True):
            rows[norm(r["name"])].append((q, float(r["Q_net_ind"] or 0) != 0, r["direct_hit_any_action_on_seed_gene"] == "1"))
    out = []
    for r in me:
        if r["tested_in_wwox_system"].lower() != "yes":
            continue
        mt = r["member_type"]
        toks = [norm(t) for t in member_tokens(r["member"])]
        if mt in ("gene_therapy", "diet"):
            gs = "OUT_OF_METHOD_MODALITY"
        elif r["unit_id"] == "U10":
            gs = "NOT_EXAMINABLE_NO_CATALOGUE_IDENTITY"
        else:
            names = [n for n in rows if any(n == t or n.startswith(t) for t in toks)]
            spec = sorted({f"{q}/{a}" for n in names for q, a in specific.get(n, [])})
            nz = sorted({q for n in names for q, nzq, _ in rows[n] if nzq})
            dh = sorted({q for n in names for q, _, d in rows[n] if d})
            if spec:
                gs = "IN_SEED_SPECIFIC_ARM:" + ";".join(spec)
            elif nz:
                gs = "SCORED_NOT_SPECIFIC:" + ",".join(nz)
            elif dh:
                gs = "DIRECT_HIT_ZERO_SCORE:" + ",".join(dh)
            else:
                gs = "NO_GRAPH_ROW"
            if names and not spec and any(n not in toks for n in names) and not gs.startswith("NO_GRAPH_ROW"):
                gs = "NAME_TWIN_" + gs
        out.append(dict(source="member_evidence", unit_id=r["unit_id"], intervention=r["member"], member_type=mt, wwox_signs=r["signs"], readout=r["what"],
                        depth=r["depth"], pmids=r["source_pmids"], graph_status=gs, entry="PHENOTYPE_FIRST"))
    if extra_path and Path(extra_path).exists():
        for r in rd(extra_path):
            r.setdefault("source", "extra")
            r["entry"] = "PHENOTYPE_FIRST"
            r["graph_status"] = r.get("graph_status") or "NOT_CHECKED"
            out.append(r)
    return out


SEL_COLS = ["question", "hypothesis", "rule", "pos", "name", "arm", "rank_v3", "n_origins", "n_seed_rows", "known_to_legend", "it9_state", "disposition", "chain_status"]
TOPN = 8


def deepening(rows_out, v3, dr, it9):
    """Which candidates to deepen first, per question and hypothesis: the BASELINE rule (v3 rank, i.e. the smallest |z| over the three nulls)
    versus the origin-aware rule (more independent evidence origins first, then v3 rank). Only unflagged seed-specific opposes/mimics rows,
    one row per normalised name. Where every candidate has one origin the two rules coincide and the table says so (no change is a result)."""
    known = {norm(r["name"]) for r in rd(dr / "ranking_it8_p9_20261029" / "unit_members.tsv") if r["family_id"].startswith("FAM:")}
    known |= set(it9)
    spec = {}
    for f in glob.glob(str(v3 / "candidates_Q*.tsv")):
        for r in rd(f):
            spec[(r["question"], r["arm"], r["rank"])] = r["seed_specific_all_three_nulls"]
    out = []
    for q, rows in sorted(rows_out.items()):
        for arm, hyp in (("opposes", "H_HARM"), ("mimics", "H_PROTECT")):
            pool, seen = [], set()
            for r in rows:
                if r[2] != arm or spec.get((q, arm, str(r[3]))) != "1":
                    continue
                k = norm(r[5])
                if k in seen:
                    continue
                seen.add(k)
                pool.append(r)
            base = sorted(pool, key=lambda r: int(r[3]))[:TOPN]
            new = sorted(pool, key=lambda r: (-int(r[11]), int(r[3])))[:TOPN]
            for rule, lst in (("baseline_v3_rank", base), ("origin_aware", new)):
                for i, r in enumerate(lst, 1):
                    kn = "known" if (norm(r[5]) in known) else "new_to_legend"
                    out.append([q, hyp, rule, i, r[5], arm, r[3], r[11], r[10], kn, r[15], r[7], r[13]])
    return out


_ENG = None
_GRAPHS = {}


def _graph(level):
    """v4 graph (edges read once) for walk decomposition; the walks use the same admissibility rules as the score."""
    global _ENG
    if _ENG is None:
        saved = list(sys.argv); sys.argv = ["x", "selftest"]
        try:
            spec = importlib.util.spec_from_file_location("seed_engine_v4_dz", HERE / "engine_v4" / "seed_engine_v4.py")
            _ENG = importlib.util.module_from_spec(spec); sys.modules["seed_engine_v4_dz"] = _ENG; spec.loader.exec_module(_ENG)
        finally:
            sys.argv = saved
        _ENG._edges = _ENG.read_edges4()
    if level not in _GRAPHS:
        g = _ENG.Graph4(_ENG._edges, extras=[]); g.level = level; _GRAPHS[level] = g
    return _GRAPHS[level]


def explain_columns(contrib_rows, level):
    """How much of the real calculation the shown chain stands for. The score is a signed sum over seeds (contrib_total) and, for each seed, over every admissible walk from
    every target of the family; the displayed chain is ONE walk for the strongest seed. Returns (note, top_seed_share, contrary_seed_share, n_walks, chain_share_of_pair, contrary_walk_share).
    chain_note: DOMINANT_CHAIN (one seed carries at least half of the gross contribution, no more than 10 percent contrary, one walk at least half of the pair) otherwise PARTIAL_EXAMPLE
    with the reasons. A walk is arithmetic, not a confirmed mechanism."""
    vals = [float(c["contrib_total"]) for c in contrib_rows]
    gross = sum(abs(v) for v in vals)
    if not vals or gross == 0:
        return "NO_CONTRIBUTION_ROWS", "", "", "", "", ""
    net = sum(vals)
    top = max(contrib_rows, key=lambda c: abs(float(c["contrib_total"])))
    top_share = abs(float(top["contrib_total"])) / gross
    contrary = sum(abs(v) for v in vals if net and v * net < 0) / gross
    t = top["main_target_hops1to3"] or top["main_target_hop0"]
    nw, bsh, cw = 0, None, None
    if t and float(top["contrib_hops1to3"] or 0) != 0:
        g = _graph(level)
        nw, bsh, cw = _ENG.walk_summary(g.walks(t, top["gene"]))
    h0 = abs(float(top["contrib_hop0"] or 0)); h13 = abs(float(top["contrib_hops1to3"] or 0))
    if h0 >= h13 and h0 > 0:                      # the strongest seed is reached mostly by the compound's own target: there is no chain to show
        return (f"DIRECT_OR_MIXED: hop-0 (the compound's own target is the seed gene) carries {h0 / (h0 + h13):.0%} of the strongest seed's contribution; walk columns describe only the indirect part",
                f"{top_share:.3f}", f"{contrary:.3f}", "", "", "")
    reasons = []
    if top_share < 0.5:
        reasons.append(f"strongest seed carries {top_share:.0%} of the gross contribution")
    if contrary > 0.10:
        reasons.append(f"{contrary:.0%} of the gross contribution opposes the net")
    if bsh is not None and bsh < 0.5:
        reasons.append(f"the shown walk is {bsh:.0%} of its pair's walk mass ({nw} walks)")
    if cw is not None and cw > 0.10:
        reasons.append(f"{cw:.0%} of the pair's walk mass opposes")
    note = "DOMINANT_CHAIN" if not reasons else "PARTIAL_EXAMPLE: " + "; ".join(reasons)
    f = lambda x: "" if x is None else f"{x:.3f}"
    return note, f"{top_share:.3f}", f"{contrary:.3f}", nw if nw else "", f(bsh), f(cw)


def build(v3, DR):
    """Dispositions of every candidate row of one engine run directory (v3 results, or results_v4)."""
    roles = load_roles(HERE / "question_roles.tsv")
    dev = rd(HERE / "dev_constraints.tsv")
    it9 = {norm(r["compound"]): r for r in rd(DR / "ranking_it8_p9_20261029" / "it9_records.tsv")}
    p1 = rd(DR / "generation_it9_p1_20261030" / "seeds.tsv")
    sidx = load_seed_index(str(DR / "generation_it9_p2_20261030" / "seeds_p1"), p1)
    rolereason = {norm(r["compound"]) for r in rd(HERE / "it9_role_dependent_reasons.tsv")}
    reach = {}                          # IT11: z under the reach-matched null (null genes matched on the F5-admissible reach), where it was run
    for pr in glob.glob(str(HERE / "results_v4_reach" / "proposals_p1_*_reach.tsv.gz")):
        sn_ = os.path.basename(pr)[len("proposals_p1_"):-len("_reach.tsv.gz")]
        reach[sn_] = {r["family_id"]: r["Z_ind_robust"] for r in rd(pr, True)}
    contrib_cache = {}
    n_by = collections.Counter()
    rows_out = collections.defaultdict(list)
    for f in sorted(glob.glob(str(v3 / "candidates_Q*.tsv"))):
        for r in rd(f):
            q = r["question"]
            role = roles[q]
            arm = r["arm"]
            hyp, disp = disposition(arm, role)
            if role["role_status"] == "not_applicable" and arm in ("opposes", "mimics"):
                raise SystemExit(f"{q}: role not_applicable but the engine returned an {arm} row; state the role with a source")
            sn = r["seed_set"]
            if sn not in contrib_cache:
                p = v3 / f"contributions_p1_{sn}.tsv.gz"
                cc = collections.defaultdict(list)
                if p.exists():
                    for c in rd(p, True):
                        cc[c["family_id"]].append(c)
                contrib_cache[sn] = cc
            nrows, norig, onote = contributing_origins(contrib_cache[sn].get(r["family_id"], []), sidx, sn) if arm in ("opposes", "mimics", "flagged_opposes", "flagged_mimics") else (0, 0, "")
            if arm.startswith("flagged_"):
                disp = "HELD_UNCERTAIN_ACTIVE_MOIETY"
            nm = r["name"]
            rec = it9.get(norm(nm))
            if rec is None:
                for k, v in it9.items():
                    if k and k in norm(nm):
                        rec = v
                        break
            st9 = rec["state"] if rec else ""
            recon = "REVIEW_ROLE_DEPENDENT_REASON" if (rec and norm(rec["compound"]) in rolereason and disp.startswith("CONDITIONAL_IF_PROTECTIVE") and arm == "mimics") else ""
            ex = explain_columns(contrib_cache[sn].get(r["family_id"], []), "expression" if "expression" in sn else "protein") if arm in ("opposes", "mimics") else ("", "", "", "", "", "")
            rows_out[q].append([q, sn, arm, r["rank"], r["family_id"], nm, hyp, disp, role["role_status"], role["resolving_measure"][:140], nrows, norig, onote,
                                r["edge_chain_main_target_to_seed_1"][:90], *ex, (reach.get(sn, {}).get(r["family_id"], "") if arm in ("opposes", "mimics") else ""), dev_scope(nm, dev) if arm in ("opposes", "mimics") else "", st9, recon,
                                r["evaluation_forbidden_on"], f"{os.path.basename(f)}#{arm}{r['rank']}"])
            n_by[(q, arm, disp)] += 1
    return rows_out, n_by, it9


def write_tsv(path, header, rows):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def cmd_run(a):
    v3 = Path(a.v3)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows_out, n_by, it9 = build(v3, DR)
    for q, rows in rows_out.items():
        write_tsv(out / f"dispositions_{q}.tsv", COLS, rows)
    write_tsv(out / "disposition_counts.tsv", ["question", "arm", "disposition", "rows"], [[q, arm, d, n] for (q, arm, d), n in sorted(n_by.items())])
    new = deepening(rows_out, v3, DR, it9)
    sel = [r[:2] + ["origin_aware_on_v4_tables" if r[2] == "origin_aware" else "baseline_on_v4_tables"] + r[3:] for r in new]
    if a.baseline and Path(a.baseline).exists():                 # the IT9 tables and the IT9 rule, and the origin-aware rule applied to the IT9 tables
        brows, _, _ = build(Path(a.baseline), DR)
        old = deepening(brows, Path(a.baseline), DR, it9)
        sel = [r[:2] + ["IT9_baseline_v3_rank" if r[2] == "baseline_v3_rank" else "origin_aware_on_IT9_tables"] + r[3:] for r in old] + \
              [r for r in sel if r[2] == "origin_aware_on_v4_tables"]
    write_tsv(out / "deepening_candidates.tsv", SEL_COLS, sel)
    ex_rows = []
    for q, rows in sorted(rows_out.items()):
        sel = [r for r in rows if r[2] in ("opposes", "mimics")]
        ci = {c: COLS.index(c) for c in COLS}
        def num(r, c):
            v = r[ci[c]]
            return float(v) if v not in ("", None) else None
        dom = sum(1 for r in sel if str(r[ci["chain_note"]]).startswith("DOMINANT"))
        ts = sorted(x for x in (num(r, "top_seed_share") for r in sel) if x is not None)
        ex_rows.append([q, len(sel), dom, len(sel) - dom, f"{ts[len(ts) // 2]:.3f}" if ts else "",
                        sum(1 for r in sel if (num(r, "contrary_seed_share") or 0) > 0.10), sum(1 for r in sel if (num(r, "chain_pair_share") or 1) < 0.5),
                        sum(1 for r in sel if (num(r, "chain_contrary_walks") or 0) > 0.10)])
    write_tsv(out / "explain_summary.tsv", ["question", "rows", "dominant_chain", "partial_example", "median_top_seed_share", "rows_contrary_seed_gt10pct", "rows_best_walk_lt50pct_of_pair", "rows_contrary_walks_gt10pct"], ex_rows)
    pf = phenotype_first(v3, DR, HERE / "phenotype_first_extra.tsv")
    cols = sorted({k for r in pf for k in r})
    with open(out / "phenotype_first.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for r in pf:
            w.writerow({k: r.get(k, "") for k in cols})
    summ = dict(dispositions={f"{q}|{arm}|{d}": n for (q, arm, d), n in sorted(n_by.items())}, phenotype_first=len(pf),
                phenotype_first_graph_status=dict(collections.Counter(r["graph_status"].split(":")[0] for r in pf)))
    (out / "summary.json").write_text(json.dumps(summ, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summ, indent=1, sort_keys=True))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run"])
    ap.add_argument("--v3", default=str(HERE / "results_v4"), help="engine run directory to disposition (v4 by default; the v3 results work too)")
    ap.add_argument("--baseline", default=str(DR / "generation_it9_p2_20261030" / "v3" / "results"), help="IT9 v3 results for the before/after selection table")
    ap.add_argument("--out", default=str(HERE / "results"))
    a = ap.parse_args()
    cmd_run(a)
