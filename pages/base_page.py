from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_link(self, link):
        self.driver.get(link)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.get_element(locator).click()

    def hover_over_element(self, locator):
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_over_element_and_click(self, locator):
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def is_element_present(self, locator):
        try:
            self.get_element(locator)
        except NoSuchElementException:
            return False
        return True