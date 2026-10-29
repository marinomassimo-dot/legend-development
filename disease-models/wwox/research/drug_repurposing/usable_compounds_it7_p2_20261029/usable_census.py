#!/usr/bin/env python3
"""Census of how much of the compound catalogue two candidate predictive methods could use (IT7 P2, roadmap R2).

  M-sig  transcriptional-signature reversal: needs a compound with an L1000/LINCS compound signature (pert_type trt_cp) in a
         stated cell context (cell line, concentration, time).
  M-net  light signed-network method: needs a documented action with a SIGN (up/down on the target) on a human target with a
         stable identifier (ChEMBL target id + UniProt, or an HGNC concept id).

Counts source records -> families -> documented action -> usable per method -> overlap, writes counts.json, the pilot tables and
the per-record flag table. It evaluates NO compound (actually evaluated = 0). Offline, deterministic, standard library only;
it reads the committed catalogue plus public GEO metadata files that must be supplied.

  usable_census.py run --geo92 DIR --geo70 DIR [--out DIR] [--catalog PATH]
  usable_census.py --help

Inputs: DIR geo92 holds GSE92742_Broad_LINCS_{pert_info,sig_info,cell_info}.txt.gz and GSE92742_SHA512SUMS.txt.gz;
DIR geo70 holds GSE70138_Broad_LINCS_{pert_info_2017-03-06,sig_info_2017-03-06,cell_info_2017-04-28}.txt.gz and
GSE70138_SHA512SUMS.txt.gz (both checksummed here). The gitignored catalogue cache (env LEGEND_CATALOG_CACHE) supplies GtoPdb
interaction detail and ChEMBL mechanism comments for the pilot tables; without it those fields read UNKNOWN (counts unchanged).
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import hashlib
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))

NEURAL_STRICT = ("NPC", "NPC.CAS9", "NPC.TAK", "NEU", "NEU.KCL", "MNEU.E")
NEURAL_EXTENDED_EXTRA = ("FIBRNPC",)
GROUPS = ("ChEMBL", "GtoPdb", "DGIdb_other")
UNSTATED = {"", "other/unknown", "unknown", "none", None}


def sha512(p: Path) -> str:
    h = hashlib.sha512()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def tab(p: Path):
    return csv.DictReader(gzip.open(p, "rt", encoding="utf-8"), delimiter="\t")


def norm_dose(v: str) -> str:
    """'10 µM' (phase I) and '10.0 um' (phase II) are the same dose: number via %g, unit with micro sign as u."""
    if v in ("-666", ""):
        return "UNKNOWN"
    parts = v.replace("\u00b5", "u").replace("\u03bc", "u").split()
    try:
        num = f"{float(parts[0]):g}"
    except (ValueError, IndexError):
        return v
    unit = parts[1] if len(parts) > 1 else ""
    return f"{num} {'uM' if unit.lower() == 'um' else unit}".strip()


def lincs_load(d92: Path, d70: Path):
    """-> (contexts, pert_key, files) ; contexts[pert_id][(cell, dose, time)] = n signatures (trt_cp only)."""
    files = {}
    spec = [(d92, "GSE92742", {"pert": "GSE92742_Broad_LINCS_pert_info.txt.gz", "sig": "GSE92742_Broad_LINCS_sig_info.txt.gz",
                               "cell": "GSE92742_Broad_LINCS_cell_info.txt.gz"}),
            (d70, "GSE70138", {"pert": "GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz", "sig": "GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz",
                               "cell": "GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz"})]
    ctx = collections.defaultdict(collections.Counter)
    key, cells, series = {}, {}, collections.defaultdict(set)
    nsig = collections.Counter()
    for d, sid, fn in spec:
        sums = {}
        for line in gzip.open(d / f"{sid}_SHA512SUMS.txt.gz", "rt"):
            p = line.split()
            if len(p) == 2:
                sums[p[1]] = p[0]
        for k, f in fn.items():
            hx = sha512(d / f)
            ok = sums.get(f) == hx
            files[f] = {"series": sid, "sha512": hx, "matches_series_SHA512SUMS": ok}
            if not ok:
                raise SystemExit(f"checksum mismatch: {f}")
        for r in tab(d / fn["cell"]):
            cells.setdefault(r["cell_id"], r)
        for r in tab(d / fn["pert"]):
            if r["pert_type"] == "trt_cp":
                ik = r["inchi_key"]
                if ik not in ("-666", ""):
                    key[r["pert_id"]] = ik
                else:
                    key.setdefault(r["pert_id"], "")
        for r in tab(d / fn["sig"]):
            if r["pert_type"] != "trt_cp":
                continue
            dose = norm_dose(r["pert_idose"])
            tm = r["pert_itime"] if r["pert_itime"] not in ("-666", "") else "UNKNOWN"
            ctx[r["pert_id"]][(r["cell_id"], dose, tm)] += 1
            series[r["pert_id"]].add(sid)
            nsig[sid] += 1
    return ctx, key, files, cells, nsig, series


def gtopdb_index(cache: Path | None):
    """(ligand id, target id) -> list of rows; empty when the cache is absent."""
    out = collections.defaultdict(list)
    if not cache or not (cache / "gtopdb/interactions.csv").exists():
        return out, False
    with open(cache / "gtopdb/interactions.csv", encoding="utf-8", newline="") as fh:
        fh.readline()  # release comment line
        for r in csv.DictReader(fh):
            out[(r["Ligand ID"], r["Target ID"])].append(r)
    return out, True


def mech_index(cache: Path | None):
    out = collections.defaultdict(list)
    if not cache or not (cache / "chembl/mechanisms.jsonl.gz").exists():
        return out, False
    for line in gzip.open(cache / "chembl/mechanisms.jsonl.gz", "rt", encoding="utf-8"):
        m = json.loads(line)
        out[(m["molecule_chembl_id"], m["target_chembl_id"])].append(m)
        if m.get("parent_molecule_chembl_id") and m["parent_molecule_chembl_id"] != m["molecule_chembl_id"]:
            out[(m["parent_molecule_chembl_id"], m["target_chembl_id"])].append(m)
    return out, True


def mol_index(cache: Path | None):
    out = {}
    if not cache or not (cache / "chembl/molecules.jsonl.gz").exists():
        return out, False
    for line in gzip.open(cache / "chembl/molecules.jsonl.gz", "rt", encoding="utf-8"):
        m = json.loads(line)
        out[m["molecule_chembl_id"]] = {k: m.get(k) for k in ("oral", "parenteral", "topical", "availability_type", "black_box_warning", "withdrawn_flag")}
    return out, True


def row_usability(rs, idx, e, t):
    """Classify one catalogue target row. Returns dict or None for rows of no interest."""
    src = t["source"]
    chembl = src.startswith("ChEMBL")
    raw = t.get("action_type") if chembl else t.get("interaction_type")
    stated = raw not in UNSTATED
    if not chembl and (t.get("interaction_type_state") or "").startswith("CONFLICT"):
        stated = False
    sign = rs.action_direction(raw) if stated else "unresolved"
    excl = rs.artefact_reason(e, t, idx.artefacts, idx.early)
    if (e["name"] or "").strip().lower() in rs.PLACEHOLDER_NAMES:
        excl = excl or "placeholder"
    if chembl:
        group = "ChEMBL"
        stable = t.get("organism") == "Homo sapiens" and bool(t.get("uniprot")) and bool(t.get("target_id"))
        symbol = ";".join(t.get("gene_symbols") or [])
        tid = t.get("target_id")
        scope = "single_protein" if t.get("target_type") in (None, "SINGLE PROTEIN") else "complex_or_group"
    else:
        group = "GtoPdb" if t.get("claim_source") == "GuideToPharmacology" else "DGIdb_other"
        hg = (t.get("gene_concept_id") or "").lower()
        stable = hg.startswith("hgnc:")
        symbol = t.get("gene") or ""
        tid = hg
        scope = rs.evidence_scope(src, t)[0]
    return {"group": group, "raw": raw, "stated": stated, "sign": sign, "excluded": excl, "stable": stable, "symbol": symbol,
            "target_id": tid, "scope": scope, "claim_source": t.get("claim_source") or "ChEMBL curated mechanism"}


def run(a) -> int:
    import compound_catalog as cc
    import repurposing_search as rs
    cache = Path(os.environ["LEGEND_CATALOG_CACHE"]) if os.environ.get("LEGEND_CATALOG_CACHE") else None
    entries = cc.load(Path(a.catalog))
    idx = rs.Index(entries, rs.load_artefacts())
    fam = idx.family
    n_rec = len(entries)
    fam_ids = sorted(set(fam.values()))
    by_id = idx.by_id

    ctx, pkey, gfiles, cells, nsig, pseries = lincs_load(Path(a.geo92), Path(a.geo70))
    skel_to_perts = collections.defaultdict(set)
    perts_no_key = 0
    for p, k in pkey.items():
        if k:
            skel_to_perts[k.split("-")[0]].add(p)
        else:
            perts_no_key += 1
    full_to_perts = collections.defaultdict(set)
    for p, k in pkey.items():
        if k:
            full_to_perts[k].add(p)
    neural_strict = set(NEURAL_STRICT)
    neural_ext = neural_strict | set(NEURAL_EXTENDED_EXTRA)

    # ---- per record
    rec = {}
    row_detail = {}  # record id -> usable signed rows (for the pilot)
    raw_counts = collections.Counter()
    claim_src_usable = collections.Counter()
    for e in entries:
        rows = [(t, row_usability(rs, idx, e, t)) for t in e["targets"]]
        raw_counts["rows_total"] += len(rows)
        any_t = bool(rows)
        stated_raw = any(u["stated"] for _, u in rows)
        stated_ok = [u for _, u in rows if u["stated"] and not u["excluded"]]
        signed_ok = [(t, u) for t, u in rows if u["stated"] and not u["excluded"] and u["sign"] in ("up", "down") and u["stable"]]
        for t, u in rows:
            if u["excluded"]:
                raw_counts["rows_excluded_by_catalogue_artefact_rules"] += 1
            if u["stated"]:
                raw_counts["rows_with_stated_action"] += 1
            if u["stated"] and u["sign"] in ("up", "down"):
                raw_counts["rows_signed_before_exclusion_and_identity"] += 1
        for t, u in signed_ok:
            claim_src_usable[u["claim_source"]] += 1
        groups = sorted({u["group"] for _, u in signed_ok})
        sk = (e.get("ids") or {}).get("skeleton_key")
        full = (e.get("ids") or {}).get("inchikey")
        perts = set(skel_to_perts.get(sk, ())) if sk else set()
        perts_full = set(full_to_perts.get(full, ())) if full else set()
        sig_any = {p for p in perts if ctx.get(p)}
        sig_strict = {p for p in sig_any if any(c[0] in neural_strict for c in ctx[p])}
        sig_ext = {p for p in sig_any if any(c[0] in neural_ext for c in ctx[p])}
        rec[e["id"]] = {"family": fam[e["id"]], "any_target_row": any_t, "stated_action_raw": stated_raw, "stated_action_ok": bool(stated_ok),
                        "net_usable": bool(signed_ok), "net_groups": groups, "perts": sig_any, "sig_any": bool(sig_any),
                        "sig_neural": bool(sig_strict), "sig_neural_ext": bool(sig_ext), "sig_fullkey_any": any(ctx.get(p) for p in perts_full),
                        "has_skeleton": bool(sk), "origin": e["origin"], "modality": e["modality"]}
        row_detail[e["id"]] = signed_ok

    def lvl(flag, unit):
        if unit == "records":
            return sum(1 for r in rec.values() if r[flag])
        return len({r["family"] for r in rec.values() if r[flag]})

    def both(flagA, flagB, unit):
        if unit == "records":
            return sum(1 for r in rec.values() if r[flagA] and r[flagB])
        fa = {r["family"] for r in rec.values() if r[flagA]}
        fb = {r["family"] for r in rec.values() if r[flagB]}
        return len(fa & fb)

    def overlap(flagA, flagB, unit):
        if unit == "records":
            A = {i for i, r in rec.items() if r[flagA]}
            B = {i for i, r in rec.items() if r[flagB]}
            U = set(rec)
        else:
            A = {r["family"] for r in rec.values() if r[flagA]}
            B = {r["family"] for r in rec.values() if r[flagB]}
            U = set(fam_ids)
        return {"both": len(A & B), "only_" + flagA: len(A - B), "only_" + flagB: len(B - A), "neither": len(U - A - B), "denominator": len(U)}

    funnel = {}
    for unit in ("records", "families"):
        f = {"L0_catalogued": n_rec if unit == "records" else len(fam_ids)}
        f["L1_with_any_target_row"] = lvl("any_target_row", unit)
        f["L2a_stated_action_any_row_before_artefact_rules"] = lvl("stated_action_raw", unit)
        f["L2_documented_action_row_passes_artefact_rules"] = lvl("stated_action_ok", unit)
        f["L3_Mnet_usable_signed_action_on_human_target_with_stable_id"] = lvl("net_usable", unit)
        f["Msig_any_context_trt_cp_signature"] = lvl("sig_any", unit)
        f["Msig_neural_lineage_context_strict"] = lvl("sig_neural", unit)
        f["Msig_neural_lineage_context_extended_with_FIBRNPC"] = lvl("sig_neural_ext", unit)
        f["overlap_Mnet_vs_Msig_neural_strict"] = overlap("net_usable", "sig_neural", unit)
        f["overlap_Mnet_vs_Msig_any_context"] = overlap("net_usable", "sig_any", unit)
        f["actually_evaluated"] = 0
        funnel[unit] = f

    # per-source M-net records (exclusive source-group regions among net-usable records)
    regions = collections.Counter()
    fam_regions = collections.defaultdict(set)
    for i, r in rec.items():
        if r["net_usable"]:
            regions["+".join(r["net_groups"])] += 1
            fam_regions[r["family"]].update(r["net_groups"])
    fam_region_counts = collections.Counter("+".join(sorted(v)) for v in fam_regions.values())
    per_group_records = {g: sum(1 for r in rec.values() if g in r["net_groups"]) for g in GROUPS}
    per_group_families = {g: len({r["family"] for r in rec.values() if g in r["net_groups"]}) for g in GROUPS}

    # modality of M-net / M-sig
    mod_net = collections.Counter(r["modality"] for r in rec.values() if r["net_usable"])
    mod_sig = collections.Counter(r["modality"] for r in rec.values() if r["sig_any"])
    origin_net = collections.Counter(r["origin"] for r in rec.values() if r["net_usable"])
    origin_sig = collections.Counter(r["origin"] for r in rec.values() if r["sig_any"])

    # LINCS side numbers
    sig_perts = {p for p, c in ctx.items() if c}
    neural_perts = {p for p in sig_perts if any(k[0] in neural_strict for k in ctx[p])}
    ext_perts = {p for p in sig_perts if any(k[0] in neural_ext for k in ctx[p])}
    perts_with_key = {p for p in sig_perts if pkey.get(p)}
    skel_all = {pkey[p].split("-")[0] for p in perts_with_key}
    cat_skel = {r for r in ((e.get("ids") or {}).get("skeleton_key") for e in entries) if r}
    neural_cell_sig = collections.Counter()
    neural_cell_perts = collections.defaultdict(set)
    all_cell_sig = collections.Counter()
    for p, c in ctx.items():
        for (cell, dose, tm), n in c.items():
            all_cell_sig[cell] += n
            if cell in neural_ext:
                neural_cell_sig[cell] += n
                neural_cell_perts[cell].add(p)
    lincs = {
        "series": {"GSE92742": "phase I (2017 Cell), signatures counted here from sig_info pert_type trt_cp",
                   "GSE70138": "phase II (2017 expansion), same"},
        "trt_cp_signatures_total": sum(sum(c.values()) for c in ctx.values()), "trt_cp_signatures_by_series": dict(nsig),
        "distinct_compound_perturbagens_with_trt_cp_signature": len(sig_perts),
        "of_which_with_inchikey": len(perts_with_key), "of_which_without_inchikey_cannot_be_matched": len(sig_perts) - len(perts_with_key),
        "distinct_skeletons_among_those": len(skel_all), "distinct_skeletons_also_in_catalogue": len(skel_all & cat_skel),
        "distinct_cell_ids_with_compound_signatures": len(all_cell_sig),
        "neural_strict_cell_ids": list(NEURAL_STRICT), "neural_extended_adds": list(NEURAL_EXTENDED_EXTRA),
        "neural_cell_signature_counts_trt_cp": dict(sorted(neural_cell_sig.items())),
        "neural_cell_compound_counts_trt_cp": {k: len(v) for k, v in sorted(neural_cell_perts.items())},
        "perturbagens_with_neural_strict_signature": len(neural_perts), "perturbagens_with_neural_extended_signature": len(ext_perts),
        "SHSY5Y_trt_cp_signatures": all_cell_sig.get("SHSY5Y", 0),
        "ASC_note": "ASC / ASC.C in cell_info are adipose-derived stem cells (primary_site adipose), NOT astrocytes; no glial compound context is counted",
        "files_checksummed_against_series_SHA512SUMS": gfiles,
    }
    # dose / time / replication stats for the strict-neural usable families
    fam_ctx = collections.defaultdict(lambda: collections.defaultdict(int))
    fam_perts = collections.defaultdict(set)
    for i, r in rec.items():
        for p in r["perts"]:
            fam_perts[r["family"]].add(p)
    for fid, ps in fam_perts.items():
        for p in ps:
            for (cell, dose, tm), n in ctx[p].items():
                if cell in neural_strict:
                    fam_ctx[fid][(cell, dose, tm)] += n
    nf = len(fam_ctx)
    ge2cells = sum(1 for v in fam_ctx.values() if len({k[0] for k in v}) >= 2)
    dr = 0
    for v in fam_ctx.values():
        per = collections.defaultdict(set)
        for (cell, dose, tm) in v:
            per[(cell, tm)].add(dose)
        if any(len(s) >= 2 for s in per.values()):
            dr += 1
    sigs_per_family = sorted(sum(v.values()) for v in fam_ctx.values())
    lincs["neural_strict_families_stats"] = {
        "families": nf, "with_signatures_in_2_or_more_neural_cell_ids": ge2cells,
        "with_2_or_more_doses_at_one_neural_cell_and_time": dr,
        "signatures_per_family_median": sigs_per_family[len(sigs_per_family) // 2] if sigs_per_family else 0,
        "signatures_per_family_max": sigs_per_family[-1] if sigs_per_family else 0}

    # ---- pilot subset
    links = json.loads((Path(a.catalog).parent / "card_links.json").read_text())
    card_of = collections.defaultdict(set)
    for cid, c in links["cards"].items():
        for l in c.get("links", []):
            if l["catalogue_id"] in by_id:
                card_of[fam[l["catalogue_id"]]].add(cid)
    fam_flags = collections.defaultdict(lambda: {"net": False, "sig_neural": False, "sig_any": False})
    fam_members = collections.defaultdict(list)
    for i, r in rec.items():
        ff = fam_flags[r["family"]]
        ff["net"] |= r["net_usable"]
        ff["sig_neural"] |= r["sig_neural"]
        ff["sig_any"] |= r["sig_any"]
        fam_members[r["family"]].append(i)
    pilot_both = sorted(f for f, v in fam_flags.items() if v["net"] and v["sig_neural"])
    pilot_card = sorted(card_of)
    pilot = sorted(set(pilot_both) | set(pilot_card))
    gt, gt_ok = gtopdb_index(cache)
    mx, mx_ok = mech_index(cache)
    mo, mo_ok = mol_index(cache)

    def clean(s):
        return str(s).replace("\t", " ").replace("\n", " ").strip()

    pilot_rows, action_rows, ctx_rows = [], [], []
    for fid in pilot:
        mem = sorted(fam_members[fid])
        lead = next((m for m in mem if m == fid.replace("FAM:", "")), mem[0])
        le = by_id[lead]
        nets = []
        for m in mem:
            for t, u in row_detail[m]:
                nets.append((m, t, u))
        # long action rows
        for m, t, u in sorted(nets, key=lambda x: (x[0], x[2]["group"], x[2]["symbol"], x[2]["raw"] or "")):
            sel = "UNKNOWN"
            assay = "UNKNOWN"
            conc = "UNKNOWN"
            aff = "UNKNOWN"
            if u["group"] == "ChEMBL":
                if mx_ok:
                    ms = mx.get((by_id[m]["ids"].get("chembl"), t.get("target_id")), [])
                    sc = sorted({x["selectivity_comment"] for x in ms if x.get("selectivity_comment")})
                    sel = "; ".join(sc) if sc else "UNKNOWN (no selectivity comment in curated mechanism)"
                    mc = sorted({x["mechanism_comment"] for x in ms if x.get("mechanism_comment")})
                    assay = "none carried by curated mechanism" + ("; mechanism comment: " + " | ".join(mc) if mc else "")
                else:
                    sel = "UNKNOWN (cache absent)"
                conc = "UNKNOWN (curated mechanism carries no concentration)"
                aff = "UNKNOWN (not carried)"
            else:
                gtype_rows = gt.get((str(t.get("iuphar_ligand_id") or ""), str(t.get("iuphar_target_id") or "")), []) if gt_ok else []
                if u["group"] == "GtoPdb" and (t.get("selectivity_stated") or []):
                    sel = "; ".join(t["selectivity_stated"])
                if gtype_rows:
                    ad = sorted({r["Assay Description"] for r in gtype_rows if r["Assay Description"]})
                    assay = " || ".join(ad[:3]) if ad else "UNKNOWN (GtoPdb row carries no assay description)"
                    cr = sorted({r["concentration Range"] for r in gtype_rows if r["concentration Range"]})
                    conc = " || ".join(cr[:3]) if cr else "UNKNOWN (GtoPdb row carries no concentration range)"
                    vals = []
                    for r in gtype_rows:
                        try:
                            vals.append(float(r["Original Affinity Median nm"]))
                        except ValueError:
                            pass
                    aff = (f"n={len(gtype_rows)} rows; original affinity median nM {min(vals):g}-{max(vals):g} ({sorted({r['Original Affinity Units'] for r in gtype_rows})}); source value, not interpreted"
                           if vals else f"n={len(gtype_rows)} rows; no numeric affinity")
                elif u["group"] == "GtoPdb":
                    assay = "UNKNOWN (no GtoPdb interaction row joined)" if gt_ok else "UNKNOWN (cache absent)"
                else:
                    assay = f"UNKNOWN (DGIdb claim source {u['claim_source']} carries no assay context)"
                    conc = "UNKNOWN"
            action_rows.append([fid, m, u["group"], u["claim_source"], u["symbol"], u["target_id"], u["scope"], u["raw"], u["sign"],
                                sel, assay, conc, aff, "; ".join(t.get("reference_ids") or []) if u["group"] == "ChEMBL" else (f"GtoPdb ligand {t.get('iuphar_ligand_id')} target {t.get('iuphar_target_id')}" if t.get("iuphar_ligand_id") else "UNKNOWN")])
        # LINCS contexts (neural strict only, long)
        perts = sorted({p for m in mem for p in rec[m]["perts"]})
        cagg = collections.Counter()
        for p in perts:
            for (cell, dose, tm), n in ctx[p].items():
                if cell in neural_ext:
                    cagg[(p, cell, dose, tm)] += n
        for (p, cell, dose, tm), n in sorted(cagg.items()):
            ctx_rows.append([fid, p, cell, "strict" if cell in neural_strict else "extended_FIBRNPC_lineage_UNKNOWN", dose, tm, n, "+".join(sorted(pseries[p]))])
        neural_cells = sorted({k[1] for k in cagg})
        doses = sorted({k[2] for k in cagg})
        times = sorted({k[3] for k in cagg})
        sigs_any = sum(sum(ctx[p].values()) for p in perts)
        # summaries
        summ = sorted({f"{u['symbol']}|{u['raw']}|{u['sign']}|{u['group']}" for _, _, u in nets})
        sel_known = sum(1 for r in action_rows if r[0] == fid and not r[9].startswith("UNKNOWN") and r[9] != "Not Determined")
        rts = []
        bb = []
        for m in mem:
            ch = by_id[m]["ids"].get("chembl")
            if ch and mo_ok and ch in mo:
                x = mo[ch]
                rts.append(f"{ch}:oral={x['oral']},parenteral={x['parenteral']},topical={x['topical']}")
                bb.append(f"{ch}:black_box={x['black_box_warning']},withdrawn={x['withdrawn_flag']}")
        stat = sorted({(s.get("max_phase"), s["source"]) for m in mem for s in by_id[m]["status_records"] if s["source"] == "ChEMBL" and s.get("max_phase") is not None})
        acc = sorted({c for m in mem for c in by_id[m]["access_categories"]})
        pilot_rows.append([
            fid, lead, clean(le["name"]), len(mem), "|".join(mem), "yes" if fid in pilot_both else "no", "|".join(sorted(card_of.get(fid, []))) or "none",
            le["modality"], le["status_class"], "|".join(acc),
            "yes" if fam_flags[fid]["net"] else "no", len(nets), clean("; ".join(summ[:6]) + (f"; ... (+{len(summ) - 6} more, see pilot_net_actions.tsv)" if len(summ) > 6 else "")) if summ else "none (no signed action on a stable target)",
            f"{sel_known} of {len([r for r in action_rows if r[0] == fid])} action rows carry a source selectivity statement" if nets else "UNKNOWN",
            "yes" if fam_flags[fid]["sig_neural"] else "no", len(perts), "+".join(neural_cells) or "none", " | ".join(doses) or "none", " | ".join(times) or "none",
            sum(n for n in cagg.values()), sigs_any,
            "; ".join(rts) if rts else "UNKNOWN (no ChEMBL molecule record)", "UNKNOWN (no brain, CSF or blood-brain-barrier statement in the catalogue or the cached ChEMBL fields; route flags above are routes, not exposure)",
            "; ".join(bb) if bb else "UNKNOWN", "NOT_ASSESSED", 0])
    # ---- write
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    hdr = ["family_id", "lead_record", "name", "n_records", "records", "usable_by_both_Mnet_and_Msig_neural", "card_ids", "modality", "status_class", "access_categories",
           "Mnet_usable", "n_signed_action_rows", "action_summary_target|action|sign|source", "selectivity", "Msig_neural_usable", "n_lincs_perturbagens",
           "lincs_neural_cell_ids", "lincs_neural_concentrations", "lincs_neural_times", "n_neural_signatures", "n_signatures_any_context",
           "exposure_route_flags_chembl", "exposure_brain_penetration", "safety_flags_in_source", "safety_assessment", "actually_evaluated"]
    with open(out / "pilot_subset.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(hdr)
        w.writerows(pilot_rows)
    with open(out / "pilot_net_actions.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family_id", "record", "source_group", "claim_source", "target_symbol", "target_stable_id", "target_scope", "action_raw", "sign",
                    "selectivity", "assay_context", "concentration", "affinity_source_value", "references"])
        w.writerows([[clean(x) for x in r] for r in action_rows])
    with open(out / "pilot_lincs_contexts.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family_id", "pert_id", "cell_id", "context_tier", "concentration", "time", "n_signatures", "series"])
        w.writerows(ctx_rows)
    with gzip.GzipFile(out / "record_usability.tsv.gz", "wb", mtime=0) as gz:
        buf = ["\t".join(["record_id", "family_id", "origin", "modality", "any_target_row", "stated_action", "Mnet_usable", "Mnet_source_groups", "Msig_any_context", "Msig_neural_strict", "Msig_neural_extended"])]
        for i in sorted(rec):
            r = rec[i]
            buf.append("\t".join([i, r["family"], r["origin"], r["modality"], *("1" if r[k] else "0" for k in ("any_target_row", "stated_action_ok", "net_usable")),
                                  "+".join(r["net_groups"]) or "-", *("1" if r[k] else "0" for k in ("sig_any", "sig_neural", "sig_neural_ext"))]))
        gz.write(("\n".join(buf) + "\n").encode())

    # access categories with source / country / date
    acc_counts = collections.Counter()
    for e in entries:
        for c in e["access"]:
            acc_counts[(c["category"], c["strength"], c["scope"].split(":")[0])] += 1
    stats = json.loads((Path(a.catalog).parent / "catalog_stats.json").read_text())
    eu = {"source": "EU Open Data Portal datasets of DG SANTE: EU register of nutrition and health claims, EU Novel Food status catalogue",
          "country_or_jurisdiction": "European Union level (not Italy or any national list)", "dataset_last_modified": "2024-08-13",
          "downloaded_utc": "2026-10-28", "scope": "name-match probes only (catalog/eu_context_probe.tsv, one row per probe string), not a catalogue-wide field: no catalogue record carries an EU access category",
          "probe_rows": sum(1 for _ in open(Path(a.catalog).parent / "eu_context_probe.tsv", encoding="utf-8")) - 1,
          "reference": "catalog/README.md, section 'European context probe, IT5 P10'"}
    counts = {
        "schema_version": 1, "task": "IT7 P2 / roadmap R2", "catalogue": {"records": n_rec, "generated_utc": stats["generated_utc"], "families_all_record_definition": len(fam_ids)},
        "units": {
            "records": "source-level substance records (a salt, a stereoisomer and a source-only row each count once)",
            "families": "ChEMBL parent/child or identical InChIKey first block, plus the 485 source-only records joined by GtoPdb ligand reconciliation; every other source-only record is its own family (identity unresolved, never merged on name)",
            "compound": "in this census a compound is a family; the record counts are given beside"},
        "definitions": {
            "L1": "record has at least one target row (ChEMBL curated mechanism or DGIdb interaction)",
            "L2": "at least one row with a STATED action (ChEMBL action_type present; DGIdb interaction_type present and not other/unknown and not a source conflict) that passes the catalogue artefact rules of repurposing_search.artefact_reason (unconfirmed identity, source artefacts, alias risk) and a non-placeholder name",
            "L3_Mnet": "L2 row whose action maps to a SIGN (down: inhibitor, antagonist, blocker, negative modulators, inverse agonist, degrader...; up: agonist, activator, positive modulators, opener, potentiator...) on a human target with a stable identifier (ChEMBL: Homo sapiens + target id + UniProt; DGIdb: HGNC concept id). Sign is the source's effect on the TARGET's activity; modulator/binding agent/antibody/unstated are not signed",
            "Msig_any": "the record's InChIKey first block (connectivity layer, the catalogue's own family key) equals the first block of a LINCS compound perturbagen that has at least one trt_cp signature in GSE92742 or GSE70138",
            "Msig_neural_strict": "as Msig_any, with at least one signature in a cell id of: " + ", ".join(NEURAL_STRICT) + " (iPSC-derived neural progenitors or neurons; cell_info primary_site central nervous system or modification text 'differentiated ... neurons')",
            "Msig_neural_extended": "strict plus FIBRNPC (cell_info gives no modification text and primary_site skin: lineage UNKNOWN, kept apart)",
            "actually_evaluated": "0: no compound has been scored or ranked by either method; usable is an input requirement, not a result"},
        "funnel": funnel,
        "Mnet_by_source_group": {
            "groups": {"ChEMBL": "ChEMBL curated mechanism action_type", "GtoPdb": "DGIdb rows whose claim source is GuideToPharmacology (target verified or corrected through GtoPdb ids), i.e. GtoPdb action as carried by the catalogue",
                       "DGIdb_other": "DGIdb interaction type from every other claim source (ChEMBL claims v33, DTC, TTD, ...); identity as served"},
            "records_with_at_least_one_usable_row_by_group": per_group_records, "families_with_at_least_one_usable_row_by_group": per_group_families,
            "records_exclusive_region_counts": dict(sorted(regions.items())), "families_exclusive_region_counts": dict(sorted(fam_region_counts.items())),
            "usable_rows_by_claim_source": dict(sorted(claim_src_usable.items())),
            "independence_note": "the groups are NOT independent votes: DGIdb carries ChEMBL (v33) and GtoPdb claims, and GtoPdb curates some of the same drugs as ChEMBL; the overlap shows redundancy, not replication"},
        "row_counts": dict(raw_counts),
        "Mnet_modality_records": dict(mod_net), "Msig_any_modality_records": dict(mod_sig), "Mnet_origin_records": dict(origin_net), "Msig_any_origin_records": dict(origin_sig),
        "lincs": lincs,
        "match_rule_sensitivity": {"records_matched_by_skeleton_any_context": lvl("sig_any", "records"), "records_matched_by_full_InChIKey_any_context": sum(1 for r in rec.values() if r["sig_fullkey_any"]),
                                   "records_with_no_skeleton_key_cannot_be_matched_to_LINCS": sum(1 for r in rec.values() if not r["has_skeleton"]),
                                   "note": "name matching is not used; source-only records without a structure are in the denominator and cannot be counted usable by M-sig (UNKNOWN, not negative)"},
        "pilot": {"definition": "families usable by BOTH M-net and M-sig (neural strict) union the families linked to a curated card (card_links.json)",
                  "both_methods_families": len(pilot_both), "card_linked_families": len(pilot_card), "union_families": len(pilot),
                  "card_linked_not_in_both": len(set(pilot_card) - set(pilot_both)), "card_linked_and_both": len(set(pilot_card) & set(pilot_both)),
                  "card_linked_families_Mnet_usable": sum(1 for f in pilot_card if fam_flags[f]["net"]), "card_linked_families_Msig_neural": sum(1 for f in pilot_card if fam_flags[f]["sig_neural"]),
                  "pilot_net_action_rows": len(action_rows), "pilot_lincs_context_rows": len(ctx_rows),
                  "cache_available": {"gtopdb_interactions": gt_ok, "chembl_mechanisms": mx_ok, "chembl_molecules": mo_ok}},
        "access_category_sources": {" | ".join(k): v for k, v in sorted(acc_counts.items())},
        "access_overlapping_category_counts": stats["access_category_overlapping_counts"], "eu_registers": eu,
    }
    (out / "counts.json").write_text(json.dumps(counts, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"funnel": funnel, "pilot": counts["pilot"]}, indent=1, sort_keys=True))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run")
    r.add_argument("--geo92", required=True)
    r.add_argument("--geo70", required=True)
    r.add_argument("--out", default=str(HERE))
    r.add_argument("--catalog", default=str(REPO / "disease-models/wwox/research/drug_repurposing/catalog/catalog.jsonl.gz"))
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__)
        return 0
    return run(a)


if __name__ == "__main__":
    sys.exit(main())
