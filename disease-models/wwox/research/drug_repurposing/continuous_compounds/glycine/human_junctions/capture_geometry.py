"""Measure the diagnostic junction's distance to the annotated transcript 3' end."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

with Path("junction_probes.tsv").open() as stream:
    probes = [p for p in csv.DictReader(stream, delimiter="\t") if p["offset"] == "15"]
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("accession", "form", "transcript_nt", "junction_after_nt", "downstream_nt"))
for record in ET.parse("human_grin1.gb.xml").findall("GBSeq"):
    seq = record.findtext("GBSeq_sequence").upper()
    probe, = [p for p in probes if p["seq"] in seq]
    assert seq.count(probe["seq"]) == 1
    junction = seq.index(probe["seq"]) + int(probe["offset"])
    writer.writerow((record.findtext("GBSeq_accession-version"), probe["class"], len(seq),
                     junction, len(seq)-junction))
