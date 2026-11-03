#!/usr/bin/env python3
"""IT21 P6 control for lincs_kd_probe.py: is the WWOX-knockdown signature in NPC more similar to WWOX knockdowns in
other cell lines than to knockdowns of OTHER genes in the same NPC context? If not, the cross-cell similarity seen in
the probe is a shared shRNA/cell-state axis and not a WWOX-specific effect.

Stdlib only; free key-less iLINCS (CC BY). Takes the first N other-gene NPC LIB_6 signatures (sorted by signature id,
no choice by outcome). Prints rho of WWOX-NPC against each, and of WWOX-NPC against the 9 WWOX signatures in other
cell lines (re-computed here so both sets are in one output).

    python3 lincs_kd_control.py --help
    python3 lincs_kd_control.py [--n 40]
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

import lincs_kd_probe as P  # same directory; run from this directory


def meta(where, limit):
    flt = json.dumps({"where": where, "limit": limit})
    req = urllib.request.Request(P.META + "?filter=" + urllib.parse.quote(flt), headers=P.UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=40)
    a = ap.parse_args()
    wnpc = [m for m in meta({"compound": "WWOX", "libraryid": "LIB_6"}, 50) if m["cellline"] == "NPC"][0]
    base = P.download(wnpc["signatureid"])
    others = sorted((m for m in meta({"cellline": "NPC", "libraryid": "LIB_6"}, 2000) if m["compound"] != "WWOX"),
                    key=lambda m: m["signatureid"])
    print(f"NPC LIB_6 other-gene signatures available: {len(others)}; using first {a.n}")
    ctl = []
    for m in others[:a.n]:
        d = P.download(m["signatureid"])
        sh = sorted(set(base) & set(d))
        ctl.append(P.spearman([base[g][0] for g in sh], [d[g][0] for g in sh]))
    wcell = []
    for m in meta({"compound": "WWOX", "libraryid": "LIB_6"}, 50):
        if m["cellline"] == "NPC":
            continue
        d = P.download(m["signatureid"])
        sh = sorted(set(base) & set(d))
        wcell.append(P.spearman([base[g][0] for g in sh], [d[g][0] for g in sh]))
    ctl.sort(); wcell.sort()
    q = lambda v, p: v[min(len(v) - 1, int(p * len(v)))]
    print(f"CONTROL NPC other genes n={len(ctl)}: min {ctl[0]:.3f} p25 {q(ctl,.25):.3f} median {q(ctl,.5):.3f} p75 {q(ctl,.75):.3f} max {ctl[-1]:.3f}")
    print(f"WWOX NPC vs WWOX other cells n={len(wcell)}: min {wcell[0]:.3f} median {q(wcell,.5):.3f} max {wcell[-1]:.3f}")
    print("WWOX-cell values above the control median:", sum(1 for x in wcell if x > q(ctl, .5)), "of", len(wcell))
    print("WWOX-cell values above the control maximum:", sum(1 for x in wcell if x > ctl[-1]), "of", len(wcell))


if __name__ == "__main__":
    sys.exit(main())
