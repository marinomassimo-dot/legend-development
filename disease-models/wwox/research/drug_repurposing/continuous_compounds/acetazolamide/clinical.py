"""Recompute follow-up concentration, outcome denominators and background ASM exposures."""
from pathlib import Path
from statistics import median
import csv
import sys
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent

def contents(element):
    return ' '.join(''.join(element.itertext()).split())

def table_rows(path, table):
    root = ET.parse(path)
    rows = root.findall('.//table-wrap')[table].findall('.//tr')
    return [[contents(c) for c in row] for row in rows]

def summarize_cohort(rows, months):
    return [len(rows),sum(months),median(months),max(months)/sum(months),sum(x>6 for x in months),
            sum(x>=12 for x in months), sum(row[4].casefold()=='seizure‐free' for row in rows)]

def run(files):
    source = files/'deepening_downloads/acetazolamide_loop_20261123'
    chd = table_rows(source/'az-chd2.xml',-1)[1:]
    slc = table_rows(source/'az-slc6a1.xml',-1)[1:]
    chd_months = [12*int(value.split('/')[0])+int(value.split('/')[1]) for value in (r[2] for r in chd)]
    def to_months(text):
        parts=text.split()
        return sum(int(parts[i])*(12 if parts[i+1].startswith('year') else 1) for i in range(0,len(parts),2))
    slc_months = [to_months(row[2]) for row in slc]
    with (HERE/'cohorts.tsv').open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow('cohort cases observed_person_months median_months longest_share observed_gt6m observed_ge12m seizure_free_at_last'.split())
        for label, rows, months in [('CHD2',chd,chd_months),('SLC6A1',slc,slc_months)]:
            writer.writerow([label,*summarize_cohort(rows,months)])
    series=table_rows(files/'fulltext/PMID36779245_Oliver2023_PMC_r2.xml',1)
    meds,=[row[1:] for row in series if row[0].startswith('ASMs trialed')]
    drug_sets=[set(x.replace(',',' ').split()) for x in meds]
    with (HERE/'background.tsv').open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['exposure_ever_listed','patients','denominator'])
        for label, drugs in [('phenobarbital',{'PHB'}),('topiramate',{'TPM'}),('zonisamide',{'ZNS'}),('topiramate_or_zonisamide',{'TPM','ZNS'}),('valproate',{'VPA'})]:
            writer.writerow([label,sum(bool(record&drugs) for record in drug_sets),len(meds)])
if __name__=='__main__':
    run(Path(sys.argv[1]))
