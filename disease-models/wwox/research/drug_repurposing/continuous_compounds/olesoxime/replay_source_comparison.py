"""Recompute contrasts from the aggregate data cited in the companion report."""

control_threshold = 34.5
nominal_concentrations = (0.1, 0.5, 1.0, 5.0)
olesoxime_thresholds = (36.6, 37.9, 35.4, 35.7)
cyclosporin_thresholds = (71.4, 80.7, 85.3, 87.7)

print("nominal_uM\tolesoxime_over_control\tcyclosporin_over_control")
for concentration, olesoxime, cyclosporin in zip(
    nominal_concentrations, olesoxime_thresholds, cyclosporin_thresholds, strict=True
):
    print(f"{concentration:g}\t{olesoxime / control_threshold:.3f}\t"
          f"{cyclosporin / control_threshold:.3f}")

stress_ocr_drop = 55.2
olesoxime_ocr_drop = 14.5
ocr_difference = stress_ocr_drop - olesoxime_ocr_drop
print(f"ocr_recovery_percentage_points\t{ocr_difference:.1f}")
print(f"ocr_decrement_attenuated_percent\t{100 * ocr_difference / stress_ocr_drop:.1f}")

olesoxime_mfm_change = 0.18
placebo_mfm_change = -1.82
print(f"sma_mfm_difference_points\t{olesoxime_mfm_change - placebo_mfm_change:.2f}")
