from django.db import models
from django.contrib.auth.models import User

# custom user class
# class User(models.Model):
#     fisrt_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     email_address = models.EmailField
    
#     def __str__(self):
#         return self.fisrt_name + " " + self.last_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    ulr = models.CharField(max_length=300)
    img = models.CharField(max_length=300)

    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # saved_by = models.ManyToManyField(User, blank=True)

    # # List product name on Admin page
    # def __str__(self):
    #     return self.name

