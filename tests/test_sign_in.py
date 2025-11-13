import pytest
from selenium.webdriver.common.by import By
from pages.sign_in_page import SignInPage


class TestSignIn:

    # @pytest.mark.run_only
    def test_successful_sign_in_with_valid_credentials_email(
        self, sign_in_page: SignInPage
    ):

        EMAIL = "it.qa@edot.id"
        PASSWORD = "it.QA2025"

        sign_in_page.sign_in(EMAIL, PASSWORD)

        # assert locators
        WELCOME_WORDING = (By.XPATH, "//span[text()='Welcome Back,']")
        assert sign_in_page.is_element_present(WELCOME_WORDING) is True
        
    # @pytest.mark.run_only
    def test_successful_sign_in_with_valid_credentials_username(
        self, sign_in_page: SignInPage
    ):

        USERNAME = "itqaedot"
        PASSWORD = "it.QA2025"

        sign_in_page.sign_in(USERNAME, PASSWORD)

        # assert locators
        WELCOME_WORDING = (By.XPATH, "//span[text()='Welcome Back,']")
        assert sign_in_page.is_element_present(WELCOME_WORDING) is True
    
    # @pytest.mark.run_only
    def test_verify_sign_in_with_valid_usernameoremail_and_invalid_password(
        self, sign_in_page: SignInPage
    ):

        USERNAME = "itqaedot"
        PASSWORD = "invalidpassword"

        sign_in_page.sign_in(USERNAME, PASSWORD)

        # assert locators
        INVALID_PASSWORD_ERRMESSAGE = (By.XPATH, "//p[text()='Incorrect password']")
        assert sign_in_page.is_element_present(INVALID_PASSWORD_ERRMESSAGE) is True
        assert sign_in_page.message(INVALID_PASSWORD_ERRMESSAGE) == "Incorrect password"
        
    # @pytest.mark.run_only
    def test_verify_sign_in_with_invalid_credentials_email(
        self, sign_in_page: SignInPage
    ):

        EMAIL = "invalidemail@test.com"

        sign_in_page.sign_in_negative(EMAIL)

        # assert locators
        INVALID_EMAIL_ERRMESSAGE = (By.XPATH, "//p[contains(text(), 'Email Not Registered')]")
        REGISTER_BUTTON = (By.XPATH, "//button[text()='Yes, Register']")
        assert sign_in_page.is_element_present(INVALID_EMAIL_ERRMESSAGE) is True
        assert sign_in_page.is_element_present(REGISTER_BUTTON) is True
        assert sign_in_page.message(INVALID_EMAIL_ERRMESSAGE) == "Email Not Registered"
        assert sign_in_page.message(REGISTER_BUTTON) == "Yes, Register"
       
    # @pytest.mark.run_only 
    def test_verify_sign_in_with_empty_credentials_usernameoremail(
        self, sign_in_page: SignInPage
    ):

        EMAIL = ""

        sign_in_page.sign_in_negative(EMAIL)

        # assert locators
        LOGIN_BUTTON_DISABLE = (By.XPATH, "//button[@disabled]")
        assert sign_in_page.get_value(sign_in_page.USERNAME_INPUT) == ""