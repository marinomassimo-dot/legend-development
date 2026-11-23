"""Recalculate the pediatric CSF and mouse CA1 contrasts from two published sources."""
import csv
from hashlib import sha256
from pathlib import Path
import re
from statistics import median
import subprocess
import sys
import xml.etree.ElementTree as ET


def write_output(path, header, rows):
    with path.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(header)
        writer.writerows(rows)


def cerebrospinal_fluid(xml, output):
    root = ET.parse(xml)
    rows = []
    table = root.find(".//table-wrap[@id='pone.0120972.t003']")
    for row in table.findall('.//tbody/tr'):
        drug, exposed, comparator, published_p = [''.join(cell.itertext()).strip() for cell in row]
        a, b = [float(text.split()[0]) for text in (exposed, comparator)]
        rows.append((drug, a, b, round(a - b, 3), round(100 * (a / b - 1), 2), published_p.rstrip('*')))
    assert len(rows) == 4
    write_output(output / 'csf.tsv', ['vitamer','treated_median_nM','comparison_median_nM','difference_nM','relative_median_difference_pct','published_p'], rows)
    # Derive only cells uniquely implied by the three reported marginal counts.
    paragraphs = [' '.join(''.join(p.itertext()).split()) for p in root.findall('.//body//p')]
    paragraph, = [p for p in paragraphs if '9/51' in p]
    assert re.search(r'9/51.*concentrations of PL were below.*PLP in CSF was decreased in seven.*Three of these children showed decreased concentrations of both', paragraph)
    total, pl, plp, both = 51, 9, 7, 3
    cells = [('both',both),('PL only',pl-both),('PLP only',plp-both),('neither',total-pl-plp+both)]
    assert sum(v for _,v in cells) == total
    write_output(output / 'thresholds.tsv',['below_observed_reference_minimum','children','denominator','percent'],[(name,v,total,round(100*v/total,2)) for name,v in cells])


def synaptic_currents(image, output):
    # Coordinates are native pixels in the original 411 x 462 image, Fig. 4A2.
    # x=303 at the 0,1,2 y-axis ticks. Use several x positions away from error bars.
    assert sha256(image.read_bytes()).hexdigest() == 'fc600ac929cbc61687410573ccceac270d1ac35c6fdd4f63f51b2c05d18e094d'
    pixels = subprocess.check_output(['convert',str(image),'-colorspace','gray','-depth','8','gray:-'])
    assert len(pixels) == 411 * 462
    def dark(x,y):
        return pixels[y*411+x] < 125
    ticks = [y for y in range(75,130) if dark(303,y)]
    assert ticks == [79,103,127]
    scale = median([b-a for a,b in zip(ticks,ticks[1:])])
    rows = []
    for group, xs in [('WT',[321,322,324]),('Gad2_KO',[369,372,383])]:
        tops = [next(y for y in range(53,115) if dark(x,y)) for x in xs]
        top = median(tops)
        baseline = 128   # bar base, within one pixel of adjacent baseline tick
        rows.append((group,top,baseline,scale,round((baseline-top)/scale,3)))
    write_output(output / 'evoked.tsv',['group','top_pixel_y','base_pixel_y','pixels_per_normalized_unit','normalized_terminal_amplitude'],rows)


if __name__ == '__main__':
    source = Path(sys.argv[1])
    output = Path(__file__).resolve().parent
    cerebrospinal_fluid(source / 'albersen.xml',output)
    synaptic_currents(source / 'tian_fig4.jpg',output)
