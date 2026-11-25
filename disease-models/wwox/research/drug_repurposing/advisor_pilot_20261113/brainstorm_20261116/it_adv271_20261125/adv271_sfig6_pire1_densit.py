import subprocess, numpy as np
r=subprocess.run(['convert','sf6-000.png','-colorspace','Gray','-depth','8','pgm:-'],capture_output=True).stdout
p=r.split(b'\n',3); w,h=map(int,p[1].split()); G=np.frombuffer(p[3],dtype=np.uint8).reshape(h,w).astype(float)
s=2238/1400
cx=[150,205,262,322,380,440,495,555]; names=['W8 untr','W8 pac24','W8 tg6','W8 tg24','V9 untr','V9 pac24','V9 tg6','V9 tg24']
def band(y0,y1,half=20):
    out=[]
    for c in cx:
        a=int((c-half)*s); b=int((c+half)*s); reg=G[int(y0*s):int(y1*s),a:b]
        out.append(reg)
    return out
# background from the strip median; pIRE-1 band window around the 110 kDa arrow (disp y 492-512); actin disp y 675-715
def sig(regs,bgregs):
    return [max(0,np.percentile(bg,50)-r).sum() if False else np.clip(np.percentile(bg,50)-r,0,None).sum() for r,bg in zip(regs,bgregs)]
ire=band(493,513); ire_bg=band(425,555)
act=band(675,715); act_bg=band(645,745)
si=sig(ire,ire_bg); sa=sig(act,act_bg)
print('lane           pIRE1   actin   ratio')
for n,i,a in zip(names,si,sa): print(f'{n:10s} {i:9.0f} {a:9.0f} {i/a:8.3f}')
