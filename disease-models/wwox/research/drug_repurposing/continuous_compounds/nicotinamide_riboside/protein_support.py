"""Report coverage of the eleven prespecified NAD-pathway genes in held WWOX proteomics."""
import csv
import hashlib
import json
from pathlib import Path
import sys

table = Path(sys.argv[1]) / "i18_proteome" / "zeng2024_table_s1_parsed.tsv"
manifest = json.loads(table.with_name("MANIFEST.json").read_text())
assert hashlib.sha256(table.read_bytes()).hexdigest() == manifest["table_sha256"]
with table.open() as stream:
    proteins = list(csv.DictReader(stream, delimiter="\t"))
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("symbol", "matching_rows", "log2FC", "BH_adjusted_p"))
for gene in "NMRK1 NMRK2 NAMPT NMNAT1 NMNAT2 NMNAT3 SARM1 CD38 PARP1 SLC25A51 SLC29A1".split():
    matches = [row for row in proteins if row["symbol"] == gene]
    assert len(matches) <= 1
    row = matches[0] if matches else {}
    writer.writerow((gene, len(matches), row.get("log2fc", "NA"), row.get("bh_adj_p", "NA")))
