from django.urls import path
from . import views
app_name = "news"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('posts/page/<int:page>', views.index, name='posts'),
    path('category/<int:category_id>/page/<int:page>/', views.category, name='category'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('search/', views.search, name='search'),
    path('tag/<int:tag_id>/', views.search, name='tag'),
    path('apps/', views.apps, name='apps'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
]
