from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from webdriver_manager.chrome import ChromeDriverManager


# Function to extract visible content excluding header and footer, ensuring no duplicates
def extract_visible_content_with_tags(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Find all elements inside <body>, excluding <header>, <footer>, and their child elements
    elements = driver.find_elements(By.XPATH, "//body//*[not(ancestor::header) and not(ancestor::footer)]")

    # Extract tag names and visible text, while avoiding duplicates
    extracted_content = []
    seen_tags = set()  # To track already processed elements

    for element in elements:
        if element.tag_name in ["h1", "h2", "h3", "h4", "p", "li", "input", "button", "a"]:  # Filter tags to include
            # Check if this tag and content has already been processed
            content = element.text.strip()
            if content and (element.tag_name, content) not in seen_tags:  # Avoid duplicates
                extracted_content.append((element.tag_name, content))
                seen_tags.add((element.tag_name, content))  # Mark this tag/content as processed

    return extracted_content

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URLs to compare
Live_URL = "https://www.uniteddirectins.com/home-insurance"  # Replace with your first page URL
Staging_URL = "https://udi.stratospherewebsites.com/home-insurance"  # Replace with your second page URL

# Extract content with tags from both pages
content1 = extract_visible_content_with_tags(driver, Live_URL)
content2 = extract_visible_content_with_tags(driver, Staging_URL)

# Save content to an Excel file
excel_file = r"C:\Users\ashish sinha\Desktop\PythhonTestData\DemoPage.xlsx"
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Comparison"

# Write headers
sheet["A1"] = "Live Page Tag Name"
sheet["B1"] = "Live Page Content"
sheet["C1"] = "Staging Page Tag Name"
sheet["D1"] = "Staging Page Content"

# Find the maximum length between the two contents
max_length = max(len(content1), len(content2))

# Write content for both URLs side by side
for i in range(max_length):
    tag1 = content1[i][0] if i < len(content1) else ""  # Tag from Page 1
    text1 = content1[i][1] if i < len(content1) else ""  # Content from Page 1
    tag2 = content2[i][0] if i < len(content2) else ""  # Tag from Page 2
    text2 = content2[i][1] if i < len(content2) else ""  # Content from Page 2
    sheet.append([tag1, text1, tag2, text2])

# Save the Excel file
workbook.save(excel_file)

# Print success message
print(f"Content with tags has been extracted and saved to {excel_file}")

# Close the driver
driver.quit()
