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
   V1-fix (independent review): a relative fold alone is not weakness. WEAK needs fold >= 10 AND a main-target potency that is not itself high
   (main target above POTENT_MAIN_NM = 100 nM). Fold >= 10 with a main target at or below 100 nM is BORDERLINE_POTENT_MAIN_TARGET: annotated, not blocked.
   A family measured on one target only has no comparison: SINGLE_MEASURED_TARGET (not 'attributable by comparison'). The median of a (ligand, gene) pool
   can mix measure types (Ki, IC50, EC50 ...): the types pooled are reported and a pool of more than one type is marked mixed_measure (never blocks alone).
   States: WEAK_ATTRIBUTION | BORDERLINE_POTENT_MAIN_TARGET | ATTRIBUTABLE | SINGLE_MEASURED_TARGET | UNMEASURED_AT_MAIN_TARGET (ligand measured elsewhere,
   annotation only, ranked after the others in the cap) | NOT_ASSESSABLE (no ligand or no measurement).
   Only WEAK_ATTRIBUTION blocks a hand-over; unknown is not negative. Affinity is an enzyme or binding measurement, not cellular occupancy or exposure.
   Identity bridge V1-fix: structure equality is necessary but not sufficient; the twin's NAME must match the ligand's or its ChEMBL record's, modulo salt and
   counter-ion words; an extra non-salt word (ester or prodrug) is related_not_merged; no name match is unresolved.

IT22 P2 (supersedes the pooled-median reading above): measures are kept per TYPE (IC50, EC50, Ki, Kd); a ratio is formed only between the same type at the main target and at
   another target, with compatible relation (exact, or a lower bound on the main side) and, when both are recorded, the same assay class (cell / cell-free). No same-type pair ->
   NOT_COMPARABLE_MEASURES (values kept, no ratio, no exclusion). A measured main target of 100-1000 nM is SECONDARY_ACTIVITY_MEASURED (kept; the experiment needs an on-target control);
   only an exact value or lower bound above 1000 nM with a comparable pair is WEAK_ATTRIBUTION. The nM conventions are stated, not laws; ratios are never converted into occupancy.

