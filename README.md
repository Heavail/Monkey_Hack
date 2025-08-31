# Monkey_Hack
It's a program created specifically to type automatcally on monkey.com website with a very high words per minute and accuracy by the help of pytesseract library and tesseract.exe which are open source and are used to extract texts from an image you can download tesseract.exe from here https://github.com/UB-Mannheim/tesseract/wiki 

[screen-recording-2025-08-31-203239_9VqDDYl3.webm](https://github.com/user-attachments/assets/925ed625-1b0a-4990-b144-9a41f83f5284)



<H1>🐒 How to use it ?</H1>

1. Make sure python is installed in your system.
2. Install the pytesseract,PIL and pyautogui libraries by typing in your cmd "pip install pytesseract", "pip install pyautogui" and "pip install pillow".
3. Install the tesseract.exe from the github link "https://github.com/UB-Mannheim/tesseract/wiki" and provide it's location in your environment path.
4. Then clone this repository in your local folder in order access the program in your device.
5. Once done open monkey type in your browser.
6. Then run the monkey_type.pyw file from the folder.
7. Then head back to the monkey type website ensuring not to press the spacebar button in the mean while.
8. Then move your mouse to the topleft position from where the text of monkeytype website starts and then hit spacebar button as shown in the image below.
<img width="1919" height="914" alt="Screenshot 2025-08-31 190857" src="https://github.com/user-attachments/assets/3923423e-1134-4771-9d7f-1c136af60aae" />
9. Then move your mouse to the bottomrigth position till where the text ends in monkeytype website and then again hit spacebar button as shown in the image below.
<img width="1774" height="951" alt="Screenshot 2025-08-31 191802" src="https://github.com/user-attachments/assets/df581926-e559-4fb4-acca-36f6944056ff" />
10. Then move your mouse to the second line of the text in monkeytype website and press the shift button as shown in the image below.
<img width="1882" height="1005" alt="Screenshot 2025-08-31 192729" src="https://github.com/user-attachments/assets/c004d34e-68d7-4272-b98f-3cee3a5782c2" />

ONCE the following 10 steps are done the program will automatically start typing until you press backspace button to stop it.

NOTE : don't forget to press the backspace once the typing timer is over on monkeytype and then rerun the monkey_type.pyw file and follow the following steps again if you want to repeat the automatic typing


<H1>🤔 How does this work ?</H1>
The code works with the help of three main libraries in python.

1. pyautogui -> which is used to take the screenshot and save it inside the working folder, also it provides the keyboard access to type in the words and take the mouse coordinates to define the area in which screenshot needs to be taken for the text extraction.
2. PIL -> which lets the main code gain the access of the screenshot image in the folder.
3. pytesseract -> which is used to extract text from the image in the form of string.

As the program starts it waits for the space button to be pushed to get it's first topleft coordinates of the rectangle as the postion of the mouse cursor where it was last placed from where the screenshot needs to be taken:-
<img width="1919" height="914" alt="Screenshot 2025-08-31 190857" src="https://github.com/user-attachments/assets/007de6d4-f779-4d16-aee4-8baf697952df" />
Similarily the program waits again for space key to be pressed after placing the mouse position for the bottom right coordinates of the rectangle to define till where the screenshot needs to be taken :-
<img width="1774" height="951" alt="Screenshot 2025-08-31 191802" src="https://github.com/user-attachments/assets/3f11cefa-dc7b-495d-b4af-d29693a1e5f3" />
Then at the last the program waits for the shift key to be pressed and demands for one more coordinate which is named as reset coordinate in order to redefine the topleft coordinates of rectangle for retaking the screenshot so that the program could keeps on typing until the timer ends :-
<img width="1882" height="1005" alt="Screenshot 2025-08-31 192729" src="https://github.com/user-attachments/assets/cfb6876f-5379-40ba-b551-27b189843a02" />
Then after the program takes a screenshot of the screen within our defined rectangle with the help of pyautogui and then it extract the text from the image in the form of string using pytesseract and then start typing until it's done typing all the texts then it agains takes screenshot from our reset coordinates and repeats the same process until the time is over.

NOTE : The program will continue typing even after the time is over so you need to press the backspace button to terminate the program yourself anytime you want to stop the program.
