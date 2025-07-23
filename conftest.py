import pytest
from selene import browser

@pytest.fixture(scope='function')
def setting_browser():
    browser.config.window_width = 1366
    browser.config.window_height = 768

@pytest.fixture(scope = 'function')
def browser_open():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.timeout = 10
    yield
    browser.quit()