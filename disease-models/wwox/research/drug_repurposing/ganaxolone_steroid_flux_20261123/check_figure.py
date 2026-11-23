"""Recalculate selected transfected-minus-mock contrasts from Keller figure 2.58."""
import argparse
import csv
import hashlib
from pathlib import Path
import pymupdf


def main(source, out):
    with pymupdf.open(source) as doc:
        page = doc[80]
        assert "Figure 2.58" in page.get_text()
        paths = page.get_drawings()
    rows = []
    for panel, left in [("testosterone_appearance",117),("androsterone_disappearance",338)]:
        vertical, = [d["rect"] for d in paths if d["color"]==(0,0,0) and abs(d["rect"].x0-left)<1
                     and d["rect"].width<1 and 107<d["rect"].height<111]
        horizontal, = [d["rect"] for d in paths if d["color"]==(0,0,0) and abs(d["rect"].x0-left)<1
                       and d["rect"].height<1 and 160<d["rect"].width<166]
        for hour in (24,48,96):
            midpoint = horizontal.x0 + horizontal.width*hour/100
            values = {}
            for drawing in paths:
                rect = drawing["rect"]
                x = (rect.x0+rect.x1)/2
                if drawing["type"]!="f" or abs(x-midpoint)>1.5 or not 2.5<rect.width<5:
                    continue
                fill = drawing["fill"]
                if fill is None:
                    continue
                if fill[2]-fill[0]>.7:
                    group="Wwox"
                elif .65<fill[0]<.73 and max(fill)-min(fill)<.04:
                    group="mock"
                else:
                    continue
                assert group not in values
                values[group]=100*(vertical.y1-(rect.y0+rect.y1)/2)/vertical.height
            assert set(values)=={"Wwox","mock"}
            rows.append([panel,hour,round(values["Wwox"]-values["mock"],1)])
    with (out/"figure_contrasts.tsv").open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow(["endpoint","hour","Wwox_minus_mock_approx_pp"])
        writer.writerows(rows)
    print("Source SHA256", hashlib.sha256(source.read_bytes()).hexdigest())


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("source",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    main(a.source,a.out)
