from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_FIELD = (By.NAME, 'login')
    PASS_FIELD = (By.NAME, 'pass')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.modal-body button[type="Submit"]')

    def clear_authorization_data(self):
        self.wait_presence_of_element(self.LOGIN_FIELD)
        self.clear_textfield(self.LOGIN_FIELD)
        self.clear_textfield(self.PASS_FIELD)

    def enter_authorization_data(self, login, password):
        self.enter_text(self.LOGIN_FIELD, login)
        self.enter_text(self.PASS_FIELD, password)
        self.click_element(self.SUBMIT_BUTTON)