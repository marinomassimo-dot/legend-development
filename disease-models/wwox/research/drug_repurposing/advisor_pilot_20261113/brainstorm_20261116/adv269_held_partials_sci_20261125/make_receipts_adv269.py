"""Build the six ADV-269 receipt JSONs (digests computed from the held files, prior receipt read from the ledger). Usage: make_receipts_adv269.py OUTDIR"""
import hashlib, json, sys, time
from pathlib import Path
ROOT = Path('/home/desktop/legend-development')
LEDGER = Path('disease-models/wwox/registries/fulltext_read_receipts.jsonl')
OUT = 'disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv269_held_partials_sci_20261125/RESULT_ADV269_SCI_20261125.md'
NR, RD, CC, NP = 'not_read', 'read', 'captions_only', 'not_present'
def cov(**k):
    base = dict(abstract=NR, introduction=NR, methods=NR, results=NR, figures=CC, tables=NR, discussion=NR, limitations=NR, supplementary=NR, references=NR)
    base.update(k); return base
PAP = {
 '31605637': dict(src='files/fulltext/PMID31605637_NQO1_P187S_PMC7027498_epmc_2026-10-29.xml', doi=None,
   cov=cov(abstract=RD, discussion=RD, tables=RD, supplementary=NR),
   basis='Held Europe PMC XML: Discussion read in full; Results subsections Binding and stabilizing effect, Inhibition and activation assays, Steady-state kinetics read; Methods subsections thermal shift, steady-state kinetics, inhibition and activation read, other Methods subsections listed only; Table 2 read and kcat/KM recomputed; Acknowledgements sentence on preliminary cell culture read; cell-culture search of the whole body; figures captions only; Tables S1 and S2 are not in the XML.'),
 '42422766': dict(src='files/fulltext/PMID42422766_Amaral2026_PMC.xml', doi=None,
   cov=cov(tables=NR, supplementary=RD),
   basis='Held supplement: mmc1.pdf text (Figures S1-S9 captions, 19 pages) and mmc2.xlsx cell-wise dump (Tables S2 and S4, every row); Table S2 parent totals checked against grade rows (68 blocks, 3 mismatches, confirmed on raw lines); figure images and the archive beyond these two files not opened.'),
 '24935251': dict(src='files/fulltext/PMID24935251_Balmer2014_PMC.xml', doi=None,
   cov=cov(supplementary=CC),
   basis='Held supplement workbooks 204_2014_1279_MOESM2 to MOESM5 (xlsx) searched with a stdlib parser for the five WWOX probe sets and the symbol: two rows found (Table S1 sheet 6h row 1354, Table S2 sheet T4d VPA row 1384); header rows read; MOESM1 pdf and figures not read.'),
 '26272509': dict(src='files/fulltext/PMID26272509_Rempel2015_PMC.xml', doi=None,
   cov=cov(methods=RD, supplementary=CC),
   basis='Held supplement MOESM2 (full probe-set tables, 14 sheets) searched for the five WWOX probe sets in every sheet, contents sheet read, fold-change direction checked on CDKN1A and MT1X; MOESM3 searched for WWOX; main-text Methods sentences on the VPA stock and concentration read; MOESM1 pdf and figures not read.'),
 '35229008': dict(src='files/fulltext/PMID35229008_Buss2022_PMC.xml', doi=None,
   cov=cov(supplementary=CC),
   basis='Held supplement mmc1 (text of the pdf, plus a rendered image of the Table S3 page): Tables S1, S2, S3, S5, S6, S7 and S17 read and cross-checked (S2 against S3 and S5 per animal); Tables S8-S16 and S18-S25, mmc2 and figure images not read.'),
 '41345172': dict(src='files/fulltext/PMID41345172_De2025_PMC.xml', doi=None,
   cov=cov(supplementary=CC),
   basis='Held XML: every WWOX passage of the body read (Results, Methods, Discussion); supplement MOESM4 Supplementary Table 4 (three sheets) parsed and WWOX association p values compared inside and outside chr16:78,371,638-78,385,000; MOESM12 (Table 12) read; MOESM8 title only; MOESM15 pdf text captions read; other workbooks and figure images not opened.'),
 '42601505': dict(src='files/fulltext/PMID42601505_Puertas2026_PMC.xml', doi=None,
   cov=cov(),
   basis='Held XML only: supplementary-material list and the Reagents and tools table inspected; statements on abolished respiration, MERRF cohort size and the exploratory caveat located in the text; Tables EV1-EV3, Appendix, source data and Expanded View are not in the held bytes.'),
 '25779665': dict(src='files/fulltext/PMID25779665_Chen2015_PMC.xml', doi=None,
   cov=cov(supplementary=RD),
   basis='Held supplement text files/fulltext/PMID25779665_Chen2015_supp_pdftotext.txt read in full (Figures S1-S5 and Videos 1-9 captions); main-text references to the supplement located; figure images and the movies are not held or not opened.'),
 '31353122': dict(src='files/fulltext/PMID31353122_Mori2019_IR.pdf', doi=None,
   cov=cov(figures=RD),
   basis='Held PDF: figure pages 16 and 17 (Figures 1 and 2) opened as images and read with their captions; Figure 3 was read in an earlier wave; WWOX passages of the text located.'),
 '40191585': dict(src='files/fulltext/PMID40191585_Robertson2025_PMC.xml', doi=None,
   cov=cov(supplementary=CC),
   basis='Held supplement pdf text searched for WWOX and E17K (Note 3, Figure 12 caption, Tables 5-6 read, percentages recomputed); zip members listed (pdf and figure images only); main-text Epi25 and 172-carrier sentences located.'),
 '41404412': dict(src='files/fulltext/PMID41404412_Grubor2025_PMC.xml', doi=None,
   cov=cov(supplementary=CC),
   basis='Held supplement mmc1 text: Tables S1 (fold-change columns recomputed on three animals), S2 and S5 read, S3-S4 listed not recomputed, Figure S11-S12 captions read; main-text day-5, EM and euthanasia sentences located.'),
 '41715204': dict(src='files/fulltext/PMID41715204_Sun2026_PMC.xml', doi=None,
   cov=cov(supplementary=CC),
   basis='Held supplement workbooks MOESM6 (Table S1, 403 rows, group means and per-animal separation of cholesteryl esters) and MOESM9 (Table S4, 265 printed ratios recomputed) read with a stdlib parser; MOESM4 and MOESM8 titles only; main-text sample sizes located.'),
}
def latest(pmid):
    best = None
    for line in (ROOT/'.claude/worktrees/sci_ag_20261125'/LEDGER).read_text().splitlines() if False else open(LEDGER):
        try: d = json.loads(line)
        except Exception: continue
        if d.get('study_id', {}).get('pmid') == pmid: best = d
    return best
