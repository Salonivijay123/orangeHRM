# conftest.py
import pytest
import os
from utilities.config_reader import get_config
from selenium import webdriver

@pytest.fixture
def setup_driver(request):
    cfg = get_config()
    browser = cfg["browser"].lower()

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver

    # Screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        file_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
        driver.save_screenshot(file_path)

    driver.quit()

def pytest_runtest_makereport(item, call):
    if call.when == "call":
        setattr(item, "rep_call", call)
