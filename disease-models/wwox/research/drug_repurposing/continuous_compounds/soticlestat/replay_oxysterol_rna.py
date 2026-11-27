"""Replay the initial WWOX oxysterol-pathway expression comparison."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "clemizole"))
from replay_receptors_and_exposure import bulk_panel, formatted, verified_expression

PANEL = ("Cyp46a1", "Ch25h", "Cyp27a1", "Sqle", "Abca1")


def main(files):
    verified_expression(files)
    print(
        "model\taccession\tgene\tctrl_n\tko_n\tctrl_positive\tko_positive\t"
        "ctrl_mean\tko_mean\tlog2_delta\tomit_min\tomit_max\tmapping"
    )
    for row in formatted(bulk_panel(files, PANEL)):
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, help="Shared checkout's files directory")
    main(parser.parse_args().files)
