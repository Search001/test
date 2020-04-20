import random

col = 30
row = 16
bomb = 99

first_move = 1
mas_cl = [['7'] * (col) for i in range(row)]
mas_cl_compare_to_zero = []
mas_cl_compare_to_self = []

import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
import win32api, win32con, win32gui, win32com.client
import time
import os
import copy

#доска 16х30
time.sleep(5)
pyautogui.moveTo(417,1060)
pyautogui.click()
os.startfile(r'C:\Program Files (x86)\MineSweeper\winmine.exe')
time.sleep(0.35)

icon = cv2.imread("pic/mine_icon.png", 0)
m1 = cv2.imread("pic/mine_1.png", 0)
m2 = cv2.imread("pic/mine_2.png", 0)
m3 = cv2.imread("pic/mine_3.png", 0)
m4 = cv2.imread("pic/mine_4.png", 0)
m5 = cv2.imread("pic/mine_5.png", 0)
m6 = cv2.imread("pic/mine_6.png", 0)
m7 = cv2.imread("pic/mine_7.png", 0)
me = cv2.imread("pic/mine_empty.png", 0)
mu = cv2.imread("pic/mine_unkn.png", 0)
mf = cv2.imread("pic/mine_flag.png", 0)

convert_coord = []

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def rclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)


def detect_icon():
    base_screen = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img_gray = cv2.cvtColor(np.array(base_screen), cv2.COLOR_BGR2GRAY)
    z = []
    res = cv2.matchTemplate(img_gray, icon, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.97)
    loc_array = np.array(loc)
    #print (np.array(loc))
    for i in range(len(loc_array[0])):
        z.append([(loc_array[1, i]), (loc_array[0, i])])
    # for pt in zip(*loc[::-1]):
    #     x = int(pt[0])
    #     y = int(pt[1])
    return z

icon_pos = detect_icon()

def detect_coord(img):
    base_screen = ImageGrab.grab(bbox=((icon_pos[0][0]+13), (icon_pos[0][1]+101), (icon_pos[0][0]+13)+480, (icon_pos[0][1]+101)+256))
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

def show_desk():
    bar = [_ for _ in range(col)]
    print(*bar)
    print('-' * (col * 2 - 1))
    for i in range(row):
        print(*mas_cl[i], '|', i)

def to_zero():
    for i in range(0, col):
        for i2 in range(0, row):
            if mas_cl[i2][i] == "B":
                mas_cl[i2][i] = 0
                try:
                    if i2 > 0 and i > 0 and mas_cl[i2 - 1][i - 1] > 0:
                        mas_cl[i2 - 1][i - 1] -= 1
                except:
                    pass
                try:
                    if i2 > 0 and mas_cl[i2 - 1][i] > 0:
                        mas_cl[i2 - 1][i] -= 1
                except:
                    pass
                try:
                    if i2 > 0 and mas_cl[i2 - 1][i + 1] > 0:
                        mas_cl[i2 - 1][i + 1] -= 1
                except:
                    pass
                try:
                    if i > 0 and mas_cl[i2][i - 1] > 0:
                        mas_cl[i2][i - 1] -= 1
                except:
                    pass
                try:
                    if mas_cl[i2][i + 1] > 0:
                        mas_cl[i2][i + 1] -= 1
                except:
                    pass
                try:
                    if i > 0 and mas_cl[i2 + 1][i - 1] > 0:
                        mas_cl[i2 + 1][i - 1] -= 1
                except:
                    pass
                try:
                    if mas_cl[i2 + 1][i] > 0:
                        mas_cl[i2 + 1][i] -= 1
                except:
                    pass
                try:
                    if mas_cl[i2 + 1][i + 1] > 0:
                        mas_cl[i2 + 1][i + 1] -= 1
                except:
                    pass



def find(i2, i, num):
    num_count = 0
    global coords
    coords = []
    try:
        if i2 > 0 and i > 0 and mas_cl[i2 - 1][i - 1] == num:
            num_count += 1
            coords.append([i2 - 1, i - 1])
    except:
        pass
    try:
        if i2 > 0 and mas_cl[i2 - 1][i] == num:
            num_count += 1
            coords.append([i2 - 1, i])
    except:
        pass
    try:
        if i2 > 0 and mas_cl[i2 - 1][i + 1] == num:
            num_count += 1
            coords.append([i2 - 1, i + 1])
    except:
        pass
    try:
        if i > 0 and mas_cl[i2][i - 1] == num:
            num_count += 1
            coords.append([i2, i - 1])
    except:
        pass
    try:
        if mas_cl[i2][i + 1] == num:
            num_count += 1
            coords.append([i2, i + 1])
    except:
        pass
    try:
        if i > 0 and mas_cl[i2 + 1][i - 1] == num:
            num_count += 1
            coords.append([i2 + 1, i - 1])
    except:
        pass
    try:
        if mas_cl[i2 + 1][i] == num:
            num_count += 1
            coords.append([i2 + 1, i])
    except:
        pass
    try:
        if mas_cl[i2 + 1][i + 1] == num:
            num_count += 1
            coords.append([i2 + 1, i + 1])
    except:
        pass
    return coords


