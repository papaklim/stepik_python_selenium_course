from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()

try:
    browser.get(url)
    elem_x = browser.find_element_by_css_selector("#input_value")
    x = elem_x.text
    checkbox = browser.find_element_by_css_selector(".form-check-label")
    checkbox.click()
    radio_robot = browser.find_element_by_css_selector("#robotsRule")
    radio_robot.click()
    result = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(result)
    submit = browser.find_element_by_css_selector("button[type=submit]")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()


