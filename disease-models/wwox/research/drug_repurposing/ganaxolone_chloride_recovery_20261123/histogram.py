"""Read the panel-D horizontal bar heights in the publisher's CC BY high-resolution image."""
import argparse
import csv
import hashlib
from pathlib import Path
import subprocess
from statistics import median

EXPECTED = "1a61590953fb9fff30e7df3198c61f6c5a29ee5608041e4a1814faeba4fddf9d"
TOTAL_EVENTS = 119


def recover(source):
    assert hashlib.sha256(source.read_bytes()).hexdigest() == EXPECTED
    pixels = subprocess.check_output(["convert", str(source), "-crop", "495x345+600+1390", "+repage",
                                      "-colorspace", "Gray", "-depth", "8", "gray:-"])
    assert len(pixels) == 495*345
    # Plot origin (118,271), tick at four seconds (291.5,271), tick at count 50 (118,39).
    # Flat bar tops are distinct from the sloping gamma fit. Restrict to a three-pixel
    # vertical window placed from visual inspection, and require a horizontal dark segment.
    observed = [(132,252),(143,44),(154,122),(165,201),(176,238),(187,261),(198,266),(209,261)]
    rows = []
    for i,(center,top) in enumerate(observed):
        flats = [y for y in range(top-1,top+2)
                 if sum(pixels[y*495+x] < 128 for x in range(center-3,center+4)) == 7]
        assert flats
        mid = median(flats)
        estimate = round((271-mid)*50/(271-39))
        # Perturb the calibrated axes and bar top by half a pixel each.
        fits = {round((base-y)*50/(base-high)) for base in (270.5,271.5)
                for high in (38.5,39.5) for y in (mid-.5,mid+.5)}
        assert fits == {estimate}, (center,mid,fits)
        lo = (126.6+10.98*i-118)*4/(291.5-118)
        hi = (126.6+10.98*(i+1)-118)*4/(291.5-118)
        rows.append((center,mid,lo,hi,estimate))
    assert rows[-1][2]<2<rows[-1][3] and rows[-2][3]<2
    with Path(__file__).with_name("wwox_burst_histogram.tsv").open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow(["panel_center_x_px","panel_top_y_px","approx_bin_lo_s","approx_bin_hi_s","events"])
        writer.writerows(rows)
    below = sum(row[-1] for row in rows[:-1])
    print("Bursts longer than 2 s:",TOTAL_EVENTS-below-rows[-1][-1],"to",TOTAL_EVENTS-below,"of",TOTAL_EVENTS)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("figure",type=Path)
    recover(parser.parse_args().figure)
