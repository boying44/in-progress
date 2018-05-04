from PIL import Image
import pytesseract
import argparse
import cv2
import os

# image = cv2.imread('health.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "grayHealth.png"
# cv2.imwrite(filename, gray)
img = Image.open(filename)
text = pytesseract.image_to_string(img)
print(text)