import fitz, numpy as np
def load():
    pix=fitz.Pixmap('/home/desktop/legend-development/files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png')
    if pix.colorspace is None or pix.colorspace.n!=3 or pix.alpha:
        pix=fitz.Pixmap(fitz.csRGB,pix)
    a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)[:,:,:3]
    return a
