#!/usr/bin/env python3
"""Same-document potency comparison from relations.tsv (chembl_activity + gtopdb rows), with a stated grade for every comparison.

IT14 wrote a ratio max/min for every document that held two or more targets. IT15 (P2) keeps the same input and the same output file
but no longer lets that ratio stand for selectivity unless the comparison earns it:

  * every value of a target is kept (n, min, median, max); the ratio is taken between the highest and the lowest target median, never from the single lowest value, and the spread
    inside a target is reported next to it;
  * a censored value ('<', '>') or a row without a value is listed apart (censored, n_no_value) and is never turned into a number;
  * a target is classified by its composition: single gene; defined complex (two genes, for example GRIN1|GRIN2B or KCNQ2|KCNQ3);
    generic complex (three genes or more: the measurement belongs to the complex and cannot be attributed to any one subunit);
    no gene symbol (not attributable);
  * rows in one document that span different gene families (a channel and metabolic enzymes, for example) are an activity PANEL, not a
    selectivity statement;
  * grade of the group: INTERPRETABLE (two or more attributable targets of one family, '=' on all, assay formats known and compatible,
    no validity comment, no discordance above 10x inside a target), LIMITED (the ratio is shown with the reason that limits it: assay
    context not retained, formats differ, complex against component, discordant values, censored value, species), NOT_DETERMINABLE
    (fewer than two attributable targets remain, or a generic complex is the only measurement of a target) and PANEL_NOT_SELECTIVITY.
    A ratio is computed only for INTERPRETABLE and LIMITED groups.

Optional assay context (assay_context.tsv next to this file: assay id, cell type, assay type, organism, description, validity comment, as
the adapter in framework/adapters/chembl.py returns them) refines the grade; a missing field limits the comparison that depends on it and
is never a reason to drop the observation. Units are nM; species are kept. Reads relations.tsv next to this file; writes
selectivity_same_document.tsv."""
import argparse, csv, os, re, statistics, collections

H = os.path.dirname(os.path.abspath(__file__))
TECH = ("patch", "flipr", "efflux", "thallium", "flux", "binding", "displacement", "enzyme", "substrate")


def family(gene):
    m = re.match(r"[A-Za-z]+", gene or "")
    return m.group(0).upper() if m else ""


def composition(gene):
    g = [x for x in (gene or "").split("|") if x]
    if not g:
        return "no_gene"
    return "single" if len(g) == 1 else "defined_complex" if len(g) == 2 else "generic_complex"


def techniques(desc):
    d = (desc or "").lower()
    return {t for t in TECH if t in d}


def load_context():
    p = os.path.join(H, "assay_context.tsv")
    if not os.path.exists(p):
        return {}
    return {r["assay_id"]: r for r in csv.DictReader(open(p), delimiter="\t")}


def collect(rows):
    """key (compound, document, measure, species) -> list of observations (gene, label, relation, value_nM or None, assay_id)."""
    g = collections.defaultdict(list)
    for r in rows:
        if r["source"] == "chembl_activity":
            if r["target_label"] in ("Unchecked", "NON-PROTEIN TARGET"):
                continue
            t, doc, assay = (r["ref"].split(";") + ["", "", ""])[:3]
            key = (r["compound"], "chembl:" + doc, r["measure_type"], r["species"])
        elif r["source"] == "gtopdb":
            pm = r["ref"].split(";")[0]
            key, assay = (r["compound"], "gtopdb:" + pm, r["measure_type"], r["species"]), ""
        else:
            continue
        if not r["gene"]:
            continue
        v = float(r["value_nM"]) if r["value_nM"] != "" else None
        g[key].append((r["gene"], r["target_label"], r["relation"] or "=", v, assay))
    return g


