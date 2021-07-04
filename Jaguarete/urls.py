""" Jaguarete URL Configuration urls """
from django.contrib import admin
from django.urls import path

import eCommerce.views

urlpatterns = [
    path('', eCommerce.views.index),
    path('about', eCommerce.views.about),
    path('admin/', admin.site.urls),
]
