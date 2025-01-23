
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver

options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)
driver.get("https://google.com/")
driver.maximize_window()
driver.find_element(By.NAME,'q')

searchbox.send_keys("Selenium")
searchbox_submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
