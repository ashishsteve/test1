from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time


def get_meta_data(driver):
    """
    Extract title, keywords, and description from the current page.
    """
    try:
        title = driver.title.strip()
    except:
        title = "N/A"

    try:
        keywords = driver.find_element(By.XPATH, "//meta[@name='keywords']").get_attribute("content").strip()
    except:
        keywords = "N/A"

    try:
        description = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content").strip()
    except:
        description = "N/A"

    return {"Title": title, "Keywords": keywords, "Description": description}


def extract_links(driver, base_url):
    """
    Extract all unique links from the homepage.
    """
    links = set()
    try:
        anchor_tags = driver.find_elements(By.TAG_NAME, "a")
        for anchor in anchor_tags:
            href = anchor.get_attribute("href")
            if href and href.startswith(base_url):
                links.add(href)
    except Exception as e:
        print(f"Error extracting links: {e}")
    return links


def save_to_excel(data, file_name):
    """
    Save data to an Excel file using openpyxl.
    """
    # Create a new workbook
    workbook = Workbook()
    sheet = workbook.active  # Get the active worksheet
    sheet.title = "Meta Data"

    # Write headers
    headers = ["URL", "Title", "Keywords", "Description"]
    sheet.append(headers)

    # Write data rows
    for row in data:
        sheet.append([row["URL"], row["Title"], row["Keywords"], row["Description"]])

    # Save the workbook to a local file
    workbook.save(file_name)
    print(f"Meta data has been saved to '{file_name}'.")


def main():
    # Setup WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    # Start with the homepage URL
    base_url = "https://udi.stratospherewebsites.com/"  # Replace with your homepage URL
    driver.get(base_url)
    time.sleep(3)  # Wait for the homepage to load

    # Extract links from the homepage
    links = extract_links(driver, base_url)
    print(f"Found {len(links)} links to visit.")

    # Collect meta data for each page
    all_meta_data = []
    for link in links:
        try:
            driver.get(link)


            time.sleep(2)  # Allow the page to load
            meta_data = get_meta_data(driver)
            meta_data["URL"] = link
            all_meta_data.append(meta_data)
        except Exception as e:
            print(f"Error visiting {link}: {e}")

    # Save results to an Excel file
    save_to_excel(all_meta_data, r"C:\Users\Vikash Jha\Desktop\PythonTestReportFile\TitleTest.xlsx")

    driver.quit()


if __name__ == "__main__":
    main()