import subprocess, numpy as np, sys
F='/home/desktop/legend-development/files/fulltext/PMID28749468_assets/cddis2017346f4.jpg'
def load():
    r=subprocess.run(['convert',F,'-colorspace','Gray','-depth','8','pgm:-'],capture_output=True).stdout
    p=r.split(b'\n',3); w,h=map(int,p[1].split()); return np.frombuffer(p[3],dtype=np.uint8).reshape(h,w).astype(float)
G=load()
def lanes(x0,x1,y0,y1):
    s=G[y0:y1,x0:x1]; bg=np.percentile(s,50); out=[]
    edges=np.linspace(0,s.shape[1],10)
    for i in range(9):
        a,b=int(edges[i]),int(edges[i+1]); w=b-a; a+=w//5; b-=w//5   # central 60% of the lane
        out.append(np.clip(bg-s[:,a:b],0,None).sum())
    return np.array(out)
T=['0','1','2','4','8','12','18','24','32']
spec={'a':{'WWOX-8':{'hsp':(110,328,20,39),'peif':(110,328,116,135)},'Vector-9':{'hsp':(408,626,16,40),'peif':(408,626,116,136)}},
      'b':{'WWOX-8':{'hsp':(112,326,220,232),'peif':(112,326,306,331)},'Vector-9':{'hsp':(408,622,218,238),'peif':(408,622,307,329)}}}
for pan,d in spec.items():
    print('panel',pan)
    res={}
    for line,r in d.items():
        h=lanes(*r['hsp']); p=lanes(*r['peif']); res[line]=p/np.where(h>0,h,np.nan)
        print(' ',line,'p-eIF2a/Hsp60 by h:',' '.join(f'{t}:{v:.2f}' for t,v in zip(T,res[line])))
    w=res['WWOX-8']; v=res['Vector-9']
    print('  ratio WWOX-8/Vector-9 (hours 2..24):',' '.join(f'{T[i]}:{w[i]/v[i]:.2f}' if v[i]>0.01 else f'{T[i]}:na' for i in range(2,8)))
