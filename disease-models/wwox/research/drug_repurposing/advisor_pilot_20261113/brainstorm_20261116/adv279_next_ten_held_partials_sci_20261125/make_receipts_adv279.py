"""Receipts for ADV-279, increment 1 (2026-11-25). Usage, from the repository root: python3 <this file> OUTDIR"""
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
       'adv279_next_ten_held_partials_sci_20261125/RESULT_ADV279_INC1_SCI_20261125.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
F = 'files/fulltext/'
TAIL = ' Classes left not_read here were not re-read in this event.'
ROWS = {
    '33914734': (F + 'PMID33914734_Gersing2021_PMC8084241.xml', ['supplementary'],
                 'reader: supplementary figures S1 to S8 opened as images, S1 Dataset workbook read and its frequencies set '
                 'against the main figures, response-to-reviewers document read in full; blind delegate (sonnet, high) on the activity statement.'),
    '37781246': (F + 'PMID37781246_KaluzinskaKolat2023_PMC.xml', ['figures'],
                 'reader: the five main figure images opened; supplementary workbooks Table 2 and Table 4 queried; '
                 'blind delegate (sonnet, high) on the two driver genes.'),
    '39769031': (F + 'PMID39769031_RicoMolina2024_PMC_r2.xml', ['supplementary'],
                 'reader: all 47 supplement pages looked at (spectra and chromatograms at page-thumbnail scale, not '
                 're-analysed), dose-response pages read; the zip holds the same PDF; Table 2 and assay Methods re-read.'),
    '42875792': (F + 'PMID42875792_RathanKumar2026_PMC13670827.xml', ['supplementary'],
                 'reader: Supplementary Materials 1 to 5 opened as images, the unedited-blot page examined at native raster '
                 'resolution with a per-lane screening measure, the GO workbook summarised sheet by sheet (all eight sheets); '
                 'blind delegate (sonnet, high) on the blot and the late-window images.'),
    '28749468': (F + 'PMID28749468_Janczar2017_PMC.xml', ['supplementary'],
                 'reader: the nine supplementary figures and the legend document read; blind delegate (sonnet, high) on '
                 'the PERK panel and the time label of Supplementary Figure 3.'),
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
        workflow='SCI ADV-279 next ten held partials, increment 1 (not a complete read)', prior_receipt=prev['event_id'])
    Path(sys.argv[1], 'RECEIPT_ADV279_%s_SCI_20261125.json' % pmid).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(pmid, prev['event_id'], '->', receipt['event_id'], done)
