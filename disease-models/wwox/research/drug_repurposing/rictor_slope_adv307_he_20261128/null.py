import itertools
def rho(a,b):
    n=len(a); return 1-6*sum((x-y)**2 for x,y in zip(a,b))/(n*(n*n-1))
base=range(1,7); v=[rho(list(base),list(p)) for p in itertools.permutations(base)]
print("n=6 permutations",len(v),"P(|rho|>=0.5)=%.3f"%(sum(abs(x)>=0.5-1e-9 for x in v)/len(v)),"P(|rho|<0.3)=%.3f"%(sum(abs(x)<0.3 for x in v)/len(v)),"smallest two-sided p=%.4f"%(sum(abs(x)>=1-1e-9 for x in v)/len(v)))
print("n=3 possible |rho|",sorted({round(abs(rho([1,2,3],list(p))),2) for p in itertools.permutations([1,2,3])}))
