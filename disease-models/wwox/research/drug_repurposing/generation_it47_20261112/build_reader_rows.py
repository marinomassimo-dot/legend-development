"""IT47 P1: the dashboard reader table (generation_it40_20261109/reader_view.tsv) gets the conditional hypotheses that the generator now reads from the hypotheses_only packages.
Rows are built from conditional_proposals_packages_it47.tsv with the same cell mapping (no second mapping); only rows listed in SHOW are written, and a row whose text would carry a
catalogue compound name is refused by the shareable audit, so SHOW is chosen after running it. Idempotent (a hyp_id already present is left alone).  python3 build_reader_rows.py"""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
csv.field_size_limit(10**9)
SHOW = {"ph_k2p_sci45_20261111::KP1": "KP1", "nrf2_inv08_20261107::H1": "NRF2-H1", "nrf2_inv08_20261107::H2": "NRF2-H2"}
import re
PFX = re.compile(r"^[a-z_]+: ")
clean = lambda t: PFX.sub("", t.strip())


def main():
    pk = {r["proposal_id"].replace("CP-", ""): r for r in csv.DictReader(open(DR / "generation_it40_20261109/conditional_proposals_packages_it47.tsv", encoding="utf-8"), delimiter="\t")}
    f = DR / "generation_it40_20261109/reader_view.tsv"
    rows = list(csv.DictReader(open(f, encoding="utf-8", newline=""), delimiter="\t")); have = {r["hyp_id"] for r in rows}; fields = list(rows[0].keys()); added = 0
    for key, hid in SHOW.items():
        if hid in have:
            continue
        r = pk[key]
        rel = clean(r["premise_and_action"].split(" || ")[0].replace("relation: ", "", 1))
        rivals = r["competing_explanations"].split("rival rows of the same package: ", 1)[-1].strip(" |")
        rows.append(dict(hyp_id=hid, inv_id=r["inv_id"], label=(r["package_title"] or rel)[:160], observed=clean(r["starting_observation_and_chain"].split(" [source")[0]),
                         hypothesised=(rel if rel != r["package_title"] else r["package_title"]) + ". Exploratory: the package states no therapeutic direction.", alternatives=rivals, strengthen=clean(r["expected_result_by_explanation"]),
                         weaken=clean(r["decision_measure"]), source_rows=r["package_ref"]))
        added += 1
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fields, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    print("added", added)


if __name__ == "__main__":
    main()
