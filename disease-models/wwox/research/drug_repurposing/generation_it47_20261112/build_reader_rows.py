"""IT47 P1: the dashboard reader table (generation_it40_20261109/reader_view.tsv) gets the conditional hypotheses that the generator now reads from the hypotheses_only packages.
Rows are built from conditional_proposals_packages_it47.tsv with the same cell mapping (no second mapping); only rows listed in SHOW are written, and a row whose text would carry a
catalogue compound name is refused by the shareable audit, so SHOW is chosen after running it. Idempotent (a hyp_id already present is left alone).  python3 build_reader_rows.py"""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
csv.field_size_limit(10**9)
SHOW = {"ph_k2p_sci45_20261111::KP1": "KP1", "nrf2_inv08_20261107::H1": "NRF2-H1", "nrf2_inv08_20261107::H2": "NRF2-H2", "gsk3_eif2b_20261107::H1": "GSK3-H1",
        "potassium_conductances_sci43_20261110::KH1": "KH1-K", "hcn_20261107::HY1": "HY1-HCN", "isr_inv02_it50_20261113::ISR1": "ISR1-INV02"}   # IT49: one row of each newly mapped package
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
        reopen = r.get("reopen_or_abandon", "")
        if reopen and not reopen.startswith("not stated"):
            # IT49: a package that states what would weaken it (opposite or weakening cells) fills `weaken` from those cells; the outcome that would favour it is a measurement outcome, not a prediction.
            dm = [x for x in r["decision_measure"].split(" | ") if x.strip()]
            fav = [clean(x) for x in dm if x.split(":", 1)[0].startswith("favourable")]
            rest = [clean(x) for x in dm if not x.split(":", 1)[0].startswith("favourable")]
            rows[-1]["weaken"] = " || ".join(short(clean(x), 400) for x in reopen.split(" | ") if x.strip())
            rows[-1]["strengthen"] = rows[-1]["strengthen"] + (" What would favour it (a measurement outcome, not a prediction): " + " ".join(fav) if fav else "") + (" Measure: " + " ".join(rest) if rest else "")
            prem = r["premise_and_action"].split(" || unresolved premise: ", 1)[-1] if " || unresolved premise: " in r["premise_and_action"] else ""
            if prem:
                cut = prem.find("[IT4")                                  # dated updates (IT48, IT49) are kept whole: they carry the limits that must travel with the row
                base, upd = (prem[:cut], prem[cut:]) if cut >= 0 else (prem, "")
                if "Missing bridge:" in base:                             # the premise lives inside the relation cell: show only the bridge, not the relation twice
                    base = base[base.index("Missing bridge:") + len("Missing bridge:"):]
                rows[-1]["hypothesised"] += " Unresolved premise: " + short(clean(base.strip()), 360) + (" " + upd.strip() if upd else "")
            for k in ("label", "observed", "hypothesised", "alternatives", "strengthen", "weaken"):    # tool names the shareable audit refuses in public text
                for a, b in (("a ZD7288-insensitive component", "a component insensitive to the Ih tool blocker"), ("ZD7288-insensitive", "insensitive to the Ih tool blocker"), ("ZD7288", "the Ih tool blocker"), ("XE991", "the Kv7 tool blocker"), ("experiment.tsv X1-X3", "the package steps X1-X3")):
                    rows[-1][k] = rows[-1][k].replace(a, b)
        added += 1
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fields, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    print("added", added)


if __name__ == "__main__":
    main()
