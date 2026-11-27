#!/usr/bin/env python3
"""Replay descriptive membrane-potential differences from Breton et al. Table 1."""

from decimal import Decimal
from hashlib import sha256
from pathlib import Path
import sys
from xml.etree import ElementTree


EXPECTED_SHA256 = "934b4e1a42ac19f5cd8912994fb171beabdeb94a6631b23d9a383dab1db906aa"
CONTRASTS = (
    ("putative_pyramidal", "Resting membrane potential", "S-WT", 0, 2),
    ("putative_pyramidal", "Resting membrane potential", "S-HT", 1, 2),
    ("untyped_interneuron", "Resting membrane potential", "pooled_S-WT_and_S-HT", 3, 4),
    ("untyped_interneuron", "AP amplitude", "pooled_S-WT_and_S-HT", 3, 4),
)


def main(xml_path):
    raw = Path(xml_path).read_bytes()
    if sha256(raw).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("Expected the held PMC8609180 XML. The source fingerprint differs.")
    table = ElementTree.fromstring(raw).find(".//table-wrap")
    rows = {}
    for row in table.iter("tr"):
        label, *values = (" ".join("".join(cell.itertext()).split()) for cell in row)
        rows[label] = values
    sample_counts = rows["N's (# cells/# animals)"]

    print(
        "region_age", "cell_class", "metric", "comparator", "comparator_cells_animals",
        "KO_cells_animals", "comparator_mean_mV", "KO_mean_mV", "KO_minus_comparator_mV",
        sep="\t",
    )
    for cell_class, metric, comparator, comparison_index, ko_index in CONTRASTS:
        comparison, knockout = (
            Decimal(rows[metric][index].split()[0].replace("−", "-"))
            for index in (comparison_index, ko_index)
        )
        print(
            "L2-3_neocortex_mouse_P13-P17", cell_class, metric, comparator,
            sample_counts[comparison_index], sample_counts[ko_index],
            comparison, knockout, knockout - comparison, sep="\t",
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 replay_native_voltage.py ARTICLE_XML")
    main(sys.argv[1])
