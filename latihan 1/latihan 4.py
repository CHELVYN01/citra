from scipy import misc
import matplotlib.pyplot as plt
import cv2 as cv

img = plt.imread('halo.jpg')
plt.gray()
print(img)
cv.imshow('daun',img)
cv.waitKey(1)
cv.destroyAllWindows()

