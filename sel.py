from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from bs4 import BeautifulSoup
import json

# Set Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode (optional)

# Set path to the ChromeDriver executable
chrome_driver_path = "/usr/local/bin/chromedriver"

# Create a Chrome service object
service = Service(chrome_driver_path)

# Start the Chrome driver
driver = Chrome(service=service, options=chrome_options)

# Open a webpage
# driver.get("https://www.fool.com/quote/nasdaq/aapl")
driver.get('https://www.tradingview.com/markets/indices/quotes-all/')

data = []

def close_popup():
    try:
        popup_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Close"]')
        popup_button.click()
    except NoSuchElementException:
        pass

try:
    while True:

        # close_popup()

        # Wait for the table rows to be present
        etfs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr.row-RdUXZpkv'))
        )
        
        # Extract data from each row

        # print(etfs)
        for row in etfs:
            tds = row.find_elements(By.TAG_NAME, 'td')
            print('TD Length: ', len(tds))
            if len(tds) > 4:
                # ticker = tds[0].span.a.text
                name = tds[0].text
                # coupon = tds[1].text
                # yld = tds[2].text
                # maturity_date = tds[3].text
                
                data.append({
                    # "Ticker": ticker,
                    "Name": name
                    # "Sector": coupon,
                    # "Yield": yld,
                    # "Maturity Date": maturity_date
                })  
                print('Appended Data')
        
        # Try to find and click the "Next" button
        # next_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Next"]'))
        # )

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-overflow-tooltip-text="Load More "]'))
        )
        
        try:
            # Click the "Next" button to load the next page of results
            next_button.click()
        except ElementClickInterceptedException:
            close_popup()
            next_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver
    driver.quit()

    # Save the collected data to a JSON file
    with open('indices.json', 'w') as f:
        json.dump(data, f)

    print("Data saved to indices.json")

# transcript_links = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr.svelte-1yyv6eq'))
# )
# for link in transcript_links:
#     print(link.text)

# # Quit the driver
# driver.quit()



