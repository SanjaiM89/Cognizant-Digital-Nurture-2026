import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('message', ['Hello', 'Selenium Automation', '12345'])
def test_simple_form_submission(driver, base_url, message):
    driver.get(base_url + "simple-form-demo/")

    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys(message)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )
    submit_button.click()

    message_display = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message_display.text == message


def test_checkbox_demo(driver, base_url):
    driver.get(base_url + "checkbox-demo/")

    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(.,'Click on check box')]/input[@type='checkbox']"))
    )

    checkbox.click()
    assert checkbox.is_selected() is True

    checkbox.click()
    assert checkbox.is_selected() is False


def test_dropdown_selection(driver, base_url):
    driver.get(base_url + "select-dropdown-demo/")

    dropdown = Select(driver.find_element(By.ID, "select-demo"))
    dropdown.select_by_visible_text("Wednesday")

    assert dropdown.first_selected_option.text == "Wednesday"
