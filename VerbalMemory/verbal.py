import cv2
import numpy as np
import pyautogui
import pytesseract
import time
from collections import deque

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Set the path to the Tesseract executable

def find_word(img):
    x1, y1, x2, y2 = 300, 294, 1180, 392
    word_region = img[y1:y2, x1:x2]
    
    # Preprocessing
    gray = cv2.cvtColor(word_region, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Use Tesseract OCR to extract the word
    word = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
    return word.strip()

def click_button(x, y):
    pyautogui.click(x, y)

def main():
    seen_words = deque(maxlen=100)  # Store the last 100 seen words
    
    while True:
        # Capture the screen
        img = np.array(pyautogui.screenshot())
        
        # Find the word on the screen
        word = find_word(img)
        if word:
            if word in seen_words:
                click_button(574, 434)  # Click the "SEEN" button
            else:
                click_button(784, 434)  # Click the "NEW" button
                seen_words.append(word)
        
        # Pause to avoid overwhelming the system
        time.sleep(0.1)

if __name__ == "__main__":
    main()