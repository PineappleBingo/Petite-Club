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

            for key in search_dresses_urls:
                # appending keyword to search url
                search_dresses_urls[key] = search_dresses_urls[key] + keyword

            for site in search_dresses_urls:
                if site == "anntaylor":
                    pid, pname, pprice, purl, pimg = get_product_data_ann(
                        search_dresses_urls[site], keyword
                    )
                    data = zip(pid, pname, pprice, purl, pimg)

                elif site == "loft":
                    pid, pname, pprice, purl, pimg = get_product_data_loft(
                        search_dresses_urls[site], keyword
                    )
                    data = zip(pid, pname, pprice, purl, pimg)

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

        # pid, pname, pprice, purl, pimg = get_product_data(url, keyword)
        # data = zip(pid, pname, pprice, purl, pimg)

        if len(pname) > 0:
            context = {"data": data}
        else:
            context = {"message": "No Matching Results Found"}

        # context = {"pid": pid, pname": pname, "pprice": pprice, "purl": purl, "pimg": pimg}
        return render(request, "search/home.html", context)

    return render(request, "search/home.html")
