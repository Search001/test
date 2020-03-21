import pyautogui
import time

ctime = time.time()
icon_coord = pyautogui.locateOnScreen("pic\py_icon01.jpg", grayscale=True)
if icon_coord:
    print ("111")

print(time.time() - ctime)
pyautogui.click(icon_coord)

