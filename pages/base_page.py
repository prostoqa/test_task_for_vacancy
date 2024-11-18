from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_link(self, link):
        self.driver.get(link)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_element_text(self, locator):
        return self.get_element(locator).text

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

    def clear_textfield(self, locator):
        self.get_element(locator).clear()

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def wait_presence_of_element(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True
