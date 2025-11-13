from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class CompaniesPage(BasePage):
    """Page object for the companies screen"""
    
    # locators
    COMPANIES_BUTTON = (By.XPATH, "//a[text()='Companies']")
    ADD_COMPANIES_BUTTON = (By.XPATH, "//button[text()='Add Company']")
    COMPANIES_NAME_INPUT = (By.XPATH, "//input[@placeholder='Input Company Name']")
    COMPANIES_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Input Email']")
    COMPANIES_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Input Phone']")
    COMPANIES_INDUSTRY_TYPE = (By.XPATH, "//span[text()='Choose Industry Type']")
    COMPANIES_INDUSTRY_TYPE_HEALTH = (By.XPATH, "//div[@data-value='healthcare']")
    COMPANIES_COMPANY_TYPE = (By.XPATH, "//span[text()='Choose Company Type']")
    COMPANIES_COMPANY_TYPE_SERVICE = (By.XPATH, "//div[@data-value='service']")
    COMPANIES_LANGUAGE = (By.XPATH, "//span[text()='Choose Language']")
    COMPANIES_LANGUAGE_INGGRIS = (By.XPATH, "//div[@data-value='english']")
    COMPANIES_ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Input Address']")
    COMPANIES_COUNTRY = (By.XPATH, "//span[text()='Choose Country']")
    COMPANIES_COUNTRY_INDONESIA = (By.XPATH, "//div[@data-value='id']")
    COMPANIES_PROVINCE = (By.XPATH, "//span[text()='Choose Province']")
    COMPANIES_PROVINCE_MALUKU = (By.XPATH, "//div[@data-value='maluku3']")
    COMPANIES_CITY_MALUKU = (By.XPATH, "//span[text()='Choose City']") 
    COMPANIES_CITY_AMBON = (By.XPATH, "//div[@data-value='kota ambon1']")
    COMPANIES_CITY_DISTRICT = (By.XPATH, "//span[text()='Choose District']")
    COMPANIES_CITY_DICTRICT_BAGUALA = (By.XPATH, "//div[@data-value='baguala2']")
    COMPANIES_CITY_SUB_DISTRICT = (By.XPATH, "//span[text()='Choose Sub District']")
    COMPANIES_CITY_SUB_DICTRICT_HALONG  = (By.XPATH, "//div[@data-value='halong4']")
    ADD_COMPANIES_BUTTON_NEXT = (By.XPATH, "//button[text()='Next']")
    TNC_BUTTON = (By.XPATH, "//button[@id='select-all']")
    ADD_COMPANIES_BUTTON_REGISTER = (By.XPATH, "//button[text()='Register']")

    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
    def add_companies(self, companies, email, phone, address):
        self.click_element(self.COMPANIES_BUTTON)
        self.click_element(self.ADD_COMPANIES_BUTTON)
        self.enter_text(self.COMPANIES_NAME_INPUT, companies)
        self.enter_text(self.COMPANIES_EMAIL_INPUT, email)
        self.enter_text(self.COMPANIES_PHONE_INPUT, phone)
        self.select_industry_type_health()
        self.select_company_type_service()
        self.select_language()
        self.enter_text(self.COMPANIES_ADDRESS_INPUT, address)
        self.select_country()
        self.select_province()
        self.select_city()
        self.select_district()
        self.select_sub_district()
        self.click_element(self.ADD_COMPANIES_BUTTON_NEXT)
        self.click_element(self.ADD_COMPANIES_BUTTON_NEXT)
        self.click_element(self.TNC_BUTTON)
        self.click_element(self.ADD_COMPANIES_BUTTON_REGISTER)   
    
    def click_and_select_dropdown(self, locator, value):
        self.click_element(locator)
        self.click_element(value)
    
    def select_industry_type_health(self):
        self.click_and_select_dropdown(self.COMPANIES_INDUSTRY_TYPE, self.COMPANIES_INDUSTRY_TYPE_HEALTH)
        
    def select_company_type_service(self):
        self.click_and_select_dropdown(self.COMPANIES_COMPANY_TYPE, self.COMPANIES_COMPANY_TYPE_SERVICE)
        
    def select_language(self):
        self.click_and_select_dropdown(self.COMPANIES_LANGUAGE, self.COMPANIES_LANGUAGE_INGGRIS)
        
    def select_country(self):
        self.click_and_select_dropdown(self.COMPANIES_COUNTRY, self.COMPANIES_COUNTRY_INDONESIA)

    def select_province(self):
        self.click_and_select_dropdown(self.COMPANIES_PROVINCE, self.COMPANIES_PROVINCE_MALUKU)
        
    def select_city(self):
        self.click_and_select_dropdown(self.COMPANIES_CITY_MALUKU, self.COMPANIES_CITY_AMBON)
        
    def select_district(self):
        self.click_and_select_dropdown(self.COMPANIES_CITY_DISTRICT, self.COMPANIES_CITY_DICTRICT_BAGUALA)
        
    def select_sub_district(self):
        self.click_and_select_dropdown(self.COMPANIES_CITY_SUB_DISTRICT, self.COMPANIES_CITY_SUB_DICTRICT_HALONG)