from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(url)
    button = browser.find_element(By.XPATH, "//*[@type='submit']")
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
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    print("finish")
    browser.quit()  # закрываем браузер после всех манипуляций