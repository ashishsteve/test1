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


import time

# Set up the ChromeDriver (you can use other WebDrivers as needed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


#def verify_content("https://www.expertins.net/payments/", "Make a Payment Online"):

   # try:
        # Open the URL in the browser
        driver.get("https://www.expertins.net/payments/")

        # Wait for the page to load (you can use WebDriverWait for more complex conditions)
        time.sleep(3)  # Simple wait, replace with better wait strategies for production

        # Check if the content is present on the page
        body_text = driver.page_source

        # Verify if the desired content exists in the page source
        if content_to_verify in body_text:
            print(f"Content '{"Make a Payment Online"}' found on the page.")
        else:
            print(f"Content '{"Make a Payment Online"}' NOT found on the page.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser window
        driver.quit()


if __name__ == "__main__":
    url = "https://www.expertins.net/payments/"  # Replace with the URL of your website
    #content_to_verify = "Make a Payment Online
#"  # Replace with the content you want to verify

 #   verify_content(url, content_to_verify)
