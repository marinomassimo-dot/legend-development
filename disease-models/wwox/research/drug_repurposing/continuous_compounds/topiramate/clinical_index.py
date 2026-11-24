"""Index topiramate mentions in the held disease-titled JATS corpus; lead finding only."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "folinic_acid"))
from held_audit import TITLE

terms = re.compile(r"\b(topiramate|topamax|TPM)\b", re.I)
studies = {}
for path in sorted((Path(sys.argv[1]) / "fulltext").glob("*.xml")):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError:
        continue
    for article in [root] if root.tag == "article" else root.findall(".//article"):
        title = article.find("front/article-meta/title-group/article-title")
        body = article.find("body")
        pmid = article.findtext("front/article-meta/article-id[@pub-id-type='pmid']")
        if not pmid or body is None or title is None or not TITLE.search("".join(title.itertext())):
            continue
        hits = studies.setdefault(pmid, set())
        for section in (*body.iter("p"), *body.iter("table")):
            hits.update(m.group().lower() for m in terms.finditer(" ".join(section.itertext())))
print("eligible_PMIDs\tPMID\tbody_or_table_matches")
for pmid, hits in sorted(studies.items()):
    if hits:
        print(len(studies), pmid, ",".join(sorted(hits)), sep="\t")
