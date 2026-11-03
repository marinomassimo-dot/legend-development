#!/usr/bin/env python3
"""IT21 V1: two general links the hand-over of IT21 P2 did not make, both from data the repository already holds.

1. IDENTITY BRIDGE. A DGIdb-only record whose Guide-to-Pharmacology claims carry the ligand id as the CLAIM NAME (drug_claim_name IUPHAR.LIGAND:<id>)
   but not as a concept id was never reconciled with its ChEMBL record, because `catalog_build.reconcile_gtopdb_ligands` reads the concept id only.
   `bridge_claim_name_ligands` applies the SAME decision rule (ChEMBL id is a catalogue record, equal standard InChIKey, not labelled or radioactive,
   no contradicting DrugBank or DGIdb ChEMBL concept id, one record joins one chemical family) to the ligand id found in the claim name. A name
   coincidence is never a basis. Output: twin family -> ChEMBL family, with the evidence; the stored catalogue is not rewritten.
2. ATTRIBUTION SCREEN. The engine scores a compound through its chain from a LISTED target; the listed target can be the weakest target of the compound
   (P4a limit 3, nanatinostat HDAC5 200 nM v HDAC1 3 nM). `attribution` reads the measured affinities of the family's ligand(s) in the local Guide to
   Pharmacology release and states, for the main target of a proposal, how much weaker it is than the compound's best measured human target.
   Reading: at the concentration that half-occupies the best target, a target FOLD times weaker is occupied 1/(1+FOLD). FOLD >= 10 (< 9 percent) is WEAK;
   the threshold is a stated pharmacological convention and the sensitivity at 3, 10, 30, 100 is reported, not hidden.
   States: WEAK_ATTRIBUTION | ATTRIBUTABLE | UNMEASURED_AT_MAIN_TARGET (ligand measured elsewhere, annotation only) | NOT_ASSESSABLE (no ligand or no measurement).
   Only WEAK_ATTRIBUTION blocks a hand-over; unknown is not negative. Affinity is an enzyme or binding measurement, not cellular occupancy or exposure.

Standard library only. The GtoPdb and DGIdb files are the shared catalogue cache (LEGEND_CATALOG_CACHE), third-party and not in git.
"""
import collections, csv, gzip, importlib.util, json, math, os, re, statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
WEAK_FOLD = 10.0
SENSITIVITY_FOLDS = (3.0, 10.0, 30.0, 100.0)
_CLAIM_ID = re.compile(r"^IUPHAR\.LIGAND:(\d+)$", re.I)


def cache_dir():
    return Path(os.environ.get("LEGEND_CATALOG_CACHE") or (DR / "catalog" / "cache"))


