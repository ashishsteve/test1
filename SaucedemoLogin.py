from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.driver import Driver

from FirstTestCase import exp_title, act_title

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()

#driver.find_element(By.ID,"user-name").send_keys("standard_user")
#driver.find_element(By.ID,"password").send_keys("secret_sauce")
#driver.find_element(By.ID,"login-button").click()



act_title=driver.title
exp_title="Swag Labs"

if act_title==exp_title:
    print("Login Test Passed")

else:
    print("Login Test Failed")
#driver.find_element(By.ID,"uname").send_keys("ashish_Ananad@gmrwebteam.com")
#driver.find_element(By.ID,"Password").send_keys()
#driver.find_element(By.ID,"login_sub_button").click()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

