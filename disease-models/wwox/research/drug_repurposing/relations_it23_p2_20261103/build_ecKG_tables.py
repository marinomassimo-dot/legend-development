"""Build the extract, the digest and the novelty tables from the fetched EC-KG rows.

Called by reproduce_ecKG_wwox.py (stage `build`). Reads only local files under --work.
Evidence class rule (decided per edge, in this order; first match wins):
  PREDICTION  knowledge_level == 'prediction', or agent_type == 'text_mining_agent',
              or primary source in TEXT_MINED, or extraction_confidence_score present
  OBSERVED    knowledge_assertion with a literature or experiment anchor: at least one PMID/DOI in
              `publications`, or an `affinity` value, or a `supporting_study_method_type`
  ANNOTATION  every other edge (database or ontology assertion with no stated anchor, statistical
              pipelines such as FAERS, logical entailment, PrimeKG edges whose primary source is the
              aggregator itself)
This is a heuristic on the declared fields; no edge was re-read at its source.
"""
import csv, gzip, hashlib, json, os, re
from collections import defaultdict, Counter

WWOX = "NCBIGene:51741"
TEXT_MINED = {"infores:semmeddb", "infores:text-mining-provider-targeted"}
LEGEND_NATIVE = {"infores:chembl", "infores:gtopdb", "infores:dgidb"}      # the generator's compound side
# claim sources that DGIdb itself aggregates: a row from these may be a second copy of a LEGEND row
DGIDB_CLAIM_SOURCES = {"infores:drugbank", "infores:drugcentral", "infores:bindingdb", "infores:pharos"}
# origins that are themselves aggregators or are known to re-publish the above: never counted as independent
COPY_PRONE = DGIDB_CLAIM_SOURCES | {"infores:primekg", "infores:hetionet", "infores:chebi", "infores:ncit"}
# licence class per primary source, from docs.dev.everycure.org/releases/primary_knowledge_sources (read 2026-11-03)
PERMISSIVE = {  # CC0 / CC BY / MIT / Apache / BSD / public domain, as stated on that page
    "infores:ncit": "CC BY 4.0", "infores:hmdb": "CC BY 4.0", "infores:dgidb": "MIT",
    "infores:reactome": "CC0 1.0", "infores:intact": "CC BY 4.0", "infores:hetionet": "CC BY 4.0",
    "infores:lincs": "CC BY 4.0", "infores:faers": "Public Domain / CC0 1.0", "infores:diseases": "CC BY 4.0",
    "infores:mondo": "CC BY 4.0", "infores:efo": "Apache 2.0", "infores:uniprot": "CC BY 4.0",
    "infores:signor": "CC BY 4.0", "infores:goa": "CC BY 4.0", "infores:go-plus": "CC BY 4.0",
    "infores:drugmechdb": "CC BY 4.0", "infores:bgee": "CC0 1.0", "infores:ensembl-gene": "Apache 2.0",
    "infores:uberon": "CC BY 3.0", "infores:chebi": "CC BY 4.0", "infores:repodb": "CC BY 4.0",
    "infores:unichem": "CC BY 4.0", "infores:text-mining-provider-targeted": "CC BY 4.0",
    "infores:cl": "CC BY 4.0", "infores:monarchinitiative": "BSD-3-Clause", "infores:panther": "CC BY 4.0",
    "infores:pr": "CC BY 4.0", "infores:foodon": "CC BY 4.0", "infores:genepio": "CC BY 3.0",
}
# everything else is RESTRICTED for redistribution here: share-alike (ChEMBL, GtoPdb, DrugCentral,
# BindingDB-ChEMBL), non-commercial (DrugBank, SIDER, PhosphoSitePlus), UMLS-licensed (SemMedDB, MeSH,
# RxNorm, MED-RT, NDDF, PDQ, VANDF, UMLS), custom (CTD, HPO, OMIM, KEGG, eRAM, PathWhiz), aggregator or
# not stated (PrimeKG, Pharos, Ubergraph, EPSD, DisGeNET "most sources").


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def ev_class(r):
    if r["knowledge_level"] == "prediction" or r["agent_type"] == "text_mining_agent" \
            or r["primary_knowledge_source"] in TEXT_MINED or r["extraction_confidence_score"] is not None:
        return "PREDICTION"
    pubs = [p for p in (r["publications"] or []) if p.startswith(("PMID:", "DOI:", "doi:"))]
    if r["knowledge_level"] == "knowledge_assertion" and (pubs or r["affinity"] is not None
                                                          or r["supporting_study_method_type"]):
        return "OBSERVED"
    return "ANNOTATION"


