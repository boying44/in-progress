import cv2
import sys
import os

# color to gray image
# sys.argv[0] is script's name
if (len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print("Missing filename")
    exit(0)

image = cv2.imread(filename)
noExtension = os.path.splitext(filename)[0]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(noExtension + 'Gray.png', gray)