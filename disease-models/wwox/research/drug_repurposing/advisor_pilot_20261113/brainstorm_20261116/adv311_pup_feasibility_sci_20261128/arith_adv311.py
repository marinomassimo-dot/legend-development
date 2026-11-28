"""ADV-311 arithmetic (SCI 2026-11-28). Held numbers only: Cheng 2020 suppl. methods (5.1% N=177 WD1 -> 9; 6.5% N=785 WD234 -> 51),
Ludes-Meyers 2009 Table 1 (WT 39, HET 85, KO 30, total 154; expected 38.5/77/38.5; chi2 p=0.257; litter size 3-11, mean 7.75, 10 matings, genotyped at 3 days),
the brief's L=7 and its knockout counts. No dose, no breeding advice, no cost."""
import math
def wilson(k,n,z=1.96):
    p=k/n; d=1+z*z/n; c=p+z*z/(2*n); a=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n)); return (c-a)/d,(c+a)/d
def fisher_two_sided(a,b,c,d):
    # table [[a,b],[c,d]]
    r1=a+b; r2=c+d; c1=a+c; n=r1+r2
    def pr(x): return math.comb(r1,x)*math.comb(r2,c1-x)/math.comb(n,c1)
    p0=pr(a); lo=max(0,c1-r2); hi=min(r1,c1)
    return sum(pr(x) for x in range(lo,hi+1) if pr(x)<=p0*(1+1e-9))
data={'Cheng WD1 (P5-P12)':(9,177),'Cheng WD234 (P5-P12)':(51,785),'Ludes-Meyers EIIA-Cre null (P3)':(30,154)}
print('FREQUENCIES (knockouts / genotyped pups)')
for k,(a,n) in data.items():
    lo,hi=wilson(a,n); print(f'  {k}: {a}/{n} = {a/n:.3f}  Wilson 95% [{lo:.3f}, {hi:.3f}]')
print('  Cheng 0.051*177 =',round(0.051*177,2),'; 0.065*785 =',round(0.065*785,2))
print('FISHER two-sided, Ludes-Meyers 30/154 vs Cheng:')
for k in list(data)[:2]:
    a,n=data[k]; print('  vs',k,'p=%.2e'%fisher_two_sided(30,154-30,a,n-a))
print('  Cheng WD1 vs WD234 p=%.2f'%fisher_two_sided(9,168,51,734))
fs={'Cheng WD1 f=0.051':0.051,'Cheng WD234 f=0.065':0.065,'Ludes-Meyers P3 f=30/154':30/154,'Mendelian 0.25':0.25}
print('\nKNOCKOUTS PER LITTER = L x f')
for L in (5,7,7.75,9):
    print('  L=%s: '%L+'; '.join(f'{k}: {L*f:.3f}' for k,f in fs.items()))
sc=[('stage 1 pilot, 6 per KO cell',6),('stage 1 pilot, 8 per KO cell',8),('11 per arm x 1 KO arm',11),('2 KO arms x 11 (stage 2)',22),('3 KO arms x 11 (brief minimum)',33),('2 KO arms x 31',62),('3 KO arms x 31',93),('plan upper bound (brief)',150),
    ('interaction, 22 per cell, 2 KO cells (ADV-061, SD 0.3)',44),('interaction low (ADV-061)',350),('interaction high (ADV-061)',630),('36 per arm x 2 (ADV-061 simple, low)',72),('109 per arm x 2 (ADV-061 simple, high)',218)]
print('\nLITTERS NEEDED = n_KO / (L x f), L = 7 (brief)')
print('%-58s %5s %9s %9s %9s %9s'%('scenario','n_KO','WD1','WD234','LudesM','Mendel'))
for name,n in sc:
    row=[math.ceil(n/(7*f)) for f in fs.values()]
    print('%-58s %5d %9d %9d %9d %9d'%(name,n,*row))
print('\nKNOCKOUTS OBTAINED IN 20 LITTERS (L=7): '+'; '.join(f'{k}: {20*7*f:.1f}' for k,f in fs.items()))
print('\nCRITICAL f = K / (cap x L), L=7')
for K in (22,33,150):
    print('  K=%d: '%K+'; '.join(f'cap {c}: f*={K/(c*7):.3f}' for c in (20,25,50,86)))
print('\nSENSITIVITY with L=5 and 9 for K=33: '+'; '.join(f'L={L}: WD1 {math.ceil(33/(L*0.051))}, WD234 {math.ceil(33/(L*0.065))}, LudesM {math.ceil(33/(L*30/154))}' for L in (5,9)))
print('\nRatio of Mendelian to observed: WD1 %.2f, WD234 %.2f, LudesM %.2f'%(0.25/0.051,0.25/0.065,0.25/(30/154)))
print('Pre-genotyping loss u (unknown): if the P3 frequency 30/154 were the birth frequency of the Cheng line, the Cheng P5-P12 survivors imply a relative KO retention of %.2f (WD1) and %.2f (WD234) between P3 and P5-12 - a comparison across two lines and laboratories, not a measurement.'%(((9/177)/(1-9/177))/((30/154)/(1-30/154)),((51/785)/(1-51/785))/((30/154)/(1-30/154))))
