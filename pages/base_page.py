from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_link(self, link):
        self.driver.get(link)

    def get_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         f'Element {str(locator)} not found')

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def click_element(self, locator, timeout=10):
        self.wait_clickable_of_element(locator, timeout).click()

    def hover_over_element(self, locator, timeout=10):
        element = self.wait_presence_of_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_over_element_and_click(self, locator, timeout=10):
        element = self.wait_clickable_of_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def is_element_present(self, locator, timeout=10):
        try:
            self.get_element(locator, timeout)
            return True
        except NoSuchElementException: #(TimeoutException,
            return False

    def clear_textfield(self, locator):
        self.get_element(locator).clear()

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def wait_presence_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         f'Element {str(locator)} not present')

    def wait_clickable_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         f'Element {str(locator)} not clickable')

    def is_element_absent(self, locator, timeout=4):
        try:
            self.get_element(locator, timeout)
            return False
        except (NoSuchElementException, TimeoutException):
            return True