def mark(i, i2, num):
    unk_cell = find(i, i2, '#')
    marks = find(i, i2, 'B')
    if mas_cl[i][i2] == num and len(unk_cell) > 0 and (len(unk_cell) + len(marks)) == num:
        # стандартная разметка
        for n, cell in enumerate(unk_cell):
            mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
            rclick(unk_cell[n][1]*16+icon_pos[0][0]+13, unk_cell[n][0]*16+icon_pos[0][1]+101)
            # pyautogui.moveTo(unk_cell[n][1]*16+icon_pos[0][0]+13, unk_cell[n][0]*16+icon_pos[0][1]+101)
            # pyautogui.rightClick()
    if mas_cl[i][i2] == 2 \
            and len(unk_cell) == 3 \
            and len(marks) == 0 \
            and mas_cl[i - 1][i2] == 1 \
            and mas_cl[i + 1][i2] == 1 \
            and unk_cell[0][1] == unk_cell[1][1] == unk_cell[2][1]:
        #121 в ряд по вертикали
        for n in range(0, 3, 2):
            mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
            rclick(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
    if mas_cl[i][i2] == 2 \
            and len(unk_cell) == 3 \
            and len(marks) == 0 \
            and mas_cl[i][i2 - 1] == 1 \
            and mas_cl[i][i2 + 1] == 1 \
            and unk_cell[0][0] == unk_cell[1][0] == unk_cell[2][0]:
        #121 в ряд по горизонтали
        for n in range(0, 3, 2):
            mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
            rclick(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
    try:
        if mas_cl[i][i2] == 2 \
                and len(unk_cell) == 3 \
                and len(marks) == 0 \
                and mas_cl[i - 1][i2] == 1 \
                and mas_cl[i + 1][i2] == 2 \
                and mas_cl[i + 2][i2] == 1 \
                and unk_cell[0][1] == unk_cell[1][1] == unk_cell[2][1]:
            #1221 в ряд по вертикали
            for n in range(1, 3, 1):
                mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
                rclick(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
    except:
        pass
    try:
        if mas_cl[i][i2] == 2 \
                and len(unk_cell) == 3 \
                and len(marks) == 0 \
                and mas_cl[i][i2 - 1] == 1 \
                and mas_cl[i][i2 + 1] == 2 \
                and mas_cl[i][i2 + 2] == 1 \
                and unk_cell[0][0] == unk_cell[1][0] == unk_cell[2][0]:
            #1221 в ряд по горизонтали
            for n in range(1, 3, 1):
                mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
                rclick(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
    except:
        pass
    if mas_cl[i][i2] == 1 \
            and i == 1 \
            and len(unk_cell) == 3 \
            and len(marks) == 0 \
            and mas_cl[i - 1][i2] == 1 \
            and mas_cl[i + 1][i2] == 1 \
            and mas_cl[i + 2][i2] == 0 \
            and mas_cl[i + 2][i2+1] != "#" \
            and mas_cl[i + 2][i2+1] != "#" \
            and unk_cell[0][1] == unk_cell[1][1] == unk_cell[2][1]:
        # 111 в ряд по вертикали с начала
        mas_cl[unk_cell[1][0]][unk_cell[1][1]] = 'B'
        rclick(unk_cell[1][1] * 16 + icon_pos[0][0] + 13, unk_cell[1][0] * 16 + icon_pos[0][1] + 101)
    if mas_cl[i][i2] == 1 \
            and i == row-2 \
            and len(unk_cell) == 3 \
            and len(marks) == 0 \
            and mas_cl[i - 1][i2] == 1 \
            and mas_cl[i + 1][i2] == 1 \
            and mas_cl[i - 2][i2] == 0 \
            and mas_cl[i - 2][i2-1] != "#" \
            and mas_cl[i - 2][i2+1] != "#" \
            and unk_cell[0][1] == unk_cell[1][1] == unk_cell[2][1]:
        # 111 в ряд по вертикали с конца
        mas_cl[unk_cell[1][0]][unk_cell[1][1]] = 'B'
        rclick(unk_cell[1][1] * 16 + icon_pos[0][0] + 13, unk_cell[1][0] * 16 + icon_pos[0][1] + 101)
    if mas_cl[i][i2] == 1 \
            and i2 == 1 \
            and len(unk_cell) == 3 \
            and len(marks) == 0 \
            and mas_cl[i][i2-1] == 1 \
            and mas_cl[i][i2+1] == 1 \
            and mas_cl[i][i2+2] == 0 \
            and mas_cl[i-1][i2+2] != "#" \
            and mas_cl[i+1][i2+2] != "#" \
            and unk_cell[0][0] == unk_cell[1][0] == unk_cell[2][0]:
        # 111 в ряд по горизонтали с начала
        mas_cl[unk_cell[1][0]][unk_cell[1][1]] = 'B'
        rclick(unk_cell[1][1] * 16 + icon_pos[0][0] + 13, unk_cell[1][0] * 16 + icon_pos[0][1] + 101)
    if mas_cl[i][i2] == 1 and i2 == col-2 \
            and len(unk_cell) == 3 \
            and len(marks) == 0 \
            and mas_cl[i][i2-1] == 1 \
            and mas_cl[i][i2+1] == 1 \
            and mas_cl[i][i2-2] == 0 \
            and mas_cl[i-1][i2-2] != "#" \
            and mas_cl[i+1][i2-2] != "#" \
            and unk_cell[0][0] == unk_cell[1][0] == unk_cell[2][0]:
        # 111 в ряд по горизонтали с конца
        mas_cl[unk_cell[1][0]][unk_cell[1][1]] = 'B'
        rclick(unk_cell[1][1] * 16 + icon_pos[0][0] + 13, unk_cell[1][0] * 16 + icon_pos[0][1] + 101)

    # print(unk_cell)
    # print('!!!!')
    # exit(0)


def open(i, i2, num):
    cur_time = time.time()
    unk_cell = find(i, i2, '#')
    marks = find(i, i2, 'B')
    if mas_cl[i][i2] == num and len(unk_cell) > 0 and len(marks) == num:
        for n, cell in enumerate(unk_cell):
            x = unk_cell[n][1] * 16 + icon_pos[0][0] + 13
            y = unk_cell[n][0] * 16 + icon_pos[0][1] + 101
            click(x, y)
            # pyautogui.moveTo(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
            # pyautogui.click()
    if time.time() - cur_time > 0:
        print(time.time() - cur_time)
show_desk()

def update():
    c = [mu, mf, m1, m2, m3, m4, m5, m6, m7]
    convert_coord = []
    for cell in c:
        if cell is mu:
            sym = "#"
        elif cell is mf:
            sym = "B"
        elif cell is m1:
            sym = 1
        elif cell is m2:
            sym = 2
        elif cell is m3:
            sym = 3
        elif cell is m4:
            sym = 4
        elif cell is m5:
            sym = 5
        elif cell is m6:
            sym = 6
        elif cell is m7:
            sym = 7
        unk_coord = (detect_coord(cell))

        for i in range(len(unk_coord)):
            #convert_coord.append([unk_coord[i][0]-(icon_pos[0][0]+13), unk_coord[i][1]-(icon_pos[0][1]+101)])
            x = int(unk_coord[i][1]/16)
            y = int(unk_coord[i][0]/16)
            convert_coord.append([x,y])
            mas_cl[x][y] = sym
    for i in range(row):
        for i2 in range(col):
            if ([i, i2]) not in convert_coord:
                mas_cl[i][i2] = 0
        #print(convert_coord)

update()
show_desk()

def new_game():
    mas_cl_compare_to_zero = []
    mas_cl_compare_to_self = []
    while len(detect_coord(mu)) > row * col - 2:
        pyautogui.press("f2")
        ce = detect_coord(mu)
        click(ce[row*col//3][0] + icon_pos[0][0] + 13, ce[row*col//3][1] + icon_pos[0][1] + 101)

    update()
    show_desk()

    while mas_cl_compare_to_self != mas_cl:
        if mas_cl_compare_to_zero == mas_cl:
            mas_cl_compare_to_self = copy.deepcopy(mas_cl)
            print("TO ZERO!")
            to_zero()
            show_desk()
        mas_cl_compare_to_zero = copy.deepcopy(mas_cl)
        for i in range(row):
            for i2 in range(col):
                if mas_cl[i][i2] != 0 and mas_cl[i][i2] != '#' and mas_cl[i][i2] != 'B':

                    mark(i, i2, 1)
                    open(i, i2, 1)
                    mark(i, i2, 2)
                    open(i, i2, 2)
                    mark(i, i2, 3)
                    open(i, i2, 3)
                    mark(i, i2, 4)
                    open(i, i2, 4)
                    mark(i, i2, 5)
                    open(i, i2, 5)
                    mark(i, i2, 6)
                    open(i, i2, 6)
                    mark(i, i2, 7)
                    open(i, i2, 7)

        update()
        #show_desk()


    show_desk()

while len(detect_coord(mu)) > 0:
    pyautogui.press("f2")
    new_game()