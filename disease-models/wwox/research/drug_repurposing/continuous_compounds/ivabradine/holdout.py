"""Reproduce contrasts from Wu's FDA nonclinical review, Che et al., and the rat exposure audit."""
import csv
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


def data_rows(pdf, xml):
    report = ' '.join(subprocess.check_output(['pdftotext','-layout',str(pdf),'-']).decode().split())
    hcn1 = re.search(r'IC\s*50 values of ([\d.]+) \+ [\d.]+ µM \(n=7\) and ([\d.]+) ± [\d.]+ µM \(n=6\)', report)
    assert hcn1
    text = ' '.join(''.join(ET.parse(xml).getroot().find('.//body').itertext()).split())
    human = re.search(r'\(IC50\) of ([\d.]+) ± [\d.]+ μM', text)
    rods = re.search(r'full block at 30 [μµ]M and IC50 of ([\d.]+) [μµ]M',report)
    assert human and rods
    # The FDA report explicitly orders the pairs HCN4 then HCN2.
    sc = re.search(r'IC50 of S16257-2: ([\d.]+) ± [\d.]+ μM and ([\d.]+) ± [\d.]+ μM, respectively; IC50 of S18982-1: ([\d.]+) ± [\d.]+ μM and ([\d.]+) ± [\d.]+ μM',report)
    assert sc
    parent_mouse, metabolite_mouse = map(float,hcn1.groups())
    parent4,parent2,metabolite4,metabolite2 = map(float,sc.groups())
    parent_brain = 0.0047  # µM; 2 h untreated-by-efflux-inhibitor arm in Iacone, Fig. 1D
    for target,parent,met in [('recombinant_mouse_HCN1_NP08442',parent_mouse,metabolite_mouse),
                              ('recombinant_human_HCN2_NP07905',parent2,metabolite2),
                              ('recombinant_human_HCN4_NP07905',parent4,metabolite4),
                              ('native_mouse_retinal_rod_NP15864',float(rods.group(1)),None),
                              ('recombinant_human_HCN1_figure_1B',float(human.group(1)),None)]:
        yield target,parent,met if met is not None else 'NA',round(met/parent,3) if met is not None else 'NA',round(parent/parent_brain,1)


if __name__ == '__main__':
    raw = Path(sys.argv[1])
    with Path(__file__).with_name('holdout.tsv').open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['assay','parent_half_block_uM','S18982_half_block_uM','metabolite_to_parent_half_block','parent_half_block_over_rat_2h_free_brain'])
        writer.writerows(data_rows(raw/'fda_pharm.pdf',raw/'human_hcn1.xml'))
