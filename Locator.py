from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.driver import Driver

from FirstTestCase import exp_title, act_title

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.ID,"small-searchterms").send_keys("laptop")

