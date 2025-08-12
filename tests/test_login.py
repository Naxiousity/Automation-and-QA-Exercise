import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from automation.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # For Docker
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    driver = webdriver.Remote(command_executor=selenium_url, options=options)

    # For Individual Testing
    # driver = webdriver.Chrome(options=options)

    driver.get("https://automationexercise.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()
    try:
        driver.quit()
    except Exception as e:
        print(f"Error during driver.quit(): {e}")


@pytest.mark.parametrize("email,password,expect_success", [
    ("bordeuxx@gmail.com", "test123", True),
    ("minininininininii@example.com", "wrongpass", False),
])
def test_login_functionality(driver, email, password, expect_success):
    login_page = LoginPage(driver)

    # Assert login section is visible
    assert login_page.is_login_section_visible()

    # Perform login
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()

    if expect_success:
        assert login_page.is_logout_button_visible(), "Logout button not visible – login may have failed"
    else:
        assert login_page.is_error_message_visible(), "Expected error message not shown"