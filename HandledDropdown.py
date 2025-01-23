from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)


driver.get("https://www.nawcare.com/request-an-appointment")
drplocation=Select(driver.find_element(By.XPATH,"//*[@id="






