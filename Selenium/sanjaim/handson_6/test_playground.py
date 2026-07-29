from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_simple_form_submission(driver):
    driver.get("https://www.testmuai.com/selenium-playground/simple-form-demo/")

    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys("Hello Selenium")
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )
    submit_button.click()

    message_display = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message_display.text == "Hello Selenium"


def test_checkbox_demo(driver):
    driver.get("https://www.testmuai.com/selenium-playground/checkbox-demo/")

    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "isAgeSelected"))
    )

    checkbox.click()
    assert checkbox.is_selected() is True

    checkbox.click()
    assert checkbox.is_selected() is False