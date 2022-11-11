from django.contrib import admin
from django.urls import path
from sparta import views

urlpatterns = [
    path("",views.index),
    path("about/",views.About),
    path("Contact/",views.contact),
    path("Services/",views.Services),



]