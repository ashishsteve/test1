from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v129.fed_cm import click_dialog_button

from FirstTestCase import exp_title, act_title

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://www.krishnamedicalcentre.org/")
sliders=driver.find_element(By.CLASS_NAME,'img-fluid')
print(len(sliders))