def sign_of(r, compound_is_subject):
    """+1 / -1 / 0 plus the level the sign is about. Only activity-level signs are comparable to LEGEND."""
    if not compound_is_subject:
        return 0, ""
    d, asp = r["object_direction_qualifier"], r["object_aspect_qualifier"]
    if d in ("decreased", "downregulated"): s = -1
    elif d in ("increased", "upregulated"): s = 1
    else: return 0, ""
    lvl = asp or "unspecified"
    return (s if lvl in ("activity", "activity_or_abundance") else 0), lvl


def run(a):
    import duckdb
    W = a.work
    con = duckdb.connect()
    con.execute(f"CREATE VIEW nd AS SELECT * FROM '{W}/nodes_slim.parquet'")
    con.execute(f"CREATE TABLE e AS SELECT * FROM '{W}/edges_full_target.parquet'")
    comp = {r[0]: r for r in con.execute(
        f"SELECT n.id,n.name,n.category,n.equivalent_identifiers FROM nd n WHERE n.id IN "
        f"(SELECT id FROM read_csv('{W}/matched_compounds.tsv',delim='\t'))").fetchall()}
    n1 = {r[0] for r in con.execute(f"SELECT id FROM '{W}/n1.parquet'").fetchall()}
    n2 = {r[0] for r in con.execute(f"SELECT id FROM '{W}/n2.parquet'").fetchall()}

    # --- LEGEND side ---------------------------------------------------------------------------
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from reproduce_ecKG_wwox import legend_compounds
    rows, comps, fam_name = legend_compounds(a.repo)
    fam_names = {f: {norm(b) for b in bs} | {norm(fam_name.get(f, ""))} for f, bs in comps.items()}
    fam_chembl = {f: "CHEMBL.COMPOUND:" + f.split(":")[-1] for f in comps if f.startswith("FAM:CAT:CHEMBL")}
    node_fams = defaultdict(set)
    for cid, (_, name, cat, eqs) in comp.items():
        nm, eqs = norm(name), set(eqs or [])
        for f in comps:
            if nm in fam_names[f] or (f in fam_chembl and fam_chembl[f] in eqs):
                node_fams[cid].add(f)
    act = {}      # (family, hgnc) -> sign
    base = os.path.join(a.repo, "generation_it21_p2_20261103/results/actions")
    with gzip.open(os.path.join(base, "family_actions.tsv.gz"), "rt") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["family_id"] in comps: act[(r["family_id"], r["hgnc_id"])] = float(r["mean_sign"])
    anyt = set()
    with gzip.open(os.path.join(base, "family_targets_any.tsv.gz"), "rt") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["family_id"] in comps: anyt.add((r["family_id"], r["target_symbol"]))
    sym_of_hgnc = {}
    with gzip.open(os.path.join(base, "family_actions.tsv.gz"), "rt") as f:
        for r in csv.DictReader(f, delimiter="\t"): sym_of_hgnc[r["hgnc_id"]] = r["target_symbol"]

    # --- node info for the other endpoint --------------------------------------------------------
    ids = [r[0] for r in con.execute("SELECT subject FROM e UNION SELECT object FROM e").fetchall()]
    con.execute("CREATE TABLE ids(id VARCHAR)"); con.executemany("INSERT INTO ids VALUES (?)", [(i,) for i in ids])
    info = {}
    for cid, name, cat, up, eqs in con.execute(
            "SELECT n.id,n.name,n.category,n.upstream_data_source,n.equivalent_identifiers FROM nd n JOIN ids USING(id)").fetchall():
        hg = next((x for x in (eqs or []) if x.startswith("HGNC:")), "")
        info[cid] = (name, cat, ";".join(up or []), hg)

    cols = [d[0] for d in con.execute("SELECT * FROM e LIMIT 0").description]
    GENE, DIS = {"biolink:Gene", "biolink:Protein"}, {"biolink:Disease", "biolink:PhenotypicFeature",
                                                      "biolink:DiseaseOrPhenotypicFeature"}
    ext_rows, digest_rows = [], []
    pairs = defaultdict(lambda: {"origins": set(), "ev": Counter(), "signs": [], "preds": Counter(), "pubs": set(),
                                 "aggs": set(), "perm_origins": set(), "solid": set(), "lvl": set(), "solid_pubs": set()})
    wleg = defaultdict(list)
    cdis = Counter()
    ev_by_src = Counter()
    for t in con.execute("SELECT * FROM e").fetchall():
        r = dict(zip(cols, t))
        s, o = r["subject"], r["object"]
        cs, co = s in comp, o in comp
        other = o if cs else s
        ev = ev_class(r); src = r["primary_knowledge_source"]; ev_by_src[(src, ev)] += 1
        oinfo = info.get(other, ("", "", "", ""))
        wwox_inc = WWOX in (s, o)
        hood = "W" if wwox_inc else ("N1" if other in n1 else ("N2" if other in n2 else ""))
        # (1) neighbourhood extract / digest
        if wwox_inc or ((cs or co) and hood in ("N1", "N2")):
            lic = PERMISSIVE.get(src)
            key = "|".join([s, r["predicate"], o, src, r["qualified_predicate"] or "", r["object_direction_qualifier"] or "",
                            ",".join(sorted(r["publications"] or []))])
            rec = [s, info.get(s, comp.get(s, ("", "")))[0] if s in info else (comp[s][1] if s in comp else ""),
                   r["predicate"], o, info[o][0] if o in info else (comp[o][1] if o in comp else ""),
                   r["qualified_predicate"] or "", r["subject_aspect_qualifier"] or "", r["subject_direction_qualifier"] or "",
                   r["object_aspect_qualifier"] or "", r["object_direction_qualifier"] or "",
                   r["species_context_qualifier"] or "", r["disease_context_qualifier"] or "",
                   src, ";".join(r["aggregator_knowledge_source"] or []), ";".join((r["publications"] or [])[:8]),
                   len(r["publications"] or []), r["knowledge_level"] or "", r["agent_type"] or "", ev,
                   ";".join(r["upstream_data_source"] or []), hood,
                   "" if r["extraction_confidence_score"] is None else round(r["extraction_confidence_score"], 3),
                   "" if r["affinity"] is None else round(r["affinity"], 3), r["affinity_parameter"] or "", lic or ""]
            if lic:
                ext_rows.append(rec)
            else:
                digest_rows.append([hashlib.sha256(key.encode()).hexdigest(), s, o, r["predicate"], src,
                                    ";".join(r["aggregator_knowledge_source"] or []), ev, hood, len(r["publications"] or [])])
        if wwox_inc and other != WWOX:
            wleg[other].append((r["predicate"] + ("/" + r["object_direction_qualifier"] if r["object_direction_qualifier"] else ""),
                                src, ev, len([x for x in (r["publications"] or []) if x.startswith("PMID:")])))
        # (2) compound-gene/protein pairs and compound-disease counts (whole fetched set)
        if cs != co and oinfo[1] in GENE:
            c = s if cs else o
            p = pairs[(c, other)]
            p["origins"].add(src); p["ev"][ev] += 1; p["preds"][r["predicate"]] += 1
            sg, lvl = sign_of(r, cs)
            if sg: p["signs"].append((sg, src))
            if ev != "PREDICTION" and not sg: pass
            p["pubs"].update(x for x in (r["publications"] or []) if x.startswith("PMID:"))
            p["aggs"].update(r["aggregator_knowledge_source"] or [])
            if src in PERMISSIVE: p["perm_origins"].add(src)
            if ev != "PREDICTION":
                p["solid"].add(src); p["solid_pubs"].update(x for x in (r["publications"] or []) if x.startswith("PMID:"))
            if lvl: p["lvl"].add(lvl)
        elif cs != co and oinfo[1] in DIS:
            cdis[(r["predicate"], ev)] += 1

    # --- slimming rule for what enters git: W-incident rows and compound-N1 rows; compound-N2 rows stay in --work.
    def keep(r): return r[20] in ("W", "N1")
    ext_keep = [r for r in ext_rows if keep(r)]
    dig_keep = [r for r in digest_rows if r[7] in ("W", "N1")]
    for nm, rows_, srt in (("full_extract_permissive_W_N1_N2.tsv", ext_rows, lambda x: (x[20], x[0], x[3])),
                           ("full_digest_restricted_W_N1_N2.tsv", digest_rows, lambda x: x[0])):
        with open(os.path.join(a.work, nm), "w", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            for r in sorted(rows_, key=srt): w.writerow(r)
    dig_summary = Counter((r[4], r[6], r[7]) for r in digest_rows)
    hdr = ["subject", "subject_name", "predicate", "object", "object_name", "qualified_predicate", "subject_aspect",
           "subject_direction", "object_aspect", "object_direction", "species_context", "disease_context",
           "primary_knowledge_source", "aggregator_knowledge_source", "publications_first8", "n_publications",
           "knowledge_level", "agent_type", "evidence_class", "upstream_data_source", "hood",
           "extraction_confidence", "affinity", "affinity_parameter", "source_licence_stated"]
    with open(os.path.join(a.out, "extract_ecKG_wwox.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(hdr)
        for r in sorted(ext_keep, key=lambda x: (x[20], x[0], x[3], x[2], x[12])): w.writerow(r)
    with open(os.path.join(a.out, "extract_digest_restricted.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["row_sha256", "subject", "object", "predicate", "primary_knowledge_source",
                    "aggregator_knowledge_source", "evidence_class", "hood", "n_publications"])
        for r in sorted(dig_keep): w.writerow(r)
    with open(os.path.join(a.out, "extract_digest_summary.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["primary_knowledge_source", "evidence_class", "hood", "n_rows_restricted_licence"])
        for k, v in sorted(dig_summary.items()): w.writerow(list(k) + [v])
    used = {r[0] for r in ext_keep} | {r[3] for r in ext_keep} | {r[1] for r in dig_keep} | {r[2] for r in dig_keep}
    with open(os.path.join(a.out, "nodes_ecKG_wwox.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["id", "name", "category", "upstream_data_source", "hood"])
        w.writerow([WWOX, info.get(WWOX, ("",))[0], info.get(WWOX, ("", ""))[1], info.get(WWOX, ("", "", ""))[2], "W"])
        for n in sorted((n1 | n2) & used):
            if n in info: w.writerow([n, info[n][0], info[n][1], info[n][2], "N1" if n in n1 else "N2"])

    # --- novelty ---------------------------------------------------------------------------------
    out_rows, status_ct, cand = [], Counter(), []
    legend_pairs_total = legend_pairs_found = 0
    for (c, g), p in sorted(pairs.items()):
        hg, sym = info[g][3], sym_of_hgnc.get(info[g][3], "")
        fams = node_fams.get(c, set())
        legend_signed = [(f, act[(f, hg)]) for f in fams if (f, hg) in act]
        legend_any = [f for f in fams if sym and (f, sym) in anyt]
        eck_signs = {s for s, _ in p["signs"]}
        origins = sorted(p["origins"]); solid = sorted(p["solid"])
        new_origin = [x for x in origins if x not in LEGEND_NATIVE]
        if not fams: st = "NO_LEGEND_FAMILY_MATCH"
        elif legend_signed:
            ls = {1 if v > 0 else -1 for _, v in legend_signed if v}
            if not eck_signs: st = "IN_LEGEND_ECKG_UNSIGNED"
            elif eck_signs <= ls: st = "IN_LEGEND_SAME_SIGN"
            elif not (eck_signs & ls): st = "IN_LEGEND_OPPOSITE_SIGN"
            else: st = "IN_LEGEND_MIXED_SIGN"
        elif legend_any: st = "IN_LEGEND_UNSIGNED_ONLY"
        elif not hg: st = "TARGET_NOT_MAPPED_TO_HGNC"
        elif set(origins) & LEGEND_NATIVE: st = "NEW_PAIR_LEGEND_ORIGIN_PRESENT"
        elif set(solid) - COPY_PRONE: st = "NEW_PAIR_INDEPENDENT_ORIGIN"
        elif solid: st = "NEW_PAIR_COPY_PRONE_ORIGIN_ONLY"
        else: st = "NEW_PAIR_PREDICTION_ONLY"
        status_ct[st] += 1
        best = ("OBSERVED" if p["ev"]["OBSERVED"] else "ANNOTATION" if p["ev"]["ANNOTATION"] else "PREDICTION")
        hood = "W" if False else ("N1" if g in n1 else ("N2" if g in n2 else ""))
        row = [c, comp[c][1], g, info[g][0], hg, sym, ";".join(sorted(fams)), st, len(origins), len(solid),
               ";".join(o for o in origins if o in PERMISSIVE), len([o for o in origins if o not in PERMISSIVE]),
               ";".join(sorted(p["aggs"])), "+".join("%s%d" % (k[0], v) for k, v in sorted(p["ev"].items())), best,
               ",".join("%+d" % s for s in sorted(eck_signs)), ";".join(sorted(p["lvl"])), len(p["pubs"]),
               ";".join(sorted(p["preds"])), ";".join(sorted(DGIDB_CLAIM_SOURCES & set(origins))), hood, ";".join(solid)]
        if st.startswith("IN_LEGEND") or st in ("NEW_PAIR_LEGEND_ORIGIN_PRESENT", "NEW_PAIR_INDEPENDENT_ORIGIN"):
            out_rows.append(row)
        if st == "NEW_PAIR_INDEPENDENT_ORIGIN" and g in n1 and wleg.get(g):
            wl = [x for x in wleg[g] if x[2] != "PREDICTION"]
            if wl:
                cand.append((len(set(solid) - COPY_PRONE), 1 if (eck_signs and "activity" in p["lvl"]) else 0, len(p["solid_pubs"]), len({x[1] for x in wl}), c, g, p, wl, hg))
    # LEGEND-side recovery: how many of the generator's signed pairs of matched families EC-KG also carries
    recov = {(c, info[g][3]) for (c, g) in pairs if info[g][3]}
    for f in {f for s in node_fams.values() for f in s}:
        for (ff, hg), v in act.items():
            if ff == f:
                legend_pairs_total += 1
                if any((c, hg) in recov for c in comp if f in node_fams.get(c, ())): legend_pairs_found += 1
    with open(os.path.join(a.out, "novelty.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["compound_id", "compound_name", "target_id", "target_name", "target_hgnc", "target_symbol_in_legend",
                    "legend_families", "status", "n_origins_primary_sources", "n_origins_non_prediction",
                    "origins_permissive_licence", "n_origins_restricted_licence", "aggregators", "evidence_edges",
                    "best_evidence_class", "eckg_activity_sign", "sign_levels_seen", "n_pmids", "predicates",
                    "possible_copy_of_legend_origin", "target_hood", "origins_non_prediction"])
        for r in out_rows: w.writerow(r)
    # top 10: one row per (compound, target), at most 2 per target and 2 per compound
    cand.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3], x[4], x[5]))
    top, per_t, per_c = [], Counter(), Counter()
    for n_sol, sg, npm, nw, c, g, p, wl, hg in cand:
        if per_t[g] >= 2 or per_c[c] >= 2: continue
        per_t[g] += 1; per_c[c] += 1
        top.append([len(top) + 1, comp[c][1], c, info[g][0], g, hg,
                    ";".join(sorted(p["solid"])), ";".join(sorted(p["preds"])),
                    ",".join("%+d" % s for s in sorted({x for x, _ in p["signs"]})), ";".join(sorted(p["lvl"])),
                    len(p["solid_pubs"]), ";".join(sorted(p["aggs"])),
                    ";".join(sorted({"%s[%s,%s,pmids=%d]" % x for x in wl})),
                    "path in a graph, not a causal chain"])
        if len(top) == 10: break
    with open(os.path.join(a.out, "top10_new_relations.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["rank", "compound", "compound_id", "bridge_node", "bridge_id", "bridge_hgnc", "compound_bridge_origins_non_prediction",
                    "compound_bridge_predicates", "activity_sign", "sign_level", "n_pmids", "aggregators",
                    "bridge_to_WWOX_legs", "caveat"])
        for r in top: w.writerow(r)
    json.dump({"pair_status": status_ct, "n_pairs": len(pairs), "compound_nodes_matched": len(comp),
               "compound_nodes_with_family": sum(1 for c in comp if node_fams.get(c)),
               "families_matched": len({f for s in node_fams.values() for f in s}), "families_in_proposals": len(comps),
               "legend_signed_pairs_of_matched_families": legend_pairs_total,
               "legend_signed_pairs_also_in_eckg_as_any_edge": legend_pairs_found,
               "new_pair_new_origin_candidates_with_wwox_neighbour_bridge": len(cand),
               "compound_disease_edge_counts": {"%s|%s" % k: v for k, v in cdis.most_common()},
               "evidence_by_source": {"%s|%s" % k: v for k, v in ev_by_src.most_common()},
               "extract_rows_full_permissive": len(ext_rows), "extract_rows_kept": len(ext_keep),
               "digest_rows_full": len(digest_rows), "digest_rows_kept": len(dig_keep), "n1": len(n1), "n2": len(n2)},
              open(os.path.join(a.out, "novelty_summary.json"), "w"), indent=1, sort_keys=True)
    print(json.dumps({"pair_status": status_ct, "extract": len(ext_keep), "digest": len(dig_keep), "top": len(top)}))
