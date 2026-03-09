import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.set_preference("intl.accept_languages", user_language)

    print(f"\nstart firefox browser for test with {user_language}...")
    browser = webdriver.Firefox(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()