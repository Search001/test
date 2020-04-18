import random

col = 30
row = 16
bomb = 99

first_move = 1
mas_cl = [['7'] * (col) for i in range(row)]

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

convert_coord = []

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


def new_desk():
    global mas
    mas = [[0] * (col) for i in range(row)]

    for i in range(bomb):
        rndx = random.randint(0, row - 1)
        rndy = random.randint(0, col - 1)
        while mas[rndx][rndy] == '*':
            rndx = random.randint(0, row - 1)
            rndy = random.randint(0, col - 1)
        mas[rndx][rndy] = '*'

    for i in range(0, col):
        for i2 in range(0, row):
            if mas[i2][i] == 0:
                try:
                    if i2 > 0 and i > 0 and mas[i2 - 1][i - 1] == '*':
                        mas[i2][i] += 1
                except:
                    pass
                try:
                    if i2 > 0 and mas[i2 - 1][i] == '*':
                        mas[i2][i] += 1
                except:
                    pass
                try:
                    if i2 > 0 and mas[i2 - 1][i + 1] == '*':
                        mas[i2][i] += 1
                except:
                    pass
                try:
                    if i > 0 and mas[i2][i - 1] == '*':
                        mas[i2][i] += 1
                except:
                    pass
                try:
                    if mas[i2][i + 1] == '*':
                        mas[i2][i] += 1
                except:
                    pass
                try:
                    if i > 0 and mas[i2 + 1][i - 1] == '*':
                        mas[i2][i] += 1
                except:
                    pass
                try:
                    if mas[i2 + 1][i] == '*':
                        mas[i2][i] += 1
                except:
                    pass
                try:
                    if mas[i2 + 1][i + 1] == '*':
                        mas[i2][i] += 1
                except:
                    pass
    for i in range(row):
        print(*mas[i])

def click(x, y):
    cell_unk = 0
    cell_mark = 0
    global first_move
    if first_move == 1:
        while mas[x][y] != 0:
            print(mas[x][y])
            new_desk()
    first_move = 0
    if mas[x][y] != '*' or mas[x][y] != 0:
        mas_cl[x][y] = mas[x][y]
    if mas[x][y] == '*':
        mas_cl[x][y] = mas[x][y]
        for i in range(row):
            print(*mas_cl[i])
        print('Game over')
        exit(0)
    if mas[x][y] == 0:
        mas_cl[x][y] = mas[x][y]
        zeros = []
        zeros2 = []
        non_zeros = []
        zeros.append([x, y])
        print()
        while zeros:
            for n, i in enumerate(zeros):
                if i not in zeros2:
                    x = i[0]
                    y = i[1]
                    try:
                        if x > 0 and y > 0 and mas[x - 1][y - 1] == 0:
                            zeros.append([x - 1, y - 1])
                    except:
                        pass
                    try:
                        if x > 0 and mas[x - 1][y] == 0:
                            zeros.append([x - 1, y])
                    except:
                        pass
                    try:
                        if x > 0 and mas[x - 1][y + 1] == 0:
                            zeros.append([x - 1, y + 1])
                    except:
                        pass
                    try:
                        if y > 0 and mas[x][y - 1] == 0:
                            zeros.append([x, y - 1])
                    except:
                        pass
                    try:
                        if mas[x][y + 1] == 0:
                            zeros.append([x, y + 1])
                    except:
                        pass
                    try:
                        if y > 0 and mas[x + 1][y - 1] == 0:
                            zeros.append([x + 1, y - 1])
                    except:
                        pass
                    try:
                        if mas[x + 1][y] == 0:
                            zeros.append([x + 1, y])
                    except:
                        pass
                    try:
                        if mas[x + 1][y + 1] == 0:
                            zeros.append([x + 1, y + 1])
                    except:
                        pass

                    try:
                        if x > 0 and y > 0 and mas[x - 1][y - 1] != 0:
                            non_zeros.append([x - 1, y - 1])
                    except:
                        pass
                    try:
                        if x > 0 and mas[x - 1][y] != 0:
                            non_zeros.append([x - 1, y])
                    except:
                        pass
                    try:
                        if x > 0 and mas[x - 1][y + 1] != 0:
                            non_zeros.append([x - 1, y + 1])
                    except:
                        pass
                    try:
                        if y > 0 and mas[x][y - 1] != 0:
                            non_zeros.append([x, y - 1])
                    except:
                        pass
                    try:
                        if mas[x][y + 1] != 0:
                            non_zeros.append([x, y + 1])
                    except:
                        pass
                    try:
                        if y > 0 and mas[x + 1][y - 1] != 0:
                            non_zeros.append([x + 1, y - 1])
                    except:
                        pass
                    try:
                        if mas[x + 1][y] != 0:
                            non_zeros.append([x + 1, y])
                    except:
                        pass
                    try:
                        if mas[x + 1][y + 1] != 0:
                            non_zeros.append([x + 1, y + 1])
                    except:
                        pass
                    zeros2.append(i)
                zeros.pop(n)
        for i in zeros2:
            x = i[0]
            y = i[1]
            mas_cl[x][y] = mas[x][y]
        for i in non_zeros:
            x = i[0]
            y = i[1]
            mas_cl[x][y] = mas[x][y]
        zeros2 = []
    show_desk()
    for i in range(row):
        for i2 in range(col):
            if mas_cl[i][i2] == '#':
                cell_unk += 1
            if mas_cl[i][i2] == 'B':
                cell_mark += 1
    if cell_unk + cell_mark == bomb:
        print('You win!!!')
        exit(0)




