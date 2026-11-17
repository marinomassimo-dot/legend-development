import sys,json,urllib.parse
sys.path.insert(0,"/tmp/it56_iso")
from framework.adapters import _http, chembl
f=_http.make_fetch("/tmp/it56_adv029/cache2",retries=2,pause=6.0)
out={}
# candidate molecule records: ChEMBL ids from the free-text name search (candidates, not identifications)
cands={"GSK2837808A":["CHEMBL3335794"],"FX11":["CHEMBL126519"],"GNE-140":["CHEMBL5027251","CHEMBL3122117","CHEMBL4475494"],"galloflavin":["CHEMBL3763517","CHEMBL4217921","CHEMBL5199516"]}
for name,ids in cands.items():
    for cid in ids:
        s,r=f("https://www.ebi.ac.uk/chembl/api/data/molecule/%s.json"%cid)
        st=(r.get("molecule_structures") or {}) if s==200 else {}
        out[(name,cid)]={"http":s,"inchikey":st.get("standard_inchi_key"),"smiles":st.get("canonical_smiles"),"pref_name":r.get("pref_name") if s==200 else None}
# published structures from PubChem by name (key-less public PUG REST)
pub={}
for name in ["GSK2837808A","GNE-140","FX11","galloflavin"]:
    s,r=f("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/%s/property/InChIKey,CanonicalSMILES,Title/JSON"%urllib.parse.quote(name))
    pub[name]={"http":s,"rows":(r.get("PropertyTable",{}).get("Properties") if s==200 and isinstance(r,dict) else str(r)[:120])}
json.dump({"chembl":{"|".join(k):v for k,v in out.items()},"pubchem":pub},open("/tmp/it56_adv029/ident.json","w"),indent=1)
for k,v in out.items(): print(k,v["http"],v["inchikey"],(v["smiles"] or "")[:90])
for k,v in pub.items(): print(k,v)
print(f.stats)
