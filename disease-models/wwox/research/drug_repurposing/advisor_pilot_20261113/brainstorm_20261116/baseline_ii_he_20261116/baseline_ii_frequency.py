"""Baseline (ii): the frequency-of-use ranking of the 15 rule classes, from IT's feasibility census (counts only).

    python3 baseline_ii_frequency.py CENSUS.tsv OUT.tsv

The measure is `children_with_a_row`: how many children of the A1 series have a row for the class (IT's upper bound; links
marked "possible" are not merged). It says how OFTEN a class appears in the series; it carries no outcome. Ties stay ties
(competition rank). The mapping from the census rows to the rule's class ids is the only judgement and is written below.
"""
import csv
import sys

# rule class id -> (census row, note)
MAPPING = {
    "gaba_at_gat": ("GABA-AT (vigabatrin)", ""),
    "ketogenic_diet": ("ketogenic diet", ""),
    "steroid_acth": ("steroid/ACTH (hormonal)", ""),
    "benzodiazepine": ("benzodiazepine and other GABA-A modulators", "merged census row: benzodiazepines and non-benzodiazepine GABA-A modulators are not separable, both rule classes carry the same upper bound"),
    "gabaa_pam_nonbzd": ("benzodiazepine and other GABA-A modulators", "merged census row: benzodiazepines and non-benzodiazepine GABA-A modulators are not separable, both rule classes carry the same upper bound"),
    "cbd_fenfluramine": ("cannabidiol", "the census counts cannabidiol alone; its fenfluramine-type row is 0"),
    "carbonic_anhydrase_multitarget": ("carbonic-anhydrase / multi-target", ""),
    "sv2a": ("SV2A (levetiracetam)", ""),
    "valproate_type": ("valproate-type", ""),
    "sodium_channel": ("sodium-channel", ""),
    "t_type_calcium": ("T-type (ethosuximide), AMPA (perampanel), fenfluramine-type, mTOR-type, pyridoxine", "one census row for five groups, all 0"),
    "ampa_antagonist": ("T-type (ethosuximide), AMPA (perampanel), fenfluramine-type, mTOR-type, pyridoxine", "one census row for five groups, all 0"),
    "nmdar_pore_blocker": (None, "no census row: 0 by absence from the series"),
    "glun2b_nam": (None, "no census row: 0 by absence from the series"),
    "kv7_opener": (None, "no census row: 0 by absence from the series"),
}
COLUMNS = ["class_id", "census_row", "children_with_a_row", "reports", "rank", "tied_with", "mapping_note"]


def main(census_path, out_path):
    with open(census_path, newline="") as handle:
        census = {r["mechanism_class"]: r for r in csv.DictReader(handle, delimiter="\t")}
    rows = []
    for cls, (row, note) in MAPPING.items():
        src = census[row] if row else None
        rows.append({"class_id": cls, "census_row": row or "none", "children_with_a_row": int(src["children_with_a_row"]) if src else 0,
                     "reports": int(src["reports"]) if src else 0, "mapping_note": note})
    rows.sort(key=lambda r: (-r["children_with_a_row"], r["class_id"]))
    for r in rows:
        r["rank"] = 1 + sum(o["children_with_a_row"] > r["children_with_a_row"] for o in rows)
        r["tied_with"] = ",".join(o["class_id"] for o in rows if o is not r and o["children_with_a_row"] == r["children_with_a_row"])
    with open(out_path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
