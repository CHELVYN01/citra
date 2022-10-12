from email.errors import NonASCIILocalPartDefect
from turtle import color
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

nilai = np.array ([[165, 250,55,145,145],
        [178,68,60,25,67],
        [60,80,62,180,186],
        [55,145,60,66,69],
        [68,60,55,50,145]])

temp = {}
his = {}
for clm in nilai :
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





