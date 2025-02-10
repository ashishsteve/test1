from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Define the start URL (Change this to your target website)
start_url = "https://www.gmrwebteam.com/"

# Set to store visited pages
visited_urls = set()


def get_all_links():
    """Extract all internal links from the current page."""
    links = set()
    elements = driver.find_elements(By.TAG_NAME, "a")  # Get all <a> elements
    for elem in elements:
        link = elem.get_attribute("href")
        if link and link.startswith(start_url):  # Follow only internal links
            links.add(link)
    return links


def crawl_website(url):
    """Recursively visit all pages and count them."""
    if url in visited_urls:
        return
    visited_urls.add(url)

    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load
        links = get_all_links()  # Get links from the page

        # Recursively visit new links
        for link in links:
            if link not in visited_urls:
                crawl_website(link)

    except Exception as e:
        print(f"Could not access {url}: {e}")


# Start crawling the website
crawl_website(start_url)

# Print the total number of website pages
print(f"\nTotal number of website pages: {len(visited_urls)}")

# Close browser
driver.quit()
