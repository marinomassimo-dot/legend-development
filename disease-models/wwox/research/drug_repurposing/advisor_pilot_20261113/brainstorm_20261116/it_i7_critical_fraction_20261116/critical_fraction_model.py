#!/usr/bin/env python3
"""I7 critical-fraction model (IT; non-canonical; hypothesis generator, not evidence).

Assumption (ASSUMED, not measured): a burst needs the isolated NMDAR current to stay above a
fraction f_c of its own untreated knockout value. A drug removes a fraction r of that current:
  pore blocker / agonist-site block: r = titration level t (uniform over receptors)
  GluN2B NAM: r = e * s_age, where s_age is the ifenprodil-sensitive share of the NMDAR EPSC
              (KNOWN wild type only, Mierau 2004: 53% P6-P8, 14% P13-P15) and e is the NAM's
              maximal efficacy on that share (e <= 1)
Bursts are abolished when 1 - r < f_c, i.e. r > 1 - f_c.
For each age window the script prints the smallest knockout share s_KO that would let a
saturating NAM (e = 1) abolish bursts, as a function of f_c. No random numbers: deterministic.
"""
import sys

if len(sys.argv) > 1:
    print("usage: critical_fraction_model.py   (no arguments; prints the table)")
    raise SystemExit(0)

SHARES = {"P6-P8 (wild type)": 0.53, "P13-P15 intact (wild type)": 0.14, "P13-P15 deprived (wild type)": 0.49}
FC = [0.0, 0.1, 0.25, 0.5, 0.75, 0.86, 0.9]

print("f_c = fraction of the untreated NMDAR current that must remain for a burst")
print("NAM (e=1) abolishes iff share s > 1 - f_c; pore block abolishes iff titration t > 1 - f_c\n")
print("%-8s" % "f_c" + "".join("%-30s" % k for k in SHARES) + "needed s_KO")
for f in FC:
    row = "%-8.2f" % f
    for k, s in SHARES.items():
        row += "%-30s" % ("abolishes" if s > 1 - f else "does not (max r=%.2f)" % s)
    row += "%.2f" % (1 - f)
    print(row)
print("\nReading: at P13-P17 with the wild-type share 0.14, a saturating NAM abolishes bursts only if f_c > 0.86,")
print("i.e. only if the burst needs almost all of the NMDAR current; for lower f_c the knockout share must be")
print("larger than the wild-type value (needed s_KO column). d-APV (r -> 1) always abolishes: consistent with INV-05 item 1.")
