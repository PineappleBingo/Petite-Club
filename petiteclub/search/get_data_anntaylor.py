import requests
from bs4 import BeautifulSoup

# keyword = input("Enter Keyword: ")
# keyword = keyword.strip().title()

# url = (
#     "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+"
#     + keyword
#     + "&N=102435"
# )


def get_dress_data(url, keyword):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "lxml")
    products = doc.find_all("li", class_="product")
    
    names = []
    prices = []
    urls = []
    images = []

    for idx, product in enumerate(products):
        name = product.select("strong")[0].string.strip()

        if keyword in name:
            url = product.select("div > a")[0].get("href")
            price = product.select("span.price > span")[0].string
            img = product.find_all("img")[0].get("src")

        names.append(name)
        prices.append(price)
        urls.append(url)
        images.append(img)

        # print(name)
        # print(price)
        # print(url)
        # print(img)

    return names, prices, urls, images

# get_dress_data(url)