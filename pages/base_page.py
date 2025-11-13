from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:

    URL = "https://esuite.edot.id"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.driver.get(self.URL)

    def get_element(self, locator):
        try:

            method, value = locator

            return self.wait.until(EC.visibility_of_element_located((method, value)))

        except NoSuchElementException:
            self.capture_screenshot()
            raise

    def click_element(self, locator):
        try:
            method, value = locator

            # Menunggu elemen terlihat (visible)
            element = self.wait.until(EC.visibility_of_element_located((method, value)))
            element.click()

        except NoSuchElementException:
            self.capture_screenshot()
            raise

    def enter_text(self, locator, text):

        element = self.get_element(locator)
        element.clear()  # Membersihkan field sebelum mengisi
        element.send_keys(str(text))

    def is_element_present(self, locator):
        try:
            self.get_element(locator)
            return True
        except TimeoutException:
            return False
        
    def get_value(self, locator):
        try:
            element = self.get_element(locator)
            return element.get_attribute('value')
            
        except TimeoutException:
            return False