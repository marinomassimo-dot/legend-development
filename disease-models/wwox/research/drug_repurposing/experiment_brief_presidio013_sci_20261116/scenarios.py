#!/usr/bin/env python3
"""Outcome -> top set table for the L7 brief: apply declared outcome codes to the FROZEN cells in a scratch copy and run the
official generator (framework/scripts/aed_matrix.py) with the rule pinned. Nothing in the repository is modified.

Outcome code per arm (seizure endpoint, P13-P15, neocortex bursting preparation):
  S  suppresses KO bursts AND the effect is genotype-specific (drug-by-genotype contrast): new cell, tier 3, directness 3, match.
  G  suppresses KO bursts but also suppresses provoked wild-type bursts to the same degree (generic): new cell, tier 1, directness 3.
  N  does not suppress KO bursts: the class's existing links in the seizure windows are rejected (sign neutral, directness 0).
  A  aggravates (raises burst rate): aggravation cell, tier 3, directness 3 (recorded in the aggravation column, never netted).
The mapping is mine (declared here and in the brief); it is not part of rule v1.

Usage: scenarios.py REPO_ROOT OUTPUT_DIR   (REPO_ROOT holds framework/scripts/aed_matrix.py and the frozen cells and rule)
"""
import csv
import os
import re
import subprocess
import sys
import tempfile

A = "disease-models/wwox/research/drug_repurposing/aed_matrix_sci_20261116/output/cells_form.tsv"
RULE = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/rule.json"
HASH = "679a60894100d26bf4e550e2f49a888e39b8451dfbf428c2157f8b0cb2d94982"
ARMS = {"pore": "nmdar_pore_blocker", "glun2b": "glun2b_nam", "ampa": "ampa_antagonist", "ttype": "t_type_calcium",
        "gabaa": "gabaa_pam_nonbzd", "benzo": "benzodiazepine", "sodium": "sodium_channel"}
SC = {  # name: (description, {arm: code})
    "S1": ("pore blocker specific; GluN2B NAM and AMPA generic; the rest do nothing", dict(pore="S", glun2b="G", ampa="G", ttype="N", gabaa="N", benzo="N", sodium="N")),
    "S2": ("GABA-A PAM and benzodiazepine specific; pore blocker generic; the rest do nothing", dict(pore="G", glun2b="N", ampa="N", ttype="N", gabaa="S", benzo="S", sodium="N")),
    "S3": ("pore blocker and GABA-A PAM both specific; the rest do nothing", dict(pore="S", glun2b="N", ampa="N", ttype="N", gabaa="S", benzo="N", sodium="N")),
    "S4": ("GluN2B NAM specific, pore blocker generic; the rest do nothing", dict(pore="G", glun2b="S", ampa="N", ttype="N", gabaa="N", benzo="N", sodium="N")),
    "S5": ("every arm suppresses, none specific (generic suppression)", {a: "G" for a in ARMS}),
    "S6": ("sodium-channel blocker specific; the others generic", dict(pore="G", glun2b="G", ampa="G", ttype="G", gabaa="G", benzo="G", sodium="S")),
    "S7": ("no arm suppresses KO bursts", {a: "N" for a in ARMS}),
    "S8": ("pore blocker specific, GABA-A PAM and sodium-channel blocker aggravate (AH1, AH3), the rest do nothing", dict(pore="S", glun2b="N", ampa="N", ttype="N", gabaa="A", benzo="A", sodium="A")),
}
SEIZURE_WINDOWS = ("P13-P15", "later_unspecified")


def build(rows, head, arms):
    ix = {c: i for i, c in enumerate(head)}
    out = []
    for r in rows:
        r = r[:]
        code = next((arms[a] for a, c in ARMS.items() if c == r[ix["class_id"]]), None)
        if code == "N" and r[ix["endpoint"]] == "seizure" and r[ix["age"]] in SEIZURE_WINDOWS and r[ix["sign"]] in ("match", "unknown"):
            r[ix["sign"]] = "neutral"; r[ix["link_directness"]] = "0"
        out.append(r)
    for a, cls in ARMS.items():
        code = arms[a]
        if code in ("S", "G", "A"):
            for age in SEIZURE_WINDOWS:
                new = [""] * len(head)
                v = dict(cell_id=f"T21-{cls}-seizure-{age}", thread_id="T21", class_id=cls, agent_id="", endpoint="seizure", age=age,
                         sign="aggravation" if code == "A" else "match", evidence_tier="1" if code == "G" else "3", link_directness="3",
                         axis=f"L7-{cls}", origin_id="O-L7", has_genotype_contrast="yes" if code in ("S", "A") else "no",
                         has_drug_by_genotype="yes" if code in ("S", "A") else "no", unit="animals", source_locator="scenario of the L7 brief (not a result)")
                for k, val in v.items():
                    new[ix[k]] = val
                out.append(new)
    return out


def run(root, cells, tmp):
    p = subprocess.run(["python3", "framework/scripts/aed_matrix.py", "score", cells, RULE, "--expect-rule-sha256", HASH, "--out", tmp],
                       cwd=root, capture_output=True, text=True)
    return p.returncode, p.stdout


def main(root, outdir):
    os.makedirs(outdir, exist_ok=True)
    rows = list(csv.reader(open(os.path.join(root, A)), delimiter="\t")); head, body = rows[0], rows[1:]
    result = []
    with tempfile.TemporaryDirectory() as td:
        for name, (desc, arms) in SC.items():
            cells = os.path.join(td, f"{name}.tsv"); sc = os.path.join(td, f"{name}.scores.tsv")
            with open(cells, "w", newline="") as f:
                w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(head); w.writerows(build(body, head, arms))
            rc, so = run(root, cells, sc)
            top = re.search(r"\[seizure P13-P15\] top set \{([^}]*)\} size (\d+) of 15, informativeness ([0-9.]+): (\w+)", so)
            agg = []
            if rc == 0:
                for r in csv.DictReader(open(sc), delimiter="\t"):
                    if r["endpoint"] == "seizure" and r["window"] == "P13-P15" and r["aggravation_score"] not in ("", "0", "0.0"):
                        agg.append(f"{r['class_id']}:{r['aggravation_score']}")
            if top:
                result.append((name, desc, "; ".join(f"{a}={c}" for a, c in arms.items()), top.group(1), top.group(2), top.group(3), top.group(4), ",".join(agg) or "-"))
            else:
                nul = "null ordering (no class scores)" if "[seizure P13-P15] not scorable" in so else "no top-set line (rc %d)" % rc
                result.append((name, desc, "; ".join(f"{a}={c}" for a, c in arms.items()), nul, "15" if "null" in nul else "", "0" if "null" in nul else "", "", ",".join(agg) or "-"))
    with open(os.path.join(outdir, "scenarios.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["scenario", "description", "outcome_codes", "top_set_seizure_P13_P15", "size_of_15", "informativeness", "label", "aggravation_scores"])
        w.writerows(result)
    for r in result:
        print(r[0], "|", r[3], "| size", r[4], "|", r[6], "| agg", r[7])
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
