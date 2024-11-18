from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    MODAL_WINDOW_TITLE = (By.CSS_SELECTOR, '.modal-title')
    MODAL_WINDOW_ITEM = (By.CSS_SELECTOR, '.modal-cart-item__title')
    MODAL_WINDOW_CART_AMOUNT = (By.CSS_SELECTOR, '.cart-amount__input input')
    MODAL_WINDOW_ITEM_PRICE = (By.CSS_SELECTOR, '.modal-cart-item__price')
    MODAL_WINDOW_GO_TO_CART = (By.CSS_SELECTOR, '[href="/cart/"].btn')
    MODAL_WINDOW_CLOSE = (By.CSS_SELECTOR, '.modal-close')

    CART_TITLE = (By.CSS_SELECTOR, '.cartCheckout  h2')
    CART_EMPTY = (By.TAG_NAME, 'h2')
    CART_ITEM_NAME = (By.CSS_SELECTOR, '.cart-checkout-item__title')
    CART_ITEMS_AMOUNT = (By.CSS_SELECTOR, '.cart-amount__input input')
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, '.checkout-total-fixed__sum')

    DELETE_ITEM = (By.CSS_SELECTOR, '.cart-checkout-item__del')

    def check_cart_modal_window(self):
        self.wait_presence_of_element(self.MODAL_WINDOW_TITLE)
        return (self.get_element_text(self.MODAL_WINDOW_ITEM), self.get_element_text(self.MODAL_WINDOW_ITEM_PRICE),
                self.get_element(self.MODAL_WINDOW_CART_AMOUNT).get_attribute("value"))

    def modal_window_close(self):
        self.hover_over_element_and_click(self.MODAL_WINDOW_CLOSE)

    def check_cart_page(self):
        self.wait_presence_of_element(self.CART_TITLE)
        return (self.get_element_text(self.CART_TITLE), self.get_element_text(self.CART_ITEM_NAME),
                self.get_element_text(self.CART_TOTAL_PRICE),
                self.get_element(self.CART_ITEMS_AMOUNT).get_attribute("value"))

    def delete_item_from_cart(self):
        self.click_element(self.DELETE_ITEM)

    def get_empty_cart_title(self):
        return self.get_element_text(self.CART_EMPTY)
