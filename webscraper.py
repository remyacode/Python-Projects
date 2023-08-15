import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the Selenium webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)

base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'

# Create or open a CSV file for writing
with open('amazon_product_details.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews', 
                         'Description', 'ASIN', 'Product Description', 'Manufacturer'])  # Write the header

    # Loop through the desired number of listing pages
    for page_number in range(1, 21):  # Scraping for 20 pages
        url = base_url.format(page_number)
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})

        # Loop through products on the current listing page
        for product in products:
            product_url = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal'})['href']
            product_name = product.find('span', {'class': 'a-text-normal'}).get_text(strip=True)
            product_price = product.find('span', {'class': 'a-price-whole'}).get_text(strip=True)
            rating = product.find('span', {'class': 'a-icon-alt'}).get_text(strip=True)
            num_reviews = product.find('span', {'class': 'a-size-base'}).get_text(strip=True)

            # Open the product URL using Selenium
            driver.get(product_url)
            time.sleep(2)  # Wait for the page to load

            product_soup = BeautifulSoup(driver.page_source, 'html.parser')

            try:
                description = product_soup.find('meta', {'name': 'description'})['content']
            except TypeError:
                description = 'N/A'

            try:
                asin = product_soup.find('th', string='ASIN').find_next('td').get_text(strip=True)
            except AttributeError:
                asin = 'N/A'

            try:
                product_description = product_soup.find('div', {'id': 'productDescription'}).get_text(strip=True)
            except AttributeError:
                product_description = 'N/A'

            try:
                manufacturer = product_soup.find('a', {'id': 'bylineInfo'}).get_text(strip=True)
            except AttributeError:
                manufacturer = 'N/A'

            # Write the extracted details to the CSV file
            csv_writer.writerow([product_url, product_name, product_price, rating, num_reviews, 
                                 description, asin, product_description, manufacturer])

            # Add a delay to avoid overloading the website's servers
            time.sleep(2)  # Adjust the delay time if needed

# Close the Selenium webdriver
driver.quit()
