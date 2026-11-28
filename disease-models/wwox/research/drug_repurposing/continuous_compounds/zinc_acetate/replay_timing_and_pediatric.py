"""Replay descriptive cortical contrasts and exact pediatric sensitivity analyses."""

import argparse
from csv import writer
from hashlib import sha256
from html import unescape
from math import comb
from pathlib import Path
import re
import sys
from xml.etree import ElementTree


MORABITO_SHA256 = "dfeab4f229ff7e8879ffd0b6211448b1cb73c160fa60d77c2feffe7ffcc7d581"


def read_cortical_values(path):
    data = path.read_bytes()
    if sha256(data).hexdigest() != MORABITO_SHA256:
        raise ValueError("Expected the versioned Morabito publisher JATS.")
    article = ElementTree.fromstring(data)
    paragraphs = [" ".join("".join(p.itertext()).split()) for p in article.findall("./body//p")]
    pairs = next(p for p in paragraphs if p.startswith("L2/3 PNs receive inputs"))
    sst_caption = next(p for p in paragraphs if p.startswith("(I) Summary plot") and "SST" in p)
    charge = re.findall(r"median\s*[:=]\s*(\d+\.\d+) pC", pairs)
    added_zinc = re.findall(r"(?:ctrl|ZnCl2): (\d+\.\d+)", sst_caption)
    total_control, total_chelator, first_control, first_chelator = map(float, charge)
    sst_first_control, sst_first_zinc, sst_total_control, sst_total_zinc = map(float, added_zinc)
    return [
        ("L2/3 pyramidal to pyramidal, chelation", "first median NMDA charge, pC", "Fig. 1G", 8, first_control, first_chelator),
        ("L2/3 pyramidal to pyramidal, chelation", "total median NMDA charge, pC", "Fig. 1G", 8, total_control, total_chelator),
        ("L2/3 pyramidal to SST, added zinc", "first median NMDA charge, pC", "Fig. 2I", 12, sst_first_control, sst_first_zinc),
        ("L2/3 pyramidal to SST, added zinc", "total median NMDA charge, pC", "Fig. 2I", 12, sst_total_control, sst_total_zinc),
    ]


def read_trial_counts(path):
    page = path.read_text(encoding="utf-8")
    table = page.split('id="tIII-181-185"', 1)[1].split("</table>", 1)[0]
    rows = []
    for row in re.findall(r"<tr>(.*?)</tr>", table, re.DOTALL):
        cells = re.findall(r"<td\b[^>]*>(.*?)</td>", row, re.DOTALL)
        if len(cells) == 4:
            cells = [unescape(re.sub(r"<[^>]+>", "", cell)).strip() for cell in cells]
            rows.append((cells[0], int(cells[1].split()[0]), int(cells[2].split()[0])))
    labels = [label for label, _, _ in rows]
    if len(labels) != 5 or labels[0] != "100%" or "≥50%" not in labels[1] or labels[-1] != "Total":
        raise ValueError(f"Unexpected Saad Table III endpoint labels: {labels}")
    counts = [(treated, placebo) for _, treated, placebo in rows]
    total = counts[-1]
    if tuple(map(sum, zip(*counts[:-1]))) != total:
        raise ValueError("Saad Table III outcome counts do not sum to the stated total.")
    return counts[0], counts[1], total


def fisher_two_sided(events, group_size):
    treated, placebo = events
    n_treated, n_placebo = group_size
    responders = treated + placebo
    observed = comb(n_treated, treated) * comb(n_placebo, placebo)
    possible_treated_counts = range(max(0, responders - n_placebo), min(responders, n_treated) + 1)
    joint_weights = (comb(n_treated, a) * comb(n_placebo, responders - a) for a in possible_treated_counts)
    return sum(weight for weight in joint_weights if weight <= observed) / comb(n_treated + n_placebo, responders)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("morabito_jats", type=Path)
    parser.add_argument("saad_pmc_html", type=Path)
    args = parser.parse_args()
    output = writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(("study", "comparison", "endpoint", "locator", "control", "comparison_value",
                     "effect", "effect_unit", "two_sided_fisher_p", "replication"))
    for comparison, endpoint, locator, pairs, control, zinc in read_cortical_values(args.morabito_jats):
        relative_change = (zinc / control - 1) * 100
        output.writerow(("Morabito", comparison, endpoint, locator, control, zinc, f"{relative_change:.3f}",
                         "% change of published marginal summaries", "", f"{pairs} pairs"))
    free, partial, total = read_trial_counts(args.saad_pmc_html)
    treated, placebo = (a + b for a, b in zip(free, partial))
    scenarios = (
        ("Published", "≥50% seizure reduction", (treated, placebo)),
        ("Sensitivity, one fewer zinc responder", "≥50% seizure reduction", (treated - 1, placebo)),
        ("Sensitivity, one more placebo responder", "≥50% seizure reduction", (treated, placebo + 1)),
        ("Published", "Seizure freedom", free),
    )
    for comparison, endpoint, events in scenarios:
        effect = 100 * (events[0] / total[0] - events[1] / total[1])
        output.writerow(("Saad", comparison, endpoint, "Table III", f"{events[1]}/{total[1]}",
                         f"{events[0]}/{total[0]}", f"{effect:.3f}", "percentage points",
                         f"{fisher_two_sided(events, total):.6f}", f"{sum(total)} children"))


if __name__ == "__main__":
    main()
