from array import array
import cv2 as cv
import numpy as np
# mengubah gambar menjadi hitam putih 
images = cv.imread('image/imagedua.jpeg',0)

# mengubah ukuran gambar pada image
image = cv.resize(images,None,fx=0.5,fy=0.5 , interpolation= cv.INTER_CUBIC)
c = image - 255
# membaca gambar 
cv.imwrite("satuS.jpg",image)

cv.imshow("gamabr",c)
cv.waitKey(0)
cv.destroyAllWindows()