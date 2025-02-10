from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver.get("http://dev23.gmrwebsites.com/admin/login")
driver.find_element(By.ID,'uname').send_keys(' leah@cai-channelislands.org')
driver.find_element(By.ID,'Password').send_keys(' CA_I_LIVE@#')
driver.find_element(By.ID,'login_sub_button').click()
#driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[4]/div[1]/div/div[2]/h4/a').click()

# Wait for the element to be visible before clicking
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//h4/a"))
)
element.click()

button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
driver.execute_script("arguments[0].click();", button)

driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/form/div/div/div[8]/div/input').click()
# Click to open the dropdown
driver.find_element(By.XPATH, "//div[@class='dropdown-button']").click()

# Select an option by text
driver.find_element(By.XPATH, "//li[text()='Option 1']").click()

driver.find_element(By.ID,'ImageName').send_keys("test12345")
driver.find_element(By.ID,'ImageDescription').send_keys("test123445678")


