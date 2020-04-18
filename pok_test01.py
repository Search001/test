import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
import win32api, win32con, win32gui, win32com.client
import time
import ctypes
import autopy

n0 = cv2.imread("pok/rsp_0.png", 0)
n1 = cv2.imread("pok/rsp_1.png", 0)
n2 = cv2.imread("pok/rsp_2.png", 0)
n3 = cv2.imread("pok/rsp_3.png", 0)
n4 = cv2.imread("pok/rsp_4.png", 0)
n5 = cv2.imread("pok/rsp_5.png", 0)
n6 = cv2.imread("pok/rsp_6.png", 0)
n7 = cv2.imread("pok/rsp_7.png", 0)
n8 = cv2.imread("pok/rsp_8.png", 0)
n9 = cv2.imread("pok/rsp_9.png", 0)

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
time.sleep(0.15)
# pyautogui.keyDown("alt")
# pyautogui.press("tab")
# pyautogui.keyUp("alt")


def detect_coord(img):
    base_screen = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img_gray = cv2.cvtColor(np.array(base_screen), cv2.COLOR_BGR2GRAY)
    z = []
    res = cv2.matchTemplate(img_gray, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.97)
    loc_array = np.array(loc)
    #print (np.array(loc))
    for i in range(len(loc_array[0])):
        z.append([(loc_array[1, i]), (loc_array[0, i])])
    # for pt in zip(*loc[::-1]):
    #     x = int(pt[0])
    #     y = int(pt[1])
    return z

coords = detect_coord(n0)
print(coords)
for i in coords:
    print(i[0])
    pyautogui.moveTo(i[0],i[1])
    time.sleep(0.15)
# pyautogui.moveTo(0,0)
