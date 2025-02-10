from selenium import webdriver
from selenium.webdriver.common.by import By

from FirstTestCase import act_title, exp_title

# Initialize WebDriver (Ensure ChromeDriver is installed and in PATH)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace with your target URL

driver.find_element(By.NAME,'textUsername').send_keys("Admin")
driver.find_element(By.ID,'txtPassword').send_keys("admin123")
driver.find_element(By.ID,btnLogin).click()

act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
    driver.close()

