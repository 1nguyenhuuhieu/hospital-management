from django.shortcuts import render, redirect
from news.models import *
from .forms import *
from human_resource_management.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


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
def edit_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            if 'draft' in (request.POST):
                new_post.status = 'draft'
            if 'send' in (request.POST):
                new_post.status = 'pending'
            new_post.save()
            return redirect('communication:index')

    else:
        post_form = PostForm()
    context = {
        'post_form': post_form
    }

    return render(request, 'communication/edit_post.html', context)