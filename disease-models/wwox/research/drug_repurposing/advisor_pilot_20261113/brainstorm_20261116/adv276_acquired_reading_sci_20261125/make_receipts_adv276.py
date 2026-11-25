"""Build the ADV-276 receipt JSONs for the acquired papers read. Usage: make_receipts_adv276.py OUTDIR"""
import glob, hashlib, json, sys, time
from pathlib import Path
LEDGER = '/home/desktop/legend-development/.claude/worktrees/sci_ag_20261125/disease-models/wwox/registries/fulltext_read_receipts.jsonl'
OUT = 'disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv276_acquired_reading_sci_20261125/RESULT_ADV276_SCI_20261125.md'
NR, RD, CC = 'not_read', 'read', 'captions_only'
def cov(**k):
    b = dict(abstract=NR, introduction=NR, methods=NR, results=NR, figures=CC, tables=NR, discussion=NR, limitations=NR, supplementary=NR, references=NR)
    b.update(k); return b
PAP = {
 '35222658': (cov(abstract=NR, introduction=RD, methods=RD, results=RD, tables=RD, discussion=RD, limitations=RD), False, 'Acquired Europe PMC XML read in full: Introduction, Methods, Results, Tables 1-4, Discussion; Table 2, 3 and 4 p values recomputed (chi-square and exact 2x3).'),
 '36967744': (cov(results=RD), True, 'Targeted: Results, Efficacy and Safety paragraphs, Methods design sentence, limitation sentence; ratios and sums recomputed.'),
 '36601084': (cov(results=RD, tables=RD), True, 'Targeted: Results text, Tables 1 to 3 rows named in the result, exclusion sentences; counts and weighted mean recomputed.'),
 '40670421': (cov(methods=RD, results=RD, tables=RD, limitations=RD), True, 'Targeted: group definitions, Results and Tables 1 and 2, the Deficiency paragraph.'),
 '24321005': (cov(methods=RD), True, 'Targeted: Methods exclusions and histology, Results statements, myelin / white matter / MRI searches (2026-11-25).'),
 '40994429': (cov(results=RD, tables=RD, methods=RD), True, 'Targeted: variant Results paragraph, Table 2 rows, PTZ results and Table 3, seizure-test Methods; ratios recomputed, Fisher exact computed on printed counts.'),
 '42470358': (cov(results=RD), True, 'Targeted: OV329 retina passage and toxicology sentence; ratios recomputed from the printed means.'),
 '38605177': (cov(introduction=RD, results=RD), True, 'Targeted: Introduction, Results opening, Methods patch-clamp and compound list, Discussion first paragraph, searches for IC50, epilepsy, apinocaltamide (0 hits).'),
 '20810895': (cov(introduction=RD), True, 'Targeted: Introduction frame, Table 1 header, Figure 2 legend, unit sentences.'),
 '28447936': (cov(results=RD, discussion=RD), True, 'Targeted: title, Sephin1 Results and Discussion statements.'),
}
def latest(p):
    b = None
    for l in open(LEDGER):
        try: d = json.loads(l)
        except Exception: continue
        if d.get('study_id', {}).get('pmid') == p: b = d
    return b
out = sys.argv[1]; Path(out).mkdir(parents=True, exist_ok=True)
now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
for p, (c, queried, basis) in PAP.items():
    f = glob.glob('/home/desktop/legend-development/files/fulltext/PMID%s_ADV272_*' % p)[0]
    prev = latest(p); sha = hashlib.sha256(open(f, 'rb').read()).hexdigest()
    loc = 'files/fulltext/' + Path(f).name
    r = dict(analysis_at=now[:16]+'Z', analysis_time_precision='minute', coverage=c, event_at=now, event_id='FTR-20261125-%s-02' % p if prev['event_id'].startswith('FTR-20261125-%s-01' % p) else 'FTR-20261125-%s-01' % p,
             evidence_basis=['coverage_map', basis+' Acquired by a permitted route in ADV-272.', 'Result and per-consumer wording: '+OUT],
             evidence_depth='queried_not_full_read' if queried else 'partial_fulltext_read', outputs=[OUT], prior_receipt=prev['event_id'], record_kind='contemporaneous_receipt',
             reread_reason='new_question_outside_prior_coverage' if queried else 'inadequate_prior_coverage', source_fingerprint=sha, source_kind='fulltext_local', source_locator=loc,
             study_id=prev['study_id'], workflow='SCI ADV-276 (newly acquired papers that cards rest on; not a complete read; figure images unread; supplement not held)')
    Path(out, 'RECEIPT_ADV276_%s_SCI_20261125.json' % p).write_text(json.dumps(r, indent=1, sort_keys=True)+'\n')
    print(p, prev['event_id'], '->', r['event_id'], r['evidence_depth'], sha[:10])
