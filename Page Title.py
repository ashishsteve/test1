from selenium import webdriver

# Initialize WebDriver (Ensure ChromeDriver is installed)
driver = webdriver.Chrome()

# Open the webpage
driver.get("http://gmrwebteam.com/")  # Replace with your website

# Expected title
expected_title = "Healthcare Digital Marketing Platform | GMR Web Team"

# Get the actual title
actual_title = driver.title

# Print both titles
print(f"Actual Title: {actual_title}")
print(f"Expected Title: {expected_title}")

# Compare titles
if actual_title == expected_title:
    print("✅ Title matches!")
else:
    print("❌ Title does NOT match!")

# Close the browser
driver.quit()

