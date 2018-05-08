import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

pyautogui.moveTo(screenWidth/2, screenHeight/2)
