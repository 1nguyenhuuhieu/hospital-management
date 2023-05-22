from django.urls import path

from . import views

app_name = "communication"

urlpatterns = [
    path('', views.index, name='index'),
    path('edit-post/', views.edit_post, name='edit_post'),
    path('edit-post/<int:post_id>/', views.edit_post, name='edit_post'),
]
