from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
import time

# WebDriver Chrome
#driver = webdriver.Chrome()

# Target URL
driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
# To load entire webpage
time.sleep(5)

# Printing the whole body text
print(driver.find_element(By.XPATH, "/html/body").text)

# Closing the driver
driver.close()

