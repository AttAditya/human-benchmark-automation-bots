from selenium import webdriver
from time import time, sleep
from pyautogui import press

MAX_TIME = float("inf")
URL = "https://humanbenchmark.com/tests/number-memory"

running = True

def inject(driver):
    with open("injection.js", "r") as injection_file:
        javascript_code = injection_file.read()
        driver.execute_script(javascript_code)

def get_element(driver, selector):
    try:
        return driver.find_element(
            "css selector",
            selector
        )
    except:
        return None

def press_button(driver):
    global running

    button = None
    while not button and running:
        button = get_element(
            driver,
            ".number-memory-test button"
        )
    
    if not button:
        return
    
    button.click()

def play(driver):
    input_element = get_element(
        driver,
        ".number-memory-test input"
    )

    if not input_element: return False
    input_element.click()

    press("space")
    press("backspace")
    press("enter")

    sleep(2)

    press_button(driver)

def main(driver):
    global running

    press_button(driver)
    start_time = time()

    while running:
        play(driver)

        current_time = time()
        if current_time - start_time > MAX_TIME:
            running = False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(URL)

    inject(driver)
    main(driver)

    driver.quit()

