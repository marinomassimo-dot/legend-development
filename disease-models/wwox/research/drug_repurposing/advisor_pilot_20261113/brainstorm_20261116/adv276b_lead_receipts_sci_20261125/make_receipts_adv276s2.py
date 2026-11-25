"""Receipts for ADV-276 step 2 batch 1 (2026-11-25). Usage, from the repository root: python3 <this file> OUTDIR"""
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = '/home/desktop/legend-development'
LEDGER = 'disease-models/wwox/registries/fulltext_read_receipts.jsonl'
OUT = ('disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/'
       'adv276b_lead_receipts_sci_20261125/RESULT_ADV276_STEP2_BATCH1_SCI_20261125.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
F = 'files/fulltext/'
ROWS = {
    '25686832': (F + 'PMID25686832_ADV272_PMC_r2.xml', 'adversarial_reanalysis',
                 'Figure 5 legend, heterozygous-mouse passages of Results and Discussion; searches of the supplement text for heterozyg and Wwox.'),
    '35339181': (F + 'PMID35339181_ADV272_PMC_r2.xml', 'adversarial_reanalysis',
                 'Abstract, Figure 1 legend, Table 1 and its footnote, the microinfusion passages.'),
    '37907746': (F + 'PMID37907746_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 'Abstract, introduction passages, animal and viral-vector Methods, result passages on KHK, NOX4 and knockdown; supplement Methods on AAV timing and primary microglia isolation.'),
    '39505840': (F + 'PMID39505840_ADV272_PMC_r2.xml', 'adversarial_reanalysis',
                 'Abstract and the result passages on antagonist timing, status epilepticus phases and chronic seizures.'),
    '41007296': (F + 'PMID41007296_ADV272_PMC_r2.xml', 'adversarial_reanalysis',
                 'Results 3.1 and 3.6 (basal breast cancer and glioblastoma), their Cox passages, figure legends in part. Figures and supplement not opened.'),
    '42171828': (F + 'PMID42171828_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 'Result sections on hypoxia and on dual time-dependent action (passages), reference 17 identified.'),
    '42260675': (F + 'PMID42260675_ADV272_PMC_r2.xml', 'adversarial_reanalysis',
                 'Abstract, objective, outcome and analysis passages of the protocol.'),
    '21029239': (F + 'PMID21029239_Yeh2010_PMC8094320_pmcpage_20261125.html', 'first_read',
                 'PMC article page: abstract, introduction, behaviour and survival results, Figure 3 legend, discussion, dose and animal statements.'),
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
        workflow='SCI ADV-276 step 2 batch 1 (not a complete read)', prior_receipt=prev['event_id'] if prev else None)
    Path(sys.argv[1], 'RECEIPT_ADV276S2_%s_SCI_20261125.json' % pmid).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(pmid, prev['event_id'] if prev else None, '->', receipt['event_id'])
