import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from automation.pages.home_page import HomePage
from automation.pages.products_page import ProductsPage
from automation.pages.cart_page import CartPage
import os
 

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    driver = webdriver.Remote(command_executor=selenium_url, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    # Navigate to products
    driver.get("http://automationexercise.com")
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible(), "Home page failed to load"


    home_page.click_products_button()

    # Select product and add to cart
    products_page = ProductsPage(driver)
    products_page.add_men_tshirt_to_cart()
    products_page.click_continue_shopping_in_modal()  

    # Verify cart page and contents
    cart_page = CartPage(driver)
    assert cart_page.is_cart_page_visible(), "Cart page not visible"
    assert cart_page.get_cart_item_count() > 0, "No items in cart"

    # Continue shopping and verify navigation
    cart_page.click_continue_shopping_button()
    assert "products" in driver.current_url.lower(), "Did not return to products page"