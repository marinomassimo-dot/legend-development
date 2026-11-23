"""Chloride flux at fixed voltage history and reanalysis of an independent cortical timing control."""
import argparse
import csv
import hashlib
from itertools import product
from math import exp, expm1, isclose, log
from pathlib import Path
from statistics import mean, median
from xml.etree import ElementTree
from zipfile import ZipFile

ROOT = Path(__file__).parent
SOURCE_SHA = "08efd1603ea3037d0611368463624e32a7470b3a1874e8d14dfd7e657935f49f"
REST = -73.62
PRIMARY_PERIOD = 26.2
PRIMARY_BURST = 0.66


def table(name, header, rows):
    with (ROOT / name).open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def flux_model():
    rows = []
    # The approximate whole-cell conductance is used as a scale. Any constant
    # chloride share multiplies both terms and leaves their sign crossover unchanged.
    for period, duration, reversal, burst_voltage in product(
        (PRIMARY_PERIOD, 71.4), (0.53, PRIMARY_BURST, 1.06), (-75, -70, -65, -55), (-40, -20, 0)
    ):
        rest_time = period - duration
        interburst_term = (REST - reversal) * rest_time
        burst_term = (burst_voltage - reversal) * duration
        crossover = -interburst_term / burst_term if interburst_term < 0 else None
        for ratio in (1, 5, 10, 15, 20):
            weighted_reversal = (REST * rest_time + burst_voltage * ratio * duration) / (rest_time + ratio * duration)
            signed_driving = interburst_term + ratio * burst_term
            assert isclose(signed_driving, (weighted_reversal - reversal) * (rest_time + ratio * duration), abs_tol=1e-10)
            rows.append((period, duration, reversal, burst_voltage, ratio, weighted_reversal, crossover,
                         signed_driving * (9.8/60), signed_driving * (0.38*(21.25*1000/143.03)/60)))
    table("flux_scenarios.tsv", ["cycle_s","burst_s","ECl_mV","burst_mV","burst_to_rest_extra_g",
        "zero_flux_ECl_mV","crossover_g_ratio","charge_pC_whole_cell_scale","charge_pC_density_scale"], rows)


def anion_sensitivity():
    # Exploratory constant-field comparison. Quantities are per unit chloride
    # permeability, with only sign and ratios interpreted; no ionic volume fit.
    thermal = 8.314462618 * 305.15 / 96485.33212 * 1000
    outside_cl, outside_bicarb = 130, 25
    def ghk(voltage, inside):
        if voltage == 0:
            return thermal * (outside_cl - inside)
        return voltage * (inside - outside_cl * exp(voltage/thermal)) / -expm1(voltage/thermal)
    rows = []
    rest_time = PRIMARY_PERIOD - PRIMARY_BURST
    for target, relative_perm, inside_bicarb in product((-65,), (0,0.2,0.25), (12,16,20)):
        inside_cl = (outside_cl + relative_perm*outside_bicarb)*exp(target/thermal) - relative_perm*inside_bicarb
        ecl = thermal*log(inside_cl/outside_cl)
        assert isclose(thermal*log((inside_cl+relative_perm*inside_bicarb) /
                                   (outside_cl+relative_perm*outside_bicarb)), target)
        for voltage in (-40,-20,0):
            rest_flux = ghk(REST,inside_cl)*rest_time
            burst_flux = ghk(voltage,inside_cl)*PRIMARY_BURST
            assert burst_flux > 0 and abs(ghk(ecl,inside_cl)) < 1e-10
            crossover = -rest_flux/burst_flux if rest_flux < 0 else None
            ohmic_rest = (REST-ecl)*rest_time
            ohmic_burst = (voltage-ecl)*PRIMARY_BURST
            rows.append([target,relative_perm,inside_bicarb,inside_cl,ecl,voltage,
                         -ohmic_rest/ohmic_burst if ohmic_rest<0 else None,crossover,
                         "loading" if rest_flux+burst_flux>0 else "clearance",
                         "loading" if ohmic_rest+ohmic_burst>0 else "clearance"])
    table("anion_sensitivity.tsv",["EGABA_mV","bicarbonate_to_chloride_permeability","intracellular_bicarbonate_mM",
          "inferred_chloride_mM","ECl_mV","burst_mV","ohmic_crossover_conductance_ratio",
          "constant_field_crossover_permeability_ratio","tonic_constant_field","tonic_ohmic"],rows)


def sheet(book, strings, number):
    root = ElementTree.fromstring(book.read(f"xl/worksheets/sheet{number}.xml"))
    data = {}
    for cell in root.findall(".//{*}c"):
        value = cell.findtext("{*}v")
        if value is not None:
            data[cell.get("r")] = strings[int(value)] if cell.get("t") == "s" else float(value)
    return data


