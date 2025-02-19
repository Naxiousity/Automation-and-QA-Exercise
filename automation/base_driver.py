# base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_until_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))