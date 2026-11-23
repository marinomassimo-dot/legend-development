"""Recalculate group-level plasma isotope outcomes from Böckmann et al., supplement 1."""
from collections import defaultdict
import csv
from pathlib import Path
from statistics import median
import sys
import xml.etree.ElementTree as ET
import zipfile

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def read(source):
    with zipfile.ZipFile(source) as doc:
        root = ET.fromstring(doc.read('word/document.xml'))
    groups = defaultdict(lambda: defaultdict(dict))
    for row in root.findall('.//w:tbl/w:tr', NS):
        cells = [''.join(n.text or '' for n in c.findall('.//w:t', NS)).strip()
                 for c in row.findall('w:tc', NS)]
        identifier, label, time, _, d9_choline, native_pc, d9_pc = cells
        if not identifier.isdigit():
            continue
        if label:
            current_group = label
        sample = groups[current_group][identifier]
        assert int(time) not in sample
        sample[int(time)] = (float(d9_choline), float(native_pc), float(d9_pc))
    assert len(groups) == 4 and all(len(group)==8 for group in groups.values())
    return groups

def auc(points):
    values = sorted(points.items())
    return sum((t1-t0)*(c0+c1)/2 for (t0,c0),(t1,c1) in zip(values,values[1:]))

def calculate(source, output):
    rows = []
    for group, infants in read(source).items():
        by_time = defaultdict(list)
        summaries = []
        observed_60 = median(sample[60][2] for sample in infants.values() if 60 in sample)
        for sample in infants.values():
            assert set(sample) in ({1,24},{12,60})
            conc = {0:0,60:0}
            percent_to_native = conc.copy()
            percent_to_total = conc.copy()
            for hour, (free, native, labelled) in sample.items():
                conc[hour] = labelled
                percent_to_native[hour] = 100*labelled/native
                percent_to_total[hour] = 100*labelled/(native+labelled)
                by_time[hour].append((free,labelled))
            sensitivity = conc.copy()
            if 60 not in sample:
                sensitivity[60] = observed_60
            summaries.append((min(sample),auc(conc),auc(percent_to_native),auc(percent_to_total),auc(sensitivity)))
        assert all(len(by_time[h]) == 4 for h in [1,12,24,60])
        def med_at(h,i):
            return median(v[i] for v in by_time[h])
        def med_auc(idx,schedule=None):
            return median(v[idx] for v in summaries if schedule is None or v[0]==schedule)
        rows.append([group,len(infants),med_at(1,0),med_at(12,1),med_at(60,1),
                     med_auc(1),med_auc(2),med_auc(3),med_auc(2,1),med_auc(2,12),med_auc(4)])
    with output.open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['supplement','infants','D9_free_1h_uM','D9_PC_12h_uM','D9_PC_60h_uM',
                         'D9_PC_AUC_uM_h','D9_to_native_PC_AUC_pct_h','D9_to_total_PC_AUC_pct_h',
                         'D9_to_native_AUC_1_24h_group','D9_to_native_AUC_12_60h_group','D9_PC_AUC_alternate_60h_uM_h'])
        for row in rows:
            writer.writerow([row[0], row[1], *[round(v,3) for v in row[2:]]])

if __name__ == '__main__':
    calculate(Path(sys.argv[1]),Path(__file__).with_name('precursors.tsv'))
