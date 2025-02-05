from pip._internal.resolution.resolvelib.factory import C
from selenium import webdriver


# Set up the WebDriver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Enable headless mode
driver = webdriver.Chrome(options=options)

from selenium import webdriver

from selenium import webdriver

from selenium import webdriver

# Set up Chrome WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH

# Open the website
driver.get("https://parkwestgc.com/philanthropy")

# Get the full page text (excluding HTML tags)
page_text = driver.find_element("tag name", "body").text  # Extract visible text

# Define the word to search for
search_word = "Parkwest"

# Count occurrences of the word (case-insensitive)
word_count = page_text.lower().count(search_word.lower())

# Display the result
if word_count > 0:
    print(f'Word "{search_word}" found {word_count} times on the page!')
else:
    print(f'Word "{search_word}" NOT found on the page.')

# Close the browser
driver.quit()

