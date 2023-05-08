from django.urls import path
from . import views
app_name = "news"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('posts/page/<int:page>', views.index, name='posts'),
    path('category/<int:category_id>/page/<int:page>/', views.category, name='category'),
    path('posts/<int:tag_id>/', views.posts, name='posts_tag'),
    path('search/', views.search, name='search'),
    path('apps/', views.apps, name='apps')
]
