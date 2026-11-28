"""Verify named destinations in the existing shareable Pages bundle."""
import argparse
from collections import Counter
import csv
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = Counter()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if anchor := attrs.get("id"):
            self.ids[anchor] += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pages", type=Path, help="directory written by the existing Pages package command")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    dossier = Path(__file__).resolve().parent
    dr = dossier.parents[1]
    sys.path.insert(0, str(dr.parents[3] / "framework" / "scripts"))
    import repurposing_view as view
    from repurposing_compound_analyses import comparison_cards, load_cards, public_slug

    page = (args.pages / "index.html").read_text()
    anchors = Anchors()
    anchors.feed(page)
    public_items = view.build_payload(dr, "shareable")["cur"]["ranking"]["compound_view"]
    cards = load_cards(dr, public_items)
    scope = {(item["inv_id"], public_slug(name["label"]))
             for item in public_items for name in item.get("names_public", [])}
    scope.update((card["investigation"], slug) for slug, card in comparison_cards(dr) if card["investigation"])
    if anchors.ids["compound-analyses"] != 1:
        raise ValueError("Use the Pages bundle with exactly one Compound Analyses section")

    investigation_links = {}
    for row in re.findall(r'<li class="inv-row\b[^>]*>.*?(?=<li class="inv-row\b|</section>)', page, re.S):
        iid = re.search(r'\bid="(INV-\d+)"', row)
        navigation = re.search(r'<p class="ca-investigation-links">.*?</p>', row, re.S)
        if iid and navigation:
            investigation_links[iid.group(1)] = set(re.findall(r'href="([^"]+)"', navigation.group()))

    rows = []
    for iid, slug in sorted(scope):
        destination = f"analysis-{slug}"
        card = cards[slug]
        if anchors.ids[destination] != 1 or f"#{destination}" not in investigation_links.get(iid, set()) or anchors.ids[iid] != 1:
            raise ValueError(f"Missing or ambiguous rendered destination {iid} / {destination}")
        rows.append((iid, card["name"], f"#{destination}", card["group"],
                     card.get("role") or "Existing dossier", len(card["links"])))

    match = re.search(r'<article class="ca-card" id="analysis-ketamine">.*?</article>', page, re.S)
    required = ('href="reports/ketamine.pdf"', 'href="#INV-05"', 'continuous_compounds/ketamine/README.md')
    if not match or any(link not in match.group() for link in required):
        raise ValueError("Ketamine card is missing its PDF, INV-05, or evidence link")
    if (args.pages / "reports" / "ketamine.pdf").read_bytes() != (dr / "view/research_reports/ketamine.pdf").read_bytes():
        raise ValueError("Packaged ketamine PDF differs from the research report")

    with args.output.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(("investigation", "compound", "anchor", "group", "research_role", "dossier_links"))
        writer.writerows(rows)
    print(f"{len(rows)} investigation-to-compound routes verified, in {len({row[2] for row in rows})} distinct cards.")


if __name__ == "__main__":
    main()
