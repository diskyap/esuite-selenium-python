from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class SignInPage(BasePage):
    """Page object for the sign in screen"""
    
    # locators
    USE_EMAIL_OR_USERNAME_BUTTON = (By.XPATH, "//button[text()='Use Email or Username']")
    USERNAME_INPUT = (By.XPATH, "//input[contains(@name, 'username')]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log In']")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@name, 'password')]")
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
    def sign_in(self, email, password):
        self.navigate()
        self.click_element(self.USE_EMAIL_OR_USERNAME_BUTTON)
        self.enter_text(self.USERNAME_INPUT, email)
        self.click_element(self.LOGIN_BUTTON)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        
    def sign_in_negative(self, email):
        self.navigate()
        self.click_element(self.USE_EMAIL_OR_USERNAME_BUTTON)
        self.enter_text(self.USERNAME_INPUT, email)
        self.click_element(self.LOGIN_BUTTON)
        
    def message(self, locator):
        element = self.get_element(locator)
        return element.text