"""Read the published horizontal bar fills in Furukawa et al. Figure 9, panels C and D."""
import csv
from pathlib import Path
import subprocess
import sys
import numpy as np

def endpoints(pixels, origin, limit, center_y, treated):
    # Error whiskers obscure the center; repeat near either side of the solid fill.
    ends = []
    for y in (center_y - 3, center_y - 2, center_y + 2, center_y + 3):
        colors = pixels[y, origin + 1:limit].astype(int)
        red, green, blue = colors.T
        mask = ((red > 150) & (green > 150) & (blue < 120) if treated
                else (blue - red > 45) & (green - red > 20))
        hits = np.flatnonzero(mask)
        if len(hits):
            ends.append(origin + 1 + hits[-1] + 1)
        else:
            ends.append(origin)
    return np.median(ends), min(ends), max(ends)

def main(source):
    raw = subprocess.check_output(['convert', source, '-depth', '8', 'RGB:-'])
    pixels = np.frombuffer(raw, dtype=np.uint8).reshape((779, 784, 3))
    # Axis origins and endpoints in the native 784 x 779 file. Only CP bars enter here.
    plots = [('E17.5','+/+',62,262,60,300,316,7,4),
             ('E17.5','+/GFP',308,507,60,300,316,6,3),
             ('E17.5','GFP/GFP',548,748,60,300,316,5,5),
             ('E16.5','GFP/GFP',138,383,100,577,593,3,6),
             ('E18.5','GFP/GFP',449,694,100,577,593,3,3)]
    with Path(__file__).with_name('cortical_plate.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['age','GAD67','n_control_fetuses','n_depleted_fetuses','control_pct','depleted_pct','delta_pp','readback_span_pp'])
        for age, genotype, origin, end, axis, cy, ty, nc, nt in plots:
            # The E16.5 legend lies to the right of its short CP bars.
            crop = 250 if age == "E16.5" else end
            c, cmin, cmax = endpoints(pixels, origin, crop, cy, False)
            t, tmin, tmax = endpoints(pixels, origin, crop, ty, True)
            scale = axis / (end - origin)
            writer.writerow([age,genotype,nc,nt,round((c-origin)*scale,1),round((t-origin)*scale,1),
                             round((t-c)*scale,1),round(max(cmax-cmin,tmax-tmin)*scale,1)])

if __name__ == '__main__':
    main(sys.argv[1])
