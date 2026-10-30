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

import argparse, collections, csv, glob, gzip, json, os, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
ROLE_VOCAB = {"harmful", "protective", "mixed", "composition", "unknown", "not_applicable"}
BASIS_VOCAB = {"SOURCE_STATED", "NONE"}
COLS = ["question", "seed_set", "arm", "rank", "family_id", "name", "hypothesis", "disposition", "role_status", "resolving_measure",
        "n_seed_rows", "n_origins", "origin_note", "chain_status", "use_scope", "it9_state", "reconcile", "evaluation_forbidden_on", "v3_row_ref"]


def rd(p, gz=False):
    with (gzip.open(p, "rt", encoding="utf-8") if gz else open(p, encoding="utf-8")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_roles(path):
    out = {}
    for r in rd(path):
        if r["role_status"] not in ROLE_VOCAB or r["role_basis"] not in BASIS_VOCAB:
            raise SystemExit(f"{path}: closed vocabulary violated for {r['question_id']}: {r['role_status']}/{r['role_basis']}")
        if r["role_status"] in ("harmful", "protective") and r["role_basis"] != "SOURCE_STATED":
            raise SystemExit(f"{r['question_id']}: a harmful/protective role needs role_basis SOURCE_STATED (a leaning orders arms, it does not set a role)")
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


def origin_key(seed):
    """Reconstructable evidence origin of one P1 seed row, or ('', False) when it cannot be rebuilt.
    Same accession/system id, or same PMID at the same readout level, is ONE origin. Different levels of one article are different
    origins (complementary measures; the article is returned as origin_group). Not deduplicated by PMID alone."""
    loc = seed["source_locator"]
    m = re.search(r"system_id=([A-Za-z0-9_,]+)", loc)
    if m:
        return "SYS:" + ",".join(sorted(m.group(1).split(","))), True
    g = re.findall(r"GSE\d+", loc + " " + seed["context"])
    if g:
        return "ACC:" + ",".join(sorted(set(g))) + "|" + seed["level"], True
    p = re.findall(r"PMID\s*(\d+)", loc)
    if len(p) == 1:
        return f"PMID:{p[0]}|{seed['level']}", True
    if "CM-IT7P4:" in loc or "SN-IT7P1:" in loc:
        sysm = re.findall(r"(ORG_KO|HNPC_KD|NEUR_KD|MS_HIP|MN_HIP|MNULL_HIP|MS_CTX|organoid_ko_w15|hnpc_shwwox)", loc)
        if sysm:
            return "SYS:" + ",".join(sorted(set(s.lower() for s in sysm))), True
    return "SEED:" + seed["seed_id"], False


def canonical_origin(seed):
    """Fold the IT7 derived tables (derived_gene_values / contrast map) of the two human deposits into one origin key."""
    k, ok = origin_key(seed)
    loc = seed["source_locator"]
    if k.startswith("SYS:") and re.search(r"organoid_ko_w15|hnpc_shwwox|org_ko|hnpc_kd|neur_kd", k.lower()):
        return "DEPOSITS:GSE156243+GSE126075(+neurons)", True
    return k, ok


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
                k, ok = canonical_origin(s)
            origins.setdefault(k, ok)
    unrec = sum(1 for ok in origins.values() if not ok)
    note = ("origins: " + "; ".join(sorted(origins))[:160]) + (f"; {unrec} origin(s) not reconstructable" if unrec else "")
    return len(keep), len(origins), note


def dev_scope(name, dev):
    hits = [d for d in dev if d["compound"].lower() in name.lower()]
    if not hits:
        return "unspecified"
    sys_block = any(d["scope"] == "systemic_development" for d in hits)
    ex_block = any(d["affects_ex_vivo_probe"] == "no" and d["scope"].startswith("probe") for d in hits)
    ex = "ex_vivo_probe_eligible" if not ex_block else "ex_vivo_probe_blocked"
    pre = any(d["scope"] == "probe_precondition" for d in hits)
    return ("systemic_development_limited;" if sys_block else "") + ex + (";probe_precondition_open" if pre else "")


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def phenotype_first(v3_dir, dr, extra_path):
    """Interventions with a signed functional result in a WWOX system (ranking member_evidence.tsv, tested_in_wwox_system = yes) plus the
    curated extras; graph_status is computed against the v3 candidate tables and the full proposal tables, never required."""
    me = rd(dr / "ranking_it8_p9_20261029" / "member_evidence.tsv")
    um = rd(dr / "ranking_it8_p9_20261029" / "unit_members.tsv")
    fam_by_unit = collections.defaultdict(list)
    for r in um:
        if r["family_id"].startswith("FAM:") and ("identity" in r["roles"] or "assertion_subject" in r["roles"] or "named_member" in r["roles"]):
            fam_by_unit[r["unit_id"]].append((r["family_id"], r["name"]))
    specific = {}
    for f in glob.glob(str(v3_dir / "candidates_Q*.tsv")):
        for r in rd(f):
            if r["arm"] in ("opposes", "mimics") and r["seed_specific_all_three_nulls"] == "1":
                specific[r["family_id"]] = (r["question"], r["arm"])
    scored = {}
    for f in glob.glob(str(v3_dir / "proposals_p1_*tiers*.tsv.gz")):
        if f.endswith(("_indeg.tsv.gz", "_adm.tsv.gz")):
            continue
        q = os.path.basename(f).split("_")[2]
        for r in rd(f, True):
            if abs(float(r["Q_net_ind"] or 0)) > 0 or r["direct_hit_any_action_on_seed_gene"] == "1":
                scored.setdefault(r["family_id"], set()).add(q)
    out = []
    for r in me:
        if r["tested_in_wwox_system"].lower() != "yes":
            continue
        fams = fam_by_unit.get(r["unit_id"], [])
        mt = r["member_type"]
        if mt in ("gene_therapy", "diet"):
            gs = "OUT_OF_METHOD_MODALITY"
        elif not fams:
            gs = "NOT_EXAMINABLE_NO_CATALOGUE_IDENTITY"
        else:
            spec = [specific[f] for f, _ in fams if f in specific]
            sc = sorted({q for f, _ in fams for q in scored.get(f, ())})
            gs = ("IN_SEED_SPECIFIC_ARM:" + ";".join(f"{q}/{a}" for q, a in spec)) if spec else (("SCORED_NOT_SPECIFIC:" + ",".join(sc)) if sc else "NO_GRAPH_ROW")
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


def build(v3, DR):
    """Dispositions of every candidate row of one engine run directory (v3 results, or results_v4)."""
    roles = load_roles(HERE / "question_roles.tsv")
    dev = rd(HERE / "dev_constraints.tsv")
    it9 = {norm(r["compound"]): r for r in rd(DR / "ranking_it8_p9_20261029" / "it9_records.tsv")}
    p1 = rd(DR / "generation_it9_p1_20261030" / "seeds.tsv")
    sidx = load_seed_index(str(DR / "generation_it9_p2_20261030" / "seeds_p1"), p1)
    contrib_cache = {}
    n_by = collections.Counter()
    rows_out = collections.defaultdict(list)
    for f in sorted(glob.glob(str(v3 / "candidates_Q*.tsv"))):
        for r in rd(f):
            q = r["question"]
            role = roles[q]
            arm = r["arm"]
            hyp, disp = disposition(arm, role)
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
            recon = "REVIEW_ROLE_DEPENDENT_DROP" if (rec and rec["state"] == "DROP" and disp.startswith("CONDITIONAL_IF_PROTECTIVE") and arm == "mimics") else ""
            rows_out[q].append([q, sn, arm, r["rank"], r["family_id"], nm, hyp, disp, role["role_status"], role["resolving_measure"][:140], nrows, norig, onote,
                                r["edge_chain_main_target_to_seed_1"][:90], dev_scope(nm, dev) if arm in ("opposes", "mimics") else "", st9, recon,
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
