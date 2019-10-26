from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/huge_form.html"
try:
    browser.get(url)
    elements = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
    for element in elements:
        element.send_keys(random.randrange(1, 999))
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла