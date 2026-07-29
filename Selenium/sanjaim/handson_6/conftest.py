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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            driver.save_screenshot(f'{item.name}_failure.png')
