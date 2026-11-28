#!/usr/bin/env python3
"""ADV-301: write verdicts.tsv = flags.tsv plus HE's hand verdict and the passage that decides it."""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
YU = "Yu Fig. 3: n=10, seizures per 8 h, 3 days per phase; means recomputed from figure3d_by_mouse.tsv"
V = {  # (brief, sentence, item) -> (verdict, basis)
    ("huperzine-a", "evidence.0.0", "53.5"): ("FALSE", YU),
    ("huperzine-a", "evidence.0.0", "98.8"): ("FALSE", YU),
    ("huperzine-a", "evidence.0.0", "119.0"): ("FALSE", YU),
    ("huperzine-a", "evidence.0.1", "every"): ("FALSE", "all 10 rows of figure3d_by_mouse.tsv: during total below pre total"),
    ("huperzine-a", "inference.0.2", "no/not"): ("FALSE", "refers to the RNA sentences; true by construction"),
    ("huperzine-a", "hypothesis.0.0", "only"): ("FALSE", "condition of the proposed mechanism, not a statement on a source"),
    ("huperzine-a", "limits.0.1", "no/not"): ("FALSE", "Fig. 3 is one cohort, paired Pre/drug/Post; article supplement not held"),
    ("bexarotene", "evidence.0.1", "every"): ("FALSE", "treated_contrasts.tsv: gates 2 and 3, both cell classes, omit_min/omit_max keep sign"),
    ("bexarotene", "limits.0.2", "all"): ("FALSE", "Brown: 'All 26 (100%) bexarotene-treated participants developed central hypothyroidism'"),
    ("etifoxine", "evidence.0.2", "no/not"): ("FALSE", "Sirimontakan Table 5.2: efficacy 13.7% (-1.1 to 26.4); the interval includes zero"),
    ("etifoxine", "hypothesis.0.0", "only"): ("FALSE", "condition of the proposed mechanism"),
    ("verapamil", "evidence.0.0", "25 %"): ("FALSE", "recomputed from figure_points.tsv and axis calibration: 151.9/121.1 = 1.255"),
    ("verapamil", "evidence.0.0", "15 %"): ("FALSE", "recomputed: 190.1/165.3 = 1.150"),
    ("verapamil", "evidence.0.1", "no/not"): ("FALSE", "Elkhayat abstract (full text not held): 'no significant differences'"),
    ("verapamil", "hypothesis.0.1", "no/not"): ("FALSE", "true by construction (baseline RNA is not a transport measure)"),
}


def main():
    rows = [line.split("\t") for line in (HERE / "flags.tsv").read_text(encoding="utf-8").splitlines()[1:]]
    flags = [r for r in rows if r[2] != "scanned"]
    assert len(flags) == len(V)
    with (HERE / "verdicts.tsv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["brief", "sentence", "class", "item", "verdict", "basis"])
        for brief, sid, cls, item, _ in flags:
            w.writerow([brief, sid, cls, item, *V[(brief, sid, item)]])


if __name__ == "__main__":
    main()