def grade_group(obs, ctx):
    by = collections.defaultdict(lambda: {"vals": [], "cens": [], "novalue": 0, "assays": set()})
    for gene, lab, rel, v, assay in obs:
        d = by[gene]
        if assay:
            d["assays"].add(assay)
        if v is None:
            d["novalue"] += 1
        elif rel == "=":
            d["vals"].append(v)
        else:
            d["cens"].append(f"{rel}{v:.3g}")
    comp = {g: composition(g) for g in by}
    reasons = []
    generic = sorted(g for g, c in comp.items() if c == "generic_complex")
    attributable = [g for g in by if comp[g] in ("single", "defined_complex") and by[g]["vals"]]
    fams = {family(g.split("|")[0]) for g in attributable}
    if generic:
        reasons.append("complex of three or more subunits cannot be attributed to one subunit: " + "; ".join(generic))
    if len(fams) > 1:
        return "PANEL_NOT_SELECTIVITY", reasons + ["gene families differ (" + ", ".join(sorted(fams)) + "): a panel of activities, not a selectivity ratio"], by, comp, attributable
    if len(attributable) < 2:
        return "NOT_DETERMINABLE", reasons + ["fewer than two attributable targets with an exact value"], by, comp, attributable
    limited = list(reasons)
    kinds = {comp[g] for g in attributable}
    if len(kinds) > 1:
        limited.append("a defined complex is compared with a single component (composition differs)")
    assays = {a for g in attributable for a in by[g]["assays"]}
    if assays and not all(a in ctx for a in assays):
        limited.append("assay context not retained for " + str(sum(1 for a in assays if a not in ctx)) + " of " + str(len(assays)) + " assays")
    elif assays:
        cells = {ctx[a]["assay_cell_type"] for a in assays if ctx[a]["assay_cell_type"]}
        tsets = [techniques(ctx[a]["description"]) for a in assays]
        if len(cells) > 1:
            limited.append("cell systems differ: " + ", ".join(sorted(cells)))
        if tsets and not set.intersection(*tsets):
            limited.append("assay techniques differ (no shared technique among the descriptions)")
        if any(ctx[a]["data_validity_comment"] for a in assays):
            limited.append("a validity comment is attached to at least one assay")
    elif not assays:
        limited.append("assay identifiers not retained")
    for g in attributable:
        v = by[g]["vals"]
        if len(v) > 1 and max(v) / min(v) > 10:
            limited.append(f"discordant values inside {g} ({min(v):.3g} to {max(v):.3g})")
    if any(by[g]["cens"] for g in by):
        limited.append("censored value present for " + ", ".join(g for g in by if by[g]["cens"]) + " (listed, not used)")
    return ("LIMITED" if limited else "INTERPRETABLE"), limited, by, comp, attributable


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    rows = list(csv.DictReader(open(os.path.join(H, "relations.tsv")), delimiter="\t"))
    ctx = load_context()
    groups = collect(rows)
    cols = ["compound", "document", "measure", "species", "n_targets", "grade", "limits", "targets_median_nM [n; min-max; censored]", "ratio_extreme_target_medians", "ratio_not_computed_because"]
    with open(os.path.join(H, "selectivity_same_document.tsv"), "w") as f:
        f.write("\t".join(cols) + "\n")
        for k, obs in sorted(groups.items()):
            if len({o[0] for o in obs}) < 2:
                continue
            fams = collections.defaultdict(list)
            for o in obs:
                fams[family(o[0].split("|")[0])].append(o)
            parts = [(k, obs, "")]
            if len(fams) > 1:     # the document is a panel; each family with two or more targets is also graded on its own
                parts = [(k, obs, "")] + [((k[0], k[1] + "#" + fam, k[2], k[3]), fo, fam) for fam, fo in sorted(fams.items()) if len({o[0] for o in fo}) > 1]
            for k, obs, fam in parts:
                emit(f, k, obs, ctx, skip_if_undeterminable=bool(fam))


def emit(f, k, obs, ctx, skip_if_undeterminable=False):
    grade, reasons, by, comp, attr = grade_group(obs, ctx)
    if skip_if_undeterminable and grade == "NOT_DETERMINABLE":
        return     # a family inside a panel document with no exact pair adds nothing beyond the panel row
    cells = []
    for g, d in sorted(by.items()):
        med = f"{statistics.median(d['vals']):.3g}" if d["vals"] else "no exact value"
        span = f"{min(d['vals']):.3g}-{max(d['vals']):.3g}" if d["vals"] else "-"
        extra = (f"; censored {'/'.join(d['cens'])}" if d["cens"] else "") + (f"; {d['novalue']} row(s) without value" if d["novalue"] else "")
        cells.append(f"{g} [{comp[g]}]={med} [n={len(d['vals'])}; {span}{extra}]")
    ratio, why = "", ""
    if grade in ("INTERPRETABLE", "LIMITED"):
        meds = sorted(statistics.median(by[g]["vals"]) for g in attr)
        ratio = f"{meds[-1] / meds[0]:.3g}" if meds[0] > 0 else ""
    else:
        why = grade
    f.write("\t".join([k[0], k[1], k[2], k[3], str(len(by)), grade, " | ".join(reasons), "; ".join(cells)[:900], ratio, why]) + "\n")


if __name__ == "__main__":
    main()
