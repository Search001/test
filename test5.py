import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
import time


base_screen = ImageGrab.grab(bbox = (60, 300, 200, 400))
#base_screen.save("pic/temp.png")

n0 = cv2.imread("pic/n0.png", 0)
n1 = cv2.imread("pic/n1.png", 0)
n2 = cv2.imread("pic/n2.png", 0)
n3 = cv2.imread("pic/n3.png", 0)
n4 = cv2.imread("pic/n4.png", 0)
n5 = cv2.imread("pic/n5.png", 0)
n6 = cv2.imread("pic/n6.png", 0)
n7 = cv2.imread("pic/n7.png", 0)
n8 = cv2.imread("pic/n8.png", 0)
n9 = cv2.imread("pic/n9.png", 0)

#w, h = template.shape[::-1]

img_gray = cv2.cvtColor(np.array(base_screen), cv2.COLOR_BGR2GRAY)
#cv2.imshow("Screenshot", img_gray)
#cv2.waitKey(0)
def detect_coord(img):
    z = []
    res = cv2.matchTemplate(img_gray, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.79)
    loc_array = np.array(loc)
    #print (np.array(loc))
    for i in range(len(loc_array[0])):
        z.append([(loc_array[1, i]), (loc_array[0, i])])
    # for pt in zip(*loc[::-1]):
    #     x = int(pt[0])
    #     y = int(pt[1])
    return z

p0 = detect_coord(n0)
p1 = detect_coord(n1)
p2 = detect_coord(n2)
p3 = detect_coord(n3)
p4 = detect_coord(n4)
p5 = detect_coord(n5)
p6 = detect_coord(n6)
p7 = detect_coord(n7)
p8 = detect_coord(n8)
p9 = detect_coord(n9)
px = p0+p1+p2+p3+p4+p5+p6+p7+p8+p9

#exit(0)
x=""
# print("px = ",px)
# print("min px = ",min(px))
while px:
    if min(px) in p0:
        x = x + "0"
        p0.pop(p0.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p1:
        x = x + "1"
        p1.pop(p1.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p2:
        x = x + "2"
        p2.pop(p2.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p3:
        x = x + "3"
        p3.pop(p3.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p4:
        x = x + "4"
        p4.pop(p4.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p5:
        x = x + "5"
        p5.pop(p5.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p6:
        x = x + "6"
        p6.pop(p6.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p7:
        x = x + "7"
        p7.pop(p7.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p8:
        x = x + "8"
        p8.pop(p8.index(min(px)))
        px.pop(px.index(min(px)))
    elif min(px) in p9:
        x = x + "9"
        p9.pop(p9.index(min(px)))
        px.pop(px.index(min(px)))

print("строка:", x)

#print(detect_coord(n2))
#pyautogui.moveTo(detect_coord(n1))