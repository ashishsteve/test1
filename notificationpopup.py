from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver
ops.add_agument("--disable-notifications")
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
driver=webdriver.Chrome(service=serv_obj,options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()