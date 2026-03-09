# tests/test_login.py

import pytest
from testpages.testbase import TestBase

class TestLogin(TestBase):

    def test_valid_login(self):
        self.logger.info("Starting valid login test...")
        self.login_page.login(self.cfg["username"], self.cfg["password"])
        assert "dashboard" in self.driver.current_url.lower()
        self.logger.info("Valid login test passed.")

    def test_invalid_login(self):
        self.logger.info("Starting invalid login test...")
        self.login_page.login("wronguser", "wrongpass")
        error = self.login_page.get_error_message()
        assert error is not None
        assert "Invalid credentials" in error
        self.logger.info("Invalid login test passed with error message.")
