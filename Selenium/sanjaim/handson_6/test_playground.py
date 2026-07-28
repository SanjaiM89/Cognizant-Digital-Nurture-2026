from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_simple_form_submission(driver):
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys("Hello Selenium")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn-default")
    submit_button.click()

    message_display = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message_display.text == "Hello Selenium"


def test_checkbox_demo(driver):
    driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

    checkbox = driver.find_element(By.ID, "isAgeSelected")

    checkbox.click()
    assert checkbox.is_selected() is True

    checkbox.click()
    assert checkbox.is_selected() is False
