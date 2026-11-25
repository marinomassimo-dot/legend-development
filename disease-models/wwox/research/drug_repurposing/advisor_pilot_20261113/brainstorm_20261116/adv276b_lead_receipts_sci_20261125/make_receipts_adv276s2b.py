"""Receipts for ADV-276 step 2 batch 2 (2026-11-25). Usage, from the repository root: python3 <this file> OUTDIR"""
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = '/home/desktop/legend-development'
LEDGER = 'disease-models/wwox/registries/fulltext_read_receipts.jsonl'
OUT = ('disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/'
       'adv276b_lead_receipts_sci_20261125/RESULT_ADV276_STEP2_BATCH2_SCI_20261125.md')
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')
F = 'files/fulltext/'
ROWS = {
    '40140574': (F + 'PMID40140574_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'Fig 1c and 1d source-data sheets, ED3e sheet, ED8 legends and blot, Supplementary Fig 1 page 22, Reporting Summary; Methods passages. Table zips not opened.'),
    '40674686': (F + 'PMID40674686_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'Figure 7 legend and result passages re-checked against the consumer line; workbook not re-derived.'),
    '40925365': (F + 'PMID40925365_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'neutral extraction of cell-number and fitting statements, Fig S3E,F, figure and table list; no judgement made.'),
    '41423560': (F + 'PMID41423560_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'Methods on Pdgfra-CreER and Plp-CreERT, Supplementary Fig S5G legend, source-data sheets (Figure 1D, 1E, 2A, 5, S5G), peer-review file; Supplementary Data 1 and 2 listed only.'),
    '41496652': (F + 'PMID41496652_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'abstract, Fig 1F, 4D, 4K and 7E,F as images, Methods, supplement legends; supplementary figures S1 to S7 (EMF) not rendered.'),
    '42011973': (F + 'PMID42011973_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'full letter text, Fig 2 image, supplement Methods (MEA recordings and drug application, statistics); Figs 1 and 3 not viewed.'),
    '42308317': (F + 'PMID42308317_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'Fig 2 and supplementary S3A as images, Methods, Discussion passages, searches for MCT, KATP and labelled lactate; peer-review file not read.'),
    '42587153': (F + 'PMID42587153_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'Methods on clone induction, Fig 2 source-data sheet, CloneSeq passages; most main-figure and ED images not opened.'),
    '42928124': (F + 'PMID42928124_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'Fig 1B and legends of Figures 2 to 8, searches for uptake, surface labelling and HDAC or WWOX; supplementary images not opened.'),
    '43047766': (F + 'PMID43047766_ADV272_PMC_r2.xml', 'inadequate_prior_coverage',
                 "targeted reading by two blind delegates (sonnet, high) plus the reader's own checks of the pivotal items: " + 'Methods (slice, CHO, HEK sections), Supplementary_file_1 statistics, Fig 1 and Fig 4 pages as images.'),
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
        workflow='SCI ADV-276 step 2 batch 2 (not a complete read)', prior_receipt=prev['event_id'] if prev else None)
    Path(sys.argv[1], 'RECEIPT_ADV276S2B_%s_SCI_20261125.json' % pmid).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(pmid, prev['event_id'] if prev else None, '->', receipt['event_id'])
