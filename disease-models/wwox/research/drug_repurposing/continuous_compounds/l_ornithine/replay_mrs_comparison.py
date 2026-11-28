"""Replay public aggregate values and cerebral MRS visits already published in Table 1."""

from statistics import correlation, median

# Marten Table 1, parieto-occipital white matter, mmol/L. Baseline peak was
# unquantifiable per Results. The table's baseline fit of 0.1 is excluded.
post_start_tcr = (3.4, 3.4, 3.7, 2.7, 2.6, 3.7, 2.7, 2.3, 2.6, 2.3, 3.0, 2.3, 2.7)
tcr = (3.4, 2.7, 2.6, 3.7, 2.3, 2.6, 2.3, 2.3)
gaa = (0.3, 0.5, 1.5, 1.3, 0.7, 0.3, 1.1, 0.5)

print("comparison\tvalue\tlocator")
print(f"post_start_visits_n\t{len(post_start_tcr)}\tMarten Table 1, tCr")
print(f"post_start_tcr_median_mmol_L\t{median(post_start_tcr):.2f}\tMarten Table 1, tCr")
print(f"post_start_tcr_range_mmol_L\t{min(post_start_tcr):.2f} to {max(post_start_tcr):.2f}\tMarten Table 1, tCr")
print(f"paired_post_start_brain_MRS_visits\t{len(tcr)}\tMarten Table 1, tCr and GAA")
print(f"paired_visit_descriptive_pearson_r\t{correlation(tcr, gaa):.3f}\tMarten Table 1, tCr and GAA")
omit = [correlation(tcr[:i] + tcr[i+1:], gaa[:i] + gaa[i+1:]) for i in range(len(tcr))]
print(f"leave_one_visit_out_r_range\t{min(omit):.3f} to {max(omit):.3f}\tMarten Table 1, tCr and GAA")
print(f"L_ornithine_add_on_GAA_percent_change\t{100 * (12.2 / 19.1 - 1):.2f}\tStockler-Ipsiroglu section 2.11.1.1, plasma")
print(f"OAT_fasting_ornithine_patient_control_ratio\t{733 / 38.2:.2f}\tSipila Table I, plasma")
