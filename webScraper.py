from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

URL = "https://www.amazon.ca/Blocking-Passport-Holder-Travel-documents/dp/B07QNVWRQV/ref=zg-bs_luggage_sccl_1/133-6290200-6221365?pd_rd_w=Sg6sG&content-id=amzn1.sym.1b333d54-760c-4345-a197-05d66e42d3ba&pf_rd_p=1b333d54-760c-4345-a197-05d66e42d3ba&pf_rd_r=5GS35ABE7DYWXWDKBCP5&pd_rd_wg=FAeJ9&pd_rd_r=531bf707-1640-4fc7-a962-e641fa79bbf2&pd_rd_i=B07QNVWRQV&psc=1/"
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")

# Outer Tag Object
title = soup.find("span", attrs={"id":'productTitle'})

# Inner NavigableString Object
title_value = title.string

# Title as a string value
title_string = title_value.strip()

# Printing types of values for efficient understanding
print(type(title))
print(type(title_value))
print(type(title_string))
print()

# Printing Product Title
print("Product Title = ", title_string)

price = soup.find('span', class_ = 'a-offscreen')

price_value = price.string

price_string = price_value.strip()

# Function calls to display all necessary product information

print("Product Price =", price_value)

print()
print()