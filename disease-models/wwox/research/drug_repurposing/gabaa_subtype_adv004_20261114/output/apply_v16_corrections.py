#!/usr/bin/env python3
"""Apply the V16 verifier corrections (ADV-004) to numbers.tsv; idempotent.

Run from this folder: python3 apply_v16_corrections.py. Changes are appended to CORRECTIONS.tsv.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "verify/verdicts.tsv item 1; verify/audit.md section 1"
FLAG = " | UNVERIFIED: the figure reading conflicts with Hammer's own text (clobazam alpha1 256 and NDMC alpha2 270 are 'slightly but significantly smaller' than diazepam, which requires diazepam alpha1 > 256 and alpha2 > 270); the blind verifier could not open the figure; do not carry"


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return
    p = os.path.join(HERE, "numbers.tsv")
    lines = open(p, encoding="utf-8").read().rstrip("\n").split("\n")
    head = lines[0].split("\t")
    ik, nk, ak = head.index("kind"), head.index("normalisation"), head.index("arithmetic")
    log = []
    for i, line in enumerate(lines[1:], 1):
        c = line.split("\t")
        rid = c[0]
        if rid in ("N072", "N073", "N074", "N075", "N076") and FLAG not in c[ik]:
            log.append(("numbers.tsv", rid, "kind", c[ik], c[ik] + FLAG[:60] + "...", "figure reading unverified and conflicting with the text", SRC))
            c[ik] += FLAG
        if rid == "N073" and "do not carry" not in c[ak]:
            log.append(("numbers.tsv", rid, "arithmetic", c[ak], c[ak] + " | do not carry (V16)", "derived from the conflicting readings", SRC))
            c[ak] += " | do not carry (V16)"
        if rid in ("N076", "N077") and "(so 256% = 2.56-fold of the EC20 response)" in c[nk]:
            new = c[nk].replace("(so 256% = 2.56-fold of the EC20 response)", "")
            log.append(("numbers.tsv", rid, "normalisation", c[nk][:100], new[:100], "copy-paste example from N072 removed", SRC))
            c[nk] = new
        lines[i] = "\t".join(c)
    open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    if log:
        cp = os.path.join(HERE, "CORRECTIONS.tsv")
        new = not os.path.exists(cp)
        with open(cp, "a", encoding="utf-8") as fh:
            if new:
                fh.write("file\trow_id\tfield\tbefore\tafter\treason\tsource\n")
            for r in log:
                fh.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    print(f"{len(log)} change(s)")


if __name__ == "__main__":
    main()
