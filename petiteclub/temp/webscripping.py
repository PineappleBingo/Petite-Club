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

product_prices = products[0].find("span", class_="price").contents
print("product_price:", product_prices)

for product_price in product_prices:
    # print(product_price)
    # print("--------------------")
    print(product_price.select())


# for product in products:
#     # product_ = product.find("span", class_="price").children
#     product_ = product.find("span", class_="price").descendants
#     print(product_)
#     # product_1 = list(product_)
#     # print(product_1)
#     # # print(product_1[3])


# dresses = dict()

# for product in products:
#     url = product.find("a", href=True)
#     name = product.find("strong").string.strip()

#     dresses[name] = url["href"]

# # print(dresses)
# # print("len:", len(dresses))
