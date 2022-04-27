import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from .get_data_anntaylor import get_dress_data

# context = {"var1": "Hello", "var2": "World"}

# def home(request):
#     return render(request, "search/home.html", context)

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

        pname, pprice, purl, pimg = get_dress_data(url, keyword)
        data = zip(pname, pprice, purl, pimg)

        if len(pname) > 0: 
            context = {"data": data}
        else:
            context = {"message": "No Matching Results Found"}

        # context = {"pname": pname, "pprice": pprice, "purl": purl, "pimg": pimg}
        return render(request, "search/home.html", context)

    return render(request, "search/home.html")
