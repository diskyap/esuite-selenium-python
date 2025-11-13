import pytest
from selenium.webdriver.common.by import By
from pages.sign_in_page import SignInPage
from pages.companies_page import CompaniesPage
from faker import Faker
fake = Faker()

class TestCompanies:

    # @pytest.mark.run_only
    def test_successful_create_a_new_company(self, sign_in_page: SignInPage, companies_page: CompaniesPage):

        EMAIL = "it.qa@edot.id"
        PASSWORD = "it.QA2025"

        sign_in_page.sign_in(EMAIL, PASSWORD)

        # assert locators
        WELCOME_WORDING = (By.XPATH, "//span[text()='Welcome Back,']")
        COMPANIES_TITLE = (By.XPATH, "//span[text()='My Company']")
        assert sign_in_page.is_element_present(WELCOME_WORDING) is True 
        
        COMPANIES_NAME = fake.company()
        EMAIL = "ptmajumundur@corp.com"
        PHONE = "880123456789"
        ADDRESS = "Jalan 123"
        
        companies_page.add_companies(COMPANIES_NAME, EMAIL, PHONE, ADDRESS)
        
        # assret locator
        assert sign_in_page.is_element_present(COMPANIES_TITLE) is True