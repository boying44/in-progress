import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

if (len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print("Missing filename")
    exit(0)

img = cv2.imread(filename,0)
edges = cv2.Canny(img,100,125) # img, low threshold, high threshold
# height, width

# get a circle around the most concentrated?
print(edges)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()