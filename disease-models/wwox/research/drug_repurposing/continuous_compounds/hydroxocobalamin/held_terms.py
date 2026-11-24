"""Count disease-titled held JATS articles and identify bounded biomarker leads."""
import csv
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "folinic_acid"))
from held_audit import TITLE

terms = {
    "methylmalonate": r"methylmalon(?:ic|ate)",
    "homocysteine": r"homocyst(?:eine|ine)|\btHcy\b",
    "cobalamin": r"cobalamin|vitamin\s*B[- ]?12\b",
}
studies = {}
for path in sorted((Path(sys.argv[1]) / "fulltext").glob("*.xml")):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError:
        continue
    for article in [root] if root.tag == "article" else root.findall(".//article"):
        meta = article.find("front/article-meta")
        if meta is None:
            continue
        pmid = meta.findtext("article-id[@pub-id-type='pmid']")
        title = meta.find("title-group/article-title")
        body = article.find("body")
        if not pmid or body is None or title is None or not TITLE.search("".join(title.itertext())):
            continue
        hits = studies.setdefault(pmid, set())
        for paragraph in body.iter("p"):
            passage = "".join(paragraph.itertext())
            hits.update(key for key, pattern in terms.items() if re.search(pattern, passage, re.I))
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("eligible_unique_PMIDs", "PMID", "body_paragraph_terms"))
for pmid, hits in sorted(studies.items()):
    if hits:
        writer.writerow((len(studies), pmid, ",".join(sorted(hits))))
if not any(studies.values()):
    writer.writerow((len(studies), "NA", "no_hits"))
