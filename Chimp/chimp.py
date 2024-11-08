from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import time

start_button = 'p'

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Optional: starts Chrome maximized

# Setup Chrome service and driver using the latest syntax
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website
browser.get("https://humanbenchmark.com/tests/chimp")

# Create a WebDriverWait instance for explicit waits
wait = WebDriverWait(browser, 10)  # 10 seconds timeout

# wait to start the program
keyboard.wait(start_button)

numbers = 4
while True:
    try:
        for i in range(1, numbers + 1):
            # Wait for element to be clickable and click it
            element = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//div[@data-cellnumber="{i}"]')
                )
            )
            element.click()

        # Wait for and click the continue button
        continue_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[text()="Continue"]')
            )
        )
        continue_button.click()
        
        # break out of the loop if the start button is pressed again
        if keyboard.is_pressed(start_button):
            break

        numbers += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Clean up
browser.quit()