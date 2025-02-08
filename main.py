from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
driver.get("https://www.automationexercise.com/")

log_in = driver.find_element(By.XPATH, "//li/a[contains(text(), 'Signup / Login')]")
log_in.click()

time.sleep(5)
driver.quit()