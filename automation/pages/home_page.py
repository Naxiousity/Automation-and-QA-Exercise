# home_page.py
from automation.base_driver import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    # Locators
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")  # Updated to match actual site
    HOME_PAGE_INDICATOR = (By.XPATH, "//img[@alt='Website for automation practice']")  # Logo as indicator

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

    def click_products_button(self):    
        products_btn = self.wait_until_element_is_clickable((By.XPATH, "//a[contains(text(), 'Products')]"))
        products_btn.click()

    def is_home_page_visible(self):
        # Check if the homepage logo or key element is visible
        return self.wait_until_element_is_visible(self.HOME_PAGE_INDICATOR).is_displayed()

    def click_signup_login_button(self):
        signup_login_btn = self.wait_until_element_is_clickable(self.SIGNUP_LOGIN_BUTTON)
        signup_login_btn.click()