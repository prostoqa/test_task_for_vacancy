from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FavoritePage(BasePage):

    FAVORITE_TITLE = (By.CSS_SELECTOR, '.rs-favorite-page h1')
    FAVORITE_ITEM_NAME = (By.CSS_SELECTOR, '.item-card__title')
    FAVORITE_ICON_ON_ITEM = (By.CSS_SELECTOR, '.fav')
    FAVORITE_EMPTY = (By.CSS_SELECTOR, '.empty-list div')

    def get_favorite_page_title(self):
        return self.get_element_text(self.FAVORITE_TITLE)

    def get_favorite_item_name(self):
        return self.get_element_text(self.FAVORITE_ITEM_NAME)

    def delete_item_from_favorite(self):
        self.hover_over_element_and_click(self.FAVORITE_ICON_ON_ITEM)

    def get_empty_favorite(self):
        self.wait_presence_of_element(self.FAVORITE_EMPTY)
        return self.get_element_text(self.FAVORITE_EMPTY)
