from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    CATALOG = (By.CSS_SELECTOR, '.head-catalog-btn')
    ELECTRONICS = (By.CSS_SELECTOR, '.head-dropdown-catalog [href="/catalog/elektronika/"]')
    TABLETS = (By.CSS_SELECTOR, '.head-dropdown-catalog [href="/catalog/planshety/"]')
    DIGMA = (By.CSS_SELECTOR, '.head-dropdown-catalog [href="/catalog/digma/"]')
    TITLE = (By.CSS_SELECTOR, '.row h1')
    BREADCRUMB_DIGMA = (By.CSS_SELECTOR, '.breadcrumb [href="/catalog/digma/"]')

    ITEM_TITLE = (By.CSS_SELECTOR, '.item-card__title')
    ITEM_PRICE = (By.CSS_SELECTOR, '.rs-price-new')
    ITEM_ADD_TO_CART = (By.CSS_SELECTOR, '.item-product-cart-action button')
    ITEM_ADD_TO_FAVORITE = (By.CSS_SELECTOR, '.rs-favorite')

    PERSONAL_ACCOUNT = (By.LINK_TEXT, 'Личный кабинет')
    AUTH = (By.CSS_SELECTOR, '.dropdown-item[href*="auth"]')
    LOGIN_USER = (By.LINK_TEXT, 'Иван Иванов')

    CART = (By.CSS_SELECTOR, '.cart')
    ITEMS_COUNT_ON_CART = (By.CSS_SELECTOR, '#rs-cart .rs-cart-items-count')
    PRICE_ON_CART = (By.CSS_SELECTOR, '#rs-cart .rs-cart-items-price')

    FAVORITE = (By.CSS_SELECTOR, '.head-icon-link[href="/favorite/"] .position-relative')
    FAVORITES_AMOUNT = (By.CSS_SELECTOR, '.head-icon-link .rs-favorite-items-count')

    def choose_digma_tablet(self):
        self.click_element(self.CATALOG)
        self.hover_over_element(self.ELECTRONICS)
        self.hover_over_element(self.TABLETS)
        self.hover_over_element_and_click(self.DIGMA)

    def get_item_name(self):
        return self.get_element_text(self.ITEM_TITLE)

    def get_title_name(self):
        return self.get_element_text(self.TITLE)

    def check_breadcrumb_digma(self):
        return self.is_element_present(self.BREADCRUMB_DIGMA)

    def go_to_personal_account_to_login(self):
        self.click_element(self.PERSONAL_ACCOUNT)
        self.click_element(self.AUTH)

    def check_successful_login(self):
        return self.wait_presence_of_element(self.LOGIN_USER)

    def get_item_price(self):
        return self.get_element_text(self.ITEM_PRICE)

    def add_item_to_cart(self):
        self.hover_over_element_and_click(self.ITEM_ADD_TO_CART)

    def get_items_and_price_on_empty_cart(self):
        self.hover_over_element(self.CART)
        return self.is_element_absent(self.ITEMS_COUNT_ON_CART) and self.is_element_absent(self.PRICE_ON_CART)

    def get_amount_and_price_on_cart_with_item(self):
        self.hover_over_element(self.CART)
        return self.get_element_text(self.ITEMS_COUNT_ON_CART), self.get_element_text(self.PRICE_ON_CART)

    def go_to_cart_from_main_page(self):
        self.hover_over_element(self.CART)
        self.click_element(self.CART)

    def add_item_to_favorite(self):
        self.hover_over_element(self.ITEM_ADD_TO_FAVORITE)
        self.click_element(self.ITEM_ADD_TO_FAVORITE)

    def get_amount_on_favorite_icon(self):
        self.hover_over_element(self.FAVORITE)
        return self.get_element_text(self.FAVORITES_AMOUNT)

    def get_no_amount_on_favorite_icon(self):
        self.hover_over_element(self.FAVORITE)
        return self.is_element_absent(self.FAVORITES_AMOUNT)

    def go_to_favorite_page(self):
        self.hover_over_element_and_click(self.FAVORITE)
