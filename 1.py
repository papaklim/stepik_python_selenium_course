from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    firstname = browser.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
    firstname.send_keys("Andrey")
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    last_name.send_keys("Klementev")
    city = browser.find_element(By.CSS_SELECTOR, '.city')
    city.send_keys("Saint Petersburg")
    country = browser.find_element(By.CSS_SELECTOR, '#country')
    country.send_keys("Russia")
    button.click()

finally:
    # успеваем скопировать
    time.sleep(10)
    browser.quit()  # закрываем браузер после всех манипуляций

