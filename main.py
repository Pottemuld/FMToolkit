from time import sleep
import tkinter
from tkinter import ttk
import cv2
import pytesseract
import numpy as np
import pyautogui
pytesseract.pytesseract.tesseract_cmd= r'D:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

date_to_test_for = "1 JUL 2036"
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = tkinter.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

while(True):
    sleep(5)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    crop_img = image[10:70, 1575:1715]
    sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    sharpen = cv2.filter2D(crop_img, -1, sharpen_kernel)

    thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(thresh)
    if date_to_test_for in text:
        popupmsg("REMINDER: " + text)



# TODO: 
#   * Do not take screenshots when popup open
#   * Popup layout
#   * JSON based calendar