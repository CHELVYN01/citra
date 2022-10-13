from email.errors import NonASCIILocalPartDefect
from turtle import color
import cv2 as cv
import math
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("image/imagedua.jpeg",0)
plt.hist(img.ravel(), 256,[0,256])
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

nilaiAmbang = avg(T)
for i in range(len(imgMatrx)):
    for j in range(len(imgMatrx[i])):
        if(imgMatrx[i,j] < nilaiAmbang):
            imgMatrx[i,j] = 0
        else:
            imgMatrx[i,j] = 255
cv.imshow("daun",imgMatrx)
cv.waitKey(0)
cv.destroyAllWindows()