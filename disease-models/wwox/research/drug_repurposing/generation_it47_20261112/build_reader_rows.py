"""IT47 P1: the dashboard reader table (generation_it40_20261109/reader_view.tsv) gets the conditional hypotheses that the generator now reads from the hypotheses_only packages.
Rows are built from conditional_proposals_packages_it47.tsv with the same cell mapping (no second mapping); only rows listed in SHOW are written, and a row whose text would carry a
catalogue compound name is refused by the shareable audit, so SHOW is chosen after running it. Idempotent (a hyp_id already present is left alone).  python3 build_reader_rows.py"""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
csv.field_size_limit(10**9)
SHOW = {"ph_k2p_sci45_20261111::KP1": "KP1", "nrf2_inv08_20261107::H1": "NRF2-H1", "nrf2_inv08_20261107::H2": "NRF2-H2", "gsk3_eif2b_20261107::H1": "GSK3-H1"}
import re
PFX = re.compile(r"^[A-Za-z_]+: ")
clean = lambda t: PFX.sub("", t.strip())
short = lambda t, n=150: t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"


def main():
    pk = {r["proposal_id"].replace("CP-", ""): r for r in csv.DictReader(open(DR / "generation_it40_20261109/conditional_proposals_packages_it47.tsv", encoding="utf-8"), delimiter="\t")}
    f = DR / "generation_it40_20261109/reader_view.tsv"
    rows = list(csv.DictReader(open(f, encoding="utf-8", newline=""), delimiter="\t")); have = {r["hyp_id"] for r in rows}; fields = list(rows[0].keys()); added = 0
    for key, hid in SHOW.items():
        if hid in have:
            continue
        r = pk[key]
        rel = clean(r["premise_and_action"].split(" || ")[0].replace("relation: ", "", 1))
        rivals = " || ".join(short(x.strip(), 140) for x in r["competing_explanations"].split("rivals, complementary or compatible): ", 1)[-1].strip(" |").split(" || ") if x.strip())
        rows.append(dict(hyp_id=hid, inv_id=r["inv_id"], label=short(r["package_title"] or rel), observed=(clean(r["starting_observation_and_chain"].split(" [source")[0]) if not r["starting_observation_and_chain"].startswith("not stated") else ("Recorded support, not a new observation (it may include the package's own audit remarks): " + clean(r["recorded_support"]) if r["recorded_support"] else "Not stated by the package as an observation.")),
                         hypothesised=(rel if rel != r["package_title"] else r["package_title"]) + ". Exploratory: the package states no therapeutic direction.", alternatives=(("Alternatives the package states: " + clean(r["competing_explanations"].split(" || other rows of the same package")[0]) + " || ") if r["competing_explanations"].split(" || other rows of the same package")[0].strip() else "") + "Other rows of the package, not classified by it as rivals, complementary or compatible: " + rivals, strengthen=(clean(r["expected_result_by_explanation"]) if not r["expected_result_by_explanation"].startswith("not stated") else "Not stated by the package (missing): a falsifiable prediction is not given."),
                         weaken=clean(r["decision_measure"]), source_rows=r["package_ref"]))
        added += 1
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fields, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    print("added", added)


if __name__ == "__main__":
    main()
