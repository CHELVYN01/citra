import imghdr
import cv2 as gbr
import numpy as np



def neighboorMin(image):
  new=np.zeros(image.shape) # membuat object new, fungsi method zeros yaitu untuk membuat semua isi matrix menjadi 0
  for baris in range(1,x-1):
    for kolom in range(1,y-1):
      temp=[image[baris-1][kolom-1],image[baris-1][kolom],image[baris-1][kolom+1],image[baris][kolom-1],image[baris][kolom+1],image[baris+1][kolom-1],image[baris+1][kolom],image[baris+1][kolom+1]]
      new[baris][kolom]=np.amin(temp)
  return new

image = gbr.imread("image/halo.jpg")
gbr("daun", image)


        

    
