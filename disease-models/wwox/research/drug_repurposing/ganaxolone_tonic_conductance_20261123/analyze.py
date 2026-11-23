"""Equivalent passive somatic conductance at the published group-mean parameters."""
import csv
from pathlib import Path

# Wwox cortical pyramidal neurons, Table 1: resistance, tau, Vrest, spike threshold.
wwox = {
    "WT": (102.88, 18.55, -79.25, -43.77),
    "HT": (143.26, 18.79, -75.51, -40.30),
    "KO": (143.03, 21.25, -73.62, -41.32),
}
# γ2-R43Q layer II/III cortex at 10 nM drug: pA and pA/pF.
current = 9.8
density = 0.38
resistance, tau, rest, threshold = wwox["KO"]
baseline = 1000 / resistance
gap = 1000 / wwox["WT"][0] - baseline
effective_capacitance = tau * baseline
path = Path(__file__).parent / "scenarios.tsv"
with path.open("w") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["transfer", "clamp_driving_force_mV", "native_EGABA_mV",
                     "added_nS", "conductance_gap_closed_fraction",
                     "post_resistance_Mohm", "post_passive_rest_mV",
                     "increment_current_at_original_spike_threshold_pA"])
    for reference, amplitude in [("whole-cell pA", current),
                                 ("pA/pF x effective KO capacitance", density * effective_capacitance)]:
        for force in [50, 60, 70]:
            extra = amplitude / force
            for reversal in [-85, -75, -65, -55, -45, threshold, -35]:
                post_g = baseline + extra
                new_rest = (rest * baseline + extra * reversal) / post_g
                threshold_current = extra * (threshold - reversal)
                writer.writerow([reference, force, reversal, extra, extra / gap,
                                 1000 / post_g, new_rest, threshold_current])
