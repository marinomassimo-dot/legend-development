import json,collections,statistics,math
R=json.load(open('../raw/acts_CHEMBL262_v.json'))["rows"]+json.load(open('../raw/acts_CHEMBL2850_v.json'))["rows"]
U={"nM":1,"uM":1e3,"mM":1e6,"pM":1e-3,"M":1e9}
def v(r):
    try: return float(r['standard_value'])*U[r['standard_units']]
    except: return None
# same document, same molecule, same assay-type, both targets human
g=collections.defaultdict(lambda:{'B':[], 'A':[]})
for r in R:
    x=v(r)
    if x is None: continue
    k=(r['molecule_chembl_id'],r['document_chembl_id'],r['standard_type'])
    side='B' if r['target_chembl_id']=='CHEMBL262' else 'A'
    g[k][side].append((x,r['standard_relation'],r['assay_chembl_id'],r['assay_description'],r.get('assay_variant_mutation'),r['activity_id'],r['data_validity_comment']))
out=[]
for k,d in g.items():
    if d['A'] and d['B']:
        a=statistics.median(x[0] for x in d['A']); b=statistics.median(x[0] for x in d['B'])
        exact=all(x[1]=='=' for x in d['A']+d['B'])
        out.append((max(a/b,b/a),k,a,b,exact,len(d['A']),len(d['B'])))
out.sort(reverse=True)
print("pairs",len(out),"exact",sum(o[4] for o in out))
ex=[o for o in out if o[4]]
print("exact pairs >4x:",sum(o[0]>4 for o in ex),">10x:",sum(o[0]>10 for o in ex))
for o in ex[:25]: print(round(o[0],1),o[1],o[2],o[3],o[5],o[6])
json.dump([(o[0],o[1],o[2],o[3],o[4]) for o in out],open('pairs.json','w'))
