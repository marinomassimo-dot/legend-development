#!/usr/bin/env python3
"""IT21 V1 forward snapshot builder (reads existing artefacts, recomputes nothing).

Writes, next to this file: forward_snapshot_inputs.tsv, forward_snapshot_vorinostat_trace.tsv,
forward_snapshot_contrast_cases.tsv.  Run from the repository root:  python3 <this file>
It is committed BEFORE any reverse analysis of the case (git log shows the order).
"""
import csv, gzip, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=HERE, text=True).strip()
D = "disease-models/wwox/research/drug_repurposing/"


def sh(*a):
    return subprocess.check_output(a, cwd=ROOT, text=True).strip()


def read_tsv(rel):
    with open(os.path.join(ROOT, D, rel), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


INPUTS = [
    ("seed table (131 rows, 65 usable)", "generation_it9_p1_20261030/seeds.tsv"),
    ("compound catalogue (44,211 entries)", "catalog/catalog.jsonl.gz"),
    ("family action table, guards on (IT21 P2)", "generation_it21_p2_20261103/results/actions/family_actions.tsv.gz"),
    ("family meta (identity flags)", "generation_it21_p2_20261103/results/actions/family_meta.tsv.gz"),
    ("IT21 P2 generator and hand-over rules", "generation_it21_p2_20261103/run_generation_it21.py"),
    ("IT21 P2 action refresh", "generation_it21_p2_20261103/refresh_actions_it21.py"),
    ("IT21 P2 proposals", "generation_it21_p2_20261103/results/proposals_it21.tsv"),
    ("IT21 P2 hand-over", "generation_it21_p2_20261103/results/handoff_it21.tsv"),
    ("IT21 P2 summary (blockers)", "generation_it21_p2_20261103/results/summary_it21.json"),
    ("IT10 v4 seed-specific list", "generation_it10_p1_20261031/results_v4/v3_seed_specific_all_nulls.tsv"),
    ("IT10 dispositions Q2", "generation_it10_p1_20261031/results/dispositions_Q2.tsv"),
    ("IT9 P3 consolidated candidates", "exploration_it9_p3_20261030/candidates_consolidated.tsv"),
    ("IT9 P3 excluded", "exploration_it9_p3_20261030/excluded.tsv"),
    ("IT9 P4c-e selection note", "qualification_it9_p4c_e_20261030/selection_note_E.md"),
    ("IT21 P4a qualification", "qualification_it21_p4a_20261103/qualification_it21_p4a.tsv"),
    ("IT21 P3b path B levers", "qualification_it21_p3b_20261103/pathb_levers_it21.tsv"),
    ("IT21 P5 decoy comparison (real rows)", "evaluation_it21_p5_20261103/results/real_rows_vs_decoy_frequency_p5.tsv"),
    ("ranking (queue/ranking/dashboard input)", "ranking_it8_p9_20261029/ranking.json"),
    ("informative negatives (NEG-03 nanatinostat)", "ranking_it8_p9_20261029/informative_negatives_it21.tsv"),
    ("needs", "needs/needs.json"),
    ("card A01 PBA class (HDAC comparator, revival trigger)", "cards/A01_pba_class.packet.json"),
    ("local GtoPdb interactions (cache, not in git)", None),
]


def inputs_table():
    rows = []
    for role, rel in INPUTS:
        if rel is None:
            p = os.environ.get("LEGEND_CATALOG_CACHE", "/home/desktop/legend-development/" + D + "catalog/cache") + "/gtopdb/interactions.csv"
            sha = subprocess.check_output(["sha256sum", p], text=True).split()[0] if os.path.exists(p) else "absent"
            rows.append(dict(role=role, path=p, blob_sha="sha256:" + sha[:16], last_commit="not tracked"))
            continue
        p = os.path.join(ROOT, D, rel)
        blob = sh("git", "hash-object", p)[:12]
        lc = sh("git", "log", "-1", "--format=%h %ad", "--date=short", "--", D + rel)
        rows.append(dict(role=role, path=D + rel, blob_sha=blob, last_commit=lc))
    return rows


def vorinostat_trace():
    t = []

    def add(stage, artefact, level, what):
        t.append(dict(stage=stage, artefact=artefact, level=level, what_the_artefact_says=what))

    add("catalogue", "catalog/catalog.jsonl.gz", "present",
        "two records: CAT:CHEMBL98 (ChEMBL, InChIKey WAEXFXRVDQXREF, approved, UNII, NDC prescription) and CAT:DGIDB:316b73312895 (DGIdb-only, no ChEMBL id, synonym IUPHAR.LIGAND:6852); coverage_matrix lists CHEMBL98 as 'possible duplicate by name, not merged'")
    add("action table", "generation_it21_p2.../actions/family_actions.tsv.gz", "present",
        "FAM:CAT:CHEMBL98 signed targets HDAC1,HDAC2,HDAC3,HDAC6 (all -1, ChEMBL single_protein); FAM:CAT:DGIDB:316b73312895 signed targets HDAC1-11 (-1, DGIdb_other;GtoPdb, single_protein_among_siblings or unspecified)")
    add("IT7 pilot (LINCS neural contexts)", "usable_compounds_it7_p2_20261029/pilot_subset.tsv", "present",
        "CHEMBL98 in the pilot subset, 6 neural contexts; network_comparison_it7_p3 family_scores O_E -1.26, freq_hit_rate_NET 0.245")
    add("IT9 P2 generation, v3", "generation_it9_p2_20261030/v3/results/candidates_Q2.tsv", "generated",
        "Q2 expression opposes rank 34, DGIdb twin only, Z robust total 5.68 / indeg 4.36 / adm 3.53, seed-specific in all three nulls, chain HDAC5 -T(+)-> SLC2A1")
    add("IT9 P2 generation, v3 (Q6)", "generation_it9_p2_20261030/v3/results/candidates_Q6.tsv", "generated (diagnostic)",
        "Q6 direct_search rank 18: DGIdb lists MYC as a target; unsigned_or_no_signed_direct_action; no hypothesis")
    add("IT9 P3 exploration", "exploration_it9_p3_20261030/candidates_consolidated.tsv", "present, not taken",
        "parent CHEMBL98 (both families merged by the P3 parent rule), direction CONFLICT (Q2 opposes, Q6 mimics), main target HDAC5, n_signed_targets 11, promiscuous=1; disposition not_taken:promiscuous(>=5 targets); also written to excluded.tsv")
    add("IT9 P4c-e selection", "qualification_it9_p4c_e_20261030/selection_note_E.md", "not selected",
        "HDAC5 -> SLC2A1 cluster (pracinostat, panobinostat, vorinostat, valproic acid, 4-PBA and 30 more): one CollecTRI edge shared by 30+ families, pan-HDAC hub-like, 'not taken for diversity'")
    add("IT10 v4 + dispositions", "generation_it10_p1_20261031/results/dispositions_Q2.tsv", "classified conditional",
        "Q2 opposes rank 36, hypothesis H_HARM, CONDITIONAL_IF_HARMFUL, role unknown, chain status DOMINANT_CHAIN (top seed share 0.745), 1 origin; not in deepening_candidates.tsv")
    add("IT21 P2 refreshed generation", "generation_it21_p2_20261103/results/proposals_it21.tsv", "generated (conditional)",
        "IT21P2-0031 CONDITIONAL_H_HARM, qualified=no, z total 5.69, reach 3.16, 1 origin; handoff_eligible=no, blocker identity_not_resolved (no ChEMBL id on the twin)")
    add("IT21 P5 decoy evaluation", "evaluation_it21_p5_20261103/results/real_rows_vs_decoy_frequency_p5.tsv", "present",
        "real row eligible=0 blocker identity_not_resolved; decoy frequencies 0.0 (coarse, degree, reach); linked_to_a_need=1, target_is_need_target=0")
    add("IT21 P3b path B", "qualification_it21_p3b_20261103/pathb_compounds_it21.tsv", "present (lever table)",
        "HDAC6 inhibitor in the H_STAB lever list (both families), lever_status NAMED_ALREADY; no qualification record")
    add("qualification records", "qualification_it9_*/ , it10_records, it11_records, qualification_it21_p4a", "absent",
        "no qualification record names vorinostat (IT9 32 records, IT10 4, IT11 3, IT21 P4a 6); the cluster neighbour nanatinostat was rejected in P4a (REJECTED_INFORMATIVE) and recorded as NEG-03")
    add("coverage priorities", "coverage/priorities.json", "present (exploration only)",
        "twin family listed against NEED-MYC-PROGENITOR-PROLIFERATION: need_direction uncertain, L1 pathway_member_only, L4 none_in_record")
    add("ranking / investigations / dashboard", "ranking_it8_p9_20261029/ranking.json; investigations_it20.tsv; view/index.html", "not visible as a candidate",
        "no ranking row, no investigation row; the compound appears in the view only as a catalogue family listing (twin, 85 target rows)")
    add("cards", "cards/A01_pba_class.packet.json", "class-level thread",
        "HDAC-inhibitor comparator (butyrate) did not raise a soluble-cytosolic mutant; revival trigger 'HDAC-inhibitor or HSP co-inducer role'; IT5 P8 applied vorinostat at about 33x (HDAC1) and 66x (HDAC6) its median IC50 in the cited precedent")
    add("WWOX-literature", "commit_candidates/CC-20261004W8-A-VPA-DIRECTION-01.md; paper_registry PAPER 222", "present as counter-evidence",
        "PMID 41254692 text says vorinostat may increase WWOX expression; its own CTD export lists vorinostat WWOX as 'Decreases expression'; reading debt DL-REPO-003; the 2026-09-22 expression-boost census found no PubMed WWOX record for vorinostat")
    add("external reference", "none in repository", "not examined",
        "Unravel's selection of vorinostat: no record of it in any repository artefact; no external contact allowed in this package")
    return t


CONTRAST = [
    ("C1_plausible", "IT21P2-0195", "GSK343", "Q5 H_HARM, EZH2 -> IL6, two mouse articles, tier B"),
    ("C2_conditional", "IT21P2-0374", "tizaterkib", "Q5 H_PROTECT role probe, MAPK1 -> BCL3 -> TNF"),
    ("C3a_contrary_hdac_class", "IT21P2-0006", "nanatinostat", "Q2 H_HARM, HDAC5 -> SLC2A1, class I HDAC inhibitor judged unfavourable in P4a"),
]


def contrast():
    P = {r["proposal_id"]: r for r in read_tsv("generation_it21_p2_20261103/results/proposals_it21.tsv")}
    H = {r.get("proposal_id"): r for r in read_tsv("generation_it21_p2_20261103/results/handoff_it21.tsv")}
    Q = {r["proposal_id"]: r for r in read_tsv("qualification_it21_p4a_20261103/qualification_it21_p4a.tsv")}
    out = []
    for cid, pid, name, role in CONTRAST:
        p, h, q = P[pid], H.get(pid, {}), Q.get(pid, {})
        out.append(dict(case=cid, proposal_id=pid, compound=name, role=role, status=p["status"], qualified=p["qualified"],
                        main_target=p["main_target"], z_total=p["z_total"], z_reach=p["z_reach"], n_origins=p["n_origins"],
                        chain=p["chain"][:80], handoff_eligible=p["handoff_eligible"], handoff_blocker=p["handoff_blocker"],
                        handed_over="yes" if h else "no", p4a_disposition=q.get("disposition", ""), p4a_status_after=q.get("status_after", "")))
    # C3b: glue-type abstention, read from the withdrawn table (no proposal row exists by design)
    W = read_tsv("generation_it21_p2_20261103/results/withdrawn_vs_it10.tsv")
    for r in W:
        if r["name"].upper() == "POMALIDOMIDE" and r["question"] == "Q6":
            out.append(dict(case="C3b_abstention_glue_crbn", proposal_id="(none, withdrawn)", compound="pomalidomide",
                            role="CRBN glue-type action: direction must be withheld, no proposal", status="no proposal row",
                            qualified="no", main_target="CRBN", z_total=r["z_total"], z_reach="", n_origins="",
                            chain=r["chain"][:80], handoff_eligible="no", handoff_blocker=r["cause"] + ":" + r["withheld_reasons_at_main_target"],
                            handed_over="no", p4a_disposition="", p4a_status_after=""))
            break
    return out


def write(name, rows):
    path = os.path.join(HERE, name)
    keys = list(rows[0].keys())
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(name, len(rows))


if __name__ == "__main__":
    write("forward_snapshot_inputs.tsv", inputs_table())
    write("forward_snapshot_vorinostat_trace.tsv", vorinostat_trace())
    write("forward_snapshot_contrast_cases.tsv", contrast())
