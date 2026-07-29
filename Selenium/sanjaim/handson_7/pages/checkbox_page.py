from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckboxPage(BasePage):
    OPTIONS = (By.CSS_SELECTOR, "input[name^='option']")

    def check_option(self, index):
        checkbox = self.driver.find_elements(*self.OPTIONS)[index]
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self, index):
        checkbox = self.driver.find_elements(*self.OPTIONS)[index]
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self, index):
        return self.driver.find_elements(*self.OPTIONS)[index].is_selected()
