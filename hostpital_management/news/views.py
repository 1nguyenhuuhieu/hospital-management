from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
import random

def index(request):
    
    latest_post = Post.objects.filter(is_public=True).latest('created_time')
    latest_posts = Post.objects.all().exclude(id=latest_post.id).order_by('-created_time')[:4]
    try:
        home_post2 = Post.objects.filter(tags=1).latest('created_time')
    except:
        home_post2 = None
    try:
        home_post3 = Post.objects.filter(tags=1).latest('created_time')
    except:
        home_post3 = None
    author_liked = sum(post.like for post in Post.objects.filter(author=home_post2.author))
    author2_liked = sum(post.like for post in Post.objects.filter(author=home_post3.author))

    context = {
        'latest_posts': latest_posts,
        'latest_post': latest_post,
        'home_post2': home_post2,
        'author_liked': author_liked,
        'home_post3': home_post3,
        'author2_liked': author2_liked
    }

    return render(request, 'index.html', context)

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    reaction_name = f'has_reaction_{post_id}'
    has_reaction = reaction_name in request.session.keys()

    if request.method == 'POST' and 'like' in request.POST:
        if has_reaction and has_reaction==True:
            del request.session[reaction_name]
            post.like -= 1
        else:
            request.session[reaction_name] = True
            post.like += 1
        post.save()
    
    if request.method == 'POST' and 'comment' in request.POST:
        comment_text = request.POST['comment_text']
        comment_author = request.POST['comment_author']
        comment = Comment(comment=comment_text, author=comment_author, post=post)
        comment.save()
    
    latest_posts = Post.objects.order_by('-created_time')[:5]
    try:
        post.view_count += 1
        post.save()
    except:
        pass

    post = Post.objects.get(pk=post_id)
    has_reaction = reaction_name in request.session.keys()
    author_liked = sum(post.like for post in Post.objects.filter(author=post.author))

    context = {
        'post': post,
        'latest_posts': latest_posts,
        'has_reaction': has_reaction,
        'author_liked': author_liked
    }
    
    return render(request, 'post.html', context)

def posts(request, tag_id=None):
    page=1
    if request.method == 'GET' and 'page' in request.GET:
        page = request.GET['page']

    if tag_id:
        posts = Post.objects.filter(tags=tag_id).order_by('-created_time')
        tag = get_object_or_404(Tag, pk=tag_id)
        tag_title = tag.title
        tag_list = Tag.objects.filter(parrent_tag=tag)
    else:
        posts = Post.objects.all().order_by('-created_time')
        tag_title = 'Tất cả bài viết'
        tag_list = Tag.objects.all()
    top_view_posts =  posts.order_by('-view_count')[:5]
    objects = posts
    p = Paginator(objects, 4)
    current_page = p.page(page)
    list_object = p.page(page).object_list
    context = {
        'p': p,
        'list_object': list_object,
        'current_page': current_page,
        'tag_id': tag_id,
        'tag_title': tag_title,
        'tag_list': tag_list ,
        'top_view_posts': top_view_posts,
        'posts': posts
    }
    return render(request, 'posts.html', context)
