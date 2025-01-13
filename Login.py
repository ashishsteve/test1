from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from FirstTestCase import exp_title, act_title

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://www.gmrwebteam.com/pricing")

act_title=driver.title
exp_title="Pricing | GMR Web Team"

if act_title==exp_title:
    print("Title is correct")
else:
    print("Title is not correct")



