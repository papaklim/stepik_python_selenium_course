import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", help="Need to choose browser: chrome or firefox"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_name = None
    if browser_name == "chrome":
        print('\nStarting test with chrome browser...')
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print('\nStarting test with firefox browser...')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
