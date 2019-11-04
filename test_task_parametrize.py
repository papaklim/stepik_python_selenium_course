from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

answer = math.log(int(time.time()))
pages_to_check = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]
code = []


@pytest.mark.parametrize("page", pages_to_check)
def test_check_feedback_text(page, browser):
    url = 'https://stepik.org/lesson/{}/step/1'.format(page)
    answer = str(math.log(int(time.time())))
    browser.get(url)
    text_area = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
    )
    text_area.click()
    text_area.send_keys(answer)
    btn = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
    )
    btn.click()
    check_feedback = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'smart-hints__hint'))
    )
    if check_feedback.text != "Correct!":
        code.append(check_feedback.text)
    assert check_feedback.text == "Correct!"



def test_code_phrase():
    print(f'\nCode phrase: \"{code[0]}{code[1]}{code[2]}\"')



