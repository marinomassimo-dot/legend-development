import subprocess, numpy as np
def load(f):
    r=subprocess.run(['convert',f,'-colorspace','Gray','-depth','8','pgm:-'],capture_output=True).stdout
    p=r.split(b'\n',3); w,h=map(int,p[1].split()); return np.frombuffer(p[3],dtype=np.uint8).reshape(h,w).astype(float)
def lanes(G,n,trim=0.15):
    bg=np.percentile(G,60); e=np.linspace(0,G.shape[1],n+1); out=[]
    for i in range(n):
        a,b=int(e[i]),int(e[i+1]); w=b-a; a+=int(w*trim); b-=int(w*trim)
        out.append(np.clip(bg-G[:,a:b],0,None).sum())
    return np.array(out)
W=lanes(load('im-005.png'),5); P=lanes(load('im-006.png'),5); A=lanes(load('im-007.png'),5)
names=['Ctrl','1.0','2.0','3.0','4.0']
print('WWOX/actin',' '.join(f'{n}:{x:.3f}' for n,x in zip(names,W/A)))
print('rel to ctrl',' '.join(f'{n}:{x:.2f}' for n,x in zip(names,(W/A)/(W[0]/A[0]))))
print('P27/actin  ',' '.join(f'{n}:{x:.3f}' for n,x in zip(names,P/A)))
print('actin raw  ',' '.join(f'{n}:{x:.0f}' for n,x in zip(names,A)))
