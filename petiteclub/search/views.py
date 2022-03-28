from django.shortcuts import render

context = {"var1": "Hello", "var2": "World"}


def home(request):
    return render(request, "search/home.html", context)
