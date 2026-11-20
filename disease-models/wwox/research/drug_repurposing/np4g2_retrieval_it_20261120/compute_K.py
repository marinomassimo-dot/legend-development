"""Compute K, the known positives of the NP4G2 retrieval comparison, from the registry fields (written before any query).
K = PAPER records of paper_registry_current.md that name the gene (Wwox/WWOX/Wox1) AND a myelin or oligodendrocyte term in their
own fields (short title, full title, identifier, summary text of the record). Deterministic; prints a TSV. Reference-genotype class only."""
import re, sys
reg = open('disease-models/wwox/registries/paper_registry_current.md', encoding='utf-8').read()
parts = re.split(r'\n## (PAPER \d+)\n', reg)
gene = re.compile(r'\b(Wwox|WWOX|Wox1|WOX1)\b')
cell = re.compile(r'(myelin|oligodendro|OPC\b|\bMBP\b|hypomyelin|white matter)', re.I)
rows = []
for i in range(1, len(parts), 2):
    pid, body = parts[i], parts[i+1]
    body = body.split('\n---')[0]
    title = re.search(r'\*\*Full title:\*\*\s*(.*)', body)
    short = re.search(r'\*\*Short title:\*\*\s*(.*)', body)
    ident = re.search(r'\*\*Identifier:\*\*\s*(.*)', body)
    year = re.search(r'\*\*Year:\*\*\s*(.*)', body)
    if gene.search(body) and cell.search(body):
        pm = re.search(r'PMID[:\s]*([0-9]{6,9})', (ident.group(1) if ident else '') + body)
        rows.append((pid, pm.group(1) if pm else '', year.group(1).strip() if year else '', (short.group(1) if short else '').strip(), (title.group(1) if title else '').strip()))
print('paper\tpmid\tyear\tshort\tfull_title')
for r in rows: print('\t'.join(r))
print('K_size', len(rows), file=sys.stderr)
