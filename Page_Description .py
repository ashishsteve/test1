from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (Ensure ChromeDriver is installed)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.gmrwebteam.com/")  # Replace with your target URL

# Expected meta description (update this based on your site)
expected_description = "We are a complete healthcare digital marketing platform to help you grow revenue, patient acquisition, enhance online reputation, improve operations, and engage more patients with our technology."

try:
    # Locate the meta description tag
    meta_description = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")

    # Print actual and expected descriptions
    print(f"Actual Description: {meta_description}")
    print(f"Expected Description: {expected_description}")

    # Compare descriptions
    if meta_description == expected_description:
        print("✅ Description matches!")
    else:
        print("❌ Description does NOT match!")

except Exception as e:
    print("❌ Meta description not found!", str(e))

# Close the browser
driver.quit()
