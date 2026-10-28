#!/usr/bin/env python3
"""Re-verification of the revised it3 coverage layer (scientist-c). No producer module imported."""
import json, gzip, collections, os
B = os.path.dirname(os.path.abspath(__file__)) + '/..'
needs = {n['id']: n for n in json.load(open(B+'/needs/needs.json'))['needs']}
S = json.load(open(B+'/coverage/coverage_summary.json'))
recs = [json.loads(l) for l in gzip.open(B+'/catalog/catalog.jsonl.gz','rt')]
HEAD = {'intervention_target','disease_gene_product'}
def rows(r):
    """yield (symbol, source, claim_source, action) for human ChEMBL and DGIdb rows"""
    for t in r['targets']:
        if t['source']=='DGIdb interaction': yield t['gene'], 'dgidb', t.get('claim_source'), t.get('interaction_type')
        elif t['source'].startswith('ChEMBL') and t.get('organism')=='Homo sapiens':
            for g in t.get('gene_symbols') or []: yield g,'chembl',None,t.get('action_type')
def excluded(r, sym, src, cs):
    if r['name']=='Null' and r['origin']=='dgidb_only': return 'placeholder'
    if sym in ('ABAT','ABCA1','ABCA2','ABCA3') and src=='dgidb' and cs=='GuideToPharmacology':
        # require a second (non-GtoP) source for the same symbol on the same record
        if not any(s2==sym and (src2=='chembl' or cs2!='GuideToPharmacology') for s2,src2,cs2,_ in rows(r)): return 'artefact'
    if sym=='PDK1' and src=='dgidb' and cs in ('TdgClinicalTrial','PharmGKB'):
        syms={s for s,_,_,_ in rows(r)}
        chem_pdk1=any(s=='PDK1' and src2=='chembl' for s,src2,_,_ in rows(r))
        if 'PDPK1' in syms and not chem_pdk1: return 'alias'
    return None
def fam(r): return r['relations'].get('parent') or r['id']
def count(kinds):
    out={nid:[set(),set()] for nid in needs}; ex=collections.Counter()
    for r in recs:
        for sym,src,cs,_ in rows(r):
            for nid,n in needs.items():
                for t in n['targets']:
                    if t['symbol']==sym and t['target_kind'] in kinds:
                        e=excluded(r,sym,src,cs)
                        if e: ex[(e,r['id'])]+=1; continue
                        out[nid][0].add(r['id']); out[nid][1].add(fam(r))
    return out,ex
o,ex=count(HEAD)
print('%-42s %5s %5s | %5s %5s'%('need','rec','fam','rep_r','rep_f'))
ur=set();uf=set()
for nid in needs:
    p=S['needs']['per_need'][nid]
    print('%-42s %5d %5d | %5d %5d'%(nid[5:],len(o[nid][0]),len(o[nid][1]),p['records_with_documented_link'],p['families_with_documented_link']))
    ur|=o[nid][0]; uf|=o[nid][1]
print('union records',len(ur),'reported',S['catalogue_coverage']['union_headline_records'],'| families(parent key)',len(uf),'reported',S['catalogue_coverage']['union_headline_families'])
print('excluded record ids by reason', collections.Counter(k[0] for k in ex), 'reported', S['catalogue_coverage']['excluded_rows']['by_reason'])
print('pct',round(100*len(ur)/len(recs),2), round(100*len(ur)/24423,2))
# with pathway members
o2,_=count(HEAD|{'pathway_member'}); u2=set()
for nid in needs: u2|=o2[nid][0]
print('union incl pathway members',len(u2),'reported',S['catalogue_coverage']['union_with_pathway_members_records'])
# effector/MAPT never links
g=[r for r in recs if any(s=='MAPT' for s,_,_,_ in rows(r))]
print('MAPT records',len(g),'of which in GSK3B headline', len(set(r['id'] for r in g)&o['NEED-GSK3B-DEREPRESSION'][0]))
# ABAT genuine
print('ABAT headline INHIB', len(o['NEED-INHIBITORY-HYPOFUNCTION'][0]), sorted(r['name'] for r in recs if r['id'] in o['NEED-INHIBITORY-HYPOFUNCTION'][0]))
# union touch distribution
cnt=collections.Counter()
for nid in needs:
    for f in o[nid][1]: cnt[f]+=1
print('touch dist',sorted(collections.Counter(cnt.values()).items()))
# priorities
P=json.load(open(B+'/coverage/priorities.json'))['priorities']
cons=[p for p in P if p['disposition']=='consistent_mechanism_candidate']
print('consistent cells',len(cons),'distinct families',len({p['row_id'] for p in cons}), collections.Counter(p['need'][5:] for p in cons))
dirs={k:v['intervention_direction']['direction'] for k,v in needs.items()}
print('uncertain-need favourable/opposed', sum(1 for p in P if dirs[p['need']]=='uncertain' and p['disposition'] in('consistent_mechanism_candidate','opposite_mechanism')))
print('dispositions',collections.Counter(p['disposition'] for p in P))
