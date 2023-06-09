from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchQuery,SearchVector, SearchHeadline
from unidecode import unidecode
from django.db.models import Count


def index(request, page=1):
    paginate = None
    posts = Post.objects.filter(status='public').order_by('-created_time')
    paginate = Paginator(posts, 5)
    posts = paginate.page(page)


    # thành viên nổi bật: đăng nhiều bài, bình luận nhiều, xem nhiều
    # bài viết nổi bật bao gồm: bài viết xem nhiều, vừa bình luận, vừa đăng tải --> kèm status(xem nhiều, mới đăng, vừa bình luận)  
    #   
    popular_posts = Post.objects.filter(status='public').order_by('-view_count')[:5]
    popular_author = Author.objects.annotate(count=Count('post__id')).order_by('-count')

    context = {
        'category': category,
        'posts': posts,
        'popular_posts': popular_posts,
        'popular_author': popular_author,
        'paginate': paginate,
        'page': page
    }

    return render(request, 'index.html', context)

def category(request, category_id, page):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(status='public').filter(category=category_id).order_by('-created_time')
    paginate = Paginator(posts, 12)
    posts = paginate.page(page)
    context = {
        'category': category,
        'posts': posts,
        'paginate': paginate,
        'page': page
    }

    return render(request, 'category.html', context)

def author(request, author_id):

    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(status='public').filter(author=author)

    context = {
        'posts': posts,
        'author': author
    }

    return render(request, 'author.html', context)

def post(request, post_id):
    try:
        post = Post.objects.filter(user=request.user).get(pk=post_id)
    except:
        post = Post.objects.filter(status='public').get(pk=post_id)

    reaction_name = f'has_reaction_{post_id}'

    if 'bookmarks' in request.session.keys():
        bookmarks = request.session['bookmarks']
        active_bookmark = post.id in bookmarks
    else:
        bookmarks = []
        active_bookmark = False

    viewed_name = f'has_viewed_{post_id}'
    has_reaction = reaction_name in request.session.keys()

    if request.method == 'POST' and 'like' in request.POST:
        if has_reaction and has_reaction==True:
            del request.session[reaction_name]
            post.like -= 1
        else:
            request.session[reaction_name] = True
            post.like += 1
        post.save()
    
    if request.method == 'POST' and 'bookmark' in request.POST:
        bookmark = int(request.POST['bookmark'])
        if bookmark in bookmarks:
            bookmarks.remove(bookmark)
            active_bookmark = False
        else:
            bookmarks.append(bookmark)
            active_bookmark = True
        request.session['bookmarks'] = bookmarks
    
    if request.method == 'POST' and 'comment' in request.POST:
        comment_text = request.POST['comment_text']
        comment_author = request.POST['comment_author']
        comment = Comment(comment=comment_text, author=comment_author, post=post)
        comment.save()
    
    latest_posts = Post.objects.order_by('-created_time')[:5]

    has_viewed = viewed_name in request.session.keys()
    if not has_viewed:
        try:
            post.view_count += 1
            post.save()
            request.session[viewed_name] = True
        except:
            pass

    post = Post.objects.get(pk=post_id)
    has_reaction = reaction_name in request.session.keys()
    author_liked = sum(post.like for post in Post.objects.filter(author=post.author))

    context = {
        'post': post,
        'latest_posts': latest_posts,
        'has_reaction': has_reaction,
        'author_liked': author_liked,
        'active_bookmark': active_bookmark
    }
    
    return render(request, 'post.html', context)


def search(request, tag_id=None):
    tags = Tag.objects.all()
    tag = None
    q = None
    if request.method == 'GET' and 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # convert q to tiếng việt không dấu
        q_khongdau = unidecode(q)

        #search in content 
        search = SearchQuery(q_khongdau) | SearchQuery(q)
        search_vector = SearchVector("plaintext_content", "title", "description", "category__title")
        
        posts = Post.objects.filter(status='public').annotate(
            search=search_vector).filter(
            search=search
            )
    
    if tag_id:
        tag = get_object_or_404(Tag, pk=tag_id)
        posts = Post.objects.filter(tags=tag)


    context = {
        'posts': posts,
        'q': q,
        'tags': tags,
        'tag': tag
    }
    return render(request, 'search.html', context)

def apps(request):
    context = {

    }

    return render(request, 'apps.html', context)

def bookmarks(request):
    if 'bookmarks' in request.session.keys():
        bookmarks = request.session['bookmarks']
    else:
        bookmarks = []

    posts = Post.objects.filter(status='public').filter(id__in=bookmarks)
    context = {
        'posts': posts
    }

    return render(request, 'bookmarks.html', context)

def book_appointment(request):
    context = {

    }

    return render(request, 'book-appointment.html', context)