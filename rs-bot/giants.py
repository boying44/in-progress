import cv2
import numpy as np
from mask import getColorMask

skin_color = ([6, 125, 128], [26, 145, 208]) #HSV
red = ([0, 255, 255], [10, 255, 255]) #HSV
gray = ([-10, 13, 21], [10, 36, 167])
white = ([4,  58, 117], [24, 73, 197])

# This can be turned into a class and the contours of an image saved
# returns center of potential giant
def find_giant(image):
    """
    Returns center of potential giant
    """
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    ##### filter giants color
    body = getColorMask(hsv_img, skin_color) # ones and zeros 
    # gray_clothes = getColorMask(hsv_img, gray)
    white_clothes = getColorMask(hsv_img, white)
    # clothes = cv2.bitwise_or(white_clothes, gray_clothes)
    # mask = cv2.bitwise_or(body, white_clothes)
    mask = body
    masked = cv2.bitwise_and(image, image, mask=mask)

    # show side by side
    combined = np.hstack([image, masked])
    height, width, channels = combined.shape
    fitScreen = cv2.resize(combined, (int(width/2), int(height/2)))

    cv2.imshow("image", fitScreen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ##### test making it into one contour
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.dilate(mask, kernel, iterations = 2)
    dilation = cv2.dilate(erosion, kernel, iterations = 3)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    ret, thresh = cv2.threshold(closing,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(closing, contours, -1, (0,255,0), 3)
    cv2.imshow("closing", closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #####

    ret, thresh = cv2.threshold(mask,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # contours are a list of x,t values of boundary

    # filters out small contours
    for c in contours:
        # c = contours[index]
        (x,y,w,h) = cv2.boundingRect(c)
        if w*h > 200:
            return x+(w/2), y+(h/2)
    return None

# filter out taken giants
# bitwise and of health and giant mask?
def detect_health(image):
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = getColorMask(hsv_img, red)
