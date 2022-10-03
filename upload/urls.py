from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("mptnd_data/",mptnd_data),
    path("display_data/",display_data)
    
]
