from django.urls import path
from . import views
app_name = "news"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:tag_id>', views.posts, name='posts'),
]
