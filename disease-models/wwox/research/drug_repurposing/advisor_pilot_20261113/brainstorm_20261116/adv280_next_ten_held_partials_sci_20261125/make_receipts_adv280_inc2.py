"""Receipts for ADV-280, increment 2 (2026-11-25). Usage, from the repository root: python3 <this file> OUTDIR"""
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
       'adv280_next_ten_held_partials_sci_20261125/RESULT_ADV280_INC2_SCI_20261125.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
TAIL = ' Classes left not_read here were not re-read in this event.'
BLIND = ' blind delegate (sonnet, high) on the pivotal items.'
ROWS = {
    '35883580': ('files/fulltext/PMID35883580_Liu2022_PMC_r2.xml', ['figures'],
                 'reader: the eight figure images opened in sheets and the yeast and sphere figures enlarged; the three '
                 'supplementary videos not watched (outside the figure class);' + BLIND),
    '38378758': ('files/fulltext/PMID38378758_Clausen2024_PMC10879094.xml', ['supplementary'],
                 'reader: all 24 pages of the supplementary information and the four reporting-summary pages looked at, '
                 'source-data workbook parsed and its two blot images opened, pathogenic-variant table recomputed; '
                 'peer-review file searched, not read in full;' + BLIND),
    '38443647': ('files/fulltext/PMID38443647_Bacq2024_PMC_r2.xml', ['figures'],
                 'reader: the five figure images opened (all schematics); exposure sentences re-read in the text;' + BLIND),
    '38731820': ('files/fulltext/PMID38731820_Poliquin2024_PMC11083348.xml', ['supplementary'],
                 'reader: the four supplementary figure pages opened at 160 dpi (the supplement has no text layer);' + BLIND),
    '38740822': ('files/fulltext/PMID38740822_Gronbaek2024_PMC11091098.xml', ['supplementary'],
                 'reader: 23 supplementary pages and four reporting-summary pages looked at, source-data workbook parsed '
                 'and pathogenic counts recomputed (large sheets not read row by row), embedded blot image opened, '
                 'peer-review file searched with one passage read;' + BLIND),
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
        event_id='FTR-20261125-%s-01' % key, evidence_basis=['coverage_map', basis + TAIL],
        evidence_depth='queried_not_full_read', outputs=[OUT], record_kind='contemporaneous_receipt',
        reread_reason='inadequate_prior_coverage',
        source_fingerprint=hashlib.sha256(open('%s/%s' % (ROOT, rel), 'rb').read()).hexdigest(),
        source_kind='fulltext_local', source_locator=rel, study_id=prev['study_id'],
        workflow='SCI ADV-280 next ten held partials, increment 2 (not a complete read)', prior_receipt=prev['event_id'])
    Path(sys.argv[1], 'RECEIPT_ADV280_%s_SCI_20261125.json' % key).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(key, prev['event_id'], prev.get('evidence_depth'), '->', receipt['event_id'], done)
