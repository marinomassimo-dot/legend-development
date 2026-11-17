#!/usr/bin/env python3
"""Lane A (ADV-031): coverage figures on the graph of the dismech entry itself (15 curated edges plus 3 implied), read from a copy of kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml (public release v0.1.48 of the Disease Mechanisms KB, file kb.zip). Usage: lane_a_graph_kb.py ENTRY.yaml. Needs PyYAML."""
import sys,collections,json
import yaml
if len(sys.argv)!=2 or sys.argv[1] in ("-h","--help"):
    print(__doc__); sys.exit(0 if len(sys.argv)==2 else 2)
d=yaml.safe_load(open(sys.argv[1])); pp=d["pathophysiology"]
nm=lambda s:s
edges=[(n["name"],x["target"]) for n in pp for x in (n.get("downstream") or [])]
names=[n["name"] for n in pp]
ROOT=names[0]; SC="Loss of WWOX Scaffold Function"
imp=[(SC,"Increased Excitatory Synaptic Drive"),(SC,"Reduced Inhibitory Synaptic Drive"),(SC,"Intrinsic Neuronal Hyperexcitability")]
def run(E,label):
    adj=collections.defaultdict(list)
    for a,b in E: adj[a].append(b)
    def reach(src,rem=frozenset()):
        seen=set(); st=[src]
        while st:
            x=st.pop()
            for y in adj[x]:
                if y in rem or y in seen: continue
                seen.add(y); st.append(y)
        return seen
    HS="Neocortical Network Hypersynchrony"; SZ="Early-Onset Drug-Resistant Seizures"; WNT="Wnt/GSK-3beta Signalling Dysregulation"
    ATR="Progressive Cerebral and Optic Atrophy"; MORT="Genotype-Stratified Mortality Risk"; DEV="Profound Developmental Impairment"
    base=reach(ROOT); N=len(base)
    def paths(a,b,cur=()):
        cur=cur+(a,)
        if a==b: return [cur]
        return [p for y in adj[a] for p in paths(y,b,cur)]
    P=paths(ROOT,SZ)
    print(f"--- {label}: edges {len(E)}; root-reachable nodes {N}; root->seizure paths {len(P)} (all via bursting: {all(HS in p for p in P)}); orphans (no parent, not root): {[n for n in names if n!=ROOT and not any(b==n for _,b in E)]}")
    for k,rem in {"AAV9 (root)":[ROOT],"Acute ketamine (bursting+Wnt)":[HS,WNT],"NMDAR arm only (bursting)":[HS],"ASM (seizure node)":[SZ],"Lithium (Wnt)":[WNT]}.items():
        if rem==[ROOT]: lost=base
        else: lost=base-reach(ROOT,frozenset(rem))
        oc=[o for o in (SZ,ATR,MORT,DEV) if o in lost or o not in base]     # counts the nodes that were never reachable (orphans) as blocked
        oc2=[o for o in (SZ,ATR,MORT,DEV) if o in lost]                       # counts only outcome nodes that were reachable and became unreachable
        print(f"  {k:32s} unreachable {len(lost)}/{N} = {100*len(lost)/N:5.1f}%   outcome nodes blocked: {len(oc2)}/4 (only those reachable before); {len(oc)}/4 (orphans counted as blocked)")
    down=reach(HS); print("  downstream of bursting (excl. itself):",len(down),"| nodes outside bursting+downstream:",len(names)-1-len(down))
run(edges+imp,"KB entry graph: 15 curated + 3 implied (the text's own definition)")
run(edges,"KB entry graph: 15 curated only")
