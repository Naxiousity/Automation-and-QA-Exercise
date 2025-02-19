# home_page.py
from automation.base_driver import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

    def click_products_button(self):
        products_btn = self.wait_until_element_is_clickable((By.XPATH, "//a[contains(text(), 'Products')]"))
        products_btn.click()