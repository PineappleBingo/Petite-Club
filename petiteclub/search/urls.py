from django.urls import path
from search.views import home
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("", home, name="home"),
]