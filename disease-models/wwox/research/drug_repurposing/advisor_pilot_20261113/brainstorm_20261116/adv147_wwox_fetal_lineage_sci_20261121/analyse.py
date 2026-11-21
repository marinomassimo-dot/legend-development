"""ADV-147 analysis (SCI X). python3 -I analyse.py ; inputs: cd_rows.json, cd_meta.tsv (job scratch). Stdlib only."""
import json,csv,math,statistics,collections
d=json.load(open("cd_rows.json")); hdr=d["hdr"]; rows=d["rows"]
meta={r[0]:r for r in list(csv.reader(open("cd_meta.tsv"),delimiter="\t"))[1:]}
G={}
for n in "EN-PFC1 EN-PFC2 EN-PFC3 EN-V1-1 EN-V1-2 EN-V1-3 nEN-early1 nEN-early2 nEN-late".split(): G[n]="excitatory"
for n in "IN-CTX-CGE1 IN-CTX-CGE2 IN-CTX-MGE1 IN-CTX-MGE2 IN-STR nIN1 nIN2 nIN3 nIN4 nIN5".split(): G[n]="inhibitory_neurons"
for n in "MGE-RG1 MGE-RG2 MGE-IPC1 MGE-IPC2 MGE-IPC3 MGE-div".split(): G[n]="inhibitory_progenitors"
for n in "vRG oRG tRG RG-early RG-div1 RG-div2 Glyc".split(): G[n]="radial_glia"
for n in "IPC-div1 IPC-div2 IPC-nEN1 IPC-nEN2 IPC-nEN3".split(): G[n]="cortical_IPC"
for n in "Astrocyte OPC Microglia Mural Endothelial Choroid".split(): G[n]="glia_other"
cells=[c for c in hdr if c in meta and meta[c][1] in G]
idx={c:i for i,c in enumerate(hdr)}
def det(gene,sel): 
    v=rows[gene]; k=sum(1 for c in sel if float(v[idx[c]])>0); return k,len(sel)
def wilson(k,n,z=1.96):
    p=k/n; den=1+z*z/n; c=(p+z*z/(2*n))/den; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den; return p,c-h,c+h
allk,alln=det("WWOX",cells); w_all=allk/alln
pool="HPRT1 TBP POLR2A YWHAZ PPIA UBE2D3 CSNK2B PSMB4 ARF1 TMEM59 SDHA GUSB TFRC HMBS PGK1 RAB7A VCP EEF2 NACA SNRPD1".split()
pa={g:det(g,cells)[0]/alln for g in pool}
ctrl=[g for g in pool if abs(pa[g]-w_all)<=0.25*w_all]
print("assigned cells",alln,"WWOX dataset-wide detection",round(w_all,3))
print("pool detection:",{g:round(v,3) for g,v in pa.items()})
print("matched controls:",ctrl,len(ctrl))
groups=collections.OrderedDict()
for c in cells: groups.setdefault(G[meta[c][1]],[]).append(c)
res={}
for gname,sel in groups.items():
    k,n=det("WWOX",sel); p,lo,hi=wilson(k,n)
    cf=[det(g,sel)[0]/n for g in ctrl]; med=statistics.median(cf) if cf else float("nan")
    res[gname]=(p,med)
    print(f"{gname:24s} n={n:5d} WWOX {k}/{n}={p:.3f} [{lo:.3f},{hi:.3f}] control median {med:.3f} ratio {p/med if med else float('nan'):.2f}")
r={g:res[g][0]/res[g][1] for g in res}
print("V2 inhibitory neurons / excitatory ratio:", round(r["inhibitory_neurons"]/r["excitatory"],2))
for g in ("inhibitory_progenitors","radial_glia","cortical_IPC"): print("V3",g,"/ excitatory:",round(r[g]/r["excitatory"],2))
print("--- cluster level (WWOX detection fraction)")
cl=collections.OrderedDict()
for c in cells: cl.setdefault(meta[c][1],[]).append(c)
for name,sel in sorted(cl.items(), key=lambda x:(G[x[0]],x[0])):
    k,n=det("WWOX",sel); print(f"{G[name]:24s} {name:12s} n={n:4d} {k/n:.3f}")
