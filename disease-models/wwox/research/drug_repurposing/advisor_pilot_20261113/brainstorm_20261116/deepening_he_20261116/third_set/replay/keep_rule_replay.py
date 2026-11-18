"""Axis-diverse keep-rule replay over held stage-1 lists (HE, 2026-11-17). No delegate, no network.

    python3 keep_rule_replay.py <third_set dir>   (reads T7/ and T9/ V3_S1_A, V3_S1_B, V4_S1_A, V4_S1_B and the final tens in blind_input.md with blind_key.json)
The rule and the flags are fixed in EXPECTATION_REPLAY.md before this script is run.
"""
import json, re, sys
from pathlib import Path
AXES = {
 "a": r"cofactor|divalent|metal ion|\bzinc\b|magnesium|nucleotide|\bGTP|\bGDP|redox|\bpH\b|catalytic|hydrolysis|GTPase|\bion\b",
 "b": r"chaperone|folding|stabilis|stabiliz|osmolyte|proteostasis|temperature|misfold|\bHsp|\bHSP|ER stress|unfolded",
 "c": r"traffick|export|surface expression|ER exit|localis|localiz|lipidation|palmitoyl|myristoyl|assembly|COPII|targeting|endocyt|membrane insertion|anchoring",
 "d": r"supplement|metabolite|precursor|\bdiet|substrate supply|substrate availability|nutrient|ketogenic",
 "e": r"degradation|proteasome|ERAD|autophag|turnover|clearance|ubiquitin|half-life",
 "f": r"bypass|downstream|effector|paralog|parallel|compensat|substitut|alternative route|alternative pathway",
 "g": r"cell-type|cell type|interneuron|restricted|conditional|developmental window|timing|dosage|\bdose\b|Cre\b|early|adult|neuron-specific|astrocyte|glia",
}
RARITY = ["d", "a", "f", "c", "b", "e", "g"]
METAL = r"Mn2\+|Mg2\+|divalent|\bmetal|\bzinc\b"
SYNTH = r"(synthesis|tyrosine hydroxylase)"
LOWER = r"(lower|reduc|cut|inhibit|haploinsufficien|heterozygous|dosage|deletion)"
REL = r"amphetamine|releaser|stimulant"
def parse(path, v4):
    t = Path(path).read_text()
    if v4: t = t.split("H1.", 1)[1]; t = "H1." + t
    parts = re.split(r"(?m)^\s*\**H(\d+)\.\s", t)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
def keep(hyps):
    assign = {}
    for n, tx in hyps.items():
        hit = [a for a in RARITY if re.search(AXES[a], tx)]
        assign[n] = hit[0] if hit else None
    chosen = []
    for a in RARITY:
        for n in sorted(hyps):
            if assign[n] == a: chosen.append(n); break
    for n in sorted(hyps):
        if len(chosen) >= 10: break
        if n not in chosen: chosen.append(n)
    return chosen[:10], assign
def main(root):
    root = Path(root)
    for tgt in ("T7", "T9"):
        for arm, v4 in (("V3_S1_A", 0), ("V3_S1_B", 0), ("V4_S1_A", 1), ("V4_S1_B", 1)):
            hy = parse(root / tgt / f"{arm}.txt", v4)
            ten, asg = keep(hy)
            flags = lambda n: {"metal": bool(re.search(METAL, hy[n], re.I)), "synth": bool(re.search(SYNTH, hy[n], re.I) and re.search(LOWER, hy[n], re.I)), "rel": bool(re.search(REL, hy[n], re.I))}
            allm = [n for n in hy if flags(n)["metal"]]; alls = [n for n in hy if flags(n)["synth"]]; allr = [n for n in hy if flags(n)["rel"]]
            print(tgt, arm, "| 15 list: metal", allm, "synth", alls, "rel", allr, "| rule-R ten", ten, "| metal in ten", [n for n in allm if n in ten], "synth in ten", [n for n in alls if n in ten], "rel in ten", [n for n in allr if n in ten])
if __name__ == "__main__":
    if len(sys.argv) != 2: print(__doc__); sys.exit(0)
    main(sys.argv[1])
