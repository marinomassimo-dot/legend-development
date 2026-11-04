"""Stdlib+numpy statistics (no scipy available): regularised incomplete beta, t and F tails, Welch t, Spearman, two-way balanced model."""
import math
import numpy as np
def _betacf(a,b,x):
    MAXIT=500;EPS=3e-14;FPMIN=1e-300
    qab=a+b;qap=a+1;qam=a-1;c=1.0;d=1-qab*x/qap
    if abs(d)<FPMIN:d=FPMIN
    d=1/d;h=d
    for m in range(1,MAXIT+1):
        m2=2*m;aa=m*(b-m)*x/((qam+m2)*(a+m2))
        d=1+aa*d
        if abs(d)<FPMIN:d=FPMIN
        c=1+aa/c
        if abs(c)<FPMIN:c=FPMIN
        d=1/d;h*=d*c
        aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2))
        d=1+aa*d
        if abs(d)<FPMIN:d=FPMIN
        c=1+aa/c
        if abs(c)<FPMIN:c=FPMIN
        d=1/d;de=d*c;h*=de
        if abs(de-1)<EPS:break
    return h
def incbeta(a,b,x):
    if x<=0:return 0.0
    if x>=1:return 1.0
    bt=math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)+a*math.log(x)+b*math.log(1-x))
    if x<(a+1)/(a+b+2):return bt*_betacf(a,b,x)/a
    return 1-bt*_betacf(b,a,1-x)/b
def t_two_sided_p(t,df):
    return incbeta(df/2.0,0.5,df/(df+t*t))
def f_sf(F,d1,d2):
    if F<=0:return 1.0
    return incbeta(d2/2.0,d1/2.0,d2/(d2+d1*F))
def t_ppf(p,df):  # upper-tail quantile for CI: returns t with two-sided prob (1-p)
    lo,hi=0.0,200.0
    for _ in range(200):
        mid=(lo+hi)/2
        if 1-t_two_sided_p(mid,df)/1.0*1.0 < p: lo=mid   # P(|T|<mid) < p
        else: hi=mid
    return (lo+hi)/2
def welch(x,y):
    x=np.asarray(x,float);y=np.asarray(y,float)
    nx,ny=len(x),len(y);vx,vy=x.var(ddof=1),y.var(ddof=1)
    se2=vx/nx+vy/ny
    t=(y.mean()-x.mean())/math.sqrt(se2)
    df=se2**2/((vx/nx)**2/(nx-1)+(vy/ny)**2/(ny-1))
    return dict(diff=y.mean()-x.mean(),t=t,df=df,p=t_two_sided_p(t,df))
def rank(a):
    a=np.asarray(a,float);o=np.argsort(a,kind='mergesort');r=np.empty(len(a));i=0
    while i<len(a):
        j=i
        while j+1<len(a) and a[o[j+1]]==a[o[i]]:j+=1
        r[o[i:j+1]]=(i+j)/2+1;i=j+1
    return r
def spearman(a,b):
    ra,rb=rank(a),rank(b)
    if ra.std()==0 or rb.std()==0:return float('nan')
    return float(np.corrcoef(ra,rb)[0,1])
def bh(ps):
    ps=np.asarray(ps,float);n=len(ps);o=np.argsort(ps);q=np.empty(n);prev=1.0
    for k in range(n-1,-1,-1):
        i=o[k];prev=min(prev,ps[i]*n/(k+1));q[i]=prev
    return q
def holm(ps):
    ps=np.asarray(ps,float);n=len(ps);o=np.argsort(ps);q=np.empty(n);run=0.0
    for k,i in enumerate(o):
        run=max(run,min(1.0,(n-k)*ps[i]));q[i]=run
    return q
def twoway(cells):
    """cells: dict {(a,b): array}, a in {0,1} (RNAi: 0 ctrl,1 Wwox), b in {0,1} (0 LacZ,1 Abeta). Balanced or not (uses cell means, harmonic n).
    Returns effects on the supplied (log2) scale with pooled-MSE t tests (df = N-4)."""
    m={k:np.mean(v) for k,v in cells.items()};n={k:len(v) for k,v in cells.items()}
    N=sum(n.values());sse=sum(((np.asarray(v)-m[k])**2).sum() for k,v in cells.items());df=N-4;mse=sse/df
    def contrast(w):
        est=sum(w[k]*m[k] for k in w);var=mse*sum(w[k]**2/n[k] for k in w)
        t=est/math.sqrt(var);p=t_two_sided_p(t,df);tc=t_ppf(0.95,df)
        return dict(est=est,se=math.sqrt(var),t=t,p=p,F=t*t,ci95=(est-tc*math.sqrt(var),est+tc*math.sqrt(var)))
    out={}
    out['KD_in_LacZ']=contrast({(1,0):1,(0,0):-1})
    out['KD_in_Abeta']=contrast({(1,1):1,(0,1):-1})
    out['KD_main']=contrast({(1,0):.5,(1,1):.5,(0,0):-.5,(0,1):-.5})
    out['Abeta_main']=contrast({(0,1):.5,(1,1):.5,(0,0):-.5,(1,0):-.5})
    out['Abeta_in_ctrl']=contrast({(0,1):1,(0,0):-1})
    out['interaction']=contrast({(1,1):1,(0,1):-1,(1,0):-1,(0,0):1})
    out['_mse']=mse;out['_df']=df
    return out
