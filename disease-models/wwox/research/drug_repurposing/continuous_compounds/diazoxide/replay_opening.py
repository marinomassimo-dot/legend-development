"""Recompute the diazoxide opening contrasts across separate primary preparations."""
import csv
import sys


MASS = 230.671


def main():
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("source_locator", "quantity", "value", "units"))
    for time, concentration in (("1 h", 0.26), ("4 h", 0.78)):
        out.writerow(("Kishore Fig S1", f"rat CSF at {time}", f"{1000 * concentration / MASS:.6f}", "micromolar"))
    ratio = 300 / (1000 * 0.78 / MASS)
    out.writerow(("Burkart Fig 1 / Kishore Fig S1", "nominal bath / 4 h CSF", f"{ratio:.4f}", "cross-matrix ratio"))
    out.writerow(("Burkart Fig 1D", "change in median physiological sharp-wave rate",
                  f"{100 * (34 / 77 - 1):.4f}", "percent"))
    out.writerow(("Burkart Fig 1G", "change in reported peak frequency", f"{28.1 - 40.3:.1f}", "Hz"))
    out.writerow(("Burkart Fig 4C", "PV-V59M minus littermate seizure incidence",
                  f"{100 * (7 / 9 - 0 / 8):.4f}", "percentage points"))
    out.writerow(("Yamada et al. abstract", "interneuron / CA1 absolute mean hyperpolarization",
                  f"{18.6 / 4.0:.2f}", "descriptive ratio"))
    terminal_ic50 = 0.935
    out.writerow(("Matsumoto Fig 7Ac", "mIPSC frequency half-inhibition", f"{terminal_ic50:.3f}", "micromolar"))
    for locator, somatic_ec50 in (("Fig 6Ba caption", 5.11), ("Results prose", 51.1)):
        out.writerow((f"Matsumoto {locator} / Fig 7Ac", "somatic EC50 / mIPSC IC50",
                      f"{somatic_ec50 / terminal_ic50:.4f}", "cross-protocol ratio"))
    out.writerow(("Kishore Fig S1 / Matsumoto Fig 7Ac", "4 h CSF / mIPSC IC50",
                  f"{(1000 * 0.78 / MASS) / terminal_ic50:.4f}", "cross-matrix ratio"))
    for locator, before, after in (("Lemak Fig 1E", 7.7, 4.6), ("Lemak Fig 2B", 7.8, 3.1)):
        out.writerow((locator, "change in reported mean burst duration", f"{100 * (after / before - 1):.4f}", "percent"))
    out.writerow(("Shao Fig 6C2", "change in reported mean epileptiform rate", f"{3.9 - 3.6:.1f}", "bursts/min"))


if __name__ == "__main__":
    main()
