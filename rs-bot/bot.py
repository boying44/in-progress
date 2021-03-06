import pyautogui
import cv2
import numpy as np
import giants
import time
import detectHealth

time.sleep(5)
image = pyautogui.screenshot()
# PIL to cv2 image
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

giants.find_giant(image)

location = giants.find_giant(image)
pyautogui.moveTo(location)
pyautogui.click()
