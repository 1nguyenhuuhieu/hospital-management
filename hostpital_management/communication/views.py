from django.shortcuts import render, redirect
from news.models import *
from .forms import *
from human_resource_management.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404


# Create your views here.


def communication_check(user):
    try:
        staffteam = StaffTeam.objects.get(staff__user=user)
        return True
    except:
        return False

@user_passes_test(communication_check)
def index(request):

    my_posts = Post.objects.filter(user=request.user).order_by('-created_time')[:5]
    context = {
        'my_posts': my_posts
    }

    return render(request, 'communication/index.html', context)


@user_passes_test(communication_check)
def edit_post(request, post_id=None):

    if post_id:
        post = get_object_or_404(Post, pk=post_id)
        post_form = PostForm(instance=post)
    else:
        post_form = PostForm()
    if request.method == 'POST':
        if post_id:
            post_form = PostForm(request.POST, request.FILES, instance=post)
        else:
            post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            try:
                author = Author.objects.get(user=request.user)
            except:
                author = Author(user=request.user)
                author.save()
            new_post.author = author
            if 'draft' in (request.POST):
                new_post.status = 'draft'
            if 'send' in (request.POST):
                new_post.status = 'pending'
            new_post.save()
            return redirect('communication:index')

        
    context = {
        'post_form': post_form
    }

    return render(request, 'communication/edit_post.html', context)