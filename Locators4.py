from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.driver import Driver

from FirstTestCase import exp_title, act_title
from Locators2 import sliders

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#sliders=driver.find_elements(By.CLASS_NAME,'nivo-imageLink')
#print(len(sliders))

driver.find_elements(By.TAG_NAME,'a')
print(len(links))