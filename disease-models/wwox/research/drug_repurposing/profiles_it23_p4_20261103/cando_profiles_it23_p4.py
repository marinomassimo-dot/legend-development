#!/usr/bin/env python3
"""IT23 P4: evaluate the CANDO interaction-signature matrix as a multi-protein comparison next to LEGEND's per-target search.

  cando_profiles_it23_p4.py --work DIR [--out DIR] [--fetch]

DIR holds the downloaded third-party files (never in git): tutorial_matrix-approved.tsv, cmpds-v2.2.tsv, pdb_2_uniprot.csv,
zen/rd.tsv (Zenodo 17241534, rd_ecfp4-homo_sapien-v2.5-approved-int_vect-dice-CxP.tsv), zen/db.tsv (drugbank-v2.5-approved.tsv).
--fetch downloads them (sizes capped at 300 MB; the 665 MB 'all' matrix is deliberately not fetched). UniProt gene symbols are looked up by
accession only (public REST, no account, no personal data) and cached in DIR/uniprot_cache.json.
Needs numpy; LEGEND_CATALOG_CACHE for the typed same-measure comparison (step 4). Writes coverage.tsv, identity_join.tsv, comparison.tsv,
sign_sensitivity.tsv and a console summary. Heavy: run under  systemd-run --user --scope -p MemoryMax=4G -p MemorySwapMax=0.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, gzip, json, os, re, subprocess, time, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))
DR = HERE.parent
PROT = "http://protinfo.compbio.buffalo.edu/cando/data/v2.2+"
ZEN = "https://zenodo.org/records/17241534/files"
CAP = 300 * 1024 * 1024
UNIPROT = re.compile(r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2}")

# ---- the WWOX questions each gene serves (LEGEND work to 2026-11-03; a gene is listed because a package names it, not because the matrix helps) ----
QUESTIONS = {
    "HDAC1": "HDAC class I / Q2 H_HARM-H_PROTECT handoff (IT21P2)", "HDAC2": "HDAC class I", "HDAC3": "HDAC class I", "HDAC4": "HDAC class IIa", "HDAC5": "HDAC class IIa (handoff IT21P2-0005 pracinostat main target)",
    "HDAC6": "stability lever L2a (tubastatin precedent), IT22 P6", "HDAC7": "HDAC class IIa", "HDAC8": "HDAC class I", "HDAC9": "HDAC class IIa", "HDAC10": "HDAC class IIb", "HDAC11": "HDAC class IV",
    "EZH1": "EZH2 glia qualification (Ezh1 compensation), IT22 P6", "EZH2": "EZH2 glia qualification, IT22 P6", "BRD4": "BET / epigenetic readers", "THRA": "TR agonist qualification: the OPC-timing isoform, IT22 P6",
    "THRB": "TR agonist qualification: liver-directed isoform, IT22 P6", "NFE2L2": "NRF2 axis (IT11 P23)", "KEAP1": "NRF2 axis (IT11 P23)", "MAPK1": "ERK axis", "MAPK3": "ERK axis", "AHR": "AHR axis",
    "CDK4": "cell-cycle / OPC cycle exit", "CDK6": "cell-cycle / OPC cycle exit", "GSK3B": "GSK3 target-first package (IT15 QB)", "GRIN1": "NMDAR pharmacology (IT6 P9, IT15 QA)", "GRIN2B": "NMDAR pharmacology",
    "EGLN1": "HIF axis (IT10 P21)", "EGLN2": "HIF axis; handoff IT21P2-0043 desidustat", "HIF1A": "HIF axis", "LDHA": "lactate / LDH axis", "PKM": "glycolysis", "SQSTM1": "autophagy / lysosomal flux (stability probes)",
    "HSPA8": "stability lever L1 (HSC70, forigerimod)", "LAMP2": "lysosomal flux control", "WWOX": "the disease gene itself", "WWP1": "WW-domain partner", "YAP1": "WW-domain partner / Hippo", "STK3": "Hippo kinase MST2 (WW-domain adjacent)",
    "SLC2A1": "GLUT1 (seed readout)", "XIAP": "handoff IT21P2-0014", "ZHX2": "handoff IT21P2-0035", "SIRT1": "deacetylase", "SIRT2": "deacetylase", "SIRT3": "deacetylase", "KDM1A": "epigenetic", "DNMT1": "epigenetic",
    "APOE": "no LEGEND question (listed because it is in the 64-protein demonstration set)", "BRD7": "no direct question (a bromodomain protein, not BRD4)",
}
SET8 = [  # (DrugBank id, role in LEGEND work, source package)
    ("DB00279", "desired action: TR agonist (native T3)", "qualification_it22_p6/tr_agonists"),
    ("DB00451", "desired action: TR agonist prohormone (T4)", "qualification_it22_p6/tr_agonists"),
    ("DB00509", "alternative in the TR class (D-T4), not in LEGEND dossier", "this package (class neighbour)"),
    ("DB02546", "HDAC pan-inhibitor; stability-probe CSF reference; HDAC6 lever class; EZH2-axis opposing-sign analogue", "qualification_it22_p6/stability_probes"),
    ("DB06603", "HDAC pan-inhibitor, potency contrast to vorinostat", "handoff_it21 class (pracinostat is an HDAC inhibitor)"),
    ("DB00608", "lysosomal-flux probe arm (chloroquine)", "qualification_it22_p6/stability_probes"),
    ("DB09073", "CDK4/6 inhibitor: potential opposing action on OPC cycle exit / differentiation", "this package (opposing-action control)"),
    ("DB08908", "NRF2 activator via covalent KEAP1 modification: similarity-blind mechanism control", "nrf2_it11_p23"),
]


def sh(cmd):
    return subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True).stdout


def fetch(work):
    work.mkdir(parents=True, exist_ok=True)
    (work / "zen").mkdir(exist_ok=True)
    jobs = [(f"{PROT}/tutorial/tutorial_matrix-approved.tsv", "tutorial_matrix-approved.tsv"), (f"{PROT}/mappings/cmpds-v2.2.tsv", "cmpds-v2.2.tsv"),
            (f"{PROT}/mappings/pdb_2_uniprot.csv", "pdb_2_uniprot.csv"), (f"{ZEN}/rd_ecfp4-homo_sapien-v2.5-approved-int_vect-dice-CxP.tsv?download=1", "zen/rd.tsv"),
            (f"{ZEN}/drugbank-v2.5-approved.tsv?download=1", "zen/db.tsv")]
    for u, f in jobs:
        if (work / f).exists():
            continue
        n = int([l for l in sh(f"curl -sIL '{u}'").lower().splitlines() if l.startswith("content-length")][-1].split(":")[1])
        assert n <= CAP, (u, n)
        sh(f"curl -sL -o '{work / f}' '{u}'")


def uniprot_genes(accs, cache_path, online):
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    todo = sorted(a for a in accs if a not in cache)
    if todo and not online:
        print(f"WARNING: {len(todo)} accessions have no cached gene symbol (run with --fetch)")
    elif todo:
        def one(batch):
            url = "https://rest.uniprot.org/uniprotkb/accessions?" + urllib.parse.urlencode({"accessions": ",".join(batch), "fields": "accession,gene_primary,organism_id,xref_hgnc", "format": "tsv"})
            for k in range(4):
                try:
                    with urllib.request.urlopen(url, timeout=60) as resp:
                        return resp.read().decode()
                except Exception as e:
                    err = e
                    time.sleep(2 + 3 * k)
            if len(batch) > 1:
                h = len(batch) // 2
                return one(batch[:h]) + "\n" + one(batch[h:])
            print("UniProt lookup failed for", batch, err)
            return ""
        for i in range(0, len(todo), 50):
            for l in one(todo[i:i + 50]).splitlines():
                p = l.split("\t")
                if len(p) >= 3 and p[0] != "Entry":
                    cache[p[0]] = p[1:]
            time.sleep(0.3)
        cache_path.write_text(json.dumps(cache))
    return cache


def load_matrix(path):
    import numpy as np
    ids, rows = [], []
    for l in open(path):
        p = l.rstrip("\n").split("\t")
        ids.append(p[0])
        rows.append(np.asarray(p[1:], dtype=np.float32))
    return ids, np.vstack(rows)


def protein_map(ids, work, online):
    """row id -> (uniprot list, gene, organism, how). Row ids are PDB chains ('4bkxB') or, for modelled proteins, a bare UniProt accession."""
    want = {(i[:4], i[4:]): i for i in ids if not UNIPROT.fullmatch(i)}
    m = collections.defaultdict(set)
    with open(work / "pdb_2_uniprot.csv") as f:
        for r in csv.DictReader(f):
            k = (r["PDB"].lower(), r["CHAIN"])
            if k in want:
                m[want[k]].add(r["SP_PRIMARY"])
    direct = {i for i in ids if UNIPROT.fullmatch(i) and i not in m}
    accs = {a for v in m.values() for a in v} | direct
    g = uniprot_genes(accs, work / "uniprot_cache.json", online)
    out = {}
    for i in ids:
        ups = sorted(m[i]) if i in m else ([i] if i in direct else [])
        how = "pdb_2_uniprot" if i in m else ("row id is a UniProt accession" if i in direct else "UNMAPPED")
        genes = sorted({(g.get(u) or ["", ""])[0] for u in ups if (g.get(u) or ["", ""])[0]})
        org = sorted({(g.get(u) or ["", ""])[1] for u in ups})
        out[i] = (ups, genes, org, how)
    return out


def main():
    import numpy as np
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--out", default=str(HERE))
    ap.add_argument("--fetch", action="store_true")
    a = ap.parse_args()
    work, out = Path(a.work), Path(a.out)
    if a.fetch:
        fetch(work)

    # ---------- (1) the 64-protein demonstration matrix ----------
    tid, T = load_matrix(work / "tutorial_matrix-approved.tsv")
    tmap = protein_map(tid, work, a.fetch)
    # ---------- the usable matrix: Zenodo human matrix ----------
    zid, Z = load_matrix(work / "zen" / "rd.tsv")
    zmap = protein_map(zid, work, a.fetch)
    db = list(csv.DictReader(open(work / "zen" / "db.tsv"), delimiter="\t"))
    cm = list(csv.DictReader(open(work / "cmpds-v2.2.tsv"), delimiter="\t"))
    cm_ap = [r for r in cm if "approved" in r["DRUG_GROUPS"].split(";")]
    print(f"tutorial matrix {T.shape}; Zenodo matrix {Z.shape}; drugbank-v2.5-approved rows {len(db)}; cmpds-v2.2 approved rows {len(cm_ap)}")
    assert T.shape[1] == len(cm_ap) == Z.shape[1] == len(db)
    same_order = [r["DRUGBANK_ID"] for r in cm_ap] == [r["DRUGBANK_ID"] for r in db]
    print("column order identical between cmpds-v2.2 (approved) and drugbank-v2.5-approved:", same_order, "; shared ids:", len({r['DRUGBANK_ID'] for r in cm_ap} & {r['DRUGBANK_ID'] for r in db}))
    print("score range tutorial", float(T.min()), float(T.max()), "Zenodo", float(Z.min()), float(Z.max()), "; Zenodo zero cells", float((Z == 0).mean()))

    # ---------- (2) identity: join by DrugBank id to the catalogue, then InChIKey/family ----------
    import compound_catalog as cc, repurposing_search as rs
    ents = cc.load(DR / "catalog" / "catalog.jsonl.gz")
    fam = rs.families(ents)
    by_db = collections.defaultdict(list)
    for e in ents:
        for d in (e.get("ids") or {}).get("drugbank") or []:
            by_db[d].append(e)
    fam_meta = {}
    with gzip.open(DR / "generation_it21_p2_20261103/results/actions/family_meta.tsv.gz", "rt") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            fam_meta[r["family_id"]] = r
    fam_act = collections.defaultdict(list)
    with gzip.open(DR / "generation_it21_p2_20261103/results/actions/family_actions.tsv.gz", "rt") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            fam_act[r["family_id"]].append(r)
    ident = []
    for j, r in enumerate(db):
        es = by_db.get(r["DRUGBANK_ID"], [])
        fams = sorted({fam.get(e["id"], "FAM:" + e["id"]) for e in es})
        iks = sorted({(e.get("ids") or {}).get("inchikey") or "" for e in es} - {""})
        names = sorted({e.get("name") or "" for e in es})
        nm = r["GENERIC_NAME"].lower().replace("_", " ")
        agree = any(nm == (n or "").lower() for n in names)
        status = "NO_CATALOGUE_RECORD_WITH_THIS_DRUGBANK_ID" if not es else ("MATCH_ONE_FAMILY" if len(fams) == 1 else "AMBIGUOUS_SEVERAL_FAMILIES")
        ident.append(dict(column_index=j, cando_id=r["CANDO_ID"], drugbank_id=r["DRUGBANK_ID"], cando_name=r["GENERIC_NAME"], join_status=status, catalogue_ids=";".join(sorted(e["id"] for e in es)),
                          chembl_id=";".join(sorted({(e.get("ids") or {}).get("chembl") or "" for e in es} - {""})), inchikey=";".join(iks), family_id=";".join(fams), catalogue_name=";".join(names),
                          name_agrees_informational_only=("yes" if agree else ("no" if es else "")), n_signed_actions_in_family_table=sum(len(fam_act.get(x, [])) for x in fams)))
    with open(out / "identity_join.tsv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(ident[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(ident)
    st = collections.Counter(x["join_status"] for x in ident)
    n_ik = sum(1 for x in ident if x["inchikey"])
    n_act = sum(1 for x in ident if x["n_signed_actions_in_family_table"])
    n_fams = len({x["family_id"] for x in ident if x["join_status"] == "MATCH_ONE_FAMILY"})
    print("identity join:", dict(st), "with InChIKey", n_ik, "with >=1 signed action row", n_act, "distinct families", n_fams, "name disagreements (informational)", sum(1 for x in ident if x["name_agrees_informational_only"] == "no"))

    # ---------- (3) coverage: which genes exist in each matrix ----------
    def gene_rows(pmap):
        g = collections.defaultdict(list)
        for rid, (ups, genes, org, how) in pmap.items():
            for s in genes:
                if "9606" in org:
                    g[s.upper()].append(rid)
        return g
    gz, gt = gene_rows(zmap), gene_rows(tmap)
    print("Zenodo: rows", len(zid), "mapped to >=1 UniProt", sum(1 for v in zmap.values() if v[0]), "human genes", len(gz), "| tutorial: human genes", sorted(gt), "| non-human or unmapped rows",
          sum(1 for v in tmap.values() if "9606" not in v[2]))
    cov = []
    for g, q in QUESTIONS.items():
        cov.append(dict(gene=g, in_zenodo_human_matrix="yes" if g in gz else "no", zenodo_rows=";".join(gz.get(g, [])), in_64_protein_demo_matrix="yes" if g in gt else "no", demo_rows=";".join(gt.get(g, [])),
                        wwox_question_served=q, n_legend_families_with_a_signed_action_at_gene=len({f for f, v in fam_act.items() if any(x["target_symbol"].upper() == g for x in v)})))
    with open(out / "coverage.tsv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(cov[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(cov)
    with open(out / "coverage_demo64.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["matrix_row", "uniprot", "gene", "organism_taxid", "mapping", "wwox_question"])
        for rid in tid:
            ups, genes, org, how = tmap[rid]
            w.writerow([rid, ";".join(ups), ";".join(genes), ";".join(org), how, "; ".join(QUESTIONS.get(x.upper(), "") for x in genes if x.upper() in QUESTIONS) or "none"])

    # ---------- column-order sanity: a known pair must be high if columns follow the mapping order ----------
    dbi = {r["DRUGBANK_ID"]: j for j, r in enumerate(db)}
    zi = {r: k for k, r in enumerate(zid)}
    def pct(row, drug):
        v = Z[zi[row]]
        return float((v < v[dbi[drug]]).mean() * 100), float(v[dbi[drug]])
    sanity = [("vorinostat at HDAC8 chain", "5vi6A", "DB02546"), ("vorinostat at HDAC6 chain", "5b8dA", "DB02546"), ("liothyronine at THRB chain", "1n46A", "DB00279"), ("liothyronine at THRA chain", "3ilzA", "DB00279")]
    print("column-order sanity (percentile of the compound among all 2449 at that protein row; score):")
    for lab, row, d in sanity:
        if row in zi:
            print("  ", lab, row, d, *["%.1f %.3f" % pct(row, d)])

    # ---------- (4) the small set ----------
    PROT_SET = ["HDAC1", "HDAC2", "HDAC3", "HDAC4", "HDAC6", "HDAC7", "HDAC8", "EZH2", "BRD4", "THRA", "THRB", "KEAP1", "MAPK1", "MAPK3", "AHR", "CDK4", "CDK6", "GSK3B", "GRIN1", "GRIN2B", "SIRT1", "SIRT2", "SIRT3", "KDM1A", "DNMT1", "EGLN1", "EGLN2", "HIF1A", "LDHA", "PKM"]
    ident_by = {x["drugbank_id"]: x for x in ident}
    rows = []
    for d, role, src in SET8:
        x = ident_by[d]
        for g in PROT_SET:
            for rid in gz.get(g, []):
                v = Z[zi[rid], dbi[d]]
                col = Z[zi[rid]]
                rank = int((col > v).sum()) + 1
                rows.append(dict(drugbank_id=d, compound=x["cando_name"], role=role, role_source=src, catalogue_family=x["family_id"], gene=g, matrix_row=rid, cxp_score=f"{v:.3f}", rank_among_2449=rank,
                                 percentile=f"{100 * (col < v).mean():.1f}", legend_signed_actions_at_gene=";".join(sorted({f"{r['mean_sign']}" for fm in x["family_id"].split(";") for r in fam_act.get(fm, []) if r["target_symbol"].upper() == g})) or "none_in_family_table",
                                 note="score = max over predicted-pocket ligands of ECFP4-Dice(compound, ligand) x COACH site confidence; carries no direction (not agonist/antagonist/inhibitor), no potency, no selectivity, no exposure"))
    with open(out / "comparison.tsv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    # whole-signature similarity over the proteins covered: cosine of z-scored columns across ALL rows (8 384) vs over the 30-gene subset
    allz = (Z - Z.mean(1, keepdims=True)) / (Z.std(1, keepdims=True) + 1e-9)
    sub_rows = [zi[r] for g in PROT_SET for r in gz.get(g, [])]
    def cos(u, v):
        return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v) + 1e-12))
    print("\nprofile similarity (cosine of per-protein z-scored scores) between the eight compounds; full signature (all rows) / 30-gene subset:")
    res = []
    for d1, *_ in SET8:
        for d2, *_ in SET8:
            if d1 < d2:
                a1, a2 = allz[:, dbi[d1]], allz[:, dbi[d2]]
                s1, s2 = allz[sub_rows, dbi[d1]], allz[sub_rows, dbi[d2]]
                # rank of d2 among all 2449 compounds by full-signature cosine to d1
                M = allz / (np.linalg.norm(allz, axis=0, keepdims=True) + 1e-12)
                sims = M.T @ M[:, dbi[d1]]
                rk = int((sims > sims[dbi[d2]]).sum()) + 1
                res.append(dict(a=ident_by[d1]["cando_name"], b=ident_by[d2]["cando_name"], cosine_all_rows=f"{cos(a1, a2):.3f}", cosine_30_gene_subset=f"{cos(s1, s2):.3f}", rank_of_b_in_a_neighbours_all_rows=rk))
    with open(out / "profile_similarity.tsv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(res)
    for r in res:
        print(" ", r["a"], "~", r["b"], r["cosine_all_rows"], r["cosine_30_gene_subset"], "rank", r["rank_of_b_in_a_neighbours_all_rows"])

    # ---------- (5) sign-convention sensitivity: nearest neighbours of each compound's THRA/THRB/HDAC-subset profile under the two readings ----------
    # reading A (the CANDO reading): high score = resembles a ligand predicted at the pocket.  reading B (a hypothetical inhibition-like reading: LOW score = more of the action): nobody
    # published B; it is computed only to show how far the neighbours move if one convention is assumed wrongly.
    sens = []
    for d, role, src in SET8:
        subs = {"TR": ["THRA", "THRB"], "HDAC": ["HDAC1", "HDAC2", "HDAC3", "HDAC4", "HDAC6", "HDAC7", "HDAC8"]}
        for lab, gl in subs.items():
            r_ = [zi[r] for g in gl for r in gz.get(g, [])]
            if not r_:
                continue
            v = Z[r_].mean(0)
            ordA = np.argsort(-v)[:25]
            ordB = np.argsort(v)[:25]
            sens.append(dict(compound=ident_by[d]["cando_name"], subset=lab, n_rows=len(r_), own_score=f"{v[dbi[d]]:.3f}", own_rank_reading_A_high_is_more=int((v > v[dbi[d]]).sum()) + 1,
                             own_rank_reading_B_low_is_more=int((v < v[dbi[d]]).sum()) + 1, top25_A=";".join(db[k]["GENERIC_NAME"] for k in ordA[:8]), top25_B=";".join(db[k]["GENERIC_NAME"] for k in ordB[:8]),
                             overlap_top25_A_vs_B=len(set(ordA) & set(ordB))))
    with open(out / "sign_sensitivity.tsv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sens[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(sens)
    print("\nsign sensitivity written:", len(sens), "rows")

    # ---------- (6) recovery of LEGEND's own signed actions by the matrix, and the sign question tested rather than assumed ----------
    def auc(v, m):
        """P(score of a known compound > score of an unknown one), ties half; rank-sum form with average ranks."""
        u, inv, cnt = np.unique(v, return_inverse=True, return_counts=True)
        avg = (np.cumsum(cnt) - (cnt - 1) / 2.0)[inv]
        n1, n0 = int(m.sum()), int((~m).sum())
        return float((avg[m].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0)) if n1 and n0 else float("nan")
    fam_of = [x["family_id"].split(";") if x["join_status"] == "MATCH_ONE_FAMILY" else [] for x in ident]
    rec = []
    for g in PROT_SET:
        for rid in gz.get(g, []):
            v = Z[zi[rid]]
            for lab, test in (("any_signed_action", lambda sg: True), ("inhibition_like_sign_negative", lambda sg: sg < 0), ("activation_like_sign_positive", lambda sg: sg > 0)):
                m = np.zeros(len(db), dtype=bool)
                for j, fl in enumerate(fam_of):
                    for fm in fl:
                        if any(r_["target_symbol"].upper() == g and test(float(r_["mean_sign"])) for r_ in fam_act.get(fm, [])):
                            m[j] = True
                if m.sum() >= 2:
                    top = np.argsort(-v)[:25]
                    rec.append(dict(gene=g, matrix_row=rid, subset=lab, n_known=int(m.sum()), auc=f"{auc(v, m):.3f}", median_percentile_of_known=f"{100 * np.median([(v < v[j]).mean() for j in np.where(m)[0]]):.1f}",
                                    known_in_top25=int(m[top].sum()), top25_are_known_fraction=f"{m[top].mean():.2f}"))
    with open(out / "recovery.tsv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rec[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rec)
    any_ = [float(r_["auc"]) for r_ in rec if r_["subset"] == "any_signed_action"]
    print("recovery of LEGEND signed actions: rows", len(any_), "median AUC", float(np.median(any_)) if any_ else None, "min/max", (min(any_), max(any_)) if any_ else None)
    for lab in ("inhibition_like_sign_negative", "activation_like_sign_positive"):
        xs = [float(r_["auc"]) for r_ in rec if r_["subset"] == lab]
        print("  ", lab, "rows", len(xs), "median AUC", float(np.median(xs)) if xs else None)



if __name__ == "__main__":
    main()
