import numpy as np
import nrrd
from PIL import Image
from mayavi import mlab
import json
import pandas as pd
from io import StringIO
def reconstruction( mouse , readdata, col ):
    # if mouse[col][-2] >= mouse[col+1][-2]:
    #     id = int(mouse[col][0])
    #     fixdata = abs(fixdata -id)<0.005
    #     return fixdata
    # else:
    #     temp = col + 1
    #     fixdata = fixdata * 0
    #     while mouse[col][-2] < mouse[temp][-2]:
    #         fixdata = fixdata + reconstruction( mouse , fixdata , temp)
    #         temp = temp + 1
    #     return fixdata
    fixdata = readdata < 0
    print(mouse[col][-1][-1])
    for id in mouse[col][-1][-1]:
        fix = readdata == id
        fixdata = fixdata | fix
        print(id)
        print(np.sum(fixdata))
    return fixdata
        

filename = './annotation_25.nrrd'
readdata, header = nrrd.read(filename)
print(readdata.dtype)
with open('mouse4.json') as f:
    mousebrain = json.load(f)
col = 1
while col < 2:
#    if mousebrain[col][-2] >= mousebrain[col+1][-2]:
    data = reconstruction (mousebrain, readdata,col) 
    # mlab.contour3d(data.astype(np.int))
    mlab.contour3d(data.astype(np.int), line_width=8)
    mlab.savefig(mousebrain[col][0]+'.obj')
    col =col + 1
    mlab.clf()

