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

url = "https://www.anntaylor.com/petite-dresses/cata000028"

result = requests.get(url)
doc = BeautifulSoup(result.text, "lxml")

# scrap title of title
cat_title = doc.find("h1", class_="page-title")
print(cat_title.string.strip())

# scrap product lists
products = doc.find_all("li", class_="product")
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

dresses = dict()
for idx, product in enumerate(products):
    url = product.select("div > a")[0].get("href")
    name = product.select("strong")[0].string.strip()
    price = product.select("span.price > span")[0].string
    img = product.find_all("img")[0].get("src")

    dresses[idx] = {"name": name, "url": url, "price": price, "img": img}

print(dresses[0])
print(dresses[1])
print(dresses[2])
# print(dresses)
print("len:", len(dresses))



#  -----------------------------------------------------------
# driver.quit()
#  -----------------------------------------------------------
