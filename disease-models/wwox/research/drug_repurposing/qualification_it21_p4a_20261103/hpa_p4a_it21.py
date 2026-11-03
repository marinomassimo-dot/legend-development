#!/usr/bin/env python3
"""IT21 P4a: Human Protein Atlas gene JSON for the six main targets (adult tissue and brain cell-class RNA summaries), written to expression_hpa_p4a_it21.tsv.
  hpa_p4a_it21.py run     live fetch (proteinatlas.org/<Ensembl id>.json); every attempt printed; a null field is written NULL, never zero
Standard library only; no key, no contact string. Adult atlas classes are not WWOX-deficient tissue and not developing tissue."""
import csv, json, sys, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENES = {"HDAC5": "ENSG00000108840", "KDM4C": "ENSG00000107077", "BTK": "ENSG00000010671", "EZH2": "ENSG00000106462", "MAPK1": "ENSG00000100030", "SIRT1": "ENSG00000096717",
         "NPY": "ENSG00000122585", "BCL3": "ENSG00000069399"}
KEYS = ["RNA tissue specificity", "RNA tissue distribution", "RNA single cell type specificity", "RNA single cell type distribution", "RNA brain regional specificity",
        "Single nuclei brain specificity", "Single nuclei brain distribution", "RNA tissue cell type enrichment", "Brain expression cluster"]


def main():
    if len(sys.argv) < 2 or sys.argv[1] != "run":
        print(__doc__)
        return
    rows = []
    for g, e in GENES.items():
        d, status = None, 0
        for wait in (0, 3, 8):
            time.sleep(wait)
            try:
                with urllib.request.urlopen(urllib.request.Request(f"https://www.proteinatlas.org/{e}.json", headers={"User-Agent": "legend-public-research/1.0"}), timeout=60) as r:
                    status, d = r.status, json.loads(r.read())
                break
            except Exception as ex:
                status = str(ex)[:60]
        print(g, e, status, flush=True)
        if not isinstance(d, dict):
            rows.append([g, e, f"SERVICE_ERROR {status}"] + [""] * len(KEYS))
            continue
        rows.append([g, e, "OK"] + [json.dumps(d.get(k), sort_keys=True)[:300] if d.get(k) is not None else "NULL" for k in KEYS])
    with open(HERE / "expression_hpa_p4a_it21.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["gene", "ensembl", "state"] + KEYS)
        w.writerows(rows)


if __name__ == "__main__":
    main()
