"""Transfer tests on group-mean thresholds, T-current availability and observed firing curves."""
from itertools import product
from math import exp
from pathlib import Path
from statistics import mean
import csv

ROOT = Path(__file__).parent
# Table 1, juvenile neocortex: rest (mV), threshold (mV), rebound (mV), resistance (MOhm).
CELLS = {"WT":(-79.25,-43.77,0.96,102.88),"HT":(-75.51,-40.30,1.24,143.26),
         "KO":(-73.62,-41.32,1.86,143.03)}

def table(name, header, rows):
    with (ROOT/name).open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)

def threshold_and_gating():
    rows,gate=[],[]
    for label,(rest,threshold,reb,res) in CELLS.items():
        margin=threshold-rest
        rows.append([label,rest,threshold,reb,res,margin,margin-reb,(margin-reb)*1000/res,
                     margin*1000/res,reb*1000/res])
        for state,v in [("rest",rest),("passive_minus_200_pA",rest-.2*res),("matched_hold",-80)]:
            # Leresche et al. inactivation, dissociated rat thalamic neurons,
            # V1/2 = -84.5 mV, k = 4 mV. Additional offsets stress cross-region transfer.
            for shift in (-10,0,10):
                fraction = 1/(1+exp((v-(-84.5+shift))/4))
                gate.append([label,state,v,shift,fraction])
    table("threshold_margins.tsv", ["group","rest_mV","threshold_mV","rebound_mV","Rm_MOhm","rest_margin_mV",
            "margin_after_rebound_mV","equivalent_post_rebound_pA","equivalent_no_rebound_pA",
            "equivalent_change_if_rebound_removed_pA"],rows)
    table("availability.tsv",["group","state","conditional_voltage_mV","midpoint_shift_mV","available_fraction"],gate)

def crossing(currents, frequencies, target):
    for i in range(len(currents)-1):
        a,b = frequencies[i:i+2]
        if a<=target<=b and b>a:
            return currents[i] + (target-a)*(currents[i+1]-currents[i])/(b-a)
    raise ValueError(f"{target} outside the visible curve")

def firing():
    # Pixel coordinates relative to the original TIFF cropped at +0+25.
    # Only the visible group markers required to bracket the target frequencies are used.
    markers = {
     ("absolute","WT"):[(80,275),(100,247),(120,210),(140,178),(160,142)],
     ("absolute","KO"):[(60,245),(80,204),(100,170),(120,137)],
     ("relative","WT"):[(20,266),(40,212),(60,194),(80,158),(100,104)],
     ("relative","KO"):[(20,249),(40,195),(60,158),(80,122)]}
    rows,points=[],[]
    for axis,base,pxperHz in [("absolute",303,238/25),("relative",302,225/25)]:
        curves=[]
        for group in ("WT","KO"):
            m=markers[axis,group]
            ix=[i for i,y in m]
            f=[(base-y)/pxperHz for i,y in m]
            points.extend((axis,group,i,y,v) for (i,y),v in zip(m,f))
            curves.append((ix,f))
        for target in (10,15):
            # A common offset of all sampled frequencies within each group gives
            # extremal horizontal crossings under a +/-0.5 Hz per-point reading tolerance.
            nominal=[crossing(ix,v,target) for ix,v in curves]
            differences=[]
            for e0,e1 in product((-.5,.5),repeat=2):
                perturbed=[crossing(ix,[x+err for x in v],target) for (ix,v),err in zip(curves,(e0,e1))]
                differences.append(perturbed[0]-perturbed[1])
            rows.append((axis,target,*nominal,nominal[0]-nominal[1],min(differences),max(differences)))
    table("curve_points.tsv",["axis","group","injected_pA","panel_y_px","frequency_Hz"],points)
    table("firing_targets.tsv",["axis","target_Hz","WT_pA","KO_pA","WT_minus_KO_pA",
          "lower_at_half_Hz_tolerance","upper_at_half_Hz_tolerance"],rows)

if __name__=="__main__":
    threshold_and_gating()
    firing()
