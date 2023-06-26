from django.urls import path

from . import views

app_name = "hqm"

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluation-criteria', views.evaluation_criteria, name='evaluation_criteria'),
]
