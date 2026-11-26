"""Receipts for ADV-292, increment 1 (2026-11-26). Usage, from the repository root: python3 <this file> OUTDIR"""
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
       'adv292_next_held_partials_sci_20261126/RESULT_ADV292_INC1_SCI_20261126.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
TAIL = ' Classes left not_read here were not re-read in this event.'
BLIND = ' blind delegate (sonnet, high) on the pivotal items.'
ROWS = {
    '39216838': ('files/fulltext/PMID39216838_Wang2024_PMC11457296.xml', ['supplementary'],
                 'reader: the supplementary docx (S1 to S7 images), the 17-page uncropped-blot PDF and three xlsx workbooks '
                 '(variants and prediction scores, primers, F values) opened and parsed; the three main-text figures were '
                 'not re-read, so figures stays not_read;' + BLIND),
    '40485335': ('files/fulltext/PMID40485335_Shah2025_PMC12146831.xml', ['figures', 'supplementary'],
                 'reader: seven main figure images and four supplementary TIFF images opened;' + BLIND),
    '41178115': ('files/fulltext/PMID41178115_Fu2025_PMC12679549.xml', ['supplementary'],
                 'reader: the 18-page supplementary PDF (supplementary figures with legends, uncropped blots, primer table) '
                 'read; one main figure (Fig 5) opened after the blind report, the other main figure images not re-read;' + BLIND),
    '42268630': ('files/fulltext/PMID42268630_Frick2026_PMC13251787.xml', ['supplementary'],
                 'reader: the statistics workbook (one sheet, 125 rows) parsed in full and checked against the text and legends;' + BLIND),
    '41664646': ('files/fulltext/PMID41664646_Ahuja2026_imec_VoR.pdf', ['figures'],
                 'reader: the five main figure pages opened as images and the Results, Methods and Discussion statements of '
                 'the sentence checked; no supplementary information is held, so supplementary stays not_read;' + BLIND),
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
        event_id='FTR-20261126-%s-01' % key, evidence_basis=['coverage_map', basis + TAIL],
        evidence_depth='queried_not_full_read', outputs=[OUT], record_kind='contemporaneous_receipt',
        reread_reason='inadequate_prior_coverage',
        source_fingerprint=hashlib.sha256(open('%s/%s' % (ROOT, rel), 'rb').read()).hexdigest(),
        source_kind='fulltext_local', source_locator=rel, study_id=prev['study_id'],
        workflow='SCI ADV-292 corrected ten held partials, increment 1 (not a complete read)', prior_receipt=prev['event_id'])
    Path(sys.argv[1], 'RECEIPT_ADV292_%s_SCI_20261126.json' % key).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(key, prev['event_id'], prev.get('evidence_depth'), '->', receipt['event_id'], done)
