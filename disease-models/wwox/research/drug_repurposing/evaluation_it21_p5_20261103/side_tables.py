#!/usr/bin/env python3
"""IT21 P5: the tables that do not need the decoy runs.

  side_tables.py novelty        the 13 hand-over rows against what LEGEND already holds, through the routed tools (never a grep of the two large registries)
  side_tables.py funnel         what survives qualification: P2 funnel, earlier qualification records, P3b dispositions
  side_tables.py errors         where proposals are eliminated, by class of error (identity, level, context, pharmacology, role, earlier decision)
  side_tables.py experiments    how many distinguishable experiments the 13 hand-over rows lead to
  side_tables.py guards         the guards' effect on decoys (needs the guards-off decoy rows)
  side_tables.py all

Routed tools used: `framework/scripts/repurposing_search.py compound` (compound to targets to needs, offline), `qualification_it21_p3b_20261103/novelty_it21.py --registries`
(whole-word module search and `registry_records.py` records, bulk generator tables never counted as LEGEND having examined a compound). A perimeter, not a literature claim.
Not medical advice. Retrospective: it tests properties of a method and shows no prospective benefit.
"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, gzip, json, re, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = DR.parents[3]
P2 = DR / "generation_it21_p2_20261103"
P3B = DR / "qualification_it21_p3b_20261103"
RANK = DR / "ranking_it8_p9_20261029"
OUT = HERE / "results"


def rd(p):
    with (gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def wr(path, rows, cols=None):
    cols = cols or (list(rows[0]) if rows else [])
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in cols})


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO))
    return r.stdout


def routed_compound(name):
    out = run([sys.executable, "framework/scripts/repurposing_search.py", "compound", name, "--json"])
    try:
        recs = json.loads(out)
    except json.JSONDecodeError:
        return dict(records=0, n_target_rows=0, needs=[])
    needs = sorted({n if isinstance(n, str) else (n.get("need") or n.get("id") or json.dumps(n)) for r in recs for n in (r.get("needs_touched") or [])})
    return dict(records=len(recs), n_target_rows=max((r.get("n_target_rows") or 0 for r in recs), default=0), needs=needs)


def novelty_line(term):
    out = run([sys.executable, str(P3B / "novelty_it21.py"), "--registries", term])
    d = dict(record_dirs=0, bulk_tables=0, card_or_need="none", registry_records=0)
    for ln in out.splitlines():
        m = re.search(r"record_dirs=(\d+)", ln)
        if m:
            d["record_dirs"] = int(m.group(1))
            d["bulk_tables"] = int(re.search(r"bulk_tables=(\d+)", ln).group(1)) if re.search(r"bulk_tables=(\d+)", ln) else 0
            d["card_or_need"] = "none" if "card_or_need=none" in ln else "yes"
        m = re.search(r"registries whole-word records=(\d+)", ln)
        if m:
            d["registry_records"] = int(m.group(1))
    return d


def cmd_novelty(a):
    H = rd(P2 / "results" / "handoff_it21.tsv")
    P = {r["proposal_id"]: r for r in rd(P2 / "results" / "proposals_it21.tsv")}
    rows = []
    for h in H:
        p = P[h["proposal_id"]]
        comp = h["compound"]
        tgt = p["main_target"]
        rc = routed_compound(comp)
        nc = novelty_line(comp)
        nt = novelty_line(tgt)
        # "named in cards/units" is the P2 flag (cards, packets, unit tables, proposal maps). record_dirs also counts exploration lists and scouting tables, which enumerate
        # a name without examining it, so it is reported as a column and not used to call a relation known.
        compound_known = p["named_in_legend_material"] == "yes" or bool(p["earlier_decision"]) or nc["registry_records"] > 0
        target_known = p["target_named_in_legend_material"] == "yes" or nt["card_or_need"] != "none"
        linked = bool(rc["needs"])
        if compound_known and target_known:
            cls = "compound and target axis both held by LEGEND"
        elif target_known:
            cls = "new compound on an axis LEGEND holds"
        elif compound_known:
            cls = "known compound on a new axis"
        else:
            cls = "neither compound nor axis in cards/units (named only in lists)" if (nc["record_dirs"] or nt["record_dirs"]) else "absent from LEGEND material"
        rows.append(dict(proposal_id=h["proposal_id"], question=h["question"], hypothesis=h["hypothesis"], compound=comp, main_target=tgt,
                         catalogue_records=rc["records"], catalogue_target_rows=rc["n_target_rows"], needs_touched_by_catalogue_targets=";".join(rc["needs"]) or "none",
                         compound_record_dirs=nc["record_dirs"], compound_registry_records=nc["registry_records"], target_record_dirs=nt["record_dirs"],
                         target_in_a_card_or_need=nt["card_or_need"], named_in_cards_units_p2=p["named_in_legend_material"], target_named_p2=p["target_named_in_legend_material"],
                         earlier_decision_p2=(p["earlier_decision"] or "")[:60], relation_class=cls,
                         relation_is_new=int(not compound_known and not linked)))
    wr(OUT / "novelty_handover_p5.tsv", rows)
    c = collections.Counter(r["relation_class"] for r in rows)
    print(dict(c), "relation_is_new:", sum(r["relation_is_new"] for r in rows), "of", len(rows))
    return rows


def cmd_funnel(a):
    P = rd(P2 / "results" / "proposals_it21.tsv")
    summ = json.loads((P2 / "results" / "summary_it21.json").read_text())
    b = summ["blockers"]
    rows = [
        dict(stage="1 seed-specific rows (P2, guards on, three nulls)", n=len(P), note="992 rows in 153 mechanism clusters; all CONDITIONAL_H_HARM / CONDITIONAL_H_PROTECT, none qualified by construction (closed status vocabulary)"),
        dict(stage="2 identity resolved (ChEMBL id) and small molecule", n=len(P) - b["identity_not_resolved"] - sum(v for k, v in b.items() if k.startswith("modality")) - 0, note="first blocker met in order: identity 662, modality 21 (an upper bound: later blockers are counted after these)"),
        dict(stage="3 eligible by H1 to H4 and H8 (stated benefit hypothesis, not decided earlier, cluster not examined earlier, reach null confirms)", n=b["ELIGIBLE"], note="141 rows in 32 mechanism clusters"),
        dict(stage="4 handed over to qualification (cap 3 per question and hypothesis)", n=summ["handed_over"], note="the rule is the author's; another cap gives another 13"),
        dict(stage="5 qualified (QUALIFIED_HYPOTHESIS)", n=0, note="no qualification record exists for the 13; L7 of the P2 README. Zero is the pipeline's closed vocabulary plus no P4-type run, not a negative result"),
    ]
    # earlier records
    rec = collections.Counter()
    for f in ("it9_records.tsv", "it10_records.tsv", "it11_records.tsv"):
        for r in rd(RANK / f):
            rec[(f.split("_")[0], r["origin"], r["state"])] += 1
    for (pk, origin, state), n in sorted(rec.items()):
        rows.append(dict(stage=f"earlier record {pk} / {origin} / {state}", n=n, note="ranking_it8_p9_20261029"))
    p3 = rd(P3B / "proposals_it21_p3b.tsv")
    dc = collections.Counter(r["disposition"] for r in p3)
    rows.append(dict(stage="P3b path-B proposals (compound to WWOX, authored handles; NOT the P2 generator)", n=len(p3), note=f"selected for qualification {sum(1 for r in p3 if r['selected_for_qualification'].lower().startswith(('y', '1', 't')))}; dispositions {dict(dc)}; QUALIFIED_HYPOTHESIS 0"))
    # of the P2 rows, those whose compound has an earlier record, by state
    st = collections.Counter(((r["earlier_decision"] or "none").split()[0]) for r in P)
    rows.append(dict(stage="P2 seed-specific rows whose compound has an earlier qualification record (state)", n=sum(v for k, v in st.items() if k != "none"), note=str(dict(st))))
    wr(OUT / "qualification_funnel_p5.tsv", rows)
    for r in rows:
        print(r["stage"][:90], r["n"])
    return rows


def cmd_errors(a):
    summ = json.loads((P2 / "results" / "summary_it21.json").read_text())
    wd = json.loads((P2 / "results" / "withdrawn_summary.json").read_text())
    b = summ["blockers"]
    cls = [
        ("identity", "twin catalogue records not merged on name; a DGIdb-only family has no ChEMBL id", "identity_not_resolved (rows)", b["identity_not_resolved"]),
        ("identity", "salt or name twins of one compound", "94 compound-at-set-and-arm rows lose novelty outright after the guards (129 withdrawn rows keep a twin)", 129),
        ("level", "class-level or group record written above the gene (group_record_mostly_outside_module_targets)", "withdrawn rows by withheld reason, IT10 list", 80),
        ("level", "republished copy of a ChEMBL claim whose level the copy does not carry", "withdrawn rows by withheld reason, IT10 list", 139),
        ("context", "a null that matches a different covariate removes the row (reach-matched null)", "reach_null_not_confirming (rows)", b["reach_null_not_confirming"]),
        ("context", "a mechanism cluster already holds an earlier qualification record", "mechanism_cluster_examined_earlier (rows)", b["mechanism_cluster_examined_earlier"]),
        ("role", "the arm has no stated benefit hypothesis (mimics in Q4, Q6, Q7)", "arm_has_no_stated_benefit_hypothesis (rows)", b["arm_has_no_stated_benefit_hypothesis"]),
        ("pharmacology", "modality is not a small molecule (antibody, peptide, unknown)", "modality_* (rows)", sum(v for k, v in b.items() if k.startswith("modality"))),
        ("pharmacology", "active moiety uncertain (prodrug or unresolved)", "HELD_UNCERTAIN_ACTIVE_MOIETY (candidate rows, capped tables)", 100),
        ("earlier decision", "compound already decided in an IT9 to IT11 record", "decided_in_earlier_qualification_record (rows)", b["decided_in_earlier_qualification_record"]),
        ("guards, all causes", "rows of the IT10 seed-specific list withdrawn by the refreshed guards", "withdrawn of 1,202", wd["withdrawn"]),
    ]
    wr(OUT / "error_classes_p5.tsv", [dict(error_class=c, what=w, measure=m, n=n) for c, w, m, n in cls])
    for c in cls:
        print(c)


def cmd_experiments(a):
    H = rd(P2 / "results" / "handoff_it21.tsv")
    step0 = collections.defaultdict(list)
    for h in H:
        s0 = h["discriminating_experiment"].split("Step 1")[0].strip()
        step0[(h["question"], s0)].append(h["proposal_id"])
    tg = collections.Counter(re.search(r"(?:inhibits/lowers|activates/raises) (\S+)", h["action_on_main_target"]).group(1) for h in H)
    rows = []
    for (q, s0), ids in sorted(step0.items()):
        rows.append(dict(question=q, step0=s0[:300], hand_over_rows_resting_on_it=len(ids), proposal_ids=";".join(ids)))
    wr(OUT / "experiments_p5.tsv", rows)
    summ = dict(handed_over=len(H), distinct_step0_experiments=len(step0), distinct_main_targets=len(tg),
                step1_template_identical=len({re.sub(r"Step 1 \(only if step 0 supports the role assumed here\): .*? versus vehicle", "Step 1 X versus vehicle", h["discriminating_experiment"]) .split("Step 0")[0] for h in H}) <= 1)
    print(summ)
    return summ


def cmd_guards(a):
    """Guards on (the refreshed action table) against guards off (the IT9 action table rebuilt on today's catalogue), same decoys, same engine."""
    def keyed(path, kmax):
        d = collections.defaultdict(set)
        for r in rd(path):
            if int(r["rep"]) <= kmax:
                d[(r["seed_set"], r["variant"], int(r["rep"]))].add((r["family_id"], int(r["sign"])))
        return d
    on = keyed(OUT / "decoy_rows.tsv.gz", 15)
    off = keyed(OUT / "decoy_rows_guards_off.tsv.gz", 15)
    sets = sorted({k[0] for k in off})
    rows = []
    for sn in sets:
        o, n = off[(sn, "real", 0)], on[(sn, "real", 0)]
        rows.append(dict(seed_set=sn, design="real", n_guards_off=len(o), n_guards_on=len(n), withdrawn=len(o - n), gained=len(n - o),
                         withdrawn_share=round(len(o - n) / len(o), 4) if o else ""))
        for v in ("deg", "reach"):
            sh, wd, gn = [], [], []
            for k in range(1, 16):
                o, n = off[(sn, v, k)], on[(sn, v, k)]
                wd.append(len(o - n)); gn.append(len(n - o))
                if o:
                    sh.append(len(o - n) / len(o))
            srt = sorted(sh)
            rows.append(dict(seed_set=sn, design=v, n_guards_off="median " + str(sorted(len(off[(sn, v, k)]) for k in range(1, 16))[7]),
                             n_guards_on="median " + str(sorted(len(on[(sn, v, k)]) for k in range(1, 16))[7]),
                             withdrawn="median " + str(sorted(wd)[7]), gained="median " + str(sorted(gn)[7]),
                             withdrawn_share=f"median {srt[len(srt) // 2]:.4f}; range {srt[0]:.4f} to {srt[-1]:.4f}; replicates with rows {len(srt)}" if srt else "no replicate has a row"))
    wr(OUT / "guards_effect_p5.tsv", rows)
    for r in rows:
        print(r)


def cmd_all(a):
    cmd_funnel(a); cmd_errors(a); cmd_experiments(a); cmd_novelty(a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["novelty", "funnel", "errors", "experiments", "guards", "all"])
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    {"novelty": cmd_novelty, "funnel": cmd_funnel, "errors": cmd_errors, "experiments": cmd_experiments, "guards": cmd_guards, "all": cmd_all}[a.cmd](a)


if __name__ == "__main__":
    main()
