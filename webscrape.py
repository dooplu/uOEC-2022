from bs4 import BeautifulSoup
import requests


# Function to extract Product Title
def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", class_='a-offscreen').string.strip()

    except AttributeError:
        price = ""

    return price

def get_weight(soup):
    try:
        weight = soup.find("span", class_='a-size-base prodDetAttrValue').string.strip()

    except AttributeError:
        weight = ""

    return weight




if __name__ == '__main__':
    # Headers for request
    HEADERS = ({'User-Agent':
                    'Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL = "https://www.amazon.com/Callaway-Driver-Ventus-Regular-Degrees/dp/B09RB45J8K/ref=sr_1_13?crid=1490WB2GFOO09&keywords=50%2Bgrams&qid=1668884457&sprefix=50%2Bgram%2Caps%2C85&sr=8-13&th=1"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # Function calls to display all necessary product information
    print("Product Title =", get_title(soup))
    print("Product Price =", get_price(soup))
    print("Product Weight =", get_weight(soup))

    print()
    print()