"""IT55 RP-008: mechanical census of the CORPUS placeholders listed by `unread_gold.py --all --json` (read-only; offline; standard library).
Usage: python3 -I census.py <repo_root> <unread_gold_json> <out_tsv>.
Per placeholder: tier, relevance, receipt state, PMID, PMC id in the identifier, citations in drug_repurposing and analysis, and lines in drug_repurposing that name the PMID together with a full-text declaration word.
A declaration is NOT a reading (no receipt, no locator checked here): it only marks bucket (a) candidates for a human look."""
import csv, json, re, subprocess, sys
R, J, OUT = sys.argv[1:4]
DECL = re.compile(r"read in full|full text read|FULL TEXT|full-text read|complete_fulltext|read in the original|was read", re.I)
rows = json.load(open(J)); out = []
for x in rows:
    m = re.search(r"PMID (\d+)", x["ident"]); pm = m.group(1) if m else ""
    hits = subprocess.run(["git", "-C", R, "grep", "-n", pm, "--", "disease-models/wwox/research/drug_repurposing", "disease-models/wwox/analysis"], capture_output=True, text=True).stdout.splitlines() if pm else []
    files = {h.split(":")[0] for h in hits}; dr = {f for f in files if "research/drug_repurposing" in f}
    decl = [h for h in hits if "research/drug_repurposing" in h and DECL.search(h)]
    dfiles = sorted({h.split(":")[0] for h in decl})
    rd = x["receipt_depths"]
    out.append({"id": x["id"].replace("CORPUS ", ""), "pmid": pm, "year": x["year"], "tier": x["tier"][:1], "relevance": x["relevance"], "pathway": x["pathway"][:40],
                "receipt": "+".join(rd) if rd else "none", "pmc_in_ident": "PMC" in x["ident"], "files_citing_any": len(files), "files_citing_drug_repurposing": len(dr),
                "declared_fulltext_lines_in_drug_repurposing": len(decl), "declaring_files_first3": ";".join(dfiles[:3]), "title": x["title"][:110]})
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
print(len(out), "rows;", sum(1 for o in out if o["receipt"] == "none"), "without receipt;", sum(1 for o in out if o["receipt"] == "none" and o["declared_fulltext_lines_in_drug_repurposing"]), "without receipt but a full-text declaration line in drug_repurposing")
