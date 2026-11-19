"""ADV-097 item 1 (IT, 2026-11-19): what the repository's compound catalogue actually holds for the premise-stage threads of the broad objective.
Read-only and offline: for each (thread, name) it calls framework/scripts/repurposing_search.py `compound <name> --json` and records whether the catalogue has a record,
its status class and access flag, how many target rows it carries and which needs it touches (need, target, action, direction state).
The NAMES are IT's own list of candidate classes and tool compounds from general pharmacology knowledge, written before the lookups (not read from a source in this window):
a name's presence or absence in the catalogue is the measurement; absence is NOT absence of the compound in the world.
Usage: python3 -I catalogue_lookup_it_20261119.py REPO_ROOT   |   --help"""
import csv, json, subprocess, sys
from pathlib import Path

if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0 if len(sys.argv) > 1 else 2)
ROOT = Path(sys.argv[1]).resolve()
HERE = Path(__file__).resolve().parent
NAMES = {
    "INV-02 ISR attenuation": ["ISRIB", "trazodone", "dibenzoylmethane", "GSK2606414", "GSK2656157", "salubrinal", "guanabenz", "sephin1", "icerguastat", "ceapin"],
    "INV-06 pro-myelinating": ["clemastine", "benztropine", "clobetasol", "miconazole", "tiratricol", "liothyronine", "bexarotene", "metformin", "quetiapine"],
    "INV-07 PDH block": ["dichloroacetate", "AZD7545", "lipoic acid", "thiamine", "pyruvate", "leelamine"],
    "INV-08 KEAP1/NRF2": ["dimethyl fumarate", "monomethyl fumarate", "sulforaphane", "omaveloxolone", "bardoxolone", "tert-butylhydroquinone"],
    "INV-12 thyroid-hormone receptor agonists": ["tiratricol", "liothyronine", "sobetirome", "eprotirome", "levothyroxine"],
    "INV-13 Q230P-class clearance and chaperones": ["forigerimod", "VER-155008", "4-phenylbutyrate", "arimoclomol", "ambroxol", "bortezomib", "chloroquine"],
    "INV-14 EZH2": ["GSK343", "tazemetostat", "GSK126", "valemetostat", "EED226"],
    "INV-16 class IIa HDAC": ["TMP269", "MC1568", "TMP195", "LMK-235", "vorinostat", "valproate", "butyrate"],
    "INV-17 MYC": ["JQ1", "omomyc", "10058-F4", "palbociclib"],
    "INV-18 Ih (HCN)": ["ivabradine", "ZD7288", "zatebradine", "cilobradine", "lamotrigine", "gabapentin"],
}
rows = []
for thread, names in NAMES.items():
    for n in names:
        r = subprocess.run([sys.executable, "-B", str(ROOT / "framework/scripts/repurposing_search.py"), "compound", n, "--json"],
                           capture_output=True, text=True, cwd=ROOT)
        try:
            recs = json.loads(r.stdout) if r.stdout.strip().startswith("[") else []
        except ValueError:
            recs = []
        if not recs:
            rows.append((thread, n, "NOT_IN_CATALOGUE", "", "", "", "", ""))
            continue
        for c in recs:
            touched = "; ".join(sorted({f"{x['need']}:{x['target']}:{x['action_on_target']}:{x['consistency']}" for x in c.get("needs_touched", [])}))
            rows.append((thread, n, "IN_CATALOGUE", c["catalogue_id"], c["name"], c["status_class"], "|".join(c.get("access", [])), f"target_rows={c['n_target_rows']}; " + touched))
with (HERE / "catalogue_lookup_it_20261119.tsv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["thread", "queried_name", "result", "catalogue_id", "catalogue_name", "status_class", "access", "targets_and_needs"])
    w.writerows(rows)
print(len(rows), sum(r[2] == "IN_CATALOGUE" for r in rows))
