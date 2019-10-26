from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

url_1 = "http://suninjuly.github.io/selects1.html"
url_2 = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()

try:
    browser.get(url_2)
    select = Select(browser.find_element_by_tag_name('select'))
    num1 = int((browser.find_element_by_id('num1')).text)
    num2 = int((browser.find_element_by_id('num2')).text)
    sum = str(num1 + num2)
    answer = select.select_by_value(sum)
    btn = browser.find_element_by_css_selector('[type="submit"]')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
