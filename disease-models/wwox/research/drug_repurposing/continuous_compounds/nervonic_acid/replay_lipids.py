"""Replay selected chain-length and delivery comparisons from public source files."""
import argparse
import hashlib
from pathlib import Path
from statistics import mean
import sys
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parents[6] / "framework" / "scripts"))
from xlsx_to_text import read_workbook


SUN_SHA = "0b293bfb43ceedf6b0c4c477adfb1d8722663fe0b96b41c56ac6d0ec72ba5533"
WU_DATA_SHA = "c075e9b09e53fe6a03d63f3a36dc218ab4370f0bcb6f1d79522fa562fe30bcd6"
WU_SOURCE_SHA = "19b82c155785d64088f347213aff905a2dc26451cc5eacd7050cfb367fcc0095"
FISH_SHA = "f4299f88e5af7cb76c02eb28219e9524fad8f53bc4b6d3f6d3e25f3a576818d6"


def verify(path, expected):
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f"Source digest differs for {path}")


def sheet(path, name, digest):
    verify(path, digest)
    sections = read_workbook(path).split("\n## sheet ")
    match, = (section for section in sections if section.startswith(repr(name) + " "))
    return [line.split("\t") for line in match.splitlines()[1:]]


def ratio(control, case, unit, label, endpoint):
    """Range across single omissions within either arm, without pairing animals."""
    central = mean(case) / mean(control)
    omissions = [mean(case[:i] + case[i+1:]) / mean(control) for i in range(len(case))]
    omissions += [mean(case) / mean(control[:i] + control[i+1:]) for i in range(len(control))]
    return [label, endpoint, unit, len(control), len(case), mean(control), mean(case),
            central, min(omissions), max(omissions)]


def sun(path):
    rows = sheet(path, "20210526 mouse brain NP", SUN_SHA)
    assert rows[1][1:] == [*(f"WT{i}" for i in range(1, 8)), *(f"CKO{i}" for i in range(1, 6))]
    species = {row[0]: row[1:] for row in rows[2:] if row}
    for acyl in ("16:0", "18:0", "24:0", "24:1"):
        feature = f"GalCer d18:1/{acyl}"
        values = [float(v) for v in species[feature]]
        yield ratio(values[:7], values[7:], "umol/g", "Sun_Cers2_nestin_cKO", feature)
    per_mouse = [float(a) / float(b) for a, b in zip(species["GalCer d18:1/24:1"],
                                                       species["GalCer d18:1/24:0"])]
    yield ratio(per_mouse[:7], per_mouse[7:], "ratio", "Sun_Cers2_nestin_cKO", "GalCer 24:1/24:0")


def wu_lipids(path):
    rows = sheet(path, "mole %", WU_DATA_SHA)
    _, *annotations, first_sample = rows[0][:7]
    assert annotations == ["category", "class", "totallength", "totaldb", "totaloh"]
    assert first_sample == "cre1"
    values = {row[0]: [float(v) for v in row[6:]]
              for row in rows[1:] if len(row) == 22 and row[2] == "HexCer" and row[0]}
    for age, block, offset in (("P14", 0, 0), ("P28", 8, 4)):
        control = list(range(block, block+4))
        case = list(range(block+4, block+8))
        assert [rows[0][6+i] for i in control] == [f"cre{i+1}" for i in range(offset, offset+4)]
        assert [rows[0][6+i] for i in case] == [f"cko{i+1}" for i in range(offset, offset+4)]
        all_hexcer = [sum(v[i] for v in values.values()) for i in range(16)]
        for feature in ("HexCer 36:1;2", "HexCer 42:1;2", "HexCer 42:2;2",
                        "HexCer 42:2;3", "Total HexCer"):
            x = all_hexcer if feature == "Total HexCer" else values[feature]
            yield ratio([x[i] for i in control], [x[i] for i in case],
                        "mol_percent_total_lipids", f"Wu_Gltp_cKO_{age}", feature)


def wu_delivery(path):
    rows = sheet(path, "Fig6h", WU_SOURCE_SHA)
    assert rows[0] == ["WT", "cKO"]
    ctrl = [float(row[0]) for row in rows[1:] if row[0]]
    case = [float(row[1]) for row in rows[1:] if len(row) > 1 and row[1]]
    assert (len(ctrl), len(case)) == (286, 265)
    # This is a descriptive cell-level average from 3 mice per group. No per-mouse
    # assignment is in the workbook, so no omission interval or new p-value.
    return ["Wu_Gltp_cKO_cells", "external/intracellular GalCer", "ratio", len(ctrl), len(case),
            mean(ctrl), mean(case), mean(case)/mean(ctrl), "NA", "NA"]


def fish_oil(path):
    verify(path, FISH_SHA)
    doc = ElementTree.parse(path).getroot()
    table, = (t for t in doc.iter("table-wrap") if t.findtext("label") == "Table 2")
    row, = (r for r in table.findall(".//tbody/tr") if "C24:1n9" in "".join(r.itertext()))
    cells = ["".join(td.itertext()).split()[0] for td in row]
    for i, hours in enumerate((24, 48, 72)):
        ctrl = float(cells[5+i])
        case = cells[8+i]
        fold = float(case)/ctrl if case != "n.d." else "NA"
        yield [f"Lewkowicz_FOM_{hours}h", "C24:1n9",
               "percent_of_lipids", 4, 4, ctrl, case, fold, "NA", "NA"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("sun_workbook", "wu_dataset", "wu_source_data", "lewkowicz_jats"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    print("comparison\tendpoint\tunit\tcontrol_n\tcase_n\tcontrol_mean\tcase_mean\tcase_over_control\tomit_min\tomit_max")
    for row in [*sun(args.sun_workbook), *wu_lipids(args.wu_dataset), wu_delivery(args.wu_source_data),
                *fish_oil(args.lewkowicz_jats)]:
        print("\t".join(f"{v:.8g}" if isinstance(v, float) else str(v) for v in row))
