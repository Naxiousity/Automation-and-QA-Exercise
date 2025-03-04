# signup_page.py
from automation.base_driver import BasePage
from selenium.webdriver.common.by import By

class SignUpPage(BasePage):
    # Locators
    NEW_USER_SIGNUP_HEADER = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    SIGNUP_NAME_FIELD = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL_FIELD = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Signup')]")
    ENTER_ACCOUNT_INFO_HEADER = (By.XPATH, "//h2/b[contains(text(), 'Enter Account Information')]")
    TITLE_MR = (By.XPATH, "//input[@value='Mr']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    DAY_DROPDOWN = (By.NAME, "days")
    MONTH_DROPDOWN = (By.NAME, "months")
    YEAR_DROPDOWN = (By.NAME, "years")
    NEWSLETTER_CHECKBOX = (By.NAME, "newsletter")
    OPTIN_CHECKBOX = (By.NAME, "optin")
    FIRST_NAME_FIELD = (By.NAME, "first_name")
    LAST_NAME_FIELD = (By.NAME, "last_name")
    COMPANY_FIELD = (By.NAME, "company")  # Added for clarity
    ADDRESS1_FIELD = (By.ID, "address1")
    ADDRESS2_FIELD = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_FIELD = (By.ID, "state")
    CITY_FIELD = (By.ID, "city")
    ZIPCODE_FIELD = (By.ID, "zipcode")
    MOBILE_NUMBER_FIELD = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Create Account')]")
    ACCOUNT_CREATED_HEADER = (By.XPATH, "//h2/b[contains(text(), 'Account Created!')]")
    CONTINUE_BUTTON = (By.XPATH, "//a[contains(text(), 'Continue')]")
    LOGGED_IN_AS = (By.XPATH, "//i[@class='fa fa-user']")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//i[@class='fa fa-trash-o']")
    ACCOUNT_DELETED_HEADER = (By.XPATH, "//b[contains(text(), 'Account Deleted!')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_new_user_signup_visible(self):
        return self.wait_until_element_is_visible(self.NEW_USER_SIGNUP_HEADER).is_displayed()

    def enter_signup_details(self, name, email):
        self.wait_until_element_is_clickable(self.SIGNUP_NAME_FIELD).send_keys(name)
        self.wait_until_element_is_clickable(self.SIGNUP_EMAIL_FIELD).send_keys(email)

    def click_signup_button(self):
        self.wait_until_element_is_clickable(self.SIGNUP_BUTTON).click()

    def is_enter_account_info_visible(self):
        return self.wait_until_element_is_visible(self.ENTER_ACCOUNT_INFO_HEADER).is_displayed()

    def fill_account_details(self, password, day, month, year):
        self.wait_until_element_is_clickable(self.TITLE_MR).click()
        self.wait_until_element_is_clickable(self.PASSWORD_FIELD).send_keys(password)
        self.wait_until_element_is_clickable(self.DAY_DROPDOWN).send_keys(day)
        self.wait_until_element_is_clickable(self.MONTH_DROPDOWN).send_keys(month)
        self.wait_until_element_is_clickable(self.YEAR_DROPDOWN).send_keys(year)

    def select_checkboxes(self):
        self.wait_until_element_is_clickable(self.NEWSLETTER_CHECKBOX).click()
        self.wait_until_element_is_clickable(self.OPTIN_CHECKBOX).click()

    def fill_address_details(self, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile):
        self.wait_until_element_is_clickable(self.FIRST_NAME_FIELD).send_keys(first_name)
        self.wait_until_element_is_clickable(self.LAST_NAME_FIELD).send_keys(last_name)
        self.wait_until_element_is_clickable(self.COMPANY_FIELD).send_keys(company)
        self.wait_until_element_is_clickable(self.ADDRESS1_FIELD).send_keys(address1)
        self.wait_until_element_is_clickable(self.ADDRESS2_FIELD).send_keys(address2)
        self.wait_until_element_is_clickable(self.COUNTRY_DROPDOWN).send_keys(country)
        self.wait_until_element_is_clickable(self.STATE_FIELD).send_keys(state)
        self.wait_until_element_is_clickable(self.CITY_FIELD).send_keys(city)
        self.wait_until_element_is_clickable(self.ZIPCODE_FIELD).send_keys(zipcode)
        self.wait_until_element_is_clickable(self.MOBILE_NUMBER_FIELD).send_keys(mobile)

    def click_create_account_button(self):
        self.wait_until_element_is_clickable(self.CREATE_ACCOUNT_BUTTON).click()

    def is_account_created_visible(self):
        return self.wait_until_element_is_visible(self.ACCOUNT_CREATED_HEADER).is_displayed()

    def click_continue_button(self):
        self.wait_until_element_is_clickable(self.CONTINUE_BUTTON).click()

    def is_logged_in_as_visible(self):
        return self.wait_until_element_is_visible(self.LOGGED_IN_AS).is_displayed()

    def click_delete_account_button(self):
        self.wait_until_element_is_clickable(self.DELETE_ACCOUNT_BUTTON).click()

    def is_account_deleted_visible(self):
        return self.wait_until_element_is_visible(self.ACCOUNT_DELETED_HEADER).is_displayed()