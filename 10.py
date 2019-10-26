from selenium import webdriver
import time
import os

url = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()

try:
    browser.get(url)
    firstname = browser.find_element_by_css_selector('[name = \'firstname\']')
    firstname.send_keys('Andrey')
    lastname = browser.find_element_by_css_selector('[name = \'lastname\']')
    lastname.send_keys('Klementev')
    email = browser.find_element_by_css_selector('[name = \'email\']')
    email.send_keys('test@test.test')
    current_dir = (os.path.abspath(os.path.dirname(__file__)))
    full_path = os.path.join(current_dir, 'requirements.txt')
    select_file = browser.find_element_by_id('file')
    select_file.send_keys(full_path)
    btn = browser.find_element_by_class_name('btn-primary')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()