from selenium import webdriver
import pytest


link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope='class')
@pytest.fixture()
def browser():
    print('\nStart browser for test')
    # browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    yield browser
    print('\nClose browser...')
    browser.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    # @pytest.mark.skip  # маркировка пропуска теста
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    @pytest.mark.smoke
    @pytest.mark.skip  # маркировка пропуска теста
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\nstart test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")

    @pytest.mark.xfail  # (strict=True)  # маркировка теста, который ожидаемо падает
    @pytest.mark.regression
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default")