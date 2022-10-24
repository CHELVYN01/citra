from email.errors import NonASCIILocalPartDefect
from turtle import color
import cv2 as cv
import math
import matplotlib.pyplot as plt
import numpy as np

gambaar = cv.imread("image/imagedua.jpeg",0)
img = cv.resize(gambaar,None,fx=0.5,fy=0.5 , interpolation= cv.INTER_CUBIC)
plt.hist(gambaar.ravel(), 256,[0,256])
plt.show()

imgMatrx = img

T =  128
def  avg(T):
    kiri = []
    kanan = []
    
    for i in range(len(imgMatrx)):
        for j in (imgMatrx[i]):
            if (j<T):
                kiri.append(j)
            else:
                kanan.append(j)
                
    avgKiri =  sum(kiri)/len(kiri)
    avgKanan = sum(kanan)/len(kanan)
    Tambang = math.ceil((avgKiri+avgKanan)/2)
    
    if(T - Tambang != 0):
        avg(Tambang)
    else:
        Tambang = Tambang
    return Tambang

print(avg(T))

nilaiAmbang = 86
for i in range(len(imgMatrx)):
    for j in range(len(imgMatrx[i])):
        if(imgMatrx[i,j] < nilaiAmbang):
            imgMatrx[i,j] = 0
        else:
            imgMatrx[i,j] = 255
cv.imshow("hp",imgMatrx)
cv.waitKey(0)
cv.destroyAllWindows()