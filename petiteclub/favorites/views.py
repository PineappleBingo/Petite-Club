from django.shortcuts import render

# load from search model(db)

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


context = {"products": products}


def favorites(request):
    return render(request, "favorites/favlist.html", context)
