from time import sleep
import numpy as np
import pyautogui
import cv2

sleep(5)
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
cv2.imwrite("in_memory_to_disk.png", image)