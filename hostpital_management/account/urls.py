from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('', views.register, name='register'),
    path('email', views.register_email, name='register_email'),
]
