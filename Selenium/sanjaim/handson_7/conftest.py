import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def base_url():
    return 'https://www.testmuai.com/selenium-playground/'
