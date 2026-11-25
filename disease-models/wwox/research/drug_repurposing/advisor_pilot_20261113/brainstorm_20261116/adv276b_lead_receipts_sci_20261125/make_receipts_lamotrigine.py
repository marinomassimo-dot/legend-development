"""Receipts for the 2026-11-25 re-check of the three lamotrigine case records. Usage: ... OUTDIR"""
import hashlib, json, sys, time
from pathlib import Path

ROOT = '/home/desktop/legend-development'
LEDGER = 'disease-models/wwox/registries/fulltext_read_receipts.jsonl'
OUT = 'disease-models/wwox/research/drug_repurposing/continuous_compounds/lamotrigine/clinical_review.md'
PAP = {
    '24456803': ('files/fulltext/PMID24456803_AbdelSalam2014_PMC.xml',
                 'Targeted: Results family paragraphs on both affected relatives and the variant; searches for lamotrigine, valproate and treatment.'),
    '31353122': ('files/fulltext/PMID31353122_Mori2019_IR.txt',
                 'Targeted: case report, molecular genetic analysis and the genetic part of the Discussion.'),
    '35792847': ('files/fulltext/PMID35792847_AlBaradie2022_JLE.pdf',
                 'Targeted: the case narratives of one family, Table 2 genetic results, Table 3 rows of the first families and of the familial report; lamotrigine searches.'),
}


def latest(pmid):
    last = None
    for line in open(LEDGER):
        row = json.loads(line)
        if row.get('study_id', {}).get('pmid') == pmid:
            last = row
    return last


now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
for pmid, (rel, basis) in PAP.items():
    prev = latest(pmid)
    coverage = {k: 'not_read' for k in ('abstract', 'introduction', 'methods', 'results', 'tables', 'discussion',
                                        'limitations', 'supplementary', 'references')}
    coverage['figures'] = 'captions_only'
    receipt = dict(
        analysis_at=now[:16] + 'Z', analysis_time_precision='minute', coverage=coverage, event_at=now,
        event_id='FTR-20261125-%s-01' % pmid, evidence_basis=['coverage_map', basis], evidence_depth='queried_not_full_read',
        outputs=[OUT], prior_receipt=prev['event_id'], record_kind='contemporaneous_receipt',
        reread_reason='adversarial_reanalysis',
        source_fingerprint=hashlib.sha256(open('%s/%s' % (ROOT, rel), 'rb').read()).hexdigest(),
        source_kind='fulltext_local', source_locator=rel, study_id=prev['study_id'],
        workflow='SCI ADV-276 continued: lamotrigine port re-check (not a complete read)')
    Path(sys.argv[1], 'RECEIPT_LTG_%s_SCI_20261125.json' % pmid).write_text(json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(pmid, prev['event_id'], '->', receipt['event_id'])
