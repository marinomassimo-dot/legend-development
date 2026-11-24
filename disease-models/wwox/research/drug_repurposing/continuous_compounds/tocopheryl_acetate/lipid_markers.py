"""Recalculate changes in parent-normalized serum lipids from Saito et al., Table 2."""
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

study = ET.parse(Path(sys.argv[1]))
assert study.findtext('.//article-id[@pub-id-type="pmid"]') == "26411970"
table, = (t for t in study.findall(".//table-wrap") if t.findtext("label") == "TABLE 2.")
rows = [["".join(cell.itertext()).strip() for cell in row] for row in table.findall(".//tr")]
assert rows[1][1:] == ["Before α-T", "α-T for 24M", "Withdrawal for 7M", "Control (n=6)"]
markers = {"EE-HODE", "7β-OHCh/Ch (μmol/mol)", "Linoleate (mM)", "Ch (mM)", "α-T (μM)", "γ-T (μM)"}
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(["marker", "before", "month24", "withdrawal_month7", "control_mean",
              "on_treatment_pct_change", "fraction_of_treatment_change_reversed"])
means = {}
for label, *values in rows[2:]:
    if label in markers:
        means[label] = [float(v.split()[0]) for v in values]
assert set(means) == markers

# Products of rounded means approximate concentration. Sample-level covariance is unavailable.
for label, numerator, parent in [
    ("EE-HODE approximate (nM)", "EE-HODE", "Linoleate (mM)"),
    ("7β-OHCh approximate (nM)", "7β-OHCh/Ch (μmol/mol)", "Ch (mM)"),
]:
    means[label] = [round(ratio * substrate, 3) for ratio, substrate in zip(means[numerator], means[parent])]

for label, (before, month24, withdrawal, control) in means.items():
    out.writerow([label, before, month24, withdrawal, control,
                  f"{100 * (month24 / before - 1):.2f}", f"{(withdrawal - month24) / (before - month24):.3f}"])
