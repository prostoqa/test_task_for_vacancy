from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    CATALOG = (By.CSS_SELECTOR, '.head-catalog-btn')
    ELECTRONICS = (By.CSS_SELECTOR, '.head-dropdown-catalog [href="/catalog/elektronika/"]')
    TABLETS = (By.CSS_SELECTOR, '.head-dropdown-catalog [href="/catalog/planshety/"]')
    DIGMA = (By.CSS_SELECTOR, '.head-dropdown-catalog [href="/catalog/digma/"]')
    ITEM = (By.CSS_SELECTOR, '.item-card__title')
    TITLE = (By.CSS_SELECTOR, '.row h1')
    BREADCRUMB_DIGMA = (By.CSS_SELECTOR, '.breadcrumb [href="/catalog/digma/"]')

    PERSONAL_ACCOUNT = (By.LINK_TEXT, 'Личный кабинет')
    AUTH = (By.CSS_SELECTOR, '.dropdown-item[href*="auth"]')
    LOGIN_USER = (By.LINK_TEXT, 'Иван Иванов')

    def choose_digma_tablet(self):
        self.click_element(self.CATALOG)
        self.hover_over_element(self.ELECTRONICS)
        self.hover_over_element(self.TABLETS)
        self.hover_over_element_and_click(self.DIGMA)

    def get_item_name(self):
        return self.get_element(self.ITEM).text

    def get_title_name(self):
        return self.get_element(self.TITLE).text

    def check_breadcrumb_digma(self):
        return self.is_element_present(self.BREADCRUMB_DIGMA)

    def go_to_personal_account_to_login(self):
        self.click_element(self.PERSONAL_ACCOUNT)
        self.click_element(self.AUTH)

    def check_successful_login(self):
        return self.wait_presence_of_element(self.LOGIN_USER)
