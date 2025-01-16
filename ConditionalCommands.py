from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
driver.get("https://www.snapdeal.com/")

driver.get("https://www.amazon.com/")
driver.maximize_window()

driver.back()
driver.forward()

driver.refresh()
driver.implicitly_wait(10000)
driver.quit()

