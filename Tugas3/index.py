from email.errors import NonASCIILocalPartDefect
from turtle import color
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread("image/imagedua.jpeg",0)
plt.hist(img.ravel(), 256,[0,256])
plt.show()