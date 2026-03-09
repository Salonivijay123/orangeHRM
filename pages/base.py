# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            raise

    def type(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Typed '{text}' into element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not visible: {locator}")
            raise

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            self.logger.info(f"Got text '{text}' from element: {locator}")
            return text
        except TimeoutException:
            self.logger.error(f"Could not get text from: {locator}")
            raise

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element visible: {locator}")
            return True
        except TimeoutException:
            self.logger.warning(f"Element not visible: {locator}")
            return False

    def open_url(self, url):
        self.driver.get(url)
        self.logger.info(f"Opened URL: {url}")
