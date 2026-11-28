"""Screen the two positive ion masses of an unresolved hexitol formula."""
import argparse
from pathlib import Path
import sys


IONS = {"protonated": 182.07903817 + 1.007276466621,
        "sodiated": 182.07903817 + 22.989220702}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("compounds", type=Path)
    parser.add_argument("spectra", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(exist_ok=True, parents=True)

    sys.path.insert(0, str(args.compounds / "l_ornithine"))
    import replay_fly_mass

    original_argv = sys.argv[:]
    try:
        for ion, mass in IONS.items():
            replay_fly_mass.MASS = mass
            sys.argv = [original_argv[0], str(args.compounds / "l_leucine"),
                        str(args.spectra), str(args.output / ion)]
            print(ion, flush=True)
            replay_fly_mass.main()
    finally:
        sys.argv = original_argv


if __name__ == "__main__":
    main()
