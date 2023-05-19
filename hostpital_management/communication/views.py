from django.shortcuts import render, redirect
from news.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.


def staff_check(user):
    try:
        staff = user.staff
        return True
    except:
        return False

@user_passes_test(staff_check)
@login_required
def index(request):
    context = {

    }

    return render(request, 'communication/index.html', context)


@login_required
def new_post(request):
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

    return render(request, 'communication/new_post.html', context)