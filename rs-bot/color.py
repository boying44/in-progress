import cv2
import numpy as np
import collections
# caa070
# 513d25

red = ([17, 15, 100], [50, 56, 200])
hsv = ([10, 50, 100], [20, 200, 200])

lower = np.array(hsv[0], dtype = "uint8")
upper = np.array(hsv[1], dtype = "uint8")
image = cv2.imread("giants.png")
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_img, lower, upper)

output = cv2.bitwise_and(hsv_img, hsv_img, mask = mask)
cv2.imshow("images", output)

def nothing(x):
    pass

cv2.createTrackbar('R','images',0,255,nothing)
cv2.createTrackbar('G','images',0,255,nothing)
cv2.createTrackbar('B','images',0,255,nothing)
cv2.waitKey(0)
