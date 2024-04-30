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
a = driver.implicitly_wait(15)
AC = ActionChains(driver)

# login

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='My Info']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Personal Details']").click()
First_Name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
time.sleep(6)
First_Name.click() and First_Name.clear()
driver.execute_script('arguments[0].select()', First_Name)
First_Name.send_keys("Mohammad")
a
Middle_Name = driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
Middle_Name.click() and Middle_Name.clear()
driver.execute_script('arguments[0].select()', Middle_Name)
Middle_Name.send_keys("Zayn")
a
Last_Name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
Last_Name.click() and Last_Name.clear()
driver.execute_script('arguments[0].select()', Last_Name)
Last_Name.send_keys("Shaikh")
a
Nick_Name = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
Nick_Name.click() and Nick_Name.clear()
driver.execute_script('arguments[0].select()', Nick_Name)
Nick_Name.send_keys("Anna")
a
Employee_Id = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
Employee_Id.click() and Employee_Id.clear()
driver.execute_script('arguments[0].select()', Employee_Id)
Employee_Id.send_keys("2014M047")
a
Other_Id = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
Other_Id.click() and Other_Id.clear()
driver.execute_script('arguments[0].select()', Employee_Id)
Employee_Id.send_keys("14016M21")
a
License_Number = driver.find_element(By.XPATH, '(//input)[7]')
License_Number.click() and License_Number.clear()
driver.execute_script('arguments[0].select()', License_Number)
License_Number.send_keys("245678")
a
Expiry_Date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
Expiry_Date.click() and Employee_Id.clear()
driver.execute_script('arguments[0].select()', Expiry_Date)
Employee_Id.send_keys('2024-10-18')
driver.save_screenshot("DateCapture.png")
AC.key_down(Keys.ENTER).perform()
a
Ssn_Num = driver.find_element(By.XPATH, "//div[@class='oxd-form-row']//div[3]//div[1]//div[1]//div[2]//input[1]")
Ssn_Num.clear() and Ssn_Num.click()
driver.execute_script('arguments[0].select()', Ssn_Num)
Ssn_Num.send_keys("80194")
a
Sin_Num = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[8]")
Sin_Num.clear() and Sin_Num.click()
driver.execute_script('arguments[0].select()', Sin_Num)
Sin_Num.send_keys("54921")
time.sleep(10)
a
nationality_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div)[82]//div[1]//div[1]")))
nationality_dropdown.click()
for x in range(5):
    AC.key_down(Keys.ARROW_DOWN).perform()
    if x == 4:
        AC.key_down(Keys.ENTER).perform()
        break
a
Status = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
Status.click()
AC = ActionChains(driver)
for x in range(3):
    AC.key_down(Keys.ARROW_DOWN).perform()
    if x == 1:
        AC.key_down(Keys.ENTER).perform()
        break
driver.implicitly_wait(10)
DOB = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
DOB.click() and DOB.clear()
driver.execute_script('arguments[0].select()', DOB)
DOB.send_keys('1998-10-18')
AC.key_down(Keys.ENTER).perform()
a
# Gender
driver.find_element(By.XPATH, "//label[normalize-space()='Female']").click()
# driver.find_element(By.XPATH, "//label[normalize-space()='Male']").click()
a
Mil_Ser = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[10]")
Mil_Ser.click() and Mil_Ser.clear()
driver.execute_script('argument[0].select()', Mil_Ser)
Mil_Ser.send_keys('35 Years')
a
Smoker = driver.find_element(By.XPATH,"//label[normalize-space()='Yes']")
Smoker.clear() and Smoker.is_selected()
a
driver.find_element(By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]").click()
Blood_Type = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]")
Blood_Type.click()
for x in range(6):
    AC.key_down(Keys.ARROW_DOWN).perform()
    if x == 1:
        AC.key_down(Keys.ENTER).perform()
        break
a
driver.find_element(By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[2]").click()
driver.save_screenshot('Sucessful.png')