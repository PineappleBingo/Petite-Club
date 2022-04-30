import requests
from bs4 import BeautifulSoup

# Testing Selenium - access denied
# import time
# from selenium import webdriver
# If we have to run Selenium in headless mode; that is without seeing the graphics interface running use below code
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(
#     executable_path=r"D:/gitproject_lib/petite_club/chromedriver.exe", options=chrome_options
# )

# items_url = "https://www.anntaylor.com/petite-dresses/cata000028"

# driver.get(items_url)
# driver.delete_all_cookies()

# doc = BeautifulSoup(driver.page_source, "lxml")
# print(doc.prettify())
#  -----------------------------------------------------------

# keyword = input("Enter Keyword: ")
# keyword = keyword.strip().title()

# url_ann ="https://www.anntaylor.com/search/searchResults.jsp?question=Petite+"+keyword+"&N=102435"

url_loft = "https://www.loft.com/search/searchResults.jsp?question=Petite+Dresses+"

# ....

# result = requests.get(url_ann)
# doc = BeautifulSoup(result.text, "lxml")

# scrap title of title
# cat_title = doc.find("h1", class_="page-title")
# print(cat_title.string.strip())

# scrap product lists
# products = doc.find_all("li", class_="product")
# print("len:", len(products))
# print(products)

# find product name in the first element of proudct lists
# product_name = products[0].find("strong").string.strip()
# print(product_name)

# # find product link in the first element of proudct lists
# product_link = products[0].find("a", href=True)
# print(product_link["href"])

# # find each product's url and print
# for product in products:
#     url = product.find("a", href=True)
#     print(url["href"])

# # find each product's name and print
# for product in products:
#     print(product.find("strong").string.strip())

# # Select fist element of price
# product_prices = products[0].select("span.price > span")
# print("product_price:", product_prices)

# for product in products:
#     product_price = product.select("span.price > span")[0].string
#     # print(product_price[0].string)
#     print(product_price)

# Find image src in product list
# imgs = products[0].find_all("img")
# for img in imgs:
#     print(img["src"])
# # or
# img = products[0].find_all("img")[0]
# print(img["src"])

# Get dress data from the Site and saved into dict()
# dresses = dict()
# for idx, product in enumerate(products):
#     url = product.select("div > a")[0].get("href")
#     name = product.select("strong")[0].string.strip()
#     price = product.select("span.price > span")[0].string
#     img = product.find_all("img")[0].get("src")

#     dresses[idx] = {"name": name, "url": url, "price": price, "img": img}
#     return print(dresses[idx])

# # print(dresses[0])
# # print(dresses[1])
# # print(dresses[2])
# # print(dresses)
# print("len:", len(dresses))

# def get_dress_ann1(url_ann):

#     result = requests.get(url_ann)
#     doc = BeautifulSoup(result.text, "lxml")
#     products = doc.find_all("li", class_="product")

#     print("products len:", len(products))

#     dresses = dict()
#     for idx, product in enumerate(products):
#         # name = product.select("strong")[0].string.strip()
#         name = product.select("strong")[0].string.strip().lower()

#         if keyword in name:
#             url = product.select("div > a")[0].get("href")
#             price = product.select("span.price > span")[0].string
#             img = product.find_all("img")[0].get("src")

#             dresses[idx] = {"name": name, "url": url, "price": price, "img": img}
#             print(dresses[idx])


# print(dresses[0])
# print(dresses[1])
# print(dresses[2])
# print(dresses)
# print("len:", len(dresses))
# return dresses

# data = get_dress_ann(url)
# print(data)

# get_dress_ann(url)
# print("----------------")
# get_dress_ann1(url)

#  -----------------------------------------------------------
# driver.quit()
#  -----------------------------------------------------------


def get_product_data_ann(search_url, keyword):
    result = requests.get(search_url)
    doc = BeautifulSoup(result.text, "lxml")
    products = doc.find_all("li", class_="product")

    ids = []
    names = []
    prices = []
    urls = []
    images = []

    for idx, product in enumerate(products):
        name = product.select("strong")[0].string.strip().lower()

        if keyword in name:
            id = idx
            url = product.select("div > a")[0].get("href")
            price = product.select("span.price > span")[0].string
            img = product.find_all("img")[0].get("src").replace("\n", "")

            ids.append(id)
            names.append(name)
            prices.append(price)
            urls.append(url)
            images.append(img)

        # print(name)
        # print(price)
        # print(url)
        # print(img)
    return ids, names, prices, urls, images


def get_product_data_loft(search_url, keyword):
    result = requests.get(search_url)
    doc = BeautifulSoup(result.text, "lxml")
    products = doc.find_all("li", class_="product")

    ids = []
    names = []
    prices = []
    urls = []
    images = []

    for idx, product in enumerate(products):
        name = product.select("strong")[0].string.strip().lower()
        # print(name)

        if keyword in name:
            id = idx
            url = product.select("div > a")[0].get("href")
            price = product.select("span.price > span")[0].string
            img = product.find_all("img")[0].get("src").replace("\n", "")

            # print(id, url, price, img)

            ids.append(id)
            names.append(name)
            prices.append(price)
            urls.append(url)
            images.append(img)

        # print(name)
        # print(price)
        # print(url)
        # print(img)

    return ids, names, prices, urls, images


# Test code

search_dresses_urls = {
    "anntaylor": "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+",
    "loft": "https://www.loft.com/search/searchResults.jsp?question=Petite+Dresses+",
}

keyword = "Dotted"
keyword = str(keyword).lower().strip()

for key in search_dresses_urls:
    # appending keyword to search url
    search_dresses_urls[key] = search_dresses_urls[key] + keyword
    print("Key:", key, search_dresses_urls[key])


for site in search_dresses_urls:

    if site == "anntaylor":
        pid, pname, pprice, purl, pimg = get_product_data_ann(
            search_dresses_urls[site], keyword
        )
        print(pid, pname, pprice, purl, pimg)

        data = zip(pid, pname, pprice, purl, pimg)

    elif site == "loft":
        pid, pname, pprice, purl, pimg = get_product_data_loft(
            search_dresses_urls[site], keyword
        )
        print(pid, pname, pprice, purl, pimg)

        data = zip(pid, pname, pprice, purl, pimg)


# print result
# for d in data:
#     print(d)

# >>> a_dict = dict(zip(fields, values))
# >>> a_dict
# {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}
