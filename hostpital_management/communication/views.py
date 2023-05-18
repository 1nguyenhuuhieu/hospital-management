from django.shortcuts import render
from news.models import *
from .forms import *
# Create your views here.

def index(request):
    context = {

    }

    return render(request, 'communication/index.html', context)

def new_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
    else:
        post_form = PostForm()
    context = {
        'post_form': post_form
    }

    return render(request, 'communication/new_post.html', context)