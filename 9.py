from selenium import webdriver
import time
import math


browser = webdriver.Chrome()
url = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(url)
    value = browser.find_element_by_id('input_value')
    x = value.text
    calc_x = calc(x)
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(calc_x)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    browser.execute_script("window.scrollBy(0, 120);")
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    btn = browser.find_element_by_css_selector('[type="submit"]')
    btn.click()

finally:
    time.sleep(5)
    browser.quit()