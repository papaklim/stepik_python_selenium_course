from selenium import webdriver
import math


url = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(url)
    btn = browser.find_element_by_css_selector('[type = "submit"]')
    btn.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = (browser.find_element_by_id('input_value')).text
    result = calc(x)
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(result)
    btn = browser.find_element_by_class_name('btn-primary')
    btn.click()
    alert_fin = browser.switch_to.alert
    code = (alert_fin.text.split(":"))[1]
    print("Код решения:", code)

finally:
    browser.quit()
