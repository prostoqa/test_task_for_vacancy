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
