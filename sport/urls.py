from venv import create
from .views import *
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', index, name='index'),
    path('list/<int:day>/<str:program>', list, name='list'),
    path('days/<str:title>', days, name='days'),

    path('done/<int:day>/<str:program>', add, name='add'),
    path('clean/', clean),
    path('create/', create_choise, name='create'),
    path('create/exercise', create_element, name='cr_exercise'),
    path('create/program', create_program, name='cr_program'),
    path('create/day', create_day, name='cr_day')
]