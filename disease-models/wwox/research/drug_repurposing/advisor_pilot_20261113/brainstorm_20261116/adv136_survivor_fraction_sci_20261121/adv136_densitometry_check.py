import pymupdf, numpy as np, sys
D='<extracted-image-folder>/'
# panel: (file, wwox_y0,y1, num_y0,y1, hsp_y0,y1, nlanes, printed values, labels)
P={
'A':('A_cortex',30,66,70,92,100,134,11,[1,1,.02,2.2,2.1,2.6,2,.5,.9,1,1.5],'WT WT KO LD LD HD HD HD* LD* LD* LD*'),
'B':('B_mid',24,58,60,82,86,120,11,[1,2.2,.1,.9,.9,5.2,4,.1,.6,.4,.2],'WT WT KO LD LD HD HD HD* LD* LD* LD*'),
'C':('C_hippo',20,56,58,80,84,118,11,[1,2.3,.1,1.4,8.5,28.2,11.8,12.9,5,3.8,2.5],'WT WT KO LD LD HD HD HD* LD* LD* LD*'),
'D':('D_cere',20,56,58,78,82,118,11,[1,.8,.02,.1,.09,.6,.6,.2,.1,.06,.1],'WT WT KO LD LD HD HD HD* LD* LD* LD*'),
}
def load(n):
    pix=pymupdf.Pixmap(D+n+'.png'); return 255-np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)[:,:,:3].mean(2)
for k,(n,w0,w1,n0,n1,h0,h1,nl,vals,lab) in P.items():
    a=load(n)
    col=a[n0:n1].sum(0); col=np.convolve(col,np.ones(5)/5,'same')
    # lane centres from number-row clusters
    thr=col.max()*0.05; on=col>thr
    segs=[];s=None
    for x,v in enumerate(on):
        if v and s is None:s=x
        if not v and s is not None: segs.append((s,x));s=None
    # merge segments within 6px (digits)
    m=[]
    for s,e in segs:
        if m and s-m[-1][1]<9: m[-1]=(m[-1][0],e)
        else: m.append((s,e))
    cen=[(s+e)/2 for s,e in m]
    print(k,len(cen),'clusters',[round(c) for c in cen])

print()
res={}
for k,(n,w0,w1,n0,n1,h0,h1,nl,vals,lab) in P.items():
    a=load(n)
    col=a[n0:n1].sum(0); col=np.convolve(col,np.ones(5)/5,'same'); on=col>col.max()*0.05
    segs=[];s=None
    for x,v in enumerate(on):
        if v and s is None:s=x
        if not v and s is not None: segs.append((s,x));s=None
    m=[]
    for s,e in segs:
        if m and s-m[-1][1]<9: m[-1]=(m[-1][0],e)
        else: m.append((s,e))
    cen=np.array([(s+e)/2 for s,e in m])
    hw=np.median(np.diff(cen))*0.42
    def integ(y0,y1):
        st=a[y0:y1]; bg=np.percentile(st,15)
        out=[]
        for c in cen:
            x0,x1=int(c-hw),int(c+hw); out.append(np.clip(st[:,x0:x1]-bg,0,None).sum())
        return np.array(out)
    W=integ(w0,w1); H=integ(h0,h1); r=W/H
    labs=lab.split(); wt=[i for i,l in enumerate(labs) if l=='WT']
    rel1=r/r[0]; relm=r/r[wt].mean()
    pv=np.array(vals)
    print(k,n)
    print(' lane  lab   printed  densRel1  densRelWTmean  W/H')
    for i in range(nl):
        print(f"  {i+1:2d}  {labs[i]:5s}  {pv[i]:6.2f}  {rel1[i]:7.2f}  {relm[i]:7.2f}  {r[i]:.2f}")
    # rank correlation printed vs dens
    rk=lambda v:np.argsort(np.argsort(v)).astype(float)
    print(' spearman printed vs densRel1:',round(float(np.corrcoef(rk(pv),rk(rel1))[0,1]),2))
