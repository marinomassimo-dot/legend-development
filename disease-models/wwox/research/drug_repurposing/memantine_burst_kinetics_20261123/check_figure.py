"""Cross-check reimplemented steady dose responses against the fitted green curves in Fig. 3."""
import argparse
import hashlib
from pathlib import Path

import numpy as np
import pymupdf

from kinetic import constant_rate

WINDOWS = [(3,12),(82,89),(122,129),(162,169),(200,208),(241,246),(279,285),(583,595)]


def level(pixels, lo, hi):
    r,g,b = pixels[39:,lo:hi].transpose(2,0,1)
    green = (g-r>65) & (g-b>65) & (r<150)
    columns = [np.median(np.where(col)[0])+39 for col in green.T if col.any()]
    if not columns:
        raise ValueError("Selected window contains no fitted curve")
    return np.median(columns)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper",type=Path)
    pdf = parser.parse_args().paper
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != "9c1143e352151d149a0978e0fa5b128ed6fd91ecc1e3b4bf990fd92a87d097ba":
        raise ValueError("Expected the archived publisher PDF")
    print("panel\tCa_uM\tmemantine_uM\tgraph_fit_residual\tcomputed_steady_residual\tabs_gap_pp")
    with pymupdf.open(pdf) as paper:
        for panel, calcium,y0,y1 in (("3C",0,274,385),("3E",10,462,565)):
            im=paper[5].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(275,y0,483,y1))
            pixels=np.frombuffer(im.samples,np.uint8).reshape((im.height,im.width,3)).astype(int)
            vals=np.array([level(pixels,*w) for w in WINDOWS])
            graphical=(vals[2:-1]-vals[0])/((vals[1]+vals[-1])/2-vals[0])
            for mem,actual in zip((.1,.5,2,10,50),graphical,strict=True):
                predicted=constant_rate(mem,calcium)/constant_rate(0.,calcium)
                print(panel,calcium,mem,f"{actual:.5f}",f"{predicted:.5f}",f"{100*abs(predicted-actual):.2f}",sep="\t")


if __name__=="__main__":
    main()
