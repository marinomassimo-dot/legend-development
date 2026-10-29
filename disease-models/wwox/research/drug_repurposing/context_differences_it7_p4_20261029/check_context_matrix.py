#!/usr/bin/env python3
"""Deterministic check of context_matrix.tsv (IT7 package P4).

What it does, with no network and no download:
  1. structure: one header, rectangular rows, no blank or trailing lines, closed vocabularies,
     every (quantity, context) pair present exactly once;
  2. numbers: every row that carries a source_key is re-read from the local cycle table it names
     and the effect_value, vs_matched_null and animal_separated fields must equal what that table says;
  3. sign rules: a row labelled higher/lower must carry a value of that sign; UNKNOWN rows carry no value;
  4. README: the direction table printed by --wide must appear verbatim in README.md.
Other modes:
  --wide          print the quantity x context direction table (Markdown) generated from the matrix
  --animal-loo    leave-one-animal-out sign check of the mouse ISR set score (descriptive resampling)
Run with:  python3 -I check_context_matrix.py [--wide | --animal-loo]
Exit code 0 only if every check passes.
"""
import argparse
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.dirname(HERE)  # .../drug_repurposing

COLUMNS = ["quantity_id", "quantity", "context_id", "context", "lesion_class", "perturbation_mode",
           "species_tissue_stage", "direction", "effect_value", "vs_matched_null", "animal_separated",
           "effect_text", "evidence_class", "provenance", "unit_of_replication", "n", "key_caveats",
           "source_ref", "source_key"]
DIRECTIONS = {"higher", "lower", "higher_sign_only", "lower_sign_only", "higher_non_specific",
              "lower_non_specific", "no_resolvable_sign", "set_dependent", "sparse", "changed_unsigned",
              "UNKNOWN"}
EVIDENCE = {"measured_transcript", "measured_protein", "measured_metabolite", "measured_function",
            "inferred", "none"}
PROVENANCE = {"cycle_computed_table", "cycle_text_only", "source_paper_carried", "none"}
NULLSTATE = {"OUT_NULL", "IN_NULL", "NA"}
SEPSTATE = {"yes", "no", "NA"}
QUANTITIES = ["Q01", "Q02", "Q03", "Q04", "Q05", "Q06", "Q07", "Q08", "Q09", "Q10", "Q11", "Q12", "Q13", "Q14"]
CONTEXTS = ["ORG_KO", "HNPC_KD", "NEUR_KD", "MS_HIP", "MN_HIP", "MNULL_HIP", "MS_CTX", "FLY_KD", "FLY_KDA",
            "RAT", "P47T", "ORG_PT"]

P_ORG_SET = "hnpc_gse126075_it5_20261029/p7_organoid_set_summary.tsv"
P_ORG_GENE = "hnpc_gse126075_it5_20261029/p7_organoid_key_genes.tsv"
P_NPC_SET = "hnpc_gse126075_it5_20261029/set_summary.tsv"
P_NPC_GENE = "hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv"
P_M_SET = "mouse_wwox_p17_it6_p4_20261029/results/set_summary.tsv"
P_M_GENE = "mouse_wwox_p17_it6_p4_20261029/results/key_genes.tsv"


