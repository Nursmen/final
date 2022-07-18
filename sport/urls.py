from .views import *
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', index, name='index'),
    path('list/<int:day>/<str:program>', list, name='list'),
    path('days/<str:title>', days, name='days'),

    path('done/<int:day>/<str:program>', add, name='add'),
    path('clean/', clean),
]