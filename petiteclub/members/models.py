from django.db import models
from django.contrib.auth.models import User
# from .models import Profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

# Create your models here.
class FavList(models.Model):
    favlist_name = models.CharField(default="My Favorites", max_length=30)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.favlist_name