"""ADV-147 post hoc (labelled): WWOX detection stratified by per-cell genes-detected tercile; stdlib only."""
import json,csv,math,collections,statistics
exec(open("analyse.py").read().split("allk,alln")[0])   # reuse G, cells, idx, rows, meta
depth=json.load(open("depth.json"))
vals=sorted(depth[c] for c in cells); t1=vals[len(vals)//3]; t2=vals[2*len(vals)//3]
def terc(c): d=depth[c]; return 0 if d<=t1 else (1 if d<=t2 else 2)
w=rows["WWOX"]
out=collections.defaultdict(lambda:[0,0])
for c in cells:
    g=G[meta[c][1]]; k=terc(c); out[(g,k)][1]+=1; out[(g,k)][0]+= float(w[idx[c]])>0
print("terciles of genes detected: <=",t1,"<=",t2)
for g in ("excitatory","inhibitory_neurons","inhibitory_progenitors","radial_glia","cortical_IPC","glia_other"):
    print(f"{g:24s}",*[f"T{k}:{out[(g,k)][0]}/{out[(g,k)][1]}={out[(g,k)][0]/max(1,out[(g,k)][1]):.3f}" for k in range(3)], " median genes",statistics.median(depth[c] for c in cells if G[meta[c][1]]==g))
# Mantel-Haenszel style pooled ratio inhibitory neurons vs excitatory across terciles
num=den=0
for k in range(3):
    a,n1=out[("inhibitory_neurons",k)]; b,n0=out[("excitatory",k)]
    N=n1+n0
    if N: num+=a*n0/N; den+=b*n1/N
print("Mantel-Haenszel risk ratio inhibitory neurons vs excitatory (strata = genes-detected terciles):",round(num/den,2))
