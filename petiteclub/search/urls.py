from django.urls import path
from search.views import search
from . import views

urlpatterns = [
    path("", views.search, name="search"),
]