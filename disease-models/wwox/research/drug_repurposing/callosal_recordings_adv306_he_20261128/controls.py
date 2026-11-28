import sys, time, importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("s", Path(__file__).with_name("search.py")); s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
for term in ["myelin", '"corpus callosum"', '"optic nerve"', "Wwox", '"compound action potential"']:
    for repo, fn in s.REPOS.items():
        try:
            total, hits = fn(term); print(time.strftime("%H:%M:%SZ", time.gmtime()), repo, term, "total", total, "got", len(hits), sep="\t")
            with open("control_hits.tsv", "a") as f:
                for i, t in hits: f.write(f"{repo}\t{term}\t{i}\t{' '.join(str(t).split())[:220]}\n")
        except Exception as e:
            print(repo, term, "error", type(e).__name__, getattr(e, "code", ""), sep="\t")
        time.sleep(0.8)
