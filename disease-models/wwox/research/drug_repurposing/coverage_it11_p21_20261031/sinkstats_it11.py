#!/usr/bin/env python3
"""IT11 P2.1: how many usable families can receive an indirect score at all (signed target with an outgoing edge in the v4 typed network); gene-class counts by symbol prefix. Read-only. Output to stdout (saved as sinkstats_it11.txt)."""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import sys,csv,gzip,importlib.util,collections,re
from pathlib import Path
DR=str(Path(__file__).resolve().parent.parent)+'/'
sys.argv=['x','run']
spec=importlib.util.spec_from_file_location('m4',DR+'generation_it10_p1_20261031/engine_v4/seed_engine_v4.py'); m=importlib.util.module_from_spec(spec); sys.modules['m4']=m; spec.loader.exec_module(m)
E=m.read_edges4()
out=collections.Counter(e[0] for e in E); inn=collections.Counter(e[1] for e in E)
acts=collections.defaultdict(set)
for r in csv.DictReader(gzip.open(DR+'generation_it9_p2_20261030/v3/results/actions/family_actions.tsv.gz','rt'),delimiter='\t'): acts[r['family_id']].add(r['target_symbol'])
genes=set().union(*acts.values())
print('usable families',len(acts),'distinct signed target genes',len(genes))
print('genes with out-edges',sum(1 for g in genes if out[g]>0),'in network at all',sum(1 for g in genes if out[g]+inn[g]>0))
fam_sc=sum(1 for f,t in acts.items() if any(out[g]>0 for g in t))
fam_net=sum(1 for f,t in acts.items() if any(out[g]+inn[g]>0 for g in t))
print('families with >=1 signed target with out-edge',fam_sc,'; with target in network (examined)',fam_net)
pat={'ion-channel/receptor subunit (CACN|SCN|KCN|GRI|GABR|CHRN|HCN|GLR|P2RX|TRP)':r'^(CACN|SCN|KCN|GRI[ANK]|GRIN|GABR|CHRN|HCN|GLR|P2RX|TRP|ASIC|RYR)','GPCR-ish (HTR|DRD|ADR|OPR|CHRM|HRH|ADORA|GRM)':r'^(HTR|DRD|ADR[AB]|OPR|CHRM|HRH|ADORA|GRM|CNR|MC[1-5]R)','solute carrier (SLC)':r'^SLC','CYP':r'^CYP'}
for k,p in pat.items():
    gs={g for g in genes if re.match(p,g)}
    print(k,'genes',len(gs),'with out-edge',sum(1 for g in gs if out[g]>0),'in net',sum(1 for g in gs if out[g]+inn[g]>0))
