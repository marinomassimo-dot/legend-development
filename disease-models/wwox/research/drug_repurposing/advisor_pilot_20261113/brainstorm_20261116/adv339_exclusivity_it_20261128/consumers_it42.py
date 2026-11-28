"""ADV-339 continuation (IT42): per claim, how many candidate sentences the net lists and how many repurposing consumers cite the claim.
Consumers = files under drug_repurposing/ (portfolio, roadmap, cards, cards_early, dossiers) that name 'CLAIM nnn'. Usage: python3 consumers_it42.py enum.json"""
import json, re, sys, subprocess, collections
enum = json.load(open(sys.argv[1]))
per = collections.Counter(e["claim"] for e in enum)
base = "disease-models/wwox/research/drug_repurposing"
files = subprocess.run(["git", "ls-files", base], capture_output=True, text=True).stdout.split("\n")
files = [f for f in files if f.endswith((".md", ".tsv", ".json")) and "/view/" not in f and "/join/" not in f and "/advisor_pilot_" not in f and "ranking_it8" not in f]
cites = collections.defaultdict(set)
for f in files:
    try:
        t = open(f, encoding="utf-8").read()
    except Exception:
        continue
    for m in set(re.findall(r"CLAIM[ _#]?0*(\d{1,3})\b", t)):
        cites[m.zfill(3)].add(f.split("/")[0] if "/" not in f[len(base) + 1:] else f[len(base) + 1:].split("/")[0])
rows = []
for c, n in per.items():
    k = c.split()[1]
    rows.append((k, n, len(cites.get(k, ())), sorted(cites.get(k, ()))[:3]))
rows.sort(key=lambda r: (-r[2], r[0]))
print("claim\tcandidate_sentences\tconsumer_folders\texamples")
for k, n, c, ex in rows:
    if int(k) >= 13:
        print(f"{k}\t{n}\t{c}\t{';'.join(ex)}")
