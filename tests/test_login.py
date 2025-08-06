import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from automation.pages.login_page import LoginPage


@pytest.mark.parametrize("email,password,expect_success", [
    ("test@example.com", "correctpass", True),   # 🔁 Replace with actual working credentials
    ("wrong@example.com", "wrongpass", False),
])

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

def test_login_functionality(driver, email, password, expect_success):
    login_page = LoginPage(driver)

    # Assert login section is visible
    assert login_page.is_login_section_visible()

    # Perform login
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()

    if expect_success:
        # If login is expected to succeed, assert that error is NOT visible
        assert not login_page.is_error_message_visible()
    else:
        # If login expected to fail, assert error message is visible
        assert login_page.is_error_message_visible()