Standard library only. The GtoPdb and DGIdb files are the shared catalogue cache (LEGEND_CATALOG_CACHE), third-party and not in git.
"""
import collections, csv, gzip, importlib.util, json, math, os, re, statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
WEAK_FOLD = 10.0
SENSITIVITY_FOLDS = (3.0, 10.0, 30.0, 100.0)
SECONDARY_MAIN_NM = 1000.0     # IT22 P2: up to here a main target with a measured value is a SECONDARY ACTIVITY (kept), above it WEAK (a stated convention, with a sensitivity)
POTENT_MAIN_NM = 100.0          # main-target affinity at or below this is potent in absolute terms: a large fold there is annotated, not blocked
_CLAIM_ID = re.compile(r"^IUPHAR\.LIGAND:(\d+)$", re.I)
# counter-ion, hydration and formulation words: a name differing from the parent by these only names the same substance (ester and prodrug groups are NOT here)
SALT_WORDS = frozenset("""hydrochloride dihydrochloride hydrobromide hydroiodide sulfate sulphate bisulfate phosphate diphosphate mesylate dimesylate besylate tosylate
fumarate maleate tartrate bitartrate citrate succinate sodium disodium potassium calcium magnesium lithium zinc chloride bromide iodide nitrate hydrate monohydrate
dihydrate trihydrate hemihydrate anhydrous micronized propanediol triethiodide acid free base salt oxalate lactate gluconate malate napsylate edisylate camsylate pamoate""".split())
_TAG = re.compile(r"<[^>]+>|&[a-z]+;")


def _name_tokens(name):
    return [t for t in re.split(r"[^a-z0-9]+", _TAG.sub(" ", (name or "").lower())) if t]


def name_relation(twin_names, *parent_names):
    """How a DGIdb-only record's name relates to the ligand / ChEMBL record names: 'match' (equal after dropping salt words), 'derivative' (one name is the other
    plus non-salt words: ester, prodrug, other form) or 'none'. Pure; no compound name appears in it."""
    core = lambda n: tuple(t for t in _name_tokens(n) if t not in SALT_WORDS)
    twins = [core(n) for n in twin_names if core(n)]
    parents = [core(n) for n in parent_names if core(n)]
    if any(a == b for a in twins for b in parents):
        return "match"
    if any(a[:len(b)] == b or b[:len(a)] == a for a in twins for b in parents):
        return "derivative"
    return "none"


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


_CELL = re.compile(r"\b(cell|cells|cellular|whole[- ]cell|culture|cultured|hek|cho|tissue|in vivo|reporter|proliferation|viability)\b", re.I)
_BIOCHEM = re.compile(r"\b(enzyme|enzymatic|recombinant|purified|kinase activity|biochemical|binding assay|radioligand|spr|surface plasmon|fret|cell[- ]free|membrane)\b", re.I)


def assay_class(text):
    """'cell', 'biochemical' or 'unknown' from the Guide-to-Pharmacology assay description. Unknown stays unknown (it is never guessed)."""
    c, b = bool(_CELL.search(text or "")), bool(_BIOCHEM.search(text or ""))
    return "cell" if c and not b else "biochemical" if b and not c else "unknown"


def load_gtopdb_affinities(cache=None):
    """(ligands {ligand id: ligands.csv row}, typed {(ligand id, HGNC symbol): {measure type: {nm, rel, assay, n}}}, kinds {(ligand id, symbol): {measure types}}), human targets only.
    IT22 P2: the measures are kept SEPARATE by type (IC50, EC50, Ki, Kd, ...; '?' when the release records none); within a type the median of exact ('=') values is used,
    and a censored value ('<', '>', '~') is kept only when no exact value exists, with its relation. Nothing is converted between types."""
    cache = cache or cache_dir()
    lig = {r["Ligand ID"]: r for r in _rd(cache / "gtopdb" / "ligands.csv") if r.get("Ligand ID")}
    raw = collections.defaultdict(list)
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
        typ = (r.get("Original Affinity Units") or "").strip()
        if typ in ("-", ""):                      # the original type is not recorded: the release's own affinity column (pKi, pIC50, pEC50, pKd ...) still names it
            au = (r.get("Affinity Units") or "").strip()
            typ = au[1:] if au.startswith("p") and au[1:] in ("Ki", "IC50", "EC50", "Kd", "KB") else (au if au not in ("", "-") else "?")
        rel = (r.get("Original Affinity Relation") or "=").strip() or "="
        raw[(r["Ligand ID"], sym, typ)].append((nm, rel, assay_class(r.get("Assay Description"))))
    typed, kinds = collections.defaultdict(dict), collections.defaultdict(set)
    for (lid, sym, typ), v in raw.items():
        exact = [x for x in v if x[1] == "="]
        use = exact or v
        classes = {x[2] for x in use if x[2] != "unknown"}
        typed[(lid, sym)][typ] = dict(nm=statistics.median(x[0] for x in use), rel="=" if exact else use[0][1],
                                      assay=(next(iter(classes)) if len(classes) == 1 else "mixed" if classes else "unknown"), n=len(use))
        kinds[(lid, sym)].add(typ)
    return lig, dict(typed), kinds


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
                    elif name_relation([e["name"], e["ids"].get("dgidb_drug_name")], l["Name"], m["name"]) == "derivative":
                        rec.update(decision="related_not_merged", reason="twin_name_is_a_derivative_of_the_ligand_name (ester, prodrug or other form)")
                    elif name_relation([e["name"], e["ids"].get("dgidb_drug_name")], l["Name"], m["name"]) == "none":
                        rec.update(decision="unresolved", reason="twin_name_matches_neither_the_ligand_nor_its_chembl_record")
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
        if e.get("origin") == "dgidb_only":       # IT24 P10 (sulfopin): the record's OWN concept-id ligand; not labelled or radioactive; several different ligands would be ambiguous and are left out
            own = {str(x) for x in ((e.get("ids") or {}).get("iuphar_ligand") or []) if str(x) in lig and lig[str(x)].get("Labelled") != "yes" and lig[str(x)].get("Radioactive") != "yes"}
            if len(own) == 1:
                out[fam[e["id"]]] |= own
    return out


def _as_typed(v):
    """A bare number (legacy callers, tests) is one measure of unknown type; a dict is already {type: {nm, rel, assay}}."""
    return v if isinstance(v, dict) else {"?": dict(nm=float(v), rel="=", assay="unknown", n=1)}


def _pair_state(m, b):
    """Interpretability of one same-type pair (main entry m, other-target entry b): 'ok', 'lower_bound' (the ratio can only be LARGER than the one computed: the main value is exact or '>' and
    the other value is exact or '<') or a reason string. Cell-based against cell-free values are not compared; an unknown assay context stays 'ok' with the unknown carried by the caller."""
    if m["assay"] in ("cell", "biochemical") and b["assay"] in ("cell", "biochemical") and m["assay"] != b["assay"]:
        return "assay_context_differs"
    if m["rel"] == "=" and b["rel"] == "=":
        return "ok"
    if m["rel"] in ("=", ">") and b["rel"] in ("=", "<"):
        return "lower_bound"
    return "censored_value_not_comparable"


def attribution(ligands, main_gene, aff, kinds=None, weak_fold=WEAK_FOLD, potent_nm=POTENT_MAIN_NM, secondary_nm=SECONDARY_MAIN_NM):
    """State of the attribution of a family (its ligand ids) to `main_gene`. Pure.

    IT22 P2. `aff` maps (ligand id, symbol) to {measure type: {nm, rel, assay}} (a bare number is one measure of unknown type). Types are never pooled or converted: a ratio is formed
    only between the SAME type at the main target and at another target (IC50 with IC50, Kd with Kd ...), with compatible relation and assay context. Where no same-type pair exists
    the state is NOT_COMPARABLE_MEASURES: the values are kept (values_kept), the limit is stated, and no quantitative exclusion follows. The ratio is a statement about the two
    measurements, never converted into occupancy of the target. Tiers for a comparable pair: fold below WEAK_FOLD ATTRIBUTABLE; fold at or above it with the main target at or below
    potent_nm BORDERLINE_POTENT_MAIN_TARGET; above potent_nm and up to secondary_nm SECONDARY_ACTIVITY_MEASURED (a measured secondary action: kept, the discriminating experiment must carry
    an on-target control because the more potent target co-acts); above secondary_nm (exact value, or a lower bound) WEAK_ATTRIBUTION, the only state that blocks a hand-over. The two nM
    conventions are stated, reported with a sensitivity, and are not a statement that the compound is inactive or that the secondary action is irrelevant."""
    main = (main_gene or "").upper()
    by_gene = collections.defaultdict(dict)                 # gene -> type -> (best entry over the family's ligands)
    for (lid, sym), v in aff.items():
        if lid not in ligands:
            continue
        for t, e in _as_typed(v).items():
            cur = by_gene[sym].get(t)
            if cur is None or e["nm"] < cur["nm"]:
                by_gene[sym][t] = dict(e, ligand=lid)
    empty = dict(main_nm="", best_target="", best_nm="", fold="", occupancy="", n_targets_measured=0, main_measure="", best_measure="", mixed_measure="", comparison_basis="", values_kept="", context_note="")
    if not ligands or not by_gene:
        return dict(empty, state="NOT_ASSESSABLE")
    flat = lambda g: "; ".join(f"{t} {e['nm']:g} nM{'' if e['rel'] == '=' else ' (' + e['rel'] + ')'}" for t, e in sorted(by_gene[g].items()))
    gbest = min(((g, t, e) for g, d in by_gene.items() for t, e in d.items()), key=lambda x: x[2]["nm"])
    if main not in by_gene:
        return dict(empty, state="UNMEASURED_AT_MAIN_TARGET", best_target=gbest[0], best_nm=round(gbest[2]["nm"], 3), n_targets_measured=len(by_gene), best_measure=gbest[1],
                    values_kept="; ".join(f"{g}: {flat(g)}" for g in sorted(by_gene)))
    mt = by_gene[main]
    mmin = min(mt.items(), key=lambda kv: kv[1]["nm"])
    base = dict(empty, n_targets_measured=len(by_gene), main_measure="|".join(sorted(mt)), values_kept="; ".join(f"{g}: {flat(g)}" for g in sorted(by_gene)))
    if len(by_gene) == 1:
        return dict(base, state="SINGLE_MEASURED_TARGET", main_nm=round(mmin[1]["nm"], 3), best_target=main, best_nm=round(mmin[1]["nm"], 3), fold=1.0, best_measure=mmin[0])
    folds, skipped = [], []
    for t, m in mt.items():
        for g, d in by_gene.items():
            if g == main or t not in d:
                continue
            ps = _pair_state(m, d[t])
            if ps == "lower_bound" and m["nm"] / d[t]["nm"] < weak_fold:
                skipped.append(f"{t}: {main} vs {g} (a censored value leaves the ratio open upward: cannot show comparable potency)")
            elif ps == "lower_bound" and m["rel"] == ">" and m["nm"] <= secondary_nm:
                skipped.append(f"{t}: {main} vs {g} (main value only bounded from below at {m['nm']:g} nM)")
            elif ps in ("ok", "lower_bound"):
                folds.append((m["nm"] / d[t]["nm"], t, g, m, d[t], ps))
            else:
                skipped.append(f"{t}: {main} vs {g} ({ps})")
    if not folds:
        why = "no other target has a value of the same type as the main target's (main: %s; others: %s)" % ("|".join(sorted(mt)), "|".join(sorted({t for g, d in by_gene.items() if g != main for t in d}))) if not skipped else "; ".join(skipped[:3])
        absn = f"; the main target's own measured value is {mmin[1]['nm']:g} nM ({mmin[0]}), above {secondary_nm:g} nM: low potency at the listed target on its own terms (no ratio, no block)" if mmin[1]["rel"] == "=" and mmin[1]["nm"] > secondary_nm else ""
        return dict(base, state="NOT_COMPARABLE_MEASURES", main_nm=round(mmin[1]["nm"], 3), best_target=gbest[0], best_nm=round(gbest[2]["nm"], 3), best_measure=gbest[1],
                    comparison_basis="none: " + why, context_note="values kept, ratio not formed; unknown is not negative" + absn)
    # one comparison per type: the most potent other target of that type; the verdict follows the type that is MOST favourable to the main target
    per_type = {}
    for f, t, g, m, b, ps in folds:
        if t not in per_type or b["nm"] < per_type[t][4]["nm"]:
            per_type[t] = (f, t, g, m, b, ps)
    f, t, g, m, b, ps = max(per_type.values(), key=lambda x: x[0])           # the verdict follows the type that shows the LARGEST deficit: a favourable type never hides a same-type weakness (IT22 P8-fix)
    note = []
    if m["assay"] == "unknown" or b["assay"] == "unknown":
        note.append("assay context (cell or cell-free) not recorded for at least one side")
    if len(per_type) > 1:
        note.append("types compared separately: " + ", ".join(f"{k} {v[0]:.1f}x" for k, v in sorted(per_type.items())))
    if skipped:
        note.append("not compared: " + "; ".join(skipped[:3]))
    cop = sum(1 for g, d in by_gene.items() if g != main and t in d and d[t]["rel"] == "=" and d[t]["nm"] <= m["nm"] * weak_fold)       # co-potent other targets, same type
    if f < weak_fold:
        state = "ATTRIBUTABLE"
    elif m["nm"] <= potent_nm and m["rel"] == "=":
        state = "BORDERLINE_POTENT_MAIN_TARGET"
    elif m["nm"] <= secondary_nm and m["rel"] == "=":
        state = "SECONDARY_ACTIVITY_MEASURED"
    else:
        state = "WEAK_ATTRIBUTION"
    return dict(base, state=state, main_nm=round(m["nm"], 3), best_target=g, best_nm=round(b["nm"], 3), fold=round(f, 1), occupancy="", best_measure=t, main_measure=t,
                comparison_basis=f"{t} at {main} vs {t} at {g}" + (" (main value is a lower bound)" if ps == "lower_bound" else ""), context_note="; ".join(note), n_copotent=cop)


def sensitivity(folds):
    """{threshold: number of assessable rows at or above it}; folds is a list of numeric fold values."""
    return {str(t): sum(1 for f in folds if f >= t) for t in SENSITIVITY_FOLDS}
