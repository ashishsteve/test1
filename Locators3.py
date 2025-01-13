from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v129.fed_cm import click_dialog_button

from FirstTestCase import exp_title, act_title

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_pass]").send_keys("abc@gmail.com")