from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
driver.get("https://demo.nopcommerce.com/")


driver.find_elements(By.TAG_NAME,'a')
print(len(links))