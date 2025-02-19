from automation.base_driver import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_continue_shopping_button(self):
        continue_btn = self.wait_until_element_is_clickable((By.XPATH, "//button[contains(text(), 'Continue Shopping')]"))
        continue_btn.click()

    def get_title(self):
        return self.driver.title