import sys; sys.path.insert(0,'.')
from meas import *
yC=lambda y: 1+(530.5-y)/121.333      # panel C: ticks 2@409.5, 1.5@470.5, 1@530.5, 0.5@591.5
yB=lambda y: 0.1+(258.5-y)/535.0      # panel B: ticks 0.5@44.5 ... 0.1@258.5
# calibration residuals
print('C tick check',[round(yC(y),3) for y in (409.5,470.5,530.5,591.5)])
print('B tick check',[round(yB(y),4) for y in (44.5,98.5,151.5,205.5,258.5)])
targets=[('C','dapv',(125,125,125),(380,640,965,1400)),('C','wash',(203,203,203),(380,640,965,1400)),('C','red',(255,0,0),(380,640,965,1400)),
         ('B','KO red',(255,0,0),(30,275,965,1400)),('B','WT black',(0,0,0),(30,275,965,1400))]
xs={5:980,10:1000,40:1114,50:1152,100:1344}
for panel,name,col,reg in targets:
    f=yC if panel=='C' else yB
    print(panel,name)
    for xu,xp in xs.items():
        vals=[]
        for tol,er in ((15,2),(25,3),(35,3),(25,4)):
            if name=='WT black': tol=min(tol,25)
            bl=[b for b in blobs(col,tol,reg,er) if abs(b[0]-xp)<8]
            if bl:
                b=max(bl,key=lambda t:t[2]); vals.append(f(b[1]))
        if vals: print('  %3d uA reads %s mean %.4f spread %.4f'%(xu,[round(v,4) for v in vals],np.mean(vals),(max(vals)-min(vals))/2))
        else: print('  %3d uA no blob'%xu)
