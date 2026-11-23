"""Partial identification of unreported high Allo-S outcomes in NCT03865732."""
import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

TOLERANCE = 0.006


def weights(indices, q, definition, n):
    size = len(indices)
    if q == 0.5:
        definition = "type2"  # Preserve the ordinary sample median in every sensitivity analysis.
    if definition in {"type1", "type2", "type3"}:
        pos = size * q
        if definition == "type2" and pos.is_integer():
            i, j, weight = int(pos) - 1, int(pos), 0.5
        else:
            rank = round(pos) if definition == "type3" else math.ceil(pos)
            i = j = max(0, min(size - 1, rank - 1))
            weight = 0
    else:
        offset = {"type4": 0, "type5": 0.5, "type6": q, "type7": 1 - q,
                  "type8": (q + 1) / 3, "type9": q / 4 + 3 / 8}[definition]
        pos = max(0, min(size - 1, size * q + offset - 1))
        i, j, weight = math.floor(pos), math.ceil(pos), pos % 1
    result = np.zeros(n)
    result[indices[i]] += 1 - weight
    result[indices[j]] += weight
    return result


def arm_bounds(n, low_n, responders, total_summary, low_summary, convention):
    all_indices = tuple(range(n))
    monotone = np.eye(n)[:-1] - np.eye(n)[1:]
    bounds = [(-100, -50)] * responders + [(-50 + 0.00001, None)] * (n - responders)
    admissible = []
    for low in itertools.combinations(all_indices, low_n):
        high = tuple(i for i in all_indices if i not in low)
        matrix = list(monotone)
        limits = [0] * len(monotone)
        for indices, values in ((all_indices, total_summary), (low, low_summary)):
            for q, value in zip([0.25, 0.50, 0.75], values):
                if convention == "medians" and q != 0.50:
                    continue
                row = weights(indices, q, convention, n)
                matrix.extend((row, -row))
                limits.extend((value + TOLERANCE, -value + TOLERANCE))
        objective = weights(high, 0.5, convention, n)
        lower = linprog(objective, A_ub=matrix, b_ub=limits, bounds=bounds)
        if lower.status == 2:
            continue
        if not lower.success:
            raise RuntimeError(lower.message)
        upper = linprog(-objective, A_ub=matrix, b_ub=limits, bounds=bounds)
        if not upper.success and upper.status != 3:
            raise RuntimeError(upper.message)
        low_r = sum(i < responders for i in low)
        rate_difference = low_r / low_n - (responders - low_r) / (n - low_n)
        admissible.append((lower.fun, -upper.fun if upper.success else math.inf,
                           low_r, rate_difference))
    return admissible


def read_arms(source):
    measures = json.loads(source.read_text())["resultsSection"]["outcomeMeasuresModule"]["outcomeMeasures"]
    total, low, count = measures[:3]
    assert "Biomarker-positive" in low["title"] and "50%" in count["title"]
    arms = {}
    for group in total["groups"]:
        gid = group["id"]
        def value(measure, key="value"):
            row = next(r for r in measure["classes"][0]["categories"][0]["measurements"]
                       if r["groupId"] == gid)
            return float(row[key])
        def size(measure):
            return int(next(r["value"] for r in measure["denoms"][0]["counts"] if r["groupId"] == gid))
        def quartiles(measure):
            return tuple(value(measure, key) for key in ("lowerLimit", "value", "upperLimit"))
        arms[group["title"]] = size(total), size(low), int(value(count)), quartiles(total), quartiles(low)
    return arms


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry_json", type=Path)
    arms = read_arms(parser.parse_args().registry_json)
    print("convention\tarm\tallocations\thigh_median_min\thigh_median_max\tlow_responders")
    for convention in ("type2", "type7", "type6", "medians",
                       "type1", "type3", "type4", "type5", "type8", "type9"):
        results = {}
        for arm, params in arms.items():
            rows = arm_bounds(*params, convention)
            results[arm] = rows
            if rows:
                counts = ",".join(str(k) for k in sorted({r[2] for r in rows}))
                print(f"{convention}\t{arm}\t{len(rows)}\t{min(r[0] for r in rows):.3f}"
                      f"\t{max(r[1] for r in rows):.3f}\t{counts}")
            else:
                print(f"{convention}\t{arm}\t0\tNA\tNA\tNA")
        g, p = results["Ganaxolone"], results["Placebo"]
        if g and p:
            lo, hi = min(r[0] for r in g) - max(r[1] for r in p), max(r[1] for r in g) - min(r[0] for r in p)
            rd = [100 * (x - y) for x in {r[3] for r in g} for y in {r[3] for r in p}]
            print(f"# {convention}: high median drug-minus-placebo [{lo:.2f}, {hi:.2f}] points;"
                  f" low-minus-high responder-rate interaction [{min(rd):.2f}, {max(rd):.2f}] pp")


if __name__ == "__main__":
    main()
