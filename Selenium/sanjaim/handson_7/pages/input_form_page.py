from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# The playground's original "Input Form Submit" and "Ajax Form Submit" pages
# have both been replaced with a "Schedule Demo" marketing form (custom
# country/product dropdowns, hidden CRM fields) that isn't safely automatable.
# This page object targets the still-working "Two Input Fields" section on
# the Simple Form Demo page instead, which is the same fill -> submit ->
# read-result pattern the exercise is testing.


class InputFormPage(BasePage):
    FIRST_VALUE = (By.ID, 'sum1')
    SECOND_VALUE = (By.ID, 'sum2')
    GET_SUM_BUTTON = (By.XPATH, "//button[text()='Get Sum']")
    RESULT = (By.ID, 'addmessage')

    def fill_form(self, first_value, second_value):
        self.driver.find_element(*self.FIRST_VALUE).send_keys(first_value)
        self.driver.find_element(*self.SECOND_VALUE).send_keys(second_value)

    def submit_form(self):
        self.driver.find_element(*self.GET_SUM_BUTTON).click()

    def get_success_message(self):
        return self.wait_for_element(self.RESULT).text
