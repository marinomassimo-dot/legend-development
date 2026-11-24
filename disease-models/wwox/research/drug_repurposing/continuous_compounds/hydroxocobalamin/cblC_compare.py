"""Count paired cblC biochemical responses per child against diagnosis and local intervals."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from openpyxl import load_workbook

folder = Path(sys.argv[1]) / "deepening_downloads/hydroxocobalamin_loop_20261124"
table = ET.parse(folder / "selvanathan.xml").find(".//table-wrap")
baseline = {}
for row in table.findall(".//tr"):
    cells = ["".join(el.itertext()).strip() for el in row]
    if cells[0].startswith(("Plasma MMA (", "Plasma total homocysteine (")):
        baseline[cells[0].split()[1]] = [float(v) for v in cells[1:]]
book = load_workbook(folder / "selvanathan_s1.xlsx", read_only=True, data_only=True)
records = {"last": [], "first_180_to_365_days": []}
for index in range(9):
    sheet = book[f"Patient {index + 1}"]
    rows = list(sheet.values)
    age, mma, hcy = [rows[0].index(key) for key in ("Age (days)", "MMA", "THcy")]
    paired = sorted((r[age], r[mma], r[hcy]) for r in rows[1:] if all(isinstance(r[j], (int, float)) for j in (age, mma, hcy)))
    assert paired and len({day for day, _, _ in paired}) == len(paired)
    early = [r for r in paired if 180 <= r[0] <= 365]
    for key, visit in (("last", paired[-1]), ("first_180_to_365_days", early[0] if early else None)):
        if visit:
            day, m, h = visit
            records[key].append((day, m < baseline["MMA"][index] and h < baseline["total"][index], m < 1.57 and 3.3 <= h <= 19.2))
print("visit\tchildren_with_paired_data\tmin_day\tmax_day\tboth_lower_than_diagnosis\tboth_in_reference")
for key, data in records.items():
    days, decrease, normal = zip(*data)
    print(key, len(data), min(days), max(days), sum(decrease), sum(normal), sep="\t")
