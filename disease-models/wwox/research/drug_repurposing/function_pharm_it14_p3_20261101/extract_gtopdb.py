#!/usr/bin/env python3
"""Extract interaction rows of a fixed ligand-ID list from the public GtoPdb bulk
download (interactions.tsv, version in its first line). Records only what the
source states. Usage: extract_gtopdb.py <interactions.tsv> <out.tsv>.
Licence of source: ODbL (database) + CC BY-SA 4.0 (contents); attribute IUPHAR/BPS."""
import csv, sys
IDS = {"4821":"vigabatrin","7149":"clobazam","4818":"tiagabine","4669":"NNC-711","2601":"retigabine",
       "12650":"azetukalner","2596":"XE991","4197":"gabazine","4168":"d-AP5","11942":"ganaxolone",
       "2599":"linopirdine","14111":"ICA-069673","4348":"zolpidem","6963":"clonazepam","3364":"diazepam"}
COLS = ["Ligand ID","Ligand","Target","Target Gene Symbol","Target Species","Type","Action","Action comment",
        "Selectivity","Primary Target","Affinity Units","Affinity Median","Affinity Low","Affinity High",
        "Original Affinity Relation","Assay Description","Receptor Site","PubMed ID"]
def main():
    if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); return 0 if len(sys.argv) > 1 and sys.argv[1] in ("-h","--help") else 2
    with open(sys.argv[1], encoding="utf8", errors="ignore") as fh:
        version = fh.readline().strip()
        rows = [r for r in csv.DictReader(fh, delimiter="\t") if r["Ligand ID"] in IDS]
    with open(sys.argv[2], "w", newline="", encoding="utf8") as out:
        w = csv.writer(out, delimiter="\t", lineterminator="\n")
        w.writerow(["source_version"] + COLS)
        for r in rows:
            w.writerow([version] + [(r[c] or "").replace("\t"," ").replace("\n"," ") for c in COLS])
    print(len(rows), "rows")
    return 0
if __name__ == "__main__": sys.exit(main())
