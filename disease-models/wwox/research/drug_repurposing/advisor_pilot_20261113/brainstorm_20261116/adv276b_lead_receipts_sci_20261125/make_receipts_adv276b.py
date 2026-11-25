"""Build the ADV-276 batch-1 receipt JSONs (five lead papers). Usage: make_receipts_adv276b.py OUTDIR

Run from the repository root of the checkout whose ledger is current. Held bytes are read from the
root checkout's files/ directory.
"""
import glob, hashlib, json, sys, time
from pathlib import Path

ROOT = '/home/desktop/legend-development'
LEDGER = 'disease-models/wwox/registries/fulltext_read_receipts.jsonl'
BASE = 'disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv276b_lead_receipts_sci_20261125/'
OUT = BASE + 'RESULT_ADV276B_BATCH1_SCI_20261125.md'
NR, RD, CC, NP = 'not_read', 'read', 'captions_only', 'not_present'


def cov(**k):
    base = dict(abstract=NR, introduction=NR, methods=NR, results=NR, figures=CC, tables=NR,
                discussion=NR, limitations=NR, supplementary=NR, references=NR)
    base.update(k)
    return base


PAP = {
    '23435430': (cov(methods=RD, results=RD, discussion=RD, limitations=NP, tables=NP, supplementary=CC),
                 'partial_fulltext_read',
                 'Methods, Results, Discussion read; supplement legends read; images opened: Figure 4 A-D, Supplementary Figures S2 and S3. Supplement archive from Europe PMC supplementaryFiles, sha256 3e917b1df75d92c390e2966361be0aff2f16ab68c31aa59689f46a50608a7303.'),
    '22479346': (cov(abstract=RD, methods=RD, results=RD, discussion=RD, limitations=RD),
                 'partial_fulltext_read',
                 'Abstract, Results with Tables 2 and 3, Discussion, Methods read; Table 1, Introduction and supplement not read (Europe PMC supplementaryFiles returned 500).'),
    '36530994': (cov(methods=RD, results=RD, discussion=RD, limitations=RD, tables=NP),
                 'partial_fulltext_read',
                 'Methods, Results, Discussion read; supplement Tables S2, S5 and S8 of DataSheet_1.docx read, the other supplement items not. Supplement archive sha256 3c3d2518341206381abc4ffcf62a1489be2d14a74aa67462d692931588831e93.'),
    '24086726': (cov(abstract=RD, introduction=RD, methods=RD, results=RD, tables=RD, discussion=RD, limitations=RD, figures=NP),
                 'partial_fulltext_read',
                 'Body and Tables 1 to 4 read in full; supplement Tables S2 and S3 read, S4 in part, S1 not. Supplement archive sha256 819917b84ac6b594fe2478cf491950d95a85fa60cd9bd19e843bf5fb34aaeace.'),
    '40500435': (cov(),
                 'queried_not_full_read',
                 'Targeted: Results subsections on microglial metabolism and behaviour, Figure 3 and 4 legends, Methods mice, diet, NMR and statistics; Figure 3 image opened and panel b measured (EMS206505-f003.jpg sha256 335ff7c7941d2e99f12d0350f2bef112a1abbb206262e18646a38fab4e30e310, PMC open-data bucket).'),
}


def latest(pmid):
    last = None
    for line in open(LEDGER):
        row = json.loads(line)
        if row.get('study_id', {}).get('pmid') == pmid:
            last = row
    return last


out = sys.argv[1]
now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
for pmid, (coverage, depth, basis) in PAP.items():
    path = glob.glob('%s/files/fulltext/PMID%s_ADV272_*.xml' % (ROOT, pmid))[0]
    prev = latest(pmid)
    receipt = dict(
        analysis_at=now[:16] + 'Z', analysis_time_precision='minute', coverage=coverage, event_at=now,
        event_id='FTR-20261125-%s-01' % pmid, evidence_basis=['coverage_map', basis,
                                                              'Result and per-consumer wording: ' + OUT],
        evidence_depth=depth, outputs=[OUT], prior_receipt=prev['event_id'],
        record_kind='contemporaneous_receipt', reread_reason='adversarial_reanalysis',
        source_fingerprint=hashlib.sha256(open(path, 'rb').read()).hexdigest(), source_kind='fulltext_local',
        source_locator='files/fulltext/' + Path(path).name, study_id=prev['study_id'],
        workflow='SCI ADV-276 continued, batch 1 (re-open of five lead papers read earlier without a receipt; not a complete read)')
    Path(out, 'RECEIPT_ADV276B_%s_SCI_20261125.json' % pmid).write_text(json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(pmid, prev['event_id'], '->', receipt['event_id'], depth, receipt['source_fingerprint'][:10])
