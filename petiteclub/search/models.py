from django.db import models
from members.models import FavList
# from django.contrib.auth.models import User

# laster we moved to favorites Models

# custom user class
# class User(models.Model):
#     fisrt_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     email_address = models.EmailField
    
#     def __str__(self):
#         return self.fisrt_name + " " + self.last_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=10)
    product_url = models.CharField(max_length=300)
    product_img = models.CharField(max_length=300)

    saved_by = models.ManyToManyField(FavList, blank=True)
    # saved_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # List product name on Admin page
    def __str__(self):
        return self.product_name

