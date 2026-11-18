# (copy of the script as run; needs PyMuPDF and numpy)
# IT independent read of Cheng 2020 Fig 7 PTZ-alone knockout curves (panels b and d, -/-). Procedure in COMMENTS below.
import sys; sys.path.insert(0,'/tmp/it56_adv063')
from load import load
import numpy as np
a=load().astype(int)
red=(a[:,:,0]>190)&(a[:,:,1]<70)&(a[:,:,2]<70)
PANELS={
 'b':dict(y6=1259.0,y0=1536.5,xlab5=269.5,xlab60=849.5,ylo=1324,yhi=1545,x_lo=205,x_hi=900),
 'd':dict(y6=1290.5,y0=1540.5,x0=1218.0,x60=1901.5,ylo=1349,yhi=1545,x_lo=1205,x_hi=1935),
}
def cal(p):
    if 'xlab5' in p:
        k=(p['xlab60']-p['xlab5'])/55.0; x0=p['xlab5']-5*k
    else:
        k=(p['x60']-p['x0'])/60.0; x0=p['x0']
    ppu=(p['y0']-p['y6'])/6.0   # px per stage unit (y0 is the larger row value for stage 0)
    return x0,k,ppu
def read1(p):
    """Read 1: marker = rows where red count within +/-3 px of the minute column is >=6; centre = mean of those rows (largest contiguous run);
       whisker top = topmost red row within +/-1 px of the column above the marker top."""
    x0,k,ppu=cal(p); out=[]
    for m in range(0,61):
        xc=int(round(x0+k*m)); sub=red[p['ylo']:p['yhi'],xc-3:xc+4]
        cnt=sub.sum(axis=1)
        rows=np.where(cnt>=6)[0]
        if len(rows)==0: out.append((m,None,None,'no_marker')); continue
        runs=np.split(rows,np.where(np.diff(rows)>1)[0]+1); run=max(runs,key=len)
        yc=p['ylo']+run.mean(); ytop_marker=p['ylo']+run[0]
        col=red[p['ylo']:p['yhi'],xc-1:xc+2].sum(axis=1)>0
        # topmost red row in the thin column, contiguous with the marker upward
        r=run[0]
        while r-1>=0 and col[r-1]: r-=1
        ytop=p['ylo']+r
        out.append((m,(p['y0']-yc)/ppu,(yc-ytop)/ppu if ytop<ytop_marker else 0.0,'ok'))
    return out
def read2(p):
    """Read 2: connected red pixels in a +/-5 px window; marker centre = row of the widest run (width>=7); whisker = highest red pixel in the window
       that lies within +/-1.5 px of the column centre, anywhere above the marker (cap included)."""
    x0,k,ppu=cal(p); out=[]
    for m in range(0,61):
        xc=x0+k*m; xi=int(round(xc)); sub=red[p['ylo']:p['yhi'],xi-5:xi+6]
        w=sub.sum(axis=1); 
        rows=np.where(w>=7)[0]
        if len(rows)==0: out.append((m,None,None,'no_marker')); continue
        runs=np.split(rows,np.where(np.diff(rows)>1)[0]+1); run=max(runs,key=len)
        yc=p['ylo']+(run[0]+run[-1])/2.0
        ys=np.where(red[p['ylo']:run[0]+p['ylo'],xi-1:xi+2].any(axis=1))[0]
        ytop=p['ylo']+ys.min() if len(ys) else None
        sem=(yc-ytop)/ppu if ytop is not None and ytop<p['ylo']+run[0] else 0.0
        out.append((m,(p['y0']-yc)/ppu,sem,'ok'))
    return out
if __name__=='__main__':
    import json
    res={}
    for name,p in PANELS.items():
        r1=read1(p); r2=read2(p); res[name]={'read1':r1,'read2':r2}
    json.dump(res,open('/tmp/it56_adv063/fig7_it_read.json','w'))
    N=6
    for name in 'bd':
        for tag in ('read1','read2'):
            r=res[name][tag]; ok=[x for x in r if x[1] is not None]
            means=np.array([x[1] for x in ok]); sems=np.array([x[2] for x in ok])
            print(name,tag,'minutes read',len(ok),'sum(mean stage) over bins',round(means.sum(),2),'peak',round(means.max(),2),'mean SEM',round(sems.mean(),3))
