"""Rebuild nominal exposure comparisons for parent ursolic acid."""

MW_G_PER_MOL = 456.7


def row(comparison, ng_ml, locator):
    print(f"{comparison}\t{ng_ml:g}\t{ng_ml / MW_G_PER_MOL:.6g}\t{locator}")


def main():
    print("comparison\tng_per_mL\tµmol_per_L\tlocator")
    row("Lowest direct OPC concentration tested", 1000, "Zhang Fig. 8A")
    row("Slice treatment and upper direct OPC concentration", 10000, "Zhang Figs. 5 and 8")
    for source_ng_ml in (1000, 5000, 10000):
        row(f"Conditional carryover from {source_ng_ml:g} ng/mL source", source_ng_ml * 0.5,
            "Zhang Fig. 6E half-volume transfer; conditional on 100% residual parent")
    row("Human apple-peel plasma mean peak", 3.3, "Stebounova Fig. 3A")
    row("Adult purified oral assay quantification floor", 10.5, "Hirsh conference abstract")
    row("Adult IV nanoliposome lowest dose-group mean plasma peak", 1835, "Zhu Table 2")
    row("Adult IV nanoliposome highest dose-group mean plasma peak", 3457, "Zhu Table 2")
    row("Rat oral mean plasma peak", 2025, "Chen Table 1")


if __name__ == "__main__":
    main()
