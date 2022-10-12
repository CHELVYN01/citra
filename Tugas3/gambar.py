from email.errors import NonASCIILocalPartDefect
from turtle import color
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("image/imagedua.jpeg",0)
temp = {}
his = {}
for clm in img :
    for data in clm :
        if data not in temp :
            temp[data] = 1
        else :
            temp [data] += 1

for i in sorted(temp):
    his[i] = temp[i]
    print(i ,":",his[i])
    
plt.bar(list(his.keys()), his.values(), color = 'g')
plt.show()