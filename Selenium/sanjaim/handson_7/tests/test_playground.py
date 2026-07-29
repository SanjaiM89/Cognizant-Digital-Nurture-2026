"""
If the Submit button's ID changed from 'submit' to 'btn-submit' in a flat
(non-POM) script, every test file that calls
driver.find_element(By.ID, 'submit') would break, and the fix would mean
searching through every test file for that locator and updating each one
individually. With POM, the ID only exists once, as a class-level tuple in
the relevant page class (e.g. SimpleFormPage.SUBMIT_BUTTON). Changing the ID
means editing that one line in that one file - every test that uses
click_submit() keeps working without being touched at all.
"""

from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage


def test_simple_form_submission(driver, base_url):
    page = SimpleFormPage(driver)
    page.navigate_to(base_url + "simple-form-demo/")
    page.enter_message("Hello Selenium")
    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"


def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(base_url + "checkbox-demo/")

    page.check_option(0)
    assert page.is_option_checked(0) is True

    page.uncheck_option(0)
    assert page.is_option_checked(0) is False


def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(base_url + "select-dropdown-demo/")
    page.select_day("Wednesday")

    assert page.get_selected_day() == "Wednesday"


def test_input_form_submit(driver, base_url):
    page = InputFormPage(driver)
    page.navigate_to(base_url + "simple-form-demo/")
    page.fill_form("4", "5")
    page.submit_form()

    assert page.get_success_message() == "9"
