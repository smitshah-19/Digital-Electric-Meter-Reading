import cv2
import easyocr
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import re #it is a library called regular expression that is used to find/match a string
from sty import fg, ef, rs, Style, RgbFg,bg, RgbBg #used for coloring the font

class OCR_Reader:
  def grayscale(self,image):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    return image

  def remove_noise(self,image):
    image = cv2.medianBlur(np.array(image), 5)
    return image

  def recognize_text(self,image):
    '''loads an image and recognizes text.'''

    reader = easyocr.Reader(['en']) #initialize the OCR reader
    return reader.readtext(image)

  def desired_output(self,result):
    '''This function is made in order to extract the digits that are necessary to yeild'''
    digits = []
    for (bbox, text, prob) in result:
        if prob >= 0.3:
            numbers = re.findall("([0-9]+[,.]+[0-9]+)", text)
            if numbers == [] and len(text) >= 4:
                number = re.findall("([0-9])", text)
                numbers = str(''.join(number))
            if numbers != []:
                digits.append(numbers)

    for element in digits: #this will remove the unnecessary elements from the digits list
        digits.remove("")
    return digits

  def show_result(self,image):
    ef_dir=dir(ef)
    fg_dir=dir(fg)
    plt.imshow(image)
    print("\n")
    name = "Summary"
    yellow_background_string = fg.da_red + bg.yellow + name + rs.all
    print(yellow_background_string)
    print("\n")

    print("Vavg = {} V".format(digits[0]))
    print("Iavg = {} A".format(digits[1]))
    print("Ptot = {} kW".format(digits[2]))
    print("E Del = {} MWh".format(digits[3]))


raw_image = cv2.imread("meter.jpg")
image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
reader = OCR_Reader()
image = reader.grayscale(image)
image = reader.remove_noise(image)
result = reader.recognize_text(image)
digits = reader.desired_output(result)
reader.show_result(raw_image)
