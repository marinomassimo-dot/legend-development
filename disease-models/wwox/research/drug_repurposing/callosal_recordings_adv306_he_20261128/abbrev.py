import sys,time,importlib.util,re
from pathlib import Path
spec=importlib.util.spec_from_file_location("s",Path(__file__).with_name("search.py")); s=importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
pat=re.compile(r"callos|optic nerve|myelin|white matter|shiver|axon|wwox|conduct|\bCAPs?\b",re.I)
seen=set()
for term in ["corpus callosum CAPs","optic nerve CAPs","shiverer CAPs","corpus callosum conduction","optic nerve conduction velocity"]:
    for repo in ["datacite","zenodo","figshare","dryad"]:
        try:
            total,hits=s.REPOS[repo](term)
            print(f"{time.strftime('%FT%TZ',time.gmtime())}\t{repo}\tadded\t{term}\tok\t{total}\t{len(hits)}")
            for i,t in hits:
                if pat.search(t) and ("dataset" in t or repo in("datacite","dryad")) and i not in seen: seen.add(i); print("HIT",repo,i,t[:130])
        except Exception as e: print(repo,term,"error",type(e).__name__,getattr(e,"code",""))
        time.sleep(0.8)
