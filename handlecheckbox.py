from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)



driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()
driver.find_element(By.XPATH,'a')
print("total number of links:",len(links))