def _cb():
    spec = importlib.util.spec_from_file_location("catalog_build_v1", DR / "catalog" / "catalog_build.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _rd(path):
    with open(path, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    return [dict(zip(rows[1], r)) for r in rows[2:]]


def load_gtopdb_affinities(cache=None):
    """({ligand id: ligands.csv row}, {(ligand id, HGNC symbol): [nM, ...]}, {(ligand id, symbol): {unit types}}), human targets only."""
    cache = cache or cache_dir()
    lig = {r["Ligand ID"]: r for r in _rd(cache / "gtopdb" / "ligands.csv") if r.get("Ligand ID")}
    aff, kinds = collections.defaultdict(list), collections.defaultdict(set)
    for r in _rd(cache / "gtopdb" / "interactions.csv"):
        if r.get("Target Species") != "Human" or not r.get("Ligand ID"):
            continue
        sym = (r.get("Target Gene Symbol") or "").upper()
        if not sym or "|" in sym:
            continue
        nm = None
        if r.get("Original Affinity Median nm"):
            try:
                nm = float(r["Original Affinity Median nm"])
            except ValueError:
                nm = None
        if nm is None and r.get("Affinity Median"):
            try:
                nm = 10 ** (9 - float(r["Affinity Median"]))
            except ValueError:
                nm = None
        if nm is None or nm <= 0:
            continue
        aff[(r["Ligand ID"], sym)].append(nm)
        kinds[(r["Ligand ID"], sym)].add(r.get("Affinity Units") or "?")
    return lig, {k: statistics.median(v) for k, v in aff.items()}, kinds


def claim_name_ligands(cache=None):
    """{DGIdb drug_name (upper): {ligand ids}} from drug_claim_name of Guide-to-Pharmacology claims."""
    cache = cache or cache_dir()
    out = collections.defaultdict(set)
    with open(cache / "dgidb" / "interactions.tsv", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            m = _CLAIM_ID.match(r["drug_claim_name"] or "")
            if m and r["interaction_source_db_name"] == "GuideToPharmacology":
                out[r["drug_name"].upper()].add(m.group(1))
    return out


def bridge_claim_name_ligands(entries, cache=None, cb=None):
    """For DGIdb-only entries with a claim-name ligand id and NO concept-id ligand id: the reconciliation decision the catalogue rule would reach.
    Returns {entry id: [record, ...]}; record = {ligand_id, chembl_ref, decision, reason, structure_check, evidence}. Pure given its inputs."""
    cb = cb or _cb()
    cache = cache or cache_dir()
    lig, _, _ = load_gtopdb_affinities(cache)
    claims = claim_name_ligands(cache)
    E = {e["id"]: e for e in entries}
    out = {}
    for e in entries:
        if e.get("origin") != "dgidb_only" or (e["ids"].get("iuphar_ligand") or []):
            continue
        ids = claims.get((e["ids"].get("dgidb_drug_name") or "").upper(), set())
        recs = []
        for lid in sorted(ids):
            l = lig.get(lid)
            rec = {"ligand_id": lid, "chembl_ref": None, "decision": None, "reason": None, "structure_check": None, "evidence": {"via": "drug_claim_name IUPHAR.LIGAND:" + lid}}
            if l is None:
                rec.update(decision="unresolved", reason="ligand_id_absent_from_gtopdb_release")
            elif not l["ChEMBL ID"]:
                continue
            else:
                rec["chembl_ref"] = r_id = l["ChEMBL ID"]
                m = E.get("CAT:" + r_id)
                if m is None or not m["origin"].startswith("chembl"):
                    rec.update(decision="out_of_selection", reason="chembl_ref_not_a_catalogue_record")
                else:
                    state, code = cb.compare_structures(l["InChIKey"], m["ids"].get("inchikey"))
                    rec["structure_check"] = code
                    rec["evidence"].update(gtopdb_inchikey=l["InChIKey"], chembl_inchikey=m["ids"].get("inchikey"), chembl_name=m["name"])
                    dg_chembl = e["ids"].get("chembl_from_dgidb_concept_not_enumerated") or []
                    if state == "conflict":
                        rec.update(decision="rejected_conflict", reason=code)
                    elif state == "unavailable":
                        rec.update(decision="unresolved", reason=code)
                    elif state == "related":
                        rec.update(decision="related_not_merged", reason=code)
                    elif l["Labelled"] == "yes" or l["Radioactive"] == "yes":
                        rec.update(decision="related_not_merged", reason="labelled_or_radioactive_form_of_the_ligand")
                    elif e["ids"].get("drugbank") and m["ids"].get("drugbank") and not set(e["ids"]["drugbank"]) & set(m["ids"]["drugbank"]):
                        rec.update(decision="unresolved", reason="drugbank_ids_disjoint")
                    elif dg_chembl and r_id not in dg_chembl:
                        rec.update(decision="unresolved", reason="dgidb_chembl_concept_differs_from_gtopdb_reference")
                    else:
                        rec.update(decision="merged", reason=code)
            recs.append(rec)
        if len({r["chembl_ref"] for r in recs if r["decision"] == "merged"}) > 1:
            for r in recs:
                if r["decision"] == "merged":
                    r.update(decision="unresolved", reason="one_dgidb_record_would_join_several_chembl_ids")
        if recs:
            out[e["id"]] = recs
    return out


def family_bridge(bridges, fam):
    """{twin family id: ChEMBL family id} for entries whose bridge is 'merged' (one target family only; otherwise nothing)."""
    res = collections.defaultdict(set)
    for eid, recs in bridges.items():
        for r in recs:
            if r["decision"] == "merged":
                res[fam[eid]].add(fam["CAT:" + r["chembl_ref"]])
    return {k: next(iter(v)) for k, v in res.items() if len(v) == 1 and next(iter(v)) != k}


def family_ligands(entries, fam, bridges, lig):
    """{family id: set of GtoPdb ligand ids}: by the ChEMBL id of a member (ligands.csv 'ChEMBL ID'), and by a merged claim-name bridge."""
    by_chembl = collections.defaultdict(set)
    for lid, r in lig.items():
        if r["ChEMBL ID"]:
            by_chembl[r["ChEMBL ID"]].add(lid)
    out = collections.defaultdict(set)
    for e in entries:
        c = (e.get("ids") or {}).get("chembl")
        if c:
            out[fam[e["id"]]] |= by_chembl.get(c, set())
        for r in bridges.get(e["id"], []):
            if r["decision"] == "merged":
                out[fam[e["id"]]].add(r["ligand_id"])
    return out


def attribution(ligands, main_gene, aff, kinds=None, weak_fold=WEAK_FOLD):
    """State of the attribution of a family (its ligand ids) to `main_gene`. Pure."""
    main = (main_gene or "").upper()
    best_by_gene = {}
    for (lid, sym), nm in aff.items():
        if lid in ligands:
            if sym not in best_by_gene or nm < best_by_gene[sym][0]:
                best_by_gene[sym] = (nm, lid)
    if not ligands or not best_by_gene:
        return dict(state="NOT_ASSESSABLE", main_nm="", best_target="", best_nm="", fold="", occupancy="", n_targets_measured=0)
    bg, (bnm, _) = min(best_by_gene.items(), key=lambda kv: kv[1][0])
    if main not in best_by_gene:
        return dict(state="UNMEASURED_AT_MAIN_TARGET", main_nm="", best_target=bg, best_nm=round(bnm, 3), fold="", occupancy="", n_targets_measured=len(best_by_gene))
    mnm = best_by_gene[main][0]
    fold = mnm / bnm
    state = "WEAK_ATTRIBUTION" if fold >= weak_fold else "ATTRIBUTABLE"
    return dict(state=state, main_nm=round(mnm, 3), best_target=bg, best_nm=round(bnm, 3), fold=round(fold, 1), occupancy=round(1 / (1 + fold), 4),
                n_targets_measured=len(best_by_gene))


def sensitivity(folds):
    """{threshold: number of assessable rows at or above it}; folds is a list of numeric fold values."""
    return {str(t): sum(1 for f in folds if f >= t) for t in SENSITIVITY_FOLDS}
