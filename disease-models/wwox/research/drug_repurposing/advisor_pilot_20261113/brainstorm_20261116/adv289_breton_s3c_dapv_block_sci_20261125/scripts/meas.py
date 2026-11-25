import sys; sys.path.insert(0,'.')
from load import load
import numpy as np
im=load('image3.ppm')
def mask(col,tol):
    return (np.abs(im-np.array(col)).max(axis=2)<=tol)
def erode(m,n):
    for _ in range(n):
        p=np.pad(m,1)
        m=p[1:-1,1:-1]&p[:-2,1:-1]&p[2:,1:-1]&p[1:-1,:-2]&p[1:-1,2:]
    return m
def label(m):
    h,w=m.shape; lab=np.zeros((h,w),int); n=0; comps=[]
    for y in range(h):
        for x in range(w):
            if m[y,x] and not lab[y,x]:
                n+=1; st=[(y,x)]; lab[y,x]=n; pts=[]
                while st:
                    a,b=st.pop(); pts.append((a,b))
                    for da,db in((1,0),(-1,0),(0,1),(0,-1)):
                        c,d=a+da,b+db
                        if 0<=c<h and 0<=d<w and m[c,d] and not lab[c,d]:
                            lab[c,d]=n; st.append((c,d))
                comps.append(pts)
    return comps
def blobs(col,tol,reg,er):
    y0,y1,x0,x1=reg
    m=mask(col,tol)[y0:y1,x0:x1]
    m=erode(m,er)
    out=[]
    for pts in label(m):
        if len(pts)<8: continue
        ys=np.array([p[0] for p in pts])+y0; xs=np.array([p[1] for p in pts])+x0
        out.append((xs.mean(),ys.mean(),len(pts),xs.min(),xs.max(),ys.min(),ys.max()))
    return sorted(out)
if __name__=='__main__':
    for panel,reg in (('C',(380,640,965,1400)),('B',(30,275,965,1400))):
        for name,col,tol in (('red',(255,0,0),40),('dapv/black',(125,125,125) if panel=='C' else (0,0,0),30),('wash',(203,203,203),20)):
            if panel=='B' and name=='wash': continue
            print(panel,name)
            for b in blobs(col,tol,reg,3): print('  x=%.1f y=%.1f n=%d bbox x[%d,%d] y[%d,%d]'%b)
