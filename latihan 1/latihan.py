# from email.mime import image
import numpy
import cv2 as cd;
image  = cd.imread("halo.jpg")
x = len(image[0])
y = len(image)
cd.imshow("daun", image)
print(x)
print(y)
cd.waitKey(0)
cd.destroyAllWindows()