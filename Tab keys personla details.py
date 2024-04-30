import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(15)

# login

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='My Info']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Personal Details']").click()
driver.implicitly_wait(10)
