# Product Data Scraping Project

This project focuses on web scraping to extract product data from e-commerce websites using Python. I employed the `requests` library to make HTTP requests and `BeautifulSoup` for parsing HTML content. The project is designed to fetch product information in a structured format, making it easier to analyze and utilize for various applications.

## Project Overview

The script retrieves product data from a specified URL, extracting information from both JSON-LD and meta tags to ensure comprehensive data capture. It supports flexibility in data extraction, adapting to the structure of the webpage.

## Libraries Used

- **Requests**: For sending HTTP requests to fetch webpage content.
- **BeautifulSoup**: For parsing HTML and extracting data.
- **JSON**: For handling JSON data formats.

## Functionality

### Key Functions

1. **`fetch_product_data_from_jsonld(soup)`**: 
   - Extracts product information from JSON-LD structured data if available on the webpage.
   - Handles both lists and dictionaries for offers to fetch the product price.

2. **`fetch_product_data_from_meta(soup)`**:
   - Retrieves product data from meta tags if JSON-LD data is not present.
   - Collects product name, price, URL, image URL, and description.

3. **`fetch_product_data(url)`**:
   - The main function that orchestrates the web scraping process.
   - Sends a GET request to the specified URL and processes the response to extract product data.

### Usage

To use the project:

1. Ensure you have Python installed along with the required libraries. You can install them using:

   ```bash
   pip install requests beautifulsoup4
   ```

2. Replace the placeholder `product_url_here` in the script with the actual URL of the product you want to scrape.

3. Run the script in your Python environment. The extracted product data will be printed in JSON format.

## Conclusion

This project allowed me to efficiently scrape product data from web pages, facilitating data collection for analysis or further application development.
