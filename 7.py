from selenium import webdriver
import math
import time

url = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(url)
    chest = browser.find_element_by_id('treasure')
    x = chest.get_attribute('valuex')
    res_x = calc(x)
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(res_x)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    submit_button = browser.find_element_by_css_selector('.btn.btn-default')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
