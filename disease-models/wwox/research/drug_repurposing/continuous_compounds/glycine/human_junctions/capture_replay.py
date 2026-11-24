"""Enumerate every 86-base read crossing GRIN1's diagnostic boundary on four RefSeq RNAs."""
import csv
import gzip
import io
import subprocess
import sys
import tempfile
from pathlib import Path
from xml.etree import ElementTree as ET

forms = {r["accession"]:r for r in csv.DictReader(Path("capture_geometry.tsv").open(), delimiter="\t")}
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("accession","class","strand","rule","Q","crossing_starts","detected","wrong","conflict"))
with tempfile.TemporaryDirectory() as work:
    for rec in ET.parse("human_grin1.gb.xml").findall("GBSeq"):
        name = rec.findtext("GBSeq_accession-version")
        seq = rec.findtext("GBSeq_sequence").upper()
        form = forms[name]
        cut = int(form["junction_after_nt"])
        for strand in ("forward","reverse"):
            path = Path(work)/"window.fastq.gz"
            with gzip.open(path,"wt") as stream:
                for start in range(cut-85,cut):
                    window = seq[start:start+86]
                    if strand=="reverse":
                        window = window.translate(str.maketrans("ACGT","TGCA"))[::-1]
                    stream.write(f"@w{start}\n{window}\n+\n{'I'*86}\n")
            output = subprocess.check_output([sys.argv[1],"count","junction_probes.tsv",path],text=True)
            for row in csv.DictReader(io.StringIO(output),delimiter="\t"):
                correct = int(row[form["form"]])
                wrong = int(row["skipped" if form["form"]=="included" else "included"])
                assert (int(row["reads"]),correct,wrong,int(row["conflict"])) == (85,56 if row["rule"]=="centered" else 67,0,0)
                writer.writerow((name,form["form"],strand,row["rule"],row["Q"],85,correct,wrong,row["conflict"]))
