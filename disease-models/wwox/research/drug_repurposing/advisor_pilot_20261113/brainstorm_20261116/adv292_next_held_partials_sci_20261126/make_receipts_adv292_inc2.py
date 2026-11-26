"""Receipts for ADV-292, increment 2 (2026-11-26). Usage, from the repository root: python3 <this file> OUTDIR"""
import hashlib
import json
import sys
import time
from pathlib import Path

if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__)
    raise SystemExit(0)

ROOT = '/home/desktop/legend-development'
LEDGER = 'disease-models/wwox/registries/fulltext_read_receipts.jsonl'
OUT = ('disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/'
       'adv292_next_held_partials_sci_20261126/RESULT_ADV292_INC2_SCI_20261126.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
TAIL = ' Classes left not_read here were not re-read in this event.'
BLIND = ' blind delegate (sonnet, high) on the pivotal items.'
ROWS = {
    '39923817': ('files/fulltext/PMID39923817_ADV272_PMC13078857_epmc_20261125.xml',
                 ['abstract', 'results', 'tables', 'discussion'],
                 'reader: Abstract, Results, Discussion and the figure legends read from the article XML, and the one in-article table (Key Resources) read; '
                 'no image files and no supplement are held, so figures, supplementary and limitations stay not_read; Methods read only for the assay and animal details;' + BLIND),
    '37946251': ('files/fulltext/PMID37946251_Pagnamenta2023_PMC.xml', ['supplementary', 'tables'],
                 'reader: Table 1 image opened; Additional file 3 read through the derived row extract of the WWOX case (not row by row) and its sharedStrings searched; '
                 'Additional file 1 (docx) not opened;' + BLIND),
    '40858643': ('files/fulltext/PMID40858643_Hamanaka2025_PMC.xml', ['supplementary', 'tables'],
                 'reader: Table 2 read; Supplementary Data 1 and 2 read through the derived row extract of the case (not row by row); the 23-page supplementary PDF searched for the gene and case, no hit, '
                 'pages not looked at;' + BLIND),
    '26419537': ('files/fulltext/PMID26419537_Chen2015_PMC_r2.xml', ['results', 'figures', 'supplementary'],
                 'reader: Results and Discussion read; of four main figures only Fig 2 opened; of the 18 supplementary files only Table S1 (read in full) and Fig S1 (opened) were looked at;' + BLIND),
    '31781019': ('files/fulltext/PMID31781019_Kam2019_PMC_r2.xml', ['results', 'figures', 'supplementary'],
                 'reader: Methods and Results read; of thirteen figures only Fig 11 opened; Supplemental Table 1 (per-mouse spike counts, 55 session rows) parsed in full and the ethosuximide direction recomputed;' + BLIND),
}
PREPRINT_DOI = '10.1101/2025.05.01.651195'


def latest(key):
    last = None
    for line in open(LEDGER):
        row = json.loads(line)
        sid = row.get('study_id', {})
        hit = sid.get('doi') == PREPRINT_DOI if key == 'PPR1015434' else sid.get('pmid') == key
        if hit:
            last = row
    return last


now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
for key, (rel, done, basis) in ROWS.items():
    prev = latest(key)
    coverage = dict(BASE)
    for name in done:
        coverage[name] = 'read'
    receipt = dict(
        analysis_at=now[:16] + 'Z', analysis_time_precision='minute', coverage=coverage, event_at=now,
        event_id='FTR-20261126-%s-02' % key, evidence_basis=['coverage_map', basis + TAIL],
        evidence_depth='queried_not_full_read', outputs=[OUT], record_kind='contemporaneous_receipt',
        reread_reason='inadequate_prior_coverage',
        source_fingerprint=hashlib.sha256(open('%s/%s' % (ROOT, rel), 'rb').read()).hexdigest(),
        source_kind='fulltext_local', source_locator=rel, study_id=prev['study_id'],
        workflow='SCI ADV-292 corrected ten held partials, increment 2 (not a complete read)', prior_receipt=prev['event_id'])
    Path(sys.argv[1], 'RECEIPT_ADV292_INC2_%s_SCI_20261126.json' % key).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(key, prev['event_id'], prev.get('evidence_depth'), '->', receipt['event_id'], done)
