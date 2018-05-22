import numpy as np
import cv2

# 
def getColorMask(img, colorRange):
    lower = np.array(colorRange[0], dtype = "uint8")
    upper = np.array(colorRange[1], dtype = "uint8")
    return cv2.inRange(img, lower, upper)