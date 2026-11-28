"""Compare published nominal phenytoin benchmarks with the free serum label reference."""
import csv
import sys


MOLAR_MASS = 252.268


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source_locator", "matrix_or_readout", "phenytoin_uM",
                     "ratio_to_upper_free_serum_reference"))
    low = 1000 / MOLAR_MASS
    high = 2 * low
    writer.writerow(("Oral label section 2.4", "free serum lower reference", f"{low:.4f}", "NA"))
    writer.writerow(("Oral label section 2.4", "free serum upper reference", f"{high:.4f}", "NA"))
    writer.writerow(("Thompson Fig 6B", "nominal recombinant NaV1.1 protocol", "10", f"{10 / high:.4f}"))
    for concentration in (8, 24, 80):
        writer.writerow(("Tidball Fig 7D", "nominal induced-neuron network protocol",
                         concentration, f"{concentration / high:.4f}"))


if __name__ == "__main__":
    main()
