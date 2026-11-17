#!/usr/bin/env python3
"""Generate the frozen briefs of the second target set from the briefs of target 3 (v1, baseline, S1, S2) with only the question and the outcome wording replaced.

    python3 make_briefs.py --target3 <engine_eval/target3 dir> --out <dir>

The only substitution allowed at run time is the path of the stage-1 output file (`<S1_FILE>`) and, for the corpus, the extraction folder (`<CUT>`): both are recorded in the run record. Nothing here is a result. Not medical advice."""
import argparse, hashlib, sys
from pathlib import Path

T = {
 "T4": ("In a developmental and epileptic encephalopathy or movement-disorder syndrome caused by variants in a gene encoding a heterotrimeric G-protein alpha subunit, in which the mutant subunit is dysfunctional rather than absent, propose 10 distinct levers that could restore the function of the mutant subunit. For each, name the single cell-type, signalling or small-molecule-class manipulation (genetic, or a class at mechanism level) whose outcome would discriminate it from its nearest rival, and say what it predicts for motor function AND for seizures.",
        "motor function and on seizures"),
 "T5": ("Missense variants in a gene encoding a GABA-A receptor subunit cause a developmental and epileptic encephalopathy through loss of the subunit protein at the cell surface. Propose 10 distinct levers that could restore the subunit's expression at the surface and the receptor's function. For each, name the single cell-type, signalling or small-molecule-class manipulation (genetic, or a class at mechanism level) whose outcome would discriminate it from its nearest rival, and say what it predicts for surface expression AND for GABA-evoked current.",
        "surface expression and on GABA-evoked current"),
 "T6": ("A bacteriophage resists several bacterial DNA-targeting immune systems (restriction-modification and CRISPR-Cas) without carrying a dedicated inhibitor of each. Propose 10 distinct mechanisms by which the phage could tolerate nuclease-induced double-strand breaks in its genome. For each, name the single genetic manipulation of the phage whose outcome would discriminate it from its nearest rival, and say what it predicts for phage survival under nuclease attack AND for the sequence of the repaired cleavage site.",
        "phage survival under nuclease attack and on the repaired cleavage site"),
}
OLDQ_START = 'QUESTION (answer it from what that folder holds, not from general recall alone): "'
def build(src: Path, out: Path):
    v1 = (src / "BRIEF_V1.txt").read_text(); bs = (src / "BRIEF_BASELINE.txt").read_text()
    s1 = (src / "BRIEF_V3_S1.txt").read_text(); s2 = (src / "BRIEF_V3_S2.txt").read_text()
    made = {}
    for tid, (q, outc) in T.items():
        def swap(text, prefix, endmark):
            a = text.index(prefix) + len(prefix); b = text.index(endmark, a)
            return text[:a] + q + text[b:]
        def wording(text):
            return text.replace("white-matter integrity and on cognitive behaviour", outc)
        def fix(text, kind):
            if kind in ("v1",):
                t = swap(text, OLDQ_START, '"\n\nWork like this')
            elif kind == "bs":
                t = swap(text, 'QUESTION: "', '"\n\nOUTPUT')
            elif kind == "s1":
                t = swap(text, 'QUESTION: "', '"\n\nOUTPUT').replace("propose 10 distinct", "propose 15 distinct").replace("Propose 10 distinct", "Propose 15 distinct")
            else:
                t = swap(text, 'QUESTION (answer it from what the folder holds and from the stage-1 list, not from general recall alone): "', '"\n\nINPUT')
            t = wording(t)
            return t.replace("/tmp/claude-1000/-home-desktop-legend-development/29e50812-fef0-4635-9c95-cfe7de2a8e2d/scratchpad/t3/S1_OUTPUT.txt", "<S1_FILE>").replace("/tmp/legend_cut_1867a26a8", "<CUT>")
        for name, text, kind in (("BRIEF_V1", v1, "v1"), ("BRIEF_BASELINE", bs, "bs"), ("BRIEF_V3_S1", s1, "s1"), ("BRIEF_V3_S2", s2, "s2")):
            t = fix(text, kind)
            # S1 and the baseline asked for 'propose 10/15 distinct mechanisms' in the old question text; the new question carries its own count, so the leftover phrase is removed
            fn = out / f"{tid}_{name}.txt"; fn.write_text(t); made[fn.name] = hashlib.sha256(t.encode()).hexdigest()
    return made

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--target3"); ap.add_argument("--out")
    a = ap.parse_args(argv[1:])
    if not (a.target3 and a.out):
        ap.print_help(); return 0
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    for k, v in build(Path(a.target3), out).items(): print(v[:16], k)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
