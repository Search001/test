import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
last_time = time.time()

base_screen = ImageGrab.grab(bbox = (0, 0, 1920, 1080))
#base_screen.save("pic/temp.png")

template = cv2.imread("pic/py_icon01.jpg", 0)
w, h = template.shape[::-1]

#img_rgb = cv2.imread("pic/temp.png")
img_gray = cv2.cvtColor(np.array(base_screen), cv2.COLOR_BGR2GRAY)
#cv2.imshow("Название окна", img_gray)
#cv2.waitKey(0)

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= 0.8)
print (np.array(loc))
print(time.time() - last_time)
for pt in zip(*loc[::-1]):
    x = int(pt[0])
    print(x)
    y = int(pt[1])
    print(y)

print(x,y)
pyautogui.moveTo(x, y)