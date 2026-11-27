"""Replay the published synaptic curve, exposure ratios and OGD archive coverage."""

import argparse
from collections import Counter, defaultdict
import csv
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path

FIG7_DIGEST = "565041bc737e1c959dd34eccaa956687109fd4470a139ea4cd20bb7087e6bdd0"
ARCHIVE_PAGES = {
    0: "256e31b9ad8dbe2983e6b1707e1ae18e13f05a252cfee128bf7738ce3b7b00e5",
    500: "a640edebcede5e550bb0643ae750e546d455ed8bca0bc6a361dd7555e90872b5",
    1000: "bfdfbe14fbf002f9823454f9b780dcb62b7e997a287d5b1376d27d4eab3700f4",
    1500: "e211fd8ed489ff1d014d9fa5d3f15dd6802652b45b81c451a208ae1b908aecec",
}


def checked_bytes(path, expected):
    raw = path.read_bytes()
    if sha256(raw).hexdigest() != expected:
        raise ValueError(f"Source fingerprint differs for {path}")
    return raw


def functional_rows(figure):
    checked_bytes(figure, FIG7_DIGEST)
    # Fig. 7g has 40% at pixel y=739 and 120% at y=556 (origin at top left).
    # The centres below are visual digitization of the group-mean markers.
    # Avoid the origin point, which overlaps the y-axis.
    marker_positions = (
        (2.5, 599.5), (5, 600), (7.5, 614), (10, 631.5), (12.5, 647),
        (15, 647), (17.5, 639), (20, 630), (22.5, 619), (25, 612),
        (27.5, 602), (30, 600),
    )
    for time, marker_y in marker_positions:
        frequency = 40 + (739 - marker_y) * 80 / (739 - 556)
        yield "Parodi Fig. 7g, digitized", f"{time:g} min", f"{frequency:.1f}", "% pre-drug frequency", f"marker y={marker_y:g}"

    csf_low = Decimal(39) / Decimal("130.10")
    csf_high = Decimal(79) / Decimal("130.10")
    for label, concentration in (
        ("Parodi Fig. 7g direct exposure", "1"),
        ("Parodi Fig. 8 N9 kinetics positive arm", "100"),
        ("Althaus Fig. 2B cerebellum fitted EC50", "4.74"),
        ("Althaus Fig. 3B hippocampus fitted EC50", "7.92"),
    ):
        value = Decimal(concentration)
        yield label, "nominal bath relative to adult CSF", f"{value/csf_high:.2f}–{value/csf_low:.2f}", "fold", f"{concentration} µM nominal MMF"


def archive_rows(evidence):
    records = []
    for offset, digest in ARCHIVE_PAGES.items():
        path = evidence / f"S-BIAD1261-{offset:04d}.json"
        page = json.loads(checked_bytes(path, digest))
        if page["pagination"]["offset"] != offset:
            raise ValueError(f"Wrong page offset for {path}")
        records.extend(page["items"])
    if len(records) != 1980 or len({item["path"] for item in records}) != len(records):
        raise ValueError("Incomplete or duplicated BioStudies deposit inventory")

    extensions = Counter(Path(item["path"]).suffix.lower() for item in records)
    for extension, count in sorted(extensions.items()):
        yield "file type", extension, count, "files"
    yield "catalog total size", "all entries", sum(int(item["Size"]) for item in records), "bytes"

    groups = defaultdict(Counter)
    for item in records:
        key = (item["Tissue"], item["Treatment"], item["OGD"])
        groups[key][item["Concentration__in_μM_"]] += 1
    for (tissue, treatment, ogd), doses in sorted(groups.items()):
        group = f"{tissue} / {treatment} / OGD {ogd}"
        for dose, count in sorted(doses.items()):
            yield "catalog concentration " + dose, group, count, "files"


def write_table(path, header, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    write_table(args.out / "functional_comparison.tsv", ("source", "condition", "value", "unit", "locator"),
                functional_rows(args.evidence / "parodi-Fig7.jpg"))
    write_table(args.out / "ogd_archive_coverage.tsv", ("measure", "scope", "value", "unit"), archive_rows(args.evidence))


if __name__ == "__main__":
    main()
