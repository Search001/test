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
m5 = cv2.imread("pic/mine_5.png", 0)
me = cv2.imread("pic/mine_empty.png", 0)
mu = cv2.imread("pic/mine_unkn.png", 0)
mf = cv2.imread("pic/mine_flag.png", 0)
done = []

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
    for i in range(len(loc_array[0])):
        z.append([(loc_array[1, i]), (loc_array[0, i])])
    return z

def lr_click():
    pyautogui.mouseDown(button='right')
    pyautogui.click()
    pyautogui.mouseUp(button='right')

def detect_mines(number_img):
    if number_img is m1:
        num = 1
    elif number_img is m2:
        num = 2
    elif number_img is m3:
        num = 3
    elif number_img is m4:
        num = 4
    elif number_img is m5:
        num = 5
    mine = detect_coord(number_img)
    for i1 in range(len(mine)):   #ищет цифры number, оценивает поле 3х3 вокруг них на наличие неоткрытых областей
        if mine[i1] not in done:
            pyautogui.moveTo(mine[i1])
            around_cursor = ImageGrab.grab(bbox=(mine[i1][0]-17, mine[i1][1]-17, mine[i1][0]+31, mine[i1][1]+31))
            global img_ar_cur
            img_ar_cur = cv2.cvtColor(np.array(around_cursor), cv2.COLOR_BGR2GRAY)
            #print(detect_coord_small(mu))
            #cv2.imshow("Screenshot", img_ar_cur)
            #cv2.waitKey(0)
            if len(detect_coord_small(mu)) == 0:
                done.append(mine[i1])
            if len(detect_coord_small(mf)) == num - 1 and len(detect_coord_small(mu)) == 1: #если вокруг цифры столько же неоткрытых клеток, помечает их
                cursor = [win32gui.GetCursorPos()]
                dcs = detect_coord_small(mu)
                pyautogui.moveTo(cursor[0][0]+dcs[0][0]-17, cursor[0][1] + dcs[0][1]-17)
                pyautogui.rightClick()


def open_unk(number_img):
    if number_img is m1:
        num = 1
    elif number_img is m2:
        num = 2
    elif number_img is m3:
        num = 3
    elif number_img is m4:
        num = 4
    elif number_img is m5:
        num = 5
    mine = detect_coord(number_img)
    for i1 in range(len(mine)):   #ищет цифры number, оценивает поле 3х3 вокруг них на наличие размеченных мин
        if mine[i1] not in done:
            pyautogui.moveTo(mine[i1])
            around_cursor = ImageGrab.grab(bbox=(mine[i1][0]-17, mine[i1][1]-17, mine[i1][0]+31, mine[i1][1]+31))
            global img_ar_cur
            img_ar_cur = cv2.cvtColor(np.array(around_cursor), cv2.COLOR_BGR2GRAY)
            #cv2.imshow("Screenshot", img_ar_cur)
            #cv2.waitKey(0)
            if len(detect_coord_small(mf)) == num and len(detect_coord_small(mu)) > 0: #если найдено, то клик на открытие
                lr_click()
            if len(detect_coord_small(mf)) + len(detect_coord_small(mu)) == num and len(detect_coord_small(mu)) > 1:
                cursor = [win32gui.GetCursorPos()]
                dcs = detect_coord_small(mu)
                for u in range(len(dcs)):
                    pyautogui.moveTo(cursor[0][0] + dcs[u][0] - 17, cursor[0][1] + dcs[u][1] - 17)
                    pyautogui.rightClick()
                    pyautogui.moveTo(cursor[0][0], cursor[0][1])

app_coord = detect_coord(icon)

print(len(detect_coord(mu)))

while len(detect_coord(mu)) > 478:
    pyautogui.press("f2")
    c = detect_coord(mu)
    pyautogui.moveTo(c[100])
    pyautogui.click()

while len(detect_coord(mu)) > 0:
    print("На удаление:", done)
    detect_mines(m1)
    open_unk(m1)
    detect_mines(m2)
    open_unk(m2)
    try:
        detect_mines(m3)
        open_unk(m3)
    except:
        print("нет 3")
    try:
        detect_mines(m4)
        open_unk(m4)
    except:
        print("нет 4")
    try:
        detect_mines(m5)
        open_unk(m5)
    except:
        print("нет 5")

