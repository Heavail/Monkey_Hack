from PIL import Image 
from pytesseract import pytesseract 
import pyautogui as pg
import keyboard as kb
import time
start = False
def coords():
    coords.topleft,coords.bottomright,coords.reset = (None,None,None)
coords() 
def topleft():
    print('topleft:')
    while coords.topleft == None:
        if kb.is_pressed('space'):
            pos = pg.position()
            print(pos)
            coords.topleft = pos
    return (coords.topleft[0],coords.topleft[1])
def bottomright():
    print('bottomright:')
    while coords.bottomright == None:
        if kb.is_pressed('space'):
            pos = pg.position()
            print(pos)
            coords.bottomright = pos
    while coords.reset == None:
        if kb.is_pressed('shift'):
            pos = pg.position()
            print(pos)
            coords.reset = pos
    return (coords.bottomright[0],coords.bottomright[1])
continues = None
while start == False:
    toplefts = topleft()
    print(toplefts)
    time.sleep(1)   
    bottomright = bottomright()
    start = True
    # time.sleep(1)
    # while continues == None:
    #     if kb.is_pressed('space'):
    #         pos = pg.position()
    #         print(pos)
    #         continues = pos
    #         start = True
while True:
    pg.screenshot(imageFilename='hack.png',region=(toplefts[0],toplefts[1],bottomright[0] - toplefts[0],bottomright[1] - toplefts[1]))

    path_to_tesseract = r"C://Program Files//Tesseract-OCR//tesseract.exe"
    image_path = r"hack.png"

    img = Image.open(image_path) 
    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img) 
    text = text.replace('\n',' ')
    # time.sleep(10)
    print(text[:-1])
    for i in text:
        if kb.is_pressed('backspace'):
            quit()
        pg.press(i,presses=1,interval=0.001,_pause=False)
    coords.topleft = None
    print('topleft: ')
    toplefts = coords.reset      
    time.sleep(0.5)
# import cv2
# from pytesseract import pytesseract
# import numpy as np

# # Load the image
# image = cv2.imread('Screenshot (908).png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply binary thresholding to segment out the text
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# # Use Tesseract-OCR to extract text and word positions from the thresholded image
# data = pytesseract.image_to_data(thresh, lang='eng', config='--psm 11', output_type=pytesseract.Output.DICT)
# text = pytesseract.image_to_string('Screenshot (908).png') 
# print(text)


# # Get the number of words
# num_words = len(data['text'])

# # Iterate over each word
# for i in range(num_words):
#     # Get the word text and position
#     word_text = data['text'][i]
#     word_x = data['left'][i]
#     word_y = data['top'][i]
#     word_w = data['width'][i]
#     word_h = data['height'][i]

#     # Print the word text and position
#     if word_text != '' or word_text != ' ' or word_text != '\n':
#         print(f"Word {i+1}: {word_text} at ({word_x}, {word_y}) with size {word_w}x{word_h}")

#     # Draw a rectangle around the word
#     cv2.rectangle(image, (word_x, word_y), (word_x + word_w, word_y + word_h), (0, 255, 0), 2)

# # Display the output
# cv2.imshow('Output', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
