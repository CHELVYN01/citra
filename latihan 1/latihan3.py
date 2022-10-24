from importlib import import_module
from turtle import color


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image/halo.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
cv2.imshow("daun",img)
cv2.destroAllWindows()