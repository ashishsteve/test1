from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver= webdriver.Edge(options=options)

driver.get("https://admin-demo.nopcommerce.com/login")

driver.maximize_window()
emailbox=driver.find_element(By.ID,'Email')
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
print("result of text:",emailbox.text)
print("result of get_attribute():",emailbox.get_attribute('value'))

button=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button')

