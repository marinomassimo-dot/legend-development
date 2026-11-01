#!/usr/bin/env python3
"""Regrade a package's relations table with the CURRENT grader. Reads --relations (selectivity_p6 relations format, optional target_type column) and
--context (assay_context.tsv format), writes --out with the columns of selectivity_same_document.tsv; with --keep, columns of an existing table that the
grader does not produce (compound name, phase, reviewer note) are carried over by (compound, document, measure, species). `--help` is safe."""
import argparse, csv, collections, importlib.util, io, os
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("selectivity_p6", os.path.join(H, "selectivity_p6.py")); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--relations", required=True); ap.add_argument("--context", required=True); ap.add_argument("--out", required=True); ap.add_argument("--keep")
    a = ap.parse_args()
    rr = list(csv.DictReader(open(a.relations, encoding="utf-8"), delimiter="\t"))
    cx = {r["assay_id"]: r for r in csv.DictReader(open(a.context, encoding="utf-8"), delimiter="\t")}
    buf = io.StringIO(); S.SEEN.clear()
    groups = S.collect(rr)
    buf.write("\t".join(["compound", "document", "measure", "species", "n_targets", "grade", "limits", "targets_median_nM [n; min-max; censored]", "ratio_extreme_target_medians", "ratio_not_computed_because"]) + "\n")
    for k, obs in sorted(groups.items()):
        if len({o[0] for o in obs}) < 2:
            continue
        fams = collections.defaultdict(list)
        for o in obs:
            fams[S.family(o[0].split("|")[0])].append(o)
        parts = [(k, obs, "")]
        if len(fams) > 1:
            parts += [((k[0], k[1] + "#" + fam, k[2], k[3]), fo, fam) for fam, fo in sorted(fams.items()) if len({o[0] for o in fo}) > 1]
        for kk, oo, fam in parts:
            S.emit(buf, kk, oo, cx, skip_if_undeterminable=bool(fam))
    new = list(csv.DictReader(io.StringIO(buf.getvalue()), delimiter="\t"))
    extra, cols = {}, list(new[0].keys()) if new else []
    if a.keep and os.path.exists(a.keep):
        old = list(csv.DictReader(open(a.keep, encoding="utf-8"), delimiter="\t"))
        keepcols = [c for c in (old[0].keys() if old else []) if c not in cols]
        extra = {(r["compound"], r["document"], r["measure"], r["species"]): {c: r[c] for c in keepcols} for r in old}
        cols = [c for c in (old[0].keys() if old else []) if c in keepcols and c != "reviewer_note"][:3] + cols + (["reviewer_note"] if "reviewer_note" in keepcols else [])
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n"); w.writeheader()
        for r in new:
            r.update(extra.get((r["compound"], r["document"], r["measure"], r["species"]), {})); w.writerow({c: r.get(c, "") for c in cols})
    print(len(new), "rows;", dict(collections.Counter(r["grade"] for r in new)))


if __name__ == "__main__":
    main()
