from PIL import Image
import matplotlib.pyplot as plt
import cv2 as cv
img=cv.imread("/img/halo.jpg")
 
w,h=img.size
for i in range(w):
    for j in range(h):
        r,g,b=img.getpixel((i,j))
        r=255-r
        g=255-g
        b=255-b
        img.putpixel((i,j),(r,g,b))
plt.axis('off')
cv.imshow(img)
cv.destroyAllWindows

