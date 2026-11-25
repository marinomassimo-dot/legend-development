"""Receipts for PMID 30202070 (supplement and Figure 1) and the four routed leads, 2026-11-25.

Usage, from the repository root: python3 <this file> OUTDIR
"""
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = '/home/desktop/legend-development'
LEDGER = 'disease-models/wwox/registries/fulltext_read_receipts.jsonl'
B = ('disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/'
     'adv276b_lead_receipts_sci_20261125/')
C = B + 'RESULT_ADV276C_30202070_SCI_20261125.md'
D = B + 'RESULT_ADV276D_ROUTED_LEADS_SCI_20261125.md'
BASE = dict(abstract='not_read', introduction='not_read', methods='not_read', results='not_read',
            figures='not_read', tables='not_read', discussion='not_read', limitations='not_read',
            supplementary='not_read', references='not_read')

ROWS = [
    dict(key='30202070', study={'pmid': '30202070', 'doi': '10.1038/s41467-018-06115-2'},
         rel='files/supplement/PMID30202070_r2/41467_2018_6115_MOESM1_ESM.pdf',
         depth='queried_not_full_read', reason='new_version_or_supplement', out=C, cov={},
         basis='Supplementary Figure 1 legend and panels opened as rendered page; main Figure 1 opened as image; '
               'XML passages on cell lines, reagents and cycloheximide chase; chloroquine and NH4Cl searches over XML '
               'and supplement. Other supplementary figures not read.'),
    dict(key='40125810', study={'pmid': '40125810', 'doi': '10.1111/cns.70334'},
         rel='files/fulltext/PMID40125810_Wang2025QO83_PMC_r2.xml',
         depth='queried_not_full_read', reason='first_read', out=D, cov={'abstract': 'read'},
         basis='Abstract; Methods passages on animals and doses; figure legends in part; supplement brain exposure and '
               'liver sections; searches for tolerability terms.'),
    dict(key='AIS2026', study={'doi': '10.1038/s42003-026-10958-7'},
         rel='files/fulltext/DOI10.1038_s42003-026-10958-7_AIS2026_inpress_20261125.pdf',
         depth='queried_not_full_read', reason='first_read', out=D, cov={'abstract': 'read'},
         basis='Article-in-press PDF: abstract (publisher page), retigabine and XE991 result passages, figure legends '
               'for sample sizes, AIS morphology passages. Supplement not read.'),
    dict(key='42723519', study={'pmid': '42723519', 'doi': '10.1002/phar.70198'},
         rel='files/fulltext/PMID42723519_VigabatrinPK2026_PMC13563110_pmcpage_20261125.html',
         depth='partial_fulltext_read', reason='first_read', out=D,
         cov=dict(abstract='read', introduction='read', methods='read', results='read', tables='read',
                  discussion='read', limitations='read', figures='captions_only'),
         basis='PMC article page: sections 1 to 4 and Tables 1 and 2 read; Table 2 medians recomputed; figure image not opened.'),
    dict(key='42441989', study={'pmid': '42441989', 'doi': '10.3171/CASE26183'},
         rel='files/fulltext/PMID42441989_VigabatrinMRI2026_PMC_r2.xml',
         depth='partial_fulltext_read', reason='first_read', out=D,
         cov=dict(abstract='read', introduction='read', results='read', discussion='read', figures='captions_only'),
         basis='XML: abstract, introduction, illustrative case and discussion read; figure images not opened.'),
]


def latest(pmid, doi):
    last = None
    for line in open(LEDGER):
        row = json.loads(line)
        sid = row.get('study_id', {})
        if (pmid and sid.get('pmid') == pmid) or (doi and sid.get('doi') == doi):
            last = row
    return last


now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
for r in ROWS:
    study = r['study']
    prev = latest(study.get('pmid'), study.get('doi'))
    coverage = dict(BASE, **r['cov'])
    receipt = dict(
        analysis_at=now[:16] + 'Z', analysis_time_precision='minute', coverage=coverage, event_at=now,
        event_id='FTR-20261125-%s-01' % r['key'], evidence_basis=['coverage_map', r['basis']],
        evidence_depth=r['depth'], outputs=[r['out']], record_kind='contemporaneous_receipt',
        reread_reason=r['reason'], source_fingerprint=hashlib.sha256(open('%s/%s' % (ROOT, r['rel']), 'rb').read()).hexdigest(),
        source_kind='fulltext_local', source_locator=r['rel'], study_id=prev['study_id'] if prev else study,
        workflow='SCI ADV-276 continued: 30202070 and routed leads (not a complete read)')
    receipt['prior_receipt'] = prev['event_id'] if prev else None
    Path(sys.argv[1], 'RECEIPT_ADV276CD_%s_SCI_20261125.json' % r['key']).write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(r['key'], prev['event_id'] if prev else None, '->', receipt['event_id'])
