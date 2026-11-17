"""Axis coverage of past generator outputs against the seven axes of the v4 template (HE, 2026-11-17).

Reads, for each target folder of the second target set, `blind_input.md` and `blind_key.json` and the two stage-2
reports `S2_A.txt` and `S2_B.txt`, and prints (1) for each condition (baseline, v1, v3) the mean number of the seven
axes named by the ten final hypotheses of a run, (2) the share of each axis, (3) for v3 the number of final hypotheses
whose origin is a stage-1 item and the number built from the held circuits (ENGINE).
The axis test is a keyword match over the statement and the discriminating manipulation text: crude, noisy, and
fixed before reading the result. It uses no delegate and no network. Not a result about any lever; a count of words.

    python3 axis_coverage.py <second_target_set dir>
"""
import json, re, sys
from pathlib import Path

AXES = {
 "a_catalytic_cycle": r"cofactor|divalent|metal ion|\bzinc\b|magnesium|nucleotide|\bGTP|\bGDP|redox|\bpH\b|catalytic|hydrolysis|GTPase|\bion\b",
 "b_folding_stability": r"chaperone|folding|stabilis|stabiliz|osmolyte|proteostasis|temperature|misfold|\bHsp|\bHSP|ER stress|unfolded",
 "c_assembly_trafficking": r"traffick|export|surface expression|ER exit|localis|localiz|lipidation|palmitoyl|myristoyl|assembly|COPII|targeting|endocyt|membrane insertion|anchoring",
 "d_substrate_supply": r"supplement|metabolite|precursor|\bdiet|substrate supply|substrate availability|nutrient|ketogenic",
 "e_degradation": r"degradation|proteasome|ERAD|autophag|turnover|clearance|ubiquitin|half-life",
 "f_downstream_bypass": r"bypass|downstream|effector|paralog|parallel|compensat|substitut|alternative route|alternative pathway",
 "g_celltype_timing_dose": r"cell-type|cell type|interneuron|restricted|conditional|developmental window|timing|dosage|\bdose\b|Cre\b|early|adult|neuron-specific|astrocyte|glia",
}
def blocks(text):
    out = {}
    for b in text.split("## ")[1:]:
        zid = b[:3]; out[zid] = b[3:]
    return out
def main(root):
    root = Path(root); per = {}
    for tid in ("T4", "T5", "T6"):
        d = root / tid
        key = json.loads((d / "blind_key.json").read_text()); bl = blocks((d / "blind_input.md").read_text())
        runs = {}
        for z, label in key.items():
            arm, h = label.rsplit("-H", 1); runs.setdefault(arm, []).append(bl[z])
        per[tid] = runs
    cond = {"BASE": ("BASE_A", "BASE_B"), "V1": ("V1_A", "V1_B"), "V3": ("V3_A", "V3_B")}
    print("axis coverage per run (number of the 7 axes named by the 10 final hypotheses; keyword test)")
    print("target | baseline A/B | v1 A/B | v3 A/B")
    tot = {c: [] for c in cond}; share = {c: {a: 0 for a in AXES} for c in cond}; n_h = {c: 0 for c in cond}; zero = {c: 0 for c in cond}
    for tid, runs in per.items():
        cells = []
        for c, arms in cond.items():
            vals = []
            for arm in arms:
                hyps = runs[arm]; named = {a for a in AXES for t in hyps if re.search(AXES[a], t)}
                vals.append(len(named)); tot[c].append(len(named))
                for t in hyps:
                    n_h[c] += 1; hit = [a for a in AXES if re.search(AXES[a], t)]; zero[c] += (not hit)
                    for a in hit: share[c][a] += 1
            cells.append("/".join(map(str, vals)))
        print(tid, "|", " | ".join(cells))
    print("mean axes per run:", {c: round(sum(v) / len(v), 2) for c, v in tot.items()})
    print("share of hypotheses naming each axis (percent), then hypotheses naming no axis:")
    for c in cond:
        print(c, {a[0]: round(100 * share[c][a] / n_h[c]) for a in AXES}, "no axis:", zero[c], "of", n_h[c])
    print("v3 final tens: origin of each hypothesis (stage-1 item versus built from the held circuits)")
    for tid in ("T4", "T5", "T6"):
        row = []
        for r in ("A", "B"):
            t = (root / tid / f"S2_{r}.txt").read_text()
            t = t.split("FINAL TEN", 1)[-1] if "FINAL TEN" in t else t
            o = re.findall(r"Origin[:\s]*(S1-\d+|ENGINE)", t); row.append((sum(x.startswith("S1") for x in o), sum(x == "ENGINE" for x in o)))
        print(tid, "run A (S1, ENGINE) =", row[0], "run B =", row[1])
if __name__ == "__main__":
    if len(sys.argv) != 2: print(__doc__); sys.exit(0)
    main(sys.argv[1])
