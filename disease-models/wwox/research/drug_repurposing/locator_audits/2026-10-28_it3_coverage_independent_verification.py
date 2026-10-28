#!/usr/bin/env python3
"""Independent recomputation for the it3 coverage audit (actor scientist-c).
Reads catalog.jsonl.gz, needs.json, coverage_summary.json directly; imports no producer module."""
import json, gzip, collections, sys, os
B = os.path.dirname(os.path.abspath(__file__)) + '/..'
needs = {n['id']: n for n in json.load(open(B+'/needs/needs.json'))['needs']}
S = json.load(open(B+'/coverage/coverage_summary.json'))
recs = [json.loads(l) for l in gzip.open(B+'/catalog/catalog.jsonl.gz', 'rt')]
print('records', len(recs))
LINK = {'intervention_target','pathway_member','effector_constraint','disease_gene_product'}
def sym2need(kinds):
    d = collections.defaultdict(set)
    for nid, n in needs.items():
        for t in n['targets']:
            if t['target_kind'] in kinds: d[t['symbol']].add(nid)
    return d
def hits(r, symset):
    """symbols of symset hit by record r; human ChEMBL components or DGIdb gene (HGNC)"""
    out = {}
    for t in r['targets']:
        if t['source'] == 'DGIdb interaction':
            if t['gene'] in symset: out.setdefault(t['gene'], set()).add('dgidb')
        elif t['source'].startswith('ChEMBL') and t.get('organism') == 'Homo sapiens':
            for g in t.get('gene_symbols') or []:
                if g in symset: out.setdefault(g, set()).add('chembl')
    return out
def fam(r):
    p = r['relations'].get('parent')
    return p if p else r['id']
def per_need(kinds):
    allsyms = {t['symbol'] for n in needs.values() for t in n['targets']}
    res = {nid: [set(), set(), collections.Counter()] for nid in needs}
    for r in recs:
        h = hits(r, allsyms)
        for g in h:
            for nid, n in needs.items():
                for t in n['targets']:
                    if t['symbol'] == g and t['target_kind'] in kinds:
                        res[nid][0].add(r['id']); res[nid][1].add(fam(r)); res[nid][2][g] += 1
    return res
res = per_need(LINK)
print('%-45s %6s %6s | %6s %6s | %s' % ('need','recs','fams','rep_r','rep_f','per-symbol'))
tot_rec = set(); tot_fam = set()
for nid in needs:
    p = S['needs']['per_need'][nid]
    print('%-45s %6d %6d | %6d %6d | %s' % (nid, len(res[nid][0]), len(res[nid][1]), p['records_with_documented_link'], p['families_with_documented_link'], dict(res[nid][2])))
    tot_rec |= res[nid][0]; tot_fam |= res[nid][1]
print('union records', len(tot_rec), 'reported', S['catalogue_coverage']['records_with_documented_link_to_a_need'])
print('union families(parent key)', len(tot_fam), 'reported', S['catalogue_coverage']['families_touching_at_least_one_need_counted_once'])
with_t = sum(1 for r in recs if r['targets'])
# "target row" definition variants
def any_row(r): return bool(r['targets'])
def row_real(r): return any(t.get('gene') or t.get('gene_symbols') or t.get('target_id') for t in r['targets'])
print('records with any target row', with_t, 'with an identifiable gene/target', sum(1 for r in recs if row_real(r)))
print('pct', round(100*len(tot_rec)/len(recs),2), round(100*len(tot_rec)/with_t,2))
# (2) identity guards, readouts
g = sym2need({'identity_guard'}); ro = sym2need({'readout_marker'})
print('guards', dict(g)); 
for sym in ['PDK1','PDPK1','LDHC','TCF4','COXFA4']:
    hs = [r['name'] for r in recs if sym in hits(r,{sym})]
    print(sym, len(hs), hs[:6])
pd = {r['id'] for r in recs if 'PDK1' in hits(r,{'PDK1'})} & {r['id'] for r in recs if 'PDPK1' in hits(r,{'PDPK1'})}
print('records hitting both PDK1 and PDPK1 (own matcher)', len(pd))
# readout-only
only = collections.Counter()
for nid,n in needs.items():
    rs = {t['symbol'] for t in n['targets'] if t['target_kind']=='readout_marker'}
    for r in recs:
        if hits(r,rs) and r['id'] not in res[nid][0]: only[nid]+=1
print('readout-only per need', dict(only), 'sum', sum(only.values()))
# (6) access
ac = collections.Counter(); multi = collections.Counter(); noacc = 0
for r in recs:
    cats = r.get('access_categories') or []
    if not cats: noacc += 1
    for c in cats: ac[c]+=1
    multi[len(cats)] += 1
print('access category counts (records can carry >1)', dict(ac), 'n cats per record', dict(multi), 'no category', noacc)
st = json.load(open(B+'/catalog/catalog_stats.json'))
print([k for k in st])

print('=== part 2 ===')
def tdetail(sym):
    c = collections.Counter()
    for r in recs:
        for t in r['targets']:
            gs = [t.get('gene')] if t['source']=='DGIdb interaction' else (t.get('gene_symbols') or [])
            if sym in gs: c[(t['source'][:5], t.get('target_name') or t.get('gene'), t.get('organism'), t.get('action_type') or t.get('interaction_type'))]+=1
    return c
for s in ['PDK1','PDPK1']:
    print(s, tdetail(s).most_common(8))
for r in recs:
    if hits(r,{'PDK1'}) and hits(r,{'PDPK1'}): print('both:', r['name'], [(t.get('gene') or t.get('gene_symbols'), t.get('target_name')) for t in r['targets'] if 'PDK' in str(t.get('gene') or t.get('gene_symbols'))])
