import sys,csv,collections,json,os
from pathlib import Path
DR=Path('.').resolve()
sys.path.insert(0,'../../../../framework/scripts'); sys.path.insert(0,'generation_it21_p2_20261103')
import compound_catalog as cc, repurposing_search as rs
import attribution_screen_it21 as AS
entries=cc.load(DR/'catalog'/'catalog.jsonl.gz')
fam=rs.families(entries); E={e['id']:e for e in entries}
mem=collections.defaultdict(list)
for e in entries: mem[fam[e['id']]].append(e)
rows=[r for r in csv.DictReader(open('generation_it22_p1_20261103/results_p4/proposals_it21.tsv'),delimiter='\t') if r['question'] in('Q2','Q4','Q8')]
lig,_,_=AS.load_gtopdb_affinities()
br=AS.bridge_claim_name_ligands(entries)
out=[]
def sk(k): return k.split('-')[0] if k else None
for r in rows:
    f=r['family_id']; ms=mem[f]
    rootrec=E.get(f.replace('FAM:',''))
    own=[m['ids'].get('inchikey') for m in ms if m['ids'].get('inchikey')]
    a_root=rootrec['ids'].get('inchikey') if rootrec else None
    # (b) merged bridges of members
    b=[];bdec=[]
    for m in ms:
        for x in br.get(m['id'],[]):
            bdec.append((x['decision'],x['reason'],x['ligand_id']))
            if x['decision']=='merged':
                b.append(lig[x['ligand_id']]['InChIKey'])
    # (c) record's own iuphar_ligand
    c=[];lab=[]; nl=set()
    for m in ms:
        for lid in m['ids'].get('iuphar_ligand') or []:
            nl.add(lid); l=lig.get(lid)
            if l is None: continue
            if l['Labelled']=='yes' or l['Radioactive']=='yes': lab.append(lid); continue
            if l['InChIKey']: c.append(l['InChIKey'])
    out.append(dict(pid=r['proposal_id'],q=r['question'],fam=f,compound=r['compound'],n_members=len(ms),origins='|'.join(sorted({m['origin'] for m in ms})),
        root_has=bool(a_root),a_any=len(set(own)),a_keys='|'.join(sorted(set(own))),b_keys='|'.join(sorted(set(b))),bdec=';'.join(map(str,bdec)),c_keys='|'.join(sorted(set(c))),c_nlig=len(nl),c_lab=len(lab),has_chembl=r['has_chembl']))
w=csv.DictWriter(open('verification_it24_20261104/v1_mine_rows.tsv','w'),fieldnames=list(out[0]),delimiter='\t');w.writeheader();w.writerows(out)
