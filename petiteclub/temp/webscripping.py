import requests
from bs4 import BeautifulSoup

url = "https://www.anntaylor.com/petite-dresses/cata000028"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

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

dresses = dict()
for idx, product in enumerate(products):
    url = product.select("div > a")[0].get("href")
    name = product.select("strong")[0].string.strip()
    price = product.select("span.price > span")[0].string

    dresses[idx] = {
                        "name" : name,
                        "url"  : url,
                        "price": price
    }

print(dresses[1])
