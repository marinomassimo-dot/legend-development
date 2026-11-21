"""ADV-135: for a fixed list of human WWOX-spectrum PMIDs, list every sentence of the held texts that names an analyte, a work-up word or a laboratory word.
Usage: python3 -I extract_candidate_sentences_adv135.py <scan_out/counts.tsv> <dossier_dir> <fulltext_dir> <out.tsv> PMID [PMID ...]
A listing is a prompt to read, never a finding. Reads text only."""
import csv, sys, os, re, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sc", os.path.join(here, "scan_held_adv135.py")); sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
counts, dos, ft, out = sys.argv[1:5]; pmids = sys.argv[5:]
rows = list(csv.DictReader(open(counts, encoding="utf-8"), delimiter="\t"))
RX = "|".join(v for k, v in sc.ANALYTES.items() if k != "failure_to_thrive") + r"|\bnormal\b|\bunremarkable\b|\bwithin normal\b|\bnegative\b|\bfailure to thrive\b|\bhypotonia\b"
core = "|".join(v for k, v in sc.ANALYTES.items() if k not in ("failure_to_thrive", "lab_general"))
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t"); w.writerow(["pmid", "source", "analyte_or_cue", "sentence"])
    for p in pmids:
        srcs = [r for r in rows if r["pmid"] == p and not r["path"].startswith(("d5b", "origin", "scientist", "PPR"))]
        # prefer held full text, else the dossier
        ordered = sorted(srcs, key=lambda r: (r["kind"] != "fulltext", -int(r["bytes"])))
        seen = set()
        for r in ordered[:2]:
            root = ft if r["kind"] == "fulltext" else dos
            t = sc.read_text(os.path.join(root, r["path"]))
            for s in sc.sentences(t):
                if re.search(core, s, re.I) or (re.search(r"\blaborator\w*|\bbiochemical\w*|\bwithin normal limits\b|\bmetabolic\b", s, re.I)):
                    k = s[:100]
                    if k in seen: continue
                    seen.add(k)
                    w.writerow([p, r["kind"] + ":" + r["path"], "", s.strip()[:900]])
