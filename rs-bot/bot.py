import numpy as np
import pyautogui
import cv2

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

pyautogui.moveTo(screenWidth/2, screenHeight/2)
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# cv2.imwrite("in_memory_to_disk.png", image)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()