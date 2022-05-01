from types import NoneType
import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from .web_scraping import get_product_data_ann
from .web_scraping import get_product_data_loft

# context = {"var1": "Hello", "var2": "World"}
# def home(request):
#     return render(request, "search/home.html", context)

search_dresses_urls = {
    "anntaylor": "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+",
    "loft": "https://www.loft.com/search/searchResults.jsp?question=Petite+Dresses+",
}
search_pants_urls = {
    "anntaylor": "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+",
    "loft": "https://www.loft.com/search/searchResults.jsp?question=Petite+Dresses+",
}
search_skirts_urls = {
    "anntaylor": "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+",
    "loft": "https://www.loft.com/search/searchResults.jsp?question=Petite+Dresses+",
}
search_suits_urls = {
    "anntaylor": "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+",
    "loft": "https://www.loft.com/search/searchResults.jsp?question=Petite+Dresses+",
}
search_jackets_urls = {
    "anntaylor": "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+",
    "loft": "https://www.loft.com/search/searchResults.jsp?question=Petite+Dresses+",
}


def home(request):

    if request.method == "POST":
        keyword = request.POST["keyword"]
        keyword = keyword.strip().title()
        category_list = request.POST["category_list"]

        if category_list == "Dresses":

            p_id = []
            p_name = []
            p_price = []
            p_url = []
            p_img = []

            for key in search_dresses_urls:
                # appending keyword to search url
                search_dresses_urls[key] = search_dresses_urls[key] + keyword

            for site in search_dresses_urls:
                if site == "anntaylor":
                    pid, pname, pprice, purl, pimg = get_product_data_ann(
                        search_dresses_urls[site], keyword
                    )
                    #  [[],[],[], ...]
                    p_id.append(pid)
                    p_name.append(pname)
                    p_price.append(pprice)
                    p_url.append(purl)
                    p_img.append(pimg)

                elif site == "loft":
                    pid, pname, pprice, purl, pimg = get_product_data_loft(
                        search_dresses_urls[site], keyword
                    )
                    #  [[],[],[], ...]
                    p_id.append(pid)
                    p_name.append(pname)
                    p_price.append(pprice)
                    p_url.append(purl)
                    p_img.append(pimg)

            # Flattening Lists
            fp_id = [item for sublist in p_id for item in sublist]
            fp_name = [item for sublist in p_name for item in sublist]
            fp_price = [item for sublist in p_price for item in sublist]
            fp_url = [item for sublist in p_url for item in sublist]
            fp_img = [item for sublist in p_img for item in sublist]

            data = zip(fp_id, fp_name, fp_price, fp_url, fp_img)

        # add code here for other categories

        if len(fp_name) > 0:
            context = {"data": data}
        else:
            context = {"message": "No Matching Results Found"}

        return render(request, "search/home.html", context)

    return render(request, "search/home.html")

    #     url = (
    #             "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+" + keyword
    #     )
    # elif category_list == "Pants":
    #     url = (
    #         "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Pants+"
    #         + keyword
    #     )
    # elif category_list == "Skirts":
    #     url = (
    #         "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Skirts+"
    #         + keyword
    #     )
    # elif category_list == "Suits":
    #     url = (
    #         "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Suits+"
    #         + keyword
    #     )
    # elif category_list == "Jackets":
    #     url = (
    #         "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Jackets+and+Blazers+"
    #         + keyword
    #     )
