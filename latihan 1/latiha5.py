import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('halo.jpg', 0)
   
color = ('b', 'g', 'r')
  
  
# for i in range(0, height ):
#     for j in range(0, width):
          
#         # Get the pixel value
#         pixel = img_bgr[i, j]
          
#         # Negate each channel by 
#         # subtracting it from 255
          
#         # 1st index contains red pixel
#         pixel[0] = 255 - pixel[0]
          
#         # 2nd index contains green pixel
#         pixel[1] = 255 - pixel[1]
          
#         # 3rd index contains blue pixel
#         pixel[2] = 255 - pixel[2]
          
#         # Store new values in the pixel
#         img_bgr[i, j] = pixel
  
# # Display the negative transformed image
# plt.imshow(img_bgr)
# plt.show()
  
# # Histogram plotting of the
# # negative transformed image
# color = ('b', 'g', 'r')
  
# for i, col in enumerate(color):
      
#     histr = cv2.calcHist([img_bgr], 
#                          [i], None,
#                          [256],
#                          [0, 256])
      
#     plt.plot(histr, color = col)
#     plt.xlim([0, 256])
      
# plt.show()