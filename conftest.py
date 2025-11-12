# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.sign_in_page import SignInPage

@pytest.fixture(scope="function")
def driver():
    """Provides a WebDriver instance for the entire module file."""

    # Setup: Configure Chrome options (headless is optional)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Initialize the WebDriver
    driver.implicitly_wait(20)  # Simple wait strategy
    driver.maximize_window()

    # Yield the driver to the test function
    yield driver
    # Teardown: Close the browser after all tests in the module run
    driver.quit()


@pytest.fixture(scope="function")
def sign_in_page(driver):

    page = SignInPage(driver)
    page.navigate()

    return page