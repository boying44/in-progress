import cv2
from mask import getColorMask


img = cv2.imread("health.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

a = getColorMask(hsv, ([6,61,64],[26,81,144])) # inside
b = getColorMask(hsv, ([0,242,67],[11,255,255])) # red
c = getColorMask(hsv, ([9,154,64],[29,174,144])) # outside
d = getColorMask(hsv, ([6,42,53],[26,62,133])) # border

green = getColorMask(hsv, ([40,190,180],[64,255,255]))

ab = cv2.bitwise_or(a, b)
abc = cv2.bitwise_or(ab, c)
abcd = cv2.bitwise_or(abc, d)
invert = 255 - abcd

mask = cv2.bitwise_and(img, img, mask = green)

cv2.imshow("mask", green)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test.png', gray)