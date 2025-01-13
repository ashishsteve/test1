from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.maximize_window()
act_title=driver.title
exp_title="Practice Pages"

if act_title==exp_title:
    print("Page title is correct")
else:
    print("Page title is incorrect")
