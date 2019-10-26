from selenium import webdriver
import math


url = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    first_window = browser.current_window_handle
    browser.get(url)
    btn = browser.find_element_by_class_name('trollface')
    btn.click()
    all_windows = browser.window_handles
    browser.switch_to.window(all_windows[1])
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
