import cv2
import numpy as np
import sys

if (len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print("Missing filename")
    exit(0)

img = cv2.imread(filename,0)
edges = cv2.Canny(img,100,125) # img, low threshold, high threshold
# height, width

cv2.imshow("edge", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()