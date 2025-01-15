from pip._internal.resolution.resolvelib.factory import C
from selenium import webdriver

# Set up the WebDriver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Enable headless mode
driver = webdriver.Chrome(options=options)


#options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)


driver.get("https://www.mypinnaclehealthcare.com/")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
