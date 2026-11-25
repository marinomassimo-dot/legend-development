"""Receipts for ADV-280, increment 1 (2026-11-25). Usage, from the repository root: python3 <this file> OUTDIR"""
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
       'adv280_next_ten_held_partials_sci_20261125/RESULT_ADV280_INC1_SCI_20261125.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
TAIL = ' Classes left not_read here were not re-read in this event.'
BLIND = ' blind delegate (sonnet, high) on the pivotal items.'
ROWS = {
    '36926521': ('files/fulltext/PMID36926521_Colin2023_PMC.xml', ['figures', 'supplementary'],
                 'reader: all five main figures and five supplementary figure images opened; legends, clinical text '
                 'and supplementary methods read; pixel profile of the western strip computed;' + BLIND),
    '37804316': ('files/fulltext/PMC10907083_PMID37804316_europepmc_fulltext_2026-10-29.xml', ['figures'],
                 'reader: six figure images opened and 16 supplement pages looked at; three videos not watched, so '
                 'supplementary stays not_read;' + BLIND),
    '41570991': ('files/fulltext/PMID41570991_Bouchez2026_PMC_r2.xml', ['figures', 'supplementary'],
                 'reader: nine figure images and six supplement pages looked at;' + BLIND),
    '41706892': ('files/fulltext/PMC12933080_PMID41706892_europepmc_fulltext_2026-10-29.xml',
                 ['figures', 'supplementary'],
                 'reader: four figure images and six supplement pages looked at; protein dataset parsed and the '
                 'differential counts recomputed;' + BLIND),
    'PPR1015434': ('files/fulltext/PPR1015434_LucasClarke2025_EPMC.xml', ['supplementary'],
                   'reader: nine supplement figure pages looked at; seven supplementary tables parsed, counts '
                   'compared with the text, large sheets sampled not read row by row;' + BLIND),
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
        workflow='SCI ADV-280 next ten held partials, increment 1 (not a complete read)', prior_receipt=prev['event_id'])
    Path(sys.argv[1], 'RECEIPT_ADV280_%s_SCI_20261125.json' % key).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(key, prev['event_id'], prev.get('evidence_depth'), '->', receipt['event_id'], done)
