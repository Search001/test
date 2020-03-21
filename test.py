import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()

while(True):
    printscreen_pil = ImageGrab.grab(bbox = (0, 400, 600, 1080))
    #printscreen_numpy = np.array(printscreen_pil.getdata(), dtype =
#q'uint8').reshape((printscreen_pil.size[1], printscreen_pil.size[0], 3))
    print(printscreen_pil)
    print(np.array(printscreen_pil))
    cv2.imshow('window', np.array(printscreen_pil))
    print(time.time() - last_time)
    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break