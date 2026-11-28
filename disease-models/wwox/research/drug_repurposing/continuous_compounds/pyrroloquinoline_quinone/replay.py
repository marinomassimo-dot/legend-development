"""Reproduce scale contrasts and one OCR non-identifiability example."""
import csv
import sys
from decimal import Decimal


def main():
    circulating_nm = Decimal("9")
    liver_bath_nm = Decimal("30") * 1000
    nmda_bath_nm = Decimal("50") * 1000
    brain_pct_of_absorbed = Decimal("0.2")
    absorbed_pct = Decimal("3.3")
    reserve_control, reserve_pqq = Decimal("69"), Decimal("97")
    tbars_control, tbars_pqq = Decimal("3.4"), Decimal("2.0")

    rows = [
        ("Hepa1-6 nominal bath / adult circulating peak",
         f"{liver_bath_nm / circulating_nm:.0f}", "ratio", "Chowanadisai Fig. 1J; Harris Fig. 2A"),
        ("rat cortical NMDA nominal bath / adult circulating peak",
         f"{nmda_bath_nm / circulating_nm:.0f}", "ratio", "Aizenman Fig. 1; Harris Fig. 2A"),
        ("6 h whole-brain label, product of group means",
         f"{brain_pct_of_absorbed * absorbed_pct / 100:.4f}", "% administered activity",
         "Smidt Tables I and II; descriptive only"),
        ("PQQ minus control spare respiratory capacity",
         str(reserve_pqq - reserve_control), "percentage points of WT", "Martino Adami Fig. 5a"),
        ("PQQ minus control hippocampal TBARS",
         str(tbars_pqq - tbars_control), "nmol/mg protein", "Martino Adami Fig. 5d"),
    ]

    # Identical observed basal and uncoupled rates can conceal opposite ATP-linked changes.
    baseline_atp_linked = 60
    for label, basal, post_oligomycin, uncoupled in (
        ("reference", 100, 40, 140),
        ("scenario A", 110, 40, 170),
        ("scenario B", 110, 60, 170),
    ):
        atp_linked = basal - post_oligomycin
        rows.append((
            label, str(atp_linked - baseline_atp_linked), "arbitrary OCR units relative to reference",
            f"illustration only; basal={basal}, after oligomycin={post_oligomycin}, maximum={uncoupled}",
        ))

    writer = csv.writer(sys.stdout, dialect="excel-tab", lineterminator="\n")
    writer.writerow(("contrast", "value", "unit", "source_or_assumption"))
    writer.writerows(rows)


if __name__ == "__main__":
    main()
