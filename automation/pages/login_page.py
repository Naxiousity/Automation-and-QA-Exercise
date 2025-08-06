# login_page.py
from automation.base_driver import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    LOGIN_SECTION = (By.XPATH, "//h2[text()='Login to your account']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Login')]")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_section_visible(self):
        # Verify the login section is visible
        return self.wait_until_element_is_visible(self.LOGIN_SECTION).is_displayed()

    def enter_email(self, email):
        email_field = self.wait_until_element_is_clickable(self.EMAIL_FIELD)
        email_field.clear()  # Clear any pre-filled text
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait_until_element_is_clickable(self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_btn = self.wait_until_element_is_clickable(self.LOGIN_BUTTON)
        login_btn.click()

    def is_error_message_visible(self):
        # Verify the error message is displayed
        return self.wait_until_element_is_visible(self.ERROR_MESSAGE).is_displayed()