from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    context = {

    }

    return render(request, 'hrm/index.html', context)


@login_required
def profile(request):
    context = {

    }

    return render(request, 'hrm/profile.html', context)