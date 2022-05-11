from django.urls import path
from . import views
# from search.views import home

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.search, name="search-home"),
]