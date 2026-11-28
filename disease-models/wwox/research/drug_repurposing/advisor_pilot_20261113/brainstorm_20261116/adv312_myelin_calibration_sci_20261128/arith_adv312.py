"""ADV-312 arithmetic (SCI 2026-11-28): effect sizes as ln(mutant or treated / control). Inputs are numbers printed in the sources (locators in the table) or ADV-304 figure readbacks (Palma)."""
import math
ln=lambda a,b: math.log(b/a)
rows=[
 # source, contrast, structural variable, control, test, conduction variable, control, test, sign (+1 if bigger=faster, -1 if bigger=slower)
 ('Palma 2022 (35372341), clemastine vs vehicle, callosum P21','myelinated axons /1e3 um2 (text, ADV-304)',287,249,'N1 velocity (ADV-304 figure readback, units as printed)',0.504,0.425,+1),
 ('Palma 2022','g-ratio small-axon bin 0-0.5 um (ADV-304 figure readback)',0.768,0.787,'N1 velocity (same)',0.504,0.425,+1),
 ('Palma 2022','g-ratio bin 0.5-1 um (ADV-304 figure readback)',0.663,0.672,'N1 velocity (same)',0.504,0.425,+1),
 ('Crawford 2010 (20858739), EAE vs normal, callosum','myelin sheath thickness um (text)',0.060,0.027,'N1 conduction velocity m/s (text)',1.82,1.69,+1),
 ('Crawford 2010, EAE vs normal','g-ratio (text)',0.87,0.94,'N1 conduction velocity m/s (text)',1.82,1.69,+1),
 ('Crawford 2010, ERbeta ligand EAE vs vehicle EAE','myelin sheath thickness um (text)',0.027,0.065,'N1 conduction velocity m/s (text)',1.69,1.92,+1),
 ('Crawford 2010, ERbeta ligand EAE vs vehicle EAE','g-ratio (text)',0.94,0.85,'N1 conduction velocity m/s (text)',1.69,1.92,+1),
 ('Nr2f1 HET vs WT (31318166), optic nerve to dLGN, adult','g-ratio P28 (text)',0.74,0.63,'latency of first evoked field-potential component ms, speed = 1/latency (text)',12.38,15.79,-1),
]
print('%-52s %-50s %8s | %-60s %8s | %s'%('contrast','structural variable','ln str','conduction variable','ln cond','|str|/|cond|'))
out=[]
for r in rows:
    s=ln(r[2],r[3]); c=ln(r[5],r[6])*r[7]
    print('%-52s %-50s %+8.3f | %-60s %+8.3f | %.2f'%(r[0][:52],r[1][:50],s,r[4][:60],c,abs(s)/abs(c)))
print()
print('Nr2f1 g-ratio direction: lower g-ratio is relatively THICKER myelin; the paper calls the P28 HET sheaths poorly compacted and the optic nerve hypomyelinated (myelinated-fibre number lower, plotted, value not read).')
print('Crawford thickness vs g-ratio, same contrast: thickness ln %.3f, g ln %.3f: the size ratio to velocity moves from %.2f to %.2f depending on the variable.'%(ln(.06,.027),ln(.87,.94),abs(ln(.06,.027))/abs(ln(1.82,1.69)),abs(ln(.87,.94))/abs(ln(1.82,1.69))))
# rank agreement across the three sources, g-ratio class, one contrast per source (Palma bin 0-0.5, Crawford EAE vs normal, Nr2f1)
st={'Palma':abs(ln(.768,.787)),'Crawford':abs(ln(.87,.94)),'Nr2f1':abs(ln(.74,.63))}
cd={'Palma':abs(ln(.504,.425)),'Crawford':abs(ln(1.82,1.69)),'Nr2f1':abs(ln(12.38,15.79))}
rk=lambda d:{k:i+1 for i,k in enumerate(sorted(d,key=lambda k:-d[k]))}
a,b=rk(st),rk(cd); n=3; d2=sum((a[k]-b[k])**2 for k in st); print('g-ratio class: struct ranks',a,'cond ranks',b,'Spearman rho (n=3, NOT stated: below the frozen 6) = %.2f'%(1-6*d2/(n*(n*n-1))))
print('Latency note, Nr2f1: latency ratio %.3f (+%.1f%%); t=-6.385 with 22 df is printed against legend N 13 (WT) and 18 (HET): 13+18-2 = 29, not 22 (as printed).'%(15.79/12.38,(15.79/12.38-1)*100))