QUERIED = {'24935251', '35229008', '41345172', '42601505', '40191585', '41404412', '41715204'}  # targeted searches of held supplements: no article section read, so the honest depth is queried_not_full_read
def main(outdir, only=None):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    for pmid, p in PAP.items():
        if only and pmid not in only: continue
        prev = latest(pmid)
        sha = hashlib.sha256((ROOT/p['src']).read_bytes()).hexdigest()
        r = dict(analysis_at=now[:16]+'Z', analysis_time_precision='minute', coverage=p['cov'], event_at=now,
                 event_id=f'FTR-20261125-{pmid}-01', evidence_basis=['coverage_map', p['basis'], 'Result and per-consumer wording: '+OUT],
                 evidence_depth=('queried_not_full_read' if pmid in QUERIED else 'partial_fulltext_read'), outputs=[OUT], prior_receipt=prev['event_id'], record_kind='contemporaneous_receipt',
                 reread_reason=('new_question_outside_prior_coverage' if pmid in QUERIED else 'inadequate_prior_coverage'), source_fingerprint=sha, source_kind='fulltext_local', source_locator=p['src'],
                 study_id=prev['study_id'], workflow='SCI ADV-269 (held partials, unread classes inside held bytes; held bytes only, no contact, no spend); not a complete read, figure images remain unread')
        Path(outdir, f'RECEIPT_ADV269_{pmid}_SCI_20261125.json').write_text(json.dumps(r, indent=1, sort_keys=True)+'\n')
        print(pmid, 'prior', prev['event_id'], 'sha', sha[:12])
main(sys.argv[1], set(sys.argv[2:]) or None)
