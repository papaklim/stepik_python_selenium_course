from selenium import webdriver
import time

url_1 = "http://suninjuly.github.io/registration1.html"
url_2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(url_2)

    # Ваш код, который заполняет обязательные поля
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
    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(5)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print('test passed')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


