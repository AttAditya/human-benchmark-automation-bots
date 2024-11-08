import time
import pytesseract
from PIL import ImageGrab, ImageEnhance, ImageOps
import pyautogui
import re

# Path to Tesseract executable (adjust this path if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define the updated screen region for OCR (left, top, right, bottom)
capture_region = (208, 336, 1159, 470)

# Wait for 3 seconds before capturing the screen
print("Waiting for 3 seconds...")
time.sleep(3)

# Capture the specified region of the screen
screenshot = ImageGrab.grab(bbox=capture_region)

# Pre-process the image: convert to grayscale, increase contrast
screenshot = ImageOps.grayscale(screenshot)
enhancer = ImageEnhance.Contrast(screenshot)
screenshot = enhancer.enhance(2)  # Increase contrast

# Perform OCR on the enhanced image
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(screenshot, config=custom_config)

# Print the raw extracted text
print("Raw extracted text:", text)

# Post-process the extracted text
def process_text(text):
    # Remove extra whitespace and newlines
    text = ' '.join(text.split())
    
    # Add space after periods that are followed by a capital letter
    text = re.sub(r'\.([A-Z])', r'. \1', text)
    
    # Common OCR corrections
    text = re.sub(r'\bI\b', 'l', text)  # Replace isolated "I" with "l"
    text = re.sub(r'\bO\b', '0', text)  # Replace isolated "O" with "0"
    
    # Ensure proper spacing after punctuation marks
    text = re.sub(r'([.!?])([A-Za-z])', r'\1 \2', text)
    
    # Remove any double spaces that might have been created
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

# Process the text
processed_text = process_text(text)

# Print the processed text
print("Processed text:", processed_text)

# Click on coordinates and wait 1 second before typing
pyautogui.click(x=206, y=404)
time.sleep(1)

# Type out the processed text
pyautogui.typewrite(processed_text)