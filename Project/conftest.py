from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

def pytest_addoption(parser):
    parser.addoption(
        '--lang', action='store', default='en', help='Specify the language.'
    )

@pytest.fixture
def browser(request):
    print('\nOpening a browser...')
    language = request.config.getoption('lang')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print('\nClosing the browser...')
    time.sleep(2)
    browser.quit()




