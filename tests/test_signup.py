# test_signup.py
import pytest
from selenium import webdriver
from automation.pages.home_page import HomePage
from automation.pages.signup_page import SignUpPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_signup_flow(driver):
    # Step 1 & 2: Launch browser and navigate to URL
    driver.get("http://automationexercise.com")

    # Step 3: Verify homepage is visible
    home_page = HomePage(driver)
    assert home_page.is_home_page_visible(), "Homepage is not visible"

    # Step 4: Click on 'Signup / Login' button
    home_page.click_signup_login_button()

    # Step 5: Verify 'New User Signup!' is visible
    signup_page = SignUpPage(driver)
    assert signup_page.is_new_user_signup_visible(), "'New User Signup!' section not visible"

    # Step 6: Enter name and email
    signup_page.enter_signup_details("Jojo Guitarte", "Jojotestteste@example.com")

    # Step 7: Click 'Signup' button
    signup_page.click_signup_button()

    # Step 8: Verify 'ENTER ACCOUNT INFORMATION' is visible
    assert signup_page.is_enter_account_info_visible(), "'Enter Account Information' not visible"

    # Step 9: Fill account details
    signup_page.fill_account_details("NotMyFather32x", "10", "January", "1969")

    # Step 10 & 11: Select checkboxes
    signup_page.select_checkboxes()

    # Step 12: Fill address details
    signup_page.fill_address_details(
        "Jojo", "Guits", "Test Company", "123 Test Street", "Suite 100",
        "United States", "California", "Los Angeles", "90001", "1234567890"
    )

    # Step 13: Click 'Create Account' button
    signup_page.click_create_account_button()

    # Step 14: Verify 'ACCOUNT CREATED!' is visible
    assert signup_page.is_account_created_visible(), "'Account Created!' not visible"

    # Step 15: Click 'Continue' button
    signup_page.click_continue_button()

    # Step 16: Verify 'Logged in as username' is visible
    assert signup_page.is_logged_in_as_visible(), "'Logged in as' not visible"

    # Step 17: Click 'Delete Account' button
    signup_page.click_delete_account_button()

    # Step 18: Verify 'ACCOUNT DELETED!' is visible and click 'Continue'
    assert signup_page.is_account_deleted_visible(), "'Account Deleted!' not visible"
    signup_page.click_continue_button()