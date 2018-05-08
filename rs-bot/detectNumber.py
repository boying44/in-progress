from PIL import Image
import cv2
import sys

if (len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print("Missing filename")
    exit(0)

img = Image.open(filename)
text = pytesseract.image_to_string(img, config='--psm 10 --eom 3 -c tessedit_char_whitelist=0123456789')
print(text)