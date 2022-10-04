from email.mime import image
from hashlib import new
import imghdr
import cv2 as cv
import numpy as np

images = cv.imread('image/halo.jpg',0)
image = cv.resize(images,None,fx=0.5,fy=0.5 , interpolation= cv.INTER_CUBIC)
def neighboorMin(image):
  new=np.zeros(image.shape) # membuat object new, fungsi method zeros yaitu untuk membuat semua isi matrix menjadi 0
  for baris in range(1,x-1):
    for kolom in range(1,y-1):
      temp=[image[baris-1][kolom-1],image[baris-1][kolom],image[baris-1][kolom+1],image[baris][kolom-1],image[baris][kolom+1],image[baris+1][kolom-1],image[baris+1][kolom],image[baris+1][kolom+1]]
      new[baris][kolom]=np.amin(temp)
  return new


print(image)
print(new)
# cv.imwrite("haha.jpg",image)
cv.imwrite("hihih.jpg",new)
cv.waitKey(0)
cv.destroyAllWindows()