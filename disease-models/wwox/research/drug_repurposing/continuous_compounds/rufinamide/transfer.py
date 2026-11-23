"""Reproduce the WWOX passive-load comparison and Dup15q inactivation contrast."""
import csv
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


class Paragraphs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = None
        self.paragraphs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.parts = []

    def handle_data(self, data):
        if self.parts is not None:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'p' and self.parts is not None:
            self.paragraphs.append(' '.join(''.join(self.parts).split()))
            self.parts = None


def summaries(wwox, dup15):
    root = ET.parse(wwox)
    table = root.find(".//table-wrap[@id='t0005']")
    result = []
    measurements = {}
    for row in table.findall('.//tr'):
        cells = [''.join(cell.itertext()).strip() for cell in row]
        if cells[0] in ('Resting membrane potential','AP Threshold (mV)','AP amplitude','Input resistance (Mohm)'):
            measurements[cells[0]] = [float(v.split()[0].replace('−','-')) for v in cells[1:]]
    for name,i,j in [('PY_WT_vs_KO',0,2),('IN_WT_plus_HT_vs_KO',3,4)]:
        for label,unit in [('AP amplitude','mV'),('Resting membrane potential','mV'),('AP Threshold (mV)','mV'),('Input resistance (Mohm)','MOhm')]:
            values = measurements[label]
            result.append([name,label,unit,values[i],values[j],values[j]-values[i]])
        def proxy(k):
            gap = measurements['AP Threshold (mV)'][k] - measurements['Resting membrane potential'][k]
            return 1000 * gap / measurements['Input resistance (Mohm)'][k]
        result.append([name,'passive_current_proxy_ratio_of_group_means','pA',proxy(i),proxy(j),proxy(j)-proxy(i)])
    html = Paragraphs()
    html.feed(dup15.read_text())
    text, = [p for p in html.paragraphs if 'Dup15q + DMSO V1/2' in p]
    def voltage(group):
        match = re.search(re.escape(group) + r' V1/2 = ([−0-9.]+)',text)
        return float(match.group(1).replace('−','-'))
    ctrl,baseline,drug = map(voltage,['Corr.Control','Dup15q + DMSO','Dup15q + RUF'])
    result.extend([['Dup15q','inactivation midpoint vehicle vs drug','mV',baseline,drug,drug-baseline],
                   ['Dup15q','signed deviation from corrected vehicle','mV',baseline-ctrl,drug-ctrl,drug-baseline],
                   ['Dup15q','absolute deviation from corrected vehicle','mV',abs(baseline-ctrl),abs(drug-ctrl),abs(drug-ctrl)-abs(baseline-ctrl)]])
    return result


if __name__ == '__main__':
    rows = summaries(Path(sys.argv[1]),Path(sys.argv[2]))
    with Path(__file__).with_name('transfer.tsv').open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['comparison','measurement','unit','reference','comparison_group','difference'])
        for *labels,a,b,d in rows:
            writer.writerow([*labels,round(a,3),round(b,3),round(d,3)])
