from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib import messages
from search.models import Product


def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("search-home")
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging. Try again"))
            return redirect("login")

    else:
        return render(request, "authenticate/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect("search-home")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("search-home")
    else:
        form = RegisterUserForm()

    return render(request, "authenticate/register_user.html", {"form": form})


products = [
    {
        "product_name": "Some Dress1",
        "product_price": "$100.00",
        "product_url": "anntalyor.com/some_dress.html",
        "product_img": "anntalyer.com/img/some_dress.jpg",
    },
    {
        "product_name": "Some Dress2",
        "product_price": "$200.00",
        "product_url": "anntalyor.com/some_dress.html",
        "product_img": "anntalyer.com/img/some_dress.jpg",
    },
    {
        "product_name": "Some Dress3",
        "product_price": "$300.00",
        "product_url": "anntalyor.com/some_dress.html",
        "product_img": "anntalyer.com/img/some_dress.jpg",
    },
]

# testing with dummy data
# context = {"products": products}
context = {"products": Product.objects.all()}


# def favorites(request):
#     return render(request, "favorites/favlist.html", context)


def favorites(request):

    # if request.method == "POST":
    return render(request, "favorites/favlist.html", context)
