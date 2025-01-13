from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v129.fed_cm import click_dialog_button


options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

API_KEY = "your_2captcha_api_key"

def solve_captcha(site_key, "https://www.facebook.com/"):
    # Request CAPTCHA solving
    response = requests.post(
        f"http://2captcha.com/in.php",
        data={
            "key": API_KEY,
            "method": "userrecaptcha",
            "googlekey": site_key,
            "pageurl": "https://www.facebook.com/",
            "json": 1,
        }
    ).json()
    request_id = response["request"]

    # Poll for the solution
    while True:
        result = requests.get(
            f"http://2captcha.com/res.php?key={API_KEY}&action=get&id={request_id}&json=1"
        ).json()
        if result["status"] == 1:
            return result["request"]

driver = webdriver.Chrome()
url = "https://www.facebook.com/"
driver.get("https://www.facebook.com/")

# Extract site_key from the CAPTCHA element
site_key = driver.find_element(By.CSS_SELECTOR, "captcha-selector").get_attribute("data-sitekey")

# Solve CAPTCHA
solution = solve_captcha(site_key, "https://www.facebook.com/")

# Enter CAPTCHA solution
driver.execute_script(
    "document.getElementById('g-recaptcha-response').innerHTML = arguments[0];", solution
)
driver.find_element(By.ID, "submit-button").click()

