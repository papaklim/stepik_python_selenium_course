from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Test(unittest.TestCase):
    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')
        # Код, который заполняет обязательные поля
        firstname = browser.find_element_by_css_selector('.first_block .first')
        firstname.send_keys("Andrey")
        lastname = browser.find_element_by_css_selector('.first_block .second')
        lastname.send_keys("K")
        email = browser.find_element_by_css_selector('.first_block .third')
        email.send_keys("test@test.test")
        phone = browser.find_element_by_css_selector('.second_block .first')
        phone.send_keys("+79991234567")
        address = browser.find_element_by_css_selector('.second_block .second')
        address.send_keys('Russia, Saint Petersburg')
        # Отправляем заполненную форму
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))
        )
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')
        # Код, который заполняет обязательные поля
        firstname = browser.find_element_by_css_selector('.first_block .first')
        firstname.send_keys("Andrey")
        lastname = browser.find_element_by_css_selector('.first_block .second')
        lastname.send_keys("K")
        email = browser.find_element_by_css_selector('.first_block .third')
        email.send_keys("test@test.test")
        phone = browser.find_element_by_css_selector('.second_block .first')
        phone.send_keys("+79991234567")
        address = browser.find_element_by_css_selector('.second_block .second')
        address.send_keys('Russia, Saint Petersburg')
        # Отправляем заполненную форму
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))
        )
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()