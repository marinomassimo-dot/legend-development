#!/usr/bin/env python3
"""Lane A (ADV-031): coverage figures on the digraph pasted at the end of the operator input. Usage: lane_a_graph_pasted.py INPUT.md (the stored input, sha256 7c6a7195...)."""
import re, sys, json
if len(sys.argv)!=2 or sys.argv[1] in ("-h","--help"):
    print(__doc__); sys.exit(0 if len(sys.argv)==2 else 2)
t=open(sys.argv[1]).read()
g=t.split("digraph wwox_ketamine")[1].split("\n}\n")[0]
def nm(s): return re.sub(r"\\n"," ",s.strip().strip('"')).replace("  "," ")
edges=[]; attrs=[]
for line in g.splitlines():
    line=line.strip().rstrip(";")
    if "->" not in line: continue
    lab=re.search(r"\[(.*)\]$",line); body=re.sub(r"\s*\[.*\]$","",line)
    parts=[nm(p) for p in body.split("->")]
    for a,b in zip(parts,parts[1:]):
        edges.append((a,b,lab.group(1) if lab and (a,b)==(parts[-2],parts[-1]) else ""))
interv={"Acute ketamine","Memantine","Prolonged ketamine","AAV9-WWOX"}
comp={"NMDAR component","Gap junction component"}
path_edges=[(a,b) for a,b,l in edges if a not in interv and b not in comp and a not in comp]
nodes=sorted({x for e in path_edges for x in e})
print("pathophysiology nodes",len(nodes)); [print("  ",n) for n in nodes]
print("edges among them",len(path_edges),"| all edges in digraph",len(edges))
adj={}
for a,b in path_edges: adj.setdefault(a,[]).append(b)
ROOT="Biallelic WWOX LoF lesion"; HS="Neocortical network hypersynchrony"; SZ="Early-onset drug- resistant seizures"
print([n for n in nodes if "seizure" in n.lower()])
SZ=[n for n in nodes if "seizure" in n.lower()][0]; HS=[n for n in nodes if "hypersync" in n.lower()][0]; ROOT=[n for n in nodes if "Biallelic" in n][0]
WNT=[n for n in nodes if n.startswith("Wnt")][0]
def reach(src,removed=frozenset()):
    seen=set(); st=[src]
    while st:
        x=st.pop()
        for y in adj.get(x,[]):
            if y in removed or y in seen: continue
            seen.add(y); st.append(y)
    return seen
def paths(a,b,cur=None):
    cur=(cur or [])+[a]
    if a==b: return [cur]
    out=[]
    for y in adj.get(a,[]): out+=paths(y,b,cur)
    return out
P=paths(ROOT,SZ); print("root->seizure paths:",len(P),"all via hypersync:",all(HS in p for p in P))
for p in P: print("   "," > ".join(x[:22] for x in p))
base=reach(ROOT); print("root-reachable nodes",len(base))
ATR=[n for n in nodes if "atrophy" in n.lower()][0]; MORT=[n for n in nodes if "mortality" in n.lower()][0]; DEV=[n for n in nodes if "developmental" in n.lower()][0]
outcome=[SZ,ATR,MORT,DEV]
D1=base-{ATR,MORT}   # 14: all but root, atrophy, mortality
D2=base              # 16
ivs={"AAV9-WWOX (root)":[ROOT],"Acute ketamine (bursting+Wnt)":[HS,WNT],"Ketamine NMDAR arm only (bursting)":[HS],"ASM (seizure node)":[SZ],"Lithium (Wnt)":[WNT]}
print("\nintervention | removed-unreachable (incl. the removed node itself) | D1/14 | D2/16 | outcome nodes unreachable /4")
for k,rem in ivs.items():
    after=reach(ROOT,frozenset(rem)); lost=base if rem==[ROOT] else base-after      # deleting the root makes every node unreachable
    d1=len(lost&D1); d2=len(lost&D2)
    oc=sum(1 for o in outcome if o in lost)
    print(f"{k:38s} lost={len(lost):2d} D1 {d1}/14={100*d1/14:5.1f}  D2 {d2}/16={100*d2/16:5.1f}  outcome {oc}/4   lost nodes: {sorted(x[:14] for x in lost)}")
# nodes not reachable from bursting
down=reach(HS); print("\ndownstream of bursting (excl itself):",len(down),[x[:20] for x in down])
print("outside the subgraph reachable from bursting incl itself:",17-len(down)-1)
print("17 nodes minus bursting minus downstream minus root:",17-len(down)-2)
