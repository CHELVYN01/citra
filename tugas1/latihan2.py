import cv2 as gambar

img = gambar.imread('halo.jpg')

print(img.shape)
print(img[0][0][0])
print(img[0][0][1])
print(img[0][0][2])
print(gambar.mean(img))