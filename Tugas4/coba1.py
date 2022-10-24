import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("image/imagedua.jpeg")

bgr = img.astype(float)/255

# mengektstra chennels
with np.errstate(invalid='ignore',divide='ignore'):
    K = 1 - np.max(bgr, axis = 2)
    C = (1-bgr[...,2] - K)/(1 - K)
    M = (1-bgr[...,1] - K)/(1 - K)
    Y = (1-bgr[...,0] - K)/(1 - K)
    
CMYK = (np.dstack((C,M,Y,K))*255).astype(np.uint8)

Y,M,C,K = cv.split(CMYK)
np.isfinite(C).all()
np.isfinite(M).all()
np.isfinite(K).all()
np.isfinite(Y).all()

n = np.isfinite(C,M,Y,K).all()
cv.imshow("tugas",n)
# cv.imwrite("image/saatu.jpg",C)
# cv.imwrite("image/duaa.jpg",M)
# cv.imwrite("image/tiiga.jpg",Y)
# cv.imwrite("image/Emmpat.jpg",K)
