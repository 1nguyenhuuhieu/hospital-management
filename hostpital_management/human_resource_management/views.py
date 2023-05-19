from django.shortcuts import render

# Create your views here.

def index(request):
    context = {

    }

    return render(request, 'hrm/index.html', context)

def profile(request):
    context = {

    }

    return render(request, 'hrm/profile.html', context)