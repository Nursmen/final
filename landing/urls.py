from .views import *
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', index, name='index'),
]