"""Estimate Figure 4E/G event areas and propagate trace-readback sensitivity."""
import argparse
import csv
import hashlib
from pathlib import Path
import subprocess

import numpy as np

HERE = Path(__file__).resolve().parent
FIGURE_SHA = "526b8122a3dc301d2c30757f7b3c6f7a081497e90675e011052ccd856e6b3de0"
# Global image crop, graph x=0 and x=24 ms, y=0 and negative units per pixel.
PANELS = {"E": (740,1050, 67,305, 89,5/(138-89)),
          "I": (1740,1050, 64,298, 82,10/(123-82))}
FREQ = {"E": (9.9,10.1), "I": (10.3,8.4)}


def save(filename, header, rows):
    with (HERE / filename).open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow(header.split())
        writer.writerows(rows)


def extract(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest() == FIGURE_SHA
    raw = subprocess.check_output(["convert", str(path), "-depth", "8", "rgb:-"])
    rgb = np.frombuffer(raw, np.uint8).reshape(2027,2126,3).astype(int)
    points, totals = [], {}
    for family,(ox,oy,x0,x24,y0,scale) in PANELS.items():
        art=rgb[oy:oy+276,ox:ox+320]
        red,green,blue=art.transpose(2,0,1)
        colored=(red-green>55)&(red-blue>45)&(green<165)
        dark=(red<100)&(green<100)&(blue<100)&(np.abs(red-green)<40)
        # Exclude axes. Both traces share a baseline segment around zero.
        window = np.arange(art.shape[0])
        eligible=(window>=y0-6)&(window<=(264 if family=="I" else 275))
        times=np.arange(x0+3,x24-1)
        for group,mask,rate in zip(("CTL","KO"),(dark,colored),FREQ[family]):
            estimates=[]
            for x in times:
                ys=np.flatnonzero(mask[:,x]&eligible)
                hidden=not len(ys)
                if hidden:
                    ys=np.flatnonzero((colored[:,x]|dark[:,x])&eligible)
                if not len(ys):
                    raise ValueError(f"No visible trace at {family} {group} x={x}")
                estimates.append([ys.min(),np.median(ys),ys.max()])
                points.append([family,group,x,(x-x0)*24/(x24-x0),*estimates[-1],hidden])
            lines=(np.array(estimates)-y0)*scale
            # The omitted endpoints occupy less than half a millisecond near baseline.
            dt=24/(x24-x0)
            areas=np.sum((lines[:-1]+lines[1:])/2,axis=0)*dt
            totals[family,group]=(rate,*areas)
    save("wave_points.tsv","current group crop_x ms outer_min_y midpoint_y outer_max_y color_occluded",points)
    return totals


def run(path):
    totals=extract(path)
    rows=[]
    for (family,group),(rate,low,mid,high) in totals.items():
        rows.append((family,group,rate,low,mid,high,rate*mid/1000))
    save("wave_areas.tsv","current group rate_Hz area_low_pAms area_mid_pAms area_high_pAms estimated_mean_pA",rows)
    def ratio(ko_e,ko_i,ctl_e,ctl_i):
        def magnitude(f,g,index):
            values=totals[f,g]
            return values[0]*values[index]
        return magnitude("E","KO",ko_e)*magnitude("I","CTL",ctl_i)/(magnitude("I","KO",ko_i)*magnitude("E","CTL",ctl_e))
    nominal=ratio(2,2,2,2)
    lo,hi=ratio(1,3,3,1),ratio(3,1,1,3)
    scenarios=[]
    for i_loss in (0,.10,.25,.50):
        for label,r in (("trace_lower",lo),("center",nominal),("trace_upper",hi)):
            scenarios.append((label,r,i_loss,1-(1-i_loss)/r))
    save("thresholds.tsv","source_bound KO_over_CTL_index fraction_inhibitory_loss excitatory_loss_to_match_control_index",scenarios)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("figure",type=Path)
    run(parser.parse_args().figure)
