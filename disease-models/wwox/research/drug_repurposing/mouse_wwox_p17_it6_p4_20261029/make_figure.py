#!/usr/bin/env python3
"""Fig 1: centred mean log2 ratio of each pre-declared set per contrast against its matched null (grey band = 2.5th to 97.5th percentile).
Pure numpy + zlib (no matplotlib in this deployment). Usage: python3 -I make_figure.py results/set_summary.tsv fig1_sets_vs_matched_null.png"""
import sys, csv, zlib, struct
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__); sys.exit(0)
import numpy as np
src, dst = sys.argv[1:3]
G = """A:01110,10001,10001,11111,10001,10001,10001|B:11110,10001,10001,11110,10001,10001,11110|C:01110,10001,10000,10000,10000,10001,01110|D:11110,10001,10001,10001,10001,10001,11110|E:11111,10000,10000,11110,10000,10000,11111|F:11111,10000,10000,11110,10000,10000,10000|G:01110,10001,10000,10111,10001,10001,01111|H:10001,10001,10001,11111,10001,10001,10001|I:01110,00100,00100,00100,00100,00100,01110|J:00111,00010,00010,00010,00010,10010,01100|K:10001,10010,10100,11000,10100,10010,10001|L:10000,10000,10000,10000,10000,10000,11111|M:10001,11011,10101,10101,10001,10001,10001|N:10001,11001,10101,10011,10001,10001,10001|O:01110,10001,10001,10001,10001,10001,01110|P:11110,10001,10001,11110,10000,10000,10000|Q:01110,10001,10001,10001,10101,10010,01101|R:11110,10001,10001,11110,10100,10010,10001|S:01111,10000,10000,01110,00001,00001,11110|T:11111,00100,00100,00100,00100,00100,00100|U:10001,10001,10001,10001,10001,10001,01110|V:10001,10001,10001,10001,10001,01010,00100|W:10001,10001,10001,10101,10101,11011,10001|X:10001,10001,01010,00100,01010,10001,10001|Y:10001,10001,01010,00100,00100,00100,00100|Z:11111,00001,00010,00100,01000,10000,11111|0:01110,10001,10011,10101,11001,10001,01110|1:00100,01100,00100,00100,00100,00100,01110|2:01110,10001,00001,00010,00100,01000,11111|3:11110,00001,00001,01110,00001,00001,11110|4:00010,00110,01010,10010,11111,00010,00010|5:11111,10000,11110,00001,00001,10001,01110|6:00110,01000,10000,11110,10001,10001,01110|7:11111,00001,00010,00100,01000,01000,01000|8:01110,10001,10001,01110,10001,10001,01110|9:01110,10001,10001,01111,00001,00010,01100|_:00000,00000,00000,00000,00000,00000,11111|-:00000,00000,00000,01110,00000,00000,00000|+:00000,00100,00100,11111,00100,00100,00000|.:00000,00000,00000,00000,00000,01100,01100|::00000,01100,01100,00000,01100,01100,00000|*:00000,10101,01110,11111,01110,10101,00000|(:00010,00100,01000,01000,01000,00100,00010|):01000,00100,00010,00010,00010,00100,01000|/:00001,00001,00010,00100,01000,10000,10000| :00000,00000,00000,00000,00000,00000,00000|=:00000,00000,11111,00000,11111,00000,00000"""
FONT = {}
for g in G.split("|"):
    k, rows = g.split(":", 1) if g[0] != ":" else (":", g[2:])
    FONT[k] = rows.split(",")
rows = list(csv.DictReader(open(src), delimiter="\t"))
SETS = ["ISR_targets", "ISR_core5", "UPR_branches", "Mito_translation", "Mito_import", "OXPHOS_nuclear", "Glycolysis_lactate", "Glycolysis_19",
        "PDK_family", "Prog_core4", "Prog_9", "Neuro_5", "Neuro_10", "Myelin_OL", "Ctl_housekeeping", "Ctl_cytosolic_ribosome"]
