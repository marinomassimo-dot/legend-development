import subprocess, numpy as np
r=subprocess.run(['convert','/home/desktop/legend-development/files/fulltext/PMID28749468_assets/cddis2017346f5.jpg','-colorspace','Gray','-depth','8','pgm:-'],capture_output=True).stdout
p=r.split(b'\n',3); w,h=map(int,p[1].split()); G=np.frombuffer(p[3],dtype=np.uint8).reshape(h,w).astype(float)
def lanes(xspan,y0,y1,n=4):
    x0,x1=xspan; e=np.linspace(x0,x1,n+1); s=G[y0:y1,x0:x1]; bg=np.percentile(s,50); out=[]
    for i in range(n):
        a=int(e[i]-x0); b=int(e[i+1]-x0); wd=b-a; a+=wd//5; b-=wd//5
        out.append(np.clip(bg-s[:,a:b],0,None).sum())
    return np.array(out)
U=(165,255); P=(262,350)
names=['W7','W8','V9','Vp2']
# actin row: locate by scanning for the darkest rows near y 385-415
col=G[380:420,165:350].mean(axis=1); ya=380+int(np.argmin(col)); print('actin centre row',ya)
act=np.concatenate([lanes(U,ya-5,ya+6),lanes(P,ya-5,ya+6)])
for label,(y0,y1) in {'pIRE1 110 band (y191-199)':(191,200),'pIRE1 upper band (y173-182)':(173,182)}.items():
    v=np.concatenate([lanes(U,y0,y1),lanes(P,y0,y1)])/act
    print(label); print('  untreated',' '.join(f'{n}:{x:.3f}' for n,x in zip(names,v[:4]))); print('  paclitaxel',' '.join(f'{n}:{x:.3f}' for n,x in zip(names,v[4:])))
    print('  pac mean WWOX(7,8)=%.3f  mean vector(9,p2)=%.3f  ratio %.2f'%(v[4:6].mean(),v[6:8].mean(),v[4:6].mean()/v[6:8].mean()))
