from automation.base_driver import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    CART_PAGE_INDICATOR = (By.XPATH, "//h2[contains(text(), 'Shopping Cart')]")
    CART_ITEMS = (By.XPATH, "//table[@class='table table-condensed']//tbody/tr")

    def __init__(self, driver):
        super().__init__(driver)

    def click_continue_shopping_button(self):
        continue_btn = self.wait_until_element_is_clickable(self.CONTINUE_SHOPPING_BUTTON)
        continue_btn.click()

    def get_title(self):
        return self.driver.title

    def is_cart_page_visible(self):
        return self.wait_until_element_is_visible(self.CART_PAGE_INDICATOR).is_displayed()

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))