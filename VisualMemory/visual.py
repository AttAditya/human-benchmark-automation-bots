from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import keyboard
import time

start_button = 'p'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up Selenium browser with WebDriver manager
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get("https://humanbenchmark.com/tests/memory")

# Wait to start the program
keyboard.wait(start_button)

num_squares = 3
while True:
    active_elements = []
    while len(active_elements) != num_squares:
        active_elements = browser.find_elements(By.CSS_SELECTOR, 'div.active')
    
    time.sleep(2)
    
    for element in active_elements:
        element.click()

    time.sleep(1)
        
    # Break out of loop
    if keyboard.is_pressed(start_button): 
        break

    num_squares += 1
