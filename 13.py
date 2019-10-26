from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


browser = webdriver.Chrome()

url = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(url)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'book'))
    )
    book_button.click()
    x = (browser.find_element_by_id('input_value')).text
    result = calc(x)
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(result)
    submit_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
    )
    submit_button.click()
    alert_fin = browser.switch_to.alert
    code = (alert_fin.text.split(":"))[1]
    alert_fin.accept()
    print("Код решения:", code)

finally:
    browser.quit()