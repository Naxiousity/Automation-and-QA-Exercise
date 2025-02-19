import pytest
from selenium import webdriver
from automation.pages.home_page import HomePage
from automation.pages.products_page import ProductsPage
from automation.pages.cart_page import CartPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    home_page = HomePage(driver)
    home_page.click_products_button()

    products_page = ProductsPage(driver)
    products_page.click_men_tshirt()

    cart_page = CartPage(driver)
    cart_page.click_continue_shopping_button()

    # Add any additional assertions or verifications here
    assert cart_page.get_title() == "Shopping Cart"