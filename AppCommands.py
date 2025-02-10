from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (Ensure ChromeDriver is installed and in PATH)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.gmrwebteam.com/contact-us")  # Replace with your target URL

# Expected values (Update these based on your website)
expected_title = "Contact Us"
expected_description = "Contact us to find how we can help you expand your healthcare business with our result-driven marketing &amp;amp; advertising solution. We will be happy to meet you!"
expected_keywords = "Healthcare Marketing Services"

# Fetch the actual title
actual_title = driver.title

# Function to get meta tag content
def get_meta_content(name):
    try:
        return driver.find_element(By.XPATH, f"//meta[@name='{name}']").get_attribute("content")
    except:
        return None  # Return None if the meta tag is not found

# Fetch actual meta description and keywords
actual_description = get_meta_content("description")
actual_keywords = get_meta_content("keywords")

# Print actual vs expected values
print(f"Actual Title: {actual_title}")
print(f"Expected Title: {expected_title}")

print(f"Actual Description: {actual_description}")
print(f"Expected Description: {expected_description}")

print(f"Actual Keywords: {actual_keywords}")
print(f"Expected Keywords: {expected_keywords}")

# Compare title
if actual_title == expected_title:
    print("✅ Title matches!")
else:
    print("❌ Title does NOT match!")

# Compare description
if actual_description and actual_description == expected_description:
    print("✅ Description matches!")
else:
    print("❌ Description does NOT match!")

# Compare keywords
if actual_keywords and actual_keywords == expected_keywords:
    print("✅ Keywords match!")
else:
    print("❌ Keywords do NOT match!")

# Close the browser
driver.quit()