# direct-only GSK3
dir_ = set(); 
for r in recs:
    if hits(r,{'GSK3B','GSK3A'}): dir_.add(r['id'])
mapt = {r['id'] for r in recs if hits(r,{'MAPT'})}
print('GSK3: records hitting GSK3A/B', len(dir_), 'MAPT', len(mapt), 'MAPT only', len(mapt-dir_), 'axin1', sum(1 for r in recs if hits(r,{'AXIN1'})))
print('MAPT hits by source', collections.Counter(tuple(sorted(hits(r,{'MAPT'})['MAPT'])) for r in recs if hits(r,{'MAPT'})))
print('MAPT action types', collections.Counter(t.get('action_type') or t.get('interaction_type') for r in recs for t in r['targets'] if (t.get('gene')=='MAPT' or 'MAPT' in (t.get('gene_symbols') or []))).most_common(8))
# intervention_target-only recount (excl pathway_member/effector/disease gene)
res2 = per_need({'intervention_target'})
for nid in ['NEED-GSK3B-DEREPRESSION','NEED-ISR-ATTENUATION','NEED-LACTATE-LDH','NEED-NEUROINFLAMMATION-GLIA','NEED-MITOCHONDRIAL-RESPIRATION','NEED-REDOX-OXIDATIVE-STRESS','NEED-PDH-PYRUVATE-AXIS','NEED-WNT-BETA-CATENIN','NEED-MYC-PROGENITOR-PROLIFERATION','NEED-MTOR-AUTOPHAGY']:
    print('intervention_target-only', nid, len(res2[nid][0]), 'vs link-type', len(res[nid][0]))
# readout-only union
allro = set(); lk=set(tot_rec)
for nid,n in needs.items():
    rs = {t['symbol'] for t in n['targets'] if t['target_kind']=='readout_marker'}
    for r in recs:
        if hits(r,rs): allro.add(r['id'])
print('records touching readout marker', len(allro), 'only readout (not linked to any need)', len(allro-lk))
# family difference
fams_by_rec = {}
famset=collections.defaultdict(set)
for r in recs: famset[fam(r)].add(r['id'])
print('source-only singletons', sum(1 for r in recs if not r['relations'].get('parent')), 'families(parent key)', len(famset))

print('=== part 3: ABAT GuideToPharmacology artefact ===')
def abat_real(r):
    return any((t['source'].startswith('ChEMBL') and t.get('organism')=='Homo sapiens' and 'ABAT' in (t.get('gene_symbols') or [])) or
               (t['source']=='DGIdb interaction' and t['gene']=='ABAT' and t['claim_source']!='GuideToPharmacology') for t in r['targets'])
def abat_gtop(r):
    return any(t['source']=='DGIdb interaction' and t['gene']=='ABAT' and t['claim_source']=='GuideToPharmacology' for t in r['targets'])
ab_all=[r for r in recs if hits(r,{'ABAT'})]
art=[r for r in ab_all if abat_gtop(r) and not abat_real(r)]
print('ABAT records', len(ab_all), 'GtoP-only (adenosine-receptor-ligand artefact pattern)', len(art), 'residual', len(ab_all)-len(art))
print('residual names', sorted(r['name'] for r in ab_all if r not in art))
P = json.load(open(B+'/coverage/priorities.json'))['priorities']
artid={'FAM:'+r['id'] for r in art}
cons=[p for p in P if p['disposition']=='consistent_mechanism_candidate' and p['need']=='NEED-SEIZURE-CONTROL-SYMPTOMATIC']
cacna=set(r['id'] for r in recs if hits(r,{'CACNA1G'}))
bad=[p for p in cons if p['row_id'] in artid and ('FAM:'+p['row_id'][4:]) and p['row_id'][4:] not in cacna]
print('seizure consistent cells', len(cons), 'resting only on artefact ABAT rows', len(bad), [p['name'] for p in bad][:12])

print('=== part 4: denominators, sensitivity ===')
u_it = set()
for nid in needs: u_it |= res2[nid][0]
print('union records, intervention_target-only', len(u_it), round(100*len(u_it)/len(recs),2))
artids = {r['id'] for r in art}
print('union records link-type minus ABAT GtoP artefact', len(tot_rec-artids), 'minus MAPT-only GSK3B', len(tot_rec-artids-({r['id'] for r in recs if hits(r,{'MAPT'})}-dir_)))
# families touching n needs (parent key)
cnt = collections.Counter()
for nid in needs:
    for f in res[nid][1]: cnt[f]+=1
dist = collections.Counter(cnt.values()); print('touch distribution (my key)', sorted(dist.items()), 'sum', sum(dist.values()))
print('sum of per-need family counts', sum(len(res[n][1]) for n in needs), '(naive double-counting total; not reported as such)')
top = [f for f,c in cnt.items() if c>=8]
for f in top: print('touches', cnt[f], [r['name'] for r in recs if r['id']==f or fam(r)==f][:2])
print('report access sum', sum(ac.values()), 'records', len(recs), 'overlap extra', sum(ac.values())-len(recs))
print(json.dumps({k:st[k] for k in ('access_signature_sums_to_total','access_category_overlapping_counts','access_unknown_unverified_entries') if k in st}, indent=0)[:1200]) if False else None

print('=== part 5: non-human / organism-None ChEMBL rows carrying a need symbol (case-insensitive) ===')
allsyms = {t['symbol'].upper() for n in needs.values() for t in n['targets']}
c = collections.Counter()
for r in recs:
    for t in r['targets']:
        if t['source'].startswith('ChEMBL') and t.get('organism') != 'Homo sapiens':
            for g in t.get('gene_symbols') or []:
                if g.upper() in allsyms: c[(t.get('organism'), g)] += 1
print(dict(c))
