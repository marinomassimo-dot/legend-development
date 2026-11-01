#!/usr/bin/env python3
"""Verifier items 1 and 2: recompute ratios from the producer's raw ChEMBL rows (relations_qa.tsv, chembl_activity only)
and the occupancy arithmetic. Writes q1_ratios.tsv and q2_occupancy.tsv. Read-only on the producer's files."""
import csv, os
D = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
P = f'{D}/target_first_it15_qa_nmdar_20261101'; O = os.path.dirname(os.path.abspath(__file__))
R = [r for r in csv.DictReader(open(f'{P}/relations_qa.tsv'), delimiter='\t') if r['source'] == 'chembl_activity']
def val(mol, gene, doc, mt='IC50'):
    return sorted({(float(r['value_nM']), r['relation'], r['species'], r['ref'].split(';')[2]) for r in R
                   if r['molecule_chembl_id'] == mol and r['gene'] == gene and r['ref'].split(';')[1] == doc and r['measure_type'] == mt and r['value_nM']})
pairs = [('ifenprodil', 'CHEMBL305187', 'CHEMBL4308825', 'IC50', 'GRIN2A', 'GRIN2B'), ('Ro 25-6981', 'CHEMBL305195', 'CHEMBL4308825', 'IC50', 'GRIN2A', 'GRIN2B'),
         ('Ro 25-6981', 'CHEMBL305195', 'CHEMBL1132364', 'IC50', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'),
         ('d-AP5', 'CHEMBL84612', 'CHEMBL1143579', 'Ki', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'), ('d-AP5', 'CHEMBL84612', 'CHEMBL4024770', 'Ki', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'),
         ('dalzanemdor', 'CHEMBL5095095', 'CHEMBL5131569', 'EC50', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'), ('dalzanemdor', 'CHEMBL5095095', 'CHEMBL6134891', 'EC50', 'GRIN2A', 'GRIN2B'),
         ('ketamine', 'CHEMBL742', 'CHEMBL1759939', 'IC50', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'), ('ketamine', 'CHEMBL742', 'CHEMBL6115009', 'IC50', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'),
         ('MK-801', 'CHEMBL284237', 'CHEMBL6115009', 'IC50', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'), ('memantine', 'CHEMBL807', 'CHEMBL6115009', 'IC50', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B'),
         ('memantine', 'CHEMBL807', 'CHEMBL1146243', 'IC50', 'GRIN1|GRIN2A', 'GRIN1|GRIN2B')]
with open(f'{O}/q1_ratios.tsv', 'w') as f:
    f.write('compound\tdocument\ttype\tGluN2A_nM\tGluN2B_nM\tratio_2A_over_2B\tdirection\tassay_ids\n')
    for n, m, d, mt, ga, gb in pairs:
        a, b = val(m, ga, d, mt), val(m, gb, d, mt)
        if not a or not b: f.write(f'{n}\t{d}\t{mt}\tNOT_FOUND\n'); continue
        ra, rb = a[0][0], b[0][0]
        f.write(f'{n}\t{d}\t{mt}\t{ra:g}\t{rb:g}\t{ra/rb:.3g}\t{"2B more potent" if ra>rb else "2A more potent"}\t{a[0][3]}|{b[0][3]}\n')
print(open(f'{O}/q1_ratios.tsv').read())
# occupancy
with open(f'{O}/q2_occupancy.tsv', 'w') as f:
    f.write('quantity\tvalue\tnote\n')
    occ = lambda c, ic: c / (c + ic)
    f.write(f'ifenprodil 1 uM occupancy GluN2B (IC50 110 nM, Hill 1)\t{occ(1000,110):.4f}\tmatches 90%\n')
    f.write(f'ifenprodil 1 uM occupancy GluN2A (IC50 39,500 nM, Hill 1)\t{occ(1000,39500):.4f}\tmatches 2.5%\n')
    f.write(f'Ro 25-6981 100 nM GluN2B (9 nM)\t{occ(100,9):.4f}\tmatches 92%\n')
    f.write(f'Ro 25-6981 100 nM GluN2A (52,000 nM)\t{occ(100,52000):.4f}\tmatches 0.2%\n')
    f.write('--- producer prediction: dI/I = 0.90 f + 0.025 (1-f) (implicitly Emax = 1 on every GluN2B receptor, no triheteromers)\n')
    for fr in (0.2, 0.5, 0.8):
        f.write(f'producer formula f={fr}\t{0.9*fr+0.025*(1-fr):.3f}\tupper bound only\n')
    f.write('--- restated: dI/I = sum_i f_i * Emax_i * occ_i ; Emax values below are ILLUSTRATIVE (GENERATED), not sourced\n')
    for emax in (1.0, 0.8, 0.6, 0.4):
        for fr in (0.2, 0.5, 0.8):
            f.write(f'Emax_2B={emax} f={fr} (all GluN2B share as diheteromer)\t{emax*0.9*fr+0.025*(1-fr)*1.0:.3f}\tillustrative\n')
print(open(f'{O}/q2_occupancy.tsv').read())
