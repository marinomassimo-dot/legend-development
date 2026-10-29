#!/usr/bin/env python3
"""IT6-P11: reuse of catalog/eu_context_probe.py on magnesium names. Offline; reads the EU registers already cached under $LEGEND_CATALOG_CACHE/eu (fetched by eu_context_probe.py fetch). Writes eu_mg_probe.tsv into the current directory and prints the authorised health-claim wordings that contain the word magnesium. Name match only: not a product, a use, a dose or a safety statement; EU level, not Italian national."""
import sys as _sys
if len(_sys.argv) > 1 and _sys.argv[1] in ('-h', '--help'):
    print(__doc__)
    raise SystemExit(0)

import sys,csv,collections
from pathlib import Path; sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'catalog'))
import eu_context_probe as e
nf,hc=e.rows("novel_food.ndjson"),e.rows("health_claims.ndjson")
nft=[(e.norm(" ; ".join(str(x.get(k) or "") for k in ("novel_food_name","novel_food_display_name","common_name","synonyms"))),x) for x in nf]
hct=[(e.norm(x.get("nutrient_subst_food_no_html") or x.get("nutrient_subst_food")),x) for x in hc]
print("rows: novel_food",len(nf),"health_claims",len(hc))
names=["Magnesium","Magnesium citrate","Magnesium glycinate","Magnesium bisglycinate","Magnesium oxide","Magnesium L-threonate","Magnesium threonate","Magnesium taurate","Magnesium malate","Magnesium chloride","Magnesium sulfate","Magnesium aspartate","Zzzxq nonsense control"]
out=csv.writer(open('eu_mg_probe.tsv','w'),delimiter='\t',lineterminator='\n')
out.writerow(["query","novel_food_entries","novel_food_status","novel_food_names","health_claim_entries","claim_status_counts"])
for q in names:
    t=e.norm(q)
    a=[x for s,x in nft if e.has(t,s)]; b=[x for s,x in hct if e.has(t,s)]
    cs=collections.Counter(x.get("claim_status") for x in b)
    row=[q,len(a),";".join(sorted({str(x.get('novel_food_status')) for x in a})),";".join(sorted({(x['novel_food_display_name'] or '')[:50] for x in a})[:3]),len(b),";".join(f"{k}={v}" for k,v in sorted(cs.items()))]
    out.writerow(row); print(row)
print()
seen=set()
for s,x in hct:
    if e.has("magnesium",s) and x.get("claim_status")=="Authorised":
        c=(x['claim'] or '')[:150]
        if c not in seen:
            seen.add(c); print(x['policy_item_code'],'|',x['nutrient_subst_food_no_html'][:40],'|',c)
