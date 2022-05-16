from django.urls import path
from search.views import home
from . import views

urlpatterns = [
     path("", home, name="home"),    
]