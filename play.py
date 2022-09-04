from time import sleep
import numpy as np
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd= r'D:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

window_name = 'image'
image = cv2.imread("simulating.jpg")

crop_img = image[110:150, 250:425]

greyscale = cv2.cvtColor(np.array(crop_img), cv2.COLOR_RGB2GRAY)

sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
sharpen = cv2.filter2D(greyscale, -1, sharpen_kernel)

thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

#cv2.rectangle(image, (250,100), (425,150), (0, 255, 0), 3)
#cv2.imshow(window_name, crop_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

text = pytesseract.image_to_string(thresh)

print(text)