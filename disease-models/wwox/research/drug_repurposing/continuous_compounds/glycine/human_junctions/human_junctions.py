"""Generate one inclusion and one skipping junction sharing the same downstream exon."""
from pathlib import Path
from xml.etree import ElementTree as ET
import csv

reference = ET.parse("human_grin1.gb.xml")
forms = {}
for rec in reference.findall("GBSeq"):
    accession = rec.findtext("GBSeq_accession-version")
    features = rec.findall(".//GBFeature")
    exons = {f.findtext("GBFeature_location") for f in features if f.findtext("GBFeature_key")=="exon"}
    seq = rec.findtext("GBSeq_sequence").upper()
    if {"727..903", "904..966", "967..1067"} <= exons:
        label, junction = "included", 966
    else:
        assert {"727..903", "904..1004"} <= exons
        label, junction = "skipped", 903
    forms[accession] = label, junction, seq
with open("junction_probes.tsv", "w") as out:
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(("class","offset","seq"))
    for label in ("included","skipped"):
        for offset in range(10,22):
            probe, = {s[j-offset:j+31-offset] for c,j,s in forms.values() if c==label}
            assert all((probe in s)==(c==label) for c,j,s in forms.values())
            writer.writerow((label,offset,probe))
