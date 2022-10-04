# from email.mime import image
# from re import I
# from PIL import Image

# def  pengurangan_dua_citra(citra_A,  citra_B, citra_hasil):
#     # citra a 
#     CITRA_A =  Image.open(citra_A)
#     # CITRA_A = CITRA_A.convert('L')
#     PIXEL_A = CITRA_A.load()
    
#     # citra b
#     CITRA_B =  Image.open(citra_B)
#     # CITRA_A = CITRA_A.convert('L')
#     PIXEL_B = CITRA_B.load()
    
#     # membuat dua ukuran citra
#     ukuran_horizontal  =  CITRA_A.size[0]
#     ukuran_vertikal = CITRA_B.size[]
#     print (ukuran_horizontal)
#     print (ukuran_vertikal)
#     # ccitra hasil
#     CITRA_HASIL  = Image.new("RGB",(ukuran_horizontal,ukuran_vertikal))
#     PIXEL_HASIL = CITRA_HASIL.load()
    
#     for x in range (ukuran_horizontal):
#         for y in range(ukuran_vertikal):
#             R =  PIXEL_A[x,y][0] - PIXEL_B[x,y][0]
#             G =  PIXEL_A[x,y][1] - PIXEL_B[x,y][1]
#             B =  PIXEL_A[x,y][2] - PIXEL_B[x,y][2]
#             PIXEL_HASIL[x,y] = (R,G,B)
            
#             if R > 0 or G > 0 or B > 0:
#                 PIXEL_HASIL[x,y] = PIXEL_B[x,y]
            
#     CITRA_HASIL.save(citra_hasil)

# pengurangan_dua_citra("image/imagedua.jpeg", "image/imagesatu.jpeg","gab.jpg")
            
