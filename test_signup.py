import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_signup_flow(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Launch browser and 2. Navigate to URL
    driver.get("http://automationexercise.com")

    # 3. Verify that home page is visible
    assert "Automation Exercise" in driver.title

    # 4. Click on Signup
    signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Signup')]")))
    signup_btn.click()

    # 5. Verify 'New User Signup!' is visible
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'New User Signup!')]")))

    # 6. Enter name and email
    name = "Jojo Guitarte"
    driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys(name)
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("Jojotestteste@example.com")

    # 7. Click 'Signup' button
    driver.find_element(By.XPATH, "//button[contains(text(), 'Signup')]").click()

    # 8. Verify 'ENTER ACCOUNT INFORMATION' is visible
    assert wait.until(EC.visibility_of_element_located((By.XPATH,"//h2/b[contains(text(), 'Enter Account Information')]")))

    # 9. Fill account details
    driver.find_element(By.XPATH, "//input[@value='Mr']").click() # hee/hee
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("NotMyFather32x") #password
    driver.find_element(By.XPATH, "//select[@name='days']").send_keys("10") #day
    driver.find_element(By.XPATH, "//select[@name='months']").send_keys("January") #month
    driver.find_element(By.XPATH, "//select[@name='years']").send_keys("1969") #year

    # 10 & 11. Select checkboxes
    driver.find_element(By.XPATH, "//input[@name='newsletter']").click()
    driver.find_element(By.XPATH, "//input[@name='optin']").click()

    # 12. Fill address details
    driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Jojo")
    driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Guits")
    driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Test Company")
    driver.find_element(By.ID, "address1").send_keys("123 Test Street")
    driver.find_element(By.ID, "address2").send_keys("Suite 100")
    driver.find_element(By.ID, "country").send_keys("United States")
    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("Los Angeles")
    driver.find_element(By.ID, "zipcode").send_keys("90001")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

    # # 13. Click 'Create Account' button
    driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]").click()

    # 14. Verify 'ACCOUNT CREATED!' is visible
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//h2/b[contains(text(),'Account Created!')]")))

    # 15. Click 'Continue' button
    driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]").click()

    # 16. Verify 'Logged in as username' is visible
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-user']")))

    # 17. Click 'Delete Account' button
    driver.find_element(By.XPATH, "//i[@class='fa fa-trash-o']").click()

    # 18. Verify 'ACCOUNT DELETED!' is visible and click 'Continue'
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Account Deleted!')]")))
    driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]").click()