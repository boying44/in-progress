import cv2
import numpy as np
import collections
# caa070
# 513d25

# lower = [0x36, 0x50, 0x80]
# upper = [0x5f, 0xa0, 0xc0]

red = ([17, 15, 100], [50, 56, 200])
hsv = ([0, 100, 100], [179, 255, 255])
# hsv = ([31, 40, 70], [36, 50, 83])
# lower = [100, 140, 220]
# upper = [120, 225, 255]

lower = np.array(hsv[0], dtype = "uint8")
upper = np.array(hsv[1], dtype = "uint8")
image = cv2.imread("giants.png")
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# mask = cv2.inRange(image, lower, upper)
mask = cv2.inRange(hsv_img, lower, upper)

# output = cv2.bitwise_and(image, image, mask = mask)
output = cv2.bitwise_and(hsv_img, hsv_img, mask = mask)
cv2.imshow("images", output)
cv2.waitKey(0)
