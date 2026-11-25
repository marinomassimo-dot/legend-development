import numpy as np
def load(p):
    b=open(p,'rb').read()
    parts=b.split(None,4)
    w,h=int(parts[1]),int(parts[2])
    data=parts[4]
    return np.frombuffer(data[-w*h*3:],dtype=np.uint8).reshape(h,w,3).astype(int)
