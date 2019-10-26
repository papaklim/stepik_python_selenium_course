from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(url)
    linktext = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element_by_link_text(linktext)
    link.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    firstname = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    firstname.send_keys("Andrey")
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    last_name.send_keys("Klementev")
    city = browser.find_element(By.CSS_SELECTOR, '.city')
    city.send_keys("Saint Petersburg")
    country = browser.find_element(By.CSS_SELECTOR, '#country')
    country.send_keys("Russia")
    button.click()

finally:
    time.sleep(10)
    browser.quit()  # закрываем браузер после всех манипуляций
