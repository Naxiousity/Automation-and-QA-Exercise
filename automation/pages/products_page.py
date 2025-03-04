# products_page.py
from automation.base_driver import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_all_products_title(self):
        return self.wait_until_element_is_visible((By.XPATH, "//h2[text()='All Products']"))

    def add_men_tshirt_to_cart(self):
        # Locate and click the "Add to Cart" button for "Men Tshirt"
        add_to_cart_btn = self.wait_until_element_is_clickable(
            (By.XPATH, "//div[@class='product-overlay' and .//p[text()='Men Tshirt']]//a[@data-product-id]")
        )
        add_to_cart_btn.click()

    def click_view_cart_in_modal(self):
        # Click "View Cart" in the modal that appears after adding to cart
        view_cart_btn = self.wait_until_element_is_clickable(
            (By.XPATH, "//a[contains(text(), 'View Cart')]")
        )
        view_cart_btn.click()

    def click_continue_shopping_in_modal(self):
        # Click "Continue Shopping" in the modal to stay on the products page
        continue_btn = self.wait_until_element_is_clickable(
            (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
        )
        continue_btn.click()