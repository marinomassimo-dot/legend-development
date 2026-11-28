# Litters needed = knockouts / (litter_size * knockout_frequency), litter size 7 (the brief's own figure).
# Fractions are used, so there is no floating-point error at integer boundaries.
# Two roundings are printed: NEAREST (reproduces the brief's own old numbers) and CEIL (used for the new numbers:
# whole litters, never fewer than needed).
from fractions import Fraction as F
import math

LITTER = 7
FREQ = {"mendel25": F(25, 100), "cheng_WD1_5.1": F(51, 1000), "cheng_WD234_6.5": F(65, 1000)}

def litters(k, f):
    return F(k) / (LITTER * f)

def nearest(x):          # round half up
    return math.floor(x + F(1, 2))

def ceil(x):
    return math.ceil(x)

# (label, knockouts, old figure printed in the brief or None)
ITEMS = [
    ("pilot knockouts low (2 ages x 6 per cell)", 12, 7),
    ("pilot knockouts high (2 ages x 8 per cell)", 16, 9),
    ("pilot wild-type low (24)", 24, 14),
    ("pilot wild-type high (32)", 32, 18),
    ("3 knockout arms x 11 (sigma 0.3)", 33, 19),
    ("3 knockout arms x 31 (sigma 0.5)", 93, 53),
    ("interaction sigma 0.3, 2 cells x 22", 44, 25),
    ("interaction sigma 0.5, 124 knockouts", 124, 71),
    ("3 knockout arms at 36 per arm", 108, 62),
    ("3 knockout arms at 109 per arm", 327, 187),
    ("interaction equal variance low (145 stated)", 145, 82),
    ("interaction equal variance low (144 = 2 x 72)", 144, 82),
    ("interaction equal variance high (435 stated)", 435, 249),
    ("interaction equal variance high (436 = 2 x 218)", 436, 249),
    ("interaction floor-bound low (350)", 350, 200),
    ("interaction floor-bound high (630)", 630, 360),
    ("planning total low (33 knockouts)", 33, 19),
    ("planning total high (150 knockouts)", 150, 86),
]

print(f"litter size {LITTER}; knockouts per litter at each frequency:")
for name, f in FREQ.items():
    print(f"  {name}: {float(LITTER*f):.4f}")
print()
hdr = f"{'item':52s} {'KO':>4s} | {'old':>4s} | {'M25 near':>8s} {'M25 ceil':>8s} | {'WD1 5.1% ceil':>13s} {'WD234 6.5% ceil':>15s} | exact WD1 / WD234"
print(hdr)
rows = {}
for label, k, old in ITEMS:
    m = litters(k, FREQ["mendel25"])
    a = litters(k, FREQ["cheng_WD1_5.1"])
    b = litters(k, FREQ["cheng_WD234_6.5"])
    flag = "" if old is None else ("OK" if nearest(m) == old else "DIFF")
    rows[(label, k)] = (old, nearest(m), ceil(m), ceil(a), ceil(b))
    print(f"{label:52s} {k:4d} | {str(old):>4s} | {nearest(m):8d} {ceil(m):8d} | {ceil(a):13d} {ceil(b):15d} | {float(a):8.2f} / {float(b):8.2f}  {flag}")

print()
print("Ranges used in the drafted sentences (low KO at WD234 .. high KO at WD1, and each line separately):")
def rng(k1, k2):
    return {n: (ceil(litters(k1, f)), ceil(litters(k2, f))) for n, f in FREQ.items() if n != "mendel25"}
for label, k1, k2 in [("pilot knockouts 12 to 16", 12, 16), ("3 arms 33", 33, 33), ("3 arms 93", 93, 93),
                      ("interaction 44", 44, 44), ("interaction 124", 124, 124),
                      ("3 arms 108 to 327", 108, 327), ("interaction equal-var 145 to 435", 145, 435),
                      ("interaction floor-bound 350 to 630", 350, 630), ("planning total 33 to 150", 33, 150)]:
    r = rng(k1, k2)
    print(f"  {label:38s} WD1 {r['cheng_WD1_5.1'][0]} to {r['cheng_WD1_5.1'][1]}   WD234 {r['cheng_WD234_6.5'][0]} to {r['cheng_WD234_6.5'][1]}   overall {r['cheng_WD234_6.5'][0]} to {r['cheng_WD1_5.1'][1]}")

print()
print("Y2 checks (ADV-311): 33 -> 93 (WD1) / 73 (WD234); 33 to 150 -> 93 to 421 / 73 to 330; 350 to 630 -> 770 to 1,765 (one end each)")
print("  350 at 6.5% =", ceil(litters(350, FREQ['cheng_WD234_6.5'])), "; 630 at 5.1% =", ceil(litters(630, FREQ['cheng_WD1_5.1'])),
      "; 350 at 5.1% =", ceil(litters(350, FREQ['cheng_WD1_5.1'])), "; 630 at 6.5% =", ceil(litters(630, FREQ['cheng_WD234_6.5'])))

print()
print("Binomial check: among litters of 7 with at least one knockout, share with two or more (DERIVED, independence assumed)")
for name, f in FREQ.items():
    p = float(f); q = 1 - p
    p0 = q**7; p1 = 7*p*q**6
    print(f"  {name}: P(0)={p0:.3f} P(1)={p1:.3f} P(>=1)={1-p0:.3f} P(>=2)={1-p0-p1:.3f}  share of knockout litters with >=2: {(1-p0-p1)/(1-p0):.3f}")

print()
print("Wild types supplied by the litters needed for the knockouts, IF wild types are 25 percent of pups (their frequency is NOT reported):")
for label, k in [("pilot 12 KO", 12), ("pilot 16 KO", 16), ("33 KO", 33), ("108 KO", 108), ("327 KO", 327)]:
    for name in ("cheng_WD1_5.1", "cheng_WD234_6.5"):
        n = ceil(litters(k, FREQ[name]))
        print(f"  {label:12s} {name:18s} litters {n:5d} -> wild types about {n*LITTER*0.25:.0f}")
print("  wild types asked: pilot 24 to 32; age series and panel 231")

print()
print("Ludes-Meyers 2009 Table 1: 30 knockouts of 154 =", f"{30/154*100:.1f}", "percent (expected 38.5 = 25 percent of 154); per litter of 7:", f"{7*30/154:.2f}")
print("Cheng supplement p. 3: 5.1% of 177 =", f"{0.051*177:.1f}", "knockouts; 6.5% of 785 =", f"{0.065*785:.1f}", "(counts not printed; percentages only)")
