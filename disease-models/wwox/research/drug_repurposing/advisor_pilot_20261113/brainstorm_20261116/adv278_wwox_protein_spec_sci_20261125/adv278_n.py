"""ADV-278 n arithmetic: paired one-sample t on log2 ratios, Monte Carlo power (no scipy)."""
import random, math, statistics as st
random.seed(278)
T975={2:4.303,3:3.182,4:2.776,5:2.571,6:2.447,7:2.365,8:2.306,9:2.262,10:2.228,11:2.201,12:2.179,15:2.145}
def power(n,s,d,N=20000):
    tc=T975[n-1]; hit=0
    for _ in range(N):
        x=[random.gauss(d,s) for _ in range(n)]
        m=st.mean(x); sd=st.stdev(x)
        if sd>0 and abs(m)/(sd/math.sqrt(n))>tc: hit+=1
    return hit/N
def mde(n,s):
    lo,hi=0.0,4.0
    for _ in range(14):
        mid=(lo+hi)/2
        if power(n,s,mid,4000)>=0.8: hi=mid
        else: lo=mid
    return hi
print('n\ts_log2\tMDE_log2\tMDE_fold(up)\tMDE_fold(down)\tpower_at_1.5x')
for s in (0.25,0.43,0.60):
    for n in (3,4,6,8):
        m=mde(n,s)
        print(n,s,round(m,2),round(2**m,2),round(2**-m,2),round(power(n,s,math.log2(1.5),6000),2),sep='\t')
