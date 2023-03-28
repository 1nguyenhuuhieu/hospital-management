from django.urls import path

from . import views

urlpattenrs = [
    path('', views.index, name='index'),
]