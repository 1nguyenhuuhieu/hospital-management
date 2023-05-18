from django.urls import path

from . import views

app_name = "communication"

urlpatterns = [
    path('', views.index, name='index'),
    path('new-post/', views.new_post, name='new_post'),
]
