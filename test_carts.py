import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Launch browser and navigate to URL
    driver.get("http://automationexercise.com")

    # 2. Verify that home page is visible
    assert "Automation Exercise" in driver.title

    # 3. Navigate to Products
    products_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Products')]")))
    products_btn.click()

    # 4. Wait for products page to load
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='All Products']")))

    # 5. Locate "Men Tshirt" product card
    men_tshirt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-overlay' and .//p[text()='Men Tshirt']]")))

    # 6. Hover over "Men Tshirt"
    actions = ActionChains(driver)
    actions.move_to_element(men_tshirt).perform()

    # 7. Click on the shopping cart icon
    cart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-overlay' and .//p[text()='Men Tshirt']]//i[@class='fa fa-shopping-cart']")))
    cart_icon.click()

    # 8. Click on Continue [Modal]
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue Shopping')]")))
    continue_btn.click()

    # Ensure modal disappears before continuing
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='cartModal']")))

    # 9. Locate Colour Blocked Shirt
    colour_blocked_shirt = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-overlay'][.//p[contains(text(), 'Colour Blocked Shirt')]]//i[@class='fa fa-shopping-cart']")))


    
    # Scroll into view to avoid interception
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", colour_blocked_shirt)

    # 10. Hover over Colour Blocked Shirt
    actions.move_to_element(colour_blocked_shirt).perform()

    # 10. Click on the shopping cart icon
    cart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-overlay'][.//p[contains(text(), 'Colour Blocked Shirt')]]//i[@class='fa fa-shopping-cart']")))
    cart_icon.click()

    view_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//u[contains(text(), 'View Cart')]")))
    view_btn.click()
