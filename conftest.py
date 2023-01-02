import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1280, 800)
    yield driver
    driver.quit()

