from selenium.webdriver.common.by import By

from pages.base import BasePage



class LoginPage(BasePage):
        def __init__(self, driver):
            super().__init__(driver)
            self.username = (By.NAME, "username")
            self.password = (By.NAME, "password")
            self.login_button = (By.XPATH, "//button[@type='submit']")
            self.error_message = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

        def login(self, user, pwd):
            self.type(self.username, user)
            self.type(self.password, pwd)
            self.click(self.login_button)

        def get_error_message(self):
            if self.is_visible(self.error_message):
                return self.get_text(self.error_message)
            return None