def read_tsv(rel):
    with open(os.path.join(MOD, rel), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def _flt(x):
    return float(x)


def _outside(mean, lo, hi):
    return mean < lo or mean > hi


def resolve(key, cache):
    """Return (value_string, outside_or_None, separated_or_None) for a source_key."""
    kind, *parts = key.split(":")
    if kind == "ORGSET":
        rows = cache.setdefault(P_ORG_SET, read_tsv(P_ORG_SET))
        r = [x for x in rows if x["set"] == parts[0]]
        assert len(r) == 1, key
        r = r[0]
        return r["mean_centred_R"], _outside(_flt(r["mean_centred_R"]), _flt(r["null_lo"]), _flt(r["null_hi"])), None
    if kind == "ORGGENE":
        rows = cache.setdefault(P_ORG_GENE, read_tsv(P_ORG_GENE))
        r = [x for x in rows if x["gene"] == parts[0]]
        assert len(r) == 1, key
        return r[0]["R_centred"], None, None
    if kind == "NPCSET":
        rows = cache.setdefault(P_NPC_SET, read_tsv(P_NPC_SET))
        r = [x for x in rows if x["set"] == parts[0] and x["contrast"] == parts[1]]
        assert len(r) == 1, key
        r = r[0]
        return r["mean_primary"], _outside(_flt(r["mean_primary"]), _flt(r["null_lo"]), _flt(r["null_hi"])), None
    if kind == "NPCGENE":
        rows = cache.setdefault(P_NPC_GENE, read_tsv(P_NPC_GENE))
        r = [x for x in rows if x["set"] == parts[0] and x["contrast"] == parts[1] and x["symbol"] == parts[2]]
        assert len(r) == 1, key
        return r[0]["R_centred"], None, None
    if kind == "MSET":
        rows = cache.setdefault(P_M_SET, read_tsv(P_M_SET))
        r = [x for x in rows if x["contrast"] == parts[0] and x["set"] == parts[1] and x["universe_thr_tpm"] == "1.0"]
        assert len(r) == 1, key
        r = r[0]
        return r["mean"], r["outside"] == "True", r["separated"] == "True"
    if kind == "MGENE":
        rows = cache.setdefault(P_M_GENE, read_tsv(P_M_GENE))
        r = [x for x in rows if x["contrast"] == parts[0] and x["gene"] == parts[1]]
        assert len(r) == 1, key
        return r[0]["R_centred"], None, r[0]["animal_separated"] == "True"
    raise ValueError("unknown source_key kind: " + key)


def load_matrix(path):
    with open(path, newline="", encoding="utf-8") as fh:
        raw = fh.read()
    problems = []
    if raw.endswith("\n\n") or not raw.endswith("\n"):
        problems.append("file must end with exactly one newline (no trailing blank line or note)")
    lines = raw.split("\n")[:-1]
    if not lines or lines[0].split("\t") != COLUMNS:
        problems.append("header differs from the declared column list")
    rows = []
    for i, ln in enumerate(lines[1:], start=2):
        cells = ln.split("\t")
        if len(cells) != len(COLUMNS):
            problems.append("line %d has %d fields, expected %d" % (i, len(cells), len(COLUMNS)))
            continue
        rows.append(dict(zip(COLUMNS, cells)))
    return rows, problems


def wide_table(rows):
    by = {(r["quantity_id"], r["context_id"]): r for r in rows}
    qname = {}
    for r in rows:
        qname[r["quantity_id"]] = r["quantity"]
    out = ["| Quantity | " + " | ".join(CONTEXTS) + " |", "|---|" + "---|" * len(CONTEXTS)]
    for q in QUANTITIES:
        cells = [by[(q, c)]["direction"] for c in CONTEXTS]
        out.append("| %s %s | %s |" % (q, qname[q], " | ".join(cells)))
    return "\n".join(out)


def check():
    fails = []
    rows, problems = load_matrix(os.path.join(HERE, "context_matrix.tsv"))
    fails += problems
    seen = {}
    cache = {}
    n_keyed = 0
    for r in rows:
        k = (r["quantity_id"], r["context_id"])
        seen[k] = seen.get(k, 0) + 1
        tag = "%s/%s" % k
        if r["quantity_id"] not in QUANTITIES or r["context_id"] not in CONTEXTS:
            fails.append(tag + ": unknown quantity or context id")
        if r["direction"] not in DIRECTIONS:
            fails.append(tag + ": direction outside vocabulary: " + r["direction"])
        if r["evidence_class"] not in EVIDENCE:
            fails.append(tag + ": evidence_class outside vocabulary")
        if r["provenance"] not in PROVENANCE:
            fails.append(tag + ": provenance outside vocabulary")
        if r["vs_matched_null"] not in NULLSTATE or r["animal_separated"] not in SEPSTATE:
            fails.append(tag + ": vs_matched_null or animal_separated outside vocabulary")
        for col in COLUMNS:
            if r[col].strip() == "" and col not in ("effect_value", "source_key"):
                fails.append("%s: empty field %s" % (tag, col))
        d = r["direction"]
        if d == "UNKNOWN":
            if r["effect_value"] or r["source_key"] or r["evidence_class"] != "none" or r["provenance"] != "none":
                fails.append(tag + ": UNKNOWN row must carry no value, no key, evidence none, provenance none")
        else:
            if r["evidence_class"] == "none" or r["provenance"] == "none":
                fails.append(tag + ": non-UNKNOWN row needs an evidence class and a provenance")
        if r["effect_value"]:
            v = _flt(r["effect_value"])
            if d.startswith("higher") and not v > 0:
                fails.append(tag + ": higher label with non-positive value")
            if d.startswith("lower") and not v < 0:
                fails.append(tag + ": lower label with non-negative value")
        if r["source_key"]:
            n_keyed += 1
            try:
                val, out, sep = resolve(r["source_key"], cache)
            except Exception as exc:  # noqa: BLE001
                fails.append("%s: source_key does not resolve (%s)" % (tag, exc))
                continue
            if _flt(val) != _flt(r["effect_value"]):
                fails.append("%s: effect_value %s != source %s" % (tag, r["effect_value"], val))
            if out is not None and r["vs_matched_null"] != ("OUT_NULL" if out else "IN_NULL"):
                fails.append("%s: vs_matched_null %s != source" % (tag, r["vs_matched_null"]))
            if out is None and r["vs_matched_null"] != "NA":
                fails.append(tag + ": source has no null but vs_matched_null is not NA")
            if sep is not None and r["animal_separated"] != ("yes" if sep else "no"):
                fails.append("%s: animal_separated %s != source" % (tag, r["animal_separated"]))
            if sep is None and r["animal_separated"] != "NA":
                fails.append(tag + ": source has no separation flag but animal_separated is not NA")
        else:
            if r["vs_matched_null"] != "NA" or r["animal_separated"] != "NA":
                fails.append(tag + ": no source_key, so vs_matched_null and animal_separated must be NA")
    for q in QUANTITIES:
        for c in CONTEXTS:
            if seen.get((q, c), 0) != 1:
                fails.append("pair %s/%s present %d times" % (q, c, seen.get((q, c), 0)))
    if len(rows) != len(QUANTITIES) * len(CONTEXTS):
        fails.append("row count %d != %d" % (len(rows), len(QUANTITIES) * len(CONTEXTS)))
    readme = os.path.join(HERE, "README.md")
    if os.path.exists(readme) and not fails:
        with open(readme, encoding="utf-8") as fh:
            if wide_table(rows) not in fh.read():
                fails.append("README.md does not contain the table printed by --wide (regenerate and paste it)")
    elif not os.path.exists(readme):
        fails.append("README.md missing")
    unknown = sum(1 for r in rows if r["direction"] == "UNKNOWN")
    print("rows %d, source-keyed %d, UNKNOWN %d, measured-or-carried %d" % (len(rows), n_keyed, unknown, len(rows) - unknown))
    if fails:
        for f in fails:
            print("FAIL " + f)
        return 1
    print("PASS all checks")
    return 0


def animal_loo():
    rows = read_tsv(P_M_SET)
    print("contrast\tn_ko\tn_ctl\tdiff_all\tloo_min\tloo_max\tsign_stable_under_leave_one_animal_out")
    for c in ["H_S", "H_N", "H_null", "C_S"]:
        r = [x for x in rows if x["contrast"] == c and x["set"] == "ISR_targets" and x["universe_thr_tpm"] == "1.0"][0]
        ko = json.loads(r["animal_scores_ko"])
        ct = json.loads(r["animal_scores_ctl"])
        mean = lambda a: sum(a) / len(a)  # noqa: E731
        full = mean(ko) - mean(ct)
        diffs = []
        for i in range(len(ko)):
            if len(ko) > 1:
                diffs.append(mean(ko[:i] + ko[i + 1:]) - mean(ct))
        for i in range(len(ct)):
            if len(ct) > 1:
                diffs.append(mean(ko) - mean(ct[:i] + ct[i + 1:]))
        stable = all(d > 0 for d in diffs) if full > 0 else all(d < 0 for d in diffs)
        print("%s\t%d\t%d\t%+.3f\t%+.3f\t%+.3f\t%s" % (c, len(ko), len(ct), full, min(diffs), max(diffs), "yes" if stable else "no"))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wide", action="store_true", help="print the quantity x context direction table")
    ap.add_argument("--animal-loo", action="store_true", help="leave-one-animal-out sign check of the mouse ISR score")
    a = ap.parse_args()
    if a.wide:
        rows, problems = load_matrix(os.path.join(HERE, "context_matrix.tsv"))
        if problems:
            print("\n".join(problems))
            return 1
        print(wide_table(rows))
        return 0
    if a.animal_loo:
        return animal_loo()
    return check()


if __name__ == "__main__":
    sys.exit(main())
