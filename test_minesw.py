import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
import win32api, win32con, win32gui, win32com.client
import time
import os

#доска 16х30

os.startfile(r'C:\Program Files (x86)\MineSweeper\winmine.exe')
time.sleep(0.35)



icon = cv2.imread("pic/mine_icon.png", 0)
m1 = cv2.imread("pic/mine_1.png", 0)
m2 = cv2.imread("pic/mine_2.png", 0)
m3 = cv2.imread("pic/mine_3.png", 0)
m4 = cv2.imread("pic/mine_4.png", 0)
me = cv2.imread("pic/mine_empty.png", 0)
mu = cv2.imread("pic/mine_unkn.png", 0)
mf = cv2.imread("pic/mine_flag.png", 0)

# cv2.imshow("Screenshot", img_gray)
# cv2.waitKey(0)
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

def detect_coord_small(img):
    z = []
    res = cv2.matchTemplate(img_ar_cur, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.97)
    loc_array = np.array(loc)
    #print (np.array(loc))
    for i in range(len(loc_array[0])):
        z.append([(loc_array[1, i]), (loc_array[0, i])])
    # for pt in zip(*loc[::-1]):
    #     x = int(pt[0])
    #     y = int(pt[1])
    return z

def detect_mines(number_img):
    if number_img is m1:
        num = 1
    elif number_img is m2:
        num = 2
    mine = detect_coord(number_img)
    for i1 in range(len(mine)):   #ищет цифры number, оценивает поле 3х3 вокруг них на наличие неоткрытых областей
        pyautogui.moveTo(mine[i1])
        #time.sleep(0.35)
        around_cursor = ImageGrab.grab(bbox=(mine[i1][0]-17, mine[i1][1]-17, mine[i1][0]+31, mine[i1][1]+31))
        global img_ar_cur
        img_ar_cur = cv2.cvtColor(np.array(around_cursor), cv2.COLOR_BGR2GRAY)
        print(detect_coord_small(mu))
        cv2.imshow("Screenshot", img_ar_cur)
        #cv2.waitKey(0)
        if len(detect_coord_small(mu))-len(detect_coord_small(mf)) == num: #если вокруг цифры столько же неоткрытых клеток, помечает их
            cursor = [win32gui.GetCursorPos()]
            print("курсор", cursor)
            print(mine[i1])
            dcs = detect_coord_small(mu)
            for i2 in range(len(dcs)):
                print(app_coord[0])
                pyautogui.moveTo(cursor[0][0]+dcs[0][0]-17, cursor[0][1] + dcs[0][1]-17)
                #pyautogui.moveTo(mine[i1][0]+app_coord[0][0]+13, mine[i1][1]+app_coord[0][1]+101)
                #print("xx:", dcs[i2][0]+app_coord[0][0]+45, dcs[i2][1]+app_coord[0][1]+101)
                pyautogui.rightClick()
                # dcs = detect_coord_small(mu)
                # for i3 in range (len(dcs)):
                #
                # pyautogui.moveTo(cursor[0][0] + dcs[0][0] - 17, cursor[0][1] + dcs[0][1] - 17)
app_coord = detect_coord(icon)
#print(app_coord)

#base_screen = ImageGrab.grab(bbox = (app_coord[0][0]+13, app_coord[0][1]+101, app_coord[0][0]+494, app_coord[0][1]+358))
#img_gray = cv2.cvtColor(np.array(base_screen), cv2.COLOR_BGR2GRAY)
# cv2.imshow("Screenshot", img_gray)
# cv2.waitKey(0)
#print(z)



print(len(detect_coord(mu)))

while len(detect_coord(mu)) > 478:
    pyautogui.press("f2")
    c = detect_coord(mu)
    pyautogui.moveTo(c[100])
    pyautogui.click()

detect_mines(m1)
#print(detect_coord(n2))