# products_page.py
from base_driver import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_all_products_title(self):
        return self.wait_until_element_is_visible((By.XPATH, "//h2[text()='All Products']"))

    def click_men_tshirt(self):
        men_tshirt = self.wait_until_element_is_visible((By.XPATH, "//div[@class='product-overlay' and .//p[text()='Men Tshirt']]"))
        men_tshirt.click()