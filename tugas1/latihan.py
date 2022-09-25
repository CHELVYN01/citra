# from email.mime import image
import numpy
import cv2 as cd;
image  = cd.imread("halo.jpg")
ras = cd.resize(image,None,fx=0.5,fy=0.5 , interpolation= cd.INTER_CUBIC)
cd.imshow("daun", ras)
cd.waitKey(0)
cd.destroyAllWindows()