def summaries(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest() == SOURCE_SHA
    with ZipFile(path) as book:
        strings = ["".join(s.itertext()) for s in ElementTree.fromstring(book.read("xl/sharedStrings.xml"))]
        timing = sheet(book, strings, 4)
        kinetics = sheet(book, strings, 3)
        supplement = sheet(book, strings, 10)
    assert timing["A41"] == "Figure 5f" and kinetics["A115"] == "Figure 4i"
    delays = ["0", "0.5", "2", ">2"]
    arms = {}
    cached = {}
    rows = []
    for delay, start, column_pairs in zip(delays, (7,109,181,225), [("BC","DE"),("GH","IJ"),("LM","NO"),("QR","ST")]):
        for group,(label,value) in zip(("GFP","KCC2"), column_pairs):
            assert timing[f"{value}46"] == group
            i = 47
            changes = []
            while str(timing[f"{label}{i}"]).startswith("Animal "):
                # normalized seizure duration indexed to light off = 100 in each animal.
                changes.append(timing[f"{value}{i}"] - 100)
                i += 1
            assert timing[f"{label}{i}"] == "Mean"
            cached[delay,group] = timing[f"{value}{i}"] - 100
            # Verify each normalized ratio against independently tabulated absolute
            # durations in Supplementary Fig. 7; expose the alternative weighting.
            lab,off,on = "JKL" if group=="GFP" else "NOP"
            pairs = []
            for j, change in enumerate(changes, start):
                assert str(supplement[f"{lab}{j}"]).startswith("Animal ")
                pair = (supplement[f"{off}{j}"],supplement[f"{on}{j}"])
                assert isclose(100 * pair[1]/pair[0] - 100, change, abs_tol=1e-8)
                pairs.append(pair)
            assert supplement[f"{lab}{start+len(changes)}"] == "Mean"
            pooled = 100 * sum(b for _,b in pairs)/sum(a for a,_ in pairs) - 100
            assert (isclose(cached[delay,group],mean(changes), abs_tol=1e-8)
                    or isclose(cached[delay,group],pooled,abs_tol=1e-8))
            arms[delay,group] = changes
            rows.append([delay, group, len(changes), mean(changes), median(changes), min(changes),
                         max(changes), sum(x > 0 for x in changes), sum(x < 0 for x in changes), cached[delay,group],pooled,mean(b-a for a,b in pairs)])
    table("timing_by_arm.tsv", ["delay_after_detection_s","group","animals","mean_change_pct",
          "median_change_pct","minimum_pct","maximum_pct","prolonged","shortened","workbook_summary_change_pct","ratio_of_group_means_change_pct","mean_within_animal_difference_s"], rows)
    # The source provides within-animal normalization. Identity across timing bins
    # cannot be guaranteed. Omit independently in each cell as an influence check.
    cells = [arms[">2","GFP"], arms[">2","KCC2"], arms["0","GFP"], arms["0","KCC2"]]
    def delta(m):
        return (m[0] - m[1]) - (m[2] - m[3])
    omissions = [[mean(x[:j] + x[j+1:]) for j in range(len(x))] for x in cells]
    influenced = [delta(m) for m in product(*omissions)]
    table("timing_interaction.tsv", ["contrast","observed_points","omit_one_per_cell_min","omit_one_per_cell_max","using_workbook_summary_points"],
          [["(GFP-KCC2)_late_minus_immediate",delta([mean(x) for x in cells]), min(influenced), max(influenced),
            delta([cached[k] for k in ((">2","GFP"),(">2","KCC2"),("0","GFP"),("0","KCC2"))])]])
    residuals = []
    for group,column in [("Halo","C"), ("Halo+KCC2","E")]:
        assert kinetics[f"{column}119"] == group
        taus = [kinetics[f"{column}{i}"] for i in range(120,127)]
        assert isclose(mean(taus),kinetics[f"{column}127"])
        for period in (PRIMARY_PERIOD, 71.4):
            gap = period - PRIMARY_BURST
            ratios = [exp(-gap / tau) for tau in taus]
            residuals.append([group,len(taus),mean(taus),median(taus),gap,mean(ratios),median(ratios),
                              min(ratios), max(ratios)])
    table("recovery_transfer.tsv", ["group","cells","mean_tau_s","median_tau_s","interburst_gap_s",
          "mean_remaining_fraction","median_remaining_fraction","min_remaining","max_remaining"], residuals)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_workbook", type=Path)
    args = parser.parse_args()
    flux_model()
    anion_sensitivity()
    summaries(args.source_workbook)
