import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); os.chdir(os.environ['D'])
import statistics as S
from pgm_reader_adv251_it_20261125 import rd
w0,h0,H=rd('g0.pgm'); w1,h1,X=rd('g1.pgm')
C={'WT':130,'1C':227,'2C':325,'1C_AAV':422,'2C_AAV':526}; HALF=40
def dark(P,c,r): return [255-P[r][x] for x in range(c-HALF,c+HALF+1)]
def sig(P,c,r0,r1,bgr):
    bg=S.median([v for r in bgr for v in dark(P,c,r)])
    return sum(S.mean(dark(P,c,r))-bg for r in range(r0,r1+1)), bg
def peak(P,c,lo,hi): return max(range(lo,hi+1),key=lambda r:S.mean(dark(P,c,r)))
res={}
# WWOX fixed window from WT peak
wp=peak(X,C['WT'],80,110); print('WT WWOX peak row',wp); r0,r1=wp-6,wp+6
bgX=list(range(r0-50,r0-20))+list(range(r1+20,min(r1+51,h1)))
print('WWOX window',r0,r1,'bg rows',bgX[0],bgX[-1])
for variant in ('perlane_peak','fixedwin'):
    R={}
    for n,c in C.items():
        if variant=='perlane_peak': hp=peak(H,c,55,85); a,b=hp-8,hp+8
        else: hp=peak(H,C['WT'],55,85); a,b=hp-8,hp+8
        bgH=list(range(max(a-50,0),a-20))+list(range(b+20,min(b+40,h0)))
        sx,bx=sig(X,c,r0,r1,bgX); sh,bh=sig(H,c,a,b,bgH); R[n]=(sx,sh,bx,bh,a,b)
    print(variant)
    for n,(sx,sh,bx,bh,a,b) in R.items():
        ratio=(max(sx,0)/sh)/(max(R['WT'][0],1e-9)/R['WT'][1]); raw=(sx/sh)/(R['WT'][0]/R['WT'][1])
        print(f'  {n:7s} WWOX net {sx:8.1f} (bg {bx:.0f})  HSP90 net {sh:8.1f} (rows {a}-{b}, bg {bh:.0f})  ratio {raw:.3f} (floored {ratio:.3f})')
# saturation check WT WWOX window: darkest pixel values
allmin=min(min(r) for r in X); print('image min grey (WWOX strip)',allmin)
print('WT band: per-row min grey in window',[ (r,min(X[r][x] for x in range(C['WT']-HALF,C['WT']+HALF+1))) for r in range(r0,r1+1)])
print('WT band: per-row mean darkness',[ (r,round(S.mean(dark(X,C['WT'],r)))) for r in range(r0,r1+1)])
# secondary exploratory: AAV band at own position (rows 70-84)
for n in ('1C_AAV','2C_AAV'):
    c=C[n]; p=peak(X,c,66,86); sx,bx=sig(X,c,p-6,p+6,bgX); print('EXPLORATORY',n,'band at own peak row',p,'net',round(sx,1))
