from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://gmrwebteam.openvio.com/admin/myhistory")
driver.maximize_window()

driver.find_element(By.ID,"uname").send_keys("ashish_Anand@gmrwebteam.com")
driver.find_element(By.ID,"Password").send_keys()

##print(PageTitle1)

#driver.get("https://www.gmrwebteam.com/about-us")
#PageTitle2=driver.title
#print(PageTitle2)

#driver.get("https://www.gmrwebteam.com/rehab-marketing")

#PageTitle3=driver.title
#print(PageTitle3)


