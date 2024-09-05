import requests
from bs4 import BeautifulSoup
import json

# Function to fetch product data from JSON-LD
def fetch_product_data_from_jsonld(soup):
    jsonld_script = soup.find('script', type='application/ld+json')
    if not jsonld_script:
        return None

    try:
        jsonld_data = json.loads(jsonld_script.string)
    except json.JSONDecodeError:
        return None

    if isinstance(jsonld_data, list):
        product_data = next((item for item in jsonld_data if item.get('@type') == 'Product'), None)
        if not product_data:
            return None
    elif isinstance(jsonld_data, dict) and jsonld_data.get('@type') == 'Product':
        product_data = jsonld_data
    else:
        return None

    # Handling offers which could be a list or a dictionary
    offers = product_data.get('offers')
    if isinstance(offers, list):
        product_price = next((offer.get('price') for offer in offers if offer.get('price')), '')
    elif isinstance(offers, dict):
        product_price = offers.get('price', '')
    else:
        product_price = ''

    extracted_data = {
        "product_name": product_data.get('name', ''),
        "product_price": product_price,
        "product_url": product_data.get('url', ''),
        "product_image_url": product_data.get('image', ''),
        "product_description": product_data.get('description', '')
    }

    return extracted_data

# Function to fetch product data from meta tags
def fetch_product_data_from_meta(soup):
    product_name = soup.find('meta', attrs={'property': 'og:title'}) or soup.find('meta', attrs={'name': 'twitter:title'})
    product_price = soup.find('meta', attrs={'property': 'product:price:amount'}) or soup.find('meta', attrs={'name': 'price'})
    product_url = soup.find('meta', attrs={'property': 'og:url'}) or soup.find('meta', attrs={'name': 'twitter:url'})
    product_image_url = soup.find('meta', attrs={'property': 'og:image'}) or soup.find('meta', attrs={'name': 'twitter:image'})
    product_description = soup.find('meta', attrs={'property': 'og:description'}) or soup.find('meta', attrs={'name': 'twitter:description'})

    extracted_data = {
        "product_name": product_name['content'] if product_name else '',
        "product_price": product_price['content'] if product_price else '',
        "product_url": product_url['content'] if product_url else '',
        "product_image_url": product_image_url['content'] if product_image_url else '',
        "product_description": product_description['content'] if product_description else ''
    }

    return extracted_data

# Function to fetch product data from a webpage
def fetch_product_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Try to fetch product data from JSON-LD
    product_data = fetch_product_data_from_jsonld(soup)
    if product_data:
        return product_data

    # If JSON-LD is not available, fetch product data from meta tags
    return fetch_product_data_from_meta(soup)

# URL of the product page
product_url = "https://www.hiketron.com/collections/scent-free-laundry-detergents/products/clear-powerful-laundry-detergent"

# Fetch product data
product_data = fetch_product_data(product_url)

if product_data:
    print(json.dumps(product_data, indent=4))
else:
    print("No product data found.")
