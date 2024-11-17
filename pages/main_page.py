from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    CATALOG = (By.XPATH, '//span[text()="Каталог"]')
    ELECTRONICS = (By.XPATH, '//div[contains(@class, "head-dropdown-catalog")]'
                                      '/a[contains(@href, "/catalog/elektronika/")]')
    TABLETS = (By.XPATH, '//div[contains(@class, "head-dropdown-catalog")]'
                                    '/a[contains(@href, "/catalog/planshety/")]')
    DIGMA = (By.XPATH, '//a[contains(@href, "/catalog/digma/")]')
    ITEM = (By.XPATH, '//a[contains(@class, "item-card__title")]')

    def choose_digma_tablet(self):
        self.click_element(self.CATALOG)
        self.hover_over_element(self.ELECTRONICS)
        self.hover_over_element(self.TABLETS)
        self.hover_over_element_and_click(self.DIGMA)

    def get_item_name(self):
        item = self.get_element(self.ITEM)
        return item.text
