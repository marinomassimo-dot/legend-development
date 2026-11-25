"""Receipts for ADV-276 six newly held papers (2026-11-25). Usage, from the repository root: python3 <this file> OUTDIR"""
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = '/home/desktop/legend-development'
LEDGER = 'disease-models/wwox/registries/fulltext_read_receipts.jsonl'
OUT = ('disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/'
       'adv276c_six_newly_held_sci_20261125/RESULT_ADV276_SIX_NEWLY_HELD_SCI_20261125.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
F = 'files/fulltext/'
ROWS = {
    '27845895': (F + 'PMID27845895_ADV272_PMC_r2.xml', 'inadequate_prior_coverage', "reader plus one blind delegate (sonnet, high): " + 'Results, Discussion, Methods, legends of Figs 2, 9, 10, whole-file search for tests and p values, Figs 2 and 10 as images; supplementary figures and videos and Figs 1, 3 to 9 images not opened.'),
    '39178853': (F + 'PMID39178853_ADV272_PMC_r2.xml', 'inadequate_prior_coverage', "reader plus one blind delegate (sonnet, high): " + 'snRNA-seq Results, T3 and animal Methods, Limitations, searches for cholesterol and sterol; figures and supplements not opened here.'),
    '27641496': (F + 'PMID27641496_ADV272_PMC_r2.xml', 'inadequate_prior_coverage', "reader plus one blind delegate (sonnet, high): " + 'Animals, Statistics, Discussion, whole-file search for limitation; Supplemental Procedures not in the file.'),
    '33363507': (F + 'PMID33363507_ADV272_PMC_r2.xml', 'inadequate_prior_coverage', "reader plus one blind delegate (sonnet, high): " + 'Conclusion, glycolysis-inhibition section, captions of Figures 1 to 5 (images not opened).'),
    '33854788': (F + 'PMID33854788_ADV272_PMC_r2.xml', 'inadequate_prior_coverage', "reader plus one blind delegate (sonnet, high): " + 'Results and Discussion on WWOX, supplement Table S3 row and Methods text, reference entries 10, 11, 32, 33; Fig 2F image not opened.'),
    '34210081': (F + 'PMID34210081_ADV272_PMC_r2.xml', 'inadequate_prior_coverage', "reader plus one blind delegate (sonnet, high): " + 'fly and metabolism paragraphs, reference entries 34 to 38.'),
}


def latest(pmid):
    last = None
    for line in open(LEDGER):
        row = json.loads(line)
        if row.get('study_id', {}).get('pmid') == pmid:
            last = row
    return last


now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
for pmid, (rel, reason, basis) in ROWS.items():
    prev = latest(pmid)
    receipt = dict(
        analysis_at=now[:16] + 'Z', analysis_time_precision='minute', coverage=dict(BASE), event_at=now,
        event_id='FTR-20261125-%s-01' % pmid, evidence_basis=['coverage_map', basis],
        evidence_depth='queried_not_full_read', outputs=[OUT], record_kind='contemporaneous_receipt',
        reread_reason=reason if prev else 'first_read',
        source_fingerprint=hashlib.sha256(open('%s/%s' % (ROOT, rel), 'rb').read()).hexdigest(),
        source_kind='fulltext_local', source_locator=rel,
        study_id=prev['study_id'] if prev else {'pmid': pmid, 'doi': '10.1111/j.1750-3639.2010.00443.x'},
        workflow='SCI ADV-276 six newly held papers (not a complete read)', prior_receipt=prev['event_id'] if prev else None)
    Path(sys.argv[1], 'RECEIPT_ADV276C_%s_SCI_20261125.json' % pmid).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(pmid, prev['event_id'] if prev else None, '->', receipt['event_id'])
