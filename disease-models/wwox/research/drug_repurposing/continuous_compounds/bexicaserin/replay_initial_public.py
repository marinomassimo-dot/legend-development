"""PACIFIC Table 3 and public adult CSF conversion."""
from math import comb

# Fixed margins: 21/35 responders in active, 3/9 placebo.
p_observed = comb(35, 21) * comb(9, 3) / comb(44, 24)
probabilities = (comb(35, k) * comb(9, 24-k) / comb(44, 24) for k in range(15, 25))
p_two_sided = sum(probability for probability in probabilities if probability <= p_observed + 1e-15)
print('comparison\tquantity\tvalue')
print(f'PACIFIC_FAS\ttwo_sided_Fisher_p\t{p_two_sided:.4f}')
for label, responders, participants in (
    ('PACIFIC_FAS', 21, 35),
    ('PACIFIC_missing_active_all_fail', 21, 43),
    ('PACIFIC_missing_active_all_respond', 29, 43),
):
    print(f'{label}\tresponder_difference_pp\t{100 * (responders / participants - 3 / 9):.3f}')

# Kallem section 3.4 and EEC 2024 poster Table 3; nominal EC50 from Ren Table 5.
for label, ng_mL in (
    ('paper_csf_peak', 17.6), ('poster_low_csf_peak', 12.287),
    ('poster_high_csf_peak', 30.357), ('poster_low_csf_average', 9.257),
    ('poster_high_csf_average', 24.360),
):
    nM = 1000 * ng_mL / 295.33
    print(f'{label}\tconcentration_nM\t{nM:.2f}')
    print(f'{label}\tconcentration_over_nominal_IP_EC50\t{nM / 42:.3f}')
