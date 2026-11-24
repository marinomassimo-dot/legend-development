"""Paired visual responses following ketone ester in the Steinwurzel et al. open deposit."""
import csv
import hashlib
from itertools import product
from pathlib import Path
import sys
import numpy as np


def read_deposit(directory, filename, checksum):
    path = directory / filename
    assert hashlib.md5(path.read_bytes()).hexdigest() == checksum
    with path.open(encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))
    by_id = {r["subjs"]: r for r in rows}
    assert len(rows) == len(by_id) == 10
    return by_id


def main(directory, output):
    eeg = read_deposit(directory, "3_EEG_SteadyStateVisualEvokedPotentials.csv",
                       "b2c129b7a69ba97ed18414176dc23f09")
    ids = sorted(eeg)
    stimuli = ["single_grating", "single_grating_plus_orthogonal_mask"]
    diffs, log_folds = [], []
    for stimulus in stimuli:
        pre, post = [np.array([float(eeg[i][stimulus + "_" + t]) for i in ids]) for t in ("pre", "post")]
        assert np.all(pre > 0) and np.all(post > 0)
        diffs.append(post - pre)
        log_folds.append(np.log(post / pre))
    rows = []
    signs = np.array(list(product([-1, 1], repeat=len(ids))))
    for label, unit, changes in [
        ("single", "native_amplitude", diffs[0]), ("masked", "native_amplitude", diffs[1]),
        ("single_minus_masked", "native_amplitude", diffs[0] - diffs[1]),
        ("single", "ln_fold", log_folds[0]), ("masked", "ln_fold", log_folds[1]),
        ("single_minus_masked", "ln_fold", log_folds[0] - log_folds[1])
    ]:
        avg = changes.mean()
        omissions = [np.delete(changes, i).mean() for i in range(len(changes))]
        null = (signs * changes).mean(axis=1)
        p = np.mean(np.abs(null) >= abs(avg) - 1e-12)
        paired_f = (avg / (changes.std(ddof=1) / np.sqrt(len(changes)))) ** 2
        rows.append([label, unit, len(changes), int(sum(changes > 0)), avg, min(omissions),
                     max(omissions), p, paired_f, np.exp(avg) if unit == "ln_fold" else "NA"])
    with output.open("w", newline="") as file:
        writer = csv.writer(file, delimiter="\t", lineterminator="\n")
        writer.writerow("contrast scale n positive mean omit_min omit_max sign_flip_p t_squared geometric_ratio".split())
        writer.writerows(rows)


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
