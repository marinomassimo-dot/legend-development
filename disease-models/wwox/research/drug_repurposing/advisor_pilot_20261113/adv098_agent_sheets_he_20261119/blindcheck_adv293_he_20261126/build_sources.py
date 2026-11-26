import json, os, sys, glob, csv, time
ROOT='/home/desktop/legend-development/.claude/worktrees/he_z_20261126'
sys.path.insert(0,ROOT+'/framework/scripts'); sys.path.insert(0,ROOT)
import eutils
from framework.adapters import openfda, _http
RAW='/home/desktop/legend-development/files/adv098_agent_sheets_raw_he_20261119'
RAW2='/home/desktop/legend-development/files/adv113_m1_comparators_raw_he_20261120'
OUT=os.path.join(os.environ['CLAUDE_JOB_DIR'],'tmp/adv293/packets')
COMP={1:['ethosuximide','lithium','memantine'],2:['ezogabine','azetukalner','ica-069673','xe991'],
3:['ganaxolone','gaboxadol'],4:['ketamine','memantine','d-ap5'],5:['vigabatrin','bumetanide'],
10:['tazemetostat','tmp195','10058-f4'],11:['apinocaltamide','ulixacaltamide','tta-a2','tta-p2','ethosuximide'],
12:['pirenzepine','telenzepine','vu0255035','tmp195']}
LAB={1:['ethosuximide','lithium','memantine'],2:['ezogabine'],3:['ganaxolone','gaboxadol'],4:['ketamine'],5:['vigabatrin','bumetanide'],
10:['tazemetostat'],11:[],12:['pirenzepine']}
COLS=['activity_id','standard_type','standard_relation','standard_value','standard_units','pchembl_value','data_validity_comment','potential_duplicate','target_chembl_id','target_pref_name','target_type','target_organism','target_genes','assay_chembl_id','assay_type','assay_organism','assay_cell_type','assay_tissue','confidence_score','assay_description','document_chembl_id','document_year']
def clean(v): return '' if v is None else str(v).replace('\t',' ').replace('\n',' ')
for n,comps in COMP.items():
    d=f'{OUT}/batch{n}'; os.makedirs(d+'/tables',exist_ok=True)
    for c in comps:
        p=f'{RAW2}/{c}.json' if os.path.exists(f'{RAW2}/{c}.json') else f'{RAW}/{c}.json'
        j=json.load(open(p))
        with open(f'{d}/tables/{c}.tsv','w') as o:
            o.write(f"# ChEMBL answer for {c}: status={j['status']} rows={len(j['hits'])} release={j.get('source_version')} retrieved={j.get('retrieved_at')} request={json.dumps(j.get('request'))}\n")
            o.write('\t'.join(COLS)+'\n')
            for h in j['hits']:
                ac=h.get('assay_context') or {}
                row={**ac,**h,'target_genes':','.join(h.get('target_gene_symbols') or [])}
                o.write('\t'.join(clean(row.get(k)) for k in COLS)+'\n')
        extra={k:v for k,v in j.items() if k not in('hits',)}
        json.dump(extra,open(f'{d}/tables/{c}.meta.json','w'),indent=1,default=str)
    pm=[x for x in json.load(open(d+'/meta.json'))['numbers7_8']]
    if pm:
        url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract&retmode=text&id='+','.join(pm)
        code,body=eutils.fetch(url)
        body=body.decode() if isinstance(body,bytes) else body
        open(d+'/abstracts.txt','w').write('# PubMed efetch abstracts, fetched 2026-11-26, for every 7-8 digit number in the sheet (some are not PMIDs: PubChem CIDs, ChEMBL activity ids)\n'+body)
        print(n,'efetch',code,len(body))
    os.makedirs(d+'/labels',exist_ok=True)
    for drug in LAB[n]:
        r=openfda.query({'drug':drug,'sections':['indications_and_usage','pediatric_use','warnings','warnings_and_cautions','nonclinical_toxicology','mechanism_of_action','pharmacokinetics','clinical_studies']})
        json.dump(r,open(f'{d}/labels/{drug}.json','w'),indent=1,default=str)
        print(n,drug,r.get('status'),len(r.get('hits',[])),r.get('source_version'))
