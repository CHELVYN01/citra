def rgb_to_cmy(r, g, b):
  
    # RGB values are divided by 255 
    # to bring them between 0 to 1.
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    return (c, m, y)
  
# Sample RGB values.
r = 40
g = 169
b = 86
 
print(rgb_to_cmy(r,g,b))