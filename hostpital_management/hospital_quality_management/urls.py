from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluation-criteria', views.evaluation_criteria, name='evaluation_criteria'),
]
