from email.mime import image
import numpy
import cv2 as cd
image  = cd.imread("halo.jpg")
gray = cd.cvtColor(image, cd.COLOR_BGR2GRAY)
cd.imshow("daun", gray)
cd.waitKey(0)
cd.destroyAllWindows()