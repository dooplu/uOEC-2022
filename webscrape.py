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






if __name__ == '__main__':
    # Headers for request
    HEADERS = ({'User-Agent':
                    'Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL = "https://www.amazon.com/Flask-Narrow-Mouth-Sports-Bottle/dp/B082H6MLKP/ref=sr_1_4_sspa?keywords=water%2Bbottles&qid=1668884014&sprefix=water%2Caps%2C76&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # Function calls to display all necessary product information
    print("Product Title =", get_title(soup))
    print("Product Price =", get_price(soup))

    print()
    print()