# x = 5
# y = 5
# click(x, y)


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
        # print(unk_cell)
        for n, cell in enumerate(unk_cell):
            mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
            pyautogui.moveTo(unk_cell[n][1]*16+icon_pos[0][0]+13, unk_cell[n][0]*16+icon_pos[0][1]+101)
            pyautogui.rightClick()
    if mas_cl[i][i2] == 2 and len(unk_cell) == 3 and len(marks) == 0 and mas_cl[i - 1][i2] == 1 and mas_cl[i + 1][
        i2] == 1 and unk_cell[0][1] == unk_cell[1][1] == unk_cell[2][1]:
        for n in range(0, 3, 2):
            mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
            pyautogui.moveTo(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
            pyautogui.rightClick()
    if mas_cl[i][i2] == 2 and len(unk_cell) == 3 and len(marks) == 0 and mas_cl[i][i2 - 1] == 1 and mas_cl[i][
        i2 + 1] == 1 and unk_cell[0][0] == unk_cell[1][0] == unk_cell[2][0]:
        for n in range(0, 3, 2):
            mas_cl[unk_cell[n][0]][unk_cell[n][1]] = 'B'
            pyautogui.moveTo(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
            pyautogui.rightClick()
    # print(unk_cell)
    # print('!!!!')
    # exit(0)


def open(i, i2, num):
    unk_cell = find(i, i2, '#')
    marks = find(i, i2, 'B')
    if mas_cl[i][i2] == num and len(unk_cell) > 0 and len(marks) == num:
        for n, cell in enumerate(unk_cell):
            pyautogui.moveTo(unk_cell[n][1] * 16 + icon_pos[0][0] + 13, unk_cell[n][0] * 16 + icon_pos[0][1] + 101)
            pyautogui.click()


# for z in range(1000):
#     for i in range(row):
#         for i2 in range(col):
#             if mas_cl[i][i2] != 0 and mas_cl[i][i2] != '#' and mas_cl[i][i2] != 'B':
#                 mark(i, i2, 1)
#                 open(i, i2, 1)
#                 mark(i, i2, 2)
#                 open(i, i2, 2)
#                 mark(i, i2, 3)
#                 open(i, i2, 3)
#                 mark(i, i2, 4)
#                 open(i, i2, 4)

show_desk()

cur_time = time.time()


def update():
    c = [mu, mf, m1, m2, m3, m4, m5]
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
print(time.time() - cur_time)

while len(detect_coord(mu)) > 478:
    pyautogui.press("f2")
    ce = detect_coord(mu)

    pyautogui.moveTo(ce[100][0]+icon_pos[0][0]+13, ce[100][1]+icon_pos[0][1]+101)
    pyautogui.click()


update()
show_desk()

for z in range(40):
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
    update()
    show_desk()
    print(z)
show_desk()