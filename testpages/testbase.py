# import pytest
# from utilities.logger import get_logger
#
# class BaseTest:
#     logger = get_logger(__name__)
#
#     @pytest.fixture(autouse=True)
#     def setup(self,driver,config):
#         self.driver = driver
#         self.config = config
#         self.logger = get_logger(self.__class__.__name__)
#         self.logger.info("-----Test Started-----")
#         yield
#         self.logger.info("-----Test Ended-----")

# tests/test_base.py

import pytest
from utilities.config_reader import get_config
from pages.login import LoginPage
from utilities.logger import get_logger

class TestBase:
    @pytest.fixture(autouse=True)
    def setup(self, setup_driver):
        """
        Common setup for all tests:
        - Launch browser
        - Navigate to base URL
        - Initialize logger
        """
        self.driver = setup_driver
        self.cfg = get_config()
        self.logger = get_logger(self.__class__.__name__)

        self.logger.info("Launching browser and opening base URL...")
        self.driver.get(self.cfg["base_url"])

        # Initialize commonly used pages
        self.login_page = LoginPage(self.driver)

        yield
        self.logger.info("Closing browser...")
        self.driver.quit()

