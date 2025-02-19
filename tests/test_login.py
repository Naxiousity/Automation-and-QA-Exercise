# import pytest

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture(scope="module")

# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

# def test_login(driver):
#     wait = WebDriverWait(driver, 10)
    
#     driver.get("http://automationexercise.com")

#     assert driver.title == "Automation Exercise"

#     driver.find_element(By.XPATH, ""
#                         # enter email
#                         # enter password
#                         # click login
    