CONTR = ["H_S", "H_N", "H_null", "C_S", "CC_SW", "CC_NW", "CC_SN"]
D = {(r["contrast"], r["set"]): r for r in rows if r["universe_thr_tpm"] == "1.0"}
SC, LAB, PW, PH, RH, TOP, XR = 2, 230, 140, 8, 22, 70, 1.0
W = LAB + PW * len(CONTR) + 10; H = TOP + RH * len(SETS) + 56
img = np.full((H, W, 3), 255, np.uint8)
def rect(x0, y0, x1, y1, c): img[max(0, y0):max(0, y1), max(0, x0):max(0, x1)] = c
def text(x, y, s, c=(0, 0, 0), sc=SC):
    for ch in s.upper():
        gl = FONT.get(ch, FONT[" "])
        for r, line in enumerate(gl):
            for q, v in enumerate(line):
                if v == "1": rect(x + q * sc, y + r * sc, x + q * sc + sc, y + r * sc + sc, c)
        x += 6 * sc
GREY, DARK, ORG, RED = (205, 205, 205), (20, 60, 140), (225, 130, 20), (170, 30, 30)
for i, c in enumerate(CONTR):
    x0 = LAB + i * PW
    text(x0 + 6, 8, c, DARK, 2)
    text(x0 + 6, 28, "N=" + {"H_S": "3V2", "H_N": "2V2", "H_null": "2V3", "C_S": "3V4", "CC_SW": "2V3", "CC_NW": "2V3", "CC_SN": "2V2"}[c], (90, 90, 90), 1)
    for k in (-1, 0, 1):
        xx = x0 + int(PW / 2 + k * (PW / 2 - 12) / XR)
        rect(xx, TOP - 6, xx + 1, TOP + RH * len(SETS), (0, 0, 0) if k == 0 else (225, 225, 225))
        text(xx - 6, TOP + RH * len(SETS) + 6, {-1: "-1", 0: "0", 1: "+1"}[k], (80, 80, 80), 1)
for j, s in enumerate(SETS):
    y = TOP + j * RH
    text(6, y + 4, s, (0, 0, 0), 1 if len(s) > 22 else 1)
    if j % 2 == 0: pass
    for i, c in enumerate(CONTR):
        r = D[(c, s)]; x0 = LAB + i * PW
        if r["mean"] == "": text(x0 + 30, y + 4, "N/A (<3 MEAS)", (150, 150, 150), 1); continue
        sx = lambda v: x0 + int(PW / 2 + max(-XR, min(XR, float(v))) * (PW / 2 - 12) / XR)
        rect(sx(r["null_lo"]), y + 3, sx(r["null_hi"]) + 1, y + 3 + 14, GREY)
        v = float(r["mean"]); col = DARK if r["separated"] == "True" else ORG
        cx = sx(v); out = r["outside"] == "True"
        if out: rect(cx - 5, y + 5, cx + 6, y + 16, col)
        else:
            rect(cx - 5, y + 5, cx + 6, y + 16, col); rect(cx - 3, y + 7, cx + 4, y + 14, (255, 255, 255))
        if abs(v) > XR: text(cx - 12 if v > 0 else cx + 8, y + 5, ">>" if v > 0 else "<<", RED, 1)
ly = TOP + RH * len(SETS) + 22
text(6, ly, "BAND = 2.5-97.5 PCT OF MATCHED NULL.  SQUARE FILLED = OUTSIDE NULL, HOLLOW = INSIDE.  BLUE = ALL KO ANIMALS ON ONE SIDE OF ALL CTL ANIMALS, ORANGE = NOT.", (0, 0, 0), 1)
text(6, ly + 12, "H_ = HIPPOCAMPUS KO VS ITS CONTROL; C_S = CORTEX; CC_ = CONTROL VS CONTROL (NO WWOX DIFFERENCE). TRANSCRIPT ONLY. NO P VALUE FOR A WWOX EFFECT.", (0, 0, 0), 1)
def png(a):
    raw = b"".join(b"\x00" + a[y].tobytes() for y in range(a.shape[0]))
    ch = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    return b"\x89PNG\r\n\x1a\n" + ch(b"IHDR", struct.pack(">IIBBBBB", a.shape[1], a.shape[0], 8, 2, 0, 0, 0)) + ch(b"IDAT", zlib.compress(raw, 9)) + ch(b"IEND", b"")
open(dst, "wb").write(png(img))
