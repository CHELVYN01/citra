from tokenize import Double
import cv2 as cv
import numpy as  np
def rgb(R,G,B):
    if max(max(R))> 1.0 or max(max(G))>1.0 or max(max(B))>1.0:
        R = Double(R) /255
        G = Double(G) /255
        B = Double(B) /255
    u = 0.5
    b = 1
    
    R = np.array(["tinggi","lebar"])
    np.size(R)
    
   
    
    