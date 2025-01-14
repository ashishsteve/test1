from pip._internal.resolution.resolvelib.factory import C
from selenium import webdriver

# Set up the WebDriver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Enable headless mode
driver = webdriver.Chrome(options=options)

# Navigate to the webpage
driver.get("https://www.fccmg.com/")

# Capture full-page screenshot
screenshot_path = "full_page_screenshot.png"
driver.get_screenshot_as_file(C:\FCCMG)
print(f"Full-page screenshot saved at: {C:\FCCMG}")

# Clean up
driver.quit()
