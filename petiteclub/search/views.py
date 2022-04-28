import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from .web_scraping import get_product_data

# context = {"var1": "Hello", "var2": "World"}
# def home(request):
#     return render(request, "search/home.html", context)

search_dresses_urls = []
search_pants_urls = []
search_skirts_urls = []
search_suits_urls = []
search_jackets_urls = []


def home(request):

    if request.method == "POST":
        keyword = request.POST["keyword"]
        keyword = keyword.strip().title()
        category_list = request.POST["category_list"]

        if category_list == "Dress":
            url = (
                "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Dresses+"
                + keyword
                + "&N=102429"
            )
        elif category_list == "Pants":
            url = (
                "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Pants+"
                + keyword
                + "&N=102429"
            )
        elif category_list == "Skirts":
            url = (
                "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Skirts+"
                + keyword
                + "&N=102429"
            )
        elif category_list == "Suits":
            url = (
                "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Suits+"
                + keyword
                + "&N=102429"
            )
        elif category_list == "Jackets":
            url = (
                "https://www.anntaylor.com/search/searchResults.jsp?question=Petite+Jackets+and+Blazers+"
                + keyword
                + "&N=102429"
            )

        pid, pname, pprice, purl, pimg = get_product_data(url, keyword)
        data = zip(pid, pname, pprice, purl, pimg)

        if len(pname) > 0: 
            context = {"data": data}
        else:
            context = {"message": "No Matching Results Found"}

        # context = {"pid": pid, pname": pname, "pprice": pprice, "purl": purl, "pimg": pimg}
        return render(request, "search/home.html", context)

    return render(request, "search/home.html")
