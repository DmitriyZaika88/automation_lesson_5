from selene import browser
import pytest


@pytest.fixture(scope='session')
def browser_settings():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6.0
