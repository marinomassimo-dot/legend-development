"""Receipts for ADV-279, increment 2 (2026-11-25). Usage, from the repository root: python3 <this file> OUTDIR"""
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
       'adv279_next_ten_held_partials_sci_20261125/RESULT_ADV279_INC2_SCI_20261125.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
F = 'files/fulltext/'
TAIL = ' Classes left not_read here were not re-read in this event.'
ROWS = {
    '30266908': (F + 'PMID30266908_Guiberson2018_PMC6162227.xml', ['supplementary'],
                 'reader: all 28 pages of the supplementary information looked at (page-thumbnail scale, the osmolyte '
                 'page large), peer-review file consulted; blind delegate (sonnet, high) on the two sorbitol panels.'),
    '34359949': (F + 'PMID34359949_Hsu2021_PMC.xml', ['figures'],
                 'reader: the three figure images opened; body text queried for the direct-binding wording; blind '
                 'delegate (sonnet, high) on that wording.'),
    '37248434': (F + 'PMID37248434_Taouis2023_PMC.xml', ['figures'],
                 'reader: the six figure images opened, printed densities of Figures 1B and 4A recomputed; blind '
                 'delegate (sonnet, high) on the Y33R densities.'),
    '37275776': (F + 'PMID37275776_Colombo2023_PMC_r2.xml', ['supplementary'],
                 'reader: all 15 supplement pages looked at, the dose-response page and its fit table large, Figure 7 '
                 'image re-opened; blind delegate (sonnet, high) on the wild-type half-inhibition value.'),
    '36278433': (F + 'PMID36278433_Guyon2022_PMC_r2.xml', ['figures'],
                 'reader: the six main figure images opened; Figure 6 source-data sheets read and the survival curve '
                 'recomputed; appendix and expanded-view pages looked at by thumbnail, peer-review file searched, other '
                 'source workbooks only listed (supplementary stays not_read); blind delegate (sonnet, high) on the '
                 'survival median and the dose.'),
}


def latest(pmid):
    last = None
    for line in open(LEDGER):
        row = json.loads(line)
        if row.get('study_id', {}).get('pmid') == pmid:
            last = row
    return last


now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
for pmid, (rel, done, basis) in ROWS.items():
    prev = latest(pmid)
    coverage = dict(BASE)
    for name in done:
        coverage[name] = 'read'
    receipt = dict(
        analysis_at=now[:16] + 'Z', analysis_time_precision='minute', coverage=coverage, event_at=now,
        event_id='FTR-20261125-%s-01' % pmid, evidence_basis=['coverage_map', basis + TAIL],
        evidence_depth='queried_not_full_read', outputs=[OUT], record_kind='contemporaneous_receipt',
        reread_reason='inadequate_prior_coverage',
        source_fingerprint=hashlib.sha256(open('%s/%s' % (ROOT, rel), 'rb').read()).hexdigest(),
        source_kind='fulltext_local', source_locator=rel, study_id=prev['study_id'],
        workflow='SCI ADV-279 next ten held partials, increment 2 (not a complete read)', prior_receipt=prev['event_id'])
    Path(sys.argv[1], 'RECEIPT_ADV279_%s_SCI_20261125.json' % pmid).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(pmid, prev['event_id'], '->', receipt['event_id'